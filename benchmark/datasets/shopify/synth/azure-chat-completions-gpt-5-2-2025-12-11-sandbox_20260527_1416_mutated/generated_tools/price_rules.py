from typing import Any, Dict, Optional

from .client import shopify_request


def create_price_rule(price_rule: Dict[str, Any]) -> Any:
    """POST /price_rules.json"""
    return shopify_request("POST", "/price_rules.json", json={"price_rule": price_rule})


def list_price_rules(*, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    """GET /price_rules.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", "/price_rules.json", params=params or None)


def get_price_rule(price_rule_id: int) -> Any:
    """GET /price_rules/{price_rule_id}.json"""
    return shopify_request("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules() -> Any:
    """GET /price_rules/count.json"""
    return shopify_request("GET", "/price_rules/count.json")


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Any:
    """PUT /price_rules/{price_rule_id}.json"""
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return shopify_request("PUT", f"/price_rules/{price_rule_id}.json", json=body)


def delete_price_rule(price_rule_id: int) -> Any:
    """DELETE /price_rules/{price_rule_id}.json"""
    return shopify_request("DELETE", f"/price_rules/{price_rule_id}.json")
