from typing import Any, Dict, Optional

from .ebay_client import EbayClient, omit_none


client = EbayClient()


def account_get_sales_tax(jurisdiction_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/sales_tax/{jurisdiction_id}")


def account_get_sales_taxes(country_code: Optional[str] = None) -> Dict[str, Any]:
    params = omit_none({"country_code": country_code})
    return client.request("GET", "/sell/account/v1/sales_tax", params=params)


def account_create_or_replace_sales_tax(jurisdiction_id: str, sales_tax: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/account/v1/sales_tax/{jurisdiction_id}", json_body=sales_tax)


def account_delete_sales_tax(jurisdiction_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/sales_tax/{jurisdiction_id}")


def account_get_fulfillment_policies(marketplace_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    params = omit_none({"marketplace_id": marketplace_id, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/account/v1/fulfillment_policy", params=params)


def account_get_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


def account_create_fulfillment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/account/v1/fulfillment_policy", json_body=policy)


def account_update_fulfillment_policy(fulfillment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}", json_body=policy)


def account_delete_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


def account_get_payment_policies(marketplace_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    params = omit_none({"marketplace_id": marketplace_id, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/account/v1/payment_policy", params=params)


def account_get_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def account_create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/account/v1/payment_policy", json_body=policy)


def account_update_payment_policy(payment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/account/v1/payment_policy/{payment_policy_id}", json_body=policy)


def account_delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def account_get_return_policies(marketplace_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    params = omit_none({"marketplace_id": marketplace_id, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/account/v1/return_policy", params=params)


def account_get_return_policy(return_policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/return_policy/{return_policy_id}")


def account_create_return_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/account/v1/return_policy", json_body=policy)


def account_update_return_policy(return_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/account/v1/return_policy/{return_policy_id}", json_body=policy)


def account_delete_return_policy(return_policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/return_policy/{return_policy_id}")
