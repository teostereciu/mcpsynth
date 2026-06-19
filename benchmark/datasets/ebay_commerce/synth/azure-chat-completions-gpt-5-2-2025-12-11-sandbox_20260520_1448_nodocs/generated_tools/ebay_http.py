import json
import os
from typing import Any, Dict, Optional, Tuple

import requests

from .ebay_auth import EbayAuth


EBAY_API_BASE = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

EBAY_MEDIA_BASE = {
    "SANDBOX": "https://apim.sandbox.ebay.com",
    "PRODUCTION": "https://apim.ebay.com",
}


class EbayClient:
    def __init__(self, auth: Optional[EbayAuth] = None):
        self.auth = auth or EbayAuth()
        env = (os.getenv("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
        self.api_base = EBAY_API_BASE.get(env, EBAY_API_BASE["SANDBOX"])
        self.media_base = EBAY_MEDIA_BASE.get(env, EBAY_MEDIA_BASE["SANDBOX"])

    def request(
        self,
        method: str,
        path: str,
        *,
        base: str = "api",
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        user_scope: Optional[str] = None,
        app_scope: str = "https://api.ebay.com/oauth/api_scope",
        timeout: int = 30,
    ) -> Dict[str, Any]:
        base_url = self.api_base if base == "api" else self.media_base
        url = base_url + path

        hdrs = {"Accept": "application/json"}
        if headers:
            hdrs.update(headers)

        if user_scope:
            token, err = self.auth.get_user_token(user_scope)
        else:
            token, err = self.auth.get_app_token(app_scope)
        if err:
            return err
        hdrs["Authorization"] = f"Bearer {token}"

        try:
            r = requests.request(
                method=method,
                url=url,
                params=params,
                json=json_body,
                data=data,
                headers=hdrs,
                timeout=timeout,
            )
        except Exception as e:
            return {"error": f"Request failed: {e}", "method": method, "url": url}

        content_type = r.headers.get("content-type", "")
        if r.status_code == 204:
            return {"status": 204}

        if "application/json" in content_type:
            try:
                body = r.json()
            except Exception:
                body = {"raw": r.text}
        else:
            body = {"raw": r.text}

        if r.status_code >= 400:
            return {
                "error": "eBay API error",
                "status": r.status_code,
                "method": method,
                "url": url,
                "response": body,
            }

        return body if isinstance(body, (dict, list)) else {"result": body}

    @staticmethod
    def build_headers(
        *,
        marketplace_id: Optional[str] = None,
        accept_language: Optional[str] = None,
        content_language: Optional[str] = None,
        additional: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        h: Dict[str, str] = {}
        if marketplace_id:
            h["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        if accept_language:
            h["Accept-Language"] = accept_language
        if content_language:
            h["Content-Language"] = content_language
        if additional:
            h.update(additional)
        return h


def compact(obj: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in obj.items() if v is not None}


def json_loads_maybe(s: Any) -> Any:
    if s is None:
        return None
    if isinstance(s, (dict, list)):
        return s
    if isinstance(s, str):
        st = s.strip()
        if not st:
            return None
        try:
            return json.loads(st)
        except Exception:
            return s
    return s
