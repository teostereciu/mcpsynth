import os
import requests
from mcp.server.fastmcp import FastMCP
import json

# Environment variables for authentication
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

if not all([ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE]):
    raise ValueError("ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set.")

BASE_URL = f"{ZULIP_SITE}/api/v1"

session = requests.Session()
session.auth = (ZULIP_EMAIL, ZULIP_API_KEY)

mcp = FastMCP()

# Placeholder for grounding.json
grounding_data = {}

# Helper function to make API requests
def make_api_request(method, endpoint, params=None, json_data=None, files=None):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = session.request(method, url, params=params, json=json_data, files=files)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": e.response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Tools will be registered here

# Write grounding.json
with open("grounding.json", "w") as f:
    json.dump(grounding_data, f, indent=2)

if __name__ == "__main__":
    mcp.run()
