from typing import Any, Dict, Optional

from .http_client import stripe_list_all, stripe_request


def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    source_transaction: Optional[str] = None,
    source_type: Optional[str] = None,
    transfer_group: Optional[str] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount": amount, "currency": currency, "destination": destination}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if source_transaction is not None:
        params["source_transaction"] = source_transaction
    if source_type is not None:
        params["source_type"] = source_type
    if transfer_group is not None:
        params["transfer_group"] = transfer_group

    return stripe_request("POST", "/v1/transfers", params=params, account=account, idempotency_key=idempotency_key)


def retrieve_transfer(transfer_id: str, *, account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/transfers/{transfer_id}", params={}, account=account)


def update_transfer(
    transfer_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def list_transfers(
    *,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    account: Optional[str] = None,
    auto_paginate: bool = False,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if destination is not None:
        params["destination"] = destination
    if transfer_group is not None:
        params["transfer_group"] = transfer_group
    if created is not None:
        params["created"] = created
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    if auto_paginate:
        return stripe_list_all("/v1/transfers", params=params, account=account, max_pages=max_pages)
    return stripe_request("GET", "/v1/transfers", params=params, account=account)
