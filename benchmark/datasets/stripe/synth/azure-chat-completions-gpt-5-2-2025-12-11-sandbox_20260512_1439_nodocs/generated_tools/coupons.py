from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def coupons_create(**kwargs) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/coupons", kwargs)


def coupons_retrieve(coupon_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/coupons/{coupon_id}", kwargs or None)


def coupons_update(coupon_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/coupons/{coupon_id}", kwargs)


def coupons_delete(coupon_id: str) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/coupons/{coupon_id}")


def coupons_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/coupons", params)


def coupons_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/coupons", kwargs, limit=limit)
