from typing import Any, Dict, Optional

from .common import client


def get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/charity/v1/charity_org/{charity_org_id}", "app")


def get_charity_orgs(q: Optional[str] = None, registration_id: Optional[str] = None, nonprofit_org_name: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/charity/v1/charity_org",
        "app",
        params={
            "q": q,
            "registration_id": registration_id,
            "nonprofit_org_name": nonprofit_org_name,
            "limit": limit,
            "offset": offset,
        },
    )
