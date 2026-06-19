from typing import Any, Dict, Optional

from .http import ShopifyClient


# Price rules

def list_price_rules(*, limit: Optional[int] = 50, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return ShopifyClient().request("GET", "/price_rules.json", params=params or None)


def get_price_rule(*, price_rule_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    return ShopifyClient().request("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules() -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/count.json"""
    return ShopifyClient().request("GET", "/price_rules/count.json")


def create_price_rule(*, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules.json"""
    return ShopifyClient().request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def update_price_rule(*, price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return ShopifyClient().request("PUT", f"/price_rules/{price_rule_id}.json", json_body=body)


def delete_price_rule(*, price_rule_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    return ShopifyClient().request("DELETE", f"/price_rules/{price_rule_id}.json")


# Discount codes

def create_discount_code(*, price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json"""
    return ShopifyClient().request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
    )


def list_discount_codes(*, price_rule_id: int, limit: Optional[int] = 50, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return ShopifyClient().request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params or None)


def get_discount_code(*, price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    return ShopifyClient().request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def update_discount_code(*, price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    body = {"discount_code": {**discount_code, "id": discount_code_id}}
    return ShopifyClient().request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json_body=body,
    )


def delete_discount_code(*, price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    return ShopifyClient().request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def count_discount_codes(*, times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/discount_codes/count.json"""
    params: Dict[str, Any] = {}
    if times_used is not None:
        params["times_used"] = times_used
    if times_used_min is not None:
        params["times_used_min"] = times_used_min
    if times_used_max is not None:
        params["times_used_max"] = times_used_max
    return ShopifyClient().request("GET", "/discount_codes/count.json", params=params or None)


def lookup_discount_code(*, code: str) -> Dict[str, Any]:
    """GET /admin/api/2026-01/discount_codes/lookup.json"""
    # Location is in headers; our client returns link/x-request-id only, so return raw headers via a direct request.
    resp = ShopifyClient().request("GET", "/discount_codes/lookup.json", params={"code": code})
    return resp


def create_discount_code_batch(*, price_rule_id: int, discount_codes: list[Dict[str, Any]]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules/{price_rule_id}/batch.json"""
    return ShopifyClient().request(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        json_body={"discount_codes": discount_codes},
    )


def get_discount_code_batch(*, price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/batch/{batch_id}.json"""
    return ShopifyClient().request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_codes_for_batch(*, price_rule_id: int, batch_id: int, limit: Optional[int] = 50) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return ShopifyClient().request(
        "GET",
        f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json",
        params=params or None,
    )
