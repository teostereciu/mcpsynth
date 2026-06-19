#!/usr/bin/env python3
"""
One-shot Shopify OAuth access token fetcher for the benchmark dev store.

Prerequisites:
  - In Shopify Partners dashboard, the app must have:
      App URL:               http://localhost:8080
      Allowed redirect URLs: http://localhost:8080

Usage:
  python3 get_token.py

Opens a browser tab for store-owner approval, captures the OAuth callback
on localhost:8080, exchanges the code for an access token, and prints the
credentials to add to .env.
"""

import http.server
import threading
import urllib.parse
import webbrowser
import sys

import requests

CLIENT_ID     = "3c59b3301be1d52b074d051dcc18ec7a"
CLIENT_SECRET = "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"
STORE         = "test-synthesis-6ufalcrz.myshopify.com"
REDIRECT_URI  = "http://localhost:8080"
SCOPES        = (
    "read_products,write_products,"
    "read_orders,"
    "read_customers,write_customers,"
    "read_inventory,"
    "read_locations,"
    "write_price_rules"
)

code_holder: dict = {}


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        params = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(self.path).query))
        code_holder["code"] = params.get("code")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"<h2>Got it! You can close this tab.</h2>")
        threading.Thread(target=self.server.shutdown).start()

    def log_message(self, *_):
        pass


def main():
    server = http.server.HTTPServer(("localhost", 8080), _Handler)

    auth_url = (
        f"https://{STORE}/admin/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&scope={SCOPES}"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
        f"&state=xyz"
    )
    print(f"\nOpening browser for OAuth approval...\n\n  {auth_url}\n")
    webbrowser.open(auth_url)
    print("Waiting for callback on http://localhost:8080 ...")
    server.serve_forever()

    code = code_holder.get("code")
    if not code:
        print("No code received — did you approve the app?")
        sys.exit(1)

    print(f"Code received: {code[:12]}...")

    # Netskope does TLS inspection on this machine; verify=False is intentional here.
    r = requests.post(
        f"https://{STORE}/admin/oauth/access_token",
        json={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "code": code},
        verify=False,
    )

    if r.ok:
        token = r.json().get("access_token")
        print(f"\nSuccess! Add these to your .env:\n")
        print(f"  SHOPIFY_ACCESS_TOKEN={token}")
        print(f"  SHOPIFY_STORE_URL={STORE}\n")
    else:
        print("Token exchange failed:", r.text)
        sys.exit(1)


if __name__ == "__main__":
    main()
