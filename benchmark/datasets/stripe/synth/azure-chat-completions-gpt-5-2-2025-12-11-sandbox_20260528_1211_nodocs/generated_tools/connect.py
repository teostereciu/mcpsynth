from typing import Any, Dict, Optional

from .http import stripe_request


def create_account(
    *,
    type: str = "express",
    country: Optional[str] = None,
    email: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    business_type: Optional[str] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"type": type}
    if country is not None:
        data["country"] = country
    if email is not None:
        data["email"] = email
    if capabilities is not None:
        data["capabilities"] = capabilities
    if business_type is not None:
        data["business_type"] = business_type
    if company is not None:
        data["company"] = company
    if individual is not None:
        data["individual"] = individual
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request(
        "POST",
        "/v1/accounts",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_account(account_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/accounts/{account_id}", stripe_account=stripe_account)
    return res if err is None else err


def update_account(
    account_id: str,
    *,
    email: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if email is not None:
        data["email"] = email
    if capabilities is not None:
        data["capabilities"] = capabilities
    if company is not None:
        data["company"] = company
    if individual is not None:
        data["individual"] = individual
    if metadata is not None:
        data["metadata"] = metadata

    res, err = stripe_request("POST", f"/v1/accounts/{account_id}", data=data, stripe_account=stripe_account)
    return res if err is None else err


def list_accounts(
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/accounts", query=query, stripe_account=stripe_account)
    return res if err is None else err


def create_account_link(
    *,
    account: str,
    refresh_url: str,
    return_url: str,
    type: str = "account_onboarding",
    collect: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "account": account,
        "refresh_url": refresh_url,
        "return_url": return_url,
        "type": type,
    }
    if collect is not None:
        data["collect"] = collect

    res, err = stripe_request(
        "POST",
        "/v1/account_links",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def create_transfer(
    amount: int,
    currency: str,
    *,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    transfer_group: Optional[str] = None,
    source_transaction: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
    }
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if transfer_group is not None:
        data["transfer_group"] = transfer_group
    if source_transaction is not None:
        data["source_transaction"] = source_transaction

    res, err = stripe_request(
        "POST",
        "/v1/transfers",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_transfer(transfer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/transfers/{transfer_id}", stripe_account=stripe_account)
    return res if err is None else err


def list_transfers(
    *,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if destination is not None:
        query["destination"] = destination
    if transfer_group is not None:
        query["transfer_group"] = transfer_group
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before

    res, err = stripe_request("GET", "/v1/transfers", query=query, stripe_account=stripe_account)
    return res if err is None else err


def create_payout(
    amount: int,
    currency: str,
    *,
    description: Optional[str] = None,
    method: Optional[str] = None,
    destination: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency}
    if description is not None:
        data["description"] = description
    if method is not None:
        data["method"] = method
    if destination is not None:
        data["destination"] = destination
    if metadata is not None:
        data["metadata"] = metadata
    if statement_descriptor is not None:
        data["statement_descriptor"] = statement_descriptor

    res, err = stripe_request(
        "POST",
        "/v1/payouts",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err


def retrieve_payout(payout_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)
    return res if err is None else err


def cancel_payout(payout_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/payouts/{payout_id}/cancel", data={}, stripe_account=stripe_account)
    return res if err is None else err


def reverse_transfer(
    transfer_id: str,
    *,
    amount: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    refund_application_fee: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if amount is not None:
        data["amount"] = amount
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if refund_application_fee is not None:
        data["refund_application_fee"] = refund_application_fee

    res, err = stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}/reversals",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return res if err is None else err
