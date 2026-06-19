from typing import Any, Dict, Optional

from .http_client import ShopifyAdminClient


def create_price_rule(price_rule: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def list_price_rules(*, api_version: str = "2026-01", limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", "/price_rules.json", params=params or None)


def get_price_rule(price_rule_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules(*, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/count.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", "/price_rules/count.json")


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """PUT /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return client.request("PUT", f"/price_rules/{price_rule_id}.json", json_body=body)


def delete_price_rule(price_rule_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("DELETE", f"/price_rules/{price_rule_id}.json")


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
    )


def list_discount_codes(
    price_rule_id: int,
    *,
    api_version: str = "2026-01",
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params or None)


def get_discount_code(price_rule_id: int, discount_code_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def update_discount_code(
    price_rule_id: int,
    discount_code_id: int,
    discount_code: Dict[str, Any],
    *,
    api_version: str = "2026-01",
) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"discount_code": {**discount_code, "id": discount_code_id}}
    return client.request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json_body=body,
    )


def delete_discount_code(price_rule_id: int, discount_code_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def create_discount_code_batch(price_rule_id: int, discount_codes: list[Dict[str, Any]], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules/{price_rule_id}/batch.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/price_rules/{price_rule_id}/batch.json", json_body={"discount_codes": discount_codes})


def get_discount_code_batch(price_rule_id: int, batch_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/batch/{batch_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_codes_for_batch(price_rule_id: int, batch_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json")


def count_discount_codes(*, api_version: str = "2026-01", times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/discount_codes/count.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {"times_used": times_used, "times_used_min": times_used_min, "times_used_max": times_used_max}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/discount_codes/count.json", params=params or None)


def lookup_discount_code(code: str, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/discount_codes/lookup.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", "/discount_codes/lookup.json", params={"code": code})
