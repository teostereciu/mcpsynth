from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_payment_policies(*, marketplace_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    """GET /payment_policy"""
    client = EbayClient()
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(
        "GET",
        "/sell/account/v1/payment_policy",
        params={"marketplace_id": marketplace_id},
        headers=headers,
    )


def get_payment_policy(payment_policy_id: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
    """GET /payment_policy/{payment_policy_id}"""
    client = EbayClient()
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(
        "GET",
        f"/sell/account/v1/payment_policy/{payment_policy_id}",
        headers=headers,
    )


def create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /payment_policy"""
    client = EbayClient()
    return client.request(
        "POST",
        "/sell/account/v1/payment_policy",
        json=policy,
        content_type="application/json",
    )


def update_payment_policy(payment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /payment_policy/{payment_policy_id}"""
    client = EbayClient()
    return client.request(
        "PUT",
        f"/sell/account/v1/payment_policy/{payment_policy_id}",
        json=policy,
        content_type="application/json",
    )


def delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    """DELETE /payment_policy/{payment_policy_id}"""
    client = EbayClient()
    return client.request("DELETE", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def get_fulfillment_policies(*, marketplace_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    """GET /fulfillment_policy"""
    client = EbayClient()
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(
        "GET",
        "/sell/account/v1/fulfillment_policy",
        params={"marketplace_id": marketplace_id},
        headers=headers,
    )


def get_fulfillment_policy(fulfillment_policy_id: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
    """GET /fulfillment_policy/{fulfillmentPolicyId}"""
    client = EbayClient()
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(
        "GET",
        f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}",
        headers=headers,
    )


def create_fulfillment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /fulfillment_policy/"""
    client = EbayClient()
    return client.request(
        "POST",
        "/sell/account/v1/fulfillment_policy/",
        json=policy,
        content_type="application/json",
    )


def update_fulfillment_policy(fulfillment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /fulfillment_policy/{fulfillmentPolicyId}"""
    client = EbayClient()
    return client.request(
        "PUT",
        f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}",
        json=policy,
        content_type="application/json",
    )


def delete_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    """DELETE /fulfillment_policy/{fulfillmentPolicyId}"""
    client = EbayClient()
    return client.request("DELETE", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


def get_return_policies(*, marketplace_id: str, content_language: Optional[str] = None) -> Dict[str, Any]:
    """GET /return_policy"""
    client = EbayClient()
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(
        "GET",
        "/sell/account/v1/return_policy",
        params={"marketplace_id": marketplace_id},
        headers=headers,
    )


def get_return_policy(return_policy_id: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
    """GET /return_policy/{return_policy_id}"""
    client = EbayClient()
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(
        "GET",
        f"/sell/account/v1/return_policy/{return_policy_id}",
        headers=headers,
    )


def create_return_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /return_policy"""
    client = EbayClient()
    return client.request(
        "POST",
        "/sell/account/v1/return_policy",
        json=policy,
        content_type="application/json",
    )


def update_return_policy(return_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /return_policy/{return_policy_id}"""
    client = EbayClient()
    return client.request(
        "PUT",
        f"/sell/account/v1/return_policy/{return_policy_id}",
        json=policy,
        content_type="application/json",
    )


def delete_return_policy(return_policy_id: str) -> Dict[str, Any]:
    """DELETE /return_policy/{return_policy_id}"""
    client = EbayClient()
    return client.request("DELETE", f"/sell/account/v1/return_policy/{return_policy_id}")


def get_sales_taxes(*, marketplace_id: str) -> Dict[str, Any]:
    """GET /sales_tax"""
    client = EbayClient()
    return client.request(
        "GET",
        "/sell/account/v1/sales_tax",
        params={"marketplace_id": marketplace_id},
    )


def get_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    """GET /sales_tax/{countryCode}/{jurisdictionId}"""
    client = EbayClient()
    return client.request(
        "GET",
        f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}",
    )


def create_or_replace_sales_tax(country_code: str, jurisdiction_id: str, sales_tax: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sales_tax/{countryCode}/{jurisdictionId}"""
    client = EbayClient()
    return client.request(
        "PUT",
        f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}",
        json=sales_tax,
        content_type="application/json",
    )


def delete_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    """DELETE /sales_tax/{countryCode}/{jurisdictionId}"""
    client = EbayClient()
    return client.request(
        "DELETE",
        f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}",
    )


def get_privileges() -> Dict[str, Any]:
    """GET /privilege"""
    client = EbayClient()
    return client.request("GET", "/sell/account/v1/privilege")


def get_opted_in_programs() -> Dict[str, Any]:
    """GET /program/get_opted_in_programs"""
    client = EbayClient()
    return client.request("GET", "/sell/account/v1/program/get_opted_in_programs")
