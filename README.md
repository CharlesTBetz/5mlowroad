# Five Minutes on the Low Road — website

Promotional website for **Five Minutes on the Low Road**, an original musical in
development by Charles T. Betz and Josiah Thomas Turner. Built with Jekyll and
deployed to GitHub Pages via GitHub Actions.

Live domain: **[5mlowroad.com](https://5mlowroad.com)**

The site's primary goal is email-list signup (ahead of a Kickstarter planned for
mid-to-late 2027); the secondary goal is letting people listen to the music. It
is the destination for two QR codes in a printed brochure distributed at the
IANDS conference (late August 2026):

- **Front door** QR → `5mlowroad.com/go/listen` → redirects to `/listen`
- **Back door** QR → `5mlowroad.com/go/subscribe` → redirects to `/subscribe`

The `/go/` pages are redirect stubs only. Their purpose is to let the QR
destination change later **without reprinting the brochure** — so edit the
`meta refresh` target in `go/listen.md` / `go/subscribe.md` instead of changing
the printed URLs.

---

## Run locally

Requires Ruby (3.x or newer recommended) and Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000>. Use `--livereload` for auto-refresh on edits.

> Note: local builds use the `jekyll` gem pinned in the `Gemfile`. Production
> deployment does **not** use this Gemfile — it builds with the
> `actions/jekyll-build-pages` GitHub Action (see below).

---

## Post-build setup checklist (things Charles needs to do)

### 1. Add music & video (YouTube)
The site is 100% YouTube for music — no self-hosted audio. Each song card takes
a `youtube="VIDEO_ID"`; without one it shows "Video coming soon." Videos are
click-to-load (a thumbnail facade swaps in a `youtube-nocookie` iframe only when
clicked, so nothing loads and no tracking fires until play).

- Home featured video: `index.md`
- Song list: `listen.md` (each `{% include song-card.html ... youtube="ID" %}`)
- Concept recording: drop `{% include youtube-embed.html id="ID" title="..." %}`
  into the "The concept recording" section of `listen.md` when that video exists.

### 2. Set up the Kit (ConvertKit) email form
Paste your Kit form embed code at every `<!-- KIT_FORM_EMBED_HERE -->` marker:

- `subscribe.md` — the primary, prominent signup form (email-only variant)
- `_includes/footer.html` — the compact inline footer widget (appears on every page)

No form ID is hardcoded anywhere — paste the full embed Kit gives you.

### 3. Set up the Formspree contact form
In `contact.md`, replace the placeholder `FORMSPREE_ID` in
`action="https://formspree.io/f/FORMSPREE_ID"` with your real Formspree form ID.

### 4. Hero image
The hero already uses Luke O'Leary's tunnel-of-light illustration
(`assets/images/hero.jpg`). To swap it, replace that file (keep the name), or
edit the `background-image` in the `.hero` rule in `assets/css/main.css`. A dark
gradient scrim is layered over the bottom for title legibility — adjust it there
if you change to a much darker or lighter image.

### 5b. Adding gallery images
Gallery images live in `assets/images/gallery/` and are listed by filename in
`gallery.md`. To add a new illustration: drop the file in that directory
(optimize large PNGs to JPG first — see the `magick ... -resize 1200x -quality 82`
commands used for the existing set), then add a `<figure class="gallery-item">`
block with an `<img>` and `<figcaption class="gallery-caption">` in `gallery.md`.
Source originals are kept in `source/` (excluded from the build).

### 6. Analytics (optional, off by default)
`_layouts/default.html` has a commented-out Plausible/GA snippet in `<head>`.
Uncomment and configure it if/when you want analytics.

---

## Deployment

Deployment is automatic: **push to `main`** and the GitHub Actions workflow at
`.github/workflows/jekyll.yml` builds the site with Jekyll and deploys it to
GitHub Pages.

One-time repo settings on GitHub: **Settings → Pages → Build and deployment →
Source: GitHub Actions.**

### DNS setup (Cloudflare)
The domain `5mlowroad.com` is registered at Cloudflare. The repo contains a
`CNAME` file with `5mlowroad.com` so GitHub Pages serves the custom domain.

In Cloudflare DNS, point the domain at GitHub Pages. The simplest approach:

- A `CNAME` record for the apex/`www` (or apex flattening) pointing to
  **`<github-username>.github.io`** (e.g. `charlestbetz.github.io`).
- Alternatively, the four GitHub Pages `A` records for the apex
  (`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`)
  plus a `CNAME` for `www`.

Set Cloudflare SSL/TLS mode to **Full** and let GitHub Pages issue its own
certificate (enable "Enforce HTTPS" in the Pages settings once the cert is
provisioned).

---

## Structure

```
_config.yml            Site config
_layouts/              default, page, listen
_includes/             header, footer, audio-player, song-card
assets/css/main.css    All styling (mobile-first, plain CSS)
assets/audio/          MP3s go here
assets/images/         Illustrations / photos go here
index.md               Home
listen.md              Front-door QR target
subscribe.md           Back-door QR target (primary CTA)
about.md               About the show and Charles
contact.md             Formspree contact form
go/listen.md           Redirect stub -> /listen
go/subscribe.md        Redirect stub -> /subscribe
CNAME                  5mlowroad.com
```

## What this site deliberately does not have

No blog, no ticketing/payment, no social embeds, no comments, no search, no CMS,
and no external JS beyond Google Fonts. It's built to load fast on a phone over
mediocre conference WiFi.
