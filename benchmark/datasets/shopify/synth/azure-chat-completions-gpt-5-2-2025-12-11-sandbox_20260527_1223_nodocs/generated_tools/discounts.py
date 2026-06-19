from typing import Any, Dict, Optional

from .client import shopify_request


def list_price_rules(*, limit: int = 50, since_id: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    return shopify_request("GET", "/price_rules.json", params=params)


def get_price_rule(*, price_rule_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/price_rules/{price_rule_id}.json")


def create_price_rule(*, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def update_price_rule(*, price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return shopify_request("PUT", f"/price_rules/{price_rule_id}.json", json_body=body)


def delete_price_rule(*, price_rule_id: int) -> Dict[str, Any]:
    return shopify_request("DELETE", f"/price_rules/{price_rule_id}.json")


def list_discount_codes(*, price_rule_id: int, limit: int = 50) -> Dict[str, Any]:
    return shopify_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params={"limit": limit})


def create_discount_code(*, price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
    )


def delete_discount_code(*, price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    return shopify_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
