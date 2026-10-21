Итог: source pyedmine | единиц 116 | уроков 116 | задач 0 (с ответами 0) | лицензия MIT | МБ 0.1

## Что это

116 модулей: алгоритмы KT и CDM на чистом Python, с примерами и конфигами. Более лёгкая (без torch) альтернатива pyKT для одиночного ученика.

## Лицензия и как проверена

Лицензия разрешает перепубликацию: `MIT`. Файл лицензии прочитан в закреплённом коммите (`upstream_commit` в `SOURCE.yaml`).
Атрибуция: pyedmine contributors, MIT License.

## Откуда и как получено

Источник: <https://github.com/ZhijieXiong/pyedmine>, закреплённый коммит `20af7967486e833899e589c37ae33ec1b28662d1`.
`fetch.py` скачивает архив репозитория по SHA с `codeload.github.com`, распаковывает в `sources/_cache/` и строит `items/*.jsonl`.
Повторный запуск: `python sources/pyedmine/fetch.py`.

## Состав `items/`

| файл | строк | КБ |
|---|---:|---:|
| `items/models.jsonl` | 116 | 59.4 |

## Назначение в учебной системе

116 модулей: алгоритмы KT и CDM на чистом Python, с примерами и конфигами. Более лёгкая (без torch) альтернатива pyKT для одиночного ученика.

## Ограничения и что не вошло

Состояние и API отличаются от pyKT; выбирать надо одно. Часть модулей требует numpy/pandas.

## Проверенные детали

- Альтернатива pyKT и EduCDM в одном месте — полезно при сравнении подходов.

## Как это используется

Каталог машинночитаем: `math_repo_education/catalog/resources.yaml`, схема единицы — `math_repo_education/schemas/item.schema.json`.
Проверка целостности: `python math_repo_education/tools/verify_catalog.py`.
