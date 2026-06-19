import hashlib
import hmac
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


BASE_URL = "https://open-api.tiktokglobalshop.com"


def _now_ts() -> int:
    return int(time.time())


def _compact_json(data: Any) -> str:
    return json.dumps(data, separators=(",", ":"), ensure_ascii=False)


def _sign(app_secret: str, path: str, query: Dict[str, Any], body: Optional[Any]) -> str:
    """TikTok Shop Partner Open API signing.

    Canonical string format (per TikTok docs):
      app_secret + path + concatenated(sorted(query_without_sign)) + body_json + app_secret

    Notes:
    - Query string concatenation is key + value with no separators.
    - Exclude 'sign' itself.
    - Body is compact JSON for application/json; empty string if no body.
    """
    items = []
    for k in sorted(query.keys()):
        if k == "sign":
            continue
        v = query[k]
        if v is None:
            continue
        items.append(f"{k}{v}")
    qs = "".join(items)
    body_str = "" if body is None else _compact_json(body)
    base = f"{app_secret}{path}{qs}{body_str}{app_secret}"
    return hmac.new(app_secret.encode("utf-8"), base.encode("utf-8"), hashlib.sha256).hexdigest()


@dataclass
class TikTokShopClient:
    app_key: str
    app_secret: str
    access_token: str
    shop_cipher: Optional[str] = None
    base_url: str = BASE_URL
    timeout: int = 60

    @classmethod
    def from_env(cls) -> "TikTokShopClient":
        return cls(
            app_key=os.environ.get("TIKTOK_APP_KEY", ""),
            app_secret=os.environ.get("TIKTOK_APP_SECRET", ""),
            access_token=os.environ.get("TIKTOK_ACCESS_TOKEN", ""),
            shop_cipher=os.environ.get("TIKTOK_SHOP_CIPHER"),
        )

    def _headers(self, content_type: Optional[str] = None) -> Dict[str, str]:
        h = {
            "x-tts-access-token": self.access_token,
        }
        if content_type:
            h["content-type"] = content_type
        return h

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Dict[str, Any]] = None,
        body: Optional[Any] = None,
        shop_cipher: Optional[str] = None,
        content_type: Optional[str] = "application/json",
    ) -> Dict[str, Any]:
        if not self.app_key or not self.app_secret:
            return {"error": "Missing TIKTOK_APP_KEY/TIKTOK_APP_SECRET env vars"}
        if not self.access_token:
            return {"error": "Missing TIKTOK_ACCESS_TOKEN env var"}

        q = dict(query or {})
        q.setdefault("app_key", self.app_key)
        q.setdefault("timestamp", _now_ts())

        sc = shop_cipher if shop_cipher is not None else self.shop_cipher
        if sc and "shop_cipher" not in q:
            q["shop_cipher"] = sc

        q["sign"] = _sign(self.app_secret, path, q, body)

        url = self.base_url.rstrip("/") + path
        try:
            resp = requests.request(
                method.upper(),
                url,
                params=q,
                headers=self._headers(content_type if body is not None else None),
                data=None if body is None else _compact_json(body),
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        try:
            data = resp.json()
        except ValueError:
            return {"error": f"Non-JSON response ({resp.status_code})", "text": resp.text}

        if resp.status_code >= 400:
            return {"error": f"HTTP {resp.status_code}", "response": data}
        return data
