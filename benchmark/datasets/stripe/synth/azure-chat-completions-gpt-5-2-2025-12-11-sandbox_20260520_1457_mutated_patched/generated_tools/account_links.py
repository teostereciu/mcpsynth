from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_account_link(
    account: str,
    type: str,
    refresh_url: str,
    return_url: str,
    *,
    collection_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "account": account,
        "type": type,
        "refresh_url": refresh_url,
        "return_url": return_url,
        "collection_options": collection_options,
    }
    _, data = stripe_request(
        "POST",
        "/v1/account_links",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data
