# Changelog

Human-readable summary of the site's major phases of work. Grouped by day, not
per commit: each entry is roughly a day's effort. Newest first.

This file is for maintainers and is excluded from the published build.

---

## 2026-08-13: Illustration finals, show credits, and house style

**Illustrations and credits**

- Replaced placeholder art with Luke O'Leary's **finished illustrations**: new
  hero and social-share image, and a rebuilt 7-piece gallery (Tanya the Tiger,
  In the ICU, the post-NDE character study, plus finals of the tunnel-of-light,
  garden, choice, and snowflake pieces). Retired the old "Tanya and Steve"
  sketch; kept the Rough Cuts production photo.
- Added the **orchestrations credit** (Ben Jossi, with website link), Luke
  O'Leary's portfolio link, and the "Loch Lomond" title etymology on Why Now.
- Added a **concept-brochure PDF download** on the home page; tightened the logline.
- Reconciled the site against brochure v1 (2026.08.11).

**Information architecture**

- Added a **Development & Team** page: the show's workshop and collaborator
  history (moved out of Why Now, which now links to it), the four bios, an
  Acknowledgements credits block, and the amalgam/disclaimer note. Development
  leads, bios follow. Closes with a line on the concept's other forms, linking
  the illustrations to the gallery and the in-progress novella to the brochure.
- Trimmed the top nav to five items with Gallery last
  (`Listen · Why Now · The Research · Development & Team · Gallery`); moved
  Contact and Stay in Touch to the footer and hero.

**House style (typography): decisions worth keeping**

- **No em dashes in reader-facing copy.** They read as an AI tell. Swept the whole
  site to zero, using commas, colons, ellipses, or parentheses as context
  warrants; the standing rule is no more than two site-wide. Rationale and rule
  recorded in `CLAUDE.md`. (This may relax over time.)
- **Ellipsis convention.** The website uses the single Unicode character `…`
  (U+2026), chosen for accessibility (screen readers announce it correctly) and
  because one glyph never breaks across a line. The print brochure instead uses
  narrow no-break spaced periods, which suit its Garamond setting. Brochure and
  site are maintained from **separate copy** and intentionally differ here; they
  are not reconciled.

## 2026-08-07: Content overhaul (Why Now, Research, polish)

- Merged the draft **"Why Now"** essay into the About page and renamed the page
  (and nav) from "About" to "Why Now."
- Overhauled the **Research** page: replaced unsourced statistics with
  Atwater-sourced figures, added a Sources section, restructured the aftereffects
  list, rewrote the author bio, and retitled the core section "Getting the NDE right."
- Baseline-aligned the wordmark and nav menu on desktop.
- Added the **Rough Cuts at Nautilus Music-Theater** (March 2026) photo to the gallery.
- Redeployed after a GitHub Actions/Pages outage.

## 2026-08-06: "Why Now" draft and contact change

- Drafted the **Why Now** page (staged, initially unpublished) and iterated on its copy.
- Changed the contact address to hello@5minlowroad.com.

## 2026-08-04: Domain move

- Moved the site to its production domain, **5minlowroad.com**.

## 2026-08-01: Print/web bridge

- Added **QR codes** (via segno) for `/go/listen` and `/go/subscribe`, linking the
  printed brochure to the site.

## 2026-07-18: Content, integrations, and email capture

- Rewrote **About** (car-crash setup, NDE prose, NMTE/Nautilus development status)
  and synced the homepage copy and logline to match.
- Added the **team** page (bios and headshots) with a Luke O'Leary placeholder, and
  linked "creative team" from About.
- Wired up email/contact plumbing: **Kit (ConvertKit)** signup form and a
  **Formspree** contact form.
- Added **Substack** links across the site.
- Switched all audio to **click-to-load YouTube** (removed self-hosted audio) and
  fixed the Listen song order to match the show.
- Replaced the favicon with a purpose-built high-contrast spiral.

## 2026-07-17: Brochure-aligned redesign

- Redesigned the site to match the **brochure and Luke O'Leary's illustrations**
  (color system, typography, hero treatment) and refined the hero composition and copy.

## 2026-07-16: Initial build

- Created the initial **5mlowroad.com Jekyll site** and session handoff doc.
