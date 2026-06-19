from typing import Any, Dict, Optional

from .http import stripe_request

# Accounts

def accounts_create(
    *,
    type: str,
    country: Optional[str] = None,
    email: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    business_type: Optional[str] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "type": type,
        "country": country,
        "email": email,
        "capabilities": capabilities,
        "business_type": business_type,
        "business_profile": business_profile,
        "company": company,
        "individual": individual,
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
    }
    data.update(extra)
    result, err = stripe_request("POST", "/v1/accounts", data=data, stripe_account=stripe_account, idempotency_key=idempotency_key)
    return err or result  # type: ignore[return-value]


def accounts_retrieve(*, account_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/accounts/{account_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def accounts_update(
    *,
    account_id: str,
    metadata: Optional[Dict[str, str]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "metadata": metadata,
        "business_profile": business_profile,
        "company": company,
        "individual": individual,
        "capabilities": capabilities,
        "settings": settings,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def accounts_list(
    *,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    result, err = stripe_request("GET", "/v1/accounts", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


# Transfers

def transfers_create(
    *,
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    transfer_group: Optional[str] = None,
    source_transaction: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "description": description,
        "metadata": metadata,
        "transfer_group": transfer_group,
        "source_transaction": source_transaction,
    }
    data.update(extra)
    result, err = stripe_request("POST", "/v1/transfers", data=data, stripe_account=stripe_account, idempotency_key=idempotency_key)
    return err or result  # type: ignore[return-value]


def transfers_retrieve(*, transfer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/transfers/{transfer_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def transfers_list(
    *,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "destination": destination,
        "transfer_group": transfer_group,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    result, err = stripe_request("GET", "/v1/transfers", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


# Payouts

def payouts_create(
    *,
    amount: int,
    currency: str,
    description: Optional[str] = None,
    method: Optional[str] = None,
    destination: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "description": description,
        "method": method,
        "destination": destination,
        "metadata": metadata,
        "statement_descriptor": statement_descriptor,
    }
    data.update(extra)
    result, err = stripe_request("POST", "/v1/payouts", data=data, stripe_account=stripe_account, idempotency_key=idempotency_key)
    return err or result  # type: ignore[return-value]


def payouts_retrieve(*, payout_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def payouts_list(
    *,
    status: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"status": status, "limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    result, err = stripe_request("GET", "/v1/payouts", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]
