Итог: source math-prm800k | единиц 16317 | уроков 0 | задач 12500 (с ответами 16315) | лицензия MIT | МБ 34.0

## Что это

Ядро банка задач: 12 500 задач с ответами и решениями, уровни 1–5 по предметам, пошаговые метки человеческих и модельных решений, нормализатор ответов для автопроверки. Основа для Immediate mastery, Transfer и Error diagnosis.

## Лицензия и как проверена

Лицензия разрешает перепубликацию: `MIT`. Файл лицензии прочитан в закреплённом коммите (`upstream_commit` в `SOURCE.yaml`).
Атрибуция: MATH dataset (Dan Hendrycks et al.) и PRM800K (OpenAI), MIT License.

## Откуда и как получено

Источник: <https://github.com/openai/prm800k>, закреплённый коммит `7ecc794703b2877f63226f2477a49b34f9b25163`.
`fetch.py` скачивает архив репозитория по SHA с `codeload.github.com`, распаковывает в `sources/_cache/` и строит `items/*.jsonl`.
Повторный запуск: `python sources/math-prm800k/fetch.py`.

## Состав `items/`

| файл | строк | КБ |
|---|---:|---:|
| `items/math-dataset.jsonl` | 12500 | 14928.5 |
| `items/prm-phase1-steps.jsonl` | 1055 | 9588.1 |
| `items/prm-phase2-test.jsonl` | 2762 | 10317.0 |

## Назначение в учебной системе

Ядро банка задач: 12 500 задач с ответами и решениями, уровни 1–5 по предметам, пошаговые метки человеческих и модельных решений, нормализатор ответов для автопроверки. Основа для Immediate mastery, Transfer и Error diagnosis.

## Ограничения и что не вошло

Задачи на английском. MATH — соревновательные задачи (AMC/AIME-уровень и выше), начальный уровень (арифметика, дроби) покрыт слабо: для ступеней 1–2 нужны другие источники. train-сплит PRM800K (456 МБ) не включён — разметка шагов приведена только для test.

## Проверенные детали

- MATH — 12 500 задач: `items/math-dataset.jsonl` (train 12 000 + test 500).
- PRM800K phase1 (человеческая пошаговая разметка): `items/prm-phase1-steps.jsonl` — 1 055 записей.
- PRM800K phase2 test (модельные решения с метками, включая ошибочные шаги): `items/prm-phase2-test.jsonl` — 2 762 записи.
- В репозитории `hendrycks/math` данных нет — только загрузчики; данные лежат на Hugging Face. Поэтому взята MIT-версия из `openai/prm800k` (`prm800k/math_splits/`), это тот же датасет.
- Тот же `math_splits/test.jsonl` (500 строк) — источник русского `math-500-ru`: unique_id, subject, level и answer совпадают (проверено на строках 0, 1, 2, 250, 499).
- Нормализатор ответов (`prm800k/grading/math_normalize.py`, `grader.py`) лежит в upstream-архиве; в MATH_PRO уже есть свой `mathpro/grading/` — norm-логику стоит сверить.

## Как это используется

Каталог машинночитаем: `math_repo_education/catalog/resources.yaml`, схема единицы — `math_repo_education/schemas/item.schema.json`.
Проверка целостности: `python math_repo_education/tools/verify_catalog.py`.
