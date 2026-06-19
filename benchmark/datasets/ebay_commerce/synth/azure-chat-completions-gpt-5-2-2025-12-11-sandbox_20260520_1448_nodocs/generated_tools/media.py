from typing import Any, Dict, Optional

from .ebay_http import EbayClient, compact, json_loads_maybe


USER_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.media.readwrite"


def create_upload_session(
    *,
    file_name: str,
    file_size: int,
    marketplace_id: Optional[str] = None,
    upload_type: str = "IMAGE",
) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/upload_session"""
    c = EbayClient()
    headers = c.build_headers(marketplace_id=marketplace_id)
    body = {
        "fileName": file_name,
        "fileSize": file_size,
        "uploadType": upload_type,
    }
    return c.request(
        "POST",
        "/commerce/media/v1_beta/upload_session",
        base="media",
        json_body=body,
        headers=headers,
        user_scope=USER_SCOPE,
    )


def get_upload_session(upload_session_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/upload_session/{uploadSessionId}"""
    c = EbayClient()
    return c.request(
        "GET",
        f"/commerce/media/v1_beta/upload_session/{upload_session_id}",
        base="media",
        user_scope=USER_SCOPE,
    )


def upload_file_part(
    upload_session_id: str,
    *,
    content_range: str,
    data: str,
    content_type: str = "application/octet-stream",
) -> Dict[str, Any]:
    """PUT /commerce/media/v1_beta/upload_session/{uploadSessionId}"""
    c = EbayClient()
    headers = {"Content-Range": content_range, "Content-Type": content_type}
    return c.request(
        "PUT",
        f"/commerce/media/v1_beta/upload_session/{upload_session_id}",
        base="media",
        data=data.encode("utf-8") if isinstance(data, str) else data,
        headers=headers,
        user_scope=USER_SCOPE,
    )


def complete_upload_session(upload_session_id: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/upload_session/{uploadSessionId}/complete"""
    c = EbayClient()
    return c.request(
        "POST",
        f"/commerce/media/v1_beta/upload_session/{upload_session_id}/complete",
        base="media",
        user_scope=USER_SCOPE,
    )


def get_asset(asset_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/asset/{assetId}"""
    c = EbayClient()
    return c.request(
        "GET",
        f"/commerce/media/v1_beta/asset/{asset_id}",
        base="media",
        user_scope=USER_SCOPE,
    )


def search_assets(
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/asset"""
    c = EbayClient()
    params = compact({"limit": limit, "offset": offset, "sort": sort})
    return c.request(
        "GET",
        "/commerce/media/v1_beta/asset",
        base="media",
        params=params,
        user_scope=USER_SCOPE,
    )


def delete_asset(asset_id: str) -> Dict[str, Any]:
    """DELETE /commerce/media/v1_beta/asset/{assetId}"""
    c = EbayClient()
    return c.request(
        "DELETE",
        f"/commerce/media/v1_beta/asset/{asset_id}",
        base="media",
        user_scope=USER_SCOPE,
    )
