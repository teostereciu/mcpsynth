"""
eBay Commerce Charity API tools.
Uses app token (client_credentials).
Base: /commerce/charity/v1
"""
from typing import Optional
import requests
from .auth import BASE_URL, app_headers, safe_json

CHARITY_BASE = f"{BASE_URL}/commerce/charity/v1"


def get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve detailed information about a specific charitable organization by its ID.
    Returns name, description, location, logo, mission statement, website, and registration ID.

    Args:
        charity_org_id: The unique ID of the charitable organization.
        marketplace_id: eBay marketplace ID — EBAY_US or EBAY_GB (default EBAY_US).
    """
    try:
        resp = requests.get(
            f"{CHARITY_BASE}/charity_org/{charity_org_id}",
            headers=app_headers(marketplace_id),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_charity_orgs(
    query: Optional[str] = None,
    registration_ids: Optional[str] = None,
    page_size: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Search for charitable organizations by keyword or registration IDs.
    Returns a paginated list of matching organizations.

    Args:
        query: Keyword string matching name, mission statement, or description.
        registration_ids: Comma-separated registration IDs (e.g. EINs). Max 20.
                          Do not combine with query.
        page_size: Results per page (1-100, default 20).
        offset: Pagination offset (0-10000, default 0).
        marketplace_id: eBay marketplace ID — EBAY_US or EBAY_GB (default EBAY_US).
    """
    try:
        params: dict = {}
        if query:
            params["query"] = query
        if registration_ids:
            params["registration_ids"] = registration_ids
        params["page_size"] = page_size
        params["offset"] = offset

        resp = requests.get(
            f"{CHARITY_BASE}/charity_org",
            headers=app_headers(marketplace_id),
            params=params,
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}
