"""
eBay Commerce Identity API tools.
Base: /commerce/identity/v1
Auth: user token (refresh_token)
"""

import requests
from .auth import BASE_URL, user_headers, safe_json

_BASE = f"{BASE_URL}/commerce/identity/v1"


def get_user_identity() -> dict:
    """
    Retrieve the authenticated eBay user's identity information,
    including username, account type, and contact details.
    """
    try:
        resp = requests.get(
            f"{_BASE}/user/",
            headers=user_headers(),
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}
