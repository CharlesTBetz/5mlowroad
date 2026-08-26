# Working notes for this repo (5minlowroad.com)

Operational guidance for Claude sessions. Not published (excluded from the Jekyll build).

## ⚠️ Two machines share this repo — ALWAYS sync first
Charles works this repo from **two machines**: this Mac Pro and a **Mac Mini**
(the Mini runs Claude on an ongoing basis and commits under the legacy name
**"Kyoshi" <noreply@kyoshi.local>**). Both push to the same `origin`.

Because of this, a local clone can silently fall behind by many commits.
**Before doing any work, run `git fetch` and check `git status` / `git log --oneline origin/main`.**
If behind, integrate before starting — don't build on a stale base (it causes
duplicated work and messy divergences).

## Deploy
- Prod is **GitHub Actions → GitHub Pages** at **5minlowroad.com** (see
  `.github/workflows/jekyll.yml` and `CNAME`). **Pushing to `main` deploys to prod.**
- Confirm with Charles before pushing; never force-push `main`.

## Git remote / networks
- `origin` is **SSH**, routed **over port 443** (`~/.ssh/config` points
  `github.com` → `ssh.github.com:443`) so it works even where port 22 is blocked
  (campus, hotel, airplane Wi-Fi). Nothing to toggle.
- **HTTPS pushes are intentionally NOT set up as a fallback.** They fail with 403
  because `~/.zshrc` exports a `read:packages`-only `GITHUB_TOKEN` that shadows the
  good credential. If SSH ever fails on some network, deal with it then (e.g., a
  one-off HTTPS remote with a `repo`-scoped PAT) — don't add a permanent toggle.

## Build / run locally
- System Ruby (2.6) **cannot** build this — its bundler is too old.
- Use **Homebrew Ruby 4.0.x**:
  ```
  export PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/4.0.0/bin:$PATH"
  bundle exec jekyll serve   # or: bundle exec jekyll build
  ```

## Content sources of truth
- The **brochure** and **design guide** are the canonical references (in Dropbox:
  `music/Projects/5 minutes/promo/brochure/brochure.pdf` and
  `.../promo/website/design-guide.md`). Reconcile site copy/credits against them.
- Illustrations come from **Luke O'Leary** (`.../graphics/Luke/<yyyymmdd>/`),
  delivered as large PNGs. Downscale to web JPGs before committing:
  gallery pieces ~1600px long edge at q82; hero cropped to 1600×1342.
  Originals are NOT committed (kept in Dropbox / `source/`).

## Writing style
- **Never use em dashes** (`—` / `&mdash;`) in site copy. They read as an AI tell.
- **When a parenthetical/dash pause is wanted, use a literal double-hyphen `--`**
  (Charles's deliberate "reverse AI tell"), e.g. `On the Low Road -- my Substack -- is…`.
  Commas/colons/ellipses/parentheses are also fine where they read better.
- Kramdown gotcha: `--` stays literal inside block HTML (`<p>`, `<div>`) — which is how
  the subscribe/lyric copy is authored — but in **plain markdown prose** kramdown may
  auto-convert `--` to an en dash. If you need a literal `--` in prose, wrap it in an
  HTML element or write `&#45;&#45;`. Verify in the built HTML.
- En dashes in numeric ranges (e.g. `2023–2025`) and ordinary hyphens are fine.
- This preference may relax over time, per Charles.
- **Ellipses on the website: use the single Unicode character `…` (U+2026).** Chosen
  for accessibility (screen readers announce it correctly) and because one glyph never
  breaks across a line. The print brochure instead uses narrow no-break spaced periods
  (a period, U+202F narrow no-break space, repeated), which suits its Garamond
  typesetting. The brochure and the site are maintained from **separate copy** and
  intentionally differ here. Do not try to reconcile them.

## Housekeeping
- Keep **CHANGELOG.md** current at day-level granularity (major phases, not per-commit).
- Excluded from the build: `README.md`, `HANDOFF.md`, `CHANGELOG.md`, `CLAUDE.md`,
  `source/`, Gemfiles, `vendor/` (see `_config.yml`).
