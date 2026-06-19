from typing import Any, Dict, List, Optional

from .client import shopify_request


def create_discount_code(price_rule_id: int, code: str) -> Any:
    """POST /price_rules/{price_rule_id}/discount_codes.json"""
    return shopify_request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json={"discount_code": {"code": code}},
    )


def list_discount_codes(price_rule_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    """GET /price_rules/{price_rule_id}/discount_codes.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params or None)


def get_discount_code(price_rule_id: int, discount_code_id: int) -> Any:
    """GET /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    return shopify_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Any:
    """PUT /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    body = {"discount_code": {**discount_code, "id": discount_code_id}}
    return shopify_request("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", json=body)


def delete_discount_code(price_rule_id: int, discount_code_id: int) -> Any:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    return shopify_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def create_discount_code_batch_job(price_rule_id: int, codes: List[str]) -> Any:
    """POST /price_rules/{price_rule_id}/batch.json"""
    return shopify_request(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        json={"discount_codes": [{"code": c} for c in codes]},
    )


def get_discount_code_batch_job(price_rule_id: int, batch_id: int) -> Any:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}.json"""
    return shopify_request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_codes_for_batch_job(price_rule_id: int, batch_id: int) -> Any:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"""
    return shopify_request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json")


def count_discount_codes(*, times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Any:
    """GET /discount_codes/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {"times_used": times_used, "times_used_min": times_used_min, "times_used_max": times_used_max}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", "/discount_codes/count.json", params=params or None)


def lookup_discount_code_location(code: str) -> Any:
    """GET /discount_codes/lookup.json"""
    return shopify_request("GET", "/discount_codes/lookup.json", params={"code": code})
