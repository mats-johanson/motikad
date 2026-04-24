#!/usr/bin/env python3
"""Local preview for motikad without a full Jekyll install.

Jekyll renders the live site on push to main, but iterating locally is painful
without a Ruby/Bundler setup. This script does the minimum Liquid processing
needed to render a visually-accurate preview of any HTML page in the repo.

What it does:
  - Walks the repo, finds every `.html` file with YAML front matter
  - Strips front matter, substitutes `{{ '/path' | relative_url }}` → `/path`,
    drops unsupported Liquid tags (control flow, expressions), wraps the
    content in `_layouts/<layout>.html`, and writes the result mirrored into
    `.preview/` at the project root
  - `.preview/` is gitignored. Re-run this script after any edit.

What it does NOT do:
  - No Liquid `{% if %}`, `{% for %}`, `{% assign %}` — those are stripped.
    Pages that rely on Liquid logic (currently just `_layouts/default.html`
    for sidebar active-state highlighting) will render without the dynamic
    bits, but layout and content still appear.
  - No `baseurl` — links resolve against the server root at localhost:4001.
    That matches the local dev setup, NOT the deployed /motikad/ path.

Usage:
  python3 _preview/preview.py              # build only
  python3 _preview/preview.py --serve      # build + start server on :4001

Then open http://localhost:4001/.preview/<page-path>.
Example: http://localhost:4001/.preview/bikes/honda-transalp-650/procedures.html
"""
from __future__ import annotations

import argparse
import http.server
import os
import re
import socketserver
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".preview"

# Dirs to skip when walking the repo for source HTML
SKIP_DIRS = {
    ".preview",
    "_preview",
    "_site",
    "_layouts",
    "_includes",
    ".git",
    ".idea",
    ".claude",
    ".playwright-mcp",
    "node_modules",
    ".jekyll-cache",
}

LIQUID_URL = re.compile(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}")
LIQUID_EXPR = re.compile(r"\{\{[^}]*\}\}")
LIQUID_TAG = re.compile(r"\{%[^%]*%\}")


def strip_frontmatter(text: str) -> tuple[str, dict[str, str]]:
    meta: dict[str, str] = {}
    if not text.startswith("---"):
        return text, meta
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text, meta
    for line in parts[1].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return parts[2].lstrip(), meta


def substitute_liquid(text: str) -> str:
    text = LIQUID_URL.sub(r"\1", text)
    text = LIQUID_EXPR.sub("", text)
    text = LIQUID_TAG.sub("", text)
    return text


def render(source: Path) -> str | None:
    raw = source.read_text()
    if not raw.startswith("---"):
        return None  # no front matter, not a Jekyll page
    body, meta = strip_frontmatter(raw)
    body = substitute_liquid(body)

    layout_name = meta.get("layout", "default")
    layout_path = ROOT / "_layouts" / f"{layout_name}.html"
    if not layout_path.exists():
        return body

    html = layout_path.read_text().replace("{{ content }}", body)
    html = substitute_liquid(html)
    title = meta.get("title", "")
    html = html.replace("<title> · </title>", f"<title>{title}</title>")
    return html


def discover_pages() -> list[Path]:
    pages: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".html"):
                pages.append(Path(dirpath) / name)
    return pages


def build() -> int:
    count = 0
    for page in discover_pages():
        rel = page.relative_to(ROOT)
        html = render(page)
        if html is None:
            continue
        out = OUT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        count += 1
    print(f"Rendered {count} pages into {OUT.relative_to(ROOT)}/")
    return count


def serve(port: int = 4001) -> None:
    os.chdir(ROOT)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving {ROOT} at http://localhost:{port}/")
        print(f"Open e.g. http://localhost:{port}/.preview/index.html")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


def main() -> int:
    parser = argparse.ArgumentParser(description="motikad local preview builder")
    parser.add_argument("--serve", action="store_true", help="start HTTP server after building")
    parser.add_argument("--port", type=int, default=4001, help="server port (default 4001)")
    args = parser.parse_args()

    build()
    if args.serve:
        serve(args.port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
