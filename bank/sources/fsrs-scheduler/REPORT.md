Итог: source fsrs-scheduler | единиц 10 | уроков 10 | задач 0 (с ответами 0) | лицензия MIT | МБ 0.0

## Что это

10 разделов с описанием модели памяти (сложность, стабильность, извлекаемость) и законов забывания. Теоретическое основание для блока delayed retention.

## Лицензия и как проверена

Лицензия разрешает перепубликацию: `MIT`. Файл лицензии прочитан в закреплённом коммите (`upstream_commit` в `SOURCE.yaml`).
Атрибуция: Free Spaced Repetition Scheduler contributors, MIT License.

## Откуда и как получено

Источник: <https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler>, закреплённый коммит `93ed713fd9c139fa12be9bba8c080a682a7c503d`.
`fetch.py` скачивает архив репозитория по SHA с `codeload.github.com`, распаковывает в `sources/_cache/` и строит `items/*.jsonl`.
Повторный запуск: `python sources/fsrs-scheduler/fetch.py`.

## Состав `items/`

| файл | строк | КБ |
|---|---:|---:|
| `items/docs.jsonl` | 10 | 9.7 |

## Назначение в учебной системе

10 разделов с описанием модели памяти (сложность, стабильность, извлекаемость) и законов забывания. Теоретическое основание для блока delayed retention.

## Ограничения и что не вошло

Только README, кода нет. Формулы вынесены на внешнюю вики, в репозитории их нет — при цитировании нужна ссылка на вики FSRS.

## Проверенные детали

- Модель DSR — общий предок SM-2; в MATH_PRO используется своя лестница 1/3/7/16/35/75 дней.

## Как это используется

Каталог машинночитаем: `math_repo_education/catalog/resources.yaml`, схема единицы — `math_repo_education/schemas/item.schema.json`.
Проверка целостности: `python math_repo_education/tools/verify_catalog.py`.
