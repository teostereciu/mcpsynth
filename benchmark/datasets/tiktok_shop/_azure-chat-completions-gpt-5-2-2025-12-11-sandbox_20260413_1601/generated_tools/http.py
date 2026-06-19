"""Shared HTTP/auth utilities for TikTok Shop Partner Open API.

Implements signature-based authentication and a small requests wrapper.

All API tools should call :func:`tiktok_request`.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional

import requests


BASE_URL = "https://open-api.tiktokglobalshop.com"


class TikTokAPIError(Exception):
    """Internal exception used for control flow; tools should return error dicts."""


def _json_dumps_compact(obj: Any) -> str:
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False)


def generate_sign(app_secret: str, path: str, params: Mapping[str, Any], body_str: str = "") -> str:
    """Generate HMAC-SHA256 signature for TikTok Shop API request."""

    exclude = {"sign", "access_token"}
    sorted_pairs = "".join(
        f"{k}{params[k]}" for k in sorted(params.keys()) if k not in exclude
    )
    to_sign = f"{app_secret}{path}{sorted_pairs}{body_str}{app_secret}"
    return hmac.new(app_secret.encode("utf-8"), to_sign.encode("utf-8"), hashlib.sha256).hexdigest()


@dataclass
class TikTokRequestOptions:
    use_shop_cipher: bool = True
    shop_cipher: Optional[str] = None
    timeout_s: int = 30
    extra_headers: Optional[Dict[str, str]] = None


def tiktok_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
    options: Optional[TikTokRequestOptions] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to TikTok Shop API.

    Returns the decoded JSON response envelope (or its `data` field when present).
    Never raises for expected API errors; instead returns {"error": ..., "code": ...}.
    """

    options = options or TikTokRequestOptions()

    try:
        app_key = os.environ["TIKTOK_APP_KEY"]
        app_secret = os.environ["TIKTOK_APP_SECRET"]
        access_token = os.environ["TIKTOK_ACCESS_TOKEN"]
    except KeyError as e:
        return {"error": f"Missing required environment variable: {e.args[0]}", "code": "ENV_MISSING"}

    query: Dict[str, Any] = {
        "app_key": app_key,
        "timestamp": str(int(time.time())),
        **(params or {}),
    }

    if options.use_shop_cipher:
        cipher = options.shop_cipher if options.shop_cipher is not None else os.environ.get("TIKTOK_SHOP_CIPHER")
        if cipher:
            query["shop_cipher"] = cipher

    body_str = _json_dumps_compact(body) if body is not None else ""
    query["sign"] = generate_sign(app_secret, path, query, body_str)

    headers = {
        "Content-Type": "application/json",
        "x-tts-access-token": access_token,
    }
    if options.extra_headers:
        headers.update(options.extra_headers)

    url = f"{BASE_URL}{path}"

    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            params=query,
            json=body,
            headers=headers,
            timeout=options.timeout_s,
        )
    except requests.RequestException as e:
        return {"error": f"Network error: {e}", "code": "NETWORK_ERROR"}

    try:
        resp_json = resp.json()
    except ValueError:
        return {"error": f"Non-JSON response (status={resp.status_code})", "code": "NON_JSON"}

    # TikTok uses HTTP 200 for many errors; still handle non-2xx.
    if resp.status_code >= 400:
        return {
            "error": resp_json.get("message") or f"HTTP error {resp.status_code}",
            "code": resp_json.get("code", resp.status_code),
            "response": resp_json,
        }

    if resp_json.get("code") != 0:
        return {
            "error": resp_json.get("message", "Unknown error"),
            "code": resp_json.get("code"),
            "request_id": resp_json.get("request_id"),
            "response": resp_json,
        }

    return resp_json.get("data", resp_json)
