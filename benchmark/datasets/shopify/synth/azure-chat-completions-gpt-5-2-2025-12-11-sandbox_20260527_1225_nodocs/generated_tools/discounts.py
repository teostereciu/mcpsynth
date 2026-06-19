from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_price_rules(limit: int = 50) -> Dict[str, Any]:
    """GET /price_rules.json"""
    client = ShopifyClient()
    return client.request("GET", "/price_rules.json", params={"limit": limit})


def get_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}.json")


def create_price_rule(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules.json"""
    client = ShopifyClient()
    return client.request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}.json"""
    client = ShopifyClient()
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return client.request("PUT", f"/price_rules/{price_rule_id}.json", json_body=body)


def delete_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/price_rules/{price_rule_id}.json")


def list_discount_codes(price_rule_id: int, limit: int = 50) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes.json"""
    client = ShopifyClient()
    return client.request(
        "GET",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        params={"limit": limit},
    )


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/discount_codes.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
    )


def delete_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = ShopifyClient()
    return client.request(
        "DELETE",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
    )
