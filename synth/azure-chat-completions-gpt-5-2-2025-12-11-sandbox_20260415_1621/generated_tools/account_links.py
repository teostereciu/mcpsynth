from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def account_links_create(
    *,
    account: str,
    refresh_url: str,
    return_url: str,
    type: str,
    collection_options: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "account": account,
        "refresh_url": refresh_url,
        "return_url": return_url,
        "type": type,
    }
    if collection_options is not None:
        data["collection_options"] = collection_options
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/account_links",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
