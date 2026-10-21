# Педагогическая основа

Короткая выжимка. Полный разбор с проверкой формулировок и ограничениями —
[reference/PEDAGOGY-NOTES.md](reference/PEDAGOGY-NOTES.md) (проверено по живым страницам 2026-10-20/21).

## Источники, на которых стоит протокол

| Источник | Что берём | Где применено |
|---|---|---|
| [Mississippi State AI Hub — сократические тьюторы](https://aihub.msstate.edu/app/news/2026-04-three-professors-ai-tutor) | бот задаёт вопросы вместо ответов, возражает ученику | [TUTOR-PROTOCOL](TUTOR-PROTOCOL.md) §1–2 |
| [ibl.ai — Socratic Mode](https://docs.ibl.ai/student/corefeatures/socraticmode) | формат ответа: 1–3 предложения указания и 2–4 наводящих вопроса; в STEM — «понятие раньше вычисления» (страница переехала, см. заметки) | §3–4 |
| Deepakness — заметки практика сократического тьюторинга (deepakness.com) | практика сократических вопросов (источник приведён по заданию, содержимое здесь не разбиралось) | §4 |
| AI Indigo — «Socratic prompting framework» (aiindigo.com) | рамка сократических промптов (источник приведён по заданию, содержимое здесь не разбиралось) | §3–4 |
| [Khanmigo — AVID Open Access](https://avidopenaccess.org/resource/khanmigo-as-an-ai-personal-tutor-and-assistant/) | тьютор подсказывает, но не даёт ответа | §2, §5 |
| [Retrieval practice](https://www.retrievalpractice.org/why-it-works) / [обзор](https://www.retrievalpractice.org/review) | извлечение из памяти — стратегия **обучения**, не только оценки; разнесённое повторение | [SESSION-CLOSE](SESSION-CLOSE.md) §3, режим `review` |
| [Learning & the Brain — желательные трудности](https://www.learningandthebrain.com/blog/the-downsides-of-desirable-difficulties/) | два критерия: думать труднее **и** суметь справиться; иначе это не польза, а провал | выбор задачи [TUTOR-PROTOCOL §6](TUTOR-PROTOCOL.md) |
| [Оценка ChatGPT/Gemini/DeepSeek по стратегиям обучения (arXiv 2603.26673)](https://arxiv.org/abs/2603.26673) | сравнение ИИ-моделей по стратегиям обучения; детали — в reference/PEDAGOGY-NOTES.md | запреты [TUTOR-PROTOCOL §2](TUTOR-PROTOCOL.md) |

Ссылки на deepakness.com и aiindigo.com даны на уровне сайта и в этом репозитории не перепроверялись; точный адрес arXiv-работы — в `reference/PEDAGOGY-NOTES.md`.

## Что из этого вытекает в правилах

1. **Производительная борьба.** Ученику даётся время и право застрять. Подсказка — только после попытки.
2. **Желательная трудность.** Задача на границе возможностей: не тривиальная, не безнадёжная. Если трудность сломала ученика — проблема в подборе, а не в ученике.
3. **Извлечение вместо пересказа.** Вначале и в конце — вопросы «вспомни/воспроизведи», а не лекция.
4. **Разнесённое повторение.** Интервалы 1 → 3 → 7 → 16 → 35 → 75 дней (из `reference/DIAGNOSTIC-SPEC.md`), см. `learner/review-queue.yaml`.
5. **Метапознание.** Прогноз перед задачей, оценка уверенности, ретро после — и всё это пишется в журнал.
6. **Нет утечки решения.** Лестница подсказок конечна и не включает «покажи решение».
