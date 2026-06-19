"""Zulip User Groups API tools."""
import json
from typing import Optional, List
from .client import zulip_request


def get_user_groups(include_deactivated_groups: bool = False) -> dict:
    """Get all user groups in the organization.

    Args:
        include_deactivated_groups: Whether to include deactivated user groups.
    """
    params = {"include_deactivated_groups": json.dumps(include_deactivated_groups)}
    return zulip_request("GET", "user_groups", params=params)


def create_user_group(
    name: str,
    description: str,
    members: List[int],
) -> dict:
    """Create a new user group.

    Args:
        name: The name of the user group.
        description: The description of the user group.
        members: List of user IDs to include as initial members.
    """
    data = {
        "name": name,
        "description": description,
        "members": json.dumps(members),
    }
    return zulip_request("POST", "user_groups/create", data=data)


def update_user_group(
    user_group_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Update a user group's name or description.

    Args:
        user_group_id: The ID of the user group to update.
        name: New name for the user group.
        description: New description for the user group.
    """
    data: dict = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    return zulip_request("PATCH", f"user_groups/{user_group_id}", data=data)


def deactivate_user_group(user_group_id: int) -> dict:
    """Deactivate a user group.

    Args:
        user_group_id: The ID of the user group to deactivate.
    """
    return zulip_request("POST", f"user_groups/{user_group_id}/deactivate")


def update_user_group_members(
    user_group_id: int,
    add: Optional[List[int]] = None,
    delete: Optional[List[int]] = None,
) -> dict:
    """Add or remove members from a user group.

    Args:
        user_group_id: The ID of the user group.
        add: List of user IDs to add to the group.
        delete: List of user IDs to remove from the group.
    """
    data: dict = {}
    if add is not None:
        data["add"] = json.dumps(add)
    if delete is not None:
        data["delete"] = json.dumps(delete)
    return zulip_request("POST", f"user_groups/{user_group_id}/members", data=data)


def get_user_group_members(user_group_id: int) -> dict:
    """Get the members of a user group.

    Args:
        user_group_id: The ID of the user group.
    """
    return zulip_request("GET", f"user_groups/{user_group_id}/members")


def get_is_user_group_member(user_group_id: int, user_id: int) -> dict:
    """Check if a user is a member of a user group.

    Args:
        user_group_id: The ID of the user group.
        user_id: The ID of the user to check.
    """
    return zulip_request("GET", f"user_groups/{user_group_id}/members/{user_id}")


def update_user_group_subgroups(
    user_group_id: int,
    add: Optional[List[int]] = None,
    delete: Optional[List[int]] = None,
) -> dict:
    """Add or remove subgroups from a user group.

    Args:
        user_group_id: The ID of the user group.
        add: List of user group IDs to add as subgroups.
        delete: List of user group IDs to remove as subgroups.
    """
    data: dict = {}
    if add is not None:
        data["add"] = json.dumps(add)
    if delete is not None:
        data["delete"] = json.dumps(delete)
    return zulip_request("POST", f"user_groups/{user_group_id}/subgroups", data=data)


def get_user_group_subgroups(user_group_id: int) -> dict:
    """Get the subgroups of a user group.

    Args:
        user_group_id: The ID of the user group.
    """
    return zulip_request("GET", f"user_groups/{user_group_id}/subgroups")
