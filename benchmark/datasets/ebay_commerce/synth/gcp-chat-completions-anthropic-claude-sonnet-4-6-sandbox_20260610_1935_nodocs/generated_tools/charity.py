"""
eBay Commerce Charity API tools.
Base path: /commerce/charity/v1
Auth: app token (client_credentials)
"""

from .auth import app_get

_BASE = "/commerce/charity/v1"


def get_charity_org(charity_org_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve details for a specific charity organization by its eBay charity ID.

    Args:
        charity_org_id: The eBay charity organization ID.
        x_ebay_c_marketplace_id: Marketplace context (default EBAY_US).

    Returns:
        Dict with charityOrgId, name, missionStatement, website, logoImage, etc.
    """
    from .auth import get_app_token
    import requests, os

    token = get_app_token()
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    base = "https://api.ebay.com" if env == "PRODUCTION" else "https://api.sandbox.ebay.com"
    url = f"{base}{_BASE}/charity_org/{charity_org_id}"
    resp = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id,
        },
        timeout=30,
    )
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json()


def search_charity_orgs(
    q: str | None = None,
    registration_ids: str | None = None,
    limit: int = 20,
    offset: int = 0,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Search for charity organizations on eBay.

    Args:
        q: Keywords to search charity names/descriptions.
        registration_ids: Comma-separated charity registration IDs (EIN for US).
        limit: Number of results to return (max 100).
        offset: Pagination offset.
        x_ebay_c_marketplace_id: Marketplace context (default EBAY_US).

    Returns:
        Dict with charityOrgs list and pagination info.
    """
    from .auth import get_app_token
    import requests, os

    token = get_app_token()
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    base = "https://api.ebay.com" if env == "PRODUCTION" else "https://api.sandbox.ebay.com"
    url = f"{base}{_BASE}/charity_org"
    params: dict = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if registration_ids:
        params["registration_ids"] = registration_ids
    resp = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id,
        },
        params=params,
        timeout=30,
    )
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json()


def get_charity_org_by_legacy_id(legacy_charity_id: str, x_ebay_c_marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve a charity organization using a legacy charity ID.

    Args:
        legacy_charity_id: The legacy eBay charity ID.
        x_ebay_c_marketplace_id: Marketplace context (default EBAY_US).

    Returns:
        Dict with charity organization details.
    """
    from .auth import get_app_token
    import requests, os

    token = get_app_token()
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    base = "https://api.ebay.com" if env == "PRODUCTION" else "https://api.sandbox.ebay.com"
    url = f"{base}{_BASE}/charity_org/get_charity_org_by_legacy_id"
    resp = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id,
        },
        params={"legacy_charity_id": legacy_charity_id},
        timeout=30,
    )
    if not resp.ok:
        return {"error": resp.text, "status_code": resp.status_code}
    return resp.json()
