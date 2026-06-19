import os
from typing import Any, Dict

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


def _request(method: str, path: str, params: Dict[str, Any] | None = None, json: Dict[str, Any] | None = None, files: Dict[str, Any] | None = None):
    if not API_BASE:
        return {"error": "MASTODON_BASE_URL is not set"}
    try:
        resp = requests.request(method, f"{API_BASE}{path}", headers=_headers(), params=params, json=json, files=files, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.text:
            try:
                return resp.json()
            except Exception:
                return resp.text
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance_info() -> Dict[str, Any]:
    return _request("GET", "/instance")


@mcp.tool()
def get_instance_statistics() -> Dict[str, Any]:
    return _request("GET", "/instance/peers")


@mcp.tool()
def get_authenticated_account() -> Dict[str, Any]:
    return _request("GET", "/accounts/verify_credentials")


@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    return _request("GET", f"/accounts/{account_id}")


@mcp.tool()
def follow_account(account_id: str) -> Dict[str, Any]:
    return _request("POST", f"/accounts/{account_id}/follow")


@mcp.tool()
def unfollow_account(account_id: str) -> Dict[str, Any]:
    return _request("POST", f"/accounts/{account_id}/unfollow")


@mcp.tool()
def get_account_followers(account_id: str, limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", f"/accounts/{account_id}/followers", params=params)


@mcp.tool()
def get_account_following(account_id: str, limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", f"/accounts/{account_id}/following", params=params)


@mcp.tool()
def create_status(status: str, in_reply_to_id: str | None = None, media_ids: list[str] | None = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"status": status}
    if in_reply_to_id:
        payload["in_reply_to_id"] = in_reply_to_id
    if media_ids:
        payload["media_ids"] = media_ids
    return _request("POST", "/statuses", json=payload)


@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    return _request("GET", f"/statuses/{status_id}")


@mcp.tool()
def delete_status(status_id: str) -> Dict[str, Any]:
    return _request("DELETE", f"/statuses/{status_id}")


@mcp.tool()
def boost_status(status_id: str) -> Dict[str, Any]:
    return _request("POST", f"/statuses/{status_id}/reblog")


@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]:
    return _request("POST", f"/statuses/{status_id}/favourite")


@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]:
    return _request("GET", f"/statuses/{status_id}/context")


@mcp.tool()
def get_home_timeline(limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/timelines/home", params=params)


@mcp.tool()
def get_public_timeline(limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/timelines/public", params=params)


@mcp.tool()
def get_hashtag_timeline(tag: str, limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", f"/timelines/tag/{tag}", params=params)


@mcp.tool()
def get_list_timeline(list_id: str, limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", f"/timelines/list/{list_id}", params=params)


@mcp.tool()
def list_notifications(limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/notifications", params=params)


@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]:
    return _request("GET", f"/notifications/{notification_id}")


@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    return _request("POST", f"/notifications/{notification_id}/dismiss")


@mcp.tool()
def clear_notifications() -> Dict[str, Any]:
    return _request("POST", "/notifications/clear")


@mcp.tool()
def search(query: str, type: str | None = None, limit: int | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": query}
    if type:
        params["type"] = type
    if limit is not None:
        params["limit"] = limit
    return _request("GET", "/search", params=params)


@mcp.tool()
def list_bookmarks(limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/bookmarks", params=params)


@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]:
    return _request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]:
    return _request("POST", f"/statuses/{status_id}/unbookmark")


@mcp.tool()
def list_favourites(limit: int | None = None) -> Dict[str, Any]:
    params = {"limit": limit} if limit is not None else None
    return _request("GET", "/favourites", params=params)


@mcp.tool()
def upload_media(file_path: str, description: str | None = None) -> Dict[str, Any]:
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description:
                data["description"] = description
            if not API_BASE:
                return {"error": "MASTODON_BASE_URL is not set"}
            resp = requests.post(f"{API_BASE}/media", headers=_headers(), data=data, files=files, timeout=30)
            if resp.status_code >= 400:
                try:
                    return {"error": resp.json()}
                except Exception:
                    return {"error": resp.text}
            return resp.json()
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run(transport="stdio")
