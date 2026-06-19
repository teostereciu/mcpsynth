import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mastodon")
BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")
API_BASE = f"{BASE_URL}/api/v1" if BASE_URL else ""
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"} if ACCESS_TOKEN else {}


def _request(method: str, path: str, *, params=None, data=None, files=None) -> Dict[str, Any]:
    if not API_BASE:
        return {"error": "MASTODON_BASE_URL is not set"}
    try:
        resp = requests.request(method, f"{API_BASE}{path}", headers=HEADERS, params=params, data=data, files=files, timeout=30)
        try:
            payload = resp.json()
        except Exception:
            payload = resp.text
        if resp.ok:
            return payload if isinstance(payload, (dict, list, str, int, float, bool)) else {"result": payload}
        return {"error": payload.get("error") if isinstance(payload, dict) and "error" in payload else f"HTTP {resp.status_code}", "details": payload if isinstance(payload, dict) else None}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["get_account", "get_status", "create_status", "delete_status", "get_status_context", "favourite_status", "unfavourite_status", "boost_status", "unboost_status", "bookmark_status", "unbookmark_status", "get_notifications", "get_notification", "clear_notifications", "dismiss_notification", "get_lists", "get_list", "create_list", "update_list", "delete_list", "get_list_accounts", "add_list_accounts", "remove_list_accounts", "search", "upload_media", "get_instance", "get_bookmarks", "get_favourites"]}


@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]: return _request("GET", f"/accounts/{account_id}")
@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]: return _request("GET", f"/statuses/{status_id}")
@mcp.tool()
def create_status(status: str = "", **kwargs) -> Dict[str, Any]: return _request("POST", "/statuses", data={"status": status, **{k: v for k, v in kwargs.items() if v is not None}})
@mcp.tool()
def delete_status(status_id: str, delete_media: bool = False) -> Dict[str, Any]: return _request("DELETE", f"/statuses/{status_id}", params={"delete_media": str(delete_media).lower()})
@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]: return _request("GET", f"/statuses/{status_id}/context")
@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]: return _request("POST", f"/statuses/{status_id}/favourite")
@mcp.tool()
def unfavourite_status(status_id: str) -> Dict[str, Any]: return _request("POST", f"/statuses/{status_id}/unfavourite")
@mcp.tool()
def boost_status(status_id: str) -> Dict[str, Any]: return _request("POST", f"/statuses/{status_id}/reblog")
@mcp.tool()
def unboost_status(status_id: str) -> Dict[str, Any]: return _request("POST", f"/statuses/{status_id}/unreblog")
@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]: return _request("POST", f"/statuses/{status_id}/bookmark")
@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]: return _request("POST", f"/statuses/{status_id}/unbookmark")
@mcp.tool()
def get_notifications(**params) -> Dict[str, Any]: return _request("GET", "/notifications", params={k: v for k, v in params.items() if v is not None})
@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]: return _request("GET", f"/notifications/{notification_id}")
@mcp.tool()
def clear_notifications() -> Dict[str, Any]: return _request("POST", "/notifications/clear")
@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]: return _request("POST", f"/notifications/{notification_id}/dismiss")
@mcp.tool()
def get_lists() -> Dict[str, Any]: return _request("GET", "/lists")
@mcp.tool()
def get_list(list_id: str) -> Dict[str, Any]: return _request("GET", f"/lists/{list_id}")
@mcp.tool()
def create_list(title: str) -> Dict[str, Any]: return _request("POST", "/lists", data={"title": title})
@mcp.tool()
def update_list(list_id: str, title: str) -> Dict[str, Any]: return _request("PUT", f"/lists/{list_id}", data={"title": title})
@mcp.tool()
def delete_list(list_id: str) -> Dict[str, Any]: return _request("DELETE", f"/lists/{list_id}")
@mcp.tool()
def get_list_accounts(list_id: str) -> Dict[str, Any]: return _request("GET", f"/lists/{list_id}/accounts")
@mcp.tool()
def add_list_accounts(list_id: str, account_ids: str) -> Dict[str, Any]: return _request("POST", f"/lists/{list_id}/accounts", data={"account_ids[]": account_ids})
@mcp.tool()
def remove_list_accounts(list_id: str, account_ids: str) -> Dict[str, Any]: return _request("DELETE", f"/lists/{list_id}/accounts", data={"account_ids[]": account_ids})
@mcp.tool()
def search(q: str, **params) -> Dict[str, Any]: return _request("GET", "/search", params={"q": q, **{k: v for k, v in params.items() if v is not None}})
@mcp.tool()
def upload_media(file_url: str) -> Dict[str, Any]: return _request("POST", "/media", data={"file": file_url})
@mcp.tool()
def get_instance() -> Dict[str, Any]: return _request("GET", "/instance")
@mcp.tool()
def get_bookmarks() -> Dict[str, Any]: return _request("GET", "/bookmarks")
@mcp.tool()
def get_favourites() -> Dict[str, Any]: return _request("GET", "/favourites")


if __name__ == "__main__":
    mcp.run()
