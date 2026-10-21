# Источники

Пакет `num-mental-arithmetic` собран из открытых уроков и задач, перечисленных в `mapping/num.yaml`.
Тексты источников не копировались: идеи, модели и типы задач пересказаны по-русски для взрослого
новичка, числа и сюжеты заменены, все ответы пересчитаны заново (`verify.py`). Ученику источники не
нужны — тема самодостаточна. Ниже по строке на каждый использованный урок и набор задач:
`<источник>:<id> — что взято, как переработано`.

## Уроки

- `im-k5:im-g1-u4-l12` «Mentally Add and Subtract Tens» — наблюдение, что прибавление и вычитание
  целых десятков сохраняет цифру единиц (а без перехода через сотню меняет десятки); стало опорой
  прибавления по частям в T02 (58 + 20 = 78) и задачи P-02. Детская игра «Write Numbers» не использована.
  https://im.kendallhunt.com/k5/teachers/grade-1/unit-4/lesson-12/preparation.html
- `im-k5:im-g1-u5-l3` «Add It, Explain It» — два маршрута одной суммы (к первому числу сначала
  десятки, потом единицы; десятки с десятками, единицы с единицами) и запись шагов равенствами; в T02
  первый маршрут — основной, второй — во врезке `:::deep`; запись цепочкой легла в обратную задачу P-10.
  https://im.kendallhunt.com/k5/teachers/grade-1/unit-5/lesson-3/preparation.html
- `im-k5:im-g2-u2-l15` «Does My Estimation Make Sense?» — прикидка до точного счёта и проверка
  оценки по смыслу действия («при вычитании не может стать больше»); пересказано в T03 и в части
  «Неправдоподобный ответ» T04, семена заменены покупками и складом.
  https://im.kendallhunt.com/k5/teachers/grade-2/unit-2/lesson-15/preparation.html
- `im-k5:im-g4-u6-l25` «Assess the Reasonableness of Solutions» — сравнение одного числа с суммой
  нескольких по оценкам (данные переписи о языках заменены условными залами и местами: P-25, EB-15) и
  проверка правдоподобия результата. В ответе источника к cool-down две разные записи одного числа —
  345 589 и 345 599; пересчёт 107 736 + 184 323 + 53 530 = 345 589, вторая запись — опечатка источника.
  https://im.kendallhunt.com/k5/teachers/grade-4/unit-6/lesson-25/preparation.html
- `im-k5:im-g3-u3-l3` «Add Your Way» — сложение по разрядам, рассуждение через близкую сотню и вывод,
  что порядок разрядов на сумму не влияет; в T01–T02 (компенсация, прибавление по частям) и во врезке
  `:::deep` T02.
  https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-3/preparation.html
- `im-k5:im-g3-u3-l7` «Subtract Your Way» — вычитание по разрядам, счёт вверх и компенсация при
  вычитании («вычел 400 вместо 398 и вернул 2»); переработано в компенсацию при вычитании T01
  (82 − 29, 134 − 98) и счёт вверх T02.
  https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-7/preparation.html
- `im-k5:im-g3-u3-l12` «Subtract Strategically» — выбор приёма по числам: 382 − 190 (вычесть 200,
  вернуть 10), 600 − 478 (счёт вверх), 700 − 599; пример 4 T02 и пример 1 T05, таблица выбора приёма
  в T05, задачи P-22, EA-14, EB-14.
  https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-12/preparation.html
- `im-k5:im-g3-u3-l17` «Does It Make Sense?» — «больше ли 400?» без точного счёта и задача о бусинах
  (124 + 96 − 53 и неправдоподобный ответ 273); пример 3 T04, запись каталога
  `E-num-mental-arithmetic-add-instead`, задачи P-18, EA-12, EB-12 с новыми сюжетами.
  https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-17/preparation.html
- `eureka-math:g3-m2-l17` — прикидка суммы до десятков, сотен и полусотен (362 + 159) и три суммы
  349 + 145, 352 + 145, 352 + 151 с прикидками 400, 500, 600; пример 1 T03 и раздел T06 целиком
  (почему прикидка до сотен промахивается, выбор разряда).
  https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_2/g3_m2_teacher_edition_v1_3_0.pdf#page=207
- `eureka-math:g3-m2-l20` — прикидка разности (362 − 189), направления округления у разности
  (349 − 154, 349 − 149, 351 − 154, 351 − 149) и сдвиг обоих чисел 532 − 198 = 534 − 200; у источника это
  наблюдение «так ближе», здесь — правило оценок сверху и снизу с моделью «разность — длина отрезка»
  (T03), сдвиг (T05) и пример 2 T06.
  https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_2/g3_m2_teacher_edition_v1_3_0.pdf#page=243
- `eureka-math:g3-m2-l21` — порядок «прикинь → посчитай → сравни» (71 − 23 ≈ 70 − 20); стал схемой
  T03 и частью разборов P-11, P-12, P-15.
  https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_2/g3_m2_teacher_edition_v1_3_0.pdf#page=257

## Наборы задач

- `eureka-math:g3-m2-l20-spa-2`, `-spa-9`, `-spa-10` (Sprint A: 301, 290, 390 до сотен) — тренажёр
  округления до сотен; переработан в диагностическую задачу D-03 с другим числом.
  https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_2/g3_m2_addtnl_matrls_v1_3_0.pdf#page=7
- `eureka-math:g3-m2-l20-ho-1`, `-ho-2` (87 − 59 км, 393 − 184 см: оцени, посчитай, правдоподобно ли) —
  форма «оценка до точного счёта» для разностей; новые числа в P-12, P-15, в промежутке на луче T03.
  https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_2/g3_m2_student_wkbook_v1_3_0.pdf#page=84
- `ck12:ck12-msm-g6-s01-02-p09` … `-p14` (Time to Practice: 45 + 62, 32 + 45, 21 + 54, 103 + 87,
  101 + 92, 342 + 509) — суммы для прикидки, в выгрузке без ответов; взята форма задания, числа
  заменены, ответы посчитаны заново (P-11, R-04, EA-03, EB-03).
  http://www.ck12.org/book/CK-12-Middle-School-Math-Grade-6/section/1.2/
- `im-k5:im1-1-u3-b-p4-d`, `im1-1-u3-c-p3-a`, `im1-1-u3-c-p5-c`, `im1-2-u2-b-p1-a` (13 + 5, 9 + 6,
  8 + 7, 60 − 5) — «дополни до десятка» и вычитание через круглое число; для взрослого укрупнены до
  38 + 7, 63 − 8 (T01) и задачи P-01.
  https://im.kendallhunt.com/k5/teachers/grade-1/unit-3/practice.html
  https://im.kendallhunt.com/k5/teachers/grade-2/unit-2/practice.html
- `openstax-prealgebra:m81244--fs-id1369108` «Elevators» (лимит 1150 фунтов, шесть человек) — сумма
  против лимита; переработано в лифт на 500 кг с условными весами (hook и пример 4 T05) и задачу P-23,
  где запас оценивается сверху без точного сложения.
  https://github.com/openstax/osbooks-prealgebra-bundle/blob/38cae454e644abf9f0a623e876994553881597c9/modules/m81244/index.cnxml#L1709
- `openstax-prealgebra:m81245--fs-id1948833` (38 − 16, вычесть и проверить сложением) — проверка
  вычитания сложением; таблица правил проверки в T04, задачи P-13, R-05, EA-04.
  https://github.com/openstax/osbooks-prealgebra-bundle/blob/38cae454e644abf9f0a623e876994553881597c9/modules/m81245/index.cnxml#L1091

Не использованы `ck12:ck12-msm-g6-s01-02-p07` и `-p08` (прикидка частного 122 : 4 и 120 : 11): деление
не входит в тему.

## Атрибуция и лицензии

- **im-k5.** Based on IM® TK–12 Math v.360 by Illustrative Mathematics®, licensed under CC BY-NC 4.0
  (учительские гайды, © 2024, колонтитул «CC BY NC 2024»); задачи практики — © 2021 Illustrative
  Mathematics, CC BY 4.0, через зеркало hyetigran/math_on_mars. Не является продуктом или одобрением
  Illustrative Mathematics. Страница курса: https://im.kendallhunt.com/k5/curriculum.html
- **eureka-math.** Eureka Math™, Grade 3, «A Story of Units», модули 1–7 (v1.3.0–1.3.1, 2015–2019).
  © 2015 Great Minds; EngageNY Mathematics Curriculum, New York State Education Department.
  Non-commercial use is licensed pursuant to a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
  license. PDF получены через публичное зеркало GitHub sanjayjaiswar/ruchi-grade3. Архив NYSED:
  https://www.nysed.gov/curriculum-instruction/engageny-mathematics-curriculum-files-archive
- **ck12.** CK-12 Foundation, «CK-12 Middle School Math — Grade 6», издание до 16.02.2021 из зеркала
  LiaBooks, лицензия CC BY-NC 3.0 (`sources/ck12/SOURCE.yaml`: поля `attribution` в паспорте нет,
  строка собрана из `notes` и `books`).
- **openstax-prealgebra.** Prealgebra 2e by Lynn Marecek, MaryAnne Anthony-Smith, Andrea Honeycutt Mathis
  and the credited contributors; OpenStax, Rice University. CC BY-NC-SA 4.0. No endorsement by OpenStax is
  implied. Книга: https://openstax.org/details/books/prealgebra-2e

Материалы под CC BY-NC и CC BY-NC-SA используются некоммерчески, с указанием авторства. Изменения:
перевод на русский и пересказ своими словами, новые числа и сюжеты, ответы пересчитаны, добавлены
оценки разности сверху и снизу, сдвиг обоих чисел, решения «уложимся ли в лимит» по оценкам, обратные
задачи и параметрические варианты. Условие ShareAlike лицензий eureka-math и openstax-prealgebra
относится и к переработанным фрагментам; какой лицензией помечать пакет целиком — вопрос мейнтейнеру
(вынесен в PR).

## Каталог ошибок

Двенадцать записей `E-num-mental-arithmetic-…` в конце `errors/catalog.yaml` — авторские гипотезы
механизмов: верные рассуждения взяты из перечисленных уроков, неверные восстановлены автором и проверены
вычислением; частота этих ошибок у учащихся не исследовалась.
