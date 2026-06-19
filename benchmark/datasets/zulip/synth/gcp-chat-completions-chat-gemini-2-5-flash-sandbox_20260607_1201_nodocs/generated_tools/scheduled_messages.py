from typing import List, Union

def schedule_message(client, type: str, to: Union[str, List[int]], content: str, schedule_send_at: int, topic: str = None):
    """Schedule a message to be sent at a future time.

    Args:
        client: The Zulip API client.
        type: The type of message, 'stream' or 'private'.
        to: For 'stream' type, the name of the stream (str). For 'private' type, a list of user IDs (List[int]).
        content: The content of the message.
        schedule_send_at: A Unix timestamp (integer) for when the message should be sent.
        topic: Required for 'stream' type messages. The topic of the message.
    """
    if type == "stream":
        if not topic:
            return {"error": "Topic is required for stream messages."}
        request_data = {
            "type": type,
            "to": to,
            "content": content,
            "topic": topic,
            "schedule_send_at": schedule_send_at
        }
    elif type == "private":
        if isinstance(to, list):
            to = [str(user_id) for user_id in to] # Convert user IDs to strings for the API
        else:
            return {"error": "'to' must be a list of user IDs for private messages."}
        request_data = {
            "type": type,
            "to": to,
            "content": content,
            "schedule_send_at": schedule_send_at
        }
    else:
        return {"error": "Invalid message type. Must be 'stream' or 'private'."}

    return client._request("POST", "/scheduled_messages", json=request_data)
