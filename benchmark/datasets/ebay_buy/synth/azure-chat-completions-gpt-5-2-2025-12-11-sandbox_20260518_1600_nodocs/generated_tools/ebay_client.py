from __future__ import annotations

from typing import Any, Dict, Optional

import requests

from .ebay_auth import EbayAuth


class EbayClient:
    def __init__(self, auth: Optional[EbayAuth] = None) -> None:
        self.auth = auth or EbayAuth()

    def request(
        self,
        method: str,
        path: str,
        *,
        scope: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        tok = self.auth.get_token(scope)
        if "error" in tok:
            return tok

        url = f"{self.auth.base_url()}{path}"
        req_headers = {
            "Authorization": f"Bearer {tok['access_token']}",
            "Accept": "application/json",
        }
        if headers:
            req_headers.update(headers)

        try:
            resp = requests.request(method, url, params=params, json=json, headers=req_headers, timeout=30)
        except Exception as e:
            return {"error": f"Request failed: {e}", "method": method, "url": url}

        if resp.status_code >= 400:
            return {
                "error": f"HTTP {resp.status_code}",
                "method": method,
                "url": url,
                "details": _safe_json(resp),
            }

        return _safe_json(resp)


def _safe_json(resp: requests.Response) -> Any:
    try:
        return resp.json()
    except Exception:
        return {"text": resp.text}
