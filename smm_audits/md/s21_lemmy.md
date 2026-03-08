---
id: s21_lemmy
source: s21_lemmy.html
updated: 2026-03-08
---

# Lemmy

> S-21 — Федеративный Reddit на ActivityPub

## 1. Алгоритм и ранжирование контента

### Как работает федерация Lemmy

Lemmy — федеративный link aggregator на ActivityPub (тот же протокол что Mastodon, Pixelfed, PeerTube). Каждый инстанс — независимый сервер, инстансы обмениваются контентом через ActivityPub. Пользователь наprogramming.devможет подписываться, голосовать и комментировать в community наlemmy.world.

### Алгоритмы сортировки

| Алгоритм | Формула/Логика | Стратегия |
| --- | --- | --- |
| Hot(по умолчанию) | log10(score) + (time / 45000)— сильное затухание по времени | Первые 1-2 часа критичны. Вовлечённость в начале решает |
| Active | Учитывает комментарии, не только голоса | Посты-дискуссии. Вопросы. Тезисы, приглашающие к спору |
| Scaled | Нормализация по размеру сообщества | Маленькие нишевые сообщества могут попасть в ленту All |
| New | Чистая хронология | Опытные пользователи просматривают New |
| Top | Чистое количество голосов за период | Цель: Top Week / Top Month для устойчивой видимости |

### Межинстансная видимость

> **Инсайт:** Критический инсайт:Пост в community на lemmy.world → "All" feed КАЖДОГО инстанса, который федерируется с lemmy.world (почти вся сеть). Но в "Local" feed — только на lemmy.world. Посты в community на HOME инстансе получают двойную видимость.

## 2. Форматы контента

### 3 типа постов

| Тип | Описание | Для Tim |
| --- | --- | --- |
| Text Post | Title + body (full Markdown). Для long-form, tutorials, build logs | PRIMARY — "Build in Public" контент |
| Link Post | Title + URL + optional body. Thumbnail из OpenGraph | Шаринг sborka.work статей с UTM |
| Image Post | Title + upload + optional body (1-10MB) | Инфографика, architecture diagrams |

### Markdown поддержка

CommonMark + расширения: headers, bold/italic/strikethrough, code blocks с syntax highlighting, таблицы, blockquotes, spoiler blocks (::: spoiler Title). HTML теги stripped. Нет iframes, JS, custom CSS.

### Communities (аналог subreddits)

Любой user может создать. Hosted на конкретном инстансе, доступны через всю федерацию. Формат:!communityname@instance.domain. Модераторы, rules sidebar, кастомный вид.

### User Profile — стратегия

Display name, bio (Markdown), avatar, banner. Post/comment score публичные. Bio должна сразу коммуницировать "AI agent architect" + ссылки на sborka.work и GitHub.

## 3. Анализ конкурентов и communities

### Уровень 1 — Высокая активность, прямая релевантность

| Сообщество | Инстанс | Подписчики | Релевантность |
| --- | --- | --- | --- |
| !technology | lemmy.world | 60,000+ | Общий tech, часто AI-новости |
| !selfhosted | lemmy.world | 40,000+ | Docker, homelab — идеально для инфры Тима |
| !linux | lemmy.ml | 50,000+ | FOSS-аудитория, ядро демографии |
| !opensource | lemmy.ml | 15,000+ | FOSS-проекты, инструменты |
| !programming | programming.dev | 10,000+ | Фокус на коде, OSS |
| !artificial_intelligence | lemmy.world | 5,000+ | AI-новости, инструменты, этика |
| !machinelearning | lemmy.world | 3,000+ | ML-статьи, инструменты |
| !python | programming.dev | 5,000+ | Стек Тима |

### Уровень 2 — Средняя активность, нишевые

| Сообщество | Инстанс | Подписчики | Угол для Тима |
| --- | --- | --- | --- |
| !privacy | lemmy.ml | 20,000+ | Самохостинг AI |
| !fediverse | lemmy.world | 15,000+ | ActivityPub, федерация |
| !homelab | lemmy.world | 8,000+ | Хард/софт лаборатория |
| !devops | lemmy.world | 3,000+ | Docker, CI/CD |
| !cybersecurity | lemmy.world | 5,000+ | Угол безопасности |

### Архетипы активных пользователей

**** ()

**** ()

**** ()

**** ()

> **Инсайт:** Что работает:Посты «Я построил X» (топ), сравнения/бенчмарки, анонсы FOSS-альтернатив, витрины инфраструктуры.Что НЕ работает:корпоративный PR, ленивые вбросы ссылок, контент за платной стеной, промо замаскированное под дискуссию.

## 4. Стратегия выбора инстансов

| Инстанс | Пользователи | Фокус | Рекомендация |
| --- | --- | --- | --- |
| lemmy.world | 150,000+ | Крупнейший, общий | ОСНОВНОЙ— макс. охват |
| programming.dev | 15,000+ | Программирование/tech | ВТОРИЧНЫЙ— dev-контент |
| tchncs.de | 10,000+ | Фокус на приватности | Уже зарег. — резерв |
| slrpnk.net | 5,000+ | Solarpunk | Уже зарег. — нишевый угол |
| lemmy.ml | 40,000+ | Оригинальный/FOSS | Рассмотреть, низкий приоритет |

> **Инсайт:** Multi-account:В отличие от Reddit, multi-account на разных инстансах — нормально и принято в Lemmy. НО не использовать для upvoting одного контента.

## 5. Культура сообщества

### Анти-Reddit настроение — культурный фактор #1

Большинство пользователей пришли во время Reddit API pricing changes (2023). Exodus был эмоциональным. Корпоративное поведение платформ (ads, algorithm manipulation) — extremely negative.

> **Внимание:** НЕ ДЕЛАТЬ:Сравнивать Lemmy с Reddit негативно. Не приносить Reddit-паттерны (karma farming, reposts, reaction GIFs в серьёзных дискуссиях).

### Ценности FOSS — идеологическая приверженность

- Рекомендация proprietary tools без FOSS альтернатив → pushback
- "Docker + свой VPS" >> "AWS/GCP/Azure"
- Open-sourcing tools генерирует massive goodwill
- Mention Claude/ChatGPT без open alternatives (Llama, Mistral, Ollama) → negative reaction

### Политический/социальный климат

| Аспект | Позиция Lemmy | Как навигировать |
| --- | --- | --- |
| Политика | Левый уклон (особенно lemmy.ml) | Нейтрально, фокус на технологиях |
| Дискурс об AI | Скептичен к хайпу, интересуется технологиями | «AI дополняет людей», не «AI заменяет работу» |
| Приватность | За приватность, за шифрование | Самохостинг, прозрачность |
| Рост | «Growth hacking» = токсичность | Органический, искренний рост |

> **Инсайт:** Позиционирование:"One Brain, Many Agents" на single VPS — воплощение small-web/indie-hacker этоса, который Lemmy users обожают. Это genuine strength, не limitation.

## 6. Tone of Voice

### Прозрачный строитель — основной голос

- "I am building AI agent systems and documenting the process. Here is what Week 3 looked like."
- "Real talk: 4 out of 6 agents failed this week. Here is why."
- "Open question for people running LLMs locally: how do you handle X?"

### Практический педагог — вторичный голос

- "I tested 5 approaches to multi-agent coordination. Detailed results inside."
- "A beginner's guide to running AI agents on a $20/month VPS (with Docker Compose configs)"

### Примеры подачи

| ❌ ПЛОХО | ✅ ХОРОШО |
| --- | --- |
| "I built a revolutionary AI system that runs 8 businesses autonomously!" | "Running 7 AI agents on a single VPS: architecture, costs, and honest failure analysis" |
| "Check out SBORKA — the AI-powered career club!" | "I built an AI-assisted job matching system. Here is the technical architecture and what I learned." |
| "AI is the future and everyone needs to adapt NOW" | "6 months of AI agents in production. Here is what works, what is hype, and what I would change." |

> **Внимание:** Анти-паттерны (минус/жалоба):Маркетинговый/PR-язык, кликбейтные заголовки, самопродвижение без содержания, снисходительный тон, фарминг вовлечённости, кросс-пост одного контента в 10 сообществ одновременно.

## 7. CTA стратегии для sborka.work

### Правило 10 к 1

На каждый 1 self-promotional пост — 10+ non-promotional комментариев/постов. Ключевой тест:"Был бы этот пост заплюсован даже БЕЗ ссылки?"

### Формат UTM

```
sborka.work?utm_source=lemmy&utm_medium=social&utm_campaign=s21_lemmy&utm_content={community}_{date}_{topic}
```

> **Внимание:** Privacy concern:Некоторые users используют link tracker detectors. Mitigation: быть transparent ("Link includes UTM for analytics, clean URL: sborka.work/research/X"). Никогда не использовать link shorteners.

## 8. Стратегия создания сообщества

> **Внимание:** НЕ создавать сообщество сейчас.Сообщество с 1 подписчиком (создатель) — мёртвое на старте. Сначала — репутация в существующих сообществах.

### Таймлайн

| Период | Действие |
| --- | --- |
| Неделя 1-4 | Ноль создания. Только участие в существующих |
| Месяц 2-3 | Оценить: есть ли пробел? «AI-агенты в продакшне» не покрыт? |
| Месяц 3-4 | Если 200+ кармы + узнаваемость → создать сообщество |
| Месяц 4+ | Наполнить качественным контентом, пригласить вовлечённых пользователей |

### Лучшие кандидаты для сообщества (в будущем)

| Сообщество | Инстанс | Жизнеспособность |
| --- | --- | --- |
| !ai_agents | programming.dev | MEDIUM — между !ml (academic) и !chatgpt (consumer) |
| !build_with_ai | lemmy.world | MEDIUM-HIGH — show-and-tell + learning |
| !local_llm | programming.dev | HIGH — strong demand, !selfhosted adjacent |

> **Инсайт:** Сообщество НЕ должно быть о СБОРКЕ.!ai_agents, не!sborka_ai. Польза для бренда = органическая от основателя + самого активного участника.

## 9. Кросс-платформенная интеграция

### ActivityPub ↔ Mastodon

Lemmy communities = Mastodon accounts.!technology@lemmy.world→ followable из Mastodon как@technology@lemmy.world. Replies из Mastodon = comments на Lemmy. Mastodon favorites ≠ Lemmy upvotes.

### RSS-ленты

```
Community: lemmy.world/feeds/c/technology.xml?sort=Active
User:      lemmy.world/feeds/u/timzinin.xml?sort=New
All:       lemmy.world/feeds/all.xml?sort=Active
```

### Lemmy API — интеграция с auto_publisher

```
POST /api/v3/user/login → JWT-токен
POST /api/v3/post → {name, body, community_id, url}
# Лимит: макс 2-3 поста/день (нормы сообщества, не API)
# Авто-постинг дополнительный — основная вовлечённость ВРУЧНУЮ
```

### Карта кросс-платформенного контента

| Источник | → Lemmy? | Как |
| --- | --- | --- |
| Блог sborka.work | ДА | Ссылочный пост + аннотация |
| Статья Dev.to | ДА | Ссылка или расширенный текстовый репост |
| Видео YouTube | ДА | Ссылка + текстовая аннотация/таймкоды |
| Репозиторий GitHub | ДА | Ссылка + техническое описание |
| Пост LinkedIn | ИНОГДА | Переписать без корпоративного тона |
| Telegram | НЕТ | Слишком коротко/неформально |
| Mastodon | НЕТ | Авто-федерация справляется |

## 10. 30-дневный план действий

80+Post karma150+Comment karma9+Постов25+sborka.work clicks

> **Инсайт:** После 30 дней:Месяц 2: увеличить до 4-5 раз/неделю, запустить повторяющиеся серии. Месяц 3: создать своё сообщество если критерии выполнены (200+ кармы, 20+ уникальных собеседников, явный пробел). Цель: 500+ общей кармы, 100+ кликов на sborka.work.


---

## РЕКОМЕНДАЦИЯ: ЛИЧНЫЙ БРЕНД (с адаптацией)

**Приоритет:** LOW-MEDIUM  
**CTA-цель:** GitHub + timzinin.com  

**Обоснование:** Сильнейшая анти-корпоративная культура. FOSS-энтузиасты. Русскоязычный карьерный клуб = мгновенный downvote.

### Конкретные изменения

- sborka.work в CTA — категорически не работает (правило 10:1)
- Позиционирование: 'One Brain, Many Agents на single VPS' — indie-hacker этос
- Контент: self-hosted AI, Docker Compose, open-source модели (Llama, Mistral)
- ОБЯЗАТЕЛЬНО упоминать open-source при упоминании Claude/ChatGPT
- Сообщество: !ai_agents, НЕ !sborka

> *Обновлено: 8 марта 2026 — аудит стратегий (личный бренд vs СБОРКА)*
