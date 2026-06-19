from typing import Any, Dict

from .ebay_client import EbayClient


IDENTITY_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly"


def get_user() -> Dict[str, Any]:
    """GET /commerce/identity/v1/user/ (apiz subdomain in docs; api base works for most apps)"""
    client = EbayClient()
    # Docs show apiz.*; in practice api.* also routes for many environments, but keep apiz.
    base = client.api_base.replace("https://api.", "https://apiz.").replace(
        "https://api.sandbox.", "https://apiz.sandbox."
    )
    return client.request(
        "GET",
        base,
        "/commerce/identity/v1/user/",
        auth="user",
        scope=IDENTITY_SCOPE,
    )
