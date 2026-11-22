"""MkDocs export hook for Astro's guide pages (mkdocs.export.yml)."""

import json
from html.parser import HTMLParser
from pathlib import Path


class HeadingLabel(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.parts = []
        self.feed(markup)
        self.close()

    def handle_data(self, data):
        self.parts.append(data)


def headings(toc):
    for item in toc:
        yield {"id": item.id, "text": "".join(HeadingLabel(item.title).parts), "level": item.level}
        yield from headings(item.children)


def on_page_context(context, *, page, config, nav):
    if page.is_homepage:
        return
    items = list(headings(page.toc))
    title = next(item["text"] for item in items if item["level"] == 1)
    route = "/" + page.url
    guide = {"slug": route.strip("/"), "route": route, "title": title,
             "html": page.content, "headings": items}
    output = Path(config.site_dir) / ".guide-export" / page.file.dest_uri
    output = output.with_suffix(".json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(guide, ensure_ascii=False), encoding="utf-8")
