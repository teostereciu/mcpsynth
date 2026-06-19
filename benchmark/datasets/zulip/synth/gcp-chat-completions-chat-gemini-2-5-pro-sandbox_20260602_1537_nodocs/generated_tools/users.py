"""Tools for interacting with users in Zulip."""

import os
import requests
from typing import Optional

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

def get_users() -> dict:
    """Gets all users in the organization."""
    response = requests.get(f"{ZULIP_SITE}/api/v1/users", auth=(ZULIP_EMAIL, ZULIP_API_KEY))
    return response.json()

def get_user_presence(user_id: int) -> dict:
    """Gets a user's presence."""
    response = requests.get(f"{ZULIP_SITE}/api/v1/users/{user_id}/presence", auth=(ZULIP_EMAIL, ZULIP_API_KEY))
    return response.json()

def get_user_by_id(user_id: int) -> dict:
    """Gets a user by ID."""
    response = requests.get(f"{ZULIP_SITE}/api/v1/users/{user_id}", auth=(ZULIP_EMAIL, ZULIP_API_KEY))
    return response.json()
