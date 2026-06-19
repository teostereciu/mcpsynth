from typing import List, Optional

def create_stream(client, stream_name: str, description: str = "", invite_only: bool = False, announce: bool = False, history_public_to_subscribers: bool = True, stream_post_policy: int = 1, message_retention_days: Optional[int] = None):
    """Create a new stream.

    Args:
        client: The Zulip API client.
        stream_name: The name of the stream to create.
        description: The description of the stream.
        invite_only: Whether the stream is invite-only.
        announce: Whether to announce the new stream to the organization.
        history_public_to_subscribers: Whether the stream's message history is public to new subscribers.
        stream_post_policy: Policy for who can post in the stream (1: everyone, 2: administrators, 3: moderators, 4: members).
        message_retention_days: Number of days to retain messages. None for indefinite.
    """
    request_data = {
        "stream": stream_name,
        "description": description,
        "invite_only": invite_only,
        "announce": announce,
        "history_public_to_subscribers": history_public_to_subscribers,
        "stream_post_policy": stream_post_policy,
    }
    if message_retention_days is not None:
        request_data["message_retention_days"] = message_retention_days

    return client._request("POST", "/streams", json=request_data)

def subscribe_to_stream(client, streams: List[str], principals: Optional[List[int]] = None, authorization_errors_fatal: bool = True):
    """Subscribe users to a list of streams.

    Args:
        client: The Zulip API client.
        streams: A list of stream names to subscribe to.
        principals: A list of user IDs to subscribe to the streams. If None, the authenticated user is subscribed.
        authorization_errors_fatal: Whether to treat authorization errors as fatal.
    """
    subscriptions = [{"name": stream_name} for stream_name in streams]
    request_data = {
        "subscriptions": subscriptions,
        "authorization_errors_fatal": authorization_errors_fatal
    }
    if principals:
        request_data["principals"] = principals

    return client._request("POST", "/users/me/subscriptions", json=request_data)

def archive_stream(client, stream_id: int):
    """Archive a stream.

    Args:
        client: The Zulip API client.
        stream_id: The ID of the stream to archive.
    """
    return client._request("DELETE", f"/streams/{stream_id}")

def update_stream_settings(client, stream_id: int, new_name: str = None, description: str = None, is_private: bool = None, is_announcing_to_principals: bool = None, history_public_to_subscribers: bool = None, stream_post_policy: int = None, message_retention_days: Optional[int] = None):
    """Update the settings of a stream.

    Args:
        client: The Zulip API client.
        stream_id: The ID of the stream to update.
        new_name: The new name for the stream.
        description: The new description for the stream.
        is_private: Whether the stream should be private.
        is_announcing_to_principals: Whether to announce the stream to new principals.
        history_public_to_subscribers: Whether the stream's message history is public to new subscribers.
        stream_post_policy: Policy for who can post in the stream.
        message_retention_days: Number of days to retain messages. None for indefinite.
    """
    request_data = {}
    if new_name is not None:
        request_data["new_name"] = new_name
    if description is not None:
        request_data["description"] = description
    if is_private is not None:
        request_data["is_private"] = is_private
    if is_announcing_to_principals is not None:
        request_data["is_announcing_to_principals"] = is_announcing_to_principals
    if history_public_to_subscribers is not None:
        request_data["history_public_to_subscribers"] = history_public_to_subscribers
    if stream_post_policy is not None:
        request_data["stream_post_policy"] = stream_post_policy
    if message_retention_days is not None:
        request_data["message_retention_days"] = message_retention_days

    if not request_data:
        return {"error": "No settings provided to update the stream."}

    return client._request("PATCH", f"/streams/{stream_id}", json=request_data)



