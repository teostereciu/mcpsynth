"""
Confluence Cloud REST API — Search (v1 CQL)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, API_TOKEN)


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


def search_content(
    cql: str,
    limit: int = 25,
    start: int = 0,
    expand: str = "body.storage,version,space",
) -> dict:
    """Search Confluence content using CQL (Confluence Query Language) (v1).

    Args:
        cql: CQL query string, e.g. 'type=page AND space=SYNTH AND title~"Meeting"'.
        limit: Maximum number of results (1-200).
        start: Offset for pagination.
        expand: Comma-separated list of properties to expand in results.

    Examples of CQL:
        - 'type=page AND space="SYNTH"'
        - 'title="My Page" AND space.key="SYNTH"'
        - 'text~"keyword" AND type=page'
        - 'label="important" AND type=blogpost'
        - 'ancestor=12345'
        - 'creator=currentUser() AND type=page'
    """
    params = {
        "cql": cql,
        "limit": limit,
        "start": start,
        "expand": expand,
    }
    resp = requests.get(_v1("/content/search"), params=params, auth=_auth())
    return _handle(resp)


def search_users(
    query: str,
    limit: int = 25,
    start: int = 0,
) -> dict:
    """Search for Confluence users by name or email (v1).

    Args:
        query: Search query string (name or email fragment).
        limit: Maximum number of results.
        start: Offset for pagination.
    """
    params = {
        "cql": f'type=user AND (fullname~"{query}" OR email~"{query}")',
        "limit": limit,
        "start": start,
    }
    resp = requests.get(_v1("/search/user"), params=params, auth=_auth())
    return _handle(resp)
