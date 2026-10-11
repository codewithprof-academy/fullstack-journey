"""Week 01 · Demo D4 — "You are the server".

A tiny web server that prints every request it receives, so students can SEE
the request/response conversation.  Python standard library only.

Run:   python3 tiny_server.py            (then open http://localhost:8000)
Stop:  Ctrl + C
"""
import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000

HOME_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Hello from the server</title></head>
<body style="font-family: system-ui; max-width: 40rem; margin: 3rem auto;">
  <h1>Hello from the server!</h1>
  <p>Your browser sent a <strong>request</strong>. This page is the <strong>response</strong>.</p>
  <ul>
    <li><a href="/about">/about</a> &ndash; another page</li>
    <li><a href="/api/time">/api/time</a> &ndash; an API: data for programs, not people</li>
    <li><a href="/does-not-exist">/does-not-exist</a> &ndash; what happens when nothing is there?</li>
  </ul>
</body></html>"""

ABOUT_PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>About</title></head>
<body style="font-family: system-ui; max-width: 40rem; margin: 3rem auto;">
<h1>About this server</h1><p>It runs on the instructor's laptop. In the cloud, it would run in a data centre.</p>
<p><a href="/">Back home</a></p></body></html>"""


class LoggingHandler(BaseHTTPRequestHandler):
    server_version = "NextGenTinyServer/1.0"

    def _send(self, status: int, body: str, content_type: str) -> None:
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(data)
        print(f"  <- RESPONSE {status} {self.responses[status][0]} ({content_type}, {len(data)} bytes)\n")

    def _log_request(self) -> None:
        print(f"-> REQUEST from {self.client_address[0]}: {self.command} {self.path}")
        for name in ("Host", "User-Agent", "Accept"):
            if self.headers.get(name):
                print(f"     {name}: {self.headers[name][:70]}")

    def do_GET(self) -> None:
        self._log_request()
        if self.path == "/":
            self._send(200, HOME_PAGE, "text/html; charset=utf-8")
        elif self.path == "/about":
            self._send(200, ABOUT_PAGE, "text/html; charset=utf-8")
        elif self.path == "/api/time":
            payload = {"server": "tiny_server", "utc_time": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            self._send(200, json.dumps(payload, indent=2), "application/json")
        elif self.path == "/favicon.ico":
            self._send(204, "", "text/plain")
        else:
            self._send(404, "<h1>404 - Not Found</h1><p>Nothing lives at this address.</p>", "text/html; charset=utf-8")

    do_HEAD = do_GET

    def log_message(self, *args) -> None:  # silence the default log; we print our own
        pass


if __name__ == "__main__":
    print(f"Server listening on http://localhost:{PORT}  (Ctrl+C to stop)\n")
    try:
        ThreadingHTTPServer(("0.0.0.0", PORT), LoggingHandler).serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
