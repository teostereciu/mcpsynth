"""Shared HTTP utilities for HubSpot API calls."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests

HUBSPOT_BASE_URL = "https://api.hubapi.com"


def _headers() -> Dict[str, str]:
    token = os.environ.get("HUBSPOT_ACCESS_TOKEN")
    if not token:
        # Return empty; caller will get 401 from API if they proceed.
        return {"Content-Type": "application/json"}
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def _handle_response(resp: requests.Response) -> Dict[str, Any] | list | str:
    content_type = resp.headers.get("Content-Type", "")
    if resp.ok:
        if resp.status_code == 204:
            return {"ok": True}
        if "application/json" in content_type:
            return resp.json()
        return resp.text

    # Error
    try:
        if "application/json" in content_type:
            body: Any = resp.json()
        else:
            body = resp.text
    except Exception:
        body = resp.text

    return {
        "error": body,
        "status": resp.status_code,
    }


def hubspot_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    timeout: float = 30.0,
) -> Dict[str, Any] | list | str:
    url = f"{HUBSPOT_BASE_URL}{path}"
    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=_headers(),
            params=params or {},
            json=json,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e)}

    return _handle_response(resp)


def hubspot_get(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any] | list | str:
    return hubspot_request("GET", path, params=params)


def hubspot_post(path: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any] | list | str:
    return hubspot_request("POST", path, json=payload or {})


def hubspot_patch(path: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any] | list | str:
    return hubspot_request("PATCH", path, json=payload or {})


def hubspot_put(path: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any] | list | str:
    return hubspot_request("PUT", path, json=payload)


def hubspot_delete(path: str) -> Dict[str, Any] | list | str:
    return hubspot_request("DELETE", path)
