def get_user_profile(client, user_id: int):
    """Get a user's profile by ID.

    Args:
        client: The Zulip API client.
        user_id: The ID of the user.
    """
    return client._request("GET", f"/users/{user_id}")

def get_user_presence(client, user_id: int):
    """Get a user's presence status.

    Args:
        client: The Zulip API client.
        user_id: The ID of the user.
    """
    return client._request("GET", f"/users/{user_id}/presence")

