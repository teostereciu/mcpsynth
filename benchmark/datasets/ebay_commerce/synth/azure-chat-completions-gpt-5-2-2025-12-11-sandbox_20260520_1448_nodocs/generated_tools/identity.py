from typing import Any, Dict

from .ebay_http import EbayClient


USER_SCOPE = "https://api.ebay.com/oauth/api_scope/identity"


def get_user() -> Dict[str, Any]:
    """GET /commerce/identity/v1/user/"""
    c = EbayClient()
    return c.request(
        "GET",
        "/commerce/identity/v1/user/",
        user_scope=USER_SCOPE,
    )
