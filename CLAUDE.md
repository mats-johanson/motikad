# Motikad - Motorbike Maintenance Log

Personal maintenance log for tracking service history, parts, and upkeep across motorbikes.

## Project Structure

- `bikes/` — one directory per bike, named by make-model (e.g., `bikes/ducati-monster-797/`)
- `shops.md` — local shop directory (shared across bikes)
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

## Conventions

- Dates are ISO 8601 (YYYY-MM-DD)
- Mileage in kilometers unless noted
- Costs in local currency, no symbol needed
- Keep entries factual and terse
