import json
from typing import Any, Dict, List, Optional, Union
from generated_tools.client import client

def send_message(
    type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Send a stream or private message to Zulip.
    
    Args:
        type: The type of message to send. Must be "stream" or "private".
        to: For stream messages, either the name (string) or ID (integer) of the stream.
            For private messages, a list containing user emails (strings) or user IDs (integers).
            If sending to a single user, a single email or ID can be passed.
        content: The content of the message in Markdown format.
        topic: The topic for the message. Required if type is "stream".
    """
    if isinstance(to, list):
        to_param = json.dumps(to)
    else:
        to_param = str(to)

    data = {
        "type": type,
        "to": to_param,
        "content": content,
    }
    if topic is not None:
        data["topic"] = topic

    return client.request("POST", "messages", data=data)

def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = "one",
    send_notification_to_old_thread: Optional[bool] = True,
    send_notification_to_new_thread: Optional[bool] = True,
) -> Dict[str, Any]:
    """
    Edit the content or topic of a message.
    
    Args:
        message_id: The ID of the message to edit.
        content: The new content of the message.
        topic: The new topic for the message (only applicable to stream messages).
        propagate_mode: Which messages to update if topic is changed.
            Must be "one" (only this message), "later" (this and all subsequent messages in the topic),
            or "all" (all messages in the topic). Default is "one".
        send_notification_to_old_thread: Whether to send a notification to the old thread. Default is True.
        send_notification_to_new_thread: Whether to send a notification to the new thread. Default is True.
    """
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
        data["propagate_mode"] = propagate_mode
        data["send_notification_to_old_thread"] = str(send_notification_to_old_thread).lower()
        data["send_notification_to_new_thread"] = str(send_notification_to_new_thread).lower()

    return client.request("PATCH", f"messages/{message_id}", data=data)

def delete_message(message_id: int) -> Dict[str, Any]:
    """
    Delete a message.
    
    Args:
        message_id: The ID of the message to delete.
    """
    return client.request("DELETE", f"messages/{message_id}")

def get_messages(
    anchor: Union[str, int],
    num_before: int,
    num_after: int,
    narrow: Optional[List[Dict[str, Any]]] = None,
    client_gravatar: Optional[bool] = False,
    apply_markdown: Optional[bool] = True,
) -> Dict[str, Any]:
    """
    Fetch messages from Zulip based on search/narrow criteria.
    
    Args:
        anchor: Integer message ID or string ("newest", "oldest", "first_unread").
        num_before: Number of messages before the anchor to retrieve.
        num_after: Number of messages after the anchor to retrieve.
        narrow: A list of search/narrow filters, e.g., [{"operator": "stream", "operand": "Denmark"}].
        client_gravatar: Whether to return gravatar URLs. Default is False.
        apply_markdown: Whether to return content rendered in HTML. Default is True.
    """
    params: Dict[str, Any] = {
        "anchor": str(anchor),
        "num_before": num_before,
        "num_after": num_after,
        "client_gravatar": str(client_gravatar).lower(),
        "apply_markdown": str(apply_markdown).lower(),
    }
    if narrow is not None:
        params["narrow"] = json.dumps(narrow)

    return client.request("GET", "messages", params=params)

def get_message(message_id: int) -> Dict[str, Any]:
    """
    Fetch a single message by its ID.
    
    Args:
        message_id: The ID of the message to retrieve.
    """
    return client.request("GET", f"messages/{message_id}")

def get_message_history(message_id: int) -> Dict[str, Any]:
    """
    Fetch the edit history of a message.
    
    Args:
        message_id: The ID of the message to retrieve history for.
    """
    return client.request("GET", f"messages/{message_id}/history")

def update_message_flags(
    messages: List[int],
    op: str,
    flag: str,
) -> Dict[str, Any]:
    """
    Add or remove a flag (like 'read' or 'starred') from a list of messages.
    
    Args:
        messages: A list of message IDs to update.
        op: The operation to perform. Must be "add" or "remove".
        flag: The flag to add or remove (e.g., "read", "starred", "collapsed").
    """
    data = {
        "messages": json.dumps(messages),
        "op": op,
        "flag": flag,
    }
    return client.request("POST", "messages/flags", data=data)
