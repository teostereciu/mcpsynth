import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


def _env_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"


def _token_url() -> str:
    return f"{_env_base_url()}/identity/v1/oauth2/token"


@dataclass
class TokenCache:
    access_token: Optional[str] = None
    expires_at: float = 0.0


class EbaySellClient:
    """Minimal eBay Sell API HTTP client with refresh-token OAuth."""

    def __init__(self) -> None:
        self._cache = TokenCache()

    def get_access_token(self, scope: str) -> str:
        now = time.time()
        if self._cache.access_token and now < (self._cache.expires_at - 30):
            return self._cache.access_token

        app_id = os.environ.get("EBAY_APP_ID")
        cert_id = os.environ.get("EBAY_CERT_ID")
        refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
        if not app_id or not cert_id or not refresh_token:
            raise RuntimeError("Missing EBAY_APP_ID/EBAY_CERT_ID/EBAY_REFRESH_TOKEN env vars")

        auth = base64.b64encode(f"{app_id}:{cert_id}".encode("utf-8")).decode("ascii")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {auth}",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": scope,
        }
        resp = requests.post(_token_url(), headers=headers, data=data, timeout=60)
        resp.raise_for_status()
        payload = resp.json()
        self._cache.access_token = payload["access_token"]
        self._cache.expires_at = time.time() + float(payload.get("expires_in", 7200))
        return self._cache.access_token

    def request(
        self,
        method: str,
        api: str,
        path: str,
        *,
        scope: str,
        marketplace_id: str = "EBAY_US",
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
    ) -> Any:
        base = _env_base_url()
        url = f"{base}{api}{path}"
        token = self.get_access_token(scope)
        req_headers: Dict[str, str] = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if json is not None:
            req_headers["Content-Type"] = "application/json"
        if marketplace_id:
            req_headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        if headers:
            req_headers.update(headers)

        try:
            resp = requests.request(
                method.upper(),
                url,
                headers=req_headers,
                params=params,
                json=json,
                timeout=90,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        if resp.status_code == 204:
            return {"status": 204}

        content_type = resp.headers.get("Content-Type", "")
        if "application/json" in content_type:
            try:
                body: Any = resp.json()
            except Exception:
                body = {"raw": resp.text}
        else:
            body = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            return body

        msg = None
        if isinstance(body, dict):
            if "errors" in body and isinstance(body["errors"], list) and body["errors"]:
                first = body["errors"][0]
                msg = first.get("message") or first.get("longMessage")
            msg = msg or body.get("message")
        return {
            "error": msg or f"HTTP {resp.status_code}",
            "status": resp.status_code,
            "details": body,
            "url": url,
        }


# Common scopes per API family
SCOPE_INVENTORY = "https://api.ebay.com/oauth/api_scope/sell.inventory"
SCOPE_ACCOUNT = "https://api.ebay.com/oauth/api_scope/sell.account"
SCOPE_FULFILLMENT = "https://api.ebay.com/oauth/api_scope/sell.fulfillment"
SCOPE_FEED = "https://api.ebay.com/oauth/api_scope/sell.feed"
SCOPE_MARKETING = "https://api.ebay.com/oauth/api_scope/sell.marketing"
SCOPE_FINANCES = "https://api.ebay.com/oauth/api_scope/sell.finances"
SCOPE_ANALYTICS = "https://api.ebay.com/oauth/api_scope/sell.analytics"
SCOPE_METADATA = "https://api.ebay.com/oauth/api_scope/sell.metadata"
SCOPE_LOGISTICS = "https://api.ebay.com/oauth/api_scope/sell.logistics"
SCOPE_NEGOTIATION = "https://api.ebay.com/oauth/api_scope/sell.negotiation"
SCOPE_RECOMMENDATION = "https://api.ebay.com/oauth/api_scope/sell.recommendation"
SCOPE_STORES = "https://api.ebay.com/oauth/api_scope/sell.stores"
SCOPE_COMPLIANCE = "https://api.ebay.com/oauth/api_scope/sell.compliance"
