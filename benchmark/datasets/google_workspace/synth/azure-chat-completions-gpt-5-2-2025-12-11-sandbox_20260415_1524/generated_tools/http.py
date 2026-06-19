import json
import os
from typing import Any, Dict, Optional

import requests


def _load_access_token() -> Optional[str]:
    token = os.getenv("GOOGLE_ACCESS_TOKEN")
    if token:
        return token.strip()
    return None


def _auth_headers() -> Dict[str, str]:
    token = _load_access_token()
    if not token:
        return {}
    return {"Authorization": f"Bearer {token}"}


def request_json(method: str, url: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None, headers: Optional[Dict[str, str]] = None, timeout: int = 60) -> Any:
    h = {"Accept": "application/json"}
    h.update(_auth_headers())
    if headers:
        h.update(headers)

    try:
        resp = requests.request(method.upper(), url, params=params, json=json_body, headers=h, timeout=timeout)
    except Exception as e:
        return {"error": str(e), "url": url}

    content_type = resp.headers.get("content-type", "")
    if resp.status_code >= 400:
        # Try to parse Google-style error JSON
        try:
            err = resp.json()
        except Exception:
            err = {"error": resp.text}
        return {"error": err, "status_code": resp.status_code, "url": url}

    if "application/json" in content_type:
        try:
            return resp.json()
        except Exception:
            return {"error": "Failed to parse JSON", "status_code": resp.status_code, "text": resp.text, "url": url}

    # Non-JSON response
    return {"status_code": resp.status_code, "content_type": content_type, "text": resp.text}


def request_bytes(method: str, url: str, *, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, timeout: int = 60) -> Any:
    h = {}
    h.update(_auth_headers())
    if headers:
        h.update(headers)

    try:
        resp = requests.request(method.upper(), url, params=params, headers=h, timeout=timeout)
    except Exception as e:
        return {"error": str(e), "url": url}

    if resp.status_code >= 400:
        try:
            err = resp.json()
        except Exception:
            err = {"error": resp.text}
        return {"error": err, "status_code": resp.status_code, "url": url}

    return {
        "status_code": resp.status_code,
        "content_type": resp.headers.get("content-type"),
        "bytes_base64": __import__("base64").b64encode(resp.content).decode("ascii"),
    }
