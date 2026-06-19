import os
import requests
from fastmcp import tool

ZULIP_SITE = os.environ["ZULIP_SITE"]
ZULIP_EMAIL = os.environ["ZULIP_EMAIL"]
ZULIP_API_KEY = os.environ["ZULIP_API_KEY"]
BASE_URL = f"{ZULIP_SITE}/api/v1"

def zulip_request(method, endpoint, **kwargs):
    url = f"{BASE_URL}{endpoint}"
    auth = (ZULIP_EMAIL, ZULIP_API_KEY)
    try:
        resp = requests.request(method, url, auth=auth, **kwargs)
        if resp.status_code >= 400:
            return {"error": resp.text, "status_code": resp.status_code}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@tool()
def get_user_profile(user_id: int):
    """Get a user's profile."""
    return zulip_request("GET", f"/users/{user_id}")

@tool()
def get_presence(user_id: int):
    """Get a user's presence."""
    return zulip_request("GET", f"/users/{user_id}/presence")
