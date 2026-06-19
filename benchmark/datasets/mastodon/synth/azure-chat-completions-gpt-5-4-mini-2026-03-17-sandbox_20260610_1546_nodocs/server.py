import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mastodon")

BASE_URL = os.getenv("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN", "")
API_BASE = f"{BASE_URL}/api/v1" if BASE_URL else ""


def _headers() -> Dict[str, str]:
    headers = {"Accept": "application/json"}
    if ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    return headers


def _request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None) -> Any:
    if not API_BASE:
        return {"error": "MASTODON_BASE_URL is not set"}
    try:
        resp = requests.request(method, f"{API_BASE}{path}", headers=_headers(), params=params, json=json, files=files, timeout=30)
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        if resp.ok:
            return data
        return {"error": "request failed", "status_code": resp.status_code, "details": data}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance() -> Any:
    return _request("GET", "/instance")


@mcp.tool()
def get_instance_activity() -> Any:
    return _request("GET", "/instance/activity")


@mcp.tool()
def get_own_account() -> Any:
    return _request("GET", "/accounts/verify_credentials")


@mcp.tool()
def get_account(account_id: str) -> Any:
    return _request("GET", f"/accounts/{account_id}")


@mcp.tool()
def follow_account(account_id: str) -> Any:
    return _request("POST", f"/accounts/{account_id}/follow")


@mcp.tool()
def unfollow_account(account_id: str) -> Any:
    return _request("POST", f"/accounts/{account_id}/unfollow")


@mcp.tool()
def get_account_followers(account_id: str, limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", f"/accounts/{account_id}/followers", params=params)


@mcp.tool()
def get_account_following(account_id: str, limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", f"/accounts/{account_id}/following", params=params)


@mcp.tool()
def post_status(status: str, in_reply_to_id: Optional[str] = None, visibility: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"status": status}
    if in_reply_to_id is not None:
        payload["in_reply_to_id"] = in_reply_to_id
    if visibility is not None:
        payload["visibility"] = visibility
    return _request("POST", "/statuses", json=payload)


@mcp.tool()
def get_status(status_id: str) -> Any:
    return _request("GET", f"/statuses/{status_id}")


@mcp.tool()
def delete_status(status_id: str) -> Any:
    return _request("DELETE", f"/statuses/{status_id}")


@mcp.tool()
def boost_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/reblog")


@mcp.tool()
def favourite_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/favourite")


@mcp.tool()
def unfavourite_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unfavourite")


@mcp.tool()
def get_status_context(status_id: str) -> Any:
    return _request("GET", f"/statuses/{status_id}/context")


@mcp.tool()
def get_home_timeline(limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/timelines/home", params=params)


@mcp.tool()
def get_public_timeline(limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/timelines/public", params=params)


@mcp.tool()
def get_hashtag_timeline(tag: str, limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", f"/timelines/tag/{tag}", params=params)


@mcp.tool()
def get_list_timeline(list_id: str, limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", f"/timelines/list/{list_id}", params=params)


@mcp.tool()
def list_notifications(limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/notifications", params=params)


@mcp.tool()
def get_notification(notification_id: str) -> Any:
    return _request("GET", f"/notifications/{notification_id}")


@mcp.tool()
def dismiss_notification(notification_id: str) -> Any:
    return _request("POST", f"/notifications/{notification_id}/dismiss")


@mcp.tool()
def clear_notifications() -> Any:
    return _request("POST", "/notifications/clear")


@mcp.tool()
def search(query: str, type: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {"q": query}
    if type is not None:
        params["type"] = type
    if limit is not None:
        params["limit"] = limit
    return _request("GET", "/search", params=params)


@mcp.tool()
def list_lists() -> Any:
    return _request("GET", "/lists")


@mcp.tool()
def create_list(title: str) -> Any:
    return _request("POST", "/lists", json={"title": title})


@mcp.tool()
def get_list(list_id: str) -> Any:
    return _request("GET", f"/lists/{list_id}")


@mcp.tool()
def update_list(list_id: str, title: str) -> Any:
    return _request("PUT", f"/lists/{list_id}", json={"title": title})


@mcp.tool()
def delete_list(list_id: str) -> Any:
    return _request("DELETE", f"/lists/{list_id}")


@mcp.tool()
def add_account_to_list(list_id: str, account_id: str) -> Any:
    return _request("POST", f"/lists/{list_id}/accounts", json={"account_ids": [account_id]})


@mcp.tool()
def remove_account_from_list(list_id: str, account_id: str) -> Any:
    return _request("DELETE", f"/lists/{list_id}/accounts", json={"account_ids": [account_id]})


@mcp.tool()
def list_bookmarks() -> Any:
    return _request("GET", "/bookmarks")


@mcp.tool()
def bookmark_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def unbookmark_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unbookmark")


@mcp.tool()
def list_favourites(limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/favourites", params=params)


@mcp.tool()
def upload_media(file_url: str, description: Optional[str] = None) -> Any:
    try:
        media_resp = requests.get(file_url, timeout=30)
        media_resp.raise_for_status()
        files = {"file": (file_url.split("/")[-1] or "upload", media_resp.content)}
        data = {}
        if description is not None:
            data["description"] = description
        if not API_BASE:
            return {"error": "MASTODON_BASE_URL is not set"}
        resp = requests.post(f"{API_BASE}/media", headers={k: v for k, v in _headers().items() if k != "Accept"}, data=data, files=files, timeout=30)
        try:
            out = resp.json()
        except Exception:
            out = resp.text
        if resp.ok:
            return out
        return {"error": "request failed", "status_code": resp.status_code, "details": out}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
