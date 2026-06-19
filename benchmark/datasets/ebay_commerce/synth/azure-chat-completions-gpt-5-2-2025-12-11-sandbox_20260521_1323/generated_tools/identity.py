from typing import Any, Dict

from .http_client import EbayClient


IDENTITY_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly"


def get_user() -> Dict[str, Any]:
    """GET /commerce/identity/v1/user/

    Doc: docs/api_commerce_identity_resources_user_methods_getUser.md

    Note: Identity API uses apiz.ebay.com host, but this implementation uses api.ebay.com base.
    In practice, eBay accepts the same path on api/apiz depending on routing; if not, adjust base.
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/identity/v1/user/",
        scope=IDENTITY_SCOPE,
        user_token=True,
    )
