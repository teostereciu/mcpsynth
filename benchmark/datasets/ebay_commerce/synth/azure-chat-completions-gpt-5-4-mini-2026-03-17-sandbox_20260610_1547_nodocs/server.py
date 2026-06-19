import base64
import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

mcp = FastMCP("ebay-commerce-api")

ENV = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
BASE_URL = "https://api.sandbox.ebay.com" if ENV != "PRODUCTION" else "https://api.ebay.com"
MEDIA_BASE_URL = "https://apim.sandbox.ebay.com" if ENV != "PRODUCTION" else "https://apim.ebay.com"
TOKEN_URL = f"{BASE_URL}/identity/v1/oauth2/token"

_app_token: Optional[str] = None
_user_token: Optional[str] = None


def _error(message: str, **extra: Any) -> Dict[str, Any]:
    data = {"error": message}
    data.update(extra)
    return data


def _get_creds() -> tuple[str, str]:
    cid = os.getenv("EBAY_APP_ID")
    secret = os.getenv("EBAY_CERT_ID")
    if not cid or not secret:
        raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")
    return cid, secret


def _basic_auth() -> str:
    cid, secret = _get_creds()
    token = base64.b64encode(f"{cid}:{secret}".encode()).decode()
    return f"Basic {token}"


def _fetch_app_token() -> str:
    global _app_token
    if _app_token:
        return _app_token
    resp = requests.post(TOKEN_URL, headers={"Authorization": _basic_auth(), "Content-Type": "application/x-www-form-urlencoded"}, data={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"}, timeout=30)
    resp.raise_for_status()
    _app_token = resp.json()["access_token"]
    return _app_token


def _fetch_user_token() -> str:
    global _user_token
    if _user_token:
        return _user_token
    rt = os.getenv("EBAY_REFRESH_TOKEN")
    if not rt:
        raise RuntimeError("Missing EBAY_REFRESH_TOKEN")
    resp = requests.post(TOKEN_URL, headers={"Authorization": _basic_auth(), "Content-Type": "application/x-www-form-urlencoded"}, data={"grant_type": "refresh_token", "refresh_token": rt}, timeout=30)
    resp.raise_for_status()
    _user_token = resp.json()["access_token"]
    return _user_token


def _request(method: str, url: str, *, token_type: str, params=None, json=None) -> Any:
    token = _fetch_app_token() if token_type == "app" else _fetch_user_token()
    resp = requests.request(method, url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}, params=params, json=json, timeout=60)
    if resp.status_code >= 400:
        try:
            return {"error": resp.json()}
        except Exception:
            return {"error": resp.text, "status_code": resp.status_code}
    try:
        return resp.json()
    except Exception:
        return resp.text


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["get_identity", "get_taxonomy_categories", "search_catalog", "create_media_upload_session", "get_media_upload_session", "create_notification_subscription", "list_notification_subscriptions"]}


@mcp.tool()
def get_identity() -> Any:
    return _request("GET", f"{BASE_URL}/commerce/identity/v1/user", token_type="user")


@mcp.tool()
def get_taxonomy_categories(category_tree_id: str) -> Any:
    return _request("GET", f"{BASE_URL}/commerce/taxonomy/v1/category_tree/{category_tree_id}", token_type="app")


@mcp.tool()
def search_catalog(q: str, limit: int = 10) -> Any:
    return _request("GET", f"{BASE_URL}/commerce/catalog/v1_beta/product_summary/search", token_type="app", params={"q": q, "limit": limit})


@mcp.tool()
def create_media_upload_session(name: str, content_type: str) -> Any:
    return _request("POST", f"{MEDIA_BASE_URL}/commerce/media/v1/upload_session", token_type="user", json={"name": name, "contentType": content_type})


@mcp.tool()
def get_media_upload_session(upload_session_id: str) -> Any:
    return _request("GET", f"{MEDIA_BASE_URL}/commerce/media/v1/upload_session/{upload_session_id}", token_type="user")


@mcp.tool()
def create_notification_subscription(topic: str, endpoint: str) -> Any:
    return _request("POST", f"{BASE_URL}/commerce/notification/v1/subscription", token_type="user", json={"topic": topic, "endpoint": endpoint})


@mcp.tool()
def list_notification_subscriptions() -> Any:
    return _request("GET", f"{BASE_URL}/commerce/notification/v1/subscription", token_type="user")


if __name__ == "__main__":
    mcp.run()
