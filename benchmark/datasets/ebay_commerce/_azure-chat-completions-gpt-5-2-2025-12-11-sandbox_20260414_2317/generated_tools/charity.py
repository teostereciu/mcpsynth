"""Tools for eBay Commerce Charity API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json


def search_charity_orgs(
    *,
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Search for supported charitable organizations.

    Docs: GET /commerce/charity/v1/charity_org?q=...&limit=...&offset=...
    Header: X-EBAY-C-MARKETPLACE-ID required (EBAY_US or EBAY_GB)
    Auth: Application token
    """

    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if registration_ids is not None:
        params["registration_ids"] = registration_ids
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    status, data, _ = request_json(
        "GET",
        "/commerce/charity/v1/charity_org",
        params=params or None,
        user_auth=False,
        media=False,
        extra_headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
    return data


def get_charity_org(charity_org_id: str, *, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get details for a specific charitable organization.

    Docs: GET /commerce/charity/v1/charity_org/{charity_org_id}
    Header: X-EBAY-C-MARKETPLACE-ID required
    Auth: Application token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        user_auth=False,
        media=False,
        extra_headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
    return data
