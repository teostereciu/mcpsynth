from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def accounts_create(
    *,
    type: Optional[str] = None,
    country: Optional[str] = None,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    external_account: Optional[str] = None,
    settings: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    account_token: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if type is not None:
        data["type"] = type
    if country is not None:
        data["country"] = country
    if email is not None:
        data["email"] = email
    if business_type is not None:
        data["business_type"] = business_type
    if capabilities is not None:
        data["capabilities"] = capabilities
    if company is not None:
        data["company"] = company
    if individual is not None:
        data["individual"] = individual
    if controller is not None:
        data["controller"] = controller
    if tos_acceptance is not None:
        data["tos_acceptance"] = tos_acceptance
    if business_profile is not None:
        data["business_profile"] = business_profile
    if default_currency is not None:
        data["default_currency"] = default_currency
    if external_account is not None:
        data["external_account"] = external_account
    if settings is not None:
        data["settings"] = settings
    if metadata is not None:
        data["metadata"] = metadata
    if account_token is not None:
        data["account_token"] = account_token
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/accounts",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def accounts_retrieve(*, account_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/accounts/{account_id}", stripe_account=stripe_account)


def accounts_update(
    *,
    account_id: str,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_currency: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if email is not None:
        data["email"] = email
    if business_type is not None:
        data["business_type"] = business_type
    if capabilities is not None:
        data["capabilities"] = capabilities
    if company is not None:
        data["company"] = company
    if individual is not None:
        data["individual"] = individual
    if controller is not None:
        data["controller"] = controller
    if tos_acceptance is not None:
        data["tos_acceptance"] = tos_acceptance
    if business_profile is not None:
        data["business_profile"] = business_profile
    if settings is not None:
        data["settings"] = settings
    if metadata is not None:
        data["metadata"] = metadata
    if default_currency is not None:
        data["default_currency"] = default_currency
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def accounts_delete(*, account_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/accounts/{account_id}", stripe_account=stripe_account)


def accounts_list(
    *,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if created is not None:
        query["created"] = created
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/accounts", params=query, stripe_account=stripe_account)
