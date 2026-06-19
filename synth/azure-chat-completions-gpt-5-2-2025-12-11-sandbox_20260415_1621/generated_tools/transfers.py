from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def transfers_create(
    *,
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    source_transaction: Optional[str] = None,
    source_type: Optional[str] = None,
    transfer_group: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency, "destination": destination}
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if source_transaction is not None:
        data["source_transaction"] = source_transaction
    if source_type is not None:
        data["source_type"] = source_type
    if transfer_group is not None:
        data["transfer_group"] = transfer_group
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/transfers",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def transfers_retrieve(*, transfer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/transfers/{transfer_id}", stripe_account=stripe_account)


def transfers_update(
    *,
    transfer_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def transfers_list(
    *,
    limit: Optional[int] = 10,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if destination is not None:
        query["destination"] = destination
    if transfer_group is not None:
        query["transfer_group"] = transfer_group
    if created is not None:
        query["created"] = created
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/transfers", params=query, stripe_account=stripe_account)
