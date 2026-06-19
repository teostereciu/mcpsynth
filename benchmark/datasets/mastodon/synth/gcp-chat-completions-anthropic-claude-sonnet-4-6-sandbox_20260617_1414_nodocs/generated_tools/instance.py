"""
Mastodon API — Instance domain tools.
Covers: get instance info, get instance peers, get instance activity,
        get instance rules, get instance trends.
"""

import requests
from config import BASE_URL, HEADERS


def get_instance() -> dict:
    """
    Retrieve general information and statistics about the Mastodon instance.

    Returns:
        An Instance object containing description, stats, languages, contact
        account, and configuration, or an error dict.
    """
    url = f"{BASE_URL}/instance"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_instance_peers() -> list:
    """
    Retrieve a list of domains that the instance is aware of (federated peers).

    Returns:
        A list of domain strings, or an error dict.
    """
    url = f"{BASE_URL}/instance/peers"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_instance_activity() -> list:
    """
    Retrieve weekly activity statistics for the instance (last 12 weeks).

    Returns:
        A list of activity objects (week, statuses, logins, registrations),
        or an error dict.
    """
    url = f"{BASE_URL}/instance/activity"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_instance_rules() -> list:
    """
    Retrieve the rules of the Mastodon instance.

    Returns:
        A list of Rule objects (id, text), or an error dict.
    """
    url = f"{BASE_URL}/instance/rules"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_trending_tags(limit: int = 10) -> list:
    """
    Retrieve hashtags that are trending on the instance.

    Args:
        limit: Maximum number of trending tags to return (default 10, max 20).

    Returns:
        A list of Tag objects with usage history, or an error dict.
    """
    url = f"{BASE_URL}/trends/tags"
    try:
        resp = requests.get(url, headers=HEADERS, params={"limit": limit})
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_trending_statuses(limit: int = 20, offset: int = 0) -> list:
    """
    Retrieve statuses that are trending on the instance.

    Args:
        limit: Maximum number of results (default 20, max 40).
        offset: Offset for pagination.

    Returns:
        A list of Status objects, or an error dict.
    """
    url = f"{BASE_URL}/trends/statuses"
    try:
        resp = requests.get(url, headers=HEADERS, params={"limit": limit, "offset": offset})
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_trending_links(limit: int = 10, offset: int = 0) -> list:
    """
    Retrieve links (articles) that are trending on the instance.

    Args:
        limit: Maximum number of results (default 10, max 20).
        offset: Offset for pagination.

    Returns:
        A list of PreviewCard objects, or an error dict.
    """
    url = f"{BASE_URL}/trends/links"
    try:
        resp = requests.get(url, headers=HEADERS, params={"limit": limit, "offset": offset})
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}
