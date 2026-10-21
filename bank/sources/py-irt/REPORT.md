Итог: source py-irt | единиц 16 | уроков 16 | задач 0 (с ответами 0) | лицензия MIT | МБ 0.0

## Что это

16 модулей: 1PL/2PL/3PL IRT, многомерный MIRT, обработка anchor-вопросов, экспорт для CAT. Техническая опора для адаптивного тестирования.

## Лицензия и как проверена

Лицензия разрешает перепубликацию: `MIT`. Файл лицензии прочитан в закреплённом коммите (`upstream_commit` в `SOURCE.yaml`).
Атрибуция: py-irt contributors (форк nd-ball/py-irt), MIT License.

## Откуда и как получено

Источник: <https://github.com/nd-ball/py-irt>, закреплённый коммит `6514928ec753771c8858bf16581e9715d6025ed9`.
`fetch.py` скачивает архив репозитория по SHA с `codeload.github.com`, распаковывает в `sources/_cache/` и строит `items/*.jsonl`.
Повторный запуск: `python sources/py-irt/fetch.py`.

## Состав `items/`

| файл | строк | КБ |
|---|---:|---:|
| `items/modules.jsonl` | 16 | 7.3 |

## Назначение в учебной системе

16 модулей: 1PL/2PL/3PL IRT, многомерный MIRT, обработка anchor-вопросов, экспорт для CAT. Техническая опора для адаптивного тестирования.

## Ограничения и что не вошло

Оригинальный `ets/py-irt` в этом окружении недоступен (404); взят поддерживаемый форк с той же лицензией MIT. Требует Python ≥3.9 и numpy/scipy.

## Проверенные детали

- Проверка доступности: `ets/py-irt` → HTTP 404 и через API, и через веб.

## Как это используется

Каталог машинночитаем: `math_repo_education/catalog/resources.yaml`, схема единицы — `math_repo_education/schemas/item.schema.json`.
Проверка целостности: `python math_repo_education/tools/verify_catalog.py`.
