"""Serve the complete static Pages artifact locally, including its 404 page."""

import argparse
import webbrowser
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


SITE = Path(__file__).resolve().parent / "dist"


class PagesHandler(SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code != HTTPStatus.NOT_FOUND:
            return super().send_error(code, message, explain)
        body = (SITE / "404.html").read_bytes()
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def list_directory(self, path):
        self.send_error(HTTPStatus.NOT_FOUND)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=4321)
    parser.add_argument("--open", action="store_true", help="open the local review in a browser")
    parser.add_argument("--check", action="store_true", help="build and validate the artifact, then exit")
    args = parser.parse_args()
    if args.check:
        from build import build
        build()
        parser.exit()
    if not (SITE / "404.html").exists():
        parser.exit(1, "Build the complete site first with python homepage/build.py.\n")
    with ThreadingHTTPServer(("127.0.0.1", args.port), partial(PagesHandler, directory=str(SITE))) as server:
        url = f"http://127.0.0.1:{server.server_port}/"
        print(f"Local review at {url}", flush=True)
        if args.open:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
