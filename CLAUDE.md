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

## Housekeeping
- Keep **CHANGELOG.md** current at day-level granularity (major phases, not per-commit).
- Excluded from the build: `README.md`, `HANDOFF.md`, `CHANGELOG.md`, `CLAUDE.md`,
  `source/`, Gemfiles, `vendor/` (see `_config.yml`).
