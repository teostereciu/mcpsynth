from typing import Any, Dict, Optional

from ._client import get_client


def create_price_rule(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules.json

    Doc: docs/api_pricerule.md
    Body wrapper: {"price_rule": {...}}
    """
    client = get_client()
    return client.request("POST", "/price_rules.json", json={"price_rule": price_rule})


def list_price_rules(
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /price_rules.json

    Doc: docs/api_pricerule.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", "/price_rules.json", params=params or None)


def get_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    """
    client = get_client()
    return client.request("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules() -> Dict[str, Any]:
    """GET /price_rules/count.json

    Doc: docs/api_pricerule.md
    """
    client = get_client()
    return client.request("GET", "/price_rules/count.json")


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    Body wrapper: {"price_rule": {..., "id": price_rule_id}}
    """
    client = get_client()
    body = dict(price_rule)
    body.setdefault("id", price_rule_id)
    return client.request("PUT", f"/price_rules/{price_rule_id}.json", json={"price_rule": body})


def delete_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    """
    client = get_client()
    return client.request("DELETE", f"/price_rules/{price_rule_id}.json")
