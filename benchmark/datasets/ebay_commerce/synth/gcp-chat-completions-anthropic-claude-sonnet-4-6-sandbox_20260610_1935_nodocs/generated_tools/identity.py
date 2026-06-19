"""
eBay Commerce Identity API tools.
Base path: /commerce/identity/v1
Auth: user token (refresh_token)
"""

from .auth import user_get

_BASE = "/commerce/identity/v1"


def get_user() -> dict:
    """
    Retrieve the authenticated eBay user's account information.

    Returns:
        Dict with userId, username, accountType, address, contact info, etc.
    """
    return user_get(f"{_BASE}/user/")
