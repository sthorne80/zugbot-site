"""Validate a built ZugBot site against its independent MkDocs reference build."""

import filecmp
import gzip
import json
import re
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree as ET


ORIGIN = "https://zugbot.net"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
HOME_ANCHORS = {"main-content", "hero-title", "features", "planner-title",
                "tools-title", "start-title", "support", "support-title"}
LEGACY_GUIDES = {
    "admin-guide", "changelog", "commands", "discord-activity", "forever", "getting-started",
    "member-guide", "peon-fight-club", "planner", "privacy", "realm-slugs", "roadmap",
    "terms", "troubleshooting", "verification",
}
PRODUCT_PAGES = {
    "/": "ZugBot",
    "/features/": "Features",
    "/guild-command-center/": "Guild Command Center",
    "/tavern/peon-fight-club/": "Peon Fight Club",
    "/guild-planner/": "Guild Planner",
    "/characters-and-groups/": "Characters & Groups",
    "/get-started/": "Get Started",
    "/support/": "Support",
    "/documentation/": "Documentation",
}


def public_route(path, site):
    return "/" + path.relative_to(site).as_posix().removesuffix("index.html")


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.canonicals = []
        self.title = []
        self.main_text = []
        self.guide = None
        self.has_guide_marker = False
        self.h1s = 0
        self.in_title = self.in_main = False
        self.article_depth = self.skip_depth = 0
        self.source = path.read_text(encoding="utf-8")
        self.line_starts = [0, *(m.end() for m in re.finditer("\n", self.source))]
        self.feed(self.source)
        self.close()

    def source_offset(self):
        line, column = self.getpos()
        return self.line_starts[line - 1] + column

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                raise ValueError(f"Duplicate HTML ID: {attrs['id']}")
            self.ids.add(attrs["id"])
        for key in ("href", "src", "action", "poster"):
            if attrs.get(key):
                self.links.append(attrs[key])
        srcset = attrs.get("srcset", "")
        if srcset and not srcset.startswith("data:"):
            self.links.extend(item.strip().split()[0] for item in srcset.split(",") if item.strip())
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonicals.append(attrs.get("href"))
        if tag == "h1":
            self.h1s += 1
        if tag == "title":
            self.in_title = True
        if tag == "main":
            self.in_main = True
        if tag in {"script", "style", "svg", "nav"}:
            self.skip_depth += 1
        if tag == "article":
            if self.article_depth:
                self.article_depth += 1
            elif "data-guide-content" in attrs or "md-content__inner" in attrs.get("class", "").split():
                self.article_depth = 1
                self.has_guide_marker = "data-guide-content" in attrs
                self.body_start = self.source_offset() + len(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "main":
            self.in_main = False
        if tag in {"script", "style", "svg", "nav"}:
            self.skip_depth -= 1
        if tag == "article" and self.article_depth:
            self.article_depth -= 1
            if not self.article_depth:
                # Strip template padding around the article. Preserve inner HTML,
                # including whitespace in code and spaces around inline links.
                self.guide = self.source[self.body_start:self.source_offset()].strip()

    def handle_data(self, data):
        if self.in_title and not self.skip_depth:
            self.title.append(data)
        if self.in_main and not self.skip_depth and data.strip():
            self.main_text.append(data.strip())


def read_pages(site):
    pages = {}
    for file in sorted(site.rglob("*.html")):
        route = public_route(file, site)
        try:
            pages[route] = Page(file)
        except ValueError as error:
            raise ValueError(f"{route}: {error}") from error
    return pages


def check_reference(site, pages, origin, link):
    url = urlsplit(urljoin(ORIGIN + origin, link))
    if url.netloc != "zugbot.net" or url.scheme not in {"http", "https"}:
        return
    target = site / unquote(url.path.lstrip("/"))
    if target.is_dir():
        target = target / "index.html"
    if not target.is_file():
        raise ValueError(f"{origin} references missing file: {link}")
    page = pages.get(public_route(target, site))
    if page and url.fragment and unquote(url.fragment) not in page.ids:
        raise ValueError(f"{origin} references missing section: {link}")


def validate(site, baseline, guides, pages):
    guide_routes = {guide["route"] for guide in guides}
    expected = set(PRODUCT_PAGES) | guide_routes | {"/404.html"}
    if set(pages) != expected:
        raise ValueError(f"Unexpected or missing HTML routes: {set(pages) ^ expected}")
    if not {f"/{slug}/" for slug in LEGACY_GUIDES} <= guide_routes:
        raise ValueError("The export is missing a legacy guide.")
    if guide_routes & PRODUCT_PAGES.keys():
        raise ValueError("A product route collides with a guide.")
    if not HOME_ANCHORS <= pages["/"].ids:
        raise ValueError(f"Missing homepage bookmarks: {HOME_ANCHORS - pages['/'].ids}")
    for route, page in pages.items():
        if page.h1s != 1:
            raise ValueError(f"{route}: expected one H1, found {page.h1s}")
        if route != "/404.html" and page.canonicals != [ORIGIN + route]:
            raise ValueError(f"{route}: unexpected canonical {page.canonicals}")
        if route in guide_routes:
            reference = Page(baseline / route.strip("/") / "index.html")
            if not page.has_guide_marker or not reference.guide or reference.guide != page.guide:
                raise ValueError(f"{route}: guide content differs from the MkDocs article")
        for link in page.links:
            check_reference(site, pages, route, link)
    index = json.loads((site / "search/search_index.json").read_text(encoding="utf-8"))
    indexed = set()
    for record in index["docs"]:
        link = "/" + record["location"].lstrip("/")
        check_reference(site, pages, "/", link)
        indexed.add(urlsplit(link).path)
    expected_index = expected - {"/404.html"}
    if indexed != expected_index:
        raise ValueError(f"Search coverage differs: {indexed ^ expected_index}")
    xml = (site / "sitemap.xml").read_bytes()
    if gzip.decompress((site / "sitemap.xml.gz").read_bytes()) != xml:
        raise ValueError("The compressed sitemap differs from the XML.")
    locations = [el.text for el in ET.fromstring(xml).iter(f"{{{SITEMAP_NS}}}loc")]
    if sorted(locations) != sorted(ORIGIN + route for route in expected_index):
        raise ValueError("The sitemap does not match the canonical public routes.")
    for original in (baseline / "assets").rglob("*"):
        if original.is_file() and not filecmp.cmp(original, site / original.relative_to(baseline),
                                                  shallow=False):
            raise ValueError(f"Legacy asset changed: {original.relative_to(baseline)}")
    for sheet in site.rglob("*.css"):
        for match in re.finditer(r"""url\(\s*['"]?([^)'"]+?)['"]?\s*\)""", sheet.read_text(encoding="utf-8")):
            check_reference(site, pages, "/" + sheet.relative_to(site).as_posix(), match.group(1))
    print(f"Validated {len(pages)} HTML routes, {len(guide_routes)} complete guide articles, "
          f"{len(index['docs'])} search records, links, legacy assets and both sitemaps.", flush=True)
