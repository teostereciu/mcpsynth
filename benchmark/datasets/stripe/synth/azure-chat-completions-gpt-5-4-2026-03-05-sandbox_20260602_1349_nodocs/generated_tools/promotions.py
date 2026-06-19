from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_coupon(
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration: str = "once",
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        "/v1/coupons",
        {
            "percent_off": percent_off,
            "amount_off": amount_off,
            "currency": currency,
            "duration": duration,
            "name": name,
            "metadata": metadata,
        },
    )


def retrieve_coupon(coupon_id: str) -> Any:
    return stripe_request("GET", f"/v1/coupons/{coupon_id}")


def update_coupon(coupon_id: str, metadata: Optional[Dict[str, Any]] = None, name: Optional[str] = None) -> Any:
    return stripe_request("POST", f"/v1/coupons/{coupon_id}", {"metadata": metadata, "name": name})


def list_coupons(limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/coupons", {"limit": limit})


def delete_coupon(coupon_id: str) -> Any:
    return stripe_request("DELETE", f"/v1/coupons/{coupon_id}")


def create_promotion_code(coupon: str, code: Optional[str] = None, active: Optional[bool] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", "/v1/promotion_codes", {"coupon": coupon, "code": code, "active": active, "metadata": metadata})


def retrieve_promotion_code(promotion_code_id: str) -> Any:
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}")


def update_promotion_code(promotion_code_id: str, active: Optional[bool] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", {"active": active, "metadata": metadata})


def list_promotion_codes(code: Optional[str] = None, coupon: Optional[str] = None, active: Optional[bool] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/promotion_codes", {"code": code, "coupon": coupon, "active": active, "limit": limit})
