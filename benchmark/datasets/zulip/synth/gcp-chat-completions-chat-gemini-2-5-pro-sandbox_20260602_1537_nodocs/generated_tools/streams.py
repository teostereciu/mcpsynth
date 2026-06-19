"""Tools for interacting with streams in Zulip."""

import os
import requests
from typing import List, Optional

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

def get_streams(include_public: bool = True, include_web_public: bool = True, include_subscribed: bool = True, include_all_active: bool = True, include_default: bool = True, include_owner: bool = True) -> dict:
    """Gets all streams in the organization."""
    params = {
        "include_public": include_public,
        "include_web_public": include_web_public,
        "include_subscribed": include_subscribed,
        "include_all_active": include_all_active,
        "include_default": include_default,
        "include_owner": include_owner,
    }
    response = requests.get(f"{ZULIP_SITE}/api/v1/streams", auth=(ZULIP_EMAIL, ZULIP_API_KEY), params=params)
    return response.json()

def subscribe_to_stream(stream: str, description: str) -> dict:
    """Subscribes to a stream."""
    response = requests.post(
        f"{ZULIP_SITE}/api/v1/users/me/subscriptions",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data={"subscriptions": f'[{{"name":"{stream}", "description":"{description}"}}]'},
    )
    return response.json()
