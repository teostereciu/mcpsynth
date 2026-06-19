from typing import Any, Dict, Optional

from .http_client import request_json


def create_price_rule(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules.json

    Doc: docs/api_pricerule.md
    Body wrapper: {"price_rule": {...}}
    """
    return request_json("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def list_price_rules(*, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /price_rules.json

    Doc: docs/api_pricerule.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", "/price_rules.json", params=params)


def get_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    """
    return request_json("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules() -> Dict[str, Any]:
    """GET /price_rules/count.json

    Doc: docs/api_pricerule.md
    """
    return request_json("GET", "/price_rules/count.json")


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    Body wrapper: {"price_rule": {...}}
    """
    return request_json("PUT", f"/price_rules/{price_rule_id}.json", json_body={"price_rule": price_rule})


def delete_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    """
    return request_json("DELETE", f"/price_rules/{price_rule_id}.json")
