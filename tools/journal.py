#!/usr/bin/env python3
"""Заготовка сессии и проверка журнала. Только stdlib.

    python tools/journal.py open  --date 2026-12-12 --time 11:00 --mode challenge
    python tools/journal.py close journal/2026/2026-12-12_1100 --time 14:00
    python tools/journal.py check journal/2026/2026-12-12_1100

Стандарт: docs/LOGGING-STANDARD.md. Инструмент ничего не придумывает: дату и время даёт ученик.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODES = {"assessment", "challenge", "learn", "review", "free"}
OUTCOMES = {"solved_unaided", "solved_hinted", "partial", "unsolved", "revealed", "abandoned"}
ORIGINS = {"bank", "agent-generated", "student"}
OBS_HEADS = ["## Со слов ученика", "## Факты", "## Интерпретации агента", "## Гипотезы на проверку"]
SESSION_HEADS = ["## План", "## Ход", "## Итог"]
FILES = ["meta.json", "session.md", "transcript.md", "observations.md", "proposals.md"]


def _phase() -> str:
    try:
        text = (ROOT / "learner" / "state.yaml").read_text(encoding="utf-8")
        m = re.search(r"^phase:\s*(\w+)", text, re.M)
        return m.group(1) if m else "assessment"
    except OSError:
        return "assessment"


def _hm(s: str) -> str:
    m = re.fullmatch(r"(\d{1,2})[:\s.]?(\d{2})", s.strip())
    if not m or int(m[1]) > 23 or int(m[2]) > 59:
        sys.exit(f"время '{s}' не распознано (ожидается ЧЧ:ММ)")
    return f"{int(m[1]):02d}:{m[2]}"


def cmd_open(a) -> int:
    try:
        d = datetime.strptime(a.date, "%Y-%m-%d")
    except ValueError:
        sys.exit("дата в формате ГГГГ-ММ-ДД")
    t = _hm(a.time)
    if a.mode not in MODES:
        sys.exit(f"режим из {sorted(MODES)}")
    sid = f"{a.date}_{t.replace(':', '')}"
    base = ROOT / "journal" / str(d.year)
    dest = base / sid
    while dest.exists():
        sid += "b"
        dest = base / sid
    (dest / "work").mkdir(parents=True)
    (dest / "work" / ".gitkeep").write_text("", encoding="utf-8")
    subs = {"id": sid, "date": a.date, "time": t, "mode": a.mode, "phase": _phase()}
    for name in FILES:
        text = (ROOT / "templates" / name).read_text(encoding="utf-8")
        for k, v in subs.items():
            text = text.replace("{" + k + "}", v)
        (dest / name).write_text(text, encoding="utf-8", newline="\n")
    print(f"создано: {dest.relative_to(ROOT)}")
    return 0


def _load_meta(folder: Path):
    return json.loads((folder / "meta.json").read_text(encoding="utf-8"))


def cmd_close(a) -> int:
    folder = Path(a.folder)
    meta = _load_meta(folder)
    if a.time:
        end = _hm(a.time)
        meta["end_time"] = end
        h1, m1 = map(int, meta["start_time"].split(":"))
        h2, m2 = map(int, end.split(":"))
        dur = (h2 * 60 + m2) - (h1 * 60 + m1)
        meta["duration_min"] = dur if dur >= 0 else dur + 1440
    meta["status"] = "closed"
    if a.late:
        meta["closed_late"] = True
    (folder / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"meta.json: status=closed, end={meta['end_time']}, duration={meta['duration_min']}")
    return cmd_check(a)


def cmd_check(a) -> int:
    folder = Path(a.folder)
    errs: list[str] = []
    if not folder.is_dir():
        return _report([f"нет папки {folder}"])
    for f in FILES:
        if not (folder / f).is_file():
            errs.append(f"нет файла {f}")
    if not (folder / "work").is_dir():
        errs.append("нет папки work/")
    extra = {p.name for p in folder.iterdir()} - set(FILES) - {"work"}
    extra = {n for n in extra if not re.fullmatch(r"addendum-\d{4}-\d{2}-\d{2}.*\.md", n)}
    if extra:
        errs.append(f"лишние файлы: {sorted(extra)}")
    if errs:
        return _report(errs)
    try:
        meta = _load_meta(folder)
    except json.JSONDecodeError as e:
        return _report([f"meta.json: {e}"])
    closed = meta.get("status") == "closed"
    if meta.get("mode") not in MODES:
        errs.append("meta.mode")
    obs = (folder / "observations.md").read_text(encoding="utf-8")
    pos = [obs.find(h) for h in OBS_HEADS]
    if -1 in pos or pos != sorted(pos):
        errs.append("observations.md: нужны 4 раздела по порядку: " + ", ".join(h[3:] for h in OBS_HEADS))
    sess = (folder / "session.md").read_text(encoding="utf-8")
    if any(h not in sess for h in SESSION_HEADS):
        errs.append("session.md: нужны разделы План / Ход / Итог")
    if closed:
        if not meta.get("end_time") and "time_unknown" not in meta.get("files_touched", []):
            errs.append("meta.end_time пуст (если время неизвестно — 'time_unknown' в files_touched)")
        for i, it in enumerate(meta.get("items", [])):
            if it.get("outcome") not in OUTCOMES:
                errs.append(f"items[{i}].outcome")
            if it.get("origin") not in ORIGINS:
                errs.append(f"items[{i}].origin")
            if not it.get("item_id"):
                errs.append(f"items[{i}].item_id")
        for name in ("session.md", "observations.md"):
            body = re.sub(r"<!--.*?-->", "", (folder / name).read_text(encoding="utf-8"), flags=re.S)
            if len(body.strip()) < 200:
                errs.append(f"{name}: выглядит незаполненным")
        tr = (folder / "transcript.md").read_text(encoding="utf-8")
        if not re.search(r"^completeness:\s*(verbatim|reconstructed)", tr, re.M):
            errs.append("transcript.md: нет строки completeness:")
        if not re.search(r"^\[[^\]]+\]\s*СТ:", tr, re.M):
            errs.append("transcript.md: нет реплик ученика")
        idx = (ROOT / "journal" / "INDEX.md").read_text(encoding="utf-8")
        if meta["id"] not in idx:
            errs.append("journal/INDEX.md: нет строки сессии")
    return _report(errs)


def _report(errs: list[str]) -> int:
    if errs:
        print("ОШИБКИ:")
        for e in errs:
            print("  -", e)
        return 1
    print("OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    o = sub.add_parser("open")
    o.add_argument("--date", required=True)
    o.add_argument("--time", required=True)
    o.add_argument("--mode", required=True)
    o.set_defaults(fn=cmd_open)
    c = sub.add_parser("close")
    c.add_argument("folder")
    c.add_argument("--time")
    c.add_argument("--late", action="store_true")
    c.set_defaults(fn=cmd_close)
    k = sub.add_parser("check")
    k.add_argument("folder")
    k.set_defaults(fn=cmd_check)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
