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


class TikTokAPIError(Exception):
    """Internal exception used for control flow; tools should catch and return dict errors."""


def _json_dumps_compact(obj: Any) -> str:
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False) if obj is not None else ""


def generate_sign(app_secret: str, path: str, params: Dict[str, Any], body_str: str = "") -> str:
    """Generate HMAC-SHA256 signature for TikTok Shop API request."""
    exclude = {"sign", "access_token"}
    sorted_pairs = "".join(f"{k}{params[k]}" for k in sorted(params.keys()) if k not in exclude)
    to_sign = f"{app_secret}{path}{sorted_pairs}{body_str}{app_secret}"
    return hmac.new(app_secret.encode("utf-8"), to_sign.encode("utf-8"), hashlib.sha256).hexdigest()


@dataclass
class TikTokClient:
    app_key: str
    app_secret: str
    access_token: str
    shop_cipher: str | None = None

    @classmethod
    def from_env(cls) -> "TikTokClient":
        return cls(
            app_key=os.environ["TIKTOK_APP_KEY"],
            app_secret=os.environ["TIKTOK_APP_SECRET"],
            access_token=os.environ["TIKTOK_ACCESS_TOKEN"],
            shop_cipher=os.environ.get("TIKTOK_SHOP_CIPHER") or None,
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        body: Any = None,
        use_shop_cipher: bool = True,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        query: Dict[str, Any] = {
            "app_key": self.app_key,
            "timestamp": str(int(time.time())),
        }
        if params:
            query.update({k: v for k, v in params.items() if v is not None})
        if use_shop_cipher and self.shop_cipher:
            query.setdefault("shop_cipher", self.shop_cipher)

        body_str = _json_dumps_compact(body) if body is not None else ""
        query["sign"] = generate_sign(self.app_secret, path, query, body_str)

        headers = {
            "Content-Type": "application/json",
            "x-tts-access-token": self.access_token,
        }

        url = f"{BASE_URL}{path}"
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=query,
                json=body if body is not None else None,
                timeout=timeout,
            )
        except requests.RequestException as e:
            raise TikTokAPIError(f"Network error: {e}") from e

        try:
            payload = resp.json()
        except ValueError:
            raise TikTokAPIError(f"Non-JSON response (status={resp.status_code}): {resp.text[:500]}")

        # HTTP errors still often return JSON envelope; prefer envelope code.
        if resp.status_code >= 400 and payload.get("code") is None:
            raise TikTokAPIError(f"HTTP {resp.status_code}: {resp.text[:500]}")

        code = payload.get("code")
        if code != 0:
            return {
                "error": payload.get("message") or "TikTok API error",
                "code": code,
                "request_id": payload.get("request_id"),
                "raw": payload,
            }

        return payload.get("data", payload)


def safe_call(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    body: Any = None,
    use_shop_cipher: bool = True,
) -> Dict[str, Any]:
    """Convenience wrapper used by tools."""
    try:
        client = TikTokClient.from_env()
        return client.request(method, path, params=params, body=body, use_shop_cipher=use_shop_cipher)
    except KeyError as e:
        return {"error": f"Missing environment variable: {e.args[0]}", "code": -1}
    except TikTokAPIError as e:
        return {"error": str(e), "code": -1}
