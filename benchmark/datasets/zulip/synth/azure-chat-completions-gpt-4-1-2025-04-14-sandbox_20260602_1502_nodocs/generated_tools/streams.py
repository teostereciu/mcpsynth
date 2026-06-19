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
def create_stream(name: str, description: str = "", invite_only: bool = False):
    """Create a new stream."""
    data = {
        "streams": [{"name": name, "description": description}],
        "invite_only": invite_only,
    }
    return zulip_request("POST", "/streams", data=data)


@tool()
def subscribe_streams(stream_names: list, user_ids: list = None):
    """Subscribe users to streams. stream_names: list of stream names. user_ids: optional list of user ids."""
    data = {
        "subscriptions": [{"name": name} for name in stream_names],
    }
    if user_ids:
        data["principals"] = user_ids
    return zulip_request("POST", "/users/me/subscriptions", data=data)
