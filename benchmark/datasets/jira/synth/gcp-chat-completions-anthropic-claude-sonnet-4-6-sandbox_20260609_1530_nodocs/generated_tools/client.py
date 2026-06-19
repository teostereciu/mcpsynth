"""
Shared HTTP client for Jira Cloud REST API v3.
Not registered as an MCP tool — internal helper only.
"""

import os
import requests
from requests.auth import HTTPBasicAuth
from typing import Any, Dict, Optional

JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

BASE = f"{JIRA_BASE_URL}/rest/api/3"


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    h = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    if extra:
        h.update(extra)
    return h


def jira_get(path: str, params: Optional[Dict[str, Any]] = None) -> Any:
    """Perform a GET request against the Jira API."""
    try:
        resp = requests.get(
            f"{BASE}{path}",
            params=params,
            auth=_auth(),
            headers=_headers(),
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "success"}
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def jira_post(path: str, json: Optional[Any] = None, params: Optional[Dict[str, Any]] = None) -> Any:
    """Perform a POST request against the Jira API."""
    try:
        resp = requests.post(
            f"{BASE}{path}",
            json=json,
            params=params,
            auth=_auth(),
            headers=_headers(),
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "success"}
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        if resp.text:
            return resp.json()
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}


def jira_put(path: str, json: Optional[Any] = None, params: Optional[Dict[str, Any]] = None) -> Any:
    """Perform a PUT request against the Jira API."""
    try:
        resp = requests.put(
            f"{BASE}{path}",
            json=json,
            params=params,
            auth=_auth(),
            headers=_headers(),
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "success"}
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        if resp.text:
            return resp.json()
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}


def jira_delete(path: str, params: Optional[Dict[str, Any]] = None) -> Any:
    """Perform a DELETE request against the Jira API."""
    try:
        resp = requests.delete(
            f"{BASE}{path}",
            params=params,
            auth=_auth(),
            headers=_headers(),
            timeout=30,
        )
        if resp.status_code in (200, 204):
            return {"status": "success"}
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}


def jira_multipart_post(path: str, files: Any, data: Optional[Dict[str, Any]] = None) -> Any:
    """Perform a multipart POST (for attachments)."""
    try:
        resp = requests.post(
            f"{BASE}{path}",
            files=files,
            data=data,
            auth=_auth(),
            headers={"Accept": "application/json", "X-Atlassian-Token": "no-check"},
            timeout=60,
        )
        if resp.status_code == 204:
            return {"status": "success"}
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
