import base64
import os
from typing import Any, Dict, Optional

import requests


def _auth_header() -> Dict[str, str]:
    email = os.environ.get("JIRA_EMAIL", "")
    token = os.environ.get("JIRA_API_TOKEN", "")
    raw = f"{email}:{token}".encode("utf-8")
    b64 = base64.b64encode(raw).decode("utf-8")
    return {"Authorization": f"Basic {b64}"}


def confluence_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    data: Any = None,
    files: Any = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    base = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
    if not base:
        return {"error": "CONFLUENCE_BASE_URL is not set"}

    url = f"{base}{path}"
    h = {"Accept": "application/json", **_auth_header()}
    if headers:
        h.update(headers)

    try:
        resp = requests.request(
            method=method,
            url=url,
            params=params,
            json=json,
            headers=h,
            data=data,
            files=files,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e)}

    content_type = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        # Try to parse JSON error body
        try:
            body = resp.json() if "json" in content_type else resp.text
        except Exception:
            body = resp.text
        return {
            "error": "Confluence API error",
            "status": resp.status_code,
            "body": body,
            "url": url,
        }

    if resp.status_code == 204:
        return {"ok": True}

    if "json" in content_type:
        try:
            return resp.json()
        except Exception:
            return {"error": "Failed to decode JSON response", "text": resp.text}

    # For downloads etc.
    return {"content_type": content_type, "text": resp.text}
