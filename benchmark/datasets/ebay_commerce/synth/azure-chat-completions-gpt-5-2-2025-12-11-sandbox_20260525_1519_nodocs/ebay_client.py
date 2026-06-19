import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class EbayApiError(Exception):
    pass


def _env(name: str, default: Optional[str] = None) -> str:
    v = os.getenv(name, default)
    if v is None or v == "":
        raise EbayApiError(f"Missing required environment variable: {name}")
    return v


def _base_urls() -> Tuple[str, str]:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env not in {"SANDBOX", "PRODUCTION"}:
        env = "SANDBOX"
    if env == "PRODUCTION":
        return "https://api.ebay.com", "https://apim.ebay.com"
    return "https://api.sandbox.ebay.com", "https://apim.sandbox.ebay.com"


@dataclass
class Token:
    access_token: str
    expires_at: float

    def valid(self) -> bool:
        return self.access_token and time.time() < (self.expires_at - 30)


class EbayOAuth:
    def __init__(self):
        self.client_id = _env("EBAY_APP_ID")
        self.client_secret = _env("EBAY_CERT_ID")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self.api_base, self.media_base = _base_urls()
        self._app_token: Optional[Token] = None
        self._user_token: Optional[Token] = None

    def _basic_auth_header(self) -> str:
        raw = f"{self.client_id}:{self.client_secret}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def _token_url(self) -> str:
        return f"{self.api_base}/identity/v1/oauth2/token"

    def get_app_token(self, scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
        if self._app_token and self._app_token.valid():
            return self._app_token.access_token
        data = {
            "grant_type": "client_credentials",
            "scope": scope,
        }
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        r = requests.post(self._token_url(), data=data, headers=headers, timeout=30)
        if r.status_code >= 400:
            raise EbayApiError(f"OAuth app token error {r.status_code}: {r.text}")
        j = r.json()
        token = j.get("access_token")
        expires_in = float(j.get("expires_in", 0))
        self._app_token = Token(token, time.time() + expires_in)
        return token

    def get_user_token(self, scope: Optional[str] = None) -> str:
        if not self.refresh_token:
            raise EbayApiError("Missing EBAY_REFRESH_TOKEN for user-scoped APIs")
        if self._user_token and self._user_token.valid():
            return self._user_token.access_token
        data: Dict[str, str] = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }
        if scope:
            data["scope"] = scope
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        r = requests.post(self._token_url(), data=data, headers=headers, timeout=30)
        if r.status_code >= 400:
            raise EbayApiError(f"OAuth user token error {r.status_code}: {r.text}")
        j = r.json()
        token = j.get("access_token")
        expires_in = float(j.get("expires_in", 0))
        self._user_token = Token(token, time.time() + expires_in)
        return token


class EbayClient:
    def __init__(self):
        self.oauth = EbayOAuth()
        self.api_base = self.oauth.api_base
        self.media_base = self.oauth.media_base

    def _request(
        self,
        method: str,
        base: str,
        path: str,
        token_type: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        url = base + path
        hdrs: Dict[str, str] = {"Accept": "application/json"}
        if headers:
            hdrs.update(headers)
        try:
            if token_type == "app":
                token = self.oauth.get_app_token()
            elif token_type == "user":
                token = self.oauth.get_user_token()
            else:
                raise EbayApiError(f"Unknown token_type: {token_type}")
            hdrs["Authorization"] = f"Bearer {token}"
        except Exception as e:
            return {"error": str(e)}

        try:
            r = requests.request(method, url, params=params, json=json, headers=hdrs, timeout=60)
        except Exception as e:
            return {"error": f"Request failed: {e}"}

        if r.status_code == 204:
            return {"status": 204}

        content_type = r.headers.get("content-type", "")
        body: Any
        if "application/json" in content_type:
            try:
                body = r.json()
            except Exception:
                body = {"raw": r.text}
        else:
            body = {"raw": r.text}

        if r.status_code >= 400:
            return {"error": f"HTTP {r.status_code}", "details": body}
        if isinstance(body, dict):
            body.setdefault("_http", {"status": r.status_code})
        return body if isinstance(body, (dict, list)) else {"result": body}

    # ---- Commerce Taxonomy (app token) ----
    def get_default_category_tree_id(self, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            "/commerce/taxonomy/v1/get_default_category_tree_id",
            "app",
            params={"marketplace_id": marketplace_id},
        )

    def get_category_tree(self, category_tree_id: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
            "app",
        )

    def get_category_subtree(self, category_tree_id: str, category_id: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
            "app",
            params={"category_id": category_id},
        )

    def get_category_suggestions(self, category_tree_id: str, q: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
            "app",
            params={"q": q},
        )

    def get_item_aspects_for_category(self, category_tree_id: str, category_id: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
            "app",
            params={"category_id": category_id},
        )

    def get_compatibility_properties(self, category_tree_id: str, category_id: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
            "app",
            params={"category_id": category_id},
        )

    def get_compatibility_property_values(
        self,
        category_tree_id: str,
        category_id: str,
        compatibility_property: str,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
        if filter:
            params["filter"] = filter
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
            "app",
            params=params,
        )

    # ---- Commerce Catalog (app token) ----
    def get_product(self, epid: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/catalog/v1/product/{epid}",
            "app",
        )

    def get_product_by_gtin(self, gtin: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            "/commerce/catalog/v1/product",
            "app",
            params={"gtin": gtin},
        )

    def search_products(self, q: str, limit: int = 20, offset: int = 0, category_ids: Optional[str] = None) -> Dict[str, Any]:
        params: Dict[str, Any] = {"q": q, "limit": limit, "offset": offset}
        if category_ids:
            params["category_ids"] = category_ids
        return self._request(
            "GET",
            self.api_base,
            "/commerce/catalog/v1/product_summary/search",
            "app",
            params=params,
        )

    # ---- Commerce Identity (user token) ----
    def get_user(self) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            "/commerce/identity/v1/user/",
            "user",
        )

    # ---- Commerce Notification (user token) ----
    def get_public_key(self, public_key_id: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/notification/v1/public_key/{public_key_id}",
            "user",
        )

    def get_public_keys(self, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            "/commerce/notification/v1/public_key",
            "user",
            params={"limit": limit, "offset": offset},
        )

    def create_subscription(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self._request(
            "POST",
            self.api_base,
            "/commerce/notification/v1/subscription",
            "user",
            json=payload,
        )

    def get_subscription(self, subscription_id: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/notification/v1/subscription/{subscription_id}",
            "user",
        )

    def get_subscriptions(self, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            "/commerce/notification/v1/subscription",
            "user",
            params={"limit": limit, "offset": offset},
        )

    def update_subscription(self, subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self._request(
            "PUT",
            self.api_base,
            f"/commerce/notification/v1/subscription/{subscription_id}",
            "user",
            json=payload,
        )

    def delete_subscription(self, subscription_id: str) -> Dict[str, Any]:
        return self._request(
            "DELETE",
            self.api_base,
            f"/commerce/notification/v1/subscription/{subscription_id}",
            "user",
        )

    # ---- Commerce Media (user token, different base) ----
    def create_upload_job(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self._request(
            "POST",
            self.media_base,
            "/commerce/media/v1_beta/upload_job",
            "user",
            json=payload,
        )

    def get_upload_job(self, upload_job_id: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.media_base,
            f"/commerce/media/v1_beta/upload_job/{upload_job_id}",
            "user",
        )

    def upload_file_part(
        self,
        upload_job_id: str,
        part_sequence: int,
        content: str,
        content_type: str = "application/octet-stream",
    ) -> Dict[str, Any]:
        # Note: This endpoint typically expects binary. We accept base64 string content for MCP JSON.
        try:
            import base64 as _b64

            data = _b64.b64decode(content)
        except Exception as e:
            return {"error": f"Invalid base64 content: {e}"}

        url = f"{self.media_base}/commerce/media/v1_beta/upload_job/{upload_job_id}/upload_part"
        try:
            token = self.oauth.get_user_token()
        except Exception as e:
            return {"error": str(e)}

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": content_type,
            "Content-Range": f"bytes */*",
            "Accept": "application/json",
        }
        params = {"part_sequence": part_sequence}
        try:
            r = requests.put(url, params=params, data=data, headers=headers, timeout=120)
        except Exception as e:
            return {"error": f"Request failed: {e}"}

        if r.status_code == 204:
            return {"status": 204}
        try:
            j = r.json()
        except Exception:
            j = {"raw": r.text}
        if r.status_code >= 400:
            return {"error": f"HTTP {r.status_code}", "details": j}
        return j

    def complete_upload_job(self, upload_job_id: str) -> Dict[str, Any]:
        return self._request(
            "POST",
            self.media_base,
            f"/commerce/media/v1_beta/upload_job/{upload_job_id}/complete",
            "user",
        )

    # ---- Commerce Charity (app token in practice; docs vary; use app token) ----
    def get_charity_org(self, charity_org_id: str) -> Dict[str, Any]:
        return self._request(
            "GET",
            self.api_base,
            f"/commerce/charity/v1/charity_org/{charity_org_id}",
            "app",
        )

    def get_charity_orgs(self, limit: int = 20, offset: int = 0, q: Optional[str] = None) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if q:
            params["q"] = q
        return self._request(
            "GET",
            self.api_base,
            "/commerce/charity/v1/charity_org",
            "app",
            params=params,
        )

    # ---- Commerce Translation (app token) ----
    def translate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self._request(
            "POST",
            self.api_base,
            "/commerce/translation/v1/translate",
            "app",
            json=payload,
        )
