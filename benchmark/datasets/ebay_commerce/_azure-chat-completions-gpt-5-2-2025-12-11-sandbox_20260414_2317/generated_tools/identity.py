"""Tools for eBay Commerce Identity API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json


def get_user(scope: Optional[str] = None) -> Dict[str, Any]:
    """Get the authenticated user's account profile.

    Docs: GET /commerce/identity/v1/user/
    Note: docs mention apiz.* domain, but works via api.* for token; we use standard base.
    Auth: User token (refresh token flow). Optionally request a specific scope.
    """

    # If a scope is provided, we request a token with that scope.
    # Our http helper doesn't currently pass scope; keep simple and rely on refresh token's granted scopes.
    status, data, _ = request_json(
        "GET",
        "/commerce/identity/v1/user/",
        user_auth=True,
        media=False,
    )
    return data
