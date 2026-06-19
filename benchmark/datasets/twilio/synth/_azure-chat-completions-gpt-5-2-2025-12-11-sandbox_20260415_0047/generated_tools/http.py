"""Shared HTTP helpers for Twilio APIs.

Twilio core API uses application/x-www-form-urlencoded bodies.
Verify + Conversations also accept form encoding.

All functions return JSON-serializable dicts/lists and never raise for expected HTTP errors.
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests
from requests.auth import HTTPBasicAuth


def _get_env(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return val


def get_auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(_get_env("TWILIO_ACCOUNT_SID"), _get_env("TWILIO_AUTH_TOKEN"))


def get_account_sid() -> str:
    return _get_env("TWILIO_ACCOUNT_SID")


def core_base_url() -> str:
    return f"https://api.twilio.com/2010-04-01/Accounts/{get_account_sid()}"


VERIFY_BASE_URL = "https://verify.twilio.com/v2"
CONVERSATIONS_BASE_URL = "https://conversations.twilio.com/v1"


def _request(
    method: str,
    url: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    timeout: float = 30.0,
) -> Dict[str, Any]:
    try:
        resp = requests.request(
            method,
            url,
            auth=get_auth(),
            params=params or {},
            data=data or {},
            timeout=timeout,
        )
        if resp.status_code >= 400:
            # Twilio returns JSON error bodies; fall back to text.
            try:
                err = resp.json()
            except Exception:
                err = {"message": resp.text}
            return {
                "error": True,
                "status_code": resp.status_code,
                "details": err,
                "url": url,
                "method": method,
            }
        if resp.status_code == 204:
            return {"status_code": 204, "deleted": True}
        return resp.json()
    except requests.RequestException as e:
        return {"error": True, "message": str(e), "url": url, "method": method}


def core_get(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("GET", f"{core_base_url()}{path}", params=params)


def core_post(path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("POST", f"{core_base_url()}{path}", data=data)


def core_delete(path: str) -> Dict[str, Any]:
    return _request("DELETE", f"{core_base_url()}{path}")


def verify_get(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("GET", f"{VERIFY_BASE_URL}{path}", params=params)


def verify_post(path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("POST", f"{VERIFY_BASE_URL}{path}", data=data)


def verify_delete(path: str) -> Dict[str, Any]:
    return _request("DELETE", f"{VERIFY_BASE_URL}{path}")


def conversations_get(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("GET", f"{CONVERSATIONS_BASE_URL}{path}", params=params)


def conversations_post(path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _request("POST", f"{CONVERSATIONS_BASE_URL}{path}", data=data)


def conversations_delete(path: str) -> Dict[str, Any]:
    return _request("DELETE", f"{CONVERSATIONS_BASE_URL}{path}")
