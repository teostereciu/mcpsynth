"""Mastodon API — Instance domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def get_instance() -> dict:
    """Fetch general information and statistics about the Mastodon instance."""
    try:
        r = requests.get(f"{BASE_URL}/instance", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_instance_peers() -> list:
    """Fetch the list of domains that this instance is aware of (peers)."""
    try:
        r = requests.get(f"{BASE_URL}/instance/peers", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_instance_activity() -> list:
    """Fetch weekly activity statistics for the instance (logins, registrations, statuses)."""
    try:
        r = requests.get(f"{BASE_URL}/instance/activity", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_instance_rules() -> list:
    """Fetch the rules of the Mastodon instance."""
    try:
        r = requests.get(f"{BASE_URL}/instance/rules", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_trending_tags(limit: int = 10) -> list:
    """Fetch hashtags that are trending on the instance.

    Args:
        limit: Maximum number of trending tags to return (default 10, max 20).
    """
    try:
        r = requests.get(
            f"{BASE_URL}/trends/tags", headers=_headers(), params={"limit": limit}
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_trending_statuses(limit: int = 20, offset: int = 0) -> list:
    """Fetch statuses that are trending on the instance.

    Args:
        limit: Maximum number of trending statuses to return (default 20).
        offset: Offset for pagination.
    """
    try:
        r = requests.get(
            f"{BASE_URL}/trends/statuses",
            headers=_headers(),
            params={"limit": limit, "offset": offset},
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_trending_links(limit: int = 10, offset: int = 0) -> list:
    """Fetch links that are trending on the instance.

    Args:
        limit: Maximum number of trending links to return (default 10).
        offset: Offset for pagination.
    """
    try:
        r = requests.get(
            f"{BASE_URL}/trends/links",
            headers=_headers(),
            params={"limit": limit, "offset": offset},
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_directory(
    order: str = "active",
    local: bool = True,
    limit: int = 40,
    offset: int = 0,
) -> list:
    """Browse the profile directory of the instance.

    Args:
        order: Sort order — 'active' (recently active) or 'new' (recently created).
        local: Show only local accounts.
        limit: Maximum number of accounts to return (default 40, max 80).
        offset: Offset for pagination.
    """
    params = {"order": order, "local": local, "limit": limit, "offset": offset}
    try:
        r = requests.get(f"{BASE_URL}/directory", headers=_headers(), params=params)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}
