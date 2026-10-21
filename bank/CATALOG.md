# Каталог источников `math_repo_education`

Числа в таблице посчитаны по фактическому содержимому `items/`, а не взяты
из описаний. Машиночитаемый вариант — `catalog/catalog.json`
(человекочитаемый YAML — `catalog/resources.yaml`); хеши файлов —
`catalog/manifest.json`. Пути в каталоге и манифесте **относительны
к папке `math_repo_education/`.

Машинные статусы у каждого источника: `availability` (доступен ли),
`download` (скачан ли), `run` (запускался ли код), `item_qa` (проверены ли
строки), `rights` (разрешает ли лицензия перепубликацию). Подробнее —
`schemas/resource.schema.json`.

**Итого: 22 источников, 25538 единиц, 46.0 МБ.**

Распределение: 17 источников с полной перепубликацией, 4 — только оглавление, 1 — не публикуется (права).

**Код ни одного источника не запускался** (`run: not_executed` у всех): это сбор и проверка материала, а не прогон чужих систем.

## Сводная таблица

| id | лицензия | права | единиц | домены | измерения | уровни | статусы |
|---|---|---|---:|---|---|---|---|
| `ai-tutor-socratic` | MIT | полная | 102 | arithmetic, fractions, ratios, percent | error_diagnosis, immediate_mastery | 1, 2, 3 | reachable / downloaded / schema_validated / permissive |
| `educdm` | Apache-2.0 | полная | 31 | meta | immediate_mastery, error_diagnosis | 3, 4, 5, 6, 7 | reachable / downloaded / schema_validated / permissive |
| `exercism-python` | MIT | полная | 163 | python | immediate_mastery, independence | 3, 4, 5, 6 | reachable / downloaded / schema_validated / permissive |
| `forallx` | CC-BY-4.0 | полная | 93 | logic, proofs | immediate_mastery, error_diagnosis | 4, 5, 6 | reachable / downloaded / schema_validated / permissive |
| `fsrs-scheduler` | MIT | полная | 10 | meta | delayed_retention | 3, 4, 5, 6, 7 | reachable / downloaded / schema_validated / permissive |
| `fsrs4anki` | MIT | полная | 50 | meta | delayed_retention | 3, 4, 5, 6, 7 | reachable / downloaded / schema_validated / permissive |
| `imosllean4` | Apache-2.0 | полная | 72 | nonstandard, proofs | transfer | 7 | reachable / downloaded / schema_validated / permissive |
| `math-prm800k` | MIT | полная | 16317 | algebra, geometry, analysis, discrete, number-theory, nonstandard | immediate_mastery, transfer, error_diagnosis | 3, 4, 5, 6, 7 | reachable / downloaded / schema_validated / permissive |
| `minif2f` | MIT | полная | 488 | nonstandard, proofs | transfer, error_diagnosis | 6, 7 | reachable / downloaded / schema_validated / permissive |
| `py-irt` | MIT | полная | 16 | meta | immediate_mastery | 3, 4, 5, 6, 7 | reachable / downloaded / schema_validated / permissive |
| `pyedmine` | MIT | полная | 116 | meta | delayed_retention, error_diagnosis | 3, 4, 5, 6, 7 | reachable / downloaded / schema_validated / permissive |
| `pykt` | MIT | полная | 94 | meta | delayed_retention, immediate_mastery | 3, 4, 5, 6, 7 | reachable / downloaded / schema_validated / permissive |
| `pypsy` | MIT | полная | 18 | meta | immediate_mastery | 3, 4, 5, 6, 7 | reachable / downloaded / schema_validated / permissive |
| `sympy-books` | MIT | полная | 8 | python, probability, linear-algebra | immediate_mastery, transfer | 4, 5, 6 | reachable / downloaded / schema_validated / permissive |
| `thealgorithms-python` | MIT | полная | 1287 | python, discrete, number-theory | immediate_mastery, transfer | 3, 4, 5, 6 | reachable / downloaded / schema_validated / permissive |
| `treecut-math` | Apache-2.0 | полная | 4000 | arithmetic, algebra | error_diagnosis, transfer | 3, 4 | reachable / downloaded / schema_validated / permissive |
| `ultimate-aptitude` | CC-BY-4.0 | полная | 1098 | arithmetic, algebra, probability, reasoning, nonstandard | immediate_mastery, transfer | 4, 5, 6 | reachable / downloaded / schema_validated / permissive |
| `aptitude-test-platform` | не указана | только оглавление | 600 | arithmetic, reasoning, discrete | immediate_mastery, transfer | 3, 4, 5, 6 | reachable / metadata_only / schema_validated / unclear |
| `iq-measurer` | не указана | только оглавление | 200 | reasoning, memory, speed | immediate_mastery | 1, 2, 3, 4, 5, 6 | reachable / metadata_only / schema_validated / unclear |
| `math-500-ru` | не указана в карточке датасета | только оглавление | 500 | algebra, geometry, analysis, nonstandard | immediate_mastery, transfer | 4, 5, 6, 7 | reachable / metadata_only / schema_validated / unclear |
| `mathforces` | не указана | только оглавление | 275 | nonstandard, proofs, geometry | transfer | 5, 6, 7 | reachable / metadata_only / schema_validated / unclear |
| `national-olympiads-bank` | All rights reserved — копирование, зеркалирование и перепубликация запрещены без письменного разрешения | только оглавление | 0 | nonstandard, proofs | transfer | 4, 5, 6, 7 | blocked_rights / not_downloaded / not_audited / restricted |

## Подробно

### `ai-tutor-socratic`

**MathMisconception-IN — граф знаний, каталог заблуждений и сократический каркас**

* адрес: <https://github.com/NavyashreeNS/ai-tutor>
* upstream: <https://github.com/NavyashreeNS/ai-tutor>, коммит `a276b1ca876c`
* лицензия: MIT (<https://github.com/NavyashreeNS/ai-tutor/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 1, 2, 3 | забрано: 2026-10-20
* атрибуция: MathMisconception-IN, MIT License.

**Назначение.** Готовый каркас для блока Error diagnosis: 18 концепций с пререквизитами и сложностью, 33 типичных заблуждения, 51 вопрос с привязкой к заблуждениям и ветвлением follow-up. Приём — ступени 1–3 (числа, дроби, проценты).

**Ограничения.** Схема ориентирована на NCERT (Индия), в `items/` нет текстов правил и пояснений — только идентификаторы и краткие подписи. Каталог заблуждений заявляет 34 записи, фактически содержит 33 — расхождение зафиксировано, не исправлено. Английский язык.

| файл | строк |
|---|---:|
| `sources/ai-tutor-socratic/items/knowledge-graph.jsonl` | 18 |
| `sources/ai-tutor-socratic/items/misconceptions.jsonl` | 33 |
| `sources/ai-tutor-socratic/items/questions.jsonl` | 51 |

### `aptitude-test-platform`

**Aptitude Test Platform — 600 вопросов двух разделов**

* адрес: <https://github.com/jidvish/aptitude-test-platform-public>
* upstream: <https://github.com/jidvish/aptitude-test-platform-public>, коммит `c62e962bf34b`
* лицензия: не указана (файла лицензии нет; происхождение исходных markdown-файлов не документировано) (<https://github.com/jidvish/aptitude-test-platform-public>)
* права в репозитории: только оглавление
* статусы: доступность `reachable`, загрузка `metadata_only`, запуск `not_executed`, проверка строк `schema_validated`, права `unclear`
* язык: en | ступени: 3, 4, 5, 6 | забрано: 2026-10-20
* атрибуция: Aptitude Test Platform by jidvish — лицензия не указана, тексты не копируются.

**Назначение.** Количественные способности (300) и логическое мышление (300) по трём уровням, с разбором каждого решения. Оглавление полезно как карта тем количественных способностей.

**Ограничения.** Тексты и разборы не копируются. Варианты ответа в сгенерированном банке — машинно сгенерированные отвлекающие варианты; качество распределения правильных ответов не проверялось. Часть вопросов имеет в формулировке `$…$`-LaTeX.

| файл | строк |
|---|---:|
| `sources/aptitude-test-platform/items/questions-index.jsonl` | 600 |

### `educdm`

**EduCDM — зоопарк моделей когнитивной диагностики**

* адрес: <https://github.com/bigdata-ustc/EduCDM>
* upstream: <https://github.com/bigdata-ustc/EduCDM>, коммит `c610e6ae7f45`
* лицензия: Apache-2.0 (<https://github.com/bigdata-ustc/EduCDM/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: EduCDM (Zhou et al.), Apache-2.0.

**Назначение.** 31 модуль моделей когнитивной диагностики (DINA, DINO, MIRT, IRT, PCM, …) — готовые алгоритмы, чтобы оценивать не «сколько баллов», а «какие компетенции освоены». Инструмент для диагностики по компетенциям.

**Ограничения.** Требует PyTorch и своих форматов данных; в MATH_PRO подход «ошибка → компетенция» реализован через `errors/catalog.yaml`, а не через CDM. Это опора и обоснование, а не готовый модуль.

| файл | строк |
|---|---:|
| `sources/educdm/items/models.jsonl` | 31 |

### `exercism-python`

**Exercism Python — 163 проверяемых упражнения**

* адрес: <https://github.com/exercism/python>
* upstream: <https://github.com/exercism/python>, коммит `6105f6d9d3ef`
* лицензия: MIT (<https://github.com/exercism/python/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6 | забрано: 2026-10-20
* атрибуция: Exercism Python track, MIT License.

**Назначение.** Практика по Python с машинно-проверяемыми тестами: 131 practice-упражнение и 32 concept-упражнения. У каждого — постановка, `tests.toml` с числом проверок и эталонное решение. Готовая система проверки для блока Python.

**Ограничения.** Тексты и тесты на английском; к каждому упражнению прилагается эталонное решение — его нельзя показывать ученику до попытки.

| файл | строк |
|---|---:|
| `sources/exercism-python/items/exercises.jsonl` | 163 |

### `forallx`

**forallx — учебник логики P. D. Magnus (CC BY 4.0)**

* адрес: <https://github.com/OpenLogicProject/forallx>
* upstream: <https://github.com/OpenLogicProject/forallx>, коммит `b9a872431eb9`
* лицензия: CC-BY-4.0 (<https://github.com/OpenLogicProject/forallx/blob/master/LICENSE.md>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 4, 5, 6 | забрано: 2026-10-20
* атрибуция: forallx: Calgary Edition by P. D. Magnus, CC BY 4.0, Open Logic Project.

**Назначение.** Готовая теория для раздела «логика»: 93 раздела — пропозициональная и предикативная логика, таблицы истинности, семантика, доказательства, естественный язык. Текст приведён в Markdown (LaTeX-команды упрощены).

**Ограничения.** Перевод LaTeX в текст грубый: команды вроде `\begin{}` убраны, математика частично потеряна. Для формул нужен исходный .tex. Упражнения в разборе не выделены — их надо искать по ключу `exercise`.

| файл | строк |
|---|---:|
| `sources/forallx/items/sections.jsonl` | 93 |

### `fsrs-scheduler`

**Free Spaced Repetition Scheduler — спецификация алгоритма FSRS**

* адрес: <https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler>
* upstream: <https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler>, коммит `93ed713fd9c1`
* лицензия: MIT (<https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: Free Spaced Repetition Scheduler contributors, MIT License.

**Назначение.** 10 разделов с описанием модели памяти (сложность, стабильность, извлекаемость) и законов забывания. Теоретическое основание для блока delayed retention.

**Ограничения.** Только README, кода нет. Формулы вынесены на внешнюю вики, в репозитории их нет — при цитировании нужна ссылка на вики FSRS.

| файл | строк |
|---|---:|
| `sources/fsrs-scheduler/items/docs.jsonl` | 10 |

### `fsrs4anki`

**FSRS4Anki — планировщик повторения на модели DSR**

* адрес: <https://github.com/open-spaced-repetition/fsrs4anki>
* upstream: <https://github.com/open-spaced-repetition/fsrs4anki>, коммит `ff7c85cee735`
* лицензия: MIT (<https://github.com/open-spaced-repetition/fsrs4anki/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: FSRS4Anki contributors, MIT License.

**Назначение.** Готовый планировщик отложенного повторения (delayed retention): 50 разделов документации и 40 экспериментальных ноутбуков с выводами по забыванию, сложности и стабильности памяти.

**Ограничения.** Код — TypeScript/JavaScript, а не Python; в MATH_PRO планировщик написан свой (`mathpro/progress/scheduler.py`) — заимствовать модель, не код. Ноутбуки требуют Jupyter.

| файл | строк |
|---|---:|
| `sources/fsrs4anki/items/docs.jsonl` | 50 |

### `imosllean4`

**IMOSLLean4 — шортлист ММО с разбором и формализацией Lean 4**

* адрес: <https://github.com/mortarsanjaya/IMOSLLean4>
* upstream: <https://github.com/mortarsanjaya/IMOSLLean4>, коммит `883b0326e585`
* лицензия: Apache-2.0 (<https://github.com/mortarsanjaya/IMOSLLean4/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 7 | забрано: 2026-10-20
* атрибуция: IMOSLLean4 (Alireza Shokrollahi et al.), Apache-2.0.

**Назначение.** 72 задачи шортлиста ММО (2006–2024) с условием, ответом и разбором. Верхняя граница сложности: годится для проверки прочности и переноса, но не для входной диагностики.

**Ограничения.** Только английский, только IMO-уровень. Задачи 2006–2024, не весь шортлист. Формализация Lean 4 требует отдельного toolchain.

| файл | строк |
|---|---:|
| `sources/imosllean4/items/imo-shortlist.jsonl` | 72 |

### `iq-measurer`

**IQ Measurer — 200 вопросов, 4 когнитивных домена**

* адрес: <https://github.com/Ksound22/iq-measurer>
* upstream: <https://github.com/Ksound22/iq-measurer>, коммит `401ceca03d0b`
* лицензия: не указана (в репозитории нет файла лицензии; по умолчанию — все права защищены) (<https://github.com/Ksound22/iq-measurer>)
* права в репозитории: только оглавление
* статусы: доступность `reachable`, загрузка `metadata_only`, запуск `not_executed`, проверка строк `schema_validated`, права `unclear`
* язык: en | ступени: 1, 2, 3, 4, 5, 6 | забрано: 2026-10-20
* атрибуция: IQ Measurer by Ksound22 — лицензия не указана, тексты не копируются.

**Назначение.** Матрицы, вербальные аналогии, рабочая память, скорость обработки. Меряет общие способности, а не знание предмета: это отдельный контур, его нельзя складывать с предметными баллами в один показатель.

**Ограничения.** Тексты вопросов не копируются (нет лицензии). В каталоге — только оглавление: домен, сложность, число вариантов, наличие SVG, лимит времени. Оценка IQ в самом приложении — самодельная («IRT-вдохновлённая»), психометрической валидности не имеет.

| файл | строк |
|---|---:|
| `sources/iq-measurer/items/questions-index.jsonl` | 200 |

### `math-500-ru`

**MATH-500-Russian — индекс 500 позиций (тексты не публикуются)**

* адрес: <https://huggingface.co/datasets/evilfreelancer/MATH-500-Russian>
* upstream: <https://huggingface.co/datasets/evilfreelancer/MATH-500-Russian>, коммит `bf0c9320c19a`
* лицензия: не указана в карточке датасета; отдельная лицензия на русский перевод не подтверждена (<https://huggingface.co/datasets/evilfreelancer/MATH-500-Russian>)
* права в репозитории: только оглавление
* статусы: доступность `reachable`, загрузка `metadata_only`, запуск `not_executed`, проверка строк `schema_validated`, права `unclear`
* лицензионный gate: `blocked_pending_written_permission` — Права на машинный перевод (qwen2.5:32b) не подтверждены; в карточке датасета лицензия не указана.
* язык: ru | ступени: 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: Индекс соответствует MATH-500 (HuggingFaceH4) и PRM800K (OpenAI) — MIT — по полю unique_id; русский перевод evilfreelancer/MATH-500-Russian лицензии не имеет, его тексты не публикуются.

**Назначение.** Единственный найденный русскоязычный банк олимпиадного уровня. Опубликован только индекс: 500 позиций, 10 из них с preview-метаданными (unique_id, предмет, уровень) и 490 позиционных заполнителей. Текстов задач, ответов и решений нет. Английский оригинал тех же задач целиком доступен под MIT в sources/math-prm800k.

**Ограничения.** Отдельная лицензия на русский перевод не подтверждена — лицензия MIT исходного MATH на перевод не распространяется. Полный корпус не скачивается, не сохраняется и не пересобирается через любой предусмотренный путь. huggingface.co из окружения напрямую недоступен (ошибка TLS). Условия корпуса содержат служебную разметку [asy], рисунки не выводятся. Индекс не является набором решаемых задач: ни условий, ни ответов, ни разборов в нём нет.

| файл | строк |
|---|---:|
| `sources/math-500-ru/items/index.jsonl` | 500 |

### `math-prm800k`

**MATH (12 500 задач) и PRM800K — пошаговые метки, нормализатор ответов**

* адрес: <https://github.com/openai/prm800k>
* upstream: <https://github.com/openai/prm800k>, коммит `7ecc794703b2`
* лицензия: MIT (<https://github.com/openai/prm800k/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: MATH dataset (Dan Hendrycks et al.) и PRM800K (OpenAI), MIT License.

**Назначение.** Ядро банка задач: 12 500 задач с ответами и решениями, уровни 1–5 по предметам, пошаговые метки человеческих и модельных решений, нормализатор ответов для автопроверки. Основа для Immediate mastery, Transfer и Error diagnosis.

**Ограничения.** Задачи на английском. MATH — соревновательные задачи (AMC/AIME-уровень и выше), начальный уровень (арифметика, дроби) покрыт слабо: для ступеней 1–2 нужны другие источники. train-сплит PRM800K (456 МБ) не включён — разметка шагов приведена только для test.

| файл | строк |
|---|---:|
| `sources/math-prm800k/items/math-dataset.jsonl` | 12500 |
| `sources/math-prm800k/items/prm-phase1-steps.jsonl` | 1055 |
| `sources/math-prm800k/items/prm-phase2-test.jsonl` | 2762 |

### `mathforces`

**Mathforces — 275 олимпиадных задач с подсказками и рейтингом MOHS**

* адрес: <https://github.com/ervin-macic/mathforces>
* upstream: <https://github.com/ervin-macic/mathforces>, коммит `b068b4468c08`
* лицензия: не указана (файла лицензии нет; условия ссылаются на AoPS — права третьих лиц) (<https://github.com/ervin-macic/mathforces>)
* права в репозитории: только оглавление
* статусы: доступность `reachable`, загрузка `metadata_only`, запуск `not_executed`, проверка строк `schema_validated`, права `unclear`
* язык: en | ступени: 5, 6, 7 | забрано: 2026-10-20
* атрибуция: Mathforces by ervin-macic; условия — Art of Problem Solving. Тексты не копируются.

**Назначение.** Оглавление 275 задач с темой, оценкой сложности по шкале MOHS, числом подсказок и ссылкой на источник. Полезно как карта сложности олимпиадных задач и как образец дизайна подсказок (три ступени: широкая → сильная → почти решение).

**Ограничения.** Условия, подсказки и решения не копируются. Задачи взяты с AoPS, поэтому распространять их нельзя. Подсказки в upstream сгенерированы моделью Gemini, то есть требуют вычитки человеком.

| файл | строк |
|---|---:|
| `sources/mathforces/items/problems-index.jsonl` | 275 |

### `minif2f`

**miniF2F — 244 задачи в неформальной постановке и на Lean 4**

* адрес: <https://github.com/yangky11/miniF2F>
* upstream: <https://github.com/yangky11/miniF2F>, коммит `c605019c4ebf`
* лицензия: MIT (<https://github.com/yangky11/miniF2F/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 6, 7 | забрано: 2026-10-20
* атрибуция: miniF2F — 244 задачи в неформальной постановке и на Lean 4

**Назначение.** Мост «задача → формальное утверждение»: 244 неформальных условия с неформальным доказательством и ссылкой на формализацию Lean 4. Источник для блока доказательств и для проверки, что агент доводит задачу до формы.

**Ограничения.** Только английский, верхний уровень (AIME/IMO-уровень). Формальные файлы `.lean` не копируются — в каталоге только ссылка и путь. В репозитории 488 записей: 244 в `valid` и 244 в `test`; заявленное «244» относится к одному сплиту.

| файл | строк |
|---|---:|
| `sources/minif2f/items/minif2f.jsonl` | 488 |

### `national-olympiads-bank`

**Pythagoras — банк задач национальных олимпиад: публикация заблокирована по лицензии**

* адрес: <https://github.com/Eisatopon/national-olympiads-bank>
* upstream: <https://github.com/Eisatopon/national-olympiads-bank>, коммит `53864f5760aa`
* лицензия: All rights reserved — копирование, зеркалирование и перепубликация запрещены без письменного разрешения; отдельно запрещено создание другого банка/датасета и использование для обучения и оценки машинных систем (<https://github.com/Eisatopon/national-olympiads-bank/blob/main/LICENSE>)
* права в репозитории: **не публикуется** (права)
* статусы: доступность `blocked_rights`, загрузка `not_downloaded`, запуск `not_executed`, проверка строк `not_audited`, права `restricted`
* лицензионный gate: `blocked_pending_written_permission` — Upstream LICENSE прямо запрещает копирование, зеркалирование и перепубликацию файлов данных, создание другого банка/датасета на их основе и использование для обучения и оценки машинных систем.
* язык: en | ступени: 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: World Mathematical Olympiads Bank (Pythagoras), © Sokratis Romanidis (eisatopon.gr). Условия задач принадлежат организаторам соответствующих соревнований. Никакой материал этого источника в репозитории не публикуется.

**Назначение.** Источник заблокирован: лицензия запрещает создание другого банка задач на основе этих данных. В репозитории нет ни индекса, ни загрузчика. Запись в каталоге существует только как предупреждение для будущего интегратора.

**Ограничения.** Публикация любых производных данных (индекса, оглавления, счётчиков, списка соревнований) запрещена лицензией без письменного разрешения. Условия задач дополнительно принадлежат организаторам соревнований (AMC, AIME и др. — MAA), и отдельной лицензии на них нет. Источник недоступен для проверки содержимого без разрешения; в репозитории не осталось ни одной записи его данных.

| файл | строк |
|---|---:|

### `py-irt`

**py-irt — оценивание параметров IRT и многомерного IRT**

* адрес: <https://github.com/nd-ball/py-irt>
* upstream: <https://github.com/nd-ball/py-irt>, коммит `6514928ec753`
* лицензия: MIT (<https://github.com/nd-ball/py-irt/blob/master/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: py-irt contributors (форк nd-ball/py-irt), MIT License.

**Назначение.** 16 модулей: 1PL/2PL/3PL IRT, многомерный MIRT, обработка anchor-вопросов, экспорт для CAT. Техническая опора для адаптивного тестирования.

**Ограничения.** Оригинальный `ets/py-irt` в этом окружении недоступен (404); взят поддерживаемый форк с той же лицензией MIT. Требует Python ≥3.9 и numpy/scipy.

| файл | строк |
|---|---:|
| `sources/py-irt/items/modules.jsonl` | 16 |

### `pyedmine`

**pyedmine — алгоритмы отслеживания усвоения и когнитивной диагностики**

* адрес: <https://github.com/ZhijieXiong/pyedmine>
* upstream: <https://github.com/ZhijieXiong/pyedmine>, коммит `20af7967486e`
* лицензия: MIT (<https://github.com/ZhijieXiong/pyedmine/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: pyedmine contributors, MIT License.

**Назначение.** 116 модулей: алгоритмы KT и CDM на чистом Python, с примерами и конфигами. Более лёгкая (без torch) альтернатива pyKT для одиночного ученика.

**Ограничения.** Состояние и API отличаются от pyKT; выбирать надо одно. Часть модулей требует numpy/pandas.

| файл | строк |
|---|---:|
| `sources/pyedmine/items/models.jsonl` | 116 |

### `pykt`

**pyKT — библиотека отслеживания усвоения (knowledge tracing)**

* адрес: <https://github.com/pykt-team/pykt-toolkit>
* upstream: <https://github.com/pykt-team/pykt-toolkit>, коммит `ccbaf37b07e3`
* лицензия: MIT (<https://github.com/pykt-team/pykt-toolkit/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: pyKT toolkit contributors, MIT License.

**Назначение.** 94 модуля моделей отслеживания усвоения (DKT, AKT, SAKT, SAINT, …) с готовыми форматами данных. Отвечает на вопрос «что ученик уже умеет, а что ещё нет» по истории ответов.

**Ограничения.** Глубокое обучение, тяжёлые зависимости (torch), формат данных — собственный (skill/question id). Для одного ученика избыточно; в MATH_PRO своё состояние в `mathpro/progress/store.py`.

| файл | строк |
|---|---:|
| `sources/pykt/items/models.jsonl` | 94 |

### `pypsy`

**pypsy — психометрика: IRT, MIRT, CFA, CTT, GRM, DINA**

* адрес: <https://github.com/inuyasha2012/pypsy>
* upstream: <https://github.com/inuyasha2012/pypsy>, коммит `f055fe1f4901`
* лицензия: MIT (<https://github.com/inuyasha2012/pypsy/blob/master/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6, 7 | забрано: 2026-10-20
* атрибуция: pypsy contributors, MIT License.

**Назначение.** 18 модулей плюс 10 демо-скриптов (irt, mirt, cfa, ctt, grm, dina, mcmc_dina). Позволяет проверить на собственных данных, что адаптивная выдача не хуже фиксированной — до того, как внедрять адаптивность.

**Ограничения.** Старый API, последний коммит — 2020 год. Для воспроизводимости в тестах лучше py-irt; pypsy полезен как эталон и как демо.

| файл | строк |
|---|---:|
| `sources/pypsy/items/models.jsonl` | 18 |

### `sympy-books`

**sympy-books — учебники по математике с решениями на SymPy**

* адрес: <https://github.com/dariober/sympy-books>
* upstream: <https://github.com/dariober/sympy-books>, коммит `ca1e9d37385a`
* лицензия: MIT (<https://github.com/dariober/sympy-books/blob/master/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 4, 5, 6 | забрано: 2026-10-20
* атрибуция: sympy-books by Diego. Alvarez, MIT License.

**Назначение.** Мост «математика → Python»: 8 разделов из книг по R, доверительным интервалам, линейной алгебре и оптимизации, с кодом SymPy рядом с теорией.

**Ограничения.** Всего 8 разделов — это демонстрация подхода, а не полноценный курс. Репозиторий не обновлялся с 2020 года. Английский, R и SymPy.

| файл | строк |
|---|---:|
| `sources/sympy-books/items/chapters.jsonl` | 8 |

### `thealgorithms-python`

**TheAlgorithms/Python — 1 287 реализаций алгоритмов**

* адрес: <https://github.com/TheAlgorithms/Python>
* upstream: <https://github.com/TheAlgorithms/Python>, коммит `6e03a48579ca`
* лицензия: MIT (<https://github.com/TheAlgorithms/Python/blob/master/LICENSE.md>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4, 5, 6 | забрано: 2026-10-20
* атрибуция: TheAlgorithms/Python contributors, MIT License.

**Назначение.** Карта вычислительных приёмов на Python: арифметика, комбинаторика, теория чисел, геометрия, сортировки, графы, динамика. У каждой записи — docstring и список функций, то есть быстрый поиск «какая функция решает класс задач».

**Ограничения.** Это справочник, а не курс: нет объяснений, нет задач для ученика, часть кода — для иллюстрации, а не для продакшна. Английский.

| файл | строк |
|---|---:|
| `sources/thealgorithms-python/items/algorithms.jsonl` | 1287 |

### `treecut-math`

**TreeCut — текстовые задачи, в том числе нерешаемые**

* адрес: <https://github.com/j-bagel/treecut-math>
* upstream: <https://github.com/j-bagel/treecut-math>, коммит `b48f3de5586d`
* лицензия: Apache-2.0 (<https://github.com/j-bagel/treecut-math/blob/main/LICENSE>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* язык: en | ступени: 3, 4 | забрано: 2026-10-20
* атрибуция: TreeCut (Jialin Ouyang et al.), Apache-2.0.

**Назначение.** 4 000 задач (2 000 решаемых / 2 000 нерешаемых). Нерешаемая версия получается вырезанием необходимого условия. Проверка на «задача не имеет ответа» — обязательный блок Error diagnosis: агент не должен домысливать ответ.

**Ограничения.** Только простые арифметико-алгебраические сюжеты (рестораны, товары). Полный набор (~21 000) лежит на Hugging Face и в этом репозитории его нет.

| файл | строк |
|---|---:|
| `sources/treecut-math/items/treecut.jsonl` | 4000 |

### `ultimate-aptitude`

**Ultimate Aptitude — банк вопросов способностей (CC BY 4.0)**

* адрес: <https://github.com/atmamoon/ultimate-aptitude>
* upstream: <https://github.com/atmamoon/ultimate-aptitude>, коммит `62437a1fc428`
* лицензия: CC-BY-4.0 (<https://github.com/atmamoon/ultimate-aptitude/blob/main/banks/LICENSE.md>)
* права в репозитории: полная
* статусы: доступность `reachable`, загрузка `downloaded`, запуск `not_executed`, проверка строк `schema_validated`, права `permissive`
* overlay качества: `ultimate-aptitude-quality`
* язык: en | ступени: 4, 5, 6 | забрано: 2026-10-20
* атрибуция: Questions from Ultimate Aptitude by Mamoon Mondal, licensed under CC BY 4.0.

**Назначение.** 1 098 авторских вопросов с разбором: квант, логика, достаточность данных, анализ данных, вербальные. Измеряет способности и устойчивость к уловкам формата, а не знание предмета — отдельный контур от «знаниевой» диагностики.

**Ограничения.** Смещение сложности: 572 «hard» и 522 «very-hard», «medium» всего 4 — входная диагностика на этом банке невозможна, нужен другой источник. Тексты — в стиле GMAT/CAT, но не из официальных экзаменов. Ещё 1 000+ procedural-вопросов генерируются кодом `js/generators.js` — код не копировался.

| файл | строк |
|---|---:|
| `sources/ultimate-aptitude/items/questions.jsonl` | 1098 |

## Как это читать

* **Полная перепубликация** — тексты источника можно свободно
  распространять при сохранении лицензии и атрибуции: они лежат в
  `items/` и пригодны для сборки тем.
* **Только оглавление** — права неясны или прямо запрещают копирование.
  В `items/` лежат метаданные (домен, сложность, число вариантов,
  ссылки), но не условия и не разборы; каждая запись помечена
  `metadata_only: true`. Полный материал остаётся в
  upstream-репозитории и в локальном кеше `sources/_cache/`.
* **Не публикуется** — лицензия прямо запрещает копирование. В папке
  остались только паспорт и уведомление о запрете.
* **Overlay качества** (`overlays/`) — отпечатки содержимого и найденные
  дефекты: структурная проверка говорит «поля верны», а overlay —
  «ответ верен» или «объяснение неполно».

Проверка: `python math_repo_education/tools/verify_catalog.py` → 0 ошибок.
