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


def _request(method: str, path: str, *, params=None, json=None, data=None, files=None) -> Any:
    if not API_BASE:
        return {"error": "MASTODON_BASE_URL is not set"}
    try:
        resp = requests.request(
            method,
            f"{API_BASE}{path}",
            headers=_headers(),
            params=params,
            json=json,
            data=data,
            files=files,
            timeout=30,
        )
        try:
            payload = resp.json()
        except Exception:
            payload = resp.text
        if resp.ok:
            return payload
        return {"error": payload if isinstance(payload, str) else payload, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance() -> Any:
    return _request("GET", "/instance")


@mcp.tool()
def get_instance_activity() -> Any:
    return _request("GET", "/instance/activity")


@mcp.tool()
def get_instance_peers() -> Any:
    return _request("GET", "/instance/peers")


@mcp.tool()
def get_account_verify_credentials() -> Any:
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
def get_account_followers(account_id: str) -> Any:
    return _request("GET", f"/accounts/{account_id}/followers")


@mcp.tool()
def get_account_following(account_id: str) -> Any:
    return _request("GET", f"/accounts/{account_id}/following")


@mcp.tool()
def get_home_timeline(limit: int = 20) -> Any:
    return _request("GET", "/timelines/home", params={"limit": limit})


@mcp.tool()
def get_public_timeline(limit: int = 20) -> Any:
    return _request("GET", "/timelines/public", params={"limit": limit})


@mcp.tool()
def get_hashtag_timeline(tag: str, limit: int = 20) -> Any:
    return _request("GET", f"/timelines/tag/{tag}", params={"limit": limit})


@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20) -> Any:
    return _request("GET", f"/timelines/list/{list_id}", params={"limit": limit})


@mcp.tool()
def list_notifications(limit: int = 20) -> Any:
    return _request("GET", "/notifications", params={"limit": limit})


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
def search(query: str, type: str = "") -> Any:
    params = {"q": query}
    if type:
        params["type"] = type
    return _request("GET", "/search", params=params)


@mcp.tool()
def list_lists() -> Any:
    return _request("GET", "/lists")


@mcp.tool()
def create_list(title: str) -> Any:
    return _request("POST", "/lists", data={"title": title})


@mcp.tool()
def get_list(list_id: str) -> Any:
    return _request("GET", f"/lists/{list_id}")


@mcp.tool()
def update_list(list_id: str, title: str) -> Any:
    return _request("PUT", f"/lists/{list_id}", data={"title": title})


@mcp.tool()
def delete_list(list_id: str) -> Any:
    return _request("DELETE", f"/lists/{list_id}")


@mcp.tool()
def add_account_to_list(list_id: str, account_id: str) -> Any:
    return _request("POST", f"/lists/{list_id}/accounts", data={"account_ids[]": account_id})


@mcp.tool()
def remove_account_from_list(list_id: str, account_id: str) -> Any:
    return _request("DELETE", f"/lists/{list_id}/accounts", data={"account_ids[]": account_id})


@mcp.tool()
def list_bookmarks(limit: int = 20) -> Any:
    return _request("GET", "/bookmarks", params={"limit": limit})


@mcp.tool()
def bookmark_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def unbookmark_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unbookmark")


@mcp.tool()
def list_favourites(limit: int = 20) -> Any:
    return _request("GET", "/favourites", params={"limit": limit})


@mcp.tool()
def upload_media(file_path: str, description: str = "") -> Any:
    files = {"file": open(file_path, "rb")}
    data = {}
    if description:
        data["description"] = description
    try:
        return _request("POST", "/media", data=data, files=files)
    finally:
        files["file"].close()


@mcp.tool()
def create_status(status: str, visibility: str = "public") -> Any:
    return _request("POST", "/statuses", data={"status": status, "visibility": visibility})


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
def get_status_context(status_id: str) -> Any:
    return _request("GET", f"/statuses/{status_id}/context")


if __name__ == "__main__":
    mcp.run(transport="stdio")
