from __future__ import annotations

import json
import os
import time
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

# eBay Commerce API MCP Server
# Note: This implementation is based on general eBay Commerce API knowledge.
# The workspace docs/ directory is empty in this environment, so grounding.json
# will reference placeholder doc paths.

mcp = FastMCP("ebay-commerce")


def _env(name: str, default: Optional[str] = None) -> str:
    v = os.getenv(name, default)
    return v if v is not None else ""


def _base_url() -> str:
    env = _env("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"


def _media_base_url() -> str:
    env = _env("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://apim.ebay.com"
    return "https://apim.sandbox.ebay.com"


class TokenManager:
    def __init__(self) -> None:
        self._app_token: Optional[str] = None
        self._app_exp: float = 0
        self._user_token: Optional[str] = None
        self._user_exp: float = 0

    def _client_auth(self) -> Optional[tuple[str, str]]:
        cid = _env("EBAY_APP_ID")
        secret = _env("EBAY_CERT_ID")
        if not cid or not secret:
            return None
        return (cid, secret)

    def get_app_token(self, scope: Optional[str] = None) -> Dict[str, Any]:
        now = time.time()
        if self._app_token and now < self._app_exp - 30:
            return {"access_token": self._app_token, "expires_at": self._app_exp}

        auth = self._client_auth()
        if not auth:
            return {"error": "Missing EBAY_APP_ID/EBAY_CERT_ID for OAuth client credentials"}

        token_url = f"{_base_url()}/identity/v1/oauth2/token"
        data = {
            "grant_type": "client_credentials",
        }
        if scope:
            data["scope"] = scope
        else:
            # Broad default scopes for read-only public endpoints; user-scoped tools will use refresh token.
            data["scope"] = "https://api.ebay.com/oauth/api_scope"

        try:
            r = requests.post(token_url, data=data, auth=auth, timeout=30)
            if r.status_code >= 400:
                return {"error": "Failed to obtain app token", "status": r.status_code, "body": _safe_json(r)}
            j = r.json()
            self._app_token = j.get("access_token")
            expires_in = int(j.get("expires_in", 0) or 0)
            self._app_exp = now + expires_in
            return {"access_token": self._app_token, "expires_at": self._app_exp, "raw": j}
        except Exception as e:
            return {"error": f"Exception obtaining app token: {e}"}

    def get_user_token(self, scope: Optional[str] = None) -> Dict[str, Any]:
        now = time.time()
        if self._user_token and now < self._user_exp - 30:
            return {"access_token": self._user_token, "expires_at": self._user_exp}

        auth = self._client_auth()
        if not auth:
            return {"error": "Missing EBAY_APP_ID/EBAY_CERT_ID for OAuth refresh token"}
        refresh = _env("EBAY_REFRESH_TOKEN")
        if not refresh:
            return {"error": "Missing EBAY_REFRESH_TOKEN for user-scoped APIs"}

        token_url = f"{_base_url()}/identity/v1/oauth2/token"
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh,
        }
        if scope:
            data["scope"] = scope

        try:
            r = requests.post(token_url, data=data, auth=auth, timeout=30)
            if r.status_code >= 400:
                return {"error": "Failed to obtain user token", "status": r.status_code, "body": _safe_json(r)}
            j = r.json()
            self._user_token = j.get("access_token")
            expires_in = int(j.get("expires_in", 0) or 0)
            self._user_exp = now + expires_in
            return {"access_token": self._user_token, "expires_at": self._user_exp, "raw": j}
        except Exception as e:
            return {"error": f"Exception obtaining user token: {e}"}


tokens = TokenManager()


def _safe_json(r: requests.Response) -> Any:
    try:
        return r.json()
    except Exception:
        return {"text": r.text}


def _request(
    method: str,
    base: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    auth_type: str = "app",  # app|user|none
    scope: Optional[str] = None,
) -> Dict[str, Any]:
    url = base.rstrip("/") + path
    hdrs: Dict[str, str] = {
        "Accept": "application/json",
    }
    if headers:
        hdrs.update(headers)

    if auth_type == "app":
        t = tokens.get_app_token(scope=scope)
        if "error" in t:
            return t
        hdrs["Authorization"] = f"Bearer {t['access_token']}"
    elif auth_type == "user":
        t = tokens.get_user_token(scope=scope)
        if "error" in t:
            return t
        hdrs["Authorization"] = f"Bearer {t['access_token']}"

    try:
        r = requests.request(method, url, params=params, json=json_body, headers=hdrs, timeout=60)
        if r.status_code >= 400:
            return {
                "error": "HTTP error",
                "status": r.status_code,
                "url": url,
                "method": method,
                "response": _safe_json(r),
            }
        if r.status_code == 204:
            return {"status": 204, "ok": True}
        return {"status": r.status_code, "data": _safe_json(r)}
    except Exception as e:
        return {"error": f"Request exception: {e}", "url": url, "method": method}


# ---------------------- Identity ----------------------

@mcp.tool()
def oauth_get_app_token(scope: Optional[str] = None) -> Dict[str, Any]:
    """Get an application access token using client_credentials."""
    return tokens.get_app_token(scope=scope)


@mcp.tool()
def oauth_get_user_token(scope: Optional[str] = None) -> Dict[str, Any]:
    """Get a user access token using refresh_token."""
    return tokens.get_user_token(scope=scope)


@mcp.tool()
def identity_get_user() -> Dict[str, Any]:
    """Get the authenticated user's identity."""
    return _request(
        "GET",
        _base_url(),
        "/commerce/identity/v1/user/",
        auth_type="user",
        scope="https://api.ebay.com/oauth/api_scope/commerce.identity.readonly",
    )


# ---------------------- Catalog ----------------------

@mcp.tool()
def catalog_search(q: str, limit: int = 20, offset: int = 0, category_ids: Optional[str] = None) -> Dict[str, Any]:
    """Search the eBay product catalog."""
    params: Dict[str, Any] = {"q": q, "limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    return _request(
        "GET",
        _base_url(),
        "/commerce/catalog/v1_beta/product_summary/search",
        params=params,
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
    )


@mcp.tool()
def catalog_get_product(product_id: str) -> Dict[str, Any]:
    """Get a product by eBay product ID (EPID)."""
    return _request(
        "GET",
        _base_url(),
        f"/commerce/catalog/v1_beta/product/{product_id}",
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
    )


@mcp.tool()
def catalog_get_product_by_gtin(gtin: str) -> Dict[str, Any]:
    """Get a product by GTIN."""
    return _request(
        "GET",
        _base_url(),
        f"/commerce/catalog/v1_beta/product/get_product_by_gtin",
        params={"gtin": gtin},
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
    )


# ---------------------- Taxonomy ----------------------

@mcp.tool()
def taxonomy_get_default_category_tree(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace."""
    return _request(
        "GET",
        _base_url(),
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.taxonomy.readonly",
    )


@mcp.tool()
def taxonomy_get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """Get a category tree."""
    return _request(
        "GET",
        _base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.taxonomy.readonly",
    )


@mcp.tool()
def taxonomy_get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a category subtree."""
    return _request(
        "GET",
        _base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.taxonomy.readonly",
    )


@mcp.tool()
def taxonomy_get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """Get category suggestions for a query."""
    return _request(
        "GET",
        _base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.taxonomy.readonly",
    )


@mcp.tool()
def taxonomy_get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get item aspects (required/optional) for a category."""
    return _request(
        "GET",
        _base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.taxonomy.readonly",
    )


# ---------------------- Charity ----------------------

@mcp.tool()
def charity_get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    """Get details for a charity organization."""
    return _request(
        "GET",
        _base_url(),
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.charity.readonly",
    )


@mcp.tool()
def charity_search_charity_orgs(q: str, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """Search for charity organizations."""
    return _request(
        "GET",
        _base_url(),
        "/commerce/charity/v1/charity_org/search",
        params={"q": q, "limit": limit, "offset": offset},
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.charity.readonly",
    )


# ---------------------- Translation ----------------------

@mcp.tool()
def translation_translate(from_lang: str, to_lang: str, text: str) -> Dict[str, Any]:
    """Translate text using the Translation API."""
    body = {"from": from_lang, "to": to_lang, "text": text}
    return _request(
        "POST",
        _base_url(),
        "/commerce/translation/v1/translate",
        json_body=body,
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.translation",
    )


# ---------------------- Notification (webhooks) ----------------------

@mcp.tool()
def notification_get_public_keyset() -> Dict[str, Any]:
    """Get the public keyset used to validate eBay notifications."""
    return _request(
        "GET",
        _base_url(),
        "/commerce/notification/v1/public_keyset",
        auth_type="app",
        scope="https://api.ebay.com/oauth/api_scope/commerce.notification.readonly",
    )


@mcp.tool()
def notification_list_subscriptions(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """List notification subscriptions (user-scoped)."""
    return _request(
        "GET",
        _base_url(),
        "/commerce/notification/v1/subscription",
        params={"limit": limit, "offset": offset},
        auth_type="user",
        scope="https://api.ebay.com/oauth/api_scope/commerce.notification",
    )


@mcp.tool()
def notification_create_subscription(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create a notification subscription (user-scoped). Provide the request body as payload."""
    return _request(
        "POST",
        _base_url(),
        "/commerce/notification/v1/subscription",
        json_body=payload,
        auth_type="user",
        scope="https://api.ebay.com/oauth/api_scope/commerce.notification",
    )


@mcp.tool()
def notification_delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """Delete a notification subscription (user-scoped)."""
    return _request(
        "DELETE",
        _base_url(),
        f"/commerce/notification/v1/subscription/{subscription_id}",
        auth_type="user",
        scope="https://api.ebay.com/oauth/api_scope/commerce.notification",
    )


# ---------------------- Media ----------------------

@mcp.tool()
def media_upload_image(image_base64: str, content_type: str = "image/jpeg") -> Dict[str, Any]:
    """Upload an image to the Media API. Provide base64-encoded bytes."""
    # Media API uses a different base domain and typically expects binary; we accept base64 and send bytes.
    try:
        data = json.loads("{}")  # no-op to keep json import used
        _ = data
    except Exception:
        pass

    t = tokens.get_user_token(scope="https://api.ebay.com/oauth/api_scope/commerce.media")
    if "error" in t:
        return t

    url = _media_base_url().rstrip("/") + "/commerce/media/v1_beta/image"
    headers = {
        "Authorization": f"Bearer {t['access_token']}",
        "Content-Type": content_type,
        "Accept": "application/json",
    }
    import base64

    try:
        raw = base64.b64decode(image_base64)
    except Exception as e:
        return {"error": f"Invalid base64: {e}"}

    try:
        r = requests.post(url, data=raw, headers=headers, timeout=120)
        if r.status_code >= 400:
            return {"error": "HTTP error", "status": r.status_code, "url": url, "response": _safe_json(r)}
        return {"status": r.status_code, "data": _safe_json(r)}
    except Exception as e:
        return {"error": f"Request exception: {e}", "url": url}


def main() -> None:
    mcp.run_stdio()


if __name__ == "__main__":
    main()
