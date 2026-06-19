"""
Confluence Cloud v1 API — Users tools.
"""
import os
import requests
from typing import Optional, List

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

def _auth():
    return (EMAIL, API_TOKEN)

def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"

def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"

def _handle(resp: requests.Response):
    if resp.status_code in (200, 201):
        try:
            return resp.json()
        except Exception:
            return {"status": resp.status_code}
    try:
        return {"error": resp.json()}
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}


def get_current_user() -> dict:
    """
    Get the currently authenticated user (v1).
    Returns user profile including accountId, displayName, email, etc.
    """
    resp = requests.get(_v1("/user/current"), auth=_auth())
    return _handle(resp)


def get_user_by_account_id(account_id: str) -> dict:
    """
    Get a user by their Atlassian account ID (v1).
    """
    params = {"accountId": account_id}
    resp = requests.get(_v1("/user"), params=params, auth=_auth())
    return _handle(resp)


def get_users_bulk(account_ids: List[str]) -> dict:
    """
    Get multiple users by their account IDs in bulk (v2).
    account_ids: list of Atlassian account ID strings.
    """
    payload = {"accountIds": account_ids}
    resp = requests.post(_v2("/users-bulk"), json=payload, auth=_auth())
    return _handle(resp)


def get_user_group_memberships(account_id: str, limit: int = 25, start: int = 0) -> dict:
    """
    Get the groups that a user is a member of (v1).
    """
    params = {"accountId": account_id, "limit": limit, "start": start}
    resp = requests.get(_v1("/user/memberof"), params=params, auth=_auth())
    return _handle(resp)
