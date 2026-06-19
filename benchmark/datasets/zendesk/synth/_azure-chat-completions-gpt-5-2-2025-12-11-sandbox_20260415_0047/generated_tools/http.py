"""Shared HTTP utilities for Zendesk APIs.

Implements:
- Basic auth using email/token
- Base URL construction
- JSON request helpers with consistent error handling

All helpers return JSON-serializable dicts and never raise for expected HTTP errors.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests
from requests.auth import HTTPBasicAuth


@dataclass(frozen=True)
class ZendeskConfig:
    subdomain: str
    email: str
    api_token: str


def _get_config() -> ZendeskConfig:
    subdomain = os.environ.get("ZENDESK_SUBDOMAIN")
    email = os.environ.get("ZENDESK_EMAIL")
    token = os.environ.get("ZENDESK_API_TOKEN")
    missing = [k for k, v in {"ZENDESK_SUBDOMAIN": subdomain, "ZENDESK_EMAIL": email, "ZENDESK_API_TOKEN": token}.items() if not v]
    if missing:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
    return ZendeskConfig(subdomain=subdomain, email=email, api_token=token)


def get_base_url() -> str:
    cfg = _get_config()
    return f"https://{cfg.subdomain}.zendesk.com/api/v2"


def get_auth() -> HTTPBasicAuth:
    cfg = _get_config()
    return HTTPBasicAuth(f"{cfg.email}/token", cfg.api_token)


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{get_base_url()}{path}"
    try:
        resp = requests.request(
            method,
            url,
            auth=get_auth(),
            headers={"Content-Type": "application/json"},
            params=params or {},
            json=json_body if json_body is not None else None,
            timeout=30,
        )
    except requests.RequestException as e:
        return {"error": "request_failed", "message": str(e), "url": url, "method": method}

    if 200 <= resp.status_code < 300:
        if not resp.content:
            return {"status": resp.status_code}
        try:
            return resp.json()
        except ValueError:
            return {"status": resp.status_code, "text": resp.text}

    # Error path: try to parse Zendesk error payload
    payload: Dict[str, Any]
    try:
        payload = resp.json()
    except ValueError:
        payload = {"message": resp.text}

    err: Dict[str, Any] = {
        "error": payload.get("error") or "http_error",
        "description": payload.get("description") or payload.get("message") or payload.get("details"),
        "status": resp.status_code,
        "url": url,
        "method": method,
    }
    # include details if present
    if "details" in payload:
        err["details"] = payload["details"]
    return err


def zendesk_get(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("GET", path, params=params)


def zendesk_post(path: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("POST", path, json_body=payload or {})


def zendesk_put(path: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("PUT", path, json_body=payload or {})


def zendesk_delete(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("DELETE", path, params=params)
