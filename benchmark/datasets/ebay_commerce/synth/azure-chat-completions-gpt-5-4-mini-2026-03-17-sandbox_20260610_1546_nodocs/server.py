import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-commerce-api")

ENV = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
BASE_URL = "https://api.sandbox.ebay.com" if ENV != "PRODUCTION" else "https://api.ebay.com"
MEDIA_BASE_URL = "https://apim.sandbox.ebay.com" if ENV != "PRODUCTION" else "https://apim.ebay.com"
TOKEN_URL = f"{BASE_URL}/identity/v1/oauth2/token"
APP_ID = os.getenv("EBAY_APP_ID", "")
CERT_ID = os.getenv("EBAY_CERT_ID", "")
REFRESH_TOKEN = os.getenv("EBAY_REFRESH_TOKEN", "")

_app_token: Optional[str] = None
_user_token: Optional[str] = None


def _error(message: str, status: Optional[int] = None) -> Dict[str, Any]:
    payload = {"error": message}
    if status is not None:
        payload["status"] = status
    return payload


def _get_token(grant_type: str) -> str:
    global _app_token, _user_token
    if grant_type == "client_credentials" and _app_token:
        return _app_token
    if grant_type == "refresh_token" and _user_token:
        return _user_token
    if not APP_ID or not CERT_ID:
        raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")
    auth = base64.b64encode(f"{APP_ID}:{CERT_ID}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": grant_type, "scope": "https://api.ebay.com/oauth/api_scope"}
    if grant_type == "refresh_token":
        if not REFRESH_TOKEN:
            raise RuntimeError("Missing EBAY_REFRESH_TOKEN")
        data["refresh_token"] = REFRESH_TOKEN
    resp = requests.post(TOKEN_URL, headers=headers, data=data, timeout=30)
    if resp.status_code >= 400:
        raise RuntimeError(resp.text)
    token = resp.json().get("access_token")
    if grant_type == "client_credentials":
        _app_token = token
    else:
        _user_token = token
    return token


def _request(method: str, path: str, *, user: bool = False, media: bool = False, params=None, json_body=None):
    try:
        token = _get_token("refresh_token" if user else "client_credentials")
        base = MEDIA_BASE_URL if media else BASE_URL
        resp = requests.request(
            method,
            f"{base}{path}",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            params=params,
            json=json_body,
            timeout=60,
        )
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        if resp.status_code >= 400:
            return _error("request failed", resp.status_code) | {"details": data}
        return data
    except Exception as e:
        return _error(str(e))


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": sorted([name for name in globals() if callable(globals()[name]) and not name.startswith("_") and name not in {"list_tools"}])}


@mcp.tool()
def get_taxonomy_categories(tree_id: str) -> Dict[str, Any]:
    return _request("GET", f"/commerce/taxonomy/v1/category_tree/{tree_id}")


@mcp.tool()
def get_taxonomy_aspects(tree_id: str, category_id: str) -> Dict[str, Any]:
    return _request("GET", f"/commerce/taxonomy/v1/category_tree/{tree_id}/get_item_aspects_for_category", params={"category_id": category_id})


@mcp.tool()
def search_catalog_products(q: str, limit: int = 10) -> Dict[str, Any]:
    return _request("GET", "/commerce/catalog/v1_beta/product_summary/search", params={"q": q, "limit": limit})


@mcp.tool()
def get_catalog_product(epid: str) -> Dict[str, Any]:
    return _request("GET", f"/commerce/catalog/v1_beta/product/{epid}")


@mcp.tool()
def get_identity_user() -> Dict[str, Any]:
    return _request("GET", "/commerce/identity/v1/user", user=True)


@mcp.tool()
def get_identity_privacy_preferences() -> Dict[str, Any]:
    return _request("GET", "/commerce/identity/v1/privacy_preferences", user=True)


@mcp.tool()
def create_media_image_upload() -> Dict[str, Any]:
    return _request("POST", "/commerce/media/v1/image_upload", user=True, media=True, json_body={})


@mcp.tool()
def list_notification_subscriptions() -> Dict[str, Any]:
    return _request("GET", "/commerce/notification/v1/subscription", user=True)


@mcp.tool()
def create_notification_subscription(payload: Dict[str, Any]) -> Dict[str, Any]:
    return _request("POST", "/commerce/notification/v1/subscription", user=True, json_body=payload)


@mcp.tool()
def delete_notification_subscription(subscription_id: str) -> Dict[str, Any]:
    return _request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}", user=True)


if __name__ == "__main__":
    mcp.run()
