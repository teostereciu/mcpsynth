def get_topics_in_stream(client, stream_id: int):
    """Get all topics in a given stream.

    Args:
        client: The Zulip API client.
        stream_id: The ID of the stream.
    """
    return client._request("GET", f"/users/me/{stream_id}/topics")

def rename_topic(client, message_id: int, new_topic: str):
    """Rename a topic by editing a message within that topic.

    Args:
        client: The Zulip API client.
        message_id: The ID of a message within the topic to be renamed.
        new_topic: The new name for the topic.
    """
    request_data = {
        "topic": new_topic,
        "propagate_mode": "change_all"
    }
    return client._request("PATCH", f"/messages/{message_id}", json=request_data)

