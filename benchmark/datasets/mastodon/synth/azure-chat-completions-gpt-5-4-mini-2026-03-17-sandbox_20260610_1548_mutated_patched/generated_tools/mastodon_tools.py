import os
import requests
from typing import Any, Dict

BASE_URL = os.getenv("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN", "")
API_BASE = f"{BASE_URL}/api/v1" if BASE_URL else ""


def _headers() -> Dict[str, str]:
    headers = {"Accept": "application/json"}
    if ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    return headers


def _request(method: str, path: str, *, params=None, data=None, files=None) -> Any:
    if not API_BASE:
        return {"error": "MASTODON_BASE_URL is not set"}
    try:
        resp = requests.request(method, f"{API_BASE}{path}", headers=_headers(), params=params, data=data, files=files, timeout=30)
        try:
            payload = resp.json()
        except Exception:
            payload = resp.text
        if resp.ok:
            return payload
        return {"error": payload.get("error") if isinstance(payload, dict) else str(payload), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_instance_info() -> Any:
    return _request("GET", "/instance")


def verify_credentials() -> Any:
    return _request("GET", "/accounts/verify_credentials")


def get_account(account_id: str) -> Any:
    return _request("GET", f"/accounts/{account_id}")


def follow_account(account_id: str) -> Any:
    return _request("POST", f"/accounts/{account_id}/follow")


def unfollow_account(account_id: str) -> Any:
    return _request("POST", f"/accounts/{account_id}/unfollow")


def get_followers(account_id: str) -> Any:
    return _request("GET", f"/accounts/{account_id}/followers")


def get_following(account_id: str) -> Any:
    return _request("GET", f"/accounts/{account_id}/following")


def search_accounts(q: str, limit: int = 40, offset: int = 0) -> Any:
    return _request("GET", "/accounts/search", params={"q": q, "limit": limit, "offset": offset})


def search(q: str, type: str = None, limit: int = 20, offset: int = 0, resolve: bool = False) -> Any:
    params = {"q": q, "limit": limit, "offset": offset, "resolve": resolve}
    if type:
        params["type"] = type
    return _request("GET", "/search", params=params)


def post_status(status: str = None, media_ids=None, reply_to_id=None, is_sensitive=False, content_warning=None, post_visibility=None, lang=None) -> Any:
    data = {}
    if status is not None: data["status"] = status
    if media_ids:
        for i, mid in enumerate(media_ids): data[f"media_ids[{i}]"] = mid
    if reply_to_id: data["in_reply_to_id"] = reply_to_id
    if is_sensitive is not None: data["sensitive"] = str(is_sensitive).lower()
    if content_warning is not None: data["spoiler_text"] = content_warning
    if post_visibility is not None: data["visibility"] = post_visibility
    if lang is not None: data["language"] = lang
    return _request("POST", "/statuses", data=data)


def get_status(status_id: str) -> Any:
    return _request("GET", f"/statuses/{status_id}")


def delete_status(status_id: str, delete_media: bool = False) -> Any:
    return _request("DELETE", f"/statuses/{status_id}", params={"delete_media": delete_media})


def get_status_context(status_id: str) -> Any:
    return _request("GET", f"/statuses/{status_id}/context")


def favourite_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unfavourite")


def boost_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/reblog")


def unboost_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unreblog")


def bookmark_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/bookmark")


def unbookmark_status(status_id: str) -> Any:
    return _request("POST", f"/statuses/{status_id}/unbookmark")


def list_bookmarks() -> Any:
    return _request("GET", "/bookmarks")


def list_favourites() -> Any:
    return _request("GET", "/favourites")


def upload_media(file_path: str, description: str = None) -> Any:
    files = {"file": open(file_path, "rb")}
    data = {}
    if description is not None: data["description"] = description
    try:
        return _request("POST", "/media", data=data, files=files)
    finally:
        files["file"].close()


def list_notifications(limit: int = 20) -> Any:
    return _request("GET", "/notifications", params={"limit": limit})


def get_notification(notification_id: str) -> Any:
    return _request("GET", f"/notifications/{notification_id}")


def dismiss_all_notifications() -> Any:
    return _request("POST", "/notifications/clear")


def dismiss_notification(notification_id: str) -> Any:
    return _request("POST", f"/notifications/{notification_id}/dismiss")


def list_lists() -> Any:
    return _request("GET", "/lists")


def get_list(list_id: str) -> Any:
    return _request("GET", f"/lists/{list_id}")


def create_list(title: str) -> Any:
    return _request("POST", "/lists", data={"title": title})


def update_list(list_id: str, title: str) -> Any:
    return _request("PUT", f"/lists/{list_id}", data={"title": title})


def delete_list(list_id: str) -> Any:
    return _request("DELETE", f"/lists/{list_id}")


def list_accounts_in_list(list_id: str) -> Any:
    return _request("GET", f"/lists/{list_id}/accounts")


def add_accounts_to_list(list_id: str, account_ids) -> Any:
    data = {}
    for i, aid in enumerate(account_ids): data[f"account_ids[{i}]"] = aid
    return _request("POST", f"/lists/{list_id}/accounts", data=data)


def remove_accounts_from_list(list_id: str, account_ids) -> Any:
    data = {}
    for i, aid in enumerate(account_ids): data[f"account_ids[{i}]"] = aid
    return _request("DELETE", f"/lists/{list_id}/accounts", data=data)
