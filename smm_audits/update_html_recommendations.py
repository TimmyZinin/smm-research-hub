#!/usr/bin/env python3
"""Add recommendation banners to HTML strategy files."""

import os
import re

AUDIT_DIR = os.path.dirname(os.path.abspath(__file__))

RECOMMENDATIONS = {
    "s01_linkedin.html": ("ЛИЧНЫЙ БРЕНД (90%)", "HIGH", "#2D8A6E", "timzinin.com / AI Blogger Factory",
        "7K подписчиков — единственная платформа для прямой конверсии в AI Blogger Factory ($1,500/мес). Saudi/Gulf CTO — LinkedIn-first.",
        ["Headline: убрать СБОРКУ → AI Blogger Factory", "CTA: sborka.work → AI Agent Playbook PDF → Discovery Call", "Newsletter: → 'The Multi-Agent Architect'"]),
    "s02_instagram.html": ("HYBRID (60% бренд / 40% СБОРКА)", "LOW", "#D4A843", "Linktree (оба продукта)",
        "ER 0.48% — критически низкий. Travel-аудитория не конвертирует. HeyGen на автопилоте.",
        ["Bio: двойное позиционирование", "DM: два keyword-потока (AGENTS / CAREER)", "Архивировать 400+ travel-постов"]),
    "s03_youtube.html": ("HYBRID (50/50)", "MEDIUM", "#D4A843", "Двойной CTA",
        "YouTube ≠ B2B conversion. Compound growth через 6-12 мес. Shorts автопилот HeyGen.",
        ["Двойной CTA: AI Blogger Factory + sborka.work", "Чередовать AI и карьерные видео", "Плейлист 'AI Blogger Factory'"]),
    "s04_telegram_personal.html": ("ЛИЧНЫЙ БРЕНД (85%)", "MEDIUM", "#2D8A6E", "AI Blogger Factory + TG @timofeyzinin",
        "93 подписчика — ядро лояльной аудитории. 40-60% view rate. Personal brand по определению.",
        ["Описание: One Brain, Many Agents", "'Карьерный сигнал' → 'Lessons from СБОРКА'", "'Открытые цифры' усилить до 1/нед"]),
    "s05_telegram_sborka.html": ("СБОРКА (100%)", "MEDIUM", "#229ED9", "sborka.work + @Sborka_work_bot",
        "Бренд-канал СБОРКИ. Менять = уничтожить продукт. Воронка канал → бот → вебинар → клуб.",
        ["Стратегия остаётся как есть", "Усилить Tim's take 1-2/нед", "Cross-sell на @timofeyzinin после оплаты"]),
    "s06_threads.html": ("ЛИЧНЫЙ БРЕНД", "LOW", "#2D8A6E", "timzinin.com",
        "Англоязычная платформа. Конверсия в СБОРКУ ≈ 0. НЕ подходит для СБОРКА-трафика.",
        ["Bio: timzinin.com вместо sborka.work", "90% EN контент", "CTA: AI agents, link in bio"]),
    "s07_facebook.html": ("HYBRID (60% СБОРКА / 40% бренд)", "MEDIUM", "#D4A843", "Профиль: бренд, Группа: СБОРКА",
        "Уникальная HYBRID: профиль для бренда, группа для СБОРКИ, Events для вебинаров.",
        ["Профиль: обложка AI Blogger Factory", "Группа: карьерное сообщество СБОРКА", "UTM разделить по источнику"]),
    "s08_tiktok.html": ("ЛИЧНЫЙ БРЕНД", "MEDIUM", "#2D8A6E", "timzinin.com",
        "Конверсия в СБОРКУ слабая — Тим прав. AI виралится лучше карьерного. Awareness machine.",
        ["80% AI-демо контент", "Linktree: timzinin.com первый", "Кросс-пост → IG → YT → FB Reels"]),
    "s09_vk.html": ("HYBRID (70% СБОРКА / 30% бренд)", "HIGH", "#D4A843", "sborka.work + VK Статьи",
        "100% русскоязычная аудитория = ЦА СБОРКИ. VK Clips — рычаг роста. SEO Яндекс.",
        ["Название: 'СБОРКА | AI-Карьера'", "VK Статьи SEO-оптимизированные", "VK Clips: кросс-пост с TikTok"]),
    "s10_vcru.html": ("ЛИЧНЫЙ БРЕНД (80%)", "HIGH", "#2D8A6E", "TG @timofeyzinin",
        "Аудитория VC.ru = предприниматели. 50K+ views → 1-3 клиента по $1,500/мес.",
        ["СБОРКА = кейс-стади, не продукт", "CTA мягкий: TG @timofeyzinin", "5-10 экспертных комментов/день"]),
    "s11_devto.html": ("ЛИЧНЫЙ БРЕНД", "HIGH", "#2D8A6E", "timzinin.com",
        "DA 90+, 15-20M organic visits/мес. EN-разработчики ≠ RU job seekers.",
        ["Bio: Multi-Agent Revenue Architect", "70% технические туториалы", "Язык: только English"]),
    "s12_medium.html": ("ЛИЧНЫЙ БРЕНД", "HIGH", "#2D8A6E", "timzinin.com",
        "DA 94-96. Публикации 800K+. Partner Program = доход + бренд.",
        ["Профиль: AI Blogger Factory", "Публикация 'One Brain, Many Agents'", "Контент: бенчмарки, кейсы клиентов"]),
    "s13_hashnode.html": ("ЛИЧНЫЙ БРЕНД", "MEDIUM-HIGH", "#2D8A6E", "blog.timzinin.com",
        "Свой домен + рассылка + GitHub-бэкап. SEO на личном домене.",
        ["Домен: blog.timzinin.com вместо blog.sborka.work", "Canonical URL первый", "Серии: Multi-Agent Architecture"]),
    "s14_bluesky.html": ("ЛИЧНЫЙ БРЕНД", "MEDIUM", "#2D8A6E", "timzinin.com (хендл)",
        "25M+ пользователей. ER 8-12%. Нет штрафа за ссылки.",
        ["Хендл: timzinin.com вместо sborka.work", "Стартер-пак: AI Builders", "Кастомная лента: AI Agents"]),
    "s15_mastodon.html": ("ЛИЧНЫЙ БРЕНД (осторожно)", "LOW-MEDIUM", "#2D8A6E", "timzinin.com",
        "Анти-коммерческая культура. sborka.work будет враждебно воспринят.",
        ["Ссылка: timzinin.com с rel='me'", "Контент: open source, FOSS", "Хештеги: #OpenSource #AI"]),
    "s16_tumblr.html": ("ЛИЧНЫЙ БРЕНД (эксп.)", "LOW", "#2D8A6E", "timzinin.com",
        "Gen Z, анти-корпоративная культура. СБОРКА не упоминать.",
        ["Юмористический/самоироничный тон", "Серия Agent Diaries", "Абсурдистские наблюдения об AI"]),
    "s17_okru.html": ("СБОРКА", "MEDIUM", "#229ED9", "sborka.work",
        "Аудитория 35-55+ = карьерные переходы. Голубой океан. Технический контент провалится.",
        ["Группа: СБОРКА — карьерный клуб", "AI объяснять просто", "myTarget реклама дешевле VK"]),
    "s18_nostr.html": ("ЛИЧНЫЙ БРЕНД", "MEDIUM", "#2D8A6E", "timzinin.com",
        "Bitcoin-максималисты, шифропанки. СБОРКА нерелевантна. AI-ниша свободна.",
        ["Контент: Building in Public", "CTA: timzinin.com", "Lightning-адрес для zaps"]),
    "s19_minds.html": ("ЛИЧНЫЙ БРЕНД", "LOW-MEDIUM", "#2D8A6E", "timzinin.com",
        "Крипто-нативная аудитория. СБОРКА = слишком корпоративно.",
        ["Supermind: AI-консалтинг", "Wire-подписки", "Hot takes об AI"]),
    "s20_writeas.html": ("ЛИЧНЫЙ БРЕНД", "LOW-MEDIUM", "#2D8A6E", "blog.timzinin.com",
        "Анти-метрическая культура. POSSE + ActivityPub.",
        ["Домен: blog.timzinin.com", "СБОРКА как кейс, не промо", "Каноничный источник для синдикации"]),
    "s21_lemmy.html": ("ЛИЧНЫЙ БРЕНД", "LOW-MEDIUM", "#2D8A6E", "GitHub + timzinin.com",
        "Анти-корпоративная среда. FOSS. sborka.work = downvote.",
        ["Правило 10:1", "Self-hosted AI, Docker", "Open-source модели"]),
    "s22_twitter.html": ("ЛИЧНЫЙ БРЕНД", "HIGH", "#2D8A6E", "timzinin.com",
        "Основная платформа AI-строителей. Saudi/MENA. AI Blogger Factory.",
        ["Закреп: 'I run 8 businesses with 6 AI agents'", "Реклама: Saudi, UAE, Qatar", "Spaces: Agent Report"]),
    "s23_mave.html": ("СБОРКА", "HIGH", "#229ED9", "sborka.work + бот",
        "Подкаст = СБОРКА. Центральный хаб RSS на 7 платформ.",
        ["2x/неделю каденция", "VK Music + CastBox подача", "Маркеры глав, транскрипты"]),
    "s24_spotify.html": ("СБОРКА (диаспора)", "HIGH", "#229ED9", "sborka.work",
        "Диаспора после релокации = карьерный переход = ЦА СБОРКИ.",
        ["Spotify for Podcasters", "Видео-эпизоды", "Ежемесячный EN-спецвыпуск"]),
    "s25_apple.html": ("СБОРКА (СРОЧНО)", "HIGH", "#C2573A", "sborka.work",
        "Окно New & Noteworthy закрывается ~середина апреля!",
        ["Apple Podcasts Connect", "Рывок по рейтингам", "HTML-описания с ссылками"]),
    "s26_yandex.html": ("СБОРКА", "HIGH", "#229ED9", "sborka.work",
        "Основная RU-площадка (Spotify заблокирован). Алиса, Дзен, Поиск.",
        ["Заклеймить на podcasts.yandex.ru", "'Алиса, включи подкаст Сборка'", "Яндекс.Дзен статьи"]),
    "s27_deezer.html": ("СБОРКА (диаспора)", "MEDIUM", "#229ED9", "sborka.work",
        "RU-диаспора в Европе. Нулевая конкуренция.",
        ["podcasters.deezer.com", "Маркеры глав", "Редакционный питч"]),
    "s28_pocketcasts.html": ("СБОРКА", "LOW-MEDIUM", "#229ED9", "sborka.work",
        "Staff-инженеры, тех-лиды. Высокоценные лиды.",
        ["Маркеры глав с URL", "Плотный тон, фреймворки", "Не просить отзывы"]),
    "s29_vkmusic_castbox.html": ("СБОРКА", "MEDIUM", "#229ED9", "sborka.work",
        "Обе платформы НЕ подключены — блокер!",
        ["Подать на VK Music и CastBox", "VK Клипы промо", "Билингвальное описание"]),
}


def add_recommendation_to_html(filepath, direction, priority, color, cta, reasoning, changes):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if recommendation already exists
    if 'recommendation-banner' in html:
        return False

    # Build recommendation HTML
    priority_colors = {"HIGH": "#C2573A", "MEDIUM": "#D4A843", "LOW": "#8B7E6A", "LOW-MEDIUM": "#8B7E6A", "MEDIUM-HIGH": "#D4A843"}
    p_color = priority_colors.get(priority, "#8B7E6A")

    rec_html = f"""
<div class="recommendation-banner" style="background:linear-gradient(135deg,{color},#2C2418);color:#FFFDF7;padding:32px 40px;border-radius:16px;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,.15)">
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
    <span style="font-family:'Playfair Display',serif;font-size:1.6em;font-weight:700">РЕКОМЕНДАЦИЯ</span>
    <span style="background:rgba(255,255,255,.2);padding:4px 14px;border-radius:20px;font-size:.75em;font-weight:700;letter-spacing:1px">{direction}</span>
    <span style="background:{p_color};padding:4px 14px;border-radius:20px;font-size:.75em;font-weight:700;letter-spacing:1px">ПРИОРИТЕТ: {priority}</span>
  </div>
  <div style="opacity:.95;margin-bottom:16px;font-size:1.05em">{reasoning}</div>
  <div style="display:flex;gap:24px;flex-wrap:wrap;margin-bottom:16px">
    <div style="background:rgba(255,255,255,.12);border-radius:10px;padding:10px 18px"><b>CTA-цель:</b> {cta}</div>
  </div>
  <div style="font-size:.9em">
    <b>Изменения:</b>
    <ul style="margin-top:6px;padding-left:20px">
      {''.join(f'<li style="margin-bottom:4px">{c}</li>' for c in changes)}
    </ul>
  </div>
  <div style="margin-top:12px;font-size:.75em;opacity:.7">Аудит: 8 марта 2026 — личный бренд vs СБОРКА</div>
</div>
"""

    # Insert after </header> or after hero div
    insert_point = html.find('</header>')
    if insert_point == -1:
        # Try .hero div (podcast templates)
        hero_idx = html.find('class="hero"')
        if hero_idx == -1:
            return False
        # Find the closing div of .hero
        depth = 0
        i = html.find('<div', hero_idx - 10)
        for j in range(i, len(html)):
            if html[j:j+4] == '<div':
                depth += 1
            elif html[j:j+6] == '</div>':
                depth -= 1
                if depth == 0:
                    insert_point = j + 6
                    break
    else:
        insert_point = html.find('\n', insert_point) + 1

    if not insert_point:
        return False

    # Find next newline
    nl = html.find('\n', insert_point)
    if nl != -1:
        insert_point = nl + 1

    html = html[:insert_point] + rec_html + html[insert_point:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    return True


def main():
    updated = 0
    for filename, (direction, priority, color, cta, reasoning, changes) in sorted(RECOMMENDATIONS.items()):
        filepath = os.path.join(AUDIT_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  SKIP: {filename}")
            continue
        if add_recommendation_to_html(filepath, direction, priority, color, cta, reasoning, changes):
            print(f"  ✓ {filename} — {direction}")
            updated += 1
        else:
            print(f"  = {filename} (already has recommendation)")

    print(f"\n{updated} HTML files updated.")


if __name__ == '__main__':
    main()
