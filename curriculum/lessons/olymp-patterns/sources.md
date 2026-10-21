# Источники

Примечание ревьюера V7: внешние страницы CK-12 ниже повторно не проверены
(доступ к этим доменам в среде ревью отсутствует). Библиография, описания влияния
и сведения о лицензии унаследованы от авторов; сведения о конкретных изданиях
и годах — **по памяти**, требуют сверки с первоисточником. Годы не выдумывались.

Пакет `olymp-patterns` — оригинальное изложение, написанное для этой темы.
Тексты источников не копировались: взяты идеи, структуры заданий и числа
примеров, переработанные под язык счёта (тема идёт в дереве раньше тем
сложения и вычитания, поэтому в теории нет знаков действий — шаг измеряют
счётом вслух).

1. CK-12 Foundation. «Train Cars» (Algebra Explorations, Pre-K through
   Grade 7, раздел 1.3), `ck12:ck12-ae-prek-7-s01-03`.
   http://www.ck12.org/book/Algebra-Explorations-Pre-K-through-Grade-7/section/1.3/
   Взята идея повторяющейся группы элементов (в источнике — цвета вагонов
   по буквам B/R/Y) и приём «назови вслух, чтобы проверить». Переработано
   в T01: наблюдение группы, её длина и продолжение с начала группы.
2. CK-12 Foundation. «Peculiar Patterns» (Algebra Explorations, Pre-K
   through Grade 7, раздел 2.7), `ck12:ck12-ae-prek-7-s02-07`.
   http://www.ck12.org/book/Algebra-Explorations-Pre-K-through-Grade-7/section/2.7/
   Взяты растущие строки букв и рамочные узоры (T…T). Переработано в T04:
   правило, описывающее рост строки, и сверка формулировки со строкой.
3. CK-12 Foundation. «Stars and Moons» (Algebra Explorations, Pre-K
   through Grade 7, раздел 3.9), `ck12:ck12-ae-prek-7-s03-09`.
   http://www.ck12.org/book/Algebra-Explorations-Pre-K-through-Grade-7/section/3.9/
   Взята модель двух независимо растущих признаков (звёзды и луны:
   2+1, 3+2, 4+3) и сверка «луны — столько, сколько номер карточки».
   Переработано в T02 (пример 3) и в предупреждении T03 про один
   проверенный признак из двух.
4. CK-12 Foundation. «GEO Patterns» (Algebra Explorations, Pre-K through
   Grade 7, раздел 4.8), `ck12:ck12-ae-prek-7-s04-08`.
   http://www.ck12.org/book/Algebra-Explorations-Pre-K-through-Grade-7/section/4.8/
   Взята структура «три признака на карточках, продолжить и ответить о
   10-й карточке». Переработано в T04 (пример 2: прогноз по номеру места).
5. CK-12 Foundation. «Peculiar Patterns» (Algebra Explorations Concepts,
   раздел 2.6), `ck12:ck12-ae-concepts-s02-06`.
   http://www.ck12.org/book/Algebra-Explorations-Concepts-Pre-K-through-Grade-7/section/2.6/
   Взят цикл «описать — задача — план — решить — проверить». Переработан
   в T04 как виджет stepper из четырёх шагов работы с рядом.
6. CK-12 Foundation. «Stars and Moons» (Algebra Explorations Concepts,
   раздел 3.6), `ck12:ck12-ae-concepts-s03-06`.
   http://www.ck12.org/book/Algebra-Explorations-Concepts-Pre-K-through-Grade-7/section/3.6/
   Взята явная сверка правила с данными карточек и формулировка проверки
   («луны — столько, сколько номер карточки»). Переработано в T03: проверка
   догадки на каждом показанном переходе.
7. CK-12 Foundation. «GEO Patterns» (Algebra Explorations Concepts,
   раздел 4.7), `ck12:ck12-ae-concepts-s04-07`.
   http://www.ck12.org/book/Algebra-Explorations-Concepts-Pre-K-through-Grade-7/section/4.7/
   Взят приём отдельного счёта каждого признака и проверка правила на
   всех показанных карточках. Переработано в T03 (пример 3 — перенос
   в контекст журнала заявок) и T04.
8. CK-12 Foundation. «Growing Patterns» (Algebra Explorations Concepts,
   раздел 7.7), `ck12:ck12-ae-concepts-s07-07`.
   http://www.ck12.org/book/Algebra-Explorations-Concepts-Pre-K-through-Grade-7/section/7.7/
   Взяты растущие узоры из плиток и сводка «число = номер фигуры и ещё
   несколько» (в источнике — таблица и правила вида «на 2 больше номера»).
   Переработано в T04 (пример 2) и в таблице T03 «наблюдение — прогноз».

Лицензия и атрибуция: CK-12 FlexBooks, Pre-K through Grade 7 (Algebra
Explorations и Algebra Explorations Concepts), CK-12 Foundation,
лицензия CC BY-NC 3.0 (выгрузка досовременных изданий через зеркало
LiaBooks; сведения о лицензии — в sources/ck12/SOURCE.yaml, retrieved
2026-10-13). Переработка выполнена автором темы; дословного копирования
нет, короткие определения («правило», «закономерность») даны своими
словами.

9. Команда MATH_PRO. «Дерево программы: тема `olymp-patterns` и её
   пререквизит `num-counting`». 2026. [tree.yaml](../../tree.yaml).
   Взяты название, ступень, часы, класс-ориентир, пререквизит и дословный
   список подтем; формулировки теории авторские.
10. Команда MATH_PRO. «Сводка ревью раздела olymp», `mapping/olymp.yaml`
    и `mapping/REVIEW-olymp.md`. 2026. Использован список уроков
    (coverage: full); ревью убрало урок 7 класса «Describing Patterns»,
    урок Eureka Math про закономерности умножения и разделы Mathigon про
    прогрессии — как выходящие за scope и пререквизиты темы. Задачи
    `eureka-math:g3-m3-l13-pr-3` и `eureka-math:g3-m3-l13-et-2` из mapping
    не использовались: это материал для банков задач, не для теории.
11. Команда MATH_PRO. «Стандарт учебного контента MATH_PRO, версия 1.2».
    2026. [STANDARD.md](../../STANDARD.md). Требования к составу пакета,
    виджетам, подсказкам, разборам и бюджетам режимов.
12. Записи каталога ошибок с префиксом `E-olymp-patterns-…` — авторские
    (в research/tasks/REVIEW.md строк для ступени 1 и раздела olymp нет);
    механизмы подобраны автором и проверены вычислением на диагностических
    параметрах. Частота ошибок у учащихся не исследовалась.
