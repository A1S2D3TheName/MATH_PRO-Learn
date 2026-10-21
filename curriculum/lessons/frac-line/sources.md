# Источники

Тема собрана по открытым урокам и задачам из `mapping/frac.yaml` (запись `frac-line`) и одному
дополнительному уроку, найденному поиском `tools/search_items.py`. Тексты источников не
копировались: идеи, модели и типы задач пересказаны по-русски и перестроены под взрослого ученика,
который учится сам; все числа, контексты и формулировки задач заменены, каждый ответ пересчитан
в `verify.py`. Ниже — что взято из каждой единицы и как переработано, затем атрибуция и лицензии.

## Уроки

1. im-k5:im-g3-u5-l5 — «To the Number Line»,
   <https://im.kendallhunt.com/k5/teachers/grade-3/unit-5/lesson-5/preparation.html>.
   Взято: переход от полоски к числовой прямой; подпись дроби ставится у точки в конце части,
   а не в середине промежутка (спор Андре и Клэр); делить нужно отрезок от 0 до 1, а не всю
   полоску бумаги. Переработано: T01 (полоска лежит вдоль единичного отрезка), T02 («дробь —
   одновременно расстояние и место»), виджет-полоска T02.
2. im-k5:im-g3-u5-l6 — «Locate Unit Fractions on the Number Line»,
   <https://im.kendallhunt.com/k5/teachers/grade-3/unit-5/lesson-6/preparation.html>.
   Взято: две ошибки разметки — четыре штриха вместо трёх (получается пять частей) и деление
   на четверти всей нарисованной прямой; место числа не меняется, если прямую продлить.
   Переработано: заметки-предупреждения T01, записи каталога `E-frac-line-marks-as-parts`,
   `E-frac-line-whole-picture`, `E-frac-line-count-zero-tick`, задачи P-03, P-05–P-07.
3. im-k5:im-g3-u5-l7 — «Non-unit Fractions on the Number Line»,
   <https://im.kendallhunt.com/k5/teachers/grade-3/unit-5/lesson-7/preparation.html>.
   Взято: счёт четвертями до шестнадцати четвертей, отметка дробей меньше и больше единицы
   на одной прямой, чтение отмеченной дроби по немаркированным штрихам. Переработано: счёт по
   долям в T02 и его продолжение за единицу в T03; группы по знаменателю в T04; задачи P-04, P-08.
4. im-k5:im-g3-u5-l8 — «Fractions and Whole Numbers»,
   <https://im.kendallhunt.com/k5/teachers/grade-3/unit-5/lesson-8/preparation.html>.
   Взято: дроби, которые стоят в натуральных точках (каждые две половины, три трети, четыре
   четверти), и поиск единицы по отмеченной единичной дроби. Переработано: T03, пример 1 T05,
   задачи P-09, P-17, P-28.
5. im-k5:im-g3-u5-l9 — «All Kinds of Numbers on the Number Line»,
   <https://im.kendallhunt.com/k5/teachers/grade-3/unit-5/lesson-9/preparation.html>.
   Взято: поиск единицы по неединичной дроби (делить нужно на числитель), поиск дроби с другим
   знаменателем через единицу. Переработано: раздел T05 целиком в клетках тетради вместо
   рисунка, записи `E-frac-line-point-as-unit` и `E-frac-line-split-by-denominator`, задачи
   P-18–P-26 и обратные задачи контрольной.
6. im-k5:im-g3-u5-l13 — «Whole Numbers and Fractions» (дополнительный урок, найден поиском,
   в сопоставлении не используется ни одной темой),
   <https://im.kendallhunt.com/k5/teachers/grade-3/unit-5/lesson-13/preparation.html>.
   Взято: смысл знаменателя 1 («целое не делили, каждая часть длиной в целое»), признак дроби,
   равной натуральному числу (числитель называется при счёте группами по знаменателю), запись
   натурального числа дробью. Переработано: часть T03 о знаменателе 1, таблица-виджет T03,
   задачи P-14, EA-09, EB-09. Уравнения вида «дробь = дробь» из урока не взяты: равенство дробей —
   тема `frac-equivalent`.
7. eureka-math:g3-m5-l14 — «Place fractions on a number line with endpoints 0 and 1»,
   <https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_5/g3_m5_teacher_edition_v1_3_0.pdf#page=168>.
   Взято: единичный отрезок отмеряют полоской-целым, концы подписывают и как 0 и 1, и как
   «ноль долей» и «все доли»; совет делить на четверти и восьмые последовательным делением
   пополам. Переработано: пример 1 T01 (середина, затем середины половин), запись нуля как
   $\frac{0}{5}$ в T02.
8. eureka-math:g3-m5-l15 — «Place any fraction on a number line with endpoints 0 and 1»,
   <https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_5/g3_m5_teacher_edition_v1_3_0.pdf#page=178>.
   Взято: «часть и ещё часть дают целое» — от точки $\frac{3}{5}$ до единицы остаются две пятых.
   Переработано: проверки «до единицы остаётся…» в примерах и разборах, задача P-04 и задачи
   контрольной на смысл (EA-03, EB-03).
9. eureka-math:g3-m5-l16 — «Place whole number fractions and fractions between whole numbers on the number line»,
   <https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_5/g3_m5_teacher_edition_v1_3_0.pdf#page=188>.
   Взято: прямая с концами 1 и 2, 2 и 4 («нуль не исчез, он левее»), подписи такого участка
   начинают с левого конца, записанного долями; дроби в натуральных точках (4/4, 8/4, 12/4).
   Переработано: «окно» луча в T04, примеры 3–4 T04, задачи P-13, P-16, EA-13, EB-13.
10. eureka-math:g3-m5-l17 — «Practice placing various fractions on the number line»,
    <https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_5/g3_m5_teacher_edition_v1_3_0.pdf#page=200>.
    Взято: смешанная отработка дробей меньше и больше единицы на одном луче. Переработано: виджет
    сортировки T04 и смешанные варианты задач P-12, P-15.
11. openstax-prealgebra:m81285--fs-id2784608 — «Locate Fractions and Mixed Numbers on the Number Line»,
    <https://github.com/openstax/osbooks-prealgebra-bundle/blob/38cae454e644abf9f0a623e876994553881597c9/modules/m81285/index.cnxml#L909>.
    Взято: взрослая сводка алгоритма — сначала натуральные точки, отрезок от 0 до 1 делят на
    равные части штрихами, которых на один меньше, чем частей; для дроби больше единицы сначала
    ищут соседние натуральные числа. Не взято: смешанные числа и отрицательные дроби (темы
    `frac-mixed` и `numsys-negative`). Переработано: правило числа штрихов в T01, порядок
    рассуждения в T04.

## Задачи

12. eureka-math:g3-m5-l14-pr-2, l14-pr-3, l14-ho-3 — разметка часа и метровой ленты долями
    (щенка выгуливают каждую четверть часа, бусины через пятую часть метра, грядка секциями по
    девятой части метра). Переработано: часы заменены километрами трассы и указателем топлива
    (время с переводом единиц — не пререквизит темы), числа заменены (P-01, P-07, F-01, F-02).
13. eureka-math:g3-m5-l14-ho-2 — «6 разрезов дают 7 кусков»,
    <https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_5/g3_m5_student_wkbook_v1_3_1.pdf#page=59>.
    Переработано: пример 3 T01 (7 кусков — 6 разрезов), задачи P-02, EA-01, EB-01.
14. eureka-math:g3-m5-l15-pr-3 — верёвка с пятью узлами на равных расстояниях делится на четыре
    части, <https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_5/g3_m5_student_wkbook_v1_3_1.pdf#page=61>.
    Переработано: «отметки, риски и таблички на рейке, индикаторе и трассе» (P-03, EA-06, EB-06).
15. eureka-math:g3-m5-l16-pr-1…pr-4, l16-ho-1…ho-4, l16-et-1, l16-et-2 — разметка прямой от 0
    до 3 на доли с выделением дробей в натуральных точках. Переработано: таблица T03, задачи
    P-09–P-11, P-14, R-03.
16. eureka-math:g3-m5-l17-pr-1…pr-3, l17-ho-1…ho-3 — отметка набора дробей на одной прямой.
    Переработано: смешанные варианты P-06, P-12, P-15, R-04. В выгрузке у этих задач потеряны
    сами дроби (известная потеря при извлечении из PDF, см. mapping/REVIEW-frac.md), поэтому взят
    только тип задачи, числа подобраны заново.

Задачи из уроков IM (активности и Cool-down уроков 5–9 и 13) использованы как образцы типов:
«отметьте 1 по отмеченной дроби», «какая дробь отмечена», «какие дроби стоят в натуральных точках».

## Что написано автором темы

- Раздел T06 «Шаг шкалы, когда подписаны не 0 и 1» и задачи P-24, P-27, R-06, EA-12, EB-12 —
  авторское развитие идеи урока im-g3-u5-l6 о делении всего рисунка вместо единичного отрезка;
  готового урока в сопоставлении нет.
- Задачи на две таблички без нуля (P-23, EA-15, EB-15) и на расстояние до правого соседа (P-25) —
  авторское соединение идей im-g3-u5-l9 и eureka-math:g3-m5-l16.
- Записи каталога `E-frac-line-restart` и `E-frac-line-whole-as-one-part` — гипотезы автора
  (отмечено в поле `source` каталога); частота этих ошибок не исследовалась.

## Атрибуция и лицензии

- **im-k5.** Based on IM® TK–12 Math v.360 by Illustrative Mathematics®, licensed under CC BY-NC 4.0
  (учительские гайды, © 2024); задачи практики — © 2021 Illustrative Mathematics, CC BY 4.0.
  Не является продуктом или одобрением Illustrative Mathematics. Лицензия:
  <https://creativecommons.org/licenses/by-nc/4.0/>.
- **eureka-math.** Eureka Math™, Grade 3, «A Story of Units», модуль 5 (v1.3.0–1.3.1). © 2015 Great Minds;
  EngageNY Mathematics Curriculum, New York State Education Department. Non-commercial use is licensed
  pursuant to a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license:
  <https://creativecommons.org/licenses/by-nc-sa/4.0/>. PDF получены через публичное зеркало GitHub
  sanjayjaiswar/ruchi-grade3.
- **openstax-prealgebra.** Prealgebra 2e by Lynn Marecek, MaryAnne Anthony-Smith, Andrea Honeycutt Mathis
  and the credited contributors; OpenStax, Rice University. CC BY-NC-SA 4.0 (текст лицензии в репозитории:
  <https://github.com/openstax/osbooks-prealgebra-bundle/blob/38cae454e644abf9f0a623e876994553881597c9/LICENSE>).
  No endorsement by OpenStax is implied.

Материалы используются некоммерчески, с указанием авторства. Изменения: перевод на русский язык,
пересказ своими словами, замена контекстов (трасса забега, указатель топлива, рулетка, полоса
загрузки, клетки тетради), замена всех чисел, перестройка порядка в шесть разделов, добавление
разборов, подсказок, откликов и проверок. Адаптация распространяется на тех же условиях
(CC BY-NC-SA 4.0 для частей, основанных на eureka-math и openstax-prealgebra).
