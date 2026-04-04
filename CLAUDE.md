# Motikad - Motorbike Maintenance Log

Personal maintenance log for tracking service history, parts, and upkeep across motorbikes.

## Project Structure

- `bikes/` — one directory per bike, named by make-model (e.g., `bikes/ducati-monster-797/`)
- `shops.md` — local shop directory (shared across bikes)
- `riding/` — route planning, motocamping, and tools
  - `routes.md` — routes organized by duration and bike suitability
  - `motocamping.md` — camping sites, wild camping rules, gear checklist
  - `apps.md` — navigation, camping, weather, and utility apps
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

## README Dashboard

`README.md` is the front page — it must reflect current state at all times. When updating any bike's `maintenance.md` or `parts.md`, also update the corresponding section in README:

- **Bike table** — status column should reflect current rideable/not rideable state
- **"What needs doing"** — mirrors the `## Pending` sections from each bike's `maintenance.md`, prioritized (Now → Soon → Later → Next season)
- **"Shopping list"** — mirrors `## Needed` tables from each bike's `parts.md`

If an item is completed, remove it from README. If a new item is added, add it to README in the right priority slot.

## Git Workflow

When asked to push, do everything in one go without pausing for confirmation:

1. Create a feature branch from main
2. Commit changes
3. Push the branch
4. Create a PR and merge it immediately
5. Switch back to main and pull

## Conventions

- Dates are ISO 8601 (YYYY-MM-DD)
- Mileage in kilometers unless noted
- Costs in local currency, no symbol needed
- Keep entries factual and terse
