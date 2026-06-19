"""Customer Service (IM) domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import TikTokRequestOptions, tiktok_request


def get_conversations(
    *,
    page_size: int = 10,
    page_token: Optional[str] = None,
    locale: Optional[str] = None,
    need_session_id: bool = False,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get conversations.

    API: GET /customer_service/202309/conversations
    """

    params: Dict[str, Any] = {
        "page_size": page_size,
        "need_session_id": str(need_session_id).lower(),
    }
    if page_token is not None:
        params["page_token"] = page_token
    if locale is not None:
        params["locale"] = locale

    return tiktok_request(
        "GET",
        "/customer_service/202309/conversations",
        params=params,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def send_message(
    *,
    conversation_id: str,
    message: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Send a text message in a conversation.

    API: POST /customer_service/202309/conversations/{conversation_id}/messages
    """

    body = {
        "type": "TEXT",
        "content": {"content": message},
    }

    return tiktok_request(
        "POST",
        f"/customer_service/202309/conversations/{conversation_id}/messages",
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )
