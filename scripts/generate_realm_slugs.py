#!/usr/bin/env python3
"""Generate the public realm-slug reference from Blizzard's Game Data API."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


SUPPORTED_REGIONS = ("us", "eu", "kr", "tw")
REGION_LOCALES = {
    "us": "en_US",
    "eu": "en_GB",
    "kr": "ko_KR",
    "tw": "zh_TW",
}
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "docs" / "assets" / "realm-slugs.json"
SOURCE_NAME = "Blizzard Game Data API realm index"


class GeneratorError(RuntimeError):
    """A safe, credential-free generation error."""


def request_json(request: Request) -> dict:
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as error:
        raise GeneratorError(f"Blizzard API returned HTTP {error.code}.") from error
    except (URLError, TimeoutError, json.JSONDecodeError) as error:
        raise GeneratorError("Blizzard API request failed or returned invalid JSON.") from error


def authenticate(region: str, client_id: str, client_secret: str) -> str:
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("ascii")
    request = Request(
        f"https://{region}.battle.net/oauth/token",
        data=urlencode({"grant_type": "client_credentials"}).encode("ascii"),
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "ZugBot realm reference generator",
        },
        method="POST",
    )
    payload = request_json(request)
    token = payload.get("access_token")
    if not isinstance(token, str) or not token:
        raise GeneratorError("Blizzard authentication response did not contain an access token.")
    return token


def display_name(value: object, locale: str) -> str | None:
    if isinstance(value, str) and value:
        return value
    if isinstance(value, dict):
        localized = value.get(locale)
        if isinstance(localized, str) and localized:
            return localized
        return next((item for item in value.values() if isinstance(item, str) and item), None)
    return None


def fetch_region(region: str, client_id: str, client_secret: str) -> list[dict[str, str]]:
    locale = REGION_LOCALES[region]
    token = authenticate(region, client_id, client_secret)
    query = urlencode({"namespace": f"dynamic-{region}", "locale": locale})
    request = Request(
        f"https://{region}.api.blizzard.com/data/wow/realm/index?{query}",
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "ZugBot realm reference generator",
        },
    )
    payload = request_json(request)
    records: dict[str, dict[str, str]] = {}
    for raw_realm in payload.get("realms", []):
        if not isinstance(raw_realm, dict):
            continue
        name = display_name(raw_realm.get("name"), locale)
        slug = raw_realm.get("slug")
        if name and isinstance(slug, str) and slug:
            records.setdefault(slug.casefold(), {"region": region, "name": name, "slug": slug})
    if not records:
        raise GeneratorError(f"Blizzard returned no usable realms for region {region}.")
    return list(records.values())


def write_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary_name = temporary.name
            json.dump(payload, temporary, ensure_ascii=False, indent=2)
            temporary.write("\n")
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_name, path)
    finally:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--regions",
        nargs="+",
        choices=SUPPORTED_REGIONS,
        default=list(SUPPORTED_REGIONS),
        help="Regions to include (default: us eu kr tw).",
    )
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    client_id = os.environ.get("BLIZZARD_CLIENT_ID")
    client_secret = os.environ.get("BLIZZARD_CLIENT_SECRET")
    if not client_id or not client_secret:
        print("BLIZZARD_CLIENT_ID and BLIZZARD_CLIENT_SECRET must be set in the environment.", file=sys.stderr)
        return 2

    regions = list(dict.fromkeys(args.regions))
    realms: list[dict[str, str]] = []
    try:
        for region in regions:
            realms.extend(fetch_region(region, client_id, client_secret))
    except GeneratorError as error:
        print(f"Realm generation failed: {error}", file=sys.stderr)
        return 1

    realms.sort(key=lambda item: (item["region"], item["name"].casefold(), item["slug"].casefold()))
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "regions": regions,
        "source": SOURCE_NAME,
        "realms": realms,
    }
    write_atomic(args.output.resolve(), payload)
    counts = {region: sum(1 for realm in realms if realm["region"] == region) for region in regions}
    print(f"Wrote {len(realms)} realms to {args.output.resolve()} ({counts}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
