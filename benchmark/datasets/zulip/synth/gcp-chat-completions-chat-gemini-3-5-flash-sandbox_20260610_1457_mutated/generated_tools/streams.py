import json
from typing import Any, Dict, List, Optional, Union
from generated_tools.client import client

def subscribe_to_streams(
    subscriptions: List[Dict[str, str]],
    invite_only: Optional[bool] = False,
    history_public_to_subscribers: Optional[bool] = True,
    stream_post_policy: Optional[int] = 1,
    principals: Optional[List[Union[str, int]]] = None,
) -> Dict[str, Any]:
    """
    Subscribe to one or more streams, creating them if they don't exist.
    
    Args:
        subscriptions: A list of dictionaries, each containing a 'name' key (and optionally 'description').
            Example: [{"name": "new-stream", "description": "A new stream"}]
        invite_only: Whether the stream(s) should be private. Default is False.
        history_public_to_subscribers: Whether history is public to new subscribers. Default is True.
        stream_post_policy: Policy for who can post. 1 = Anyone, 2 = Admins only, 3 = Creators only, 4 = Admins and moderators.
        principals: A list of user emails or user IDs to subscribe. If not specified, subscribes the current user.
    """
    data = {
        "subscriptions": json.dumps(subscriptions),
        "invite_only": str(invite_only).lower(),
        "history_public_to_subscribers": str(history_public_to_subscribers).lower(),
        "stream_post_policy": stream_post_policy,
    }
    if principals is not None:
        data["principals"] = json.dumps(principals)

    return client.request("POST", "users/me/subscriptions", data=data)

def unsubscribe_from_streams(
    subscriptions: List[str],
    principals: Optional[List[Union[str, int]]] = None,
) -> Dict[str, Any]:
    """
    Unsubscribe from one or more streams.
    
    Args:
        subscriptions: A list of stream names (strings) to unsubscribe from.
        principals: A list of user emails or user IDs to unsubscribe. If not specified, unsubscribes the current user.
    """
    data = {
        "subscriptions": json.dumps(subscriptions),
    }
    if principals is not None:
        data["principals"] = json.dumps(principals)

    return client.request("DELETE", "users/me/subscriptions", data=data)

def get_subscriptions() -> Dict[str, Any]:
    """
    Get all streams that the current user is subscribed to.
    """
    return client.request("GET", "users/me/subscriptions")

def get_streams(
    include_public: Optional[bool] = True,
    include_web_public: Optional[bool] = False,
    include_subscribed: Optional[bool] = True,
    include_all_active: Optional[bool] = False,
    include_default: Optional[bool] = False,
) -> Dict[str, Any]:
    """
    Get all streams/channels in the Zulip organization.
    
    Args:
        include_public: Include public streams. Default is True.
        include_web_public: Include web-public streams. Default is False.
        include_subscribed: Include streams the user is subscribed to. Default is True.
        include_all_active: Include all active streams. Default is False.
        include_default: Include default streams. Default is False.
    """
    params = {
        "include_public": str(include_public).lower(),
        "include_web_public": str(include_web_public).lower(),
        "include_subscribed": str(include_subscribed).lower(),
        "include_all_active": str(include_all_active).lower(),
        "include_default": str(include_default).lower(),
    }
    return client.request("GET", "streams", params=params)

def get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    """
    Get details of a stream by its ID.
    
    Args:
        stream_id: The ID of the stream.
    """
    return client.request("GET", f"streams/{stream_id}")

def get_stream_id(stream: str) -> Dict[str, Any]:
    """
    Get the unique ID of a stream by its name.
    
    Args:
        stream: The name of the stream.
    """
    params = {"stream": stream}
    return client.request("GET", "get_stream_id", params=params)

def update_stream(
    stream_id: int,
    description: Optional[str] = None,
    new_name: Optional[str] = None,
    is_private: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    stream_post_policy: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Update settings of a stream.
    
    Args:
        stream_id: The ID of the stream to update.
        description: New description for the stream.
        new_name: New name for the stream.
        is_private: Change stream privacy (True for private, False for public).
        history_public_to_subscribers: Whether history is public to new subscribers.
        stream_post_policy: Policy for who can post.
    """
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if new_name is not None:
        data["new_name"] = new_name
    if is_private is not None:
        data["is_private"] = str(is_private).lower()
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = str(history_public_to_subscribers).lower()
    if stream_post_policy is not None:
        data["stream_post_policy"] = stream_post_policy

    return client.request("PATCH", f"streams/{stream_id}", data=data)

def archive_stream(stream_id: int) -> Dict[str, Any]:
    """
    Archive a stream (delete it).
    
    Args:
        stream_id: The ID of the stream to archive.
    """
    return client.request("DELETE", f"streams/{stream_id}")

def get_stream_subscribers(stream_id: int) -> Dict[str, Any]:
    """
    Get the list of users subscribed to a stream.
    
    Args:
        stream_id: The ID of the stream.
    """
    return client.request("GET", f"streams/{stream_id}/members")
