#!/usr/bin/env python3
"""Generate Claude Code skill plugin files from sr_toc.json."""

import json
import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SR_TOC_PATH = PROJECT_ROOT / "sr_toc.json"
PLUGIN_DIR = PROJECT_ROOT / ".claude-plugin"
SKILLS_DIR = PLUGIN_DIR / "skills"

NOISE_NUMBERS = {"main-navigation", "content", "site-map", "context-top"}

# Skill metadata for the 9 categories
SKILL_META = {
    "1": {
        "slug": "staat",
        "title_en": "State - Constitutional Law",
        "keywords": "Bundesverfassung, BV, constitutional, Bürgerrecht, citizenship, Staatsrecht, Behörden, authorities, Parlament, Bundesrat, Bundesgericht, SR 1xx",
    },
    "2": {
        "slug": "privatrecht",
        "title_en": "Private Law",
        "keywords": "ZGB, OR, Zivilgesetzbuch, Obligationenrecht, civil code, contract law, Privatrecht, Handelsrecht, commercial law, SR 2xx",
    },
    "3": {
        "slug": "strafrecht",
        "title_en": "Criminal Law",
        "keywords": "StGB, Strafgesetzbuch, penal code, criminal law, Strafrecht, Jugendstrafrecht, Strafprozessordnung, SR 3xx",
    },
    "4": {
        "slug": "schule",
        "title_en": "Education, Science, Culture",
        "keywords": "Bildung, education, Forschung, research, Kultur, culture, ETH, Universität, Schule, SR 4xx",
    },
    "5": {
        "slug": "landesverteidigung",
        "title_en": "National Defence",
        "keywords": "Armee, army, Militär, military, Zivilschutz, civil protection, Landesverteidigung, Bevölkerungsschutz, SR 5xx",
    },
    "6": {
        "slug": "finanzen",
        "title_en": "Finance",
        "keywords": "Steuern, taxes, Zoll, customs, Nationalbank, Finanzmarkt, MWST, VAT, Finanzen, SR 6xx",
    },
    "7": {
        "slug": "oeffentliche-werke",
        "title_en": "Public Works, Energy, Transport",
        "keywords": "Energie, energy, Verkehr, transport, Post, Strassen, roads, Eisenbahn, railway, Umwelt, environment, SR 7xx",
    },
    "8": {
        "slug": "gesundheit",
        "title_en": "Health, Social Security",
        "keywords": "health, Gesundheit, Sozialversicherung, AHV, IV, Heilmittel, Krankenversicherung, KVG, Lebensmittel, SR 8xx",
    },
    "9": {
        "slug": "wirtschaft",
        "title_en": "Economy, Trade",
        "keywords": "economics, Wirtschaft, Handel, trade, Landwirtschaft, agriculture, Wettbewerb, competition, Arbeit, labour, SR 9xx",
    },
}


def is_noise(node: dict) -> bool:
    return node.get("number", "") in NOISE_NUMBERS


def is_search_field(node: dict) -> bool:
    return node.get("number", "") == "search-field"


def collect_laws(node: dict) -> list[dict]:
    """Recursively collect all laws from a node, skipping noise."""
    laws = []
    if is_noise(node):
        return laws
    # search-field laws belong to parent — collect them
    if is_search_field(node):
        laws.extend(node.get("laws", []))
        return laws
    # Regular node: collect own laws + recurse children
    laws.extend(node.get("laws", []))
    for child in node.get("children", []):
        laws.extend(collect_laws(child))
    return laws


def build_toc_sections(category: dict) -> list[dict]:
    """Build structured TOC from a top-level category.

    Returns list of {heading, laws} for each subcategory.
    """
    sections = []
    for subcategory in category.get("children", []):
        if is_noise(subcategory) or is_search_field(subcategory):
            continue
        # Extract subcategory title (e.g. "10 Bundesverfassung")
        heading = subcategory.get("title", "").strip()
        laws = collect_laws(subcategory)
        if laws:
            sections.append({"heading": heading, "laws": laws})
    return sections


def generate_skill_md(category: dict, meta: dict, sections: list[dict]) -> str:
    """Generate SKILL.md content."""
    number = category["number"]
    title = category["title"].strip()
    slug = meta["slug"]
    title_en = meta["title_en"]
    keywords = meta["keywords"]
    total_laws = sum(len(s["laws"]) for s in sections)

    lines = []
    # YAML frontmatter
    lines.append("---")
    lines.append(f"name: {slug}")
    desc = (
        f"Use when user asks about {title}, {title_en}, "
        f"{keywords}. "
        f"Covers SR category {number} of the Systematische Rechtssammlung."
    )
    lines.append(f'description: "{desc}"')
    lines.append("---")
    lines.append("")

    # Header
    lines.append(f"# SR {number} – {title}")
    lines.append("")

    # Overview
    lines.append("## Overview")
    lines.append("")
    lines.append(
        f"Category **{number}** of the Swiss Systematische Rechtssammlung (SR) "
        f"covers **{title_en}**. "
        f"Contains **{total_laws} laws** across **{len(sections)} subcategories**."
    )
    lines.append("")

    # Usage
    lines.append("## Usage")
    lines.append("")
    lines.append("- Search by SR number or keyword in the table of contents below")
    lines.append(
        "- Full URLs: prefix relative ELI paths with `https://www.fedlex.admin.ch`"
    )
    lines.append("- For detailed article listings, see `references/articles.md`")
    lines.append("")

    # Table of Contents
    lines.append("## Table of Contents")
    lines.append("")
    for section in sections:
        lines.append(f"### {section['heading']}")
        lines.append("")
        for law in section["laws"]:
            sr = law["sr_number"]
            law_title = law["title"]
            url = law["url"]
            lines.append(f"- **SR {sr}** {law_title} ([ELI]({url}))")
        lines.append("")

    return "\n".join(lines)


def generate_articles_md(category: dict, sections: list[dict]) -> str:
    """Generate references/articles.md content."""
    title = category["title"].strip()
    number = category["number"]

    lines = []
    lines.append(f"# SR {number} – {title}: Article Listings")
    lines.append("")

    for section in sections:
        lines.append(f"## {section['heading']}")
        lines.append("")
        for law in section["laws"]:
            sr = law["sr_number"]
            law_title = law["title"]
            url = law["url"]
            articles = law.get("articles", [])
            lines.append(f"### SR {sr} – {law_title}")
            lines.append("")
            lines.append(f"ELI: `{url}`")
            lines.append("")
            if articles:
                for art in articles:
                    lines.append(f"- {art}")
                lines.append("")
            else:
                lines.append("_No articles listed._")
                lines.append("")

    return "\n".join(lines)


def generate_main_skill_md(categories: list[dict], category_stats: list[dict]) -> str:
    """Generate the main router SKILL.md that directs to all 9 sub-skills."""
    all_keywords = set()
    for meta in SKILL_META.values():
        all_keywords.update(k.strip() for k in meta["keywords"].split(","))

    lines = []
    # YAML frontmatter
    lines.append("---")
    lines.append("name: swiss-law-sr")
    desc = (
        "Use when user asks about Swiss federal law, SR numbers, "
        "Bundesrecht, Systematische Rechtssammlung, Rechtssammlung, "
        "Swiss law, Swiss legislation, Fedlex, or any specific Swiss law topic. "
        "Main entry point that routes to 9 specialized categories."
    )
    lines.append(f'description: "{desc}"')
    lines.append("---")
    lines.append("")

    # Header
    lines.append("# Swiss Systematische Rechtssammlung (SR)")
    lines.append("")

    # Overview
    total_laws = sum(s["law_count"] for s in category_stats)
    lines.append("## Overview")
    lines.append("")
    lines.append(
        "The **Systematische Rechtssammlung (SR)** is the official classified compilation "
        "of Swiss federal legislation. It is organized into **9 categories** (SR 1–9) "
        f"containing a total of **{total_laws} laws**."
    )
    lines.append("")

    # Routing table
    lines.append("## Category Routing Table")
    lines.append("")
    lines.append("| SR | Category (DE) | Category (EN) | Key Topics | Laws | Skill Path |")
    lines.append("|---|---|---|---|---|---|")
    for stat in category_stats:
        number = stat["number"]
        title_de = stat["title_de"]
        meta = SKILL_META[number]
        title_en = meta["title_en"]
        slug = meta["slug"]
        # Pick first 3-4 keywords for brevity
        kw_list = [k.strip() for k in meta["keywords"].split(",")]
        short_kw = ", ".join(kw_list[:4])
        lines.append(
            f"| {number}xx | {title_de} | {title_en} | {short_kw} | {stat['law_count']} | `skills/{slug}` |"
        )
    lines.append("")

    # Usage instructions
    lines.append("## How to Use")
    lines.append("")
    lines.append("1. **Identify the category** from the SR number's first digit (e.g., SR 210 → category 2)")
    lines.append("2. **Read the sub-skill's `SKILL.md`** for the full table of contents of that category")
    lines.append("3. **Read `references/articles.md`** in the sub-skill for detailed article listings")
    lines.append("")
    lines.append("### SR Number → Category Mapping")
    lines.append("")
    lines.append("The first digit of any SR number determines its category:")
    lines.append("")
    for stat in category_stats:
        number = stat["number"]
        meta = SKILL_META[number]
        lines.append(f"- **SR {number}xx** → `skills/{meta['slug']}/SKILL.md`")
    lines.append("")

    # ELI URL format
    lines.append("### ELI URL Format")
    lines.append("")
    lines.append("All law URLs use the European Legislation Identifier (ELI) format:")
    lines.append("")
    lines.append("```")
    lines.append("https://www.fedlex.admin.ch/eli/cc/{year}/{number}/de")
    lines.append("```")
    lines.append("")
    lines.append("Relative ELI paths in the sub-skills should be prefixed with `https://www.fedlex.admin.ch`.")
    lines.append("")

    return "\n".join(lines)


def generate_marketplace_json(categories: list[dict], total_laws: int) -> dict:
    """Generate marketplace.json."""
    # Main router skill as first entry
    skills = [
        {
            "name": "swiss-law-sr",
            "title": "Swiss Systematische Rechtssammlung (SR)",
            "description": (
                f"Main entry point for Swiss federal law. "
                f"Routes to 9 specialized categories covering {total_laws} laws."
            ),
            "path": "skills/swiss-law-sr",
        }
    ]
    for cat in categories:
        number = cat["number"]
        meta = SKILL_META[number]
        slug = meta["slug"]
        title = cat["title"].strip()
        skills.append(
            {
                "name": slug,
                "title": f"SR {number} – {title}",
                "description": (
                    f"Swiss federal law category {number}: {meta['title_en']}. "
                    f"Navigate laws, SR numbers, and articles."
                ),
                "path": f"skills/{slug}",
            }
        )
    return {
        "name": "swiss-law-sr",
        "title": "Swiss Systematische Rechtssammlung (SR)",
        "description": f"Navigate all 9 categories of Swiss federal law with {total_laws} laws and ~76K articles.",
        "skills": skills,
    }


def main():
    print("Reading sr_toc.json...")
    with open(SR_TOC_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = [
        c
        for c in data["children"]
        if c.get("number", "") in SKILL_META
    ]
    print(f"Found {len(categories)} categories")

    total_laws = 0
    files_created = 0
    category_stats = []

    for cat in categories:
        number = cat["number"]
        meta = SKILL_META[number]
        slug = meta["slug"]
        sections = build_toc_sections(cat)
        law_count = sum(len(s["laws"]) for s in sections)
        total_laws += law_count
        category_stats.append({
            "number": number,
            "title_de": cat["title"].strip(),
            "law_count": law_count,
        })

        # Create directories
        skill_dir = SKILLS_DIR / slug
        refs_dir = skill_dir / "references"
        refs_dir.mkdir(parents=True, exist_ok=True)

        # Write SKILL.md
        skill_md = generate_skill_md(cat, meta, sections)
        skill_path = skill_dir / "SKILL.md"
        skill_path.write_text(skill_md, encoding="utf-8")
        files_created += 1

        # Write articles.md
        articles_md = generate_articles_md(cat, sections)
        articles_path = refs_dir / "articles.md"
        articles_path.write_text(articles_md, encoding="utf-8")
        files_created += 1

        print(f"  {slug}: {law_count} laws, {len(sections)} subcategories")

    # Generate main router skill
    main_skill_dir = SKILLS_DIR / "swiss-law-sr"
    main_skill_dir.mkdir(parents=True, exist_ok=True)
    main_skill_md = generate_main_skill_md(categories, category_stats)
    main_skill_path = main_skill_dir / "SKILL.md"
    main_skill_path.write_text(main_skill_md, encoding="utf-8")
    files_created += 1
    print(f"  swiss-law-sr: main router skill (covers {total_laws} laws)")

    # Write marketplace.json
    PLUGIN_DIR.mkdir(parents=True, exist_ok=True)
    marketplace = generate_marketplace_json(categories, total_laws)
    marketplace_path = PLUGIN_DIR / "marketplace.json"
    with open(marketplace_path, "w", encoding="utf-8") as f:
        json.dump(marketplace, f, indent=2, ensure_ascii=False)
    files_created += 1

    print(f"\nDone! Created {files_created} files.")
    print(f"Total laws: {total_laws}")


if __name__ == "__main__":
    main()
