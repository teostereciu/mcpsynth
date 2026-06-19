"""Customer service domain tools (conversations, messages)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .client import TikTokShopClient


def send_message(
    *,
    conversation_id: str,
    type: str,
    content: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /customer_service/202309/conversations/{conversation_id}/messages

    Note: `content` must be a JSON-serialized string per TikTok docs.
    """

    client = TikTokShopClient.from_env()
    body = {"type": type, "content": content}
    return client.request(
        "POST",
        f"/customer_service/202309/conversations/{conversation_id}/messages",
        params={"shop_cipher": shop_cipher},
        body=body,
        use_shop_cipher=True,
    )


def get_conversations(
    *,
    page_size: int = 10,
    page_token: Optional[str] = None,
    locale: Optional[str] = None,
    need_session_id: Optional[bool] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /customer_service/202309/conversations"""

    client = TikTokShopClient.from_env()
    params: Dict[str, Any] = {
        "page_size": page_size,
        "page_token": page_token,
        "locale": locale,
        "need_session_id": need_session_id,
        "shop_cipher": shop_cipher,
    }
    return client.request(
        "GET",
        "/customer_service/202309/conversations",
        params=params,
        use_shop_cipher=True,
    )
