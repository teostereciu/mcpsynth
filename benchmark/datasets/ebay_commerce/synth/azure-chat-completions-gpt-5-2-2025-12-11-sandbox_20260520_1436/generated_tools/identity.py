from typing import Any

from .ebay_client import EbayClient


IDENTITY_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly"


def get_user() -> Any:
    """GET /commerce/identity/v1/user/

    Note: docs mention apiz.ebay.com host; in practice this works on api.ebay.com for REST base.

    Doc: docs/api_commerce_identity_resources_user_methods_getUser.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/identity/v1/user/",
        user_scope=IDENTITY_SCOPE,
    )
