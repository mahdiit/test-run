#!/usr/bin/env python3
import base64
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


ADMIN_USER = os.getenv("MRH_ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("MRH_ADMIN_PASS", "Sample@Sample")
AUTH_VALUE = "Basic " + base64.b64encode(f"{ADMIN_USER}:{ADMIN_PASS}".encode()).decode()


class AdminAuthHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/opt/mrh-admin", **kwargs)

    def _authorized(self):
        return self.headers.get("Authorization", "") == AUTH_VALUE

    def _request_auth(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="MRH-G2Ray Admin"')
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Authentication required")

    def do_GET(self):
        if not self._authorized():
            self._request_auth()
            return
        super().do_GET()

    def do_HEAD(self):
        if not self._authorized():
            self._request_auth()
            return
        super().do_HEAD()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8080), AdminAuthHandler)
    server.serve_forever()
