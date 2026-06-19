from typing import Any, Dict, Optional

from generated_tools.common import shopify_request


def create_price_rule(price_rule: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def list_price_rules(limit: Optional[int] = None, fields: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"limit": limit, "fields": fields}.items() if v is not None}
    return shopify_request("GET", "/price_rules.json", params=params)


def get_price_rule(price_rule_id: int) -> Any:
    return shopify_request("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules() -> Any:
    return shopify_request("GET", "/price_rules/count.json")


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Any:
    payload = dict(price_rule)
    payload.setdefault("id", price_rule_id)
    return shopify_request("PUT", f"/price_rules/{price_rule_id}.json", json_body={"price_rule": payload})


def delete_price_rule(price_rule_id: int) -> Any:
    return shopify_request("DELETE", f"/price_rules/{price_rule_id}.json")


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json_body={"discount_code": discount_code})


def create_discount_code_batch(price_rule_id: int, discount_codes: list[Dict[str, Any]]) -> Any:
    return shopify_request("POST", f"/price_rules/{price_rule_id}/batch.json", json_body={"discount_codes": discount_codes})


def get_discount_code_batch(price_rule_id: int, batch_id: int) -> Any:
    return shopify_request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_code_batch_codes(price_rule_id: int, batch_id: int) -> Any:
    return shopify_request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json")


def list_discount_codes(price_rule_id: int, limit: Optional[int] = None) -> Any:
    params = {"limit": limit} if limit is not None else None
    return shopify_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


def get_discount_code(price_rule_id: int, discount_code_id: int) -> Any:
    return shopify_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Any:
    payload = dict(discount_code)
    payload.setdefault("id", discount_code_id)
    return shopify_request("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", json_body={"discount_code": payload})


def delete_discount_code(price_rule_id: int, discount_code_id: int) -> Any:
    return shopify_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def count_discount_codes(times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"times_used": times_used, "times_used_min": times_used_min, "times_used_max": times_used_max}.items() if v is not None}
    return shopify_request("GET", "/discount_codes/count.json", params=params)


def lookup_discount_code(code: str) -> Any:
    return shopify_request("GET", "/discount_codes/lookup.json", params={"code": code})
