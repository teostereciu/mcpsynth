from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def accounts_create(
    *,
    type: str = "express",
    country: Optional[str] = None,
    email: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "type": type,
        "country": country,
        "email": email,
        "capabilities": capabilities,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/accounts", params=params, stripe_account=stripe_account)


def accounts_retrieve(*, account_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/accounts/{account_id}", stripe_account=stripe_account)


def accounts_update(
    *,
    account_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata, "business_profile": business_profile}
    return stripe_request("POST", f"/v1/accounts/{account_id}", params=params, stripe_account=stripe_account)


def accounts_list(
    *,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    return stripe_request("GET", "/v1/accounts", params=params, stripe_account=stripe_account)


def account_links_create(
    *,
    account: str,
    refresh_url: str,
    return_url: str,
    type: str = "account_onboarding",
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"account": account, "refresh_url": refresh_url, "return_url": return_url, "type": type}
    return stripe_request("POST", "/v1/account_links", params=params, stripe_account=stripe_account)
