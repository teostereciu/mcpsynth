import os
from typing import Any, Dict, List, Optional

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mastodon")

BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social").rstrip("/")
API_BASE = f"{BASE_URL}/api/v1"
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")


def _headers() -> Dict[str, str]:
    headers = {"Accept": "application/json"}
    if ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    return headers


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Any:
    url = f"{API_BASE}{path}"
    with httpx.Client(timeout=60.0, headers=_headers()) as client:
        resp = client.request(method, url, params=params, data=data)
        resp.raise_for_status()
        if resp.status_code == 204:
            return {}
        return resp.json()


@mcp.tool()
def get_instance() -> Any:
    return _request("GET", "/instance")


@mcp.tool()
def verify_credentials() -> Any:
    return _request("GET", "/accounts/verify_credentials")


@mcp.tool()
def get_status(status_id: str) -> Any:
    return _request("GET", f"/statuses/{status_id}")


@mcp.tool()
def create_status(status: str, media_ids: Optional[List[str]] = None, in_reply_to_id: Optional[str] = None, sensitive: Optional[bool] = None, spoiler_text: Optional[str] = None, visibility: Optional[str] = None, language: Optional[str] = None, scheduled_at: Optional[str] = None) -> Any:
    data: Dict[str, Any] = {"status": status}
    if media_ids is not None:
        for i, mid in enumerate(media_ids):
            data[f"media_ids[{i}]"] = mid
    for k, v in {"in_reply_to_id": in_reply_to_id, "sensitive": sensitive, "spoiler_text": spoiler_text, "visibility": visibility, "language": language, "scheduled_at": scheduled_at}.items():
        if v is not None:
            data[k] = str(v).lower() if isinstance(v, bool) else v
    return _request("POST", "/statuses", data=data)


@mcp.tool()
def delete_status(status_id: str, delete_media: Optional[bool] = None) -> Any:
    params = {"delete_media": str(delete_media).lower()} if delete_media is not None else None
    return _request("DELETE", f"/statuses/{status_id}", params=params)


@mcp.tool()
def favourite_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/favourite")


@mcp.tool()
def unfavourite_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unfavourite")


@mcp.tool()
def boost_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/reblog")


@mcp.tool()
def unboost_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unreblog")


@mcp.tool()
def bookmark_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def unbookmark_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unbookmark")


@mcp.tool()
def get_status_context(status_id: str) -> Any:
    return _request("GET", f"/statuses/{status_id}/context")


@mcp.tool()
def get_home_timeline(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    return _request("GET", "/timelines/home", params=params)


@mcp.tool()
def get_public_timeline(local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"local": local, "remote": remote, "only_media": only_media, "limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    return _request("GET", "/timelines/public", params=params)


@mcp.tool()
def search(q: str, type: Optional[str] = None, resolve: Optional[bool] = None, following: Optional[bool] = None, account_id: Optional[str] = None, exclude_unreviewed: Optional[bool] = None, limit: Optional[int] = None, offset: Optional[int] = None, max_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"q": q, "type": type, "resolve": resolve, "following": following, "account_id": account_id, "exclude_unreviewed": exclude_unreviewed, "limit": limit, "offset": offset, "max_id": max_id, "min_id": min_id}.items() if v is not None}
    return _request("GET", "/search", params=params)


@mcp.tool()
def list_lists() -> Any:
    return _request("GET", "/lists")


@mcp.tool()
def create_list(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    data = {k: v for k, v in {"title": title, "replies_policy": replies_policy, "exclusive": exclusive}.items() if v is not None}
    return _request("POST", "/lists", data=data)


@mcp.tool()
def get_bookmarks(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    return _request("GET", "/bookmarks", params=params)


@mcp.tool()
def get_favourites(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    return _request("GET", "/favourites", params=params)


@mcp.tool()
def upload_media(description: Optional[str] = None, focus: Optional[str] = None) -> Any:
    data = {k: v for k, v in {"description": description, "focus": focus}.items() if v is not None}
    return _request("POST", "/media", data=data)


if __name__ == "__main__":
    mcp.run()
