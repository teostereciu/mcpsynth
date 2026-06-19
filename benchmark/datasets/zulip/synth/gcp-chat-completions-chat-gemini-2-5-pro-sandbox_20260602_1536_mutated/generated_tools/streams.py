from .zulip_client import make_request
from typing import List, Optional, Union, Dict
import json

def subscribe_to_stream(
    subscriptions: List[Dict[str, str]],
    principals: Optional[List[Union[int, str]]] = None,
    authorization_errors_fatal: Optional[bool] = None,
    announce: Optional[bool] = None,
    invite_only: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    stream_post_policy: Optional[int] = None,
    message_retention_days: Optional[Union[int, str]] = None,
) -> dict:
    """Subscribe users to a stream.

    Args:
        subscriptions: A list of dictionaries containing the stream name and description.
        principals: A list of user IDs or emails to subscribe.
        authorization_errors_fatal: Whether to throw an error if a user is not authorized to subscribe.
        announce: Whether to announce the new stream to all users.
        invite_only: Whether the stream is invite-only.
        history_public_to_subscribers: Whether the stream's history is public to subscribers.
        stream_post_policy: The policy for who can post to the stream.
        message_retention_days: The number of days to retain messages in the stream.
    """
    data = {
        "subscriptions": json.dumps(subscriptions),
    }
    if principals:
        data["principals"] = json.dumps(principals)
    if authorization_errors_fatal is not None:
        data["authorization_errors_fatal"] = authorization_errors_fatal
    if announce is not None:
        data["announce"] = announce
    if invite_only is not None:
        data["invite_only"] = invite_only
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = history_public_to_subscribers
    if stream_post_policy is not None:
        data["stream_post_policy"] = stream_post_policy
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days

    return make_request("POST", "users/me/subscriptions", data=data)
