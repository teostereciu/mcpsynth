from typing import Any, Dict, List, Optional

from .client import request_json


def discount_code_create(price_rule_id: int, discount_code: Dict[str, Any]) -> Any:
    """POST /price_rules/{price_rule_id}/discount_codes.json"""
    return request_json(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
    )


def discount_codes_list(price_rule_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    """GET /price_rules/{price_rule_id}/discount_codes.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params or None)


def discount_code_get(price_rule_id: int, discount_code_id: int) -> Any:
    """GET /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    return request_json("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def discount_code_update(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Any:
    """PUT /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    body = {"discount_code": {**discount_code, "id": discount_code_id}}
    return request_json("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", json_body=body)


def discount_code_delete(price_rule_id: int, discount_code_id: int) -> Any:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    return request_json("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def discount_codes_count(*, times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Any:
    """GET /discount_codes/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {"times_used": times_used, "times_used_min": times_used_min, "times_used_max": times_used_max}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/discount_codes/count.json", params=params or None)


def discount_code_lookup(code: str) -> Any:
    """GET /discount_codes/lookup.json (deprecated)

    Note: Shopify returns the discount code location in the Location header.
    This helper returns the response JSON if any; otherwise returns text.
    """
    return request_json("GET", "/discount_codes/lookup.json", params={"code": code})


def discount_codes_batch_create(price_rule_id: int, discount_codes: List[Dict[str, Any]]) -> Any:
    """POST /price_rules/{price_rule_id}/batch.json"""
    return request_json(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        json_body={"discount_codes": discount_codes},
    )


def discount_codes_batch_get(price_rule_id: int, batch_id: int) -> Any:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}.json"""
    return request_json("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def discount_codes_batch_list_codes(price_rule_id: int, batch_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json", params=params or None)
