# north-pattaya.com

Independent static-HTML guide to the northern end of Pattaya bay (Chonburi, Thailand):
Wong Amat beach, Naklua, the beach at North Pattaya, the North Pattaya bus station and the
hotels along that shore.

Published by WL Media. Owner repo: `winnietsoi/north-pattaya.com`.

## Status

**Skeleton — content in progress.** This repo holds the site chrome, the hub page, the five
section pages and the estate's standard supporting pages. The five section pages are opened
but not yet written: each states the questions it will answer and nothing it cannot support.
Do not describe this site as complete.

## How it is built and deployed

| item | value |
|---|---|
| host | Cloudflare Pages project `north-pattaya-com`, git-linked to this repo |
| build command | `python remove_html.py` (the fleet script: strips `.html` from `href` values and drops `.private`/`.github` at build time) |
| production branch | `main` |
| output | repository root (no framework, no bundler) |
| custom domain | **not bound yet** — deliberately pending the registrar/DNS card |

`remove_html.py` rewrites links in place in the build container only; commit the `.html`
`href` values and let the build produce clean URLs. Cloudflare Pages resolves `/about` to
`about.html`.

`404.html` at the repository root is required: without it Pages answers 200 with the homepage
for every unknown path.

## Template

`inside.dwt` is the estate interior-page template, ported unchanged in shape from
`corralejo-fuerteventura.net` (same `site-container` / `site-header` / `main-navigation` /
`main-content` / `site-footer` chrome, same `styles.css` and `mobile-menu.js`).

This repo does **not** carry `.private/dwt_tool.py`, and a copy must not be added to make a
sync step possible — tooling is a fleet-wide change. Pages were materialised from `inside.dwt`
by hand: every template-static line is byte-identical across the pages, and only the
`doctitle` and `body` editable regions differ. When you edit `inside.dwt`, reproduce the change
in the same static lines of every page (the carrier set is `inside.dwt` plus the twelve `.html`
pages).

## Page set

| file | purpose |
|---|---|
| `index.html` | hub: what North Pattaya is, and the five sections |
| `wong-amat-beach.html` | Wong Amat beach |
| `naklua.html` | Naklua, the fishing quarter |
| `north-pattaya-beach.html` | the beach at North Pattaya |
| `north-pattaya-bus-station.html` | arrival and onward transport |
| `north-pattaya-hotels.html` | hotels and price bands by sub-area |
| `404.html` | error page (noindex) |
| `about.html`, `contact.html`, `copyright.html`, `credits.html`, `privacy-policy.html` | estate supporting pages |

Page plan and the demand evidence behind it:
`~/wl-knowledge/sites/north-pattaya/findings/seo/2026-11-18-keyword-demand.md`.

## Deliberately absent (do not add without a decision)

- **Google Analytics / GA4** — no property exists for this domain yet. No tag is in the head.
- **Hand-placed AdSense units** — the Auto Ads loader is in the template (the estate uses Auto
  Ads only); no `<ins class="adsbygoogle">` unit goes on any page, ever. Error pages carry
  neither loader nor units, per the estate ruling.
- **`ads.txt`** — goes in with the AdSense onboarding decision, not before.
- **favicon** and **photography** — none supplied yet. `styles.css` `.hero-section` has
  `background-image: none` so the header gradient shows; do not put another site's photograph
  here to fill the gap.
- **sitemap.xml / sitemap.html** — on the estate block list. Do not create one.
