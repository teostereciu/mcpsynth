from typing import Any, Dict, List, Optional

from ._client import get_client


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/discount_codes.json

    Doc: docs/api_discountcode.md
    Body wrapper: {"discount_code": {...}}
    """
    client = get_client()
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        json={"discount_code": discount_code},
    )


def list_discount_codes(
    price_rule_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes.json

    Doc: docs/api_discountcode.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request(
        "GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params or None
    )


def get_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    """
    client = get_client()
    return client.request(
        "GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
    )


def update_discount_code(
    price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]
) -> Dict[str, Any]:
    """PUT /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    Body wrapper: {"discount_code": {..., "id": discount_code_id}}
    """
    client = get_client()
    body = dict(discount_code)
    body.setdefault("id", discount_code_id)
    return client.request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        json={"discount_code": body},
    )


def delete_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    """DELETE /price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json

    Doc: docs/api_discountcode.md
    """
    client = get_client()
    return client.request(
        "DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json"
    )


def create_discount_code_batch(price_rule_id: int, discount_codes: List[Dict[str, Any]]) -> Dict[str, Any]:
    """POST /price_rules/{price_rule_id}/batch.json

    Doc: docs/api_discountcode.md
    Body wrapper: {"discount_codes": [{"code": ...}, ...]}
    """
    client = get_client()
    return client.request(
        "POST", f"/price_rules/{price_rule_id}/batch.json", json={"discount_codes": discount_codes}
    )


def get_discount_code_batch(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}.json

    Doc: docs/api_discountcode.md
    """
    client = get_client()
    return client.request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


def list_discount_codes_for_batch(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    """GET /price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json

    Doc: docs/api_discountcode.md
    """
    client = get_client()
    return client.request(
        "GET", f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json"
    )


def count_discount_codes(
    *,
    times_used: Optional[int] = None,
    times_used_min: Optional[int] = None,
    times_used_max: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /discount_codes/count.json

    Doc: docs/api_discountcode.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    for k, v in {
        "times_used": times_used,
        "times_used_min": times_used_min,
        "times_used_max": times_used_max,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/discount_codes/count.json", params=params or None)


def lookup_discount_code(code: str) -> Dict[str, Any]:
    """GET /discount_codes/lookup.json?code=...

    Doc: docs/api_discountcode.md

    Note: Shopify returns the location in headers; this tool returns the raw response body if any.
    """
    client = get_client()
    return client.request("GET", "/discount_codes/lookup.json", params={"code": code})
