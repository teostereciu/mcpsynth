from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def account_get_sales_tax(jurisdiction_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/sales_tax/{jurisdictionId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/account/v1/sales_tax/{jurisdiction_id}")


def account_get_sales_taxes(country_code: Optional[str] = None) -> Dict[str, Any]:
    """GET /sell/account/v1/sales_tax"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if country_code is not None:
        params["country_code"] = country_code
    return c.request("GET", "/sell/account/v1/sales_tax", params=params)


def account_create_or_replace_sales_tax(jurisdiction_id: str, sales_tax: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/account/v1/sales_tax/{jurisdictionId}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/account/v1/sales_tax/{jurisdiction_id}", json=sales_tax)


def account_delete_sales_tax(jurisdiction_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/sales_tax/{jurisdictionId}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/account/v1/sales_tax/{jurisdiction_id}")


def account_get_fulfillment_policies(marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/fulfillment_policy"""
    c = EbayClient()
    return c.request("GET", "/sell/account/v1/fulfillment_policy", params={"marketplace_id": marketplace_id})


def account_get_fulfillment_policy(policy_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/account/v1/fulfillment_policy/{policy_id}")


def account_create_fulfillment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/account/v1/fulfillment_policy"""
    c = EbayClient()
    return c.request("POST", "/sell/account/v1/fulfillment_policy", json=policy)


def account_update_fulfillment_policy(policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/account/v1/fulfillment_policy/{policy_id}", json=policy)


def account_delete_fulfillment_policy(policy_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/account/v1/fulfillment_policy/{policy_id}")


def account_get_payment_policies(marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/payment_policy"""
    c = EbayClient()
    return c.request("GET", "/sell/account/v1/payment_policy", params={"marketplace_id": marketplace_id})


def account_get_payment_policy(policy_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/payment_policy/{paymentPolicyId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/account/v1/payment_policy/{policy_id}")


def account_create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/account/v1/payment_policy"""
    c = EbayClient()
    return c.request("POST", "/sell/account/v1/payment_policy", json=policy)


def account_update_payment_policy(policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/account/v1/payment_policy/{paymentPolicyId}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/account/v1/payment_policy/{policy_id}", json=policy)


def account_delete_payment_policy(policy_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/payment_policy/{paymentPolicyId}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/account/v1/payment_policy/{policy_id}")


def account_get_return_policies(marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/return_policy"""
    c = EbayClient()
    return c.request("GET", "/sell/account/v1/return_policy", params={"marketplace_id": marketplace_id})


def account_get_return_policy(policy_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/return_policy/{returnPolicyId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/account/v1/return_policy/{policy_id}")


def account_create_return_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/account/v1/return_policy"""
    c = EbayClient()
    return c.request("POST", "/sell/account/v1/return_policy", json=policy)


def account_update_return_policy(policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/account/v1/return_policy/{returnPolicyId}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/account/v1/return_policy/{policy_id}", json=policy)


def account_delete_return_policy(policy_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/return_policy/{returnPolicyId}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/account/v1/return_policy/{policy_id}")


def account_get_shipping_policies(marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/shipping_policy"""
    c = EbayClient()
    return c.request("GET", "/sell/account/v1/shipping_policy", params={"marketplace_id": marketplace_id})


def account_get_shipping_policy(policy_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/shipping_policy/{shippingPolicyId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/account/v1/shipping_policy/{policy_id}")


def account_create_shipping_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/account/v1/shipping_policy"""
    c = EbayClient()
    return c.request("POST", "/sell/account/v1/shipping_policy", json=policy)


def account_update_shipping_policy(policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/account/v1/shipping_policy/{shippingPolicyId}"""
    c = EbayClient()
    return c.request("PUT", f"/sell/account/v1/shipping_policy/{policy_id}", json=policy)


def account_delete_shipping_policy(policy_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/shipping_policy/{shippingPolicyId}"""
    c = EbayClient()
    return c.request("DELETE", f"/sell/account/v1/shipping_policy/{policy_id}")
