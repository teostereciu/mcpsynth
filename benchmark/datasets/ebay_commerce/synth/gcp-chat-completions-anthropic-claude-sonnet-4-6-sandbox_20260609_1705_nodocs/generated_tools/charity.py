"""
eBay Commerce Charity API tools.
Uses app-token (client_credentials).
Base: /commerce/charity/v1
"""

from typing import Optional
import requests
from .auth import BASE_URL, app_headers, safe_json

_BASE = f"{BASE_URL}/commerce/charity/v1"


# ── Charity Organizations ─────────────────────────────────────────────────────

def get_charity_org(charity_org_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve details for a single charity organization by its eBay charity ID.

    Args:
        charity_org_id: The eBay charity organization ID.
        x_ebay_c_marketplace_id: Marketplace ID header (default 'EBAY_US').
    """
    url = f"{_BASE}/charity_org/{charity_org_id}"
    headers = app_headers()
    headers["X-EBAY-C-MARKETPLACE-ID"] = x_ebay_c_marketplace_id
    resp = requests.get(url, headers=headers, timeout=15)
    return safe_json(resp)


def get_charity_orgs_by_keyword(
    q: str,
    limit: int = 10,
    offset: int = 0,
    x_ebay_c_marketplace_id: str = "EBAY_US",
    registration_ids: Optional[str] = None,
) -> dict:
    """
    Search for charity organizations by keyword.

    Args:
        q: Keyword search string (e.g. 'Red Cross').
        limit: Number of results to return (default 10, max 100).
        offset: Pagination offset (default 0).
        x_ebay_c_marketplace_id: Marketplace ID header (default 'EBAY_US').
        registration_ids: Comma-separated charity registration IDs to filter by.
    """
    url = f"{_BASE}/charity_org"
    headers = app_headers()
    headers["X-EBAY-C-MARKETPLACE-ID"] = x_ebay_c_marketplace_id
    params: dict = {"q": q, "limit": limit, "offset": offset}
    if registration_ids:
        params["registration_ids"] = registration_ids
    resp = requests.get(url, headers=headers, params=params, timeout=15)
    return safe_json(resp)


def get_charity_org_by_legacy_id(
    legacy_charity_id: str,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve a charity organization using its legacy eBay Giving Works charity ID.

    Args:
        legacy_charity_id: The legacy charity ID.
        x_ebay_c_marketplace_id: Marketplace ID header (default 'EBAY_US').
    """
    url = f"{_BASE}/charity_org/get_charity_org_by_legacy_id"
    headers = app_headers()
    headers["X-EBAY-C-MARKETPLACE-ID"] = x_ebay_c_marketplace_id
    params = {"legacy_charity_id": legacy_charity_id}
    resp = requests.get(url, headers=headers, params=params, timeout=15)
    return safe_json(resp)
