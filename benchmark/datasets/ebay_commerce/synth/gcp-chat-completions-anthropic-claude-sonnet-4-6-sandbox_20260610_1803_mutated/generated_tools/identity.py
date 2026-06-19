"""
eBay Commerce Identity API tools.
Base URL: https://api.sandbox.ebay.com/commerce/identity/v1
Auth: User token (refresh_token) with commerce.identity.readonly scope
"""

import requests
from .auth import get_user_token, _base_url


def _identity_url(path: str) -> str:
    return f"{_base_url()}/commerce/identity/v1{path}"


def get_user() -> dict:
    """
    Retrieve the account profile information for the authenticated user.
    Returns accountType, userId, username, status, registrationMarketplaceId,
    and either businessAccount or individualAccount details depending on account type.
    Requires a valid EBAY_REFRESH_TOKEN with commerce.identity.readonly scope.
    """
    try:
        resp = requests.get(
            _identity_url("/user/"),
            headers={"Authorization": f"Bearer {get_user_token()}"},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
