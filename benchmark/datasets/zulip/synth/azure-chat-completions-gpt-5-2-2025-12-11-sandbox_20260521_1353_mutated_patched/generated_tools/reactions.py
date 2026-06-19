from typing import Any, Dict, Optional

from .http_client import ZulipClient


def add_reaction(*, message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    """POST /messages/{message_id}/reactions

    Doc: docs/api_add-reaction.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return client.request("POST", f"/messages/{message_id}/reactions", data=data)


def remove_reaction(*, message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /messages/{message_id}/reactions

    Doc: docs/api_remove-reaction.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return client.request("DELETE", f"/messages/{message_id}/reactions", data=data)
