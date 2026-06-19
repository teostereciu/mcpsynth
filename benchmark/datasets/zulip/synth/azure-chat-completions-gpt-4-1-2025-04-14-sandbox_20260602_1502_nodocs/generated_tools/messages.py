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
def send_message(type: str, to: str, content: str, topic: str = None):
    """Send a Zulip message. type: 'stream' or 'private'. to: stream name or user id/email. content: message text. topic: required for stream messages."""
    data = {
        "type": type,
        "to": to,
        "content": content,
    }
    if type == "stream":
        if not topic:
            return {"error": "topic is required for stream messages"}
        data["topic"] = topic
    return zulip_request("POST", "/messages", data=data)


@tool()
def get_messages(anchor: str = "newest", num_before: int = 0, num_after: int = 10, narrow: list = None):
    """Fetch message history. anchor: message id or 'newest'. num_before/after: number of messages before/after anchor. narrow: list of search filters."""
    params = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
    }
    if narrow:
        params["narrow"] = narrow
    return zulip_request("GET", "/messages", params=params)
