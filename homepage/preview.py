"""Assemble and check a temporary homepage + documentation site for local review."""

import argparse
import filecmp
import json
import shutil
import subprocess
import sys
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import unquote, urljoin, urlsplit


PROJECT = Path(__file__).resolve().parent
HOST = "https://zugbot.net"
HOME_ANCHORS = {"main-content", "hero-title", "features", "planner-title",
                "tools-title", "start-title", "support", "support-title"}


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


def files(root):
    return {p.relative_to(root) for p in root.rglob("*") if p.is_file()}


def check_links(site):
    pages = {path: Page(path) for path in site.rglob("*.html")}
    home = site / "index.html"
    missing = HOME_ANCHORS - pages[home].ids
    if missing:
        raise ValueError(f"Missing public homepage IDs: {sorted(missing)}")
    search = json.loads((site / "search/search_index.json").read_text(encoding="utf-8"))
    references = [(path, link) for path, page in pages.items() for link in page.links]
    references.extend((home, entry["location"] or "/") for entry in search["docs"])
    for origin, link in references:
        url = urlsplit(urljoin(f"{HOST}/{origin.relative_to(site).as_posix()}", link))
        if url.netloc != "zugbot.net" or url.scheme not in {"http", "https"}:
            continue
        target = site / unquote(url.path.lstrip("/"))
        if target.is_dir():
            target = target / "index.html"
        if not target.is_file():
            raise ValueError(f"{origin.relative_to(site)} links to missing {link}")
        if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            raise ValueError(f"{origin.relative_to(site)} links to missing fragment {link}")
    return len(pages), len(references)


def assemble(temp):
    baseline, site = temp / "mkdocs", temp / "review"
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict",
                    "--site-dir", str(baseline)], cwd=PROJECT.parent, check=True)
    astro = PROJECT / "dist"
    homepage = Path("index.html")
    astro_files = files(astro)
    if homepage not in astro_files:
        raise ValueError("Build the homepage first with npm run build in homepage/.")
    for path in astro_files - {homepage}:
        if path.parts[0] != "_zugbot" or (baseline / path).exists():
            raise ValueError(f"Unexpected Astro output or MkDocs collision: {path}")
    shutil.copytree(baseline, site)
    shutil.copytree(astro, site, dirs_exist_ok=True)
    docs_files = files(baseline)
    for path in docs_files - {homepage}:
        if not filecmp.cmp(baseline / path, site / path, shallow=False):
            raise ValueError(f"MkDocs output changed: {path}")
    pages, links = check_links(site)
    print(f"Verified {len(docs_files) - 1} unchanged MkDocs files, {pages} HTML files, "
          f"and {links} link, asset and search references.", flush=True)
    return site


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate and exit")
    parser.add_argument("--port", type=int, default=4321)
    args = parser.parse_args()
    with TemporaryDirectory(prefix="zugbot-review-") as directory:
        site = assemble(Path(directory))
        if args.check:
            return
        handler = partial(SimpleHTTPRequestHandler, directory=str(site))
        with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
            print(f"Local review at http://127.0.0.1:{server.server_port}/", flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    main()
