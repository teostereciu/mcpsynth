"""
Confluence Cloud REST API — Users (v1 + v2)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, API_TOKEN)


def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"


def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"


def _handle(resp: requests.Response) -> dict:
    try:
        data = resp.json()
    except Exception:
        data = {"raw": resp.text}
    if not resp.ok:
        return {"error": data, "status_code": resp.status_code}
    return data


def get_current_user(expand: str = "operations") -> dict:
    """Get the currently authenticated user (v1).

    Args:
        expand: Comma-separated list of properties to expand.
    """
    params = {"expand": expand}
    resp = requests.get(_v1("/user/current"), params=params, auth=_auth())
    return _handle(resp)


def get_user_by_account_id(account_id: str, expand: str = "") -> dict:
    """Get a user by their Atlassian account ID (v1).

    Args:
        account_id: The Atlassian account ID (e.g. '5b10a2844c20165700ede21g').
        expand: Comma-separated list of properties to expand.
    """
    params: dict = {"accountId": account_id}
    if expand:
        params["expand"] = expand
    resp = requests.get(_v1("/user"), params=params, auth=_auth())
    return _handle(resp)


def get_user_groups(account_id: str, limit: int = 25, start: int = 0) -> dict:
    """Get groups that a user belongs to (v1).

    Args:
        account_id: The Atlassian account ID.
        limit: Maximum number of results.
        start: Offset for pagination.
    """
    params = {"accountId": account_id, "limit": limit, "start": start}
    resp = requests.get(_v1("/user/memberof"), params=params, auth=_auth())
    return _handle(resp)


def get_user_by_username(username: str, expand: str = "") -> dict:
    """Get a user by username (v1). Note: username is the user's display name key.

    Args:
        username: The username (not email).
        expand: Comma-separated list of properties to expand.
    """
    params: dict = {"username": username}
    if expand:
        params["expand"] = expand
    resp = requests.get(_v1("/user"), params=params, auth=_auth())
    return _handle(resp)


def list_group_members(group_name: str, limit: int = 25, start: int = 0) -> dict:
    """List members of a Confluence group (v1).

    Args:
        group_name: The group name.
        limit: Maximum number of results.
        start: Offset for pagination.
    """
    params = {"limit": limit, "start": start}
    resp = requests.get(
        _v1(f"/group/{group_name}/member"),
        params=params,
        auth=_auth(),
    )
    return _handle(resp)


def get_anonymous_user() -> dict:
    """Get information about anonymous (unauthenticated) access (v1)."""
    resp = requests.get(_v1("/user/anonymous"), auth=_auth())
    return _handle(resp)
