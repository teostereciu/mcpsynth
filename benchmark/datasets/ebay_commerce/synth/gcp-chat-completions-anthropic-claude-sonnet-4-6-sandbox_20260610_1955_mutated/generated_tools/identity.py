"""
eBay Commerce Identity API tools.
Uses user token (refresh_token grant).
Base: /commerce/identity/v1
Note: Identity API uses apiz.sandbox.ebay.com / apiz.ebay.com subdomain.
"""
import os
import requests
from .auth import get_user_token, safe_json

EBAY_ENV = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
if EBAY_ENV == "PRODUCTION":
    IDENTITY_BASE = "https://apiz.ebay.com/commerce/identity/v1"
else:
    IDENTITY_BASE = "https://apiz.sandbox.ebay.com/commerce/identity/v1"


def get_user() -> dict:
    """
    Retrieve the account profile information for the authenticated user.
    Returns account type (INDIVIDUAL or BUSINESS), user ID, username, status,
    registration marketplace, and account details (individual or business).
    Requires a user access token with commerce.identity.readonly scope.
    """
    try:
        resp = requests.get(
            f"{IDENTITY_BASE}/user/",
            headers={
                "Authorization": f"Bearer {get_user_token()}",
                "Content-Type": "application/json",
            },
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}
