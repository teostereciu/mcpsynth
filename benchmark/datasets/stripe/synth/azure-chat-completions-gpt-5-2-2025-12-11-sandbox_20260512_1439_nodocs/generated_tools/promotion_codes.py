from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def promotion_codes_create(coupon: str, **kwargs) -> Dict[str, Any]:
    params = {"coupon": coupon}
    params.update(kwargs)
    return stripe_request("POST", "/v1/promotion_codes", params)


def promotion_codes_retrieve(promotion_code_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}", kwargs or None)


def promotion_codes_update(promotion_code_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", kwargs)


def promotion_codes_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/promotion_codes", params)


def promotion_codes_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/promotion_codes", kwargs, limit=limit)
