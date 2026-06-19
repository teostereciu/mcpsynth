from typing import Any, Dict

from .http_client import EbayHTTP


IDENTITY_SCOPE_USER = "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly"


def get_user() -> Dict[str, Any]:
    """GET /commerce/identity/v1/user/

    Doc: docs/api_commerce_identity_resources_user_methods_getUser.md

    Note: Identity API uses apiz.* host per doc; we route via api_base which should work for most commerce APIs,
    but to follow doc we use apiz subdomain.
    """
    http = EbayHTTP()
    base = "https://apiz.ebay.com" if http.oauth.environment == "PRODUCTION" else "https://apiz.sandbox.ebay.com"
    return http.request(
        "GET",
        base,
        "/commerce/identity/v1/user/",
        scope=IDENTITY_SCOPE_USER,
        user=True,
    )
