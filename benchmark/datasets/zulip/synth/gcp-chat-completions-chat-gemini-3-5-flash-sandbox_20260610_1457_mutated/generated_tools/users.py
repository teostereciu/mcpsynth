from typing import Any, Dict, Optional, Union
from generated_tools.client import client

def get_users(
    client_gravatar: Optional[bool] = False,
    include_custom_profile_fields: Optional[bool] = True,
) -> Dict[str, Any]:
    """
    Get all users in the Zulip organization.
    
    Args:
        client_gravatar: Whether to return gravatar URLs. Default is False.
        include_custom_profile_fields: Whether to include custom profile fields. Default is True.
    """
    params = {
        "client_gravatar": str(client_gravatar).lower(),
        "include_custom_profile_fields": str(include_custom_profile_fields).lower(),
    }
    return client.request("GET", "users", params=params)

def get_user(user_id: int) -> Dict[str, Any]:
    """
    Get details of a user by their user ID.
    
    Args:
        user_id: The ID of the user.
    """
    return client.request("GET", f"users/{user_id}")

def get_user_by_email(email: str) -> Dict[str, Any]:
    """
    Get details of a user by their email address.
    
    Args:
        email: The email address of the user.
    """
    return client.request("GET", f"users/{email}")

def get_own_user() -> Dict[str, Any]:
    """
    Get details of the current authenticated user.
    """
    return client.request("GET", "users/me")

def create_user(
    email: str,
    password: str,
    full_name: str,
) -> Dict[str, Any]:
    """
    Create a new user in the Zulip organization.
    
    Args:
        email: The email address of the new user.
        password: The password of the new user.
        full_name: The full name of the new user.
    """
    data = {
        "email": email,
        "password": password,
        "full_name": full_name,
    }
    return client.request("POST", "users", data=data)

def update_user(
    user_id: int,
    full_name: Optional[str] = None,
    role: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Update details of a user.
    
    Args:
        user_id: The ID of the user to update.
        full_name: New full name for the user.
        role: New role for the user (e.g., 100 = Member, 200 = Administrator, 300 = Moderator, 400 = Guest).
    """
    data: Dict[str, Any] = {}
    if full_name is not None:
        data["full_name"] = full_name
    if role is not None:
        data["role"] = role

    return client.request("PATCH", f"users/{user_id}", data=data)

def deactivate_user(user_id: int) -> Dict[str, Any]:
    """
    Deactivate a user.
    
    Args:
        user_id: The ID of the user to deactivate.
    """
    return client.request("DELETE", f"users/{user_id}")

def reactivate_user(user_id: int) -> Dict[str, Any]:
    """
    Reactivate a deactivated user.
    
    Args:
        user_id: The ID of the user to reactivate.
    """
    return client.request("POST", f"users/{user_id}/reactivate")

def get_user_presence(user_id_or_email: Union[str, int]) -> Dict[str, Any]:
    """
    Get the presence status of a user.
    
    Args:
        user_id_or_email: The user ID (integer) or email address (string) of the user.
    """
    return client.request("GET", f"users/{user_id_or_email}/presence")

def get_realm_presence() -> Dict[str, Any]:
    """
    Get the presence status of all active users in the organization.
    """
    return client.request("GET", "realm/presence")
