"""Internal HTTP client helper for GitHub API calls."""

import os
import requests
from typing import Any, Optional


BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def _headers() -> dict:
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


def github_get(path: str, params: Optional[dict] = None) -> Any:
    """Make a GET request to the GitHub API."""
    try:
        resp = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params or {})
        resp.raise_for_status()
        if resp.status_code == 204:
            return {"status": "success", "code": 204}
        return resp.json()
    except requests.exceptions.HTTPError as e:
        try:
            body = e.response.json()
        except Exception:
            body = e.response.text
        return {"error": str(e), "status_code": e.response.status_code, "detail": body}
    except Exception as e:
        return {"error": str(e)}


def github_post(path: str, json_data: Optional[dict] = None) -> Any:
    """Make a POST request to the GitHub API."""
    try:
        resp = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=json_data)
        resp.raise_for_status()
        if resp.status_code == 204:
            return {"status": "success", "code": 204}
        if resp.status_code == 202:
            try:
                return resp.json()
            except Exception:
                return {"status": "accepted", "code": 202}
        return resp.json()
    except requests.exceptions.HTTPError as e:
        try:
            body = e.response.json()
        except Exception:
            body = e.response.text
        return {"error": str(e), "status_code": e.response.status_code, "detail": body}
    except Exception as e:
        return {"error": str(e)}


def github_patch(path: str, json_data: Optional[dict] = None) -> Any:
    """Make a PATCH request to the GitHub API."""
    try:
        resp = requests.patch(f"{BASE_URL}{path}", headers=_headers(), json=json_data)
        resp.raise_for_status()
        if resp.status_code == 204:
            return {"status": "success", "code": 204}
        return resp.json()
    except requests.exceptions.HTTPError as e:
        try:
            body = e.response.json()
        except Exception:
            body = e.response.text
        return {"error": str(e), "status_code": e.response.status_code, "detail": body}
    except Exception as e:
        return {"error": str(e)}


def github_put(path: str, json_data: Optional[dict] = None) -> Any:
    """Make a PUT request to the GitHub API."""
    try:
        resp = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=json_data or {})
        resp.raise_for_status()
        if resp.status_code == 204:
            return {"status": "success", "code": 204}
        try:
            return resp.json()
        except Exception:
            return {"status": "success", "code": resp.status_code}
    except requests.exceptions.HTTPError as e:
        try:
            body = e.response.json()
        except Exception:
            body = e.response.text
        return {"error": str(e), "status_code": e.response.status_code, "detail": body}
    except Exception as e:
        return {"error": str(e)}


def github_delete(path: str, json_data: Optional[dict] = None) -> Any:
    """Make a DELETE request to the GitHub API."""
    try:
        kwargs = {"headers": _headers()}
        if json_data:
            kwargs["json"] = json_data
        resp = requests.delete(f"{BASE_URL}{path}", **kwargs)
        resp.raise_for_status()
        if resp.status_code == 204:
            return {"status": "success", "code": 204}
        try:
            return resp.json()
        except Exception:
            return {"status": "success", "code": resp.status_code}
    except requests.exceptions.HTTPError as e:
        try:
            body = e.response.json()
        except Exception:
            body = e.response.text
        return {"error": str(e), "status_code": e.response.status_code, "detail": body}
    except Exception as e:
        return {"error": str(e)}
