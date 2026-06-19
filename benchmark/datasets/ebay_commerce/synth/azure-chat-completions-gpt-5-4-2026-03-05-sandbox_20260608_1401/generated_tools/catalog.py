import os
from typing import Any, Dict, Optional

import requests


API_BASE = "https://api.sandbox.ebay.com"
PROD_BASE = "https://api.ebay.com"
TOKEN_URL_PATH = "/identity/v1/oauth2/token"
APP_SCOPE = "https://api.ebay.com/oauth/api_scope"


class EbayClient:
    def __init__(self) -> None:
        env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.base_url = API_BASE if env == "SANDBOX" else PROD_BASE
        self.client_id = os.getenv("EBAY_APP_ID", "")
        self.client_secret = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self._app_token: Optional[str] = None
        self._user_token: Optional[str] = None

    def _token_request(self, data: Dict[str, str]) -> Dict[str, Any]:
        if not self.client_id or not self.client_secret:
            return {"error": "Missing EBAY_APP_ID or EBAY_CERT_ID"}
        try:
            response = requests.post(
                f"{self.base_url}{TOKEN_URL_PATH}",
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                auth=(self.client_id, self.client_secret),
                timeout=60,
            )
            payload = response.json()
            if response.status_code >= 400:
                return {"error": payload}
            return payload
        except Exception as exc:
            return {"error": str(exc)}

    def get_app_token(self) -> Dict[str, Any]:
        if self._app_token:
            return {"access_token": self._app_token}
        payload = self._token_request({"grant_type": "client_credentials", "scope": APP_SCOPE})
        if "access_token" in payload:
            self._app_token = payload["access_token"]
        return payload

    def get_user_token(self, scope: str) -> Dict[str, Any]:
        if self._user_token:
            return {"access_token": self._user_token}
        if not self.refresh_token:
            return {"error": "Missing EBAY_REFRESH_TOKEN"}
        payload = self._token_request({
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "scope": scope,
        })
        if "access_token" in payload:
            self._user_token = payload["access_token"]
        return payload

    def request(
        self,
        method: str,
        path: str,
        *,
        token_type: str,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        base_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        token_payload = self.get_app_token() if token_type == "app" else self.get_user_token("https://api.ebay.com/oauth/api_scope/commerce.identity.readonly") if token_type == "user_identity" else {"error": "Unsupported token type"}
        if "error" in token_payload:
            return token_payload
        req_headers = {"Authorization": f"Bearer {token_payload['access_token']}"}
        if headers:
            req_headers.update(headers)
        try:
            response = requests.request(
                method,
                f"{base_url or self.base_url}{path}",
                params=params,
                json=json_body,
                headers=req_headers,
                timeout=120,
            )
            if response.content:
                try:
                    payload: Any = response.json()
                except Exception:
                    payload = {"text": response.text}
            else:
                payload = {}
            if response.status_code >= 400:
                return {"error": payload, "status_code": response.status_code}
            return payload if isinstance(payload, dict) else {"data": payload}
        except Exception as exc:
            return {"error": str(exc)}


client = EbayClient()


def get_product(epid: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    return client.request(
        "GET",
        f"/commerce/catalog/v1_beta/product/{epid}",
        token_type="app",
        headers=headers,
    )


def search_products(
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    for key, value in {
        "q": q,
        "gtin": gtin,
        "mpn": mpn,
        "category_ids": category_ids,
        "aspect_filter": aspect_filter,
        "fieldgroups": fieldgroups,
        "limit": limit,
        "offset": offset,
    }.items():
        if value is not None:
            params[key] = value
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    return client.request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        token_type="app",
        params=params,
        headers=headers,
    )
