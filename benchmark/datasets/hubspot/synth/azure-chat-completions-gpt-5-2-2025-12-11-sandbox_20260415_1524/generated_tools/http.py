import os
import json
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.hubapi.com"


def _auth_headers() -> Dict[str, str]:
    token = os.getenv("HUBSPOT_ACCESS_TOKEN")
    if not token:
        return {}
    return {"Authorization": f"Bearer {token}"}


def hubspot_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: int = 30,
) -> Dict[str, Any]:
    """Make a HubSpot API request and return JSON-serializable dict.

    Returns either parsed JSON, or {"status_code": ..., "text": ...}.
    Errors are returned as {"error": ..., "status_code": ..., "details": ...}.
    """
    url = BASE_URL + path
    headers = {
        **_auth_headers(),
        "Accept": "application/json",
    }
    if json_body is not None:
        headers["Content-Type"] = "application/json"

    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=json_body,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": "request_failed", "details": str(e)}

    content_type = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        details: Any
        if "application/json" in content_type:
            try:
                details = resp.json()
            except Exception:
                details = resp.text
        else:
            details = resp.text
        return {
            "error": "hubspot_api_error",
            "status_code": resp.status_code,
            "details": details,
        }

    if resp.status_code == 204:
        return {"status_code": 204}

    if "application/json" in content_type:
        try:
            return resp.json()
        except Exception:
            return {"status_code": resp.status_code, "text": resp.text}

    return {"status_code": resp.status_code, "text": resp.text}


def parse_csv_param(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, str):
        v = value.strip()
        return v if v else None
    return str(value)


def ensure_dict(value: Any) -> Dict[str, Any]:
    if value is None:
        return {}
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, dict) else {}
        except Exception:
            return {}
    return {}
