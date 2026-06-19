"""Tools for eBay Commerce Charity API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import EbayApiError, error_dict, get_api_base_url, request_json


def search_charity_orgs(
    *,
    marketplace_id: str = "EBAY_US",
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Search for supported charitable organizations.

    Provide either q or registration_ids (comma-separated).

    Charity API requires X-EBAY-C-MARKETPLACE-ID header.
    """
    try:
        params: Dict[str, Any] = {}
        if q:
            params["q"] = q
        if registration_ids:
            params["registration_ids"] = registration_ids
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset

        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/charity/v1/charity_org/",
            params=params or None,
            headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Get details for a specific charitable organization."""
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/charity/v1/charity_org/{charity_org_id}",
            headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)
