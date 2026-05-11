#!/usr/bin/env python3
import base64
import os
import secrets
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def _auth_value():
    admin_user = os.getenv("MRH_ADMIN_USER", "admin")
    admin_pass = os.getenv("MRH_ADMIN_PASS", "Sample@Sample")
    encoded = base64.b64encode(f"{admin_user}:{admin_pass}".encode()).decode()
    return f"Basic {encoded}"


EXPECTED_AUTH = _auth_value()


class AdminAuthHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/opt/mrh-admin", **kwargs)

    def _authorized(self):
        provided = self.headers.get("Authorization", "")
        return secrets.compare_digest(provided, EXPECTED_AUTH)

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
