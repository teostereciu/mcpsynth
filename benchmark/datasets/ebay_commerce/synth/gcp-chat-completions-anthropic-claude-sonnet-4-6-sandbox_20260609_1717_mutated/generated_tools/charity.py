"""eBay Commerce Charity API tools — app-token authenticated."""
from __future__ import annotations
import os
from typing import Optional
import requests
from .auth import get_app_token

SANDBOX = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper() == "SANDBOX"
BASE = "https://api.sandbox.ebay.com" if SANDBOX else "https://api.ebay.com"


def _headers(marketplace_id: str = "EBAY_US") -> dict:
    token = get_app_token()
    return {
        "Authorization": f"Bearer {token}",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }


def get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve detailed information about a charitable organization by its ID.

    Args:
        charity_org_id: The unique ID of the charitable organization.
        marketplace_id: eBay marketplace ID — EBAY_US or EBAY_GB (default EBAY_US).
    """
    url = f"{BASE}/commerce/charity/v1/charity_org/{charity_org_id}"
    try:
        resp = requests.get(url, headers=_headers(marketplace_id), timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_charity_orgs(
    query: Optional[str] = None,
    registration_ids: Optional[str] = None,
    page_size: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Search for charitable organizations. Provide either query or registration_ids.

    Args:
        query: Keyword string matching name, mission statement, or description.
        registration_ids: Comma-separated list of registration IDs (max 20).
        page_size: Results per page (1-100, default 20).
        offset: Pagination offset (0-10000, default 0).
        marketplace_id: eBay marketplace ID — EBAY_US or EBAY_GB (default EBAY_US).
    """
    url = f"{BASE}/commerce/charity/v1/charity_org"
    params: dict = {"page_size": page_size, "offset": offset}
    if query:
        params["q"] = query
    if registration_ids:
        params["registration_ids"] = registration_ids
    try:
        resp = requests.get(url, headers=_headers(marketplace_id), params=params, timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
