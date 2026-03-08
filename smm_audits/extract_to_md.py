#!/usr/bin/env python3
"""Extract HTML strategy documents to Markdown format."""

import os
import re
from bs4 import BeautifulSoup, NavigableString

AUDIT_DIR = os.path.dirname(os.path.abspath(__file__))

def html_to_md(html_file):
    """Convert an HTML strategy document to Markdown."""
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    lines = []

    # Extract title and subtitle from header
    header = soup.find('header')
    if header:
        h1 = header.find('h1')
        if h1:
            lines.append(f"# {h1.get_text(strip=True)}")
        sub = header.find(class_='sub')
        if sub:
            lines.append(f"\n> {sub.get_text(strip=True)}")

        # Extract meta items
        metas = header.find_all(class_='meta-item')
        if metas:
            lines.append("\n| Метрика | Значение |")
            lines.append("|---------|----------|")
            for m in metas:
                num = m.find(class_='meta-num')
                label = m.find(class_='meta-label')
                if num and label:
                    lines.append(f"| {label.get_text(strip=True)} | {num.get_text(strip=True)} |")
        lines.append("")

    # Process all sections (some files use <div class="section">, others use <section>)
    sections = soup.find_all(class_='section')
    if not sections:
        sections = soup.find_all('section')
    for section in sections:
        # Section title
        h2 = section.find('h2')
        if h2:
            title_text = h2.get_text(strip=True)
            # Clean HTML entities
            title_text = title_text.replace('→', '→').replace('—', '—')
            lines.append(f"\n## {title_text}\n")

        # Process all children
        for child in section.children:
            if isinstance(child, NavigableString):
                continue

            tag = child.name
            if not tag:
                continue

            cls = ' '.join(child.get('class', []))

            if tag == 'h2':
                continue  # already processed
            elif tag == 'h3':
                lines.append(f"\n### {child.get_text(strip=True)}\n")
            elif tag == 'h4':
                lines.append(f"\n#### {child.get_text(strip=True)}\n")
            elif tag == 'p':
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"{text}\n")
            elif tag == 'table':
                # Convert table to markdown
                rows = child.find_all('tr')
                if rows:
                    headers = rows[0].find_all(['th', 'td'])
                    header_texts = [h.get_text(strip=True) for h in headers]
                    if header_texts:
                        lines.append("| " + " | ".join(header_texts) + " |")
                        lines.append("| " + " | ".join(["---"] * len(header_texts)) + " |")
                    for row in rows[1:]:
                        cells = row.find_all(['td', 'th'])
                        cell_texts = [c.get_text(strip=True).replace('\n', ' ') for c in cells]
                        if cell_texts:
                            lines.append("| " + " | ".join(cell_texts) + " |")
                    lines.append("")
            elif tag == 'ul' or tag == 'ol':
                items = child.find_all('li', recursive=False)
                for i, item in enumerate(items):
                    prefix = f"{i+1}." if tag == 'ol' else "-"
                    lines.append(f"{prefix} {item.get_text(strip=True)}")
                lines.append("")
            elif 'insight' in cls:
                text = child.get_text(strip=True)
                lines.append(f"> **Инсайт:** {text}\n")
            elif 'warning' in cls:
                text = child.get_text(strip=True)
                lines.append(f"> **Внимание:** {text}\n")
            elif 'tactic' in cls:
                title_el = child.find(class_='tactic-title')
                data_el = child.find(class_='tactic-data')
                action_el = child.find(class_='tactic-action')
                parts = []
                if title_el:
                    parts.append(f"**{title_el.get_text(strip=True)}**")
                if data_el:
                    parts.append(f"`{data_el.get_text(strip=True)}`")
                if action_el:
                    parts.append(action_el.get_text(strip=True))
                if parts:
                    lines.append("- " + " — ".join(parts) + "\n")
            elif 'formula' in cls:
                text = child.get_text(strip=True)
                lines.append(f"```\n{text}\n```\n")
            elif 'competitor' in cls:
                name_el = child.find(class_='name')
                stats_el = child.find(class_='stats')
                name = name_el.get_text(strip=True) if name_el else ""
                stats = stats_el.get_text(strip=True) if stats_el else ""
                # Get remaining text
                desc_parts = []
                for p in child.find_all('p'):
                    if 'name' not in ' '.join(p.get('class', [])) and 'stats' not in ' '.join(p.get('class', [])):
                        desc_parts.append(p.get_text(strip=True))
                desc = ' '.join(desc_parts)
                lines.append(f"**{name}** ({stats})")
                if desc:
                    lines.append(f"  {desc}")
                lines.append("")
            elif 'action-item' in cls or 'action-plan' in cls:
                if 'action-plan' in cls:
                    for item in child.find_all(class_='action-item'):
                        lines.append(f"- {item.get_text(strip=True)}")
                else:
                    lines.append(f"- {child.get_text(strip=True)}")
            elif 'do-list' in cls or 'dont-list' in cls:
                h4 = child.find('h4')
                if h4:
                    lines.append(f"\n**{h4.get_text(strip=True)}**")
                for li in child.find_all('li'):
                    lines.append(f"- {li.get_text(strip=True)}")
                lines.append("")
            elif 'timeline' in cls:
                items = child.find_all(class_='timeline-item')
                for item in items:
                    week_el = item.find(class_='week')
                    week = week_el.get_text(strip=True) if week_el else ""
                    text = item.get_text(strip=True)
                    if week:
                        text = text.replace(week, '', 1).strip()
                    lines.append(f"- **{week}**: {text}")
                lines.append("")
            elif tag == 'div' and 'grid-2' in cls:
                for sub in child.children:
                    if hasattr(sub, 'get') and sub.name:
                        sub_cls = ' '.join(sub.get('class', []))
                        if 'do-list' in sub_cls or 'dont-list' in sub_cls:
                            h4 = sub.find('h4')
                            if h4:
                                lines.append(f"\n**{h4.get_text(strip=True)}**")
                            for li in sub.find_all('li'):
                                lines.append(f"- {li.get_text(strip=True)}")
                            lines.append("")
                        else:
                            text = sub.get_text(strip=True)
                            if text:
                                lines.append(text + "\n")
            elif tag == 'div':
                # Generic div - extract text if meaningful
                inner_text = child.get_text(strip=True)
                if inner_text and len(inner_text) > 20 and not any(c in cls for c in ['topnav', 'container', 'meta']):
                    # Check for sub-elements
                    has_structure = child.find(['h3', 'h4', 'table', 'ul', 'ol'])
                    if not has_structure:
                        lines.append(f"{inner_text}\n")

    # Add frontmatter
    basename = os.path.basename(html_file).replace('.html', '')
    md_content = f"---\nid: {basename}\nsource: {os.path.basename(html_file)}\nupdated: 2026-03-08\n---\n\n"
    md_content += "\n".join(lines)

    # Clean up multiple blank lines
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)

    return md_content


def main():
    md_dir = os.path.join(AUDIT_DIR, 'md')
    os.makedirs(md_dir, exist_ok=True)

    html_files = sorted([f for f in os.listdir(AUDIT_DIR) if f.startswith('s') and f.endswith('.html')])

    for html_file in html_files:
        filepath = os.path.join(AUDIT_DIR, html_file)
        md_content = html_to_md(filepath)

        md_filename = html_file.replace('.html', '.md')
        md_path = os.path.join(md_dir, md_filename)

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        lines_count = len(md_content.split('\n'))
        print(f"✓ {md_filename} ({lines_count} lines)")

    print(f"\nDone! {len(html_files)} files converted to {md_dir}/")


if __name__ == '__main__':
    main()
