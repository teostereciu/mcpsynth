from typing import Any, Dict, Optional

from .http_client import stripe_list_all, stripe_request


def create_account(
    *,
    type: Optional[str] = None,
    country: Optional[str] = None,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    external_account: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    account_token: Optional[str] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if type is not None:
        params["type"] = type
    if country is not None:
        params["country"] = country
    if email is not None:
        params["email"] = email
    if business_type is not None:
        params["business_type"] = business_type
    if capabilities is not None:
        params["capabilities"] = capabilities
    if company is not None:
        params["company"] = company
    if individual is not None:
        params["individual"] = individual
    if controller is not None:
        params["controller"] = controller
    if business_profile is not None:
        params["business_profile"] = business_profile
    if default_currency is not None:
        params["default_currency"] = default_currency
    if external_account is not None:
        params["external_account"] = external_account
    if metadata is not None:
        params["metadata"] = metadata
    if tos_acceptance is not None:
        params["tos_acceptance"] = tos_acceptance
    if settings is not None:
        params["settings"] = settings
    if account_token is not None:
        params["account_token"] = account_token

    return stripe_request("POST", "/v1/accounts", params=params, account=account, idempotency_key=idempotency_key)


def retrieve_account(account_id: str, *, account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/accounts/{account_id}", params={}, account=account)


def update_account(
    account_id: str,
    *,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    settings: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if business_type is not None:
        params["business_type"] = business_type
    if capabilities is not None:
        params["capabilities"] = capabilities
    if company is not None:
        params["company"] = company
    if individual is not None:
        params["individual"] = individual
    if business_profile is not None:
        params["business_profile"] = business_profile
    if default_currency is not None:
        params["default_currency"] = default_currency
    if email is not None:
        params["email"] = email
    if metadata is not None:
        params["metadata"] = metadata
    if settings is not None:
        params["settings"] = settings
    if tos_acceptance is not None:
        params["tos_acceptance"] = tos_acceptance

    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        params=params,
        account=account,
        idempotency_key=idempotency_key,
    )


def delete_account(account_id: str, *, account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/accounts/{account_id}", params={}, account=account)


def list_accounts(
    *,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    account: Optional[str] = None,
    auto_paginate: bool = False,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if created is not None:
        params["created"] = created
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before

    if auto_paginate:
        return stripe_list_all("/v1/accounts", params=params, account=account, max_pages=max_pages)
    return stripe_request("GET", "/v1/accounts", params=params, account=account)
