"""Build the complete static site, or prepare MkDocs content for Astro dev."""

import argparse
import filecmp
import gzip
import json
import os
import shutil
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from xml.etree import ElementTree as ET

from check_site import ORIGIN, PRODUCT_PAGES, SITEMAP_NS, read_pages, validate


PROJECT = Path(__file__).resolve().parent
REPO = PROJECT.parent
SEARCH = Path("search/search_index.json")
METADATA = {SEARCH, Path("sitemap.xml"), Path("sitemap.xml.gz")}


@contextmanager
def build_lock():
    # Dev preparation and release builds share generated input. An OS lock is
    # released even if a build is interrupted or its process is terminated.
    with (PROJECT / ".build.lock").open("a+b") as lock:
        try:
            if os.name == "nt":
                import msvcrt
                lock.seek(0)
                msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            raise RuntimeError("Another site build is using this checkout.") from error
        yield


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def install_tree(source, destination, scratch):
    """Retain the previous successful tree until its replacement is ready."""
    previous = scratch / ("previous-" + destination.name)
    if destination.exists():
        destination.rename(previous)
    try:
        source.rename(destination)
    except OSError:
        if previous.exists():
            previous.rename(destination)
        raise


def write_index(directory, original, product_entries):
    # Keep section-level guide records and discard MkDocs' superseded home records.
    records = [entry for entry in original["docs"] if entry["location"].split("#", 1)[0]]
    save_json(directory / SEARCH, {**original, "docs": [*records, *product_entries]})


def prepare(scratch):
    baseline = scratch / "mkdocs"
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file",
                    "mkdocs.export.yml", "--site-dir", str(baseline)], cwd=REPO, check=True)
    generated = scratch / "generated"
    exports = sorted((baseline / ".guide-export").rglob("*.json"))
    guides = [json.loads(file.read_text(encoding="utf-8")) for file in exports]
    if not guides:
        raise ValueError("MkDocs produced no guide content.")
    save_json(generated / "guides.json", guides)
    public = generated / "public"
    shutil.copytree(PROJECT / "public", public)
    for item in public.rglob("*"):
        if item.is_file() and (item.suffix == ".html" or item.relative_to(public) in METADATA):
            raise ValueError(f"Static file would overwrite a generated page, index or sitemap: {item}")
    for file in baseline.rglob("*"):
        path = file.relative_to(baseline)
        if not file.is_file() or path.parts[0] == ".guide-export" or path.suffix == ".html" or path in METADATA:
            continue
        if (public / path).exists():
            raise ValueError(f"Public assets collide at {path}")
        (public / path).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, public / path)
    search = json.loads((baseline / SEARCH).read_text(encoding="utf-8"))
    dev_products = [{"location": route.lstrip("/"), "title": title, "text": title}
                    for route, title in PRODUCT_PAGES.items()]
    write_index(public, search, dev_products)
    write_sitemaps(public, set(PRODUCT_PAGES) | {guide["route"] for guide in guides})
    install_tree(generated, PROJECT / ".generated", scratch)
    print(f"Prepared {len(guides)} guides and their original assets for Astro.", flush=True)
    return baseline, guides, search


def write_sitemaps(site, pages):
    ET.register_namespace("", SITEMAP_NS)
    root = ET.Element(f"{{{SITEMAP_NS}}}urlset")
    for route in sorted(set(pages) - {"/404.html"}):
        entry = ET.SubElement(root, f"{{{SITEMAP_NS}}}url")
        ET.SubElement(entry, f"{{{SITEMAP_NS}}}loc").text = ORIGIN + route
    xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    (site / "sitemap.xml").write_bytes(xml)
    (site / "sitemap.xml.gz").write_bytes(gzip.compress(xml, mtime=0))


def build(prepare_only=False):
    with build_lock(), TemporaryDirectory(prefix=".build-", dir=PROJECT) as temp:
        scratch = Path(temp)
        baseline, guides, search = prepare(scratch)
        if prepare_only:
            return
        candidate = scratch / "astro"
        astro_package = PROJECT / "node_modules/astro"
        package = json.loads((astro_package / "package.json").read_text(encoding="utf-8"))
        environment = os.environ.copy()
        environment.setdefault("ASTRO_TELEMETRY_DISABLED", "1")
        subprocess.run(["node", str(astro_package / package["bin"]["astro"]), "build",
                        "--outDir", str(candidate)], cwd=PROJECT, env=environment, check=True)
        public = PROJECT / ".generated/public"
        for file in public.rglob("*"):
            if file.is_file():
                destination = candidate / file.relative_to(public)
                if not destination.is_file() or not filecmp.cmp(file, destination, shallow=False):
                    raise ValueError(f"Build did not preserve public asset: {file.relative_to(public)}")
        pages = read_pages(candidate)
        entries = [{"location": route.lstrip("/"), "title": "".join(pages[route].title).strip(),
                    "text": " ".join(pages[route].main_text)}
                   for route in PRODUCT_PAGES if route in pages]
        write_index(candidate, search, entries)
        write_sitemaps(candidate, pages)
        validate(candidate, baseline, guides, pages)
        install_tree(candidate, PROJECT / "dist", scratch)
        print("Complete site ready in homepage/dist/.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare", action="store_true", help="only export guide and development data")
    build(prepare_only=parser.parse_args().prepare)
