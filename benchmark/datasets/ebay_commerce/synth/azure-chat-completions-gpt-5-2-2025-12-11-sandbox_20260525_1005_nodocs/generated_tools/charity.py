from typing import Any, Dict, Optional

from .ebay_auth import auth_header, get_base_url, request_json


# Charity API (application token)


def get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/{charityOrgId}"""
    url = get_base_url() + f"/commerce/charity/v1/charity_org/{charity_org_id}"
    res, err = request_json("GET", url, headers={**auth_header(user=False)})
    return err or res  # type: ignore


def charity_search(
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/search"""
    url = get_base_url() + "/commerce/charity/v1/charity_org/search"
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if registration_ids:
        params["registration_ids"] = registration_ids
    res, err = request_json("GET", url, headers={**auth_header(user=False)}, params=params)
    return err or res  # type: ignore
