from typing import Any, Dict, Optional

from .http import stripe_get, stripe_post


def accounts_create(
    *,
    type: str = "express",
    country: Optional[str] = None,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "type": type,
        "country": country,
        "email": email,
        "business_type": business_type,
        "capabilities": capabilities,
        "company": company,
        "individual": individual,
        "metadata": metadata,
        "tos_acceptance": tos_acceptance,
    }
    res, err = stripe_post("/v1/accounts", data=data, idempotency_key=idempotency_key)
    return err or res


def accounts_retrieve(*, account_id: str):
    res, err = stripe_get(f"/v1/accounts/{account_id}")
    return err or res


def accounts_update(*, account_id: str, data: Dict[str, Any], idempotency_key: Optional[str] = None):
    res, err = stripe_post(f"/v1/accounts/{account_id}", data=data, idempotency_key=idempotency_key)
    return err or res


def account_links_create(
    *,
    account: str,
    refresh_url: str,
    return_url: str,
    type: str = "account_onboarding",
    collect: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "account": account,
        "refresh_url": refresh_url,
        "return_url": return_url,
        "type": type,
        "collect": collect,
    }
    res, err = stripe_post("/v1/account_links", data=data, idempotency_key=idempotency_key)
    return err or res


def transfers_create(
    *,
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    source_transaction: Optional[str] = None,
    transfer_group: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "description": description,
        "metadata": metadata,
        "source_transaction": source_transaction,
        "transfer_group": transfer_group,
    }
    res, err = stripe_post("/v1/transfers", data=data, idempotency_key=idempotency_key)
    return err or res


def transfers_retrieve(*, transfer_id: str):
    res, err = stripe_get(f"/v1/transfers/{transfer_id}")
    return err or res


def transfers_list(*, limit: int = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None):
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    res, err = stripe_get("/v1/transfers", params=params)
    return err or res


def payouts_create(
    *,
    amount: int,
    currency: str,
    description: Optional[str] = None,
    method: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    data: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "description": description,
        "method": method,
        "metadata": metadata,
        "statement_descriptor": statement_descriptor,
        "destination": destination,
    }
    res, err = stripe_post(
        "/v1/payouts",
        data=data,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
    return err or res


def payouts_retrieve(*, payout_id: str, stripe_account: Optional[str] = None):
    res, err = stripe_get(f"/v1/payouts/{payout_id}", stripe_account=stripe_account)
    return err or res


def payouts_list(
    *,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    res, err = stripe_get("/v1/payouts", params=params, stripe_account=stripe_account)
    return err or res
