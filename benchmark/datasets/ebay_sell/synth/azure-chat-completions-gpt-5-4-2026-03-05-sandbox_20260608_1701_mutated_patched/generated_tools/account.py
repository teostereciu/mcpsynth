from typing import Any, Optional

from generated_tools.common import client, compact_kwargs, parse_json_body


API_BASE = "/sell/account/v1"


def get_payment_policies(market_id: str, content_language: Optional[str] = None) -> Any:
    try:
        headers = {"Content-Language": content_language} if content_language else None
        return client.request(API_BASE, "GET", "/payment_policy", params={"marketplace_id": market_id}, headers=headers)
    except Exception as e:
        return {"error": str(e)}


def get_payment_policy(payment_policy_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/payment_policy/{payment_policy_id}")
    except Exception as e:
        return {"error": str(e)}


def get_payment_policy_by_name(marketplace_id: str, name: str) -> Any:
    try:
        return client.request(API_BASE, "GET", "/payment_policy/get_by_policy_name", params={"marketplace_id": marketplace_id, "name": name})
    except Exception as e:
        return {"error": str(e)}


def create_payment_policy(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/payment_policy", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def update_payment_policy(payment_policy_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "PUT", f"/payment_policy/{payment_policy_id}", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def delete_payment_policy(payment_policy_id: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/payment_policy/{payment_policy_id}")
    except Exception as e:
        return {"error": str(e)}


def get_fulfillment_policies(marketplace_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", "/fulfillment_policy", params={"marketplace_id": marketplace_id})
    except Exception as e:
        return {"error": str(e)}


def get_fulfillment_policy(fulfillment_policy_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/fulfillment_policy/{fulfillment_policy_id}")
    except Exception as e:
        return {"error": str(e)}


def get_fulfillment_policy_by_name(marketplace_id: str, name: str) -> Any:
    try:
        return client.request(API_BASE, "GET", "/fulfillment_policy/get_by_policy_name", params={"marketplace_id": marketplace_id, "name": name})
    except Exception as e:
        return {"error": str(e)}


def create_fulfillment_policy(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/fulfillment_policy/", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def update_fulfillment_policy(fulfillment_policy_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "PUT", f"/fulfillment_policy/{fulfillment_policy_id}", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def delete_fulfillment_policy(fulfillment_policy_id: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/fulfillment_policy/{fulfillment_policy_id}")
    except Exception as e:
        return {"error": str(e)}


def get_return_policies(marketplace_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", "/return_policy", params={"marketplace_id": marketplace_id})
    except Exception as e:
        return {"error": str(e)}


def get_return_policy(return_policy_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/return_policy/{return_policy_id}")
    except Exception as e:
        return {"error": str(e)}


def get_return_policy_by_name(marketplace_id: str, name: str) -> Any:
    try:
        return client.request(API_BASE, "GET", "/return_policy/get_by_policy_name", params={"marketplace_id": marketplace_id, "name": name})
    except Exception as e:
        return {"error": str(e)}


def create_return_policy(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/return_policy", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def update_return_policy(return_policy_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "PUT", f"/return_policy/{return_policy_id}", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def delete_return_policy(return_policy_id: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/return_policy/{return_policy_id}")
    except Exception as e:
        return {"error": str(e)}


def get_privileges() -> Any:
    try:
        return client.request(API_BASE, "GET", "/privilege")
    except Exception as e:
        return {"error": str(e)}


def get_rate_tables(marketplace_id: Optional[str] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/rate_table", params=compact_kwargs(marketplace_id=marketplace_id))
    except Exception as e:
        return {"error": str(e)}


def get_subscription() -> Any:
    try:
        return client.request(API_BASE, "GET", "/subscription")
    except Exception as e:
        return {"error": str(e)}


def get_opted_in_programs() -> Any:
    try:
        return client.request(API_BASE, "GET", "/program/get_opted_in_programs")
    except Exception as e:
        return {"error": str(e)}


def opt_in_to_program(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/program/opt_in", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def opt_out_of_program(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/program/opt_out", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}
