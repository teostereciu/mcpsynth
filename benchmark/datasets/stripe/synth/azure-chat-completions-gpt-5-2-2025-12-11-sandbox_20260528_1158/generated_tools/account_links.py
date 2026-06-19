from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_account_link(
    account: str,
    type: str,
    refresh_url: str,
    return_url: str,
    *,
    collection_options: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "account": account,
        "type": type,
        "refresh_url": refresh_url,
        "return_url": return_url,
    }
    if collection_options is not None:
        params["collection_options"] = collection_options

    return stripe_request("POST", "/v1/account_links", params=params)
