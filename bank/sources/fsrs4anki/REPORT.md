Итог: source fsrs4anki | единиц 50 | уроков 50 | задач 0 (с ответами 0) | лицензия MIT | МБ 0.0

## Что это

Готовый планировщик отложенного повторения (delayed retention): 50 разделов документации и 40 экспериментальных ноутбуков с выводами по забыванию, сложности и стабильности памяти.

## Лицензия и как проверена

Лицензия разрешает перепубликацию: `MIT`. Файл лицензии прочитан в закреплённом коммите (`upstream_commit` в `SOURCE.yaml`).
Атрибуция: FSRS4Anki contributors, MIT License.

## Откуда и как получено

Источник: <https://github.com/open-spaced-repetition/fsrs4anki>, закреплённый коммит `ff7c85cee735472d1c9cec0b9252d184087f74d8`.
`fetch.py` скачивает архив репозитория по SHA с `codeload.github.com`, распаковывает в `sources/_cache/` и строит `items/*.jsonl`.
Повторный запуск: `python sources/fsrs4anki/fetch.py`.

## Состав `items/`

| файл | строк | КБ |
|---|---:|---:|
| `items/docs.jsonl` | 50 | 36.5 |

## Назначение в учебной системе

Готовый планировщик отложенного повторения (delayed retention): 50 разделов документации и 40 экспериментальных ноутбуков с выводами по забыванию, сложности и стабильности памяти.

## Ограничения и что не вошло

Код — TypeScript/JavaScript, а не Python; в MATH_PRO планировщик написан свой (`mathpro/progress/scheduler.py`) — заимствовать модель, не код. Ноутбуки требуют Jupyter.

## Проверенные детали

- Это обоснование для интервальной лестницы, а не готовый модуль MATH_PRO.

## Как это используется

Каталог машинночитаем: `math_repo_education/catalog/resources.yaml`, схема единицы — `math_repo_education/schemas/item.schema.json`.
Проверка целостности: `python math_repo_education/tools/verify_catalog.py`.
