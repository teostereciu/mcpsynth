import os
from typing import Any, Dict, Optional

import requests

from .ebay_auth import EbayAuth


BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


class EbayClient:
    def __init__(self, auth: Optional[EbayAuth] = None):
        self.auth = auth or EbayAuth()
        env = (os.getenv("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
        self.base_url = BASE_URLS.get(env, BASE_URLS["SANDBOX"])

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        tok = self.auth.get_access_token(scope=scope)
        if "error" in tok:
            return tok

        url = self.base_url + path
        h = {
            "Authorization": f"Bearer {tok['access_token']}",
            "Accept": "application/json",
        }
        if headers:
            h.update(headers)

        try:
            resp = requests.request(method, url, params=params, json=json, headers=h, timeout=60)
        except Exception as e:
            return {"error": f"Request failed: {e}", "method": method, "url": url}

        if resp.status_code == 204:
            return {"status": 204}

        body = _safe_json(resp)
        if resp.status_code >= 400:
            return {
                "error": "API error",
                "status": resp.status_code,
                "method": method,
                "path": path,
                "body": body,
            }
        return body


def _safe_json(resp: requests.Response):
    try:
        return resp.json()
    except Exception:
        return {"text": resp.text}
