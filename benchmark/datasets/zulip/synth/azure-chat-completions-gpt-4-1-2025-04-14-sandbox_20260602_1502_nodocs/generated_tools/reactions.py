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
def add_reaction(message_id: int, emoji_name: str):
    """Add a reaction to a message."""
    data = {"emoji_name": emoji_name}
    return zulip_request("POST", f"/messages/{message_id}/reactions", data=data)

@tool()
def remove_reaction(message_id: int, emoji_name: str):
    """Remove a reaction from a message."""
    params = {"emoji_name": emoji_name}
    return zulip_request("DELETE", f"/messages/{message_id}/reactions", params=params)
