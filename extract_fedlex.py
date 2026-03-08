"""Extract Swiss legal articles from Fedlex using Playwright."""
import asyncio
import re
from playwright.async_api import async_playwright


STPO_URL = "https://www.fedlex.admin.ch/eli/cc/2010/267/de"
BV_URL = "https://www.fedlex.admin.ch/eli/cc/1999/404/de"
STGB_URL = "https://www.fedlex.admin.ch/eli/cc/54/757_781_799/de"

STPO_ARTICLES = [197, 212, 221, 226, 227, 228, 237]
BV_ARTICLES = [5, 10, 31, 36]
STGB_ARTICLES = [30]


async def extract_articles(page, url, article_numbers, law_name):
    """Navigate to a Fedlex law page and extract specific articles."""
    print(f"\n{'='*60}")
    print(f"Extracting from {law_name}: {url}")
    print(f"{'='*60}")

    await page.goto(url, wait_until="networkidle", timeout=60000)
    # Extra wait for JS rendering
    await page.wait_for_timeout(5000)

    # Take screenshot for debugging
    screenshot_path = f"/Users/mengbing/WorkSync/Git/multiskill/{law_name}_screenshot.png"
    await page.screenshot(path=screenshot_path, full_page=False)
    print(f"Screenshot saved: {screenshot_path}")

    # Get full page text
    body_text = await page.inner_text("body")

    results = {}
    for art_num in article_numbers:
        # Try multiple patterns to find article text
        patterns = [
            # Pattern: "Art. 221" followed by content until next "Art. NNN"
            rf'(Art\.?\s*{art_num}\b[^\n]*\n(?:.*?\n)*?)(?=Art\.?\s*\d+[a-z]?\s)',
            # Simpler: just find "Art. NNN" and grab following lines
            rf'(Art\.?\s*{art_num}\b.+?)(?=Art\.?\s*(?:{art_num+1}|{art_num+2})\b)',
        ]

        found = False
        for pattern in patterns:
            matches = re.findall(pattern, body_text, re.DOTALL)
            if matches:
                # Take the longest match (most complete)
                text = max(matches, key=len).strip()
                # Truncate if too long
                if len(text) > 3000:
                    text = text[:3000] + "..."
                results[art_num] = text
                found = True
                break

        if not found:
            # Fallback: search for the article heading and grab surrounding text
            idx = body_text.find(f"Art. {art_num}")
            if idx == -1:
                idx = body_text.find(f"Art.{art_num}")
            if idx >= 0:
                snippet = body_text[idx:idx+2000]
                # Try to cut at next article
                next_art = re.search(rf'Art\.?\s*(?:{art_num+1}|{art_num+2})\b', snippet[10:])
                if next_art:
                    snippet = snippet[:10 + next_art.start()]
                results[art_num] = snippet.strip()
            else:
                results[art_num] = f"NOT FOUND: Art. {art_num}"

    return results


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            locale="de-CH",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()

        # Extract StPO articles
        stpo = await extract_articles(page, STPO_URL, STPO_ARTICLES, "StPO")
        for art_num, text in stpo.items():
            print(f"\n--- Art. {art_num} StPO ---")
            print(text[:1500])

        # Extract BV articles
        bv = await extract_articles(page, BV_URL, BV_ARTICLES, "BV")
        for art_num, text in bv.items():
            print(f"\n--- Art. {art_num} BV ---")
            print(text[:1500])

        # Extract StGB articles
        stgb = await extract_articles(page, STGB_URL, STGB_ARTICLES, "StGB")
        for art_num, text in stgb.items():
            print(f"\n--- Art. {art_num} StGB ---")
            print(text[:1500])

        await browser.close()


asyncio.run(main())
