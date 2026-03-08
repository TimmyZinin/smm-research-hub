---
id: s20_writeas
source: s20_writeas.html
updated: 2026-03-08
---

# Write.as / WriteFreely

> S-20 — Минималистичный блоггинг с ActivityPub федерацией

## 1. Алгоритм и распространение контента

Write.as — фундаментально другая платформа.Нет алгоритмической ленты, нет рекомендательной системы, нет ранжирования по вовлечённости.Контент распространяется через 4 канала:

| Канал | Потенциальный охват | Усилия | Релевантность |
| --- | --- | --- | --- |
| ActivityPub (Fediverse) | 5K-50K на вирусный пост | Низкие (авто) | ВЫСОКИЙ |
| Прямой шаринг (HN, Reddit) | 1K-100K на вирусный пост | Средние | ВЫСОКИЙ |
| RSS подписчики | 10-500 (органический рост) | Нулевые | СРЕДНИЙ |
| read.write.as | 100-1K просмотров | Нулевые | НИЗКИЙ |
| SEO (поисковики) | Варьируется, медленный рост | Средние | СРЕДНИЙ |

> **Инсайт:** Ключевой инсайт:Write.as — это не платформа для обнаружения. Это каноничный источник для длинного контента, который распространяется ЧЕРЕЗ другие каналы (Fediverse, HN, Reddit). Стратегия: POSSE — Publish Own Site, Syndicate Everywhere (публикуй на своём сайте, распространяй везде).

## 2. Форматы контента

### Блог-посты (Collections) — основной формат

Посты привязаны к именованному блогу (collection). Постоянные URL с кастомными slug'ами, редактирование после публикации, федерация через ActivityPub, RSS.

> **Внимание:** Критическое ограничение — изображения:Free план НЕ хостит картинки. Решение: хостить на RUVDS (sborka.work/images/writeas/...) — полный контроль, быстрый сервер, соответствие бренду "own your infrastructure".

### Кастомный CSS (Pro или self-hosted)

Write.as Pro ($9/мес) или self-hosted WriteFreely поддерживают кастомный CSS для brand consistency:

```
body { font-family: 'DM Sans', sans-serif; color: #2C2418; background: #FFFDF7; }
h1, h2, h3 { font-family: 'Playfair Display', serif; }
a { color: #C2573A; }
code, pre { font-family: 'JetBrains Mono', monospace; background: #F5EDE0; }
```

### Write.as API — автоматизация

| Эндпоинт | Метод | Назначение |
| --- | --- | --- |
| /api/collections/{alias}/posts | POST | Публикация в блог |
| /api/posts/{id} | PUT | Обновление поста |
| /api/collections/{alias}/posts | GET | Список постов |
| /api/auth/login | POST | Авторизация (получение токена) |

### Мульти-блог стратегия

| Блог | Назначение | Аудитория |
| --- | --- | --- |
| write.as/timzinin | Основной: «One Brain, Many Agents» | EN — глобальная tech/AI |
| write.as/timzinin-ru | Русский контент, СБОРКА | RU — предприниматели |
| write.as/agent-logs | Публичные логи сборки агентов | EN — deep tech |

> **Инсайт:** Рекомендация: начать с одного блогаwrite.as/timzininдля консолидации аудитории. Разделять только при 100+ подписчиках.

## 3. Анализ конкурентов

На Write.as/WriteFreelyпрактически НИКТОне пишет о multi-agent AI системах. Ниша пуста — огромная возможность.

**** ()

**** ()

**** ()

**** ()

**** ()

**** ()

> **Инсайт:** Анализ пробелов:Верхний правый квадрант (ВЫСОКАЯ техническая глубина + ПРАКТИЧЕСКИЙ строитель) — ПУСТ на Write.as/WriteFreely. Xe Iaso — философский, Drew DeVault — FOSS/политика. Тим = реальные продакшн мультиагентные системы с реальными метриками выручки.

## 4. Культура сообщества

Write.as создан Matt Baer в 2015 с философией:"writing should be about writing, not about metrics."

### Что платформа УДАЛИЛА специально

- Счётчики просмотров (нет публичных view counts)
- Лайки/хлопки/реакции (нет engagement метрик)
- Счётчики подписчиков (нет vanity metrics)
- Комментарии (опционально, выключены по умолчанию)
- Аналитика (нет встроенной на free плане)
- Реклама (нет рекламы, никогда)
- Трекинг (нет third-party trackers, нет cookies)

### Ценности аудитории

| Ценность | Проявление | Последствия для Tim |
| --- | --- | --- |
| Суть важнее показухи | Никто не пишет ради лайков | Подход ПИСАТЕЛЯ, не маркетолога |
| Приватность как функция | Анти-слежка, анти-трекинг | UTM должны быть прозрачными |
| Длинное важнее короткого | 800-2,000 слов норма | Глубокий контент вознаграждается |
| IndieWeb / POSSE | Свой контент, своя платформа | Мульти-платформа = хорошо, если правильно подано |
| Медленные медиа | 1-3 поста/неделю максимум | Качество, не количество |

### Демография (оценка)

| Сегмент | % |
| --- | --- |
| Разработчики | 35-40% |
| Писатели / журналисты | 15-20% |
| Адвокаты FOSS / приватности | 15-20% |
| Академики / исследователи | 10-15% |
| Tech-основатели / строители | 5-10% ← целевая аудитория Тима |

> **Внимание:** Потенциальные фрикции:Агрессивные CTA будут восприняты враждебно. AI content automation (Lisa) — спорная тема (authenticity). "Revenue architect" может показаться слишком коммерческим. UTM в ссылках могут вызвать вопросы у privacy-сообщества.

## 5. SEO-механика и обнаружение

### Преимущества Write.as для SEO

- Чистый HTML (нет JS-фреймворков, нет проблем с рендерингом SPA)
- Быстрая загрузка = высокие Core Web Vitals
- HTTPS по умолчанию
- Семантический HTML (h1, h2, article)
- Нет interstitials, попапов, consent-баннеров
- Доменная авторитетность write.as ~DA 55-60

### Стратегия кастомного домена

| Вариант | URL | SEO-эффект |
| --- | --- | --- |
| blog.sborka.work | blog.sborka.work/post | Строит DA для sborka.work ←ЛУЧШИЙ |
| blog.timzinin.com | blog.timzinin.com/post | Строит личный бренд |
| write.as/timzinin | write.as/timzinin/post | Минимальный SEO для своих доменов |

### Целевые ключевые кластеры

```
SEO Checklist per post:
✓ Заголовок содержит primary keyword (H1)
✓ Первый абзац — primary keyword естественно
✓ H2/H3 с related keywords
✓ Описательный slug (/multi-agent-system-architecture)
✓ Internal link на другой Write.as пост
✓ External link на авторитетный источник
✓ 1,200+ слов | ✓ Code blocks с syntax highlighting
```

## 6. Tone of Voice — адаптация

### Что СОХРАНИТЬ от тона Тима

- Начинать с проблемы читателя, не с самопродвижения
- Называть конкретные инструменты, людей и метрики
- Direct, no-BS коммуникация
- Честность о фейлах и trade-offs

### Что АДАПТИРОВАТЬ для Write.as

- Длинные предложения и абзацы — acceptable (аудитория ожидает литературное качество)
- Больше нюансов (аудитория умная, избегать oversimplification)
- Меньше "exclamation energy" — спокойная, уверенная экспертиза
- Техническая глубина выше (код, архитектурные диаграммы, логи)

### Примеры адаптации

| ❌ НЕ так | ✅ Так |
| --- | --- |
| "How I 10X'd My Content Output with AI Agents" | "Running 6 AI Agents in Production: Architecture, Costs, and What Broke" |
| "Everyone talks about AI agents. But how many actually run them?" | "For the past eight months, I have been running six autonomous AI agents. This post breaks down the architecture, the actual costs, and the three things that failed." |
| "Sign up NOW at sborka.work!" | "If you are building something similar, see the career platform itself at sborka.work." |

### Контентные столпы для Write.as

| Столп | Write.as адаптация | Частота |
| --- | --- | --- |
| Публичная сборка | Глубокие tech-разборы: архитектура, стоимость, провалы. 2,000-4,000 слов | 2x/мес |
| Глубокий технический | Гайды: паттерны CrewAI, дизайн MCP-серверов, AI-видео пайплайн. Много кода | 1x/мес |
| Экономика AI-агентов | Реальный анализ затрат: сколько стоят 6 агентов. Разбивка по задачам | 1x/мес |
| Кейс-стади СБОРКА | AI-трансформация подбора вакансий. MCP-first стратегия. Архитектура карьерной платформы | 1x/мес |

> **Инсайт:** Итого: 5-6 постов/мес на Write.as (один каждые 5-6 дней). Достаточно для видимости без выгорания. Язык: ОСНОВНОЙ — английский. Иногда русский — отмечать в заголовке.

## 7. Стратегии CTA для sborka.work

> **Внимание:** Главный вызов:Сообщество Write.as аллергично на открытый маркетинг. Традиционные CTA («Нажми здесь!», «Зарегистрируйся!») мгновенно разрушат доверие. Стратегия: давать столько ценности, что читатели САМИ ищут другие работы Тима.

### Формат UTM

```
sborka.work?utm_source=writeas&utm_medium=social&utm_campaign=s20_writeas&utm_content=wa_{slug}
```

> **Внимание:** НЕ ДЕЛАТЬ:Формы подписки на рассылку, сокращатели ссылок, CTA в первом абзаце, продвижение СБОРКИ в каждом посте (макс 60-70% постов с sborka.work ссылкой). UTM отслеживают ИСТОЧНИК, не ПОЛЬЗОВАТЕЛЯ — важное различие если спросят.

## 8. WriteFreely Self-Hosting на RUVDS

WriteFreely — open-source движок Write.as. Self-hosting даёт: custom domain, full CSS, federation control, no subscription ($0 vs $9/мес), data ownership, SEO benefits.

### Docker-настройка на RUVDS

```
services:
  writefreely:
    image: writeas/writefreely:latest
    ports: ["8083:8080"]
    volumes:
      - writefreely_data:/go/app/data
      - ./config.ini:/go/app/config.ini:ro

# config.ini: federation = true, max_blogs = 3
# Nginx reverse proxy → blog.sborka.work → :8083
```

### Матрица решения

| Фактор | Write.as хостинг ($9/мес) | Самохостинг ($0) |
| --- | --- | --- |
| Настройка | 0 (уже работает) | 2-4 часа |
| Кастомный домен | Да (Pro) | Да (полный контроль) |
| Хостинг картинок | snap.as ($6/мес) | Самохостинг (бесплатно) |
| SEO | Ограниченный | Полный контроль |
| Обслуживание | Нет | Обновления, бэкапы |

> **Инсайт:** Рекомендация:Начать с write.as/timzinin (уже работает). Через 30 дней оценить: генерирует ли трафик? CSS ограничивает бренд? Картинки — проблема? Если 2+ да → мигрировать на self-hosted WriteFreely.

> **Внимание:** При миграции:Смена ActivityPub хендла (@timzinin@write.as → @timzinin@blog.sborka.work) означает, что подписчики НЕ переносятся автоматически. Планировать миграцию и объявлять заранее на Write.as и Mastodon.

## 9. Кросс-платформенная синдикация (POSSE)

### Поток контента — Write.as как каноничный источник

```
Write.as (canonical)
  ├── ActivityPub → Mastodon followers (AUTO)
  ├── RSS feed → RSS readers (AUTO)
  └── API export → RUVDS publishing pipeline
        ├── Dev.to (cross-post + canonical_url)
        ├── Hashnode (cross-post + canonical_url)
        ├── Medium (adapted version)
        ├── LinkedIn (excerpt + link)
        ├── Telegram (excerpt + link)
        ├── VK (excerpt + link)
        ├── Bluesky (excerpt + link)
        ├── Tumblr (cross-post)
        ├── Minds (cross-post)
        └── Nostr (excerpt + link)
```

### Интеграция с Mastodon

Подписка на @timzinin@write.as из mastodon.social → новый пост появляется в ленте → буст с комментарием → двойной охват для подписчиков обоих аккаунтов.

### Канонический URL (критично для SEO)

При кросс-посте на Dev.to и Hashnode — ВСЕГДАcanonical_urlна Write.as. Без этого Google штрафует за дублированный контент.

```
Dev.to frontmatter:
---
canonical_url: https://write.as/timzinin/running-6-ai-agents-in-production
---

Hashnode mutation:
originalArticleURL: "https://write.as/timzinin/running-6-ai-agents-in-production"
```

### Автоматизация (Python на RUVDS)

```
import feedparser
FEED_URL = "https://write.as/timzinin/feed/"
# Опрос каждые 30 мин → парсинг → адаптация по платформам → публикация через API → лог
```

## 10. 30-дневный план действий

50+Fediverse подписчиков8Постов за 30 дней25+Визитов на sborka.work15+RSS подписчиков

> **Инсайт:** Карта позиционирования:Целевая позиция Тима — верхний правый квадрант: ВЫСОКАЯ техническая глубина + ПРАКТИЧЕСКИЙ строитель. Этот квадрант ПУСТ на Write.as/WriteFreely. Ближайший конкурент Xe Iaso — философский, не практический. Тим = реальные продакшн-системы + реальные метрики выручки.


---

## РЕКОМЕНДАЦИЯ: ЛИЧНЫЙ БРЕНД

**Приоритет:** LOW-MEDIUM  
**CTA-цель:** blog.timzinin.com  

**Обоснование:** Анти-метрическая культура. Аллергия на маркетинг. Ценен для POSSE и ActivityPub-федерации.

### Конкретные изменения

- Кастомный домен: blog.timzinin.com ВМЕСТО blog.sborka.work
- Мульти-блог: write.as/timzinin (EN) — НЕ как СБОРКА, а как Тим Зинин
- 'СБОРКА Case Study' → 'Building an AI-Powered Career Platform' — кейс, не промо
- POSSE: каноничный источник → синдикация на Dev.to, Medium, Hashnode

> *Обновлено: 8 марта 2026 — аудит стратегий (личный бренд vs СБОРКА)*
