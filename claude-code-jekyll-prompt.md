# Claude Code Prompt: 5mlowroad.com Jekyll Site

## Context and Purpose

You are building the promotional website for **Five Minutes on the Low Road**, an original musical in development by Charles T. Betz and Josiah Thomas Turner. The show is about a pharmaceutical executive who has a near-death experience and returns transformed. The target audience is NDE researchers, spiritual seekers, musical theater professionals, and general literary audiences.

This site is the destination for QR codes printed in a physical brochure distributed at the IANDS (International Association for Near Death Studies) conference in late August 2026. The brochure will have two QR codes:

1. **Front door** (cover/early page) → routes to `5mlowroad.com/go/listen` → redirects to `/listen` (audio/podcast experience)
2. **Back door** (back cover) → routes to `5mlowroad.com/go/subscribe` → redirects to `/subscribe` (email capture)

The `/go/` paths are **redirect stubs only** — their sole purpose is to allow the destination to be changed in the future without reprinting the brochure. They contain nothing except a `<meta http-equiv="refresh">` redirect. Do not add content to them.

The site is **not** selling tickets or collecting payment. It is building an audience for a future Kickstarter campaign (mid-to-late 2027). The primary call to action is email list signup. Secondary CTA is listening to the music/podcast.

---

## Technical Stack

- **Generator:** Jekyll (latest stable)
- **Hosting:** GitHub Pages via GitHub Actions workflow (NOT the legacy `gh-pages` branch approach — use the modern Actions-based deployment)
- **Domain:** `5mlowroad.com` (registered via Cloudflare). Add a `CNAME` file to the repo root containing `5mlowroad.com`. Charles will point the Cloudflare DNS to GitHub Pages manually.
- **CSS:** Plain CSS, no framework. Mobile-first. The site must work perfectly on a phone — it will be scanned and visited on phones at a conference.
- **JavaScript:** Minimal vanilla JS only. No React, no Vue, no build pipeline.
- **Email list:** Kit (ConvertKit). Embed their standard HTML signup form on the `/subscribe` page and as a secondary widget in the site footer. Leave a clearly marked placeholder comment `<!-- KIT_FORM_EMBED_HERE -->` where the form goes, so Charles can paste in the Kit embed code. Do NOT hardcode a specific Kit form ID — Charles will supply this.
- **Contact routing:** Formspree. On the `/contact` page, create an HTML form with `action="https://formspree.io/f/FORMSPREE_ID"` method="POST". Leave `FORMSPREE_ID` as a literal placeholder string — Charles will replace it.
- **Audio players:** Use standard HTML5 `<audio>` elements with controls for individual song embeds. Leave src attributes as placeholder paths (`/assets/audio/song-name.mp3`) with comments indicating what goes there. Also leave a clearly marked block for a podcast player iframe embed (`<!-- PODCAST_PLAYER_EMBED_HERE -->`).
- **No Disqus, no analytics yet.** Leave a commented-out placeholder for Google Analytics or Plausible in `_layouts/default.html` but do not activate it.

---

## Git and GitHub Setup

1. Initialize a git repository in the current directory: `git init`
2. Create an initial commit with all files
3. Create a GitHub repository named `5mlowroad` under Charles's GitHub account (use the `gh` CLI if available, otherwise provide the exact commands Charles needs to run)
4. Push to `main` branch
5. Set up a GitHub Actions workflow at `.github/workflows/jekyll.yml` that builds and deploys to GitHub Pages on every push to `main`
6. The Actions workflow should use `actions/jekyll-build-pages` and `actions/deploy-pages`

---

## Directory Structure

```
5mlowroad/
├── .github/
│   └── workflows/
│       └── jekyll.yml
├── _config.yml
├── _layouts/
│   ├── default.html       # Base layout: nav, footer, head
│   ├── page.html          # Standard content page
│   └── listen.html        # Audio-focused layout (larger player area)
├── _includes/
│   ├── header.html        # Site nav
│   ├── footer.html        # Footer with Kit signup widget + contact link
│   ├── audio-player.html  # Reusable HTML5 audio player component
│   └── song-card.html     # Individual song card: title, description, player
├── assets/
│   ├── css/
│   │   └── main.css
│   ├── audio/             # Placeholder directory (actual MP3s added later)
│   │   └── .gitkeep
│   └── images/
│       └── .gitkeep       # Luke O'Leary illustrations go here when ready
├── index.md               # Home/landing page
├── listen.md              # Front-door QR target: audio + podcast
├── subscribe.md           # Back-door QR target: email signup
├── about.md               # About the show and Charles T. Betz
├── contact.md             # Contact form via Formspree
├── go/
│   ├── listen.md          # Redirect stub → /listen
│   └── subscribe.md       # Redirect stub → /subscribe
├── CNAME                  # Contains: 5mlowroad.com
├── Gemfile
└── README.md
```

---

## Pages: Content and Purpose

### `/` — Home (index.md)

**Purpose:** First impression for anyone arriving directly (not via QR code). Establishes what the show is, invites listening, invites subscribing.

**Layout:** `default.html`

**Content structure (use placeholder text marked with `<!-- TODO -->`):**
1. **Hero section** — full-width image placeholder (`<!-- TODO: Luke O'Leary hero illustration -->`), overlaid with show title "Five Minutes on the Low Road" in large type, subtitle "A new musical by Charles T. Betz"
2. **One-line logline** — placeholder: `<!-- TODO: one-sentence description -->`
3. **Two prominent CTAs side by side:** "Listen Now" (→ `/listen`) and "Stay in Touch" (→ `/subscribe`)
4. **Brief show description** — 2-3 sentences placeholder
5. **Featured song** — one `audio-player` include (placeholder src)
6. **Footer** with Kit signup widget

### `/listen` — Listen (listen.md)

**Purpose:** Front-door QR destination. Someone scans the brochure at IANDS and lands here. They should be able to start listening within one tap.

**Layout:** `listen.html`

**Content structure:**
1. **Podcast player at top** — prominent embed placeholder: `<!-- PODCAST_PLAYER_EMBED_HERE: paste iframe from Buzzsprout/Transistor/etc -->`; label it "Five Minutes on the Low Road — Full Audio Experience" with a brief sentence: "Narrated story with original songs. ~20 minutes."
2. **Individual songs section** below the podcast — heading "Individual Songs"
3. **Song cards** for each song using `song-card.html` include. Include cards for the following (all with placeholder audio src and placeholder descriptions):
   - "This Side of Tomorrow" — `<!-- TODO: description -->`
   - "Earth Was the Dream" — `<!-- TODO: description -->`
   - "This Was You" — `<!-- TODO: description -->`
   - "Leaderboard" — `<!-- TODO: description -->`
4. **Brief CTA at bottom:** "Want updates as new music is released?" → link to `/subscribe`

### `/subscribe` — Stay in Touch (subscribe.md)

**Purpose:** Back-door QR destination and general email signup. This is the primary conversion goal of the entire site.

**Layout:** `page.html`

**Content structure:**
1. **Headline:** Something like "Stay Close to Five Minutes on the Low Road" (placeholder — Charles will write final copy)
2. **2-3 sentences** about what subscribers get: development updates, new song releases, Kickstarter announcement when it launches (placeholder copy)
3. **Kit signup form:** `<!-- KIT_FORM_EMBED_HERE -->` — prominent, centered, email field only, large submit button
4. **Promise line below form:** "Occasional emails. No spam. No shared contacts." (placeholder — Charles will refine)
5. **Link back to** `/listen` for those who arrived here first

### `/about` — About (about.md)

**Purpose:** Who Charles is, what the show is, where it is in development.

**Layout:** `page.html`

**Content structure:**
1. **About the show** — placeholder paragraph describing FMLR as a musical in development exploring near-death experience, empathy, and transformation. Note it is pre-production, with concept recordings in development.
2. **About Charles T. Betz** — placeholder bio paragraph. Credit line: "Book, lyrics, and music by Charles T. Betz. Additional book, lyrics, and music by Josiah Thomas Turner. Dramaturgical guidance by Josiah Thomas Turner."
3. **Development status** — "Currently in development. Concept recordings in progress. Kickstarter campaign anticipated mid-to-late 2027."
4. **Photo placeholder** — `<!-- TODO: author photo -->`

### `/contact` — Contact (contact.md)

**Purpose:** Industry contacts, press, collaboration inquiries.

**Layout:** `page.html`

**Content structure:**
1. Brief intro: "For industry inquiries, press, and collaboration."
2. **Direct email line:** `char@charlestbetz.com`
3. **Formspree contact form** with fields: Name, Email, Message, Submit. Action = `https://formspree.io/f/FORMSPREE_ID`

### `/go/listen` and `/go/subscribe` — Redirect Stubs

These pages exist solely to serve as stable QR code targets. Do not add navigation, content, or design — just the redirect meta tag and a brief "Redirecting..." text fallback.

```markdown
---
layout: null
permalink: /go/listen/
---
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="0; url=/listen">
</head>
<body>Redirecting...</body>
</html>
```

Same pattern for `/go/subscribe/` → `/subscribe`.

---

## Design Direction

**Register:** Literary, minimal, slightly otherworldly. This is not a pop concert site. Think chapbook meets spiritual memoir. The brochure uses EB Garamond for body text and Gill Sans for headers — the website should feel like the same family.

**Typography:**
- Load EB Garamond from Google Fonts (`https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap`)
- Load a clean sans-serif for headers — use `font-family: 'Gill Sans', 'Gill Sans MT', Calibri, sans-serif` (system stack, no web font needed)
- Body text: 18px / 1.7 line height on desktop, 16px on mobile
- Generous white space

**Color palette (suggested — Charles may revise):**
- Background: near-white (`#f8f6f2`) — warm, paper-like
- Text: near-black (`#1a1a1a`)
- Accent: deep teal (`#2a6b6b`) — the "other side" color, used for links, CTAs, active states
- Secondary accent: warm gold (`#c9a84c`) — used sparingly for highlights
- No pure white, no pure black

**Mobile-first requirements:**
- Navigation collapses to hamburger on mobile (simple CSS-only toggle is fine)
- Audio players full-width on mobile
- CTA buttons minimum 44px touch target height
- All text readable without zooming

**Hero image:** Use a CSS background placeholder (`background-color: #2a6b6b`) until Luke O'Leary's illustration is provided. Add an HTML comment `<!-- TODO: replace background-color with background-image: url('/assets/images/hero.jpg') -->` so Charles can drop the image in.

---

## _config.yml

```yaml
title: Five Minutes on the Low Road
description: A new musical about near-death experience, empathy, and transformation. By Charles T. Betz.
url: "https://5mlowroad.com"
baseurl: ""
author: Charles T. Betz
email: char@charlestbetz.com

# Build settings
markdown: kramdown
theme: null  # Custom theme, no gem theme

plugins:
  - jekyll-seo-tag
  - jekyll-sitemap

# Exclude from build
exclude:
  - Gemfile
  - Gemfile.lock
  - README.md
  - claude-code-jekyll-prompt.md
```

---

## Navigation

Top nav links (in order): Listen · About · Stay in Touch · Contact

On mobile: hamburger toggle revealing the same links vertically.

The site title/logo in the nav ("Five Minutes on the Low Road") links to `/`.

---

## Footer

Every page footer contains:
1. Short email signup: "Stay in touch:" + Kit form inline (single email field + button), with `<!-- KIT_FORM_EMBED_HERE -->` placeholder
2. Copyright line: "© 2026 Charles T. Betz. All rights reserved."
3. Contact email: `char@charlestbetz.com`
4. Link to `/contact`

---

## SEO and Metadata

Use `jekyll-seo-tag` plugin. In `_layouts/default.html`, include `{% seo %}` in the `<head>`. Set meaningful `description` front matter on each page.

Add Open Graph tags for social sharing — the podcast page in particular should have `og:type: music.song` or `og:type: website` with the hero image as `og:image` once available.

---

## README.md

Write a practical README covering:
- What this site is
- How to run locally (`bundle exec jekyll serve`)
- How to add audio files (drop MP3s in `/assets/audio/`, update song cards)
- How to set up Kit form (where to paste the embed code)
- How to set up Formspree (where to paste the form ID)
- How to add hero image (where to update the CSS)
- How deployment works (push to main → GitHub Actions builds and deploys)
- DNS setup note: Cloudflare CNAME → `[github-username].github.io`

---

## What NOT to Build

- No blog/posts system (Jekyll posts disabled — this is not a blog)
- No ticketing or payment integration
- No social media feed embeds
- No comments
- No search
- No admin CMS
- No dependencies on external JS CDNs except Google Fonts

Keep it simple. This site needs to load fast on a conference attendee's phone on mediocre hotel WiFi.

---

## Deliverable Checklist

When done, confirm:
- [ ] `git log` shows initial commit with all files
- [ ] GitHub remote is set and `git push` has been run
- [ ] GitHub Actions workflow file is present and syntactically valid
- [ ] `CNAME` file contains `5mlowroad.com`
- [ ] All placeholder comments are clearly marked with `<!-- TODO -->` or `<!-- KIT_FORM_EMBED_HERE -->` etc.
- [ ] Site builds locally with `bundle exec jekyll serve` without errors
- [ ] `/go/listen` and `/go/subscribe` redirect correctly
- [ ] Mobile nav works on narrow viewport
- [ ] README explains all post-build setup steps Charles needs to take
