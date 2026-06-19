"""Zulip Server & Organization API tools."""
import json
from typing import Optional, List
from .client import zulip_request


def get_server_settings() -> dict:
    """Get global settings for the Zulip server (no authentication required)."""
    return zulip_request("GET", "server_settings")


def get_linkifiers() -> dict:
    """Get all linkifiers configured for the organization."""
    return zulip_request("GET", "realm/linkifiers")


def add_linkifier(pattern: str, url_template: str) -> dict:
    """Add a new linkifier to the organization.

    Args:
        pattern: The regex pattern to linkify.
        url_template: The RFC 6570 URL template for the linkified URL.
    """
    data = {"pattern": pattern, "url_template": url_template}
    return zulip_request("POST", "realm/filters", data=data)


def update_linkifier(filter_id: int, pattern: str, url_template: str) -> dict:
    """Update an existing linkifier.

    Args:
        filter_id: The ID of the linkifier to update.
        pattern: The new regex pattern.
        url_template: The new RFC 6570 URL template.
    """
    data = {"pattern": pattern, "url_template": url_template}
    return zulip_request("PATCH", f"realm/filters/{filter_id}", data=data)


def remove_linkifier(filter_id: int) -> dict:
    """Remove a linkifier from the organization.

    Args:
        filter_id: The ID of the linkifier to remove.
    """
    return zulip_request("DELETE", f"realm/filters/{filter_id}")


def reorder_linkifiers(ordered_linkifier_ids: List[int]) -> dict:
    """Reorder the linkifiers in the organization.

    Args:
        ordered_linkifier_ids: List of linkifier IDs in the desired order.
    """
    return zulip_request(
        "PATCH",
        "realm/linkifiers",
        data={"ordered_linkifier_ids": json.dumps(ordered_linkifier_ids)},
    )


def get_custom_emoji() -> dict:
    """Get all custom emoji in the organization."""
    return zulip_request("GET", "realm/emoji")


def upload_custom_emoji(emoji_name: str, file_path: str) -> dict:
    """Upload a custom emoji for the organization.

    Args:
        emoji_name: The name for the custom emoji.
        file_path: Local path to the image file to upload.
    """
    try:
        with open(file_path, "rb") as f:
            return zulip_request(
                "POST",
                f"realm/emoji/{emoji_name}",
                files={"f": f},
            )
    except Exception as e:
        return {"error": str(e)}


def deactivate_custom_emoji(emoji_name: str) -> dict:
    """Deactivate a custom emoji in the organization.

    Args:
        emoji_name: The name of the custom emoji to deactivate.
    """
    return zulip_request("DELETE", f"realm/emoji/{emoji_name}")


def get_custom_profile_fields() -> dict:
    """Get all custom profile fields defined in the organization."""
    return zulip_request("GET", "realm/profile_fields")


def create_custom_profile_field(
    name: str,
    field_type: int,
    hint: Optional[str] = None,
    field_data: Optional[dict] = None,
    display_in_profile_summary: Optional[bool] = None,
    required: Optional[bool] = None,
) -> dict:
    """Create a new custom profile field (admin only).

    Args:
        name: The name of the custom profile field.
        field_type: Field type: 1=short text, 2=long text, 3=select, 4=date,
                    5=link, 6=user, 7=external account, 8=pronouns.
        hint: Hint text for the field.
        field_data: Additional data for select/external account fields.
        display_in_profile_summary: Whether to display in profile summary.
        required: Whether the field is required.
    """
    data: dict = {"name": name, "field_type": field_type}
    if hint is not None:
        data["hint"] = hint
    if field_data is not None:
        data["field_data"] = json.dumps(field_data)
    if display_in_profile_summary is not None:
        data["display_in_profile_summary"] = json.dumps(display_in_profile_summary)
    if required is not None:
        data["required"] = json.dumps(required)
    return zulip_request("POST", "realm/profile_fields", data=data)


def reorder_custom_profile_fields(order: List[int]) -> dict:
    """Reorder custom profile fields.

    Args:
        order: List of custom profile field IDs in the desired order.
    """
    return zulip_request(
        "PATCH",
        "realm/profile_fields",
        data={"order": json.dumps(order)},
    )


def add_code_playground(name: str, pygments_language: str, url_template: str) -> dict:
    """Add a code playground to the organization.

    Args:
        name: The name of the code playground.
        pygments_language: The Pygments language identifier.
        url_template: The URL template for the playground.
    """
    data = {
        "name": name,
        "pygments_language": pygments_language,
        "url_template": url_template,
    }
    return zulip_request("POST", "realm/playgrounds", data=data)


def remove_code_playground(playground_id: int) -> dict:
    """Remove a code playground from the organization.

    Args:
        playground_id: The ID of the code playground to remove.
    """
    return zulip_request("DELETE", f"realm/playgrounds/{playground_id}")


def get_realm_exports() -> dict:
    """Get all data exports for the organization (admin only)."""
    return zulip_request("GET", "export/realm")


def export_realm() -> dict:
    """Create a new data export for the organization (admin only)."""
    return zulip_request("POST", "export/realm")


def get_realm_export_consents() -> dict:
    """Get the data export consent state for all users (admin only)."""
    return zulip_request("GET", "export/realm/consents")


def register_event_queue(
    event_types: Optional[List[str]] = None,
    narrow: Optional[List[List[str]]] = None,
    all_public_streams: bool = False,
) -> dict:
    """Register an event queue for real-time events.

    Args:
        event_types: List of event types to subscribe to (e.g. ["message", "presence"]).
        narrow: Narrow filter for message events.
        all_public_streams: Whether to receive events for all public streams.
    """
    data: dict = {"all_public_streams": json.dumps(all_public_streams)}
    if event_types is not None:
        data["event_types"] = json.dumps(event_types)
    if narrow is not None:
        data["narrow"] = json.dumps(narrow)
    return zulip_request("POST", "register", data=data)


def get_events(queue_id: str, last_event_id: int = -1, dont_block: bool = True) -> dict:
    """Get events from a registered event queue.

    Args:
        queue_id: The ID of the event queue.
        last_event_id: The ID of the last event received (-1 for all events).
        dont_block: If True, return immediately even if no events are available.
    """
    params = {
        "queue_id": queue_id,
        "last_event_id": last_event_id,
        "dont_block": json.dumps(dont_block),
    }
    return zulip_request("GET", "events", params=params)


def delete_event_queue(queue_id: str) -> dict:
    """Delete a registered event queue.

    Args:
        queue_id: The ID of the event queue to delete.
    """
    return zulip_request("DELETE", "events", data={"queue_id": queue_id})
