from typing import Any, Dict, Optional
from generated_tools.client import client

def add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add an emoji reaction to a message.
    
    Args:
        message_id: The ID of the message to react to.
        emoji_name: The name of the emoji (e.g., "thumbs_up", "smile").
        emoji_code: The code of the emoji (optional, e.g., "1f44d").
        reaction_type: The type of emoji (optional, e.g., "unicode_emoji", "realm_emoji", "zulip_extra_emoji").
    """
    data = {
        "emoji_name": emoji_name,
    }
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type

    return client.request("POST", f"messages/{message_id}/reactions", data=data)

def remove_reaction(
    message_id: int,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Remove an emoji reaction from a message.
    
    Args:
        message_id: The ID of the message to remove the reaction from.
        emoji_name: The name of the emoji (optional).
        emoji_code: The code of the emoji (optional).
        reaction_type: The type of emoji (optional).
    """
    data: Dict[str, Any] = {}
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type

    return client.request("DELETE", f"messages/{message_id}/reactions", data=data)
