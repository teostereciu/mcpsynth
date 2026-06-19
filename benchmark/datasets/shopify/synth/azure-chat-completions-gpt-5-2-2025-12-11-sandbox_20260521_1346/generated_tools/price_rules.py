from typing import Any, Dict, Optional

from .client import ShopifyClient, clean_params


def create_price_rule(price_rule: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /price_rules.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/price_rules.json", json={"price_rule": price_rule})


def list_price_rules(*, limit: Optional[int] = None, since_id: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /price_rules.json"""
    client = client or ShopifyClient()
    params = clean_params({"limit": limit, "since_id": since_id})
    return client.request("GET", "/price_rules.json", params=params)


def get_price_rule(price_rule_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /price_rules/{price_rule_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules(*, client: Optional[ShopifyClient] = None) -> Any:
    """GET /price_rules/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/price_rules/count.json")


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """PUT /price_rules/{price_rule_id}.json"""
    client = client or ShopifyClient()
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return client.request("PUT", f"/price_rules/{price_rule_id}.json", json=body)


def delete_price_rule(price_rule_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """DELETE /price_rules/{price_rule_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/price_rules/{price_rule_id}.json")
