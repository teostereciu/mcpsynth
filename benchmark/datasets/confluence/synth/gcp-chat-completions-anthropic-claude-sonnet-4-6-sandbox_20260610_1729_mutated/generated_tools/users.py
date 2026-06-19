"""
Confluence Cloud Users tools.
v1: GET /wiki/rest/api/user, GET /wiki/rest/api/user/current
v2: POST /wiki/api/v2/users-bulk
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


def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"


def get_current_user() -> dict:
    """Return the currently authenticated Confluence user."""
    try:
        r = requests.get(_v1("/user/current"), auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_user_by_account_id(account_id: str) -> dict:
    """Return a Confluence user by their Atlassian account ID."""
    try:
        r = requests.get(_v1("/user"), params={"accountId": account_id}, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_users_bulk(account_ids: list[str]) -> dict:
    """Return user details for multiple account IDs (v2 API)."""
    payload = {"accountIds": account_ids}
    try:
        r = requests.post(_v2("/users-bulk"), json=payload, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
