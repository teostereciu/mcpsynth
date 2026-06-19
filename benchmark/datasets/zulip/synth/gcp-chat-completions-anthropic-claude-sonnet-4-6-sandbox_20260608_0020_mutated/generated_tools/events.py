"""Zulip Real-time Events API tools."""
import json
from typing import Optional, List
from .client import zulip_request


def register_event_queue(
    event_types: Optional[List[str]] = None,
    narrow: Optional[List[List[str]]] = None,
    all_public_streams: bool = False,
    apply_markdown: bool = False,
) -> dict:
    """Register an event queue to receive real-time events.

    Args:
        event_types: List of event types to subscribe to (e.g. ['message', 'subscription']).
                     If not specified, all events are received.
        narrow: Narrow filter for message events e.g. [['channel', 'Denmark']].
        all_public_streams: Whether to receive events from all public channels.
        apply_markdown: Whether to receive message content as rendered HTML.

    Returns:
        Dict with 'queue_id' and 'last_event_id' for use with get_events.
    """
    try:
        data: dict = {
            "all_public_streams": json.dumps(all_public_streams),
            "apply_markdown": json.dumps(apply_markdown),
        }
        if event_types is not None:
            data["event_types"] = json.dumps(event_types)
        if narrow is not None:
            data["narrow"] = json.dumps(narrow)
        return zulip_request("POST", "register", data=data)
    except Exception as e:
        return {"error": str(e)}


def get_events(
    queue_id: str,
    last_event_id: int = -1,
    dont_block: bool = True,
) -> dict:
    """Get events from a registered event queue.

    Args:
        queue_id: The ID of the event queue (from register_event_queue).
        last_event_id: The ID of the last event received (-1 for all events).
        dont_block: If True, return immediately even if no events are available.
                    If False, use long-polling (waits up to 90 seconds).
    """
    try:
        params = {
            "queue_id": queue_id,
            "last_event_id": last_event_id,
            "dont_block": json.dumps(dont_block),
        }
        return zulip_request("GET", "events", params=params)
    except Exception as e:
        return {"error": str(e)}


def delete_event_queue(queue_id: str) -> dict:
    """Delete an event queue.

    Args:
        queue_id: The ID of the event queue to delete.
    """
    try:
        return zulip_request("DELETE", f"events?queue_id={queue_id}")
    except Exception as e:
        return {"error": str(e)}
