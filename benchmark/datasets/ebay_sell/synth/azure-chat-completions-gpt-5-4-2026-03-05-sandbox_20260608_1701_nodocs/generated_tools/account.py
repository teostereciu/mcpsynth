from typing import Any, Dict, Optional

from .common import client


def list_payment_policies(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return client.request("GET", "/sell/account/v1/payment_policy", params={"marketplace_id": marketplace_id})


def get_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def create_payment_policy(data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/account/v1/payment_policy", json_body=data)


def update_payment_policy(payment_policy_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/account/v1/payment_policy/{payment_policy_id}", json_body=data)


def delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def list_return_policies(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return client.request("GET", "/sell/account/v1/return_policy", params={"marketplace_id": marketplace_id})


def get_return_policy(return_policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/return_policy/{return_policy_id}")


def create_return_policy(data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/account/v1/return_policy", json_body=data)


def update_return_policy(return_policy_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/account/v1/return_policy/{return_policy_id}", json_body=data)


def delete_return_policy(return_policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/return_policy/{return_policy_id}")


def list_fulfillment_policies(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return client.request("GET", "/sell/account/v1/fulfillment_policy", params={"marketplace_id": marketplace_id})


def get_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


def create_fulfillment_policy(data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/account/v1/fulfillment_policy", json_body=data)


def update_fulfillment_policy(fulfillment_policy_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}", json_body=data)


def delete_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")
