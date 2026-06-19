from typing import Any, Dict, Optional

from .http import stripe_request


# Coupons

def create_coupon(duration: str, percent_off: Optional[float] = None, amount_off: Optional[int] = None, currency: Optional[str] = None, duration_in_months: Optional[int] = None, name: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"duration": duration}
    if percent_off is not None:
        data["percent_off"] = percent_off
    if amount_off is not None:
        data["amount_off"] = amount_off
    if currency is not None:
        data["currency"] = currency
    if duration_in_months is not None:
        data["duration_in_months"] = duration_in_months
    if name is not None:
        data["name"] = name
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/coupons", data=data)
    return err or res  # type: ignore


def get_coupon(coupon_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/coupons/{coupon_id}")
    return err or res  # type: ignore


def update_coupon(coupon_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/coupons/{coupon_id}", data=kwargs)
    return err or res  # type: ignore


def delete_coupon(coupon_id: str) -> Dict[str, Any]:
    res, err = stripe_request("DELETE", f"/v1/coupons/{coupon_id}")
    return err or res  # type: ignore


def list_coupons(limit: int = 10, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/coupons", params=params)
    return err or res  # type: ignore


# Promotion Codes

def create_promotion_code(coupon: str, code: Optional[str] = None, active: Optional[bool] = None, customer: Optional[str] = None, max_redemptions: Optional[int] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"coupon": coupon}
    if code is not None:
        data["code"] = code
    if active is not None:
        data["active"] = active
    if customer is not None:
        data["customer"] = customer
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/promotion_codes", data=data)
    return err or res  # type: ignore


def get_promotion_code(promotion_code_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}")
    return err or res  # type: ignore


def update_promotion_code(promotion_code_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", data=kwargs)
    return err or res  # type: ignore


def list_promotion_codes(limit: int = 10, active: Optional[bool] = None, code: Optional[str] = None, coupon: Optional[str] = None, customer: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if active is not None:
        params["active"] = active
    if code is not None:
        params["code"] = code
    if coupon is not None:
        params["coupon"] = coupon
    if customer is not None:
        params["customer"] = customer
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/promotion_codes", params=params)
    return err or res  # type: ignore
