from typing import Any, Dict, Optional

from .http import stripe_request


# Customers

def create_customer(email: Optional[str] = None, name: Optional[str] = None, phone: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if email is not None:
        data["email"] = email
    if name is not None:
        data["name"] = name
    if phone is not None:
        data["phone"] = phone
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/customers", data=data)
    return err or res  # type: ignore


def get_customer(customer_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/customers/{customer_id}")
    return err or res  # type: ignore


def update_customer(customer_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/customers/{customer_id}", data=kwargs)
    return err or res  # type: ignore


def delete_customer(customer_id: str) -> Dict[str, Any]:
    res, err = stripe_request("DELETE", f"/v1/customers/{customer_id}")
    return err or res  # type: ignore


def list_customers(limit: int = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, email: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if email:
        params["email"] = email
    res, err = stripe_request("GET", "/v1/customers", params=params)
    return err or res  # type: ignore


# Products

def create_product(name: str, description: Optional[str] = None, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"name": name}
    if description is not None:
        data["description"] = description
    if active is not None:
        data["active"] = active
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/products", data=data)
    return err or res  # type: ignore


def get_product(product_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/products/{product_id}")
    return err or res  # type: ignore


def update_product(product_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/products/{product_id}", data=kwargs)
    return err or res  # type: ignore


def delete_product(product_id: str) -> Dict[str, Any]:
    res, err = stripe_request("DELETE", f"/v1/products/{product_id}")
    return err or res  # type: ignore


def list_products(limit: int = 10, active: Optional[bool] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if active is not None:
        params["active"] = active
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/products", params=params)
    return err or res  # type: ignore


# Prices

def create_price(unit_amount: Optional[int] = None, currency: str = "usd", product: Optional[str] = None, recurring: Optional[Dict[str, Any]] = None, nickname: Optional[str] = None, active: Optional[bool] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"currency": currency}
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if product is not None:
        data["product"] = product
    if recurring is not None:
        data["recurring"] = recurring
    if nickname is not None:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = active
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/prices", data=data)
    return err or res  # type: ignore


def get_price(price_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/prices/{price_id}")
    return err or res  # type: ignore


def update_price(price_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/prices/{price_id}", data=kwargs)
    return err or res  # type: ignore


def list_prices(limit: int = 10, product: Optional[str] = None, active: Optional[bool] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if product:
        params["product"] = product
    if active is not None:
        params["active"] = active
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/prices", params=params)
    return err or res  # type: ignore
