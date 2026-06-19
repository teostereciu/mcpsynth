"""Twilio Conversations API tools.

Uses shortened URLs (default Conversation Service) unless otherwise specified.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import conversations_delete, conversations_get, conversations_post


def conversations_create(
    *,
    friendly_name: Optional[str] = None,
    unique_name: Optional[str] = None,
    attributes: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a Conversation (CH...)."""
    data: Dict[str, Any] = {}
    if friendly_name is not None:
        data["FriendlyName"] = friendly_name
    if unique_name is not None:
        data["UniqueName"] = unique_name
    if attributes is not None:
        data["Attributes"] = attributes
    return conversations_post("/Conversations", data=data)


def conversations_fetch(*, conversation_sid: str) -> Dict[str, Any]:
    """Fetch a Conversation by SID or unique_name."""
    return conversations_get(f"/Conversations/{conversation_sid}")


def conversations_list(*, page_size: int = 50, state: Optional[str] = None) -> Dict[str, Any]:
    """List conversations."""
    params: Dict[str, Any] = {"PageSize": page_size}
    if state is not None:
        params["State"] = state
    return conversations_get("/Conversations", params=params)


def conversations_update(
    *,
    conversation_sid: str,
    friendly_name: Optional[str] = None,
    attributes: Optional[str] = None,
    state: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a Conversation."""
    data: Dict[str, Any] = {}
    if friendly_name is not None:
        data["FriendlyName"] = friendly_name
    if attributes is not None:
        data["Attributes"] = attributes
    if state is not None:
        data["State"] = state
    return conversations_post(f"/Conversations/{conversation_sid}", data=data)


def conversations_delete_tool(*, conversation_sid: str) -> Dict[str, Any]:
    """Delete a Conversation."""
    return conversations_delete(f"/Conversations/{conversation_sid}")


def conversation_messages_create(
    *,
    conversation_sid: str,
    author: Optional[str] = None,
    body: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a message in a conversation (IM...)."""
    data: Dict[str, Any] = {}
    if author is not None:
        data["Author"] = author
    if body is not None:
        data["Body"] = body
    return conversations_post(f"/Conversations/{conversation_sid}/Messages", data=data)


def conversation_messages_fetch(*, conversation_sid: str, message_sid: str) -> Dict[str, Any]:
    """Fetch a conversation message."""
    return conversations_get(f"/Conversations/{conversation_sid}/Messages/{message_sid}")


def conversation_messages_list(*, conversation_sid: str, page_size: int = 50) -> Dict[str, Any]:
    """List messages in a conversation."""
    return conversations_get(
        f"/Conversations/{conversation_sid}/Messages",
        params={"PageSize": page_size},
    )


def conversation_participants_create(
    *,
    conversation_sid: str,
    identity: Optional[str] = None,
    messaging_binding_address: Optional[str] = None,
    messaging_binding_proxy_address: Optional[str] = None,
) -> Dict[str, Any]:
    """Add a participant.

    For identity-based participants, pass identity.
    For SMS participants, pass messaging_binding_address (+E.164) and proxy address.
    """
    data: Dict[str, Any] = {}
    if identity is not None:
        data["Identity"] = identity
    if messaging_binding_address is not None:
        data["MessagingBinding.Address"] = messaging_binding_address
    if messaging_binding_proxy_address is not None:
        data["MessagingBinding.ProxyAddress"] = messaging_binding_proxy_address
    return conversations_post(f"/Conversations/{conversation_sid}/Participants", data=data)


def conversation_participants_fetch(
    *,
    conversation_sid: str,
    participant_sid: str,
) -> Dict[str, Any]:
    """Fetch a participant (MB...)."""
    return conversations_get(f"/Conversations/{conversation_sid}/Participants/{participant_sid}")


def conversation_participants_list(*, conversation_sid: str, page_size: int = 50) -> Dict[str, Any]:
    """List participants."""
    return conversations_get(
        f"/Conversations/{conversation_sid}/Participants",
        params={"PageSize": page_size},
    )


def conversation_participants_delete(
    *,
    conversation_sid: str,
    participant_sid: str,
) -> Dict[str, Any]:
    """Remove a participant."""
    return conversations_delete(f"/Conversations/{conversation_sid}/Participants/{participant_sid}")
