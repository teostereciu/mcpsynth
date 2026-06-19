from typing import List, Union

def send_message(client, type: str, to: Union[str, List[int]], content: str, topic: str = None):
    """Send a message to a stream or a private message to users.

    Args:
        client: The Zulip API client.
        type: The type of message, 'stream' or 'private'.
        to: For 'stream' type, the name of the stream (str). For 'private' type, a list of user IDs (List[int]).
        content: The content of the message.
        topic: Required for 'stream' type messages. The topic of the message.
    """
    if type == "stream":
        if not topic:
            return {"error": "Topic is required for stream messages."}
        request_data = {
            "type": type,
            "to": to,
            "content": content,
            "topic": topic
        }
    elif type == "private":
        if isinstance(to, list):
            to = [str(user_id) for user_id in to] # Convert user IDs to strings for the API
        else:
            return {"error": "'to' must be a list of user IDs for private messages."}
        request_data = {
            "type": type,
            "to": to,
            "content": content
        }
    else:
        return {"error": "Invalid message type. Must be 'stream' or 'private'."}

    return client._request("POST", "/messages", json=request_data)

def get_message_history(client, anchor: Union[int, str] = "newest", num_before: int = 100, num_after: int = 0, narrow: str = "[]", client_gravatar: bool = False, apply_markdown: bool = True, use_first_unread_anchor: bool = False):
    """Fetch message history.

    Args:
        client: The Zulip API client.
        anchor: The ID of the message to anchor the results around. Can be an integer message ID, or "newest", "oldest", or "first_unread".
        num_before: The number of messages to retrieve before the anchor.
        num_after: The number of messages to retrieve after the anchor.
        narrow: A JSON-encoded array of narrow terms.
        client_gravatar: Whether to include the client's gravatar.
        apply_markdown: Whether to apply markdown to the message content.
        use_first_unread_anchor: Whether to use the first unread message as the anchor.
    """
    params = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "narrow": narrow,
        "client_gravatar": "true" if client_gravatar else "false",
        "apply_markdown": "true" if apply_markdown else "false",
        "use_first_unread_anchor": "true" if use_first_unread_anchor else "false",
    }
    return client._request("GET", "/messages", params=params)

def edit_message(client, message_id: int, topic: str = None, content: str = None, propagate_mode: str = "change_one", send_notification_to_old_thread: bool = True, send_notification_to_new_thread: bool = True):
    """Edit a previously sent message's content or topic.

    Args:
        client: The Zulip API client.
        message_id: The ID of the message to edit.
        topic: The new topic for the message (if moving/renaming topic).
        content: The new content for the message.
        propagate_mode: How to propagate the topic change. Can be 'change_one', 'change_all', or 'change_later'.
        send_notification_to_old_thread: Whether to send a notification to the old thread when moving a message.
        send_notification_to_new_thread: Whether to send a notification to the new thread when moving a message.
    """
    request_data = {}
    if topic:
        request_data["topic"] = topic
    if content:
        request_data["content"] = content
    if topic and propagate_mode:
        request_data["propagate_mode"] = propagate_mode
        request_data["send_notification_to_old_thread"] = send_notification_to_old_thread
        request_data["send_notification_to_new_thread"] = send_notification_to_new_thread

    if not request_data:
        return {"error": "Either 'topic' or 'content' must be provided to edit a message."}

    return client._request("PATCH", f"/messages/{message_id}", json=request_data)

def delete_message(client, message_id: int):
    """Delete a message.

    Args:
        client: The Zulip API client.
        message_id: The ID of the message to delete.
    """
    return client._request("DELETE", f"/messages/{message_id}")

def update_message_flags(client, messages: List[int], op: str, flag: str):
    """Add or remove flags (e.g., read, starred) for messages.

    Args:
        client: The Zulip API client.
        messages: A list of message IDs to update flags for.
        op: The operation to perform, 'add' or 'remove'.
        flag: The flag to update (e.g., 'read', 'starred').
    """
    request_data = {
        "messages": messages,
        "op": op,
        "flag": flag
    }
    return client._request("POST", "/messages/flags", json=request_data)




