"""TikTok Shop Partner Open API client utilities.

Implements signature-based authentication and a small wrapper around requests.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://open-api.tiktokglobalshop.com"


def _json_dumps_compact(obj: Any) -> str:
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False) if obj is not None else ""


def generate_sign(app_secret: str, path: str, params: Dict[str, Any], body_str: str = "") -> str:
    """Generate HMAC-SHA256 signature.

    String to sign:
      {app_secret}{path}{sorted_param_pairs}{body}{app_secret}

    sorted_param_pairs: all query params excluding sign and access_token, sorted by key,
    concatenated as key+value.
    """

    exclude = {"sign", "access_token"}
    sorted_pairs = "".join(f"{k}{v}" for k, v in sorted(params.items()) if k not in exclude)
    to_sign = f"{app_secret}{path}{sorted_pairs}{body_str}{app_secret}"
    return hmac.new(app_secret.encode("utf-8"), to_sign.encode("utf-8"), hashlib.sha256).hexdigest()


@dataclass
class TikTokShopClient:
    app_key: str
    app_secret: str
    access_token: str
    shop_cipher: Optional[str] = None
    base_url: str = BASE_URL
    timeout_s: int = 60

    @staticmethod
    def from_env() -> "TikTokShopClient":
        return TikTokShopClient(
            app_key=os.environ.get("TIKTOK_APP_KEY", ""),
            app_secret=os.environ.get("TIKTOK_APP_SECRET", ""),
            access_token=os.environ.get("TIKTOK_ACCESS_TOKEN", ""),
            shop_cipher=os.environ.get("TIKTOK_SHOP_CIPHER"),
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        use_shop_cipher: bool = True,
    ) -> Dict[str, Any]:
        """Make an authenticated request.

        Returns a JSON-serializable dict. Never raises for expected API errors.
        """

        if not self.app_key or not self.app_secret:
            return {"error": "Missing TIKTOK_APP_KEY/TIKTOK_APP_SECRET in environment", "code": "CONFIG"}
        if not self.access_token:
            return {"error": "Missing TIKTOK_ACCESS_TOKEN in environment", "code": "CONFIG"}

        query: Dict[str, Any] = {
            "app_key": self.app_key,
            "timestamp": str(int(time.time())),
        }
        if params:
            query.update({k: v for k, v in params.items() if v is not None})

        if use_shop_cipher:
            cipher = (params or {}).get("shop_cipher") if params else None
            cipher = cipher or self.shop_cipher
            if cipher:
                query.setdefault("shop_cipher", cipher)

        body_str = _json_dumps_compact(body) if body else ""
        query["sign"] = generate_sign(self.app_secret, path, query, body_str)

        headers = {
            "Content-Type": "application/json",
            "x-tts-access-token": self.access_token,
        }

        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=query,
                json=body if body else None,
                timeout=self.timeout_s,
            )
        except requests.RequestException as e:
            return {"error": f"Network error: {e}", "code": "NETWORK"}

        try:
            payload = resp.json()
        except ValueError:
            return {"error": f"Non-JSON response (status={resp.status_code})", "status_code": resp.status_code}

        # HTTP-level errors still often return JSON envelope.
        if resp.status_code >= 400 and payload.get("code") in (None, 0):
            return {"error": f"HTTP error {resp.status_code}", "status_code": resp.status_code, "response": payload}

        if payload.get("code") != 0:
            return {
                "error": payload.get("message", "TikTok API error"),
                "code": payload.get("code"),
                "request_id": payload.get("request_id"),
                "data": payload.get("data"),
            }

        return payload.get("data", payload)
