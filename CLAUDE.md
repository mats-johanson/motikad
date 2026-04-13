# Motikad - Motorbike Maintenance Log

Personal maintenance log for tracking service history, parts, and upkeep across motorbikes.

## Project Structure

- `bikes/` — one directory per bike, named by make-model (e.g., `bikes/ducati-monster-797/`)
- `shops.md` — local shop directory (shared across bikes)
- `riding/` — route planning, motocamping, and tools
  - `routes.md` — routes organized by duration and bike suitability
  - `motocamping.md` — camping sites, wild camping rules, gear checklist
  - `apps.md` — navigation, camping, weather, and utility apps
  - `menus.md` — camp meal recipes (1L pot + pan, serves 2)
- Each bike directory contains:
  - `README.md` — bike details, specs, known model quirks
  - `maintenance.md` — chronological maintenance log (newest first), pending items at top
  - `parts.md` — parts inventory: installed, on order, needed, consumables
  - `technical-notes.md` — model-specific knowledge and reference
  - `docs/` — manuals, invoices, spreadsheets (original files from seller, shops, etc.)
  - `photos/` — bike photos

## Maintenance Log Format

Each entry in `maintenance.md` follows this format:

```markdown
## YYYY-MM-DD — [Summary]

- **Mileage:** [odometer reading]
- **Type:** [routine | repair | upgrade | inspection]
- **Work done:**
  - [item]
- **Parts used:**
  - [part name] — [part number if known]
- **Cost:** [amount]
- **Shop/Self:** [shop name or "self"]
- **Notes:** [optional]
```

## Dashboard

`index.html` is the website homepage dashboard — it must reflect current state at all times. When updating any bike's `maintenance.md` or `parts.md`, also update the corresponding section in `index.html`:

- **Bike cards** — status should reflect current rideable/not rideable state
- **"What needs doing"** — mirrors the `## Pending` sections from each bike's `maintenance.md`

`README.md` is the GitHub landing page — keep it minimal (bikes + link to website). Don't duplicate the dashboard there.

## Git Workflow

When asked to push, do everything in one go without pausing for confirmation:

1. Create a feature branch from main
2. Commit changes
3. Push the branch
4. Create a PR and merge it immediately
5. Switch back to main and pull

## Hosting

- Site served via GitHub Pages with Jekyll, auto-built from main branch
- Layout: `_layouts/default.html`, styles: `assets/css/style.css`, config: `_config.yml`
- No build step — push to main and GitHub builds automatically
- Homepage is `index.html` (HTML, not markdown) — full layout control with cards, grids, sidebar nav
- Sub-pages render from markdown via GitHub Pages plugins: `jekyll-optional-front-matter`, `jekyll-relative-links`, `jekyll-titles-from-headings`
- `README.md` is excluded from build (GitHub-only landing page)

## Conventions

- Dates are ISO 8601 (YYYY-MM-DD)
- Mileage in kilometers unless noted
- Costs in local currency, no symbol needed
- Keep entries factual and terse
