from __future__ import annotations

from typing import Any, Dict

from .http import commerce_base_url, request_json


SCOPE_IDENTITY_READONLY = "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly"


def get_user() -> Dict[str, Any]:
    """GET /commerce/identity/v1/user/ (user token)."""
    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/identity/v1/user/",
        user_auth=True,
        scope=SCOPE_IDENTITY_READONLY,
    )
