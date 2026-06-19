from __future__ import annotations

from typing import Any, Dict, Optional

from .http import safe_call


def create_activity(activity: Dict[str, Any], shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """POST /promotion/202309/activities"""
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("POST", "/promotion/202309/activities", params=params, body=activity)


def search_activities(
    status: Optional[str] = None,
    activity_type: Optional[str] = None,
    page_size: int = 20,
    page_token: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /promotion/202309/activities/search"""
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    body: Dict[str, Any] = {
        "status": status,
        "activity_type": activity_type,
        "page_size": page_size,
        "page_token": page_token,
    }
    return safe_call("POST", "/promotion/202309/activities/search", params=params, body=body)


def update_activity_product(activity_id: str, payload: Dict[str, Any], shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """POST /promotion/202309/activities/{activity_id}/products"""
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    return safe_call("POST", f"/promotion/202309/activities/{activity_id}/products", params=params, body=payload)
