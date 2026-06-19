from typing import Any, Dict, Optional

from .client import request_json


# Price rules

def list_price_rules(*, limit: int = 50) -> Any:
    return request_json("GET", "/price_rules.json", params={"limit": limit})


def get_price_rule(price_rule_id: int) -> Any:
    return request_json("GET", f"/price_rules/{price_rule_id}.json")


def create_price_rule(price_rule: Dict[str, Any]) -> Any:
    return request_json("POST", "/price_rules.json", json={"price_rule": price_rule})


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/price_rules/{price_rule_id}.json", json={"price_rule": price_rule})


def delete_price_rule(price_rule_id: int) -> Any:
    return request_json("DELETE", f"/price_rules/{price_rule_id}.json")


# Discount codes

def list_discount_codes(price_rule_id: int, *, limit: int = 50) -> Any:
    return request_json("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params={"limit": limit})


def get_discount_code(price_rule_id: int, discount_code_id: int) -> Any:
    return request_json("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]) -> Any:
    return request_json("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json={"discount_code": discount_code})


def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Any:
    return request_json(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json={"discount_code": discount_code},
    )


def delete_discount_code(price_rule_id: int, discount_code_id: int) -> Any:
    return request_json("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
