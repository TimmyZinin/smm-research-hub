#!/usr/bin/env python3
"""Replace all topnav in HTML strategy files with a unified navigation containing all 29 platforms."""

import os
import re

AUDIT_DIR = os.path.dirname(os.path.abspath(__file__))

# Canonical navigation: all 29 platforms with correct filenames and short labels
NAV_ITEMS = [
    ("s01_linkedin.html", "LinkedIn"),
    ("s02_instagram.html", "Instagram"),
    ("s03_youtube.html", "YouTube"),
    ("s04_telegram_personal.html", "TG Личный"),
    ("s05_telegram_sborka.html", "TG СБОРКА"),
    ("s06_threads.html", "Threads"),
    ("s07_facebook.html", "Facebook"),
    ("s08_tiktok.html", "TikTok"),
    ("s09_vk.html", "VK"),
    ("s10_vcru.html", "VC.ru"),
    ("s11_devto.html", "Dev.to"),
    ("s12_medium.html", "Medium"),
    ("s13_hashnode.html", "Hashnode"),
    ("s14_bluesky.html", "Bluesky"),
    ("s15_mastodon.html", "Mastodon"),
    ("s16_tumblr.html", "Tumblr"),
    ("s17_okru.html", "OK.ru"),
    ("s18_nostr.html", "Nostr"),
    ("s19_minds.html", "Minds"),
    ("s20_writeas.html", "Write.as"),
    ("s21_lemmy.html", "Lemmy"),
    ("s22_twitter.html", "Twitter/X"),
    ("s23_mave.html", "Mave"),
    ("s24_spotify.html", "Spotify"),
    ("s25_apple.html", "Apple"),
    ("s26_yandex.html", "Яндекс"),
    ("s27_deezer.html", "Deezer"),
    ("s28_pocketcasts.html", "PocketCasts"),
    ("s29_vkmusic_castbox.html", "VK+Cast"),
]

# Group separators for visual clarity
GROUPS = {
    0: None,   # LinkedIn - start
    8: "|",    # After TikTok - separator before RU platforms
    11: "|",   # After Dev.to - separator before blogs
    16: "|",   # After Tumblr - separator before alt platforms
    22: "|",   # After Twitter - separator before podcasts
}


def build_nav_html(current_file):
    """Build the unified navigation HTML for a given file."""
    lines = []
    lines.append('<nav class="topnav">')
    lines.append('  <span class="logo">SMM Hub</span>')
    lines.append('  <a href="../index.html">Обзор</a>')

    for i, (href, label) in enumerate(NAV_ITEMS):
        if i in GROUPS and GROUPS[i]:
            lines.append(f'  <span class="sep">{GROUPS[i]}</span>')

        active = ' class="active"' if href == current_file else ''
        lines.append(f'  <a href="{href}"{active}>{label}</a>')

    lines.append('</nav>')
    return '\n'.join(lines)


def fix_file(filepath):
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    nav_html = build_nav_html(filename)

    # Find and replace the existing nav
    # Pattern: <nav class="topnav">...</nav>
    nav_pattern = re.compile(r'<nav\s+class="topnav"[^>]*>.*?</nav>', re.DOTALL)
    match = nav_pattern.search(html)

    if not match:
        print(f"  SKIP {filename}: no topnav found")
        return False

    old_nav = match.group(0)
    old_links = re.findall(r'href="(s\d+[^"]*)"', old_nav)

    html = html[:match.start()] + nav_html + html[match.end():]

    # Also ensure the CSS has the necessary styles for .logo and .sep
    # Check if .logo style exists
    if '.topnav .logo' not in html and '.logo{' not in html:
        # Add logo/sep styles before </style>
        style_addition = """
.topnav .logo{font-family:'Playfair Display',serif;font-size:1.1em;font-weight:700;margin-right:8px;color:#D4A843}
.topnav .sep{color:#8B7E6A;font-size:.7em}
"""
        html = html.replace('</style>', style_addition + '</style>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  ✓ {filename}: {len(old_links)} links → 29 links")
    return True


def main():
    html_files = sorted([f for f in os.listdir(AUDIT_DIR) if f.startswith('s') and f.endswith('.html')])

    print(f"Fixing navigation in {len(html_files)} files...\n")

    fixed = 0
    for html_file in html_files:
        filepath = os.path.join(AUDIT_DIR, html_file)
        if fix_file(filepath):
            fixed += 1

    print(f"\nDone! {fixed}/{len(html_files)} files updated with unified 29-item navigation.")


if __name__ == '__main__':
    main()
