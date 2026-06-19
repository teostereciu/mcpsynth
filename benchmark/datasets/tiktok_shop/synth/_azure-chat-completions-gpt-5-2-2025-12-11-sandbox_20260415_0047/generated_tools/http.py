"""HTTP/auth utilities for TikTok Shop Partner Open API.

Implements signature-based authentication and a thin requests wrapper.
"""

from __future__ import annotations

import json
import os
import time
import hashlib
import hmac
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://open-api.tiktokglobalshop.com"


class TikTokAPIError(Exception):
    """Internal exception used to normalize error handling."""


def _compact_json(body: Any) -> str:
    if body is None:
        return ""
    return json.dumps(body, separators=(",", ":"), ensure_ascii=False)


def generate_sign(app_secret: str, path: str, params: Dict[str, Any], body_str: str = "") -> str:
    """Generate HMAC-SHA256 signature.

    String to sign:
      {app_secret}{path}{sorted_param_pairs}{body}{app_secret}

    sorted_param_pairs: all query params excluding sign and access_token, sorted by key,
    concatenated as key+value.
    """

    exclude = {"sign", "access_token"}
    sorted_pairs = "".join(f"{k}{params[k]}" for k in sorted(params.keys()) if k not in exclude)
    to_sign = f"{app_secret}{path}{sorted_pairs}{body_str}{app_secret}"
    return hmac.new(app_secret.encode("utf-8"), to_sign.encode("utf-8"), hashlib.sha256).hexdigest()


@dataclass
class TikTokClient:
    app_key: str
    app_secret: str
    access_token: str
    shop_cipher: str = ""

    @classmethod
    def from_env(cls) -> "TikTokClient":
        return cls(
            app_key=os.environ.get("TIKTOK_APP_KEY", ""),
            app_secret=os.environ.get("TIKTOK_APP_SECRET", ""),
            access_token=os.environ.get("TIKTOK_ACCESS_TOKEN", ""),
            shop_cipher=os.environ.get("TIKTOK_SHOP_CIPHER", ""),
        )


def tiktok_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
    use_shop_cipher: bool = True,
    timeout_s: int = 60,
) -> Dict[str, Any]:
    """Make an authenticated request.

    Returns the API envelope's `data` on success, or an error dict on failure.
    """

    client = TikTokClient.from_env()
    if not client.app_key or not client.app_secret:
        return {"error": "Missing TIKTOK_APP_KEY/TIKTOK_APP_SECRET in environment"}
    if not client.access_token:
        return {"error": "Missing TIKTOK_ACCESS_TOKEN in environment"}

    query: Dict[str, Any] = {
        "app_key": client.app_key,
        "timestamp": str(int(time.time())),
        **(params or {}),
    }
    if use_shop_cipher and client.shop_cipher:
        query.setdefault("shop_cipher", client.shop_cipher)

    body_str = _compact_json(body)
    query["sign"] = generate_sign(client.app_secret, path, query, body_str)

    headers = {
        "Content-Type": "application/json",
        "x-tts-access-token": client.access_token,
    }

    url = f"{BASE_URL}{path}"

    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=query,
            json=body if body is not None else None,
            timeout=timeout_s,
        )
        resp.raise_for_status()
        payload = resp.json()
    except requests.HTTPError as e:
        # Try to parse TikTok envelope even on non-2xx.
        try:
            payload = resp.json()  # type: ignore[name-defined]
        except Exception:
            return {"error": f"HTTP error: {str(e)}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

    if isinstance(payload, dict) and payload.get("code") == 0:
        return payload.get("data", payload)

    if isinstance(payload, dict):
        return {
            "error": payload.get("message", "Unknown error"),
            "code": payload.get("code"),
            "request_id": payload.get("request_id"),
            "raw": payload,
        }

    return {"error": "Unexpected response", "raw": payload}
