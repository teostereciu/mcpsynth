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
def list_topics(stream_id: int):
    """List topics in a stream."""
    return zulip_request("GET", f"/users/me/{stream_id}/topics")

@tool()
def rename_topic(stream_id: int, old_topic_name: str, new_topic_name: str):
    """Rename a topic in a stream."""
    data = {
        "stream_id": stream_id,
        "topic_name": old_topic_name,
        "new_topic_name": new_topic_name,
    }
    return zulip_request("PATCH", "/rename_topic", data=data)
