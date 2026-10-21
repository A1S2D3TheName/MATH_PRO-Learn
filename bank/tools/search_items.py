#!/usr/bin/env python3
"""Поиск по единицам учебного материала в двух деревьях репозитория.

    python bank/tools/search_items.py "quadratic formula discriminant"
    python bank/tools/search_items.py "производная" -k 5
    python bank/tools/search_items.py "place value" --kind lesson --source openstax-prealgebra
    python bank/tools/search_items.py --id math-prm800k:math-500-1
    python bank/tools/search_items.py --scope all "logic table"
    python bank/tools/search_items.py --index "percentages"     # только оглавления
    python bank/tools/search_items.py --metadata-only "matrix" # только мета-записи

Области поиска (`--scope`):

  education  (по умолчанию) — math_repo_education/sources/*/items/*.jsonl
  core                      — sources/*/items/*.jsonl (базовое дерево MATH_PRO)
  all                      — оба дерева

Флаг `--index` включает записи-указатели (metadata_only: true) — оглавления
источников с неясной лицензией, где опубликован только индекс. По умолчанию
такие записи в выдаче НЕ участвуют: иначе поиск выглядит так, будто в базе
есть условия задач, которых на самом деле нет. `--metadata-only` — только
такие записи.

Ранжирование — BM25 по заголовку, пути и тексту (заголовок и путь весят втрое),
как в корневом tools/search_items.py. Индекс кэшируется в .cache/ и
перестраивается при изменении файлов источников.

Ссылка вида `<source>:<id>` — так единицы указываются в mapping/*.yaml.
"""
from __future__ import annotations

import argparse
import json
import math
import pickle
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # папка bank/
EDU = ROOT
CACHE = EDU / ".cache" / "items.pkl"
TOKEN_RE = re.compile(r"[a-zа-яё0-9]+", re.I)
K1, B = 1.4, 0.75

TREES = {
    "education": EDU / "sources",
    "core": EDU / "sources",
}


def stem(w: str) -> str:
    w = w.lower().replace("ё", "е")
    if re.search(r"[а-я]", w):
        return w[:5]
    for suf in ("ing", "ed", "es", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def tokens(text: str) -> list[str]:
    return [stem(t) for t in TOKEN_RE.findall(text or "")]


def item_files(scope: str) -> list[Path]:
    out: list[Path] = []
    trees = [TREES["education"]] if scope == "education" else (
        [TREES["core"]] if scope == "core" else [TREES["core"], TREES["education"]])
    for t in trees:
        if t.is_dir():
            out.extend(sorted(t.glob("*/items/*.jsonl")))
    return out


def signature(scope: str) -> list:
    return [(str(p.relative_to(ROOT)), p.stat().st_size, int(p.stat().st_mtime))
            for p in item_files(scope)]


def build_index(scope: str) -> dict:
    docs: list[dict] = []
    postings: dict[str, list[tuple[int, int]]] = defaultdict(list)
    lengths: list[int] = []
    for p in item_files(scope):
        source = p.parent.parent.name
        with p.open(encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    it = json.loads(line)
                except json.JSONDecodeError:
                    continue
                path = it.get("path")
                path_s = " / ".join(path) if isinstance(path, list) else str(path or "")
                text = it.get("text") or ""
                toks = tokens(it.get("title", "")) * 3 + tokens(path_s) * 3 + tokens(text[:4000])
                doc_id = len(docs)
                docs.append({
                    "ref": "%s:%s" % (source, it.get("id")),
                    "kind": it.get("kind"),
                    "title": it.get("title", ""),
                    "path": path_s,
                    "answer": bool(it.get("answer")),
                    "level": it.get("level"),
                    "metadata_only": bool(it.get("metadata_only")),
                    "snippet": re.sub(r"\s+", " ", text[:240]),
                    "source": source,
                })
                lengths.append(len(toks))
                for term, tf in Counter(toks).items():
                    postings[term].append((doc_id, tf))
    return {"sig": signature(scope), "scope": scope, "docs": docs,
            "postings": dict(postings), "lengths": lengths}


def load_index(scope: str, rebuild: bool = False) -> dict:
    cache = CACHE.with_name("items-%s.pkl" % scope)
    if not rebuild and cache.exists():
        try:
            idx = pickle.loads(cache.read_bytes())
            if idx.get("sig") == signature(scope):
                return idx
        except Exception:  # noqa: BLE001
            pass
    idx = build_index(scope)
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_bytes(pickle.dumps(idx, protocol=4))
    return idx


def search(idx: dict, query: str, k: int, kind: str | None, source: str | None,
           answers: bool, include_index: bool, only_index: bool) -> list[tuple[float, dict]]:
    docs, postings, lengths = idx["docs"], idx["postings"], idx["lengths"]
    n = len(docs)
    avg = sum(lengths) / max(n, 1)
    scores: dict[int, float] = defaultdict(float)
    for term in set(tokens(query)):
        plist = postings.get(term)
        if not plist:
            continue
        idf = math.log(1 + (n - len(plist) + 0.5) / (len(plist) + 0.5))
        for doc_id, tf in plist:
            d = docs[doc_id]
            if kind and d["kind"] != kind:
                continue
            if source and d["source"] != source:
                continue
            if answers and not d["answer"]:
                continue
            if d["metadata_only"] and not (include_index or only_index):
                continue
            if only_index and not d["metadata_only"]:
                continue
            scores[doc_id] += idf * tf * (K1 + 1) / (tf + K1 * (1 - B + B * lengths[doc_id] / avg))
    top = sorted(scores.items(), key=lambda x: -x[1])[:k]
    return [(s, docs[i]) for i, s in top]


def show(ref: str) -> int:
    """Показать единицу целиком. Ищет в обоих деревьях."""
    source, _, iid = ref.partition(":")
    for base in (EDU / "sources",):
        d = base / source / "items"
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.jsonl")):
            with p.open(encoding="utf-8") as fh:
                for line in fh:
                    if line.strip() and '"%s"' % iid in line:
                        try:
                            it = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        if it.get("id") == iid:
                            print(json.dumps(it, ensure_ascii=False, indent=1))
                            return 0
    print("не найдено: %s" % ref)
    return 1


def main() -> int:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except AttributeError:
            pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("queries", nargs="*")
    ap.add_argument("-k", type=int, default=10, help="сколько результатов на запрос")
    ap.add_argument("--scope", choices=("education", "core", "all"), default="education",
                    help="какое дерево источников смотреть (по умолчанию education)")
    ap.add_argument("--kind")
    ap.add_argument("--source")
    ap.add_argument("--answers", action="store_true", help="только единицы с ответом")
    ap.add_argument("--index", action="store_true",
                    help="включить записи-указатели (metadata_only: true)")
    ap.add_argument("--metadata-only", action="store_true",
                    help="показать ТОЛЬКО записи-указатели")
    ap.add_argument("--id", help="показать единицу целиком: <source>:<id>")
    ap.add_argument("--rebuild", action="store_true")
    a = ap.parse_args()
    if a.id:
        return show(a.id)
    if not a.queries:
        ap.error("нужен запрос или --id")
    idx = load_index(a.scope, a.rebuild)
    for q in a.queries:
        print("== %s" % q)
        for score, d in search(idx, q, a.k, a.kind, a.source, a.answers, a.index, a.metadata_only):
            flag = " [оглавление]" if d["metadata_only"] else ""
            print("%6.2f %s [%s]%s %s | %s | ответ: %s"
                  % (score, d["ref"], d["kind"], flag, d["title"][:70], d["path"][:90],
                     "да" if d["answer"] else "нет"))
            if d["snippet"]:
                print("       %s" % d["snippet"][:160])
    return 0


if __name__ == "__main__":
    sys.exit(main())
