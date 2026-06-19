from __future__ import annotations

import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-buy-api")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

TOKEN_CACHE: Dict[str, Any] = {"token": None, "expires_at": 0}


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    value = os.getenv(name, default)
    return value


def _base_url() -> str:
    env = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
    return BASE_URLS.get(env, BASE_URLS["SANDBOX"])


def _auth_token() -> str:
    import time

    now = time.time()
    if TOKEN_CACHE["token"] and TOKEN_CACHE["expires_at"] > now + 30:
        return TOKEN_CACHE["token"]

    app_id = _env("EBAY_APP_ID")
    cert_id = _env("EBAY_CERT_ID")
    if not app_id or not cert_id:
        raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID")

    creds = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    url = f"{_base_url()}/identity/v1/oauth2/token"
    headers = {
        "Authorization": f"Basic {creds}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    data = {"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"}
    resp = requests.post(url, headers=headers, data=data, timeout=30)
    if not resp.ok:
        raise ValueError(f"Token request failed: {resp.status_code} {resp.text}")
    payload = resp.json()
    TOKEN_CACHE["token"] = payload["access_token"]
    TOKEN_CACHE["expires_at"] = now + int(payload.get("expires_in", 7200))
    return TOKEN_CACHE["token"]


def _request(method: str, path: str, params: Optional[dict] = None, json_body: Any = None) -> Any:
    try:
        headers = {
            "Authorization": f"Bearer {_auth_token()}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        resp = requests.request(method, f"{_base_url()}{path}", headers=headers, params=params, json=json_body, timeout=60)
        if resp.status_code >= 400:
            return {"error": f"HTTP {resp.status_code}", "details": resp.text}
        if not resp.text:
            return {}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_items(q: str, limit: int = 10, offset: int = 0) -> Any:
    return _request("GET", "/buy/browse/v1/item_summary/search", params={"q": q, "limit": limit, "offset": offset})


@mcp.tool()
def get_item(item_id: str) -> Any:
    return _request("GET", f"/buy/browse/v1/item/{item_id}")


@mcp.tool()
def get_item_by_legacy_id(legacy_item_id: str) -> Any:
    return _request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params={"legacy_item_id": legacy_item_id})


@mcp.tool()
def get_item_group(item_group_id: str) -> Any:
    return _request("GET", f"/buy/browse/v1/item_group/{item_group_id}")


@mcp.tool()
def get_item_group_legacy(item_group_id: str) -> Any:
    return _request("GET", "/buy/browse/v1/item_group/get_item_group_by_legacy_id", params={"legacy_item_group_id": item_group_id})


@mcp.tool()
def get_deal(deal_id: str) -> Any:
    return _request("GET", f"/buy/deal/v1/deal/{deal_id}")


@mcp.tool()
def get_deals(limit: int = 10, offset: int = 0) -> Any:
    return _request("GET", "/buy/deal/v1/deal", params={"limit": limit, "offset": offset})


@mcp.tool()
def get_event(event_id: str) -> Any:
    return _request("GET", f"/buy/deal/v1/event/{event_id}")


@mcp.tool()
def get_events(limit: int = 10, offset: int = 0) -> Any:
    return _request("GET", "/buy/deal/v1/event", params={"limit": limit, "offset": offset})


@mcp.tool()
def get_item_feed(feed_type: str, limit: int = 10, offset: int = 0) -> Any:
    return _request("GET", "/buy/feed/v1/item_feed", params={"feed_type": feed_type, "limit": limit, "offset": offset})


@mcp.tool()
def get_item_snapshot(snapshot_id: str) -> Any:
    return _request("GET", f"/buy/feed/v1/item_snapshot/{snapshot_id}")


@mcp.tool()
def guest_checkout_session_create(body: dict) -> Any:
    return _request("POST", "/buy/order/v1/guest_checkout_session", json_body=body)


@mcp.tool()
def get_guest_checkout_session(session_id: str) -> Any:
    return _request("GET", f"/buy/order/v1/guest_checkout_session/{session_id}")


@mcp.tool()
def update_guest_checkout_session(session_id: str, body: dict) -> Any:
    return _request("PATCH", f"/buy/order/v1/guest_checkout_session/{session_id}", json_body=body)


@mcp.tool()
def place_order(session_id: str, body: dict) -> Any:
    return _request("POST", f"/buy/order/v1/guest_checkout_session/{session_id}/place_order", json_body=body)


if __name__ == "__main__":
    mcp.run(transport="stdio")
