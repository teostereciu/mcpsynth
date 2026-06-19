from typing import Any, Dict, Optional

from shopify_client import ShopifyClient, build_pagination_params


def list_price_rules(*, limit: Optional[int] = 50, page_info: Optional[str] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /price_rules.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    return c.request("GET", "/price_rules.json", params=params)


def get_price_rule(*, price_rule_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/price_rules/{price_rule_id}.json")


def create_price_rule(*, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules.json"""
    c = ShopifyClient()
    return c.request("POST", "/price_rules.json", json={"price_rule": price_rule})


def update_price_rule(*, price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}.json"""
    c = ShopifyClient()
    body = {"price_rule": {**price_rule, "id": price_rule_id}}
    return c.request("PUT", f"/price_rules/{price_rule_id}.json", json=body)


def delete_price_rule(*, price_rule_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}.json"""
    c = ShopifyClient()
    return c.request("DELETE", f"/price_rules/{price_rule_id}.json")


def list_discount_codes(*, price_rule_id: int, limit: Optional[int] = 50, page_info: Optional[str] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    return c.request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


def create_discount_code(*, price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/discount_codes.json"""
    c = ShopifyClient()
    return c.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json={"discount_code": discount_code},
    )


def delete_discount_code(*, price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"""
    c = ShopifyClient()
    return c.request(
        "DELETE",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
    )
