import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-commerce-api")

STANDARD_BASE = "https://api.ebay.com"
MEDIA_BASE = "https://apim.ebay.com"
TOKEN_URL = f"{STANDARD_BASE}/identity/v1/oauth2/token"
SCOPE = "https://api.ebay.com/oauth/api_scope"

_app_token_cache: Dict[str, Any] = {"token": None, "expires_at": 0}
_user_token_cache: Dict[str, Any] = {"token": None, "expires_at": 0}


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.environ.get(name, default)


def _base_url_for(path: str) -> str:
    return MEDIA_BASE if path.startswith("/commerce/media/") else STANDARD_BASE


def _auth_header(path: str) -> Dict[str, str]:
    if path.startswith(("/commerce/taxonomy/", "/commerce/catalog/")):
        return {"Authorization": f"Bearer {_get_app_token()}"}
    return {"Authorization": f"Bearer {_get_user_token()}"}


def _token_request(grant_type: str, extra: Dict[str, str]) -> Dict[str, Any]:
    app_id = _env("EBAY_APP_ID")
    cert_id = _env("EBAY_CERT_ID")
    if not app_id or not cert_id:
        return {"error": "Missing EBAY_APP_ID or EBAY_CERT_ID"}
    auth = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": grant_type, "scope": SCOPE, **extra}
    resp = requests.post(TOKEN_URL, headers=headers, data=data, timeout=30)
    if resp.status_code >= 400:
        return {"error": "Token request failed", "status": resp.status_code, "details": resp.text}
    return resp.json()


def _get_app_token() -> str:
    token = _app_token_cache.get("token")
    if token:
        return token
    data = _token_request("client_credentials", {})
    if "error" in data:
        raise RuntimeError(data["error"])
    _app_token_cache["token"] = data["access_token"]
    return data["access_token"]


def _get_user_token() -> str:
    token = _user_token_cache.get("token")
    if token:
        return token
    refresh = _env("EBAY_REFRESH_TOKEN")
    if not refresh:
        raise RuntimeError("Missing EBAY_REFRESH_TOKEN")
    data = _token_request("refresh_token", {"refresh_token": refresh})
    if "error" in data:
        raise RuntimeError(data["error"])
    _user_token_cache["token"] = data["access_token"]
    return data["access_token"]


def _request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    url = f"{_base_url_for(path)}{path}"
    headers = {"Accept": "application/json", **_auth_header(path)}
    resp = requests.request(method, url, headers=headers, params=params, json=json_body, timeout=60)
    if resp.status_code >= 400:
        try:
            details = resp.json()
        except Exception:
            details = resp.text
        return {"error": "API request failed", "status": resp.status_code, "details": details}
    if not resp.text:
        return {"ok": True}
    try:
        return resp.json()
    except Exception:
        return resp.text


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": [
        "get_taxonomy_categories",
        "get_category_tree",
        "get_category_tree_aspects",
        "get_category_suggestions",
        "get_item_aspects_for_category",
        "get_compatibility_properties",
        "get_catalog_product",
        "search_catalog_products",
        "get_product_metadata",
        "create_media_upload_session",
        "get_media_upload_session",
        "complete_media_upload_session",
        "create_notification_subscription",
        "get_notification_subscriptions",
        "delete_notification_subscription",
        "get_identity_me",
        "get_identity_user",
        "translate_text",
    ]}


@mcp.tool()
def get_taxonomy_categories(category_tree_id: str) -> Any:
    return _request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}")


@mcp.tool()
def get_category_tree(category_tree_id: str) -> Any:
    return _request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}")


@mcp.tool()
def get_category_tree_aspects(category_tree_id: str, category_id: Optional[str] = None) -> Any:
    params = {"category_id": category_id} if category_id else None
    return _request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category", params=params)


@mcp.tool()
def get_category_suggestions(q: str) -> Any:
    return _request("GET", "/commerce/taxonomy/v1/category_tree/0/get_category_suggestions", params={"q": q})


@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Any:
    return _request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category", params={"category_id": category_id})


@mcp.tool()
def get_compatibility_properties(category_tree_id: str, category_id: str) -> Any:
    return _request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties", params={"category_id": category_id})


@mcp.tool()
def get_catalog_product(epid: str) -> Any:
    return _request("GET", f"/commerce/catalog/v1/product/{epid}")


@mcp.tool()
def search_catalog_products(q: str) -> Any:
    return _request("GET", "/commerce/catalog/v1/product_summary/search", params={"q": q})


@mcp.tool()
def get_product_metadata() -> Any:
    return _request("GET", "/commerce/catalog/v1/product_metadata")


@mcp.tool()
def create_media_upload_session(name: str, size: int) -> Any:
    return _request("POST", "/commerce/media/v1/upload_session", json_body={"name": name, "size": size})


@mcp.tool()
def get_media_upload_session(upload_session_id: str) -> Any:
    return _request("GET", f"/commerce/media/v1/upload_session/{upload_session_id}")


@mcp.tool()
def complete_media_upload_session(upload_session_id: str) -> Any:
    return _request("POST", f"/commerce/media/v1/upload_session/{upload_session_id}/complete")


@mcp.tool()
def create_notification_subscription(topic: str, endpoint: str) -> Any:
    return _request("POST", "/commerce/notification/v1/subscription", json_body={"topic": topic, "endpoint": endpoint})


@mcp.tool()
def get_notification_subscriptions() -> Any:
    return _request("GET", "/commerce/notification/v1/subscription")


@mcp.tool()
def delete_notification_subscription(subscription_id: str) -> Any:
    return _request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}")


@mcp.tool()
def get_identity_me() -> Any:
    return _request("GET", "/commerce/identity/v1/user/")


@mcp.tool()
def get_identity_user() -> Any:
    return _request("GET", "/commerce/identity/v1/user/")


@mcp.tool()
def translate_text(text: str, target_language: str) -> Any:
    return _request("POST", "/commerce/translation/v1_beta/translate", json_body={"text": text, "targetLanguage": target_language})


if __name__ == "__main__":
    mcp.run(transport="stdio")
