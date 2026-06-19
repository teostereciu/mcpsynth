from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def cs_get_conversations(page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get conversations.

    API: GET /customer_service/202309/conversations
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/customer_service/202309/conversations", params=params)


@mcp.tool()
def cs_get_conversation_messages(conversation_id: str, page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get messages in a conversation.

    API: GET /customer_service/202309/conversations/{conversation_id}/messages
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", f"/customer_service/202309/conversations/{conversation_id}/messages", params=params)


@mcp.tool()
def cs_send_message(conversation_id: str, message: str) -> Dict[str, Any]:
    """Send a text message in a conversation.

    API: POST /customer_service/202309/messages/send
    """

    body = {"conversation_id": conversation_id, "content": {"text": message}, "message_type": "TEXT"}
    return tiktok_request("POST", "/customer_service/202309/messages/send", body=body)
