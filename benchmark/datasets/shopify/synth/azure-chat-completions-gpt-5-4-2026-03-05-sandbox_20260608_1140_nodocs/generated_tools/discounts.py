from typing import Any, Dict, Optional

from generated_tools.common import clean_params, shopify_request


def list_price_rules(limit: Optional[int] = None, page_info: Optional[str] = None) -> Any:
    params = clean_params(limit=limit, page_info=page_info)
    return shopify_request("GET", "/price_rules.json", params=params)


def get_price_rule(price_rule_id: int) -> Any:
    return shopify_request("GET", f"/price_rules/{price_rule_id}.json")


def create_price_rule(price_rule: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Any:
    body = {"price_rule": {"id": price_rule_id, **price_rule}}
    return shopify_request("PUT", f"/price_rules/{price_rule_id}.json", json_body=body)


def delete_price_rule(price_rule_id: int) -> Any:
    return shopify_request("DELETE", f"/price_rules/{price_rule_id}.json")


def list_discount_codes(price_rule_id: int) -> Any:
    return shopify_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json")


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json_body={"discount_code": discount_code})
