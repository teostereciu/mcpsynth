from typing import Any, Dict, Optional

from ._client import get_client


def create_price_rule(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules.json

    Doc: docs/api_pricerule.md
    """
    return get_client().request("POST", "/price_rules.json", json_body={"price_rule": price_rule})


def list_price_rules(*, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /price_rules.json

    Doc: docs/api_pricerule.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return get_client().request("GET", "/price_rules.json", params=params)


def get_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    """
    return get_client().request("GET", f"/price_rules/{price_rule_id}.json")


def count_price_rules() -> Dict[str, Any]:
    """GET /price_rules/count.json

    Doc: docs/api_pricerule.md
    """
    return get_client().request("GET", "/price_rules/count.json")


def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    """
    return get_client().request(
        "PUT",
        f"/price_rules/{price_rule_id}.json",
        json_body={"price_rule": {**price_rule, "id": price_rule_id}},
    )


def delete_price_rule(price_rule_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}.json

    Doc: docs/api_pricerule.md
    """
    return get_client().request("DELETE", f"/price_rules/{price_rule_id}.json")


def create_discount_code(price_rule_id: int, code: str) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/discount_codes.json

    Doc: docs/api_discountcode.md
    """
    return get_client().request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": {"code": code}},
    )


def list_discount_codes(price_rule_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes.json

    Doc: docs/api_discountcode.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return get_client().request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


def get_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    """
    return get_client().request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def update_discount_code(price_rule_id: int, discount_code_id: int, code: str) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    """
    return get_client().request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json_body={"discount_code": {"id": discount_code_id, "code": code}},
    )


def delete_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    """
    return get_client().request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def create_discount_code_batch(price_rule_id: int, codes: list[str]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/batch.json

    Doc: docs/api_discountcode.md
    """
    return get_client().request(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        json_body={"discount_codes": [{"code": c} for c in codes]},
    )


def get_discount_code_batch(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}.json

    Doc: docs/api_discountcode.md
    """
    return get_client().request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_codes_for_batch(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json

    Doc: docs/api_discountcode.md
    """
    return get_client().request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json")


def count_discount_codes(*, times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Dict[str, Any]:
    """GET /discount_codes/count.json

    Doc: docs/api_discountcode.md
    """
    params: Dict[str, Any] = {}
    if times_used is not None:
        params["times_used"] = times_used
    if times_used_min is not None:
        params["times_used_min"] = times_used_min
    if times_used_max is not None:
        params["times_used_max"] = times_used_max
    return get_client().request("GET", "/discount_codes/count.json", params=params)


def lookup_discount_code(code: str) -> Dict[str, Any]:
    """GET /discount_codes/lookup.json?code=...

    Doc: docs/api_discountcode.md
    """
    return get_client().request("GET", "/discount_codes/lookup.json", params={"code": code})
