from __future__ import annotations

import json
from typing import Any, Dict, Optional

from .http import safe_call


def get_conversations(
    page_size: int = 10,
    page_token: Optional[str] = None,
    locale: Optional[str] = None,
    need_session_id: bool = False,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /customer_service/202309/conversations"""
    params: Dict[str, Any] = {
        "page_size": page_size,
        "page_token": page_token,
        "locale": locale,
        "need_session_id": need_session_id,
    }
    if shop_cipher:
        params["shop_cipher"] = shop_cipher
    return safe_call("GET", "/customer_service/202309/conversations", params=params)


def send_message(
    conversation_id: str,
    message: str,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /customer_service/202309/conversations/{conversation_id}/messages

    Sends a TEXT message.
    """
    params = {"shop_cipher": shop_cipher} if shop_cipher else None
    body = {"type": "TEXT", "content": json.dumps({"content": message}, ensure_ascii=False)}
    return safe_call("POST", f"/customer_service/202309/conversations/{conversation_id}/messages", params=params, body=body)
