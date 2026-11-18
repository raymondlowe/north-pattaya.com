# Copilot instructions — north-pattaya.com

Read this before touching the repo. Read `README.md` first for what this site is and what is
deliberately absent.

## 0. This is a static Dreamweaver-template site, not an app

- `inside.dwt` is the interior-page template. Pages carry
  `<!-- #BeginTemplate "inside.dwt" -->` under `<html>` and `<!-- #EndTemplate -->` before
  `</html>`.
- Edit only inside the editable regions: `doctitle` and `body`. Header, navigation, breadcrumb
  wrapper and footer are template-static: a change there belongs in `inside.dwt` **and** in the
  same static lines of every `.html` page in the carrier set.
- No `.private/dwt_tool.py` in this repo and none may be added. Reproduce template changes by
  hand and say in the PR which static lines you changed and which pages you changed them on.
- `remove_html.py` runs as the Pages build command: commit `href="page.html"` and let the build
  strip the extension. Never commit extension-less `href` values.

## 1. Content rules

- One `<h1>` per page, containing the page's subject in plain words.
- Unique `<title>` and a `<meta name="description">` that is factually correct for the page.
  There is **no** length target for either: do not trim, pad, count characters, add meta
  keywords or build keyword blocks.
- Every number a reader can act on — fares, lounger prices, ticket prices, opening hours,
  market days, hotel rates, distances — carries the month it was checked. If a figure has not
  been checked, it does not go on the page. Never restore a figure from memory or from another
  travel guide.
- Do not invent business details. If an address, phone or rate cannot be verified from a
  current source, leave it out.
- A page that is unfinished says so. Never pad an unwritten guide with generic travel advice to
  reach a word count.
- Style: full sentences, warm and factual, no hype. Paragraphs under ~250 words, callout boxes
  between them (`.callout-info`, `.callout-tips`, `.callout-success`, `.callout-neutral`,
  `.callout-cultural` in `styles.css`).

## 2. Advertising and analytics

- The estate uses **Auto Ads only**. Never add a manual `<ins class="adsbygoogle">` unit.
- There is no AdSense loader and no GA4 tag in this repo: neither account is provisioned for
  this domain. Adding either is a human decision, not a code cleanup.
- AdSense code, `ads.txt` and ad-unit changes are Raymond's call. Prepare the diff, do not land
  it.

## 3. Out of scope on this site

- Sitemaps of any kind (`sitemap.xml`, `sitemap.html`).
- Technical SEO churn: meta/canonical/robots/schema tweaks that do not fix a factual error.
  A canonical that already resolves to the page is not an edit.
- Redesigns. The chrome is the estate chrome; do not restyle it.

## 4. Links

- Internal links use descriptive anchor text and must resolve to a file in this repo.
- Every external link goes to the authoritative source for that entity, opens in a new tab
  (`target="_blank" rel="noopener"`) and must load when checked — verify with a GET, not a HEAD.
- A new page is not finished until the pages that should link to it do.

## 5. Git

- Branch names: `content/<slug>` or `feature/<topic>`. Never push to `main`.
- Commit format: `<scope>: <action> — <short outcome>`, referencing the issue/card.
- PRs open as drafts; the current checker result goes in the PR comment. Nobody merges but
  Raymond or Winnie.
