from typing import Any, Dict, Optional

from .http import hubspot_request


def owners_list(*, archived: bool = False, email: Optional[str] = None, after: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"archived": str(bool(archived)).lower()}
    if email is not None:
        params["email"] = email
    if after is not None:
        params["after"] = after
    if limit is not None:
        params["limit"] = limit
    return hubspot_request("GET", "/crm/v3/owners", params=params)


def owners_get(owner_id: str, *, archived: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if archived is not None:
        params["archived"] = str(bool(archived)).lower()
    return hubspot_request("GET", f"/crm/v3/owners/{owner_id}", params=params)
