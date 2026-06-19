from typing import Any, Dict, Optional

from .client import request_json


def price_rule_create(price_rule: Dict[str, Any]) -> Any:
    """POST /price_rules.json"""
    return request_json("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def price_rules_list(*, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    """GET /price_rules.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/price_rules.json", params=params or None)


def price_rule_get(price_rule_id: int) -> Any:
    """GET /price_rules/{price_rule_id}.json"""
    return request_json("GET", f"/price_rules/{price_rule_id}.json")


def price_rules_count() -> Any:
    """GET /price_rules/count.json"""
    return request_json("GET", "/price_rules/count.json")


def price_rule_update(price_rule_id: int, price_rule: Dict[str, Any]) -> Any:
    """PUT /price_rules/{price_rule_id}.json"""
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return request_json("PUT", f"/price_rules/{price_rule_id}.json", json_body=body)


def price_rule_delete(price_rule_id: int) -> Any:
    """DELETE /price_rules/{price_rule_id}.json"""
    return request_json("DELETE", f"/price_rules/{price_rule_id}.json")
