# Motikad - Motorbike Maintenance Log

Personal maintenance log for tracking service history, parts, and upkeep across motorbikes.

## Project Structure

- `bikes/` — one directory per bike, named by make-model
- `shops.md` — local shop directory (shared across bikes)
- `riding/` — route planning and trip preparation
  - `routes.md` — routes organized by duration and bike suitability
  - `trip-prep.md` — camping rules, gear checklist, apps & tools (merged reference for trip planning)
  - `menus.md` — camp meal recipes (1L pot + pan, serves 2)
- Each bike directory contains:
  - `overview.md` — bike dashboard: photo, key specs, status, last service
  - `todo.md` — prioritized pending items with full diagnostic context
  - `history.md` — completed maintenance log (newest first) + prior owner work
  - `parts.md` — parts inventory grouped by category: installed, on order, needed
  - `reference.md` — stable knowledge: mods, specs, procedures, KOSO dash, troubleshooting
  - `issues.md` — active investigations with status (Transalp only, currently)
  - `docs/` — manuals, invoices, spreadsheets
  - `photos/` — bike photos

## Service History Format

Each entry in `history.md` follows this format:

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

## Todo Format

Each item in `todo.md` uses priority pills:

```html
- <b class="p now">Now</b> **Item** — description
- <b class="p soon">Soon</b> **Item** — description
- <b class="p later">Later</b> **Item** — description
```

Priority classes: `now` (red), `deadline` (red), `soon`/`quick` (amber), `later`/`next` (grey).

Todo items with meaningful diagnostic context should link to a detailed entry in `issues.html` (anchored by id). The todo stays concise — one-liner with a link. The issues page holds the full write-up: observations, diagnosis, what was tried, next steps.

## Dashboard

`index.html` is the website homepage dashboard — it must reflect current state at all times. When updating any bike's `todo.md` or `parts.md`, also update the corresponding section in `index.html`:

- **Bike cards** — status should reflect current rideable/not rideable state
- **"What needs doing"** — mirrors each bike's `todo.md`

`README.md` is the GitHub landing page — keep it minimal. Don't duplicate the dashboard there.

## Git Workflow

When asked to push, do everything in one go without pausing for confirmation:

1. Create a feature branch from main
2. Commit changes
3. Push the branch
4. Create a PR and merge it immediately
5. Switch back to main and pull

## Hosting

- Site served via GitHub Pages with Jekyll, auto-built from main branch
- Layout: `_layouts/default.html` (sidebar nav), styles: `assets/css/style.css`, config: `_config.yml`
- No build step — push to main and GitHub builds automatically
- Homepage is `index.html` (HTML, not markdown) — sidebar nav, card grids, dashboard layout
- Sub-pages render from markdown via GitHub Pages plugins: `jekyll-optional-front-matter`, `jekyll-relative-links`, `jekyll-titles-from-headings`
- `README.md` is excluded from build (GitHub-only landing page)

## Conventions

- Dates are ISO 8601 (YYYY-MM-DD)
- Mileage in kilometers unless noted
- Costs in local currency, no symbol needed
- Keep entries factual and terse
