"""
Zulip MCP Tools — Realm / Organization domain
Covers: realm info, emoji, filters, profile fields, linkifiers, playgrounds
"""

from typing import Optional
from .client import zulip_get, zulip_post, zulip_patch, zulip_delete


def get_server_settings() -> dict:
    """Get the server's public settings (no authentication required)."""
    return zulip_get("/server_settings")


def get_realm_info() -> dict:
    """Get information about the current Zulip organization (realm)."""
    return zulip_get("/realm")


def get_realm_emoji() -> dict:
    """Get all custom emoji defined in the organization."""
    return zulip_get("/realm/emoji")


def upload_realm_emoji(emoji_name: str, file_path: str) -> dict:
    """Upload a custom emoji for the organization.

    Args:
        emoji_name: The name for the new custom emoji (alphanumeric + hyphens).
        file_path: Path to the image file (PNG, GIF, or JPEG, max 25 MB).
    """
    import os
    from .client import zulip_post_file
    if not os.path.isfile(file_path):
        return {"result": "error", "msg": f"File not found: {file_path}"}
    filename = os.path.basename(file_path)
    try:
        with open(file_path, "rb") as f:
            files = {"f1": (filename, f)}
            return zulip_post_file(f"/realm/emoji/{emoji_name}", files)
    except Exception as exc:
        return {"result": "error", "msg": str(exc)}


def delete_realm_emoji(emoji_name: str) -> dict:
    """Delete a custom emoji from the organization.

    Args:
        emoji_name: The name of the custom emoji to delete.
    """
    return zulip_delete(f"/realm/emoji/{emoji_name}")


def get_realm_filters() -> dict:
    """Get all linkifier (URL filter) rules for the organization."""
    return zulip_get("/realm/filters")


def add_realm_filter(pattern: str, url_format_string: str) -> dict:
    """Add a linkifier rule to the organization.

    Args:
        pattern: A Python regular expression to match in messages.
        url_format_string: The URL template to linkify matches to,
                           using %(group_name)s for capture groups.
    """
    return zulip_post(
        "/realm/filters",
        {"pattern": pattern, "url_format_string": url_format_string},
    )


def update_realm_filter(filter_id: int, pattern: str, url_format_string: str) -> dict:
    """Update an existing linkifier rule.

    Args:
        filter_id: The ID of the linkifier to update.
        pattern: New regular expression pattern.
        url_format_string: New URL template.
    """
    return zulip_patch(
        f"/realm/filters/{filter_id}",
        {"pattern": pattern, "url_format_string": url_format_string},
    )


def delete_realm_filter(filter_id: int) -> dict:
    """Delete a linkifier rule from the organization.

    Args:
        filter_id: The ID of the linkifier to delete.
    """
    return zulip_delete(f"/realm/filters/{filter_id}")


def get_realm_profile_fields() -> dict:
    """Get all custom profile fields defined in the organization."""
    return zulip_get("/realm/profile_fields")


def create_realm_profile_field(
    name: str,
    field_type: int,
    hint: Optional[str] = None,
    field_data: Optional[str] = None,
) -> dict:
    """Create a custom profile field for the organization.

    Args:
        name: The name of the profile field.
        field_type: Field type integer:
                    1=Short text, 2=Long text, 3=List of options,
                    4=Date, 5=Link, 6=Person, 7=Pronouns.
        hint: Hint text shown below the field.
        field_data: JSON-encoded field options (for type 3 list fields).
    """
    params: dict = {"name": name, "field_type": field_type}
    if hint is not None:
        params["hint"] = hint
    if field_data is not None:
        params["field_data"] = field_data
    return zulip_post("/realm/profile_fields", params)


def reorder_realm_profile_fields(order: str) -> dict:
    """Reorder the custom profile fields in the organization.

    Args:
        order: JSON-encoded list of profile field IDs in the desired order,
               e.g. "[3, 1, 2]".
    """
    return zulip_patch("/realm/profile_fields", {"order": order})


def delete_realm_profile_field(field_id: int) -> dict:
    """Delete a custom profile field from the organization.

    Args:
        field_id: The ID of the profile field to delete.
    """
    return zulip_delete(f"/realm/profile_fields/{field_id}")


def get_realm_playgrounds() -> dict:
    """Get all code playgrounds configured for the organization."""
    return zulip_get("/realm/playgrounds")


def add_realm_playground(
    name: str, pygments_language: str, url_prefix: str
) -> dict:
    """Add a code playground to the organization.

    Args:
        name: A human-readable name for the playground.
        pygments_language: The Pygments language identifier (e.g. "python").
        url_prefix: The URL prefix for the playground, e.g.
                    "https://replit.com/languages/python3?code=".
    """
    return zulip_post(
        "/realm/playgrounds",
        {
            "name": name,
            "pygments_language": pygments_language,
            "url_prefix": url_prefix,
        },
    )


def delete_realm_playground(playground_id: int) -> dict:
    """Delete a code playground from the organization.

    Args:
        playground_id: The ID of the playground to delete.
    """
    return zulip_delete(f"/realm/playgrounds/{playground_id}")


def get_realm_linkifiers() -> dict:
    """Get all linkifiers (URL filters) for the organization (alias for get_realm_filters)."""
    return zulip_get("/realm/linkifiers")
