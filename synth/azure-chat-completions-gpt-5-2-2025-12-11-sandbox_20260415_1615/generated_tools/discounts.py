from typing import Any, Dict, Optional

from .http_client import get_client


def price_rule_create(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules.json"""
    return get_client().request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def price_rules_list(*, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /price_rules.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", "/price_rules.json", params=params or None)


def price_rule_get(price_rule_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}.json"""
    return get_client().request("GET", f"/price_rules/{price_rule_id}.json")


def price_rules_count() -> Dict[str, Any]:
    """GET /price_rules/count.json"""
    return get_client().request("GET", "/price_rules/count.json")


def price_rule_update(price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}.json"""
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return get_client().request("PUT", f"/price_rules/{price_rule_id}.json", json_body=body)


def price_rule_delete(price_rule_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}.json"""
    return get_client().request("DELETE", f"/price_rules/{price_rule_id}.json")


def discount_code_create(price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/discount_codes.json"""
    return get_client().request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
    )


def discount_codes_list(price_rule_id: int, *, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes.json"""
    params = {"limit": limit} if limit is not None else None
    return get_client().request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


def discount_code_get(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    return get_client().request(
        "GET",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
    )


def discount_code_update(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    body = {"discount_code": {**discount_code, "id": discount_code_id}}
    return get_client().request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json_body=body,
    )


def discount_code_delete(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    return get_client().request(
        "DELETE",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
    )


def discount_codes_count(*, times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Dict[str, Any]:
    """GET /discount_codes/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {"times_used": times_used, "times_used_min": times_used_min, "times_used_max": times_used_max}.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", "/discount_codes/count.json", params=params or None)


def discount_code_lookup(code: str) -> Dict[str, Any]:
    """GET /discount_codes/lookup.json?code=... (deprecated by Shopify but still useful)"""
    return get_client().request("GET", "/discount_codes/lookup.json", params={"code": code})


def discount_code_batch_create(price_rule_id: int, discount_codes: list[Dict[str, Any]]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/batch.json"""
    return get_client().request(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        json_body={"discount_codes": discount_codes},
    )


def discount_code_batch_get(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}.json"""
    return get_client().request(
        "GET",
        f"/price_rules/{price_rule_id}/batch/{batch_id}.json",
    )


def discount_code_batch_codes_list(price_rule_id: int, batch_id: int, *, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"""
    params = {"limit": limit} if limit is not None else None
    return get_client().request(
        "GET",
        f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json",
        params=params,
    )
