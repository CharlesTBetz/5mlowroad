# Handoff — 5mlowroad.com (Jekyll site for *Five Minutes on the Low Road*)

Working dir: `/Users/char/code/5min`. This file is git-ignored from the *build*
but committed to the repo. Read `source/design-guide.md` and
`source/claude-code-jekyll-update-prompt.md` for the full design brief, and
`source/brochure.pdf` for the story/voice.

## Current state (2026-07-17): LIVE and redesigned

The site is deployed and verified at **https://5mlowroad.com**. Fully redesigned
to match the brochure + Luke O'Leary's illustrations. Last commit on `main`:
"Redesign to match brochure + Luke O'Leary illustrations" — pushed, Actions
deploy succeeded, live pages confirmed 200.

- **Repo:** https://github.com/CharlesTBetz/5mlowroad (public).
- **Deploy:** push to `main` → `.github/workflows/jekyll.yml` (GitHub Actions) builds
  and deploys to GitHub Pages. Runs green (Node/gem deprecation warnings are noise).
- **DNS/TLS:** domain is proxied through **Cloudflare** (not raw Pages A-records).
  Cloudflare terminates TLS, so GitHub's own cert state stays `none` — that's expected.
  "Always Use HTTPS" is on in Cloudflare.

### Design system (implemented in `assets/css/main.css`)
- Palette: indigo `#4b46b3` (links/CTAs), gold `#D4AA60` (show title/hover/dividers),
  lavender `#9B88BC`, copper `#C47860`, warm paper `#F5F2EE`, ink `#1C2340`. **No teal.**
- Type: **Cinzel** = show title only (`.show-title`, gold, uppercase); **Cormorant
  Garamond** = h1/h2/display; **EB Garamond** = body/h3+; **Gill Sans** system stack = nav/labels.
- Indigo masthead + footer; full-bleed hero (`assets/images/hero.jpg`, Luke's
  tunnel-of-light, with a bottom gradient scrim for gold-title legibility);
  spiral-ornament divider `{% include divider.html %}`; favicon = the luminous spiral.

### Pages
Home (`index.md`), Listen (song descriptions from the story), About (show-only),
**The Research** (`research.md` — NDE science, the IANDS-audience standout), **Gallery**
(`gallery.md` — 5 of Luke's pieces), **Team** (`team.md` — DRAFT bios, need Charles's edits),
Subscribe (styled fallback signup), Contact, + `/go/listen` `/go/subscribe` redirect stubs.

### Privacy: `source/` is git-ignored AND build-excluded
Brochure PDF + Luke's hi-res originals stay local only — never in the public repo or
the site. Web-optimized derivatives live in `assets/images/` (+ `gallery/`).

## What remains (Charles's — all marked in-file as HTML comments)

1. **Kit email form** (free ConvertKit). Create account at kit.com → Grow → Landing
   Pages & Forms → + Create New → Form → Inline → email-only → Publish/Embed → copy the
   HTML snippet. Paste it at the two `<!-- KIT_FORM_EMBED_HERE -->` markers
   (`subscribe.md` primary + `_includes/footer.html` compact) and delete the
   `.signup-fallback` block in subscribe.md. Free up to ~10k subscribers.
2. **Formspree ID** — replace `FORMSPREE_ID` in `contact.md`.
3. **Music/video** — 100% YouTube (no self-hosted audio). Add `youtube="ID"` to
   the song cards in `listen.md` (+ the featured card in `index.md`) as videos are
   produced; EWTD is live. Concept-recording video TBD.
4. **Team** — headshots + edit the two DRAFT bios in `team.md`.
5. **Gallery** — snowflake caption (`<!-- TODO: caption -->` in `gallery.md`).

## Environment quirks (this Mac) — IMPORTANT

- **Local dev/build needs Homebrew Ruby**, not system Ruby:
  `export PATH="/opt/homebrew/opt/ruby/bin:$PATH"` then `bundle exec jekyll serve --no-watch`
  (rebuild with `bundle exec jekyll build` after edits when using `--no-watch`).
- **git push:** three traps — an invalid `GITHUB_TOKEN` in `~/.zshrc`, a global
  `url.git@github.com:.insteadOf https://github.com/` rewrite, and blocked SSH port 22.
  Push recipe:
  ```
  git config --global --unset url.git@github.com:.insteadof
  env -u GITHUB_TOKEN git push origin main
  git config --global url."git@github.com:".insteadOf "https://github.com/"   # restore
  ```
  Use `env -u GITHUB_TOKEN gh ...` for all gh commands.
- **Screenshot verification:** headless Chrome exists at
  `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`. macOS enforces a
  ~500px min window width, so for true phone widths use CDP
  `Emulation.setDeviceMetricsOverride` (see /tmp/measure2.mjs pattern), not `--window-size`.
- Publishing (push, DNS, anything outward-facing) is Charles's call — confirm first.
