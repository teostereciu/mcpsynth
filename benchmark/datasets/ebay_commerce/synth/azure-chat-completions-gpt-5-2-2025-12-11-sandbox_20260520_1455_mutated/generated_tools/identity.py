from __future__ import annotations

from typing import Any, Dict

from .ebay_client import EbayClient


def get_user() -> Dict[str, Any]:
    """GET /user/

    OAuth scope: commerce.identity.readonly (user token)
    Base domain: apiz.ebay.com (note: sandbox uses apiz.sandbox.ebay.com)
    """
    client = EbayClient.for_identity_api(user_scoped=True)
    return client.request("GET", "/commerce/identity/v1/user/")
