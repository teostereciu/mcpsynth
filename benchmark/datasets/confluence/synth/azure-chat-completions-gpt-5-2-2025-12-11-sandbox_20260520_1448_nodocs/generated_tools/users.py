from typing import Any, Dict, Optional

from .http import confluence_request


def get_current_user() -> Dict[str, Any]:
    return confluence_request("GET", "/rest/api/user/current")


def get_user(account_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"accountId": account_id}
    if expand:
        params["expand"] = expand
    return confluence_request("GET", "/rest/api/user", params=params)
