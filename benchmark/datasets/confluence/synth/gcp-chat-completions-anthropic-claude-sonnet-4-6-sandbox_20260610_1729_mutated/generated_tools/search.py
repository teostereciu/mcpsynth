"""
Confluence Cloud v1 Search tools.
Endpoints: GET /wiki/rest/api/search, GET /wiki/rest/api/search/user
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, TOKEN)


def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"


def search_content(
    query: str,
    max_results: int = 25,
    cursor: str | None = None,
    include_archived_spaces: bool = False,
    excerpt: str | None = None,
) -> dict:
    """
    Search Confluence content using CQL (Confluence Query Language).
    Example query: 'type=page AND space.key=MYSPACE AND title~"Meeting Notes"'
    """
    params: dict = {
        "query": query,
        "max_results": max_results,
    }
    if cursor:
        params["cursor"] = cursor
    if include_archived_spaces:
        params["includeArchivedSpaces"] = "true"
    if excerpt:
        params["excerpt"] = excerpt
    try:
        r = requests.get(_v1("/search"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def search_users(
    query: str,
    max_results: int = 25,
    offset: int = 0,
) -> dict:
    """
    Search Confluence users using CQL user-specific fields.
    Example query: 'user.fullname="John Doe"'
    """
    params: dict = {
        "query": query,
        "max_results": max_results,
        "offset": offset,
    }
    try:
        r = requests.get(_v1("/search/user"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
