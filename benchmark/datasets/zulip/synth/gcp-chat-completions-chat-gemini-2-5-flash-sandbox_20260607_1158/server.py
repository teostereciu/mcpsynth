import os
import requests
import json
from mcp.server.fastmcp import FastMCP

# Load environment variables
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

if not all([ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE]):
    raise ValueError("ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set.")

BASE_URL = f"{ZULIP_SITE}/api/v1"

class ZulipClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.auth = (ZULIP_EMAIL, ZULIP_API_KEY)

    def _request(self, method, path, **kwargs):
        url = f"{BASE_URL}{path}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code, "response": e.response.json()}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

zulip_client = ZulipClient()
server = FastMCP(zulip_client)

if __name__ == "__main__":
    server.run()
