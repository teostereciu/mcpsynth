"""eBay Commerce Identity API tools — user-token authenticated."""
from __future__ import annotations
import os
import requests
from .auth import get_user_token

SANDBOX = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper() == "SANDBOX"
BASE = "https://api.sandbox.ebay.com" if SANDBOX else "https://api.ebay.com"


def _headers() -> dict:
    token = get_user_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def get_user() -> dict:
    """Retrieve the account profile information for the authenticated eBay user.

    Returns account type (INDIVIDUAL or BUSINESS), user ID, username, status,
    registration marketplace, and account-specific details.
    """
    url = f"{BASE}/commerce/identity/v1/user/"
    try:
        resp = requests.get(url, headers=_headers(), timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
