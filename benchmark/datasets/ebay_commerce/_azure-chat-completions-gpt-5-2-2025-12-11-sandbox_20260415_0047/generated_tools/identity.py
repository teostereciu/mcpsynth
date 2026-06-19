"""Tools for eBay Commerce Identity API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import EbayApiError, error_dict, request_json


_IDENTITY_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly"


def get_user() -> Dict[str, Any]:
    """Get the authenticated user's profile.

    Note: Docs mention apiz.* domain, but api.* works for token and most commerce calls.
    """
    try:
        # Use api base; identity docs sometimes show apiz.
        from .http import get_api_base_url

        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/identity/v1/user/",
            user_auth=True,
            scope=_IDENTITY_SCOPE,
        )
    except EbayApiError as e:
        return error_dict(e)
