from typing import Any, Dict, List, Optional

from .client import ShopifyClient


def create_discount_code_creation_job(
    price_rule_id: int,
    discount_codes: List[Dict[str, Any]],
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules/{price_rule_id}/batch.json"""
    client = client or ShopifyClient()
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        json_body={"discount_codes": discount_codes},
    )


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json"""
    client = client or ShopifyClient()
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
    )


def count_discount_codes(
    *,
    times_used: Optional[int] = None,
    times_used_min: Optional[int] = None,
    times_used_max: Optional[int] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/discount_codes/count.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"times_used": times_used, "times_used_min": times_used_min, "times_used_max": times_used_max}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/discount_codes/count.json", params=params)


def lookup_discount_code(code: str, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/discount_codes/lookup.json?code=..."""
    client = client or ShopifyClient()
    # This endpoint returns location header; we return status + headers when possible.
    url_path = "/discount_codes/lookup.json"
    resp = client.request("GET", url_path, params={"code": code})
    return resp


def get_discount_code_creation_job(price_rule_id: int, batch_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/batch/{batch_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_codes_for_creation_job(
    price_rule_id: int,
    batch_id: int,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json")


def list_discount_codes(
    price_rule_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


def get_discount_code(price_rule_id: int, discount_code_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def update_discount_code(
    price_rule_id: int,
    discount_code_id: int,
    discount_code: Dict[str, Any],
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = client or ShopifyClient()
    return client.request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json_body={"discount_code": discount_code},
    )


def delete_discount_code(price_rule_id: int, discount_code_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
