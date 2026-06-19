from typing import Any, Dict, Optional

from .http import stripe_request


def accounts_create(
    type: str = "express",
    country: Optional[str] = None,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    external_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "type": type,
        "country": country,
        "email": email,
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
        "settings": settings,
        "external_account": external_account,
    }
    data, err = stripe_request("POST", "/v1/accounts", params=params, idempotency_key=idempotency_key)
    return data or err  # type: ignore[return-value]


def accounts_retrieve(account_id: str) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/accounts/{account_id}")
    return data or err  # type: ignore[return-value]


def accounts_update(
    account_id: str,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    external_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "email": email,
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
        "settings": settings,
        "external_account": external_account,
    }
    data, err = stripe_request("POST", f"/v1/accounts/{account_id}", params=params, idempotency_key=idempotency_key)
    return data or err  # type: ignore[return-value]


def accounts_list(limit: int = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None) -> Dict[str, Any]:
    params = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    data, err = stripe_request("GET", "/v1/accounts", params=params)
    return data or err  # type: ignore[return-value]


def account_links_create(
    account: str,
    refresh_url: str,
    return_url: str,
    type: str = "account_onboarding",
    collect: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "account": account,
        "refresh_url": refresh_url,
        "return_url": return_url,
        "type": type,
        "collect": collect,
    }
    data, err = stripe_request("POST", "/v1/account_links", params=params, idempotency_key=idempotency_key)
    return data or err  # type: ignore[return-value]


def transfers_create(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    source_transaction: Optional[str] = None,
    transfer_group: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "description": description,
        "metadata": metadata,
        "source_transaction": source_transaction,
        "transfer_group": transfer_group,
    }
    data, err = stripe_request("POST", "/v1/transfers", params=params, idempotency_key=idempotency_key)
    return data or err  # type: ignore[return-value]


def transfers_retrieve(transfer_id: str) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/transfers/{transfer_id}")
    return data or err  # type: ignore[return-value]


def transfers_list(limit: int = 10, destination: Optional[str] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None) -> Dict[str, Any]:
    params = {"limit": limit, "destination": destination, "starting_after": starting_after, "ending_before": ending_before}
    data, err = stripe_request("GET", "/v1/transfers", params=params)
    return data or err  # type: ignore[return-value]


def payouts_create(
    amount: int,
    currency: str,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "method": method,
        "description": description,
        "metadata": metadata,
        "statement_descriptor": statement_descriptor,
    }
    data, err = stripe_request(
        "POST",
        "/v1/payouts",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def payouts_retrieve(payout_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def payouts_cancel(payout_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    data, err = stripe_request("POST", f"/v1/payouts/{payout_id}/cancel", stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]


def payouts_reverse(
    payout_id: str,
    amount: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"amount": amount, "metadata": metadata}
    data, err = stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return data or err  # type: ignore[return-value]


def payouts_list(limit: int = 10, status: Optional[str] = None, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    params = {"limit": limit, "status": status, "starting_after": starting_after, "ending_before": ending_before}
    data, err = stripe_request("GET", "/v1/payouts", params=params, stripe_account=stripe_account)
    return data or err  # type: ignore[return-value]
