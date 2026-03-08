# Swiss Law SR Skill — Introduction

## What is it?

**swiss-law-sr** is a Claude Code skill that provides structured access to the entire **Systematische Rechtssammlung (SR)** — Switzerland's official classified compilation of federal legislation. It covers **2,147 laws** organized across 9 categories, making Swiss federal law searchable and navigable directly within Claude Code.

## Architecture

The skill uses a **hub-and-spoke routing model**. The main `swiss-law-sr` skill acts as the entry point, routing queries to 9 specialized sub-skills based on the SR number's first digit:

| SR Range | Sub-Skill | Domain | Laws |
|----------|-----------|--------|------|
| 1xx | `staat` | Constitutional Law — Bundesverfassung, citizenship, authorities | 275 |
| 2xx | `privatrecht` | Private Law — ZGB, OR, civil & commercial law | 130 |
| 3xx | `strafrecht` | Criminal Law — StGB, penal code, criminal procedure | 65 |
| 4xx | `schule` | Education, Science & Culture — ETH, research, universities | 408 |
| 5xx | `landesverteidigung` | National Defence — army, military, civil protection | 120 |
| 6xx | `finanzen` | Finance — taxes, customs, financial markets, VAT | 176 |
| 7xx | `oeffentliche-werke` | Public Works, Energy & Transport — roads, railways, environment | 291 |
| 8xx | `gesundheit` | Health & Social Security — AHV, IV, healthcare, insurance | 353 |
| 9xx | `wirtschaft` | Economy & Trade — agriculture, competition, labour | 329 |

## How It Works

1. **Query routing** — When a user asks about Swiss law, the main skill identifies the relevant SR category and delegates to the appropriate sub-skill.
2. **Table of contents** — Each sub-skill's `SKILL.md` provides a full overview and table of contents for its SR category.
3. **Article-level detail** — Each sub-skill includes a `references/articles.md` file with detailed article listings, SR numbers, full law titles, and Fedlex ELI URLs.
4. **Source linking** — All laws link to their official source on [Fedlex](https://www.fedlex.admin.ch) using the European Legislation Identifier (ELI) format: `https://www.fedlex.admin.ch/eli/cc/{year}/{number}/de`.

## Fedlex Extraction

Since Fedlex pages require JavaScript rendering, the skill includes a Playwright-based extraction script (`extract_fedlex.py`) that can:

- Render full law text from any Fedlex ELI URL using headless Chromium
- Extract specific articles by number with all Absätze and Litera
- Verify citation accuracy (e.g., confirming exact Abs./lit. references)

## Use Cases

- **Legal research** — Look up any Swiss federal law by SR number or topic keyword
- **Citation verification** — Extract and verify exact article text before citing
- **Cross-referencing** — Navigate related laws across SR categories
- **Multilingual access** — Skill triggers on German (Bundesrecht, Rechtssammlung) and English (Swiss law, federal legislation) queries alike

## Quick Start

Ask Claude Code any question about Swiss law:

- *"What does SR 210 cover?"* → Routes to `privatrecht` (Zivilgesetzbuch)
- *"Show me the structure of the StGB"* → Routes to `strafrecht`
- *"What are the AHV regulations?"* → Routes to `gesundheit`
- *"Find laws about energy policy"* → Routes to `oeffentliche-werke`

The skill handles the routing automatically — no need to specify which sub-skill to use.
