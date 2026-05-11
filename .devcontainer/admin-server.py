#!/usr/bin/env python3
import base64
import os
import secrets
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def _current_credentials():
    admin_user = os.getenv("MRH_ADMIN_USER", "admin")
    admin_pass = os.getenv("MRH_ADMIN_PASS", "Sample@Sample")
    return admin_user, admin_pass


class AdminAuthHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/opt/mrh-admin", **kwargs)

    def _authorized(self):
        auth_header = self.headers.get("Authorization", "")
        if not auth_header.startswith("Basic "):
            return False

        encoded = auth_header[6:].strip()
        try:
            decoded = base64.b64decode(encoded, validate=True).decode("utf-8")
        except Exception:
            return False

        if ":" not in decoded:
            return False

        provided_user, provided_pass = decoded.split(":", 1)
        expected_user, expected_pass = _current_credentials()
        return secrets.compare_digest(provided_user, expected_user) and secrets.compare_digest(
            provided_pass, expected_pass
        )

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
