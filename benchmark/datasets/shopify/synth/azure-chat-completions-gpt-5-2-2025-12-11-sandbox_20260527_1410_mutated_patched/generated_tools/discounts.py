from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def price_rule_create(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules.json"""
    client = ShopifyClient()
    return client.request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def price_rules_list(*, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", "/price_rules.json", params=params if params else None)


def price_rule_get(price_rule_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}.json")


def price_rules_count() -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/count.json"""
    client = ShopifyClient()
    return client.request("GET", "/price_rules/count.json")


def price_rule_update(price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = ShopifyClient()
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return client.request("PUT", f"/price_rules/{price_rule_id}.json", json_body=body)


def price_rule_delete(price_rule_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/price_rules/{price_rule_id}.json")


def discount_code_create(price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
    )


def discount_codes_list(price_rule_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request(
        "GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params if params else None
    )


def discount_code_get(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = ShopifyClient()
    return client.request(
        "GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
    )


def discount_code_update(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = ShopifyClient()
    body = {"discount_code": {**discount_code, "id": discount_code_id}}
    return client.request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json_body=body,
    )


def discount_code_delete(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = ShopifyClient()
    return client.request(
        "DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
    )


def discount_codes_count(
    *,
    times_used: Optional[int] = None,
    times_used_min: Optional[int] = None,
    times_used_max: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/discount_codes/count.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {
        "times_used": times_used,
        "times_used_min": times_used_min,
        "times_used_max": times_used_max,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/discount_codes/count.json", params=params if params else None)


def discount_code_lookup(code: str) -> Dict[str, Any]:
    """GET /admin/api/2026-01/discount_codes/lookup.json?code=... (deprecated)"""
    client = ShopifyClient()
    return client.request("GET", "/discount_codes/lookup.json", params={"code": code})


def discount_code_batch_create(price_rule_id: int, discount_codes: list[Dict[str, Any]]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules/{price_rule_id}/batch.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        json_body={"discount_codes": discount_codes},
    )


def discount_code_batch_get(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/batch/{batch_id}.json"""
    client = ShopifyClient()
    return client.request(
        "GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json"
    )


def discount_code_batch_codes_list(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"""
    client = ShopifyClient()
    return client.request(
        "GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"
    )
