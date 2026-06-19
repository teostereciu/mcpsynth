"""
eBay Commerce Charity API tools.
Base URL: https://api.sandbox.ebay.com/commerce/charity/v1
Auth: App token (client_credentials)
"""

import requests
from .auth import app_headers, _base_url


def _charity_url(path: str) -> str:
    return f"{_base_url()}/commerce/charity/v1{path}"


def get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve detailed information about a specific charitable organization by its ID.
    marketplace_id: EBAY_US or EBAY_GB (required).
    """
    try:
        resp = requests.get(
            _charity_url(f"/charity_org/{charity_org_id}"),
            headers=app_headers(marketplace_id),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_charity_orgs(
    query: str | None = None,
    registration_ids: str | None = None,
    page_size: int | None = None,
    offset: int | None = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Search for charitable organizations. Provide either query (keyword search) or
    registration_ids (comma-separated EINs/registration IDs), but not both.
    marketplace_id: EBAY_US or EBAY_GB (required).
    """
    try:
        params: dict = {}
        if query:
            params["q"] = query
        if registration_ids:
            params["registration_ids"] = registration_ids
        if page_size is not None:
            params["page_size"] = page_size
        if offset is not None:
            params["offset"] = offset

        resp = requests.get(
            _charity_url("/charity_org"),
            headers=app_headers(marketplace_id),
            params=params,
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
