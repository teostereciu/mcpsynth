def add_reaction(client, message_id: int, emoji_name: str):
    """Add a reaction to a message.

    Args:
        client: The Zulip API client.
        message_id: The ID of the message to react to.
        emoji_name: The name of the emoji to add (e.g., 'thumbs_up').
    """
    request_data = {
        "emoji_name": emoji_name
    }
    return client._request("POST", f"/messages/{message_id}/reactions", json=request_data)

def remove_reaction(client, message_id: int, emoji_name: str):
    """Remove a reaction from a message.

    Args:
        client: The Zulip API client.
        message_id: The ID of the message to remove the reaction from.
        emoji_name: The name of the emoji to remove.
    """
    params = {
        "emoji_name": emoji_name
    }
    return client._request("DELETE", f"/messages/{message_id}/reactions", params=params)

