from typing import Any, Dict, List, Optional

from .client import ShopifyClient, clean_params


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /price_rules/{price_rule_id}/discount_codes.json"""
    client = client or ShopifyClient()
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json={"discount_code": discount_code},
    )


def list_discount_codes(price_rule_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /price_rules/{price_rule_id}/discount_codes.json"""
    client = client or ShopifyClient()
    params = clean_params({"limit": limit, "since_id": since_id})
    return client.request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


def get_discount_code(price_rule_id: int, discount_code_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """PUT /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = client or ShopifyClient()
    body = {"discount_code": {**discount_code, "id": discount_code_id}}
    return client.request("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", json=body)


def delete_discount_code(price_rule_id: int, discount_code_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def create_discount_code_batch(price_rule_id: int, discount_codes: List[Dict[str, Any]], *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /price_rules/{price_rule_id}/batch.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/price_rules/{price_rule_id}/batch.json", json={"discount_codes": discount_codes})


def get_discount_code_batch(price_rule_id: int, batch_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_codes_for_batch(price_rule_id: int, batch_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json")


def count_discount_codes(*, times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /discount_codes/count.json"""
    client = client or ShopifyClient()
    params = clean_params({"times_used": times_used, "times_used_min": times_used_min, "times_used_max": times_used_max})
    return client.request("GET", "/discount_codes/count.json", params=params)


def lookup_discount_code(code: str, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /discount_codes/lookup.json (deprecated)"""
    client = client or ShopifyClient()
    params = {"code": code}
    return client.request("GET", "/discount_codes/lookup.json", params=params)
