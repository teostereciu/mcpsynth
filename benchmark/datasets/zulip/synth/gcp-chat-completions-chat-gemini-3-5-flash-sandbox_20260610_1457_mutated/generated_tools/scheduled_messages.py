import json
from typing import Any, Dict, List, Optional, Union
from generated_tools.client import client

def create_scheduled_message(
    type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    deliver_at: int,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Schedule a message to be sent at a future time.
    
    Args:
        type: The type of message. Must be "stream" or "private".
        to: For stream messages, either the name (string) or ID (integer) of the stream.
            For private messages, a list containing user emails (strings) or user IDs (integers).
        content: The content of the message in Markdown format.
        deliver_at: The UNIX epoch timestamp (in seconds) when the message should be delivered.
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
        "deliver_at": deliver_at,
    }
    if topic is not None:
        data["topic"] = topic

    return client.request("POST", "scheduled_messages", data=data)

def get_scheduled_messages() -> Dict[str, Any]:
    """
    Get all scheduled messages for the current user.
    """
    return client.request("GET", "scheduled_messages")

def update_scheduled_message(
    scheduled_message_id: int,
    type: Optional[str] = None,
    to: Optional[Union[str, int, List[Union[str, int]]]] = None,
    content: Optional[str] = None,
    deliver_at: Optional[int] = None,
    topic: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a scheduled message.
    
    Args:
        scheduled_message_id: The ID of the scheduled message to update.
        type: The type of message. Must be "stream" or "private".
        to: For stream messages, either the name (string) or ID (integer) of the stream.
            For private messages, a list containing user emails (strings) or user IDs (integers).
        content: The content of the message in Markdown format.
        deliver_at: The UNIX epoch timestamp (in seconds) when the message should be delivered.
        topic: The topic for the message.
    """
    data: Dict[str, Any] = {}
    if type is not None:
        data["type"] = type
    if to is not None:
        if isinstance(to, list):
            data["to"] = json.dumps(to)
        else:
            data["to"] = str(to)
    if content is not None:
        data["content"] = content
    if deliver_at is not None:
        data["deliver_at"] = deliver_at
    if topic is not None:
        data["topic"] = topic

    return client.request("PATCH", f"scheduled_messages/{scheduled_message_id}", data=data)

def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    """
    Delete a scheduled message.
    
    Args:
        scheduled_message_id: The ID of the scheduled message to delete.
    """
    return client.request("DELETE", f"scheduled_messages/{scheduled_message_id}")
