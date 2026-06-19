from typing import Any, Dict, Optional

from .client import ZulipClient


def add_reaction(
    client: ZulipClient,
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    return client.request("POST", f"/messages/{message_id}/reactions", params)


def remove_reaction(
    client: ZulipClient,
    message_id: int,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if emoji_name is not None:
        params["emoji_name"] = emoji_name
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    return client.request("DELETE", f"/messages/{message_id}/reactions", params)
