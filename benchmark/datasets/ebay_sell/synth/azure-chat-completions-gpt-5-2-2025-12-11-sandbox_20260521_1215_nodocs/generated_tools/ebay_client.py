from __future__ import annotations

import json
from typing import Any, Dict, Optional

import requests

from .ebay_auth import EbayAuth


class EbayClient:
    def __init__(self, auth: Optional[EbayAuth] = None):
        self.auth = auth or EbayAuth()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        url = self.auth.base_url + path
        token = self.auth.get_access_token()
        h = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if content_type:
            h["Content-Type"] = content_type
        if headers:
            h.update(headers)

        try:
            resp = requests.request(
                method,
                url,
                params=params,
                json=json_body,
                headers=h,
                timeout=60,
            )
        except Exception as e:
            return {"error": str(e)}

        if resp.status_code == 204:
            return {"status": 204}

        text = resp.text or ""
        if resp.status_code >= 400:
            # Try to parse eBay error payloads
            try:
                return {"error": resp.json(), "status": resp.status_code}
            except Exception:
                return {"error": text, "status": resp.status_code}

        if not text:
            return {"status": resp.status_code}

        # Prefer JSON
        try:
            return resp.json()
        except Exception:
            return {"status": resp.status_code, "body": text}


def omit_none(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}
