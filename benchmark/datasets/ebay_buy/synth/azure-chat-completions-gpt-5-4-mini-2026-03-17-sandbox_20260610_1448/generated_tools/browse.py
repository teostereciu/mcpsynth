import os
from typing import Any, Dict, List, Optional

import requests

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _base_url() -> str:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return BASE_URLS.get(env, BASE_URLS["SANDBOX"])


def _token() -> Optional[str]:
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    if not app_id or not cert_id:
        return None
    resp = requests.post(
        "https://api.ebay.com/identity/v1/oauth2/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        auth=(app_id, cert_id),
        data={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"},
        timeout=30,
    )
    if resp.status_code >= 400:
        return None
    return resp.json().get("access_token")


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {"Accept": "application/json"}
    token = _token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if extra:
        headers.update(extra)
    return headers


def _get(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    r = requests.get(_base_url() + path, headers=_headers(), params=params, timeout=30)
    if r.status_code >= 400:
        return {"error": f"HTTP {r.status_code}", "details": r.text}
    return r.json()


def _post(path: str, json: Dict[str, Any]) -> Dict[str, Any]:
    r = requests.post(_base_url() + path, headers=_headers({"Content-Type": "application/json"}), json=json, timeout=30)
    if r.status_code >= 400:
        return {"error": f"HTTP {r.status_code}", "details": r.text}
    return r.json()


def search_items(q: Optional[str] = None, category_ids: Optional[str] = None, limit: int = 10, offset: int = 0, **kwargs):
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if q is not None: params["q"] = q
    if category_ids is not None: params["category_ids"] = category_ids
    params.update(kwargs)
    return _get("/buy/browse/v1/item_summary/search", params)


def search_items_by_image(image_url: str, **kwargs):
    params = {"image_url": image_url, **kwargs}
    return _get("/buy/browse/v1/item_summary/search_by_image", params)


def get_item(item_id: str, fieldgroups: Optional[str] = None):
    params = {"fieldgroups": fieldgroups} if fieldgroups else None
    return _get(f"/buy/browse/v1/item/{item_id}", params)


def get_item_by_legacy_id(legacy_item_id: str, fieldgroups: Optional[str] = None):
    params = {"legacy_item_id": legacy_item_id}
    if fieldgroups: params["fieldgroups"] = fieldgroups
    return _get("/buy/browse/v1/item/get_item_by_legacy_id", params)


def get_items(item_ids: Optional[str] = None, item_group_ids: Optional[str] = None):
    params: Dict[str, Any] = {}
    if item_ids: params["item_ids"] = item_ids
    if item_group_ids: params["item_group_ids"] = item_group_ids
    return _get("/buy/browse/v1/item", params)


def get_items_by_item_group(item_group_id: str, fieldgroups: Optional[str] = None):
    params = {"item_group_id": item_group_id}
    if fieldgroups: params["fieldgroups"] = fieldgroups
    return _get("/buy/browse/v1/item/get_items_by_item_group", params)


def check_compatibility(item_id: str, compatibility_properties: Dict[str, Any]):
    return _post(f"/buy/browse/v1/item/{item_id}/check_compatibility", compatibility_properties)
