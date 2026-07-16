# Handoff — 5mlowroad.com Jekyll site

Copy everything below the line into a new Claude Code session started in
`/Users/char/code/5min` to continue the work.

---

You are picking up an in-progress build of the promotional website for **Five
Minutes on the Low Road**, a musical by Charles T. Betz. The full spec is in
`claude-code-jekyll-prompt.md` in this directory — read it if you need detail.
The site was built and verified end-to-end in a browser in a prior session.

## Current state (all committed on `main`, one commit)

- Full Jekyll site is built: pages (`index`, `listen`, `subscribe`, `about`,
  `contact`), `/go/listen` + `/go/subscribe` redirect stubs, layouts
  (`default`/`page`/`listen`), includes (`header`/`footer`/`audio-player`/
  `song-card`), `assets/css/main.css`, `_config.yml`, `Gemfile`, `CNAME`
  (`5mlowroad.com`), `README.md`, and `.github/workflows/jekyll.yml`
  (GitHub Actions Pages deploy via `jekyll-build-pages` + `deploy-pages`).
- Verified: `bundle exec jekyll build` runs clean; all routes 200; `/go/listen/`
  redirects to `/listen/`; desktop + mobile render correctly; mobile hamburger
  nav toggles open. Sitemap and `{% seo %}` metadata generate.
- The redirect stubs are `.html` (not `.md` as the original spec showed) because
  Kramdown mangles `<!DOCTYPE>` in markdown; the `permalink` keeps the
  `/go/...` URLs identical. Keep them as `.html`.

## Environment (important)

Local Jekyll requires the Homebrew Ruby, NOT macOS system Ruby (2.6, too old):

```bash
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

## What remains

1. **GitHub repo + push (blocked in prior session).** `gh`'s stored token is
   invalid, so the repo was never created or pushed. It needs an interactive
   `gh auth login` that Charles must run himself. Do NOT attempt to enter
   credentials. Once Charles has authenticated, the commands are:
   ```bash
   gh auth login -h github.com                 # Charles runs this
   gh repo create 5mlowroad --public --source=. --remote=origin --push
   ```
   Then on GitHub: Settings → Pages → Source: **GitHub Actions**.

2. **Placeholders Charles fills later** (all clearly marked in-file; documented
   in `README.md`): Kit form embed (`<!-- KIT_FORM_EMBED_HERE -->` in
   `subscribe.md` and `_includes/footer.html`), Formspree ID (`FORMSPREE_ID` in
   `contact.md`), podcast iframe (`<!-- PODCAST_PLAYER_EMBED_HERE -->` in
   `listen.md`), MP3s in `assets/audio/`, hero image swap in `main.css`,
   and copy marked `<!-- TODO -->` throughout. Only touch these if Charles
   provides the actual content.

## Rules of engagement

- Anything that publishes (repo creation, push, DNS) is Charles's call — confirm
  or hand him the exact commands; don't do it silently.
- Verify changes by building/serving and observing in the browser, not just by
  asserting success.
