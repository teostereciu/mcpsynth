from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_price_rule(price_rule: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/price_rules.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def list_price_rules(
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", "/price_rules.json", params=params)


def get_price_rule(price_rule_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules(*, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/price_rules/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/price_rules/count.json")


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/price_rules/{price_rule_id}.json", json_body={"price_rule": price_rule})


def delete_price_rule(price_rule_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/price_rules/{price_rule_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/price_rules/{price_rule_id}.json")
