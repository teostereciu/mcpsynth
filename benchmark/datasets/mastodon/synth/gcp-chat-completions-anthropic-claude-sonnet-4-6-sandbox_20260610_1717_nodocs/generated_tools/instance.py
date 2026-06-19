"""
Mastodon API — Instance domain tools.
Covers: get instance info, get instance peers, get instance activity.
"""

import os
import requests


def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update(
        {"Authorization": f"Bearer {os.environ.get('MASTODON_ACCESS_TOKEN', '')}"}
    )
    return s


def _base() -> str:
    return os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"


# ---------------------------------------------------------------------------
# Get instance information
# ---------------------------------------------------------------------------
def get_instance() -> dict:
    """
    Return general information about the Mastodon instance.

    Returns:
        An Instance object containing title, description, version, stats,
        languages, contact account, and rules, or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/instance")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get instance peers
# ---------------------------------------------------------------------------
def get_instance_peers() -> list:
    """
    Return a list of domains that the instance is aware of (federated peers).

    Returns:
        A list of domain strings or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/instance/peers")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get instance activity
# ---------------------------------------------------------------------------
def get_instance_activity() -> list:
    """
    Return weekly activity statistics for the instance (last 12 weeks).

    Returns:
        A list of activity objects (week, statuses, logins, registrations)
        or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/instance/activity")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get instance rules
# ---------------------------------------------------------------------------
def get_instance_rules() -> list:
    """
    Return the rules of the Mastodon instance.

    Returns:
        A list of Rule objects (id, text) or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/instance/rules")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}
