from typing import Any, Dict, Optional
from generated_tools.client import client

def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """
    Get all topics in a stream.
    
    Args:
        stream_id: The ID of the stream.
    """
    return client.request("GET", f"users/me/{stream_id}/topics")

def update_user_topic(
    stream_id: int,
    topic: str,
    visibility_policy: int,
) -> Dict[str, Any]:
    """
    Update visibility policy (mute, unmute, follow) for a topic.
    
    Args:
        stream_id: The ID of the stream containing the topic.
        topic: The name of the topic.
        visibility_policy: The visibility policy:
            0 = None (default)
            1 = Muted
            2 = Unmuted
            3 = Followed
    """
    data = {
        "stream_id": stream_id,
        "topic": topic,
        "visibility_policy": visibility_policy,
    }
    return client.request("POST", "users/me/user_topics", data=data)

def delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """
    Delete all messages in a topic (effectively deleting the topic).
    
    Args:
        stream_id: The ID of the stream containing the topic.
        topic_name: The name of the topic to delete.
    """
    data = {
        "topic_name": topic_name,
    }
    return client.request("POST", f"streams/{stream_id}/delete_topic", data=data)
