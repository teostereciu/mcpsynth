from typing import Any, Dict

from .ebay_auth import request_json


# Charity API (application token)


def get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/{charityOrgId}"""
    status, body = request_json(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        user=False,
    )
    return {"status": status, "data": body}


def charity_search(query: str, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/search"""
    status, body = request_json(
        "GET",
        "/commerce/charity/v1/charity_org/search",
        params={"q": query, "limit": limit, "offset": offset},
        user=False,
    )
    return {"status": status, "data": body}
