from typing import Any, Dict, Optional, List

from .http_client import request_json


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/discount_codes.json

    Doc: docs/api_discountcode.md
    Body wrapper: {"discount_code": {...}}
    """
    return request_json(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json_body={"discount_code": discount_code},
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
    return request_json("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)


def get_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    """
    return request_json("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    Body wrapper: {"discount_code": {...}}
    """
    return request_json(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json_body={"discount_code": discount_code},
    )


def delete_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    """
    return request_json("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")


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
    return request_json("GET", "/discount_codes/count.json", params=params)


def lookup_discount_code(code: str) -> Dict[str, Any]:
    """GET /discount_codes/lookup.json?code=...

    Doc: docs/api_discountcode.md

    Note: Shopify returns the discount code location in the Location header.
    This tool returns the response JSON (if any) and status; headers are not exposed by this client.
    """
    return request_json("GET", "/discount_codes/lookup.json", params={"code": code})


def create_discount_code_batch(price_rule_id: int, discount_codes: List[Dict[str, Any]]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/batch.json

    Doc: docs/api_discountcode.md
    Body: {"discount_codes": [{"code": ...}, ...]}
    """
    return request_json(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        json_body={"discount_codes": discount_codes},
    )


def get_discount_code_batch(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}.json

    Doc: docs/api_discountcode.md
    """
    return request_json("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_codes_for_batch(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json

    Doc: docs/api_discountcode.md
    """
    return request_json("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json")
