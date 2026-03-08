#!/usr/bin/env python3
"""Add strategy recommendations (Personal Brand vs СБОРКА) to each MD file."""

import os

RECOMMENDATIONS = {
    "s01_linkedin.md": {
        "direction": "ЛИЧНЫЙ БРЕНД (90%)",
        "priority": "HIGH",
        "cta": "timzinin.com / AI Blogger Factory лендинг",
        "changes": [
            "Headline профиля: убрать СБОРКУ → 'I build AI agent systems that run businesses 24/7 | AI Blogger Factory'",
            "CTA-воронка: sborka.work → AI Agent Playbook PDF → Discovery Call → Retainer $1,500-10,000/мес",
            "СБОРКА упоминается только как социальное доказательство ('мой карьерный клуб с 55 участниками')",
            "Контент: 30% 'Карьера и навыки' → 30% 'AI Blogger Factory results' + Saudi/MENA targeting",
            "Лид-магниты: 'AI Agent Build Checklist', 'AI Blogger Factory ROI Calculator' вместо 'Career Transition Framework'",
            "Newsletter: 'AI Career Architect Weekly' → 'The Multi-Agent Architect'"
        ],
        "reasoning": "7K подписчиков — единственная платформа для прямой конверсии в AI Blogger Factory ($1,500/мес). Saudi/Gulf CTO — LinkedIn-first. 1 клиент Blogger Factory = ~30 участников СБОРКИ."
    },
    "s02_instagram.md": {
        "direction": "HYBRID (60% бренд / 40% СБОРКА)",
        "priority": "LOW",
        "cta": "Linktree: 1) AI Blogger Factory 2) sborka.work 3) YouTube 4) TG",
        "changes": [
            "Bio: 'AI Agent Architect | Building systems 24/7 | Career club: @public_sborka'",
            "DM-автоматизация: два keyword-потока — 'AGENTS' → AI playbook, 'CAREER' → карьерный чек-лист",
            "Контент: 35% AI demo (бренд) + 35% карьерные данные (СБОРКА) + 20% build in public + 10% community",
            "Reels: AI-демо в EN (discovery) + карьерные советы в RU (conversion)",
            "Архивировать 400+ старых travel-постов"
        ],
        "reasoning": "ER 0.48% — критически низкий. Travel-аудитория не конвертирует. Instagram не среда для B2B ($1,500+). HeyGen Reels на автопилоте — не тратить ресурсы Тима."
    },
    "s03_youtube.md": {
        "direction": "HYBRID (50% бренд / 50% СБОРКА)",
        "priority": "MEDIUM",
        "cta": "Двойной CTA: AI Blogger Factory (бизнес) + sborka.work (карьера)",
        "changes": [
            "Описание канала: 'AI + Career + Documentary. Основатель AI Blogger Factory и СБОРКА'",
            "Закрепленный комментарий: двойной CTA — AI Blogger Factory + sborka.work",
            "Чередовать: видео про AI-агенты (personal brand) и карьерные видео (СБОРКА)",
            "Shorts: AI-демо + 'Career tip за 30 сек'",
            "Плейлист 'AI Blogger Factory' к существующим 5"
        ],
        "reasoning": "YouTube ≠ conversion для B2B-клиентов за $10K/мес. YouTube = маркетинговый канал. Compound growth через 6-12 мес. Shorts на автопилоте HeyGen."
    },
    "s04_telegram_personal.md": {
        "direction": "ЛИЧНЫЙ БРЕНД (85%)",
        "priority": "MEDIUM",
        "cta": "Soft CTA на AI Blogger Factory 1/нед, на СБОРКУ 1/2нед",
        "changes": [
            "Описание: 'One Brain, Many Agents. AI-агенты, revenue architecture, build in public. AI Blogger Factory + ещё 7 проектов'",
            "'Карьерный сигнал' → 'Lessons from СБОРКА' — инсайты как часть build-in-public, не как промо",
            "'Открытые цифры' — усилить до 1/нед (killer content для личного бренда)",
            "Закрепленный пост: 'Управляю 6 AI-агентами на 26 платформах. Строю AI Blogger Factory ($1,500/клиент)'",
            "СБОРКА — как один из проектов, не как основной продукт"
        ],
        "reasoning": "93 подписчика — ядро лояльной аудитории. Telegram Personal = по определению personal brand. 40-60% view rate — каждый пост ценен. Минимум усилий, максимум ROI на единицу."
    },
    "s05_telegram_sborka.md": {
        "direction": "СБОРКА (100%)",
        "priority": "MEDIUM",
        "cta": "sborka.work + @Sborka_work_bot",
        "changes": [
            "Стратегия остаётся как есть — грамотно построена",
            "Усилить 'Tim's take' — 1-2 экспертных мнения/нед ОТ ЛИЦА Тима о карьерных темах",
            "Cross-sell в бот: после оплаты → предложить подписку на @timofeyzinin",
            "TG Ads тест (5,000 RUB) — дешёвый эксперимент для валидации CAC"
        ],
        "reasoning": "Бренд-канал СБОРКИ. Менять назначение = уничтожить продукт. Воронка канал → бот → вебинар → клуб работает. Потолок revenue ограничен (4,900 руб × N)."
    },
    "s06_threads.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "LOW",
        "cta": "timzinin.com / AI Blogger Factory лендинг",
        "changes": [
            "Bio: убрать sborka.work → timzinin.com или AI Blogger Factory",
            "UTM: utm_campaign=personal_brand",
            "Контент: 90% EN, 'I built 30 AI agents — here's what works'",
            "CTA: 'Building AI agents for revenue. Link in bio'",
            "СБОРКА НЕ подходит для EN-аудитории Threads"
        ],
        "reasoning": "Англоязычная платформа. Конверсия в СБОРКУ ≈ 0. Ссылки штрафуются -30-50%. Подозрение Тима НЕ подтверждается — Threads не для СБОРКА-трафика."
    },
    "s07_facebook.md": {
        "direction": "HYBRID (60% СБОРКА / 40% бренд)",
        "priority": "MEDIUM",
        "cta": "Профиль: timzinin.com | Группа: sborka.work",
        "changes": [
            "Профиль: обложка 'Multi-Agent Revenue Architect | AI Blogger Factory'",
            "Группа: оставить 'AI-Powered Job Search (СБОРКА Community)'",
            "Reels: 60% AI-демо (бренд) + 40% карьерные советы (СБОРКА)",
            "Events/вебинары — сохранить для СБОРКА-воронки",
            "UTM разделить: profile → timzinin.com, group → sborka.work"
        ],
        "reasoning": "1,600 друзей = стартовая база. Уникальная платформа для HYBRID: профиль для бренда, группа для СБОРКИ, Events для вебинаров. Facebook Ads $100-150/мес → 5-15 заявок в СБОРКУ."
    },
    "s08_tiktok.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "MEDIUM",
        "cta": "timzinin.com",
        "changes": [
            "Описание: 'AI Agent Architect | Built 30+ agents | Building in public'",
            "Linktree: 1) timzinin.com 2) YouTube 3) sborka.work (опционально)",
            "Контент: 80% AI-демо + 20% карьерные советы (мост к AI, не к СБОРКЕ)",
            "CTA: 'Follow for daily AI agent builds'",
            "Кросс-пост: TikTok → IG Reels → YT Shorts → FB Reels с personal brand messaging"
        ],
        "reasoning": "Тим прав — конверсия в СБОРКУ слабая. TikTok = awareness machine. AI-контент виралится лучше карьерного. Виральный ролик → узнаваемость → конверсия на LinkedIn/YouTube."
    },
    "s09_vk.md": {
        "direction": "HYBRID (70% СБОРКА / 30% бренд)",
        "priority": "HIGH",
        "cta": "sborka.work + VK Статьи",
        "changes": [
            "Название сообщества: 'СБОРКА | AI-Карьера'",
            "Контент: 70% карьерный + 30% personal brand кейсы",
            "VK Статьи: SEO-оптимизированные лонгриды про AI-карьеру с soft CTA на sborka.work",
            "VK Clips: кросс-пост с TikTok (без водяных знаков), RU-озвучка",
            "Мини-приложение 'AI-проверка резюме' → воронка на sborka.work"
        ],
        "reasoning": "100% русскоязычная аудитория = ЦА СБОРКИ. VK Clips — рычаг роста с нуля. VK Статьи индексируются Яндексом → SEO. VK Donut после 500 подписчиков."
    },
    "s10_vcru.md": {
        "direction": "ЛИЧНЫЙ БРЕНД (80%)",
        "priority": "HIGH",
        "cta": "TG @timofeyzinin (мягкий CTA)",
        "changes": [
            "Подсайты: AI (40%) + Технологии (30%) + Карьера как кейс (20%) + Маркетинг (10%)",
            "СБОРКА = кейс-стади: 'Месяц N: 55 юзеров, $165 MRR'",
            "CTA мягкий: 'Подписывайтесь на TG @timofeyzinin' или 'Пишите @timofeyzinin'",
            "Комментарии: 5-10 экспертных комментов/день → рост кармы +7 → +200",
            "SEO: 'AI агенты' (15K+/мес), 'автоматизация бизнеса AI' (20K+)"
        ],
        "reasoning": "Аудитория VC.ru = скептичные профессионалы, предприниматели. Не job seekers. Одна статья 50K+ views + мягкий CTA = 1-3 клиента по $1,500/мес."
    },
    "s11_devto.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "HIGH",
        "cta": "timzinin.com",
        "changes": [
            "Bio: 'Multi-Agent Revenue Architect. Running 6 AI agents in production across 8 businesses → timzinin.com'",
            "UTM: timzinin.com?utm_source=devto&utm_campaign=personal_brand",
            "Контент: 70% технические туториалы по мульти-агентам + 20% бенчмарки + 10% build in public",
            "Серии: воронка → timzinin.com/consulting или AI Blogger Factory, НЕ sborka.work",
            "Язык: только English"
        ],
        "reasoning": "DA 90+, 15-20M organic visits/мес. Англоязычные разработчики ≠ русскоязычные job seekers. sborka.work бессмысленен для EN-аудитории."
    },
    "s12_medium.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "HIGH",
        "cta": "timzinin.com",
        "changes": [
            "Профиль: 'Multi-Agent Revenue Architect | AI Blogger Factory | Running production AI systems across 8 businesses'",
            "Website в профиле: timzinin.com (не sborka.work)",
            "Публикация 'One Brain, Many Agents' — чистый personal brand",
            "Контент: AI-архитектура, бенчмарки, кейсы с клиентами (Marshall, КРМКТЛ)",
            "Partner Program: контент под пейволом = доход + бренд"
        ],
        "reasoning": "DA 94-96. Публикации 'The Startup' (800K+), 'Towards Data Science' (700K+). Аудитория принимает бизнес-решения. Монетизация Partner Program."
    },
    "s13_hashnode.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "MEDIUM-HIGH",
        "cta": "blog.timzinin.com (свой домен)",
        "changes": [
            "Домен: blog.timzinin.com ВМЕСТО blog.sborka.work — SEO juice на личный домен",
            "Canonical URL: blog.timzinin.com первый → Dev.to (48ч) → Medium (72ч)",
            "Рассылка: подписчики = собственная аудитория для personal brand",
            "Серии: 'Multi-Agent Architecture in Production'"
        ],
        "reasoning": "Свой домен + рассылка + GitHub-бэкап. SEO на собственном домене. Более техническая аудитория чем Dev.to."
    },
    "s14_bluesky.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "MEDIUM",
        "cta": "timzinin.com (доменный хендл)",
        "changes": [
            "Доменный хендл: timzinin.com ВМЕСТО sborka.work",
            "Стартер-пак: 'AI Builders & Multi-Agent Architects' вместо 'Карьера в технологиях'",
            "Карьерный столп → 'Future of AI Work' (EN)",
            "Кастомная лента: 'AI Agents & Multi-Agent Systems'"
        ],
        "reasoning": "25M+ пользователей. Tech/journalism аудитория. ER 8-12% (лучше X). Нет штрафа за внешние ссылки."
    },
    "s15_mastodon.md": {
        "direction": "ЛИЧНЫЙ БРЕНД (с осторожностью)",
        "priority": "LOW-MEDIUM",
        "cta": "timzinin.com (верифицированная ссылка rel='me')",
        "changes": [
            "CTA на sborka.work будут восприняты враждебно (анти-коммерческая культура)",
            "Контент: open source, self-hosting, FOSS. СБОРКУ упоминать ТОЛЬКО как open-source проект",
            "Хештеги: #OpenSource #AI #BuildInPublic — НЕ #CareerAdvice",
            "Ссылка: timzinin.com с верификацией rel='me'"
        ],
        "reasoning": "Анти-коммерческая культура. Скептичны к хайпу. Русскоязычная аудитория минимальна."
    },
    "s16_tumblr.md": {
        "direction": "ЛИЧНЫЙ БРЕНД (экспериментальный)",
        "priority": "LOW",
        "cta": "timzinin.com (только в bio)",
        "changes": [
            "СБОРКА вообще НЕ должна упоминаться",
            "Контент: юмористический/самоироничный взгляд на AI-агентов",
            "Серия 'Agent Diaries' — от лица агентов, юмористическая",
            "Тон: полностью отличается от LinkedIn/Dev.to — абсурдистские наблюдения"
        ],
        "reasoning": "Gen Z (50%), анти-корпоративная культура. sborka.work будет полностью проигнорирован."
    },
    "s17_okru.md": {
        "direction": "СБОРКА",
        "priority": "MEDIUM",
        "cta": "sborka.work",
        "changes": [
            "Группа: 'СБОРКА — карьерный клуб | AI и работа'",
            "Тим упоминается как 'основатель СБОРКИ', не как AI-архитектор",
            "AI объяснять просто: 'ChatGPT — это AI-ассистент, как умный коллега'",
            "myTarget реклама на 30-50% дешевле VK",
            "Яндекс SEO индексирует контент OK.ru"
        ],
        "reasoning": "Аудитория 35-55+ = карьерные переходы ('карьера после 40'). Голубой океан. Технический контент про мульти-агенты провалится."
    },
    "s18_nostr.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "MEDIUM",
        "cta": "timzinin.com",
        "changes": [
            "NIP-05: tim@sborka.work оставить (для домена), но контент = personal brand",
            "Контент: Building in Public — мульти-агентные системы, AI Video Factory",
            "CTA: timzinin.com, НЕ sborka.work",
            "Язык: только English",
            "Lightning-адрес через Alby/Wallet of Satoshi"
        ],
        "reasoning": "Bitcoin-максималисты, шифропанки. СБОРКА нерелевантна. AI/мульти-агентная ниша свободна на Nostr."
    },
    "s19_minds.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "LOW-MEDIUM",
        "cta": "timzinin.com",
        "changes": [
            "CTA: timzinin.com, НЕ sborka.work",
            "Контент: оригинальные фреймворки ('One Brain, Many Agents'), hot takes об AI",
            "Supermind: 'Спроси меня о мульти-агентном AI' — прямая монетизация",
            "Wire-подписки как мини-Patreon",
            "Язык: только English. Убрать ВСЕ упоминания СБОРКИ"
        ],
        "reasoning": "Крипто-нативная аудитория. СБОРКА = слишком корпоративно. Встроенная монетизация через токены."
    },
    "s20_writeas.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "LOW-MEDIUM",
        "cta": "blog.timzinin.com",
        "changes": [
            "Кастомный домен: blog.timzinin.com ВМЕСТО blog.sborka.work",
            "Мульти-блог: write.as/timzinin (EN) — НЕ как СБОРКА, а как Тим Зинин",
            "'СБОРКА Case Study' → 'Building an AI-Powered Career Platform' — кейс, не промо",
            "POSSE: каноничный источник → синдикация на Dev.to, Medium, Hashnode"
        ],
        "reasoning": "Анти-метрическая культура. Аллергия на маркетинг. Ценен для POSSE и ActivityPub-федерации."
    },
    "s21_lemmy.md": {
        "direction": "ЛИЧНЫЙ БРЕНД (с адаптацией)",
        "priority": "LOW-MEDIUM",
        "cta": "GitHub + timzinin.com",
        "changes": [
            "sborka.work в CTA — категорически не работает (правило 10:1)",
            "Позиционирование: 'One Brain, Many Agents на single VPS' — indie-hacker этос",
            "Контент: self-hosted AI, Docker Compose, open-source модели (Llama, Mistral)",
            "ОБЯЗАТЕЛЬНО упоминать open-source при упоминании Claude/ChatGPT",
            "Сообщество: !ai_agents, НЕ !sborka"
        ],
        "reasoning": "Сильнейшая анти-корпоративная культура. FOSS-энтузиасты. Русскоязычный карьерный клуб = мгновенный downvote."
    },
    "s22_twitter.md": {
        "direction": "ЛИЧНЫЙ БРЕНД",
        "priority": "HIGH",
        "cta": "timzinin.com",
        "changes": [
            "Bio: timzinin.com, СБОРКУ упоминать как проект ('Built СБОРКА, an AI career platform')",
            "Закреплённый тред: 'I run 8 businesses with 6 AI agents → timzinin.com/consulting'",
            "Saudi/MENA angle: чистый personal brand + consulting",
            "Реклама $250/мес: таргетинг Saudi Arabia, UAE, Qatar",
            "Spaces: 'Agent Report' — personal brand формат"
        ],
        "reasoning": "Основная платформа AI-строителей. Прямой доступ к Saudi/MENA. Критический канал для AI Blogger Factory."
    },
    "s23_mave.md": {
        "direction": "СБОРКА",
        "priority": "HIGH",
        "cta": "sborka.work + бот",
        "changes": [
            "Подкаст = СБОРКА, менять бессмысленно",
            "Подать на VK Music и CastBox (блокер!)",
            "Каденция: 2x/неделю (цель 12 эпизодов/мес)",
            "Маркеры глав, транскрипты, уникальные обложки",
            "Рассмотреть второй EN-подкаст 'Tim Zinin: AI Architect' после 20+ эпизодов СБОРКИ"
        ],
        "reasoning": "Подкаст называется СБОРКА. Центральный хаб дистрибуции RSS на 7 платформ."
    },
    "s24_spotify.md": {
        "direction": "СБОРКА (с диаспорным ракурсом)",
        "priority": "HIGH",
        "cta": "sborka.work + бот",
        "changes": [
            "Заявить шоу в Spotify for Podcasters",
            "Транскрипты, маркеры глав, опросы",
            "Видео-эпизоды (слайды + voiceover через ffmpeg)",
            "Ежемесячный EN-спецвыпуск 'SBORKA International'",
            "Трейлер 60 сек"
        ],
        "reasoning": "Spotify ушёл из России. Аудитория = диаспора после релокации = карьерный переход = ЦА СБОРКИ."
    },
    "s25_apple.md": {
        "direction": "СБОРКА",
        "priority": "HIGH (СРОЧНО)",
        "cta": "sborka.work + бот",
        "changes": [
            "СРОЧНО: доступ в Apple Podcasts Connect",
            "Заголовок: 'СБОРКА | Подкаст про поиск работы и карьеру'",
            "Рывок по рейтингам: просьба в TG, на вебинарах, в боте",
            "HTML-описания с кликабельными ссылками",
            "Маркеры глав (дифференциатор)",
            "Структура сезонов"
        ],
        "reasoning": "Окно 'New & Noteworthy' закрывается ~середина апреля. Аудитория 30-45, высокий доход → платящие клиенты СБОРКИ."
    },
    "s26_yandex.md": {
        "direction": "СБОРКА",
        "priority": "HIGH",
        "cta": "sborka.work + бот",
        "changes": [
            "Заклеймить шоу на podcasts.yandex.ru",
            "Голосовой тест: 'Алиса, включи подкаст Сборка'",
            "Статьи на Яндекс.Дзен со ссылками на подкаст",
            "Оптимизация описания под Wordstat",
            "Бейдж 'Слушайте на Яндекс.Музыке' на sborka.work"
        ],
        "reasoning": "Основная площадка для российской аудитории (Spotify заблокирован). Экосистема Яндекса: Алиса, Дзен, Поиск."
    },
    "s27_deezer.md": {
        "direction": "СБОРКА (диаспорный фокус)",
        "priority": "MEDIUM",
        "cta": "sborka.work",
        "changes": [
            "Заклеймить шоу на podcasters.deezer.com",
            "Маркеры глав",
            "Редакционный питч на podcasts@deezer.com",
            "Темы для диаспоры: 'Работа в новой стране', 'CV по европейским стандартам'",
            "Встраиваемый плеер Deezer на sborka.work"
        ],
        "reasoning": "Deezer = ворота к RU-диаспоре в Европе (Германия, Франция, Израиль). Нулевая конкуренция в RU-карьерных подкастах."
    },
    "s28_pocketcasts.md": {
        "direction": "СБОРКА (адаптированный тон)",
        "priority": "LOW-MEDIUM",
        "cta": "sborka.work",
        "changes": [
            "Маркеры глав с URL sborka.work (глава 5 = CTA)",
            "Тон: плотнее, больше фреймворков, минимум воды, данные",
            "Заголовки: нумерация '#01: [Конкретная проблема]'",
            "НЕ просить 'подпишись и оставь отзыв' (PC-пользователи считают снисходительным)",
            "pca.st/95ecagwv во все списки ссылок"
        ],
        "reasoning": "Аудитория = staff-инженеры, тех-лиды. Высокоценные лиды для СБОРКИ."
    },
    "s29_vkmusic_castbox.md": {
        "direction": "СБОРКА",
        "priority": "MEDIUM",
        "cta": "sborka.work + бот",
        "changes": [
            "СРОЧНО: подать на VK Music и CastBox",
            "VK Music: подкаст-виджет на VK-сообществе, VK Клипы (15-60 сек промо)",
            "CastBox: HTML-ссылки с UTM, комментарии к аудио",
            "VK Music: описание простой текст (ссылки НЕ кликабельны в плеере)",
            "CastBox: билингвальное описание (RU + EN ключевые слова)"
        ],
        "reasoning": "VK Music = молодая RU-аудитория. CastBox = дополнительный охват диаспоры. Обе платформы НЕ подключены — блокер."
    }
}


def update_md_file(md_dir, filename, rec):
    filepath = os.path.join(md_dir, filename)
    if not os.path.exists(filepath):
        print(f"  SKIP: {filename} not found")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove existing recommendation section if present
    if "## РЕКОМЕНДАЦИЯ: " in content:
        idx = content.index("## РЕКОМЕНДАЦИЯ: ")
        content = content[:idx].rstrip()

    # Build recommendation section
    section = f"\n\n---\n\n## РЕКОМЕНДАЦИЯ: {rec['direction']}\n\n"
    section += f"**Приоритет:** {rec['priority']}  \n"
    section += f"**CTA-цель:** {rec['cta']}  \n\n"
    section += f"**Обоснование:** {rec['reasoning']}\n\n"
    section += "### Конкретные изменения\n\n"
    for change in rec['changes']:
        section += f"- {change}\n"
    section += f"\n> *Обновлено: 8 марта 2026 — аудит стратегий (личный бренд vs СБОРКА)*\n"

    content += section

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ {filename} — {rec['direction']}")


def main():
    md_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'md')

    print("Обновление MD-стратегий с рекомендациями...\n")

    for filename, rec in sorted(RECOMMENDATIONS.items()):
        update_md_file(md_dir, filename, rec)

    print(f"\nГотово! {len(RECOMMENDATIONS)} файлов обновлено.")


if __name__ == '__main__':
    main()
