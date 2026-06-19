"""
eBay Commerce Identity API tools.
Uses user-token (refresh_token grant).
Base: /commerce/identity/v1
"""

import requests
from .auth import BASE_URL, user_headers, safe_json

_BASE = f"{BASE_URL}/commerce/identity/v1"


def get_user() -> dict:
    """
    Return the authenticated eBay user's account information,
    including username, account type, and contact details.
    """
    url = f"{_BASE}/user/"
    resp = requests.get(url, headers=user_headers(), timeout=15)
    return safe_json(resp)
