# Источники темы frac-notation

Формат: `<источник>:<id> — что взято, как переработано`. Тексты источников дословно
не переносятся: идеи, порядок и модели пересказаны по-русски под взрослого ученика,
все числа задач изменены и перепроверены в `verify.py`.

## Библиографические записи

- Illustrative Mathematics. **IM K–5 Math, Grade 3, Unit 5: Fractions as Numbers**, 2024,
  уроки 2; **Grade 5, Unit 2: Fractions as Quotients and Fraction Multiplication**, 2024,
  уроки 3 и 5. Карточка урока 3.5.2:
  <https://im.kendallhunt.com/k5/teachers/grade-3/unit-5/lesson-2/preparation.html>.
- Great Minds / New York State Education Department. **Eureka Math, Grade 3,
  Module 5: Fractions as Numbers on the Number Line**, редакция 1.3.0, 2015,
  уроки 5–9 и 13. Проверяемая копия модуля:
  <https://github.com/sanjayjaiswar/ruchi-grade3/blob/main/EurekaMath-Sources/Module_5/g3_m5_teacher_edition_v1_3_0.pdf>.
- Lynn Marecek, MaryAnne Anthony-Smith, Andrea Honeycutt Mathis et al. **OpenStax
  Prealgebra 2e, 4.1 Visualize Fractions**, OpenStax / Rice University, 2020.
  Исходный модуль фиксированной ревизии:
  <https://github.com/openstax/osbooks-prealgebra-bundle/blob/38cae454e644abf9f0a623e876994553881597c9/modules/m81285/index.cnxml>.

## Уроки

- im-k5:im-g3-u5-l2 — запись единичной дроби 1/b и именование частей полоски; идея записи
  одной доли через знаменатель переработана в раздел T02 и виджет с полоской.
- im-k5:im-g5-u2-l5 — связь «дробь как результат деления» на ситуации деления поровну;
  переработано в раздел T03: делимое — числитель, делитель — знаменатель.
- im-k5:im-g5-u2-l3 — интерпретация равенства a/b = a ÷ b; использовано как усиление
  раздела T03 (переход в обе стороны: частное ↔ дробь).
- eureka-math:g3-m5-l05 — деление целого на равные части и запись единичной дроби числом;
  модель полоски переработана в разделы T01–T02.
- eureka-math:g3-m5-l06 — сборка неединичных дробей из единичных; переработано в раздел T02
  (дробь a/b как a единичных долей) и задачи на счёт долей.
- eureka-math:g3-m5-l07 — заштрихованная и незаштрихованная часть одного целого;
  переработано в задачи по полоске и финальную цепочку.
- eureka-math:g3-m5-l08 — запись частей целого через числовой лучок (number bond);
  идея пары «взято/всего» переработана в задачи «числитель по рисунку».
- eureka-math:g3-m5-l09 — дроби больше одного целого из единичных долей; переработано
  в пример 3 раздела T01 и задачи на количество больше целого (без термина будущей темы).
- eureka-math:g3-m5-l13 — одна и та же заштрихованная часть получает разные записи
  при разном целом; переработано в пример 3 раздела T02.
- openstax-prealgebra:m81285--fs-id1402015 — краткое правило «числитель/знаменатель»
  раздела 4.1; использовано только как итоговая сводка в разделе T01, не как основа текста.

## Задачи (типы, числа и сюжеты изменены, ответы пересчитаны)

- eureka-math:g3-m5-l07-ho-9, g3-m5-l07-ho-10, g3-m5-l07-ho-11 — типы задач на запись
  заштрихованной части; сюжеты заменены (лента, пирог, торт), числа новые.
- eureka-math:g3-m5-l08-pr-5, g3-m5-l08-pr-6, g3-m5-l08-ho-1, g3-m5-l08-ho-2,
  g3-m5-l08-ho-3, g3-m5-l08-ho-5, g3-m5-l08-et-1 — типы задач «часть целого по рисунку»;
  переработаны в параметрические варианты практики.
- eureka-math:g3-m5-l09-et-1, g3-m5-l09-et-2, g3-m5-l09-et-3 — типы задач на дроби
  больше целого; переработаны, термин будущей темы не используется.
- openstax-prealgebra:m81285--fs-id2179866, m81285--fs-id2388014, m81285--fs-id1363556,
  m81285--fs-id1262704, m81285--fs-id2130641 — задачи на счёт единичных долей и сборку
  целого из долей («fraction circles»); модели заменены полоской, числа новые.

Предупреждение из mapping/REVIEW-frac.md учтено: в выгрузке eureka-math часть inline-дробей
и ответов потеряна при извлечении из PDF, поэтому ответы источников не копировались —
каждый ответ темы пересчитан независимо в `verify.py` (426 проверок).

## Написано автором темы (пробелы источников)

- Русские названия долей и правила чтения дроби вслух (раздел T04, таблица знаменателей
  2–12 и правило для больших знаменателей): в англоязычных источниках чтение есть только
  попутно (halves, thirds), русской таблицы нет — mapping/frac.yaml прямо указывает, что
  автору придётся дописать её самому.
- Раздел T05 «Проверка записи дроби» (проверка размером, обратным счётом долей и чтением):
  в источниках такой сводной проверки записи нет, раздел собран автором из правил T01–T04.

## Лицензии и атрибуция

- IM K–5: Based on IM® TK–12 Math v.360 by Illustrative Mathematics®, licensed under
  CC BY-NC 4.0 (учительские гайды, © 2024); задачи практики — © 2021 Illustrative Mathematics,
  CC BY 4.0. Не является продуктом или одобрением Illustrative Mathematics.
- Eureka Math™, Grade 3, «A Story of Units», модули 1–7 (v1.3.0–1.3.1, 2015–2019).
  © 2015 Great Minds; EngageNY Mathematics Curriculum, New York State Education Department.
  Non-commercial use is licensed pursuant to a Creative Commons
  Attribution-NonCommercial-ShareAlike 4.0 license.
- OpenStax Prealgebra 2e by Lynn Marecek, MaryAnne Anthony-Smith, Andrea Honeycutt Mathis
  and the credited contributors; OpenStax, Rice University. CC BY-NC-SA 4.0.

Материал использован некоммерчески, с указанием авторства; изменения (перевод, перестройка
под стандарт MATH_PRO, новые числа и сюжеты задач) описаны выше построчно.
