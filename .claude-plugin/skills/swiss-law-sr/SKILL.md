---
name: swiss-law-sr
description: "Use when user asks about Swiss federal law, SR numbers, Bundesrecht, Systematische Rechtssammlung, Rechtssammlung, Swiss law, Swiss legislation, Fedlex, or any specific Swiss law topic. Main entry point that routes to 9 specialized categories."
---

# Swiss Systematische Rechtssammlung (SR)

## Overview

The **Systematische Rechtssammlung (SR)** is the official classified compilation of Swiss federal legislation. It is organized into **9 categories** (SR 1–9) containing a total of **2147 laws**.

## Category Routing Table

| SR | Category (DE) | Category (EN) | Key Topics | Laws | Skill Path |
|---|---|---|---|---|---|
| 1xx | 1 Staat | State - Constitutional Law | Bundesverfassung, BV, constitutional, Bürgerrecht | 275 | `skills/staat` |
| 2xx | 2 Privatrecht | Private Law | ZGB, OR, Zivilgesetzbuch, Obligationenrecht | 130 | `skills/privatrecht` |
| 3xx | 3 Strafrecht | Criminal Law | StGB, Strafgesetzbuch, penal code, criminal law | 65 | `skills/strafrecht` |
| 4xx | 4 Schule | Education, Science, Culture | Bildung, education, Forschung, research | 408 | `skills/schule` |
| 5xx | 5 Landesverteidigung | National Defence | Armee, army, Militär, military | 120 | `skills/landesverteidigung` |
| 6xx | 6 Finanzen | Finance | Steuern, taxes, Zoll, customs | 176 | `skills/finanzen` |
| 7xx | 7 Öffentliche Werke | Public Works, Energy, Transport | Energie, energy, Verkehr, transport | 291 | `skills/oeffentliche-werke` |
| 8xx | 8 Gesundheit | Health, Social Security | health, Gesundheit, Sozialversicherung, AHV | 353 | `skills/gesundheit` |
| 9xx | 9 Wirtschaft | Economy, Trade | economics, Wirtschaft, Handel, trade | 329 | `skills/wirtschaft` |

## How to Use

1. **Identify the category** from the SR number's first digit (e.g., SR 210 → category 2)
2. **Read the sub-skill's `SKILL.md`** for the full table of contents of that category
3. **Read `references/articles.md`** in the sub-skill for detailed article listings

### SR Number → Category Mapping

The first digit of any SR number determines its category:

- **SR 1xx** → `skills/staat/SKILL.md`
- **SR 2xx** → `skills/privatrecht/SKILL.md`
- **SR 3xx** → `skills/strafrecht/SKILL.md`
- **SR 4xx** → `skills/schule/SKILL.md`
- **SR 5xx** → `skills/landesverteidigung/SKILL.md`
- **SR 6xx** → `skills/finanzen/SKILL.md`
- **SR 7xx** → `skills/oeffentliche-werke/SKILL.md`
- **SR 8xx** → `skills/gesundheit/SKILL.md`
- **SR 9xx** → `skills/wirtschaft/SKILL.md`

### ELI URL Format

All law URLs use the European Legislation Identifier (ELI) format:

```
https://www.fedlex.admin.ch/eli/cc/{year}/{number}/de
```

Relative ELI paths in the sub-skills should be prefixed with `https://www.fedlex.admin.ch`.

## Extracting Article Text from Fedlex with Playwright

Fedlex pages require JavaScript rendering — `WebFetch` and `curl` return empty/incomplete content. Use the Playwright-based script `extract_fedlex.py` (project root) to extract full article text including all Absätze and Litera.

### Prerequisites

```bash
pip3 install --break-system-packages playwright && python3 -m playwright install chromium
```

### How it works

The script uses headless Chromium to:
1. Navigate to a Fedlex ELI URL (e.g., `https://www.fedlex.admin.ch/eli/cc/2010/267/de` for StPO)
2. Wait for JS rendering (`networkidle` + 5s timeout)
3. Extract full rendered page text
4. Find specific articles by number via regex and output their complete text

### Configuration

Edit the URL and article-number lists at the top of the script:

```python
STPO_URL = "https://www.fedlex.admin.ch/eli/cc/2010/267/de"   # StPO (SR 312.0)
BV_URL   = "https://www.fedlex.admin.ch/eli/cc/1999/404/de"   # BV (SR 101)
STGB_URL = "https://www.fedlex.admin.ch/eli/cc/54/757_781_799/de"  # StGB (SR 311.0)

STPO_ARTICLES = [197, 212, 221, 226, 227, 228, 237]
BV_ARTICLES   = [5, 10, 31, 36]
STGB_ARTICLES = [30]
```

Add any Fedlex law by its ELI URL and the article numbers you need.

### Running

```bash
python3 extract_fedlex.py
```

Output: full text of each article with all Abs./lit., plus debug screenshots (`StPO_screenshot.png`, etc.).

### Use case: Citation verification

Use the extracted text to verify that citation Abs./lit. numbers are correct before producing citation lists. See `swiss_citations_kollusionsgefahr.py` for an example — 31 verified citations for pre-trial detention extension under Art. 221 Abs. 1 lit. b StPO (Kollusionsgefahr).
