# Происхождение репозитория

`MATH_PRO-Learn` — чистый старт. Предыдущий репозиторий
[`A1S2D3TheName/MATH_PRO`](https://github.com/A1S2D3TheName/MATH_PRO) (приватный) служил сборщиком
датасета и содержал локальную обучающую программу (`python -m mathpro`), уроки по 32 темам,
конвейер промптов для агентов-авторов, независимые аудиты. Выяснилось:

1. Старт был слишком простым — сначала нужен анализ компетенций (→ [ASSESSMENT.md](ASSESSMENT.md)).
2. Пользовательский интерфейс не нужен — лишняя кодовая база.

## Что перенесено

| Откуда (MATH_PRO) | Куда | Что |
|---|---|---|
| `tree.yaml` (ветка `main`) | `curriculum/tree.yaml` | карта программы: 7 ступеней, 18 разделов, 270 тем, пререквизиты |
| `topics/` (ветка `main`) | `curriculum/lessons/` | материалы 35 тем ступеней 1–3 (теория, задачи, `topic.yaml`) — справка для агента |
| `math_repo_education/sources` (PR [#353](https://github.com/A1S2D3TheName/MATH_PRO/pull/353), ветка `arena/25979f4f-math-pro`) | `bank/sources` | 22 источника задач и материалов с `SOURCE.yaml`, `REPORT.md`, `items/*.jsonl` |
| `math_repo_education/{catalog,schemas,overlays,CATALOG.md}` | `bank/` | каталог источников, схемы, пометки о дефектах содержимого |
| `math_repo_education/tools/search_items.py` | `bank/tools/search_items.py` | поиск по банку (адаптирован под новый путь) |
| `math_repo_education/specs/*` | `docs/reference/` | таксономия, пробелы покрытия, спецификация диагностики, педагогические заметки |

## Что намеренно **не** перенесено

`app/`, `mathpro/`, `product/`, `design/` (интерфейс), `prompts/` и `tools/`
конвейера авторов, `vendor/magistra/`, `reviews/`, `drafts/`, `mapping/`, `engines/`, `errors/`,
`sources/` основной ветки (OpenStax, WeBWorK, im-k5/6-8, ck12, Project Euler — 250 МБ), промежуточные
отчёты и тесты. Всё это остаётся в старом репозитории; при необходимости достаётся оттуда.

Из `math-prm800k` не перенесены два служебных файла (`prm-phase1-steps.jsonl`, `prm-phase2-test.jsonl`,
≈ 20 МБ): это разметка шагов для обучения моделей, не задачи для ученика. Файл `math-dataset.jsonl` на месте.

Открытые PR [#354](https://github.com/A1S2D3TheName/MATH_PRO/pull/354) и [#356](https://github.com/A1S2D3TheName/MATH_PRO/pull/356) старого репозитория — два варианта той же чистки (удаление UI); здесь они заменены чистым стартом. Из #354 по идее взят подход «вход по диагностике», из #356 — отказ от веб-кода.

## Известные ограничения банка

* Данные **не перепроверялись математически** при переносе: решение владельца — не тратить время на сверку.
  Ответы и разборы в `bank/` могут содержать ошибки; в ходе занятий агент проверяет их кодом ([AGENTS.md](../AGENTS.md) §4).
* В `bank/catalog/catalog.json` и `bank/CATALOG.md` остались ссылки на `fetch.py`, `manifest.json`, удалённые файлы
  и исходные размеры источников — это следы старого этапа. Подсчёты (`22 источника, 25 538 единиц`) относятся к исходному набору.
* `bank/tools/verify_catalog.py` и `manifest.json` убраны (проверка целостности исходного набора).
* Источники `math-500-ru`, `aptitude-test-platform`, `national-olympiads-bank` — только индекс/паспорт (права на тексты не подтверждены) — задач для выдачи в них нет.
* Русскоязычных задач начального уровня (ступени 1–2) в банке мало: [reference/COVERAGE-GAPS.md](reference/COVERAGE-GAPS.md). Агент допускается их составлять сам (`origin: agent-generated`) с проверкой ответа кодом.
* Лицензии источников — в `bank/sources/<id>/SOURCE.yaml`; перепубликация и использование — в рамках этих условий.
