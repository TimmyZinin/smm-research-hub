---
id: s33_publer_integration
updated: 2026-03-21
---

# S-33: Publer интеграция

## Гибридная схема (актуальная, 21 мар 2026)

LinkedIn, VK, Threads RU — работают НАПРЯМУЮ через API. Publer нужен только для платформ где прямой API недоступен.

| Канал | Метод | Стоимость | Статус |
|-------|-------|-----------|--------|
| Telegram | Прямой Bot API | Бесплатно | РАБОТАЕТ |
| LinkedIn | Прямой API (ugcPosts) | Бесплатно | РАБОТАЕТ |
| Threads RU @timzinin | Прямой Graph API | Бесплатно | РАБОТАЕТ |
| VK | Прямой wall.post | Бесплатно | РАБОТАЕТ |
| Bluesky | Прямой AT Protocol | Бесплатно | РАБОТАЕТ |
| Dev.to, Hashnode | Прямые API | Бесплатно | РАБОТАЕТ |
| OK.ru | Прямой OAuth | Бесплатно | РАБОТАЕТ |
| **Facebook** | **Publer API** | ~$20/мес (Business) | В Publer |
| **TikTok** | **Publer API** | входит в план | В Publer |
| **Threads EN** | **Publer API** | входит в план | В Publer |

## Publer API

- **Base URL:** `https://app.publer.com/api/v1`
- **Auth:** Header `Authorization: Bearer-API {ключ}` (нестандартный формат!)
- **Workspace header:** `Publer-Workspace-Id: YOUR_WORKSPACE_ID`
- **Rate limit:** 100 requests / 2 minutes
- **Docs:** https://publer.com/docs
- **План:** Business (~$20/мес, TRY 930)
- **Login:** tim.zinin@gmail.com (Google OAuth)

### Endpoints
- `GET /posts` — список постов (filter: state, from)
- `POST /posts` — создание/расписание
- `DELETE /posts/{post_id}` — удаление
- `GET /job_status/{job_id}` — статус async операции

### Подключённые аккаунты в Publer
1. Facebook — Timofey Zinin (личный профиль)
2. TikTok — Tim Zinin
3. Threads EN — Tim Zinin (timzinin_en)

## Content Pipeline интеграция

Content Pipeline v2 (n8n) → Adapter → Publisher → Publer API → Facebook/TikTok/Threads EN

Прямые API публикации через n8n HTTP nodes → TG/LinkedIn/Threads RU/VK/Bluesky/OK.ru
