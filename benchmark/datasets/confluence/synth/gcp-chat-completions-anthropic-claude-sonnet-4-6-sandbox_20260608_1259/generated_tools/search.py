"""
Confluence Cloud v1 API — Search tools.
"""
import os
import requests
from typing import Optional

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

def _auth():
    return (EMAIL, API_TOKEN)

def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"

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


def search_content(
    cql: str,
    limit: int = 25,
    start: int = 0,
    cursor: Optional[str] = None,
    include_archived_spaces: bool = False,
    excerpt: Optional[str] = None,
) -> dict:
    """
    Search Confluence content using CQL (Confluence Query Language).
    Example CQL: 'type=page AND space.key=MYSPACE AND title~"Meeting"'
    Note: user-specific fields (user, user.fullname, etc.) are not supported here.
    Use search_users for user-specific queries.
    """
    params: dict = {"cql": cql, "limit": limit, "start": start}
    if cursor:
        params["cursor"] = cursor
    if include_archived_spaces:
        params["includeArchivedSpaces"] = "true"
    if excerpt:
        params["excerpt"] = excerpt
    resp = requests.get(_v1("/search"), params=params, auth=_auth())
    return _handle(resp)


def search_users(
    cql: str,
    limit: int = 25,
    start: int = 0,
) -> dict:
    """
    Search Confluence users using user-specific CQL fields.
    Supports: user, user.fullname, user.accountid, user.userkey.
    Example CQL: 'user.fullname="John Doe"'
    """
    params: dict = {"cql": cql, "limit": limit, "start": start}
    resp = requests.get(_v1("/search/user"), params=params, auth=_auth())
    return _handle(resp)
