from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_product(
    name: str,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        "/v1/products",
        {"name": name, "description": description, "active": active, "metadata": metadata},
    )


def retrieve_product(product_id: str) -> Any:
    return stripe_request("GET", f"/v1/products/{product_id}")


def update_product(
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        f"/v1/products/{product_id}",
        {"name": name, "description": description, "active": active, "metadata": metadata},
    )


def list_products(active: Optional[bool] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/products", {"active": active, "limit": limit})


def delete_product(product_id: str) -> Any:
    return stripe_request("DELETE", f"/v1/products/{product_id}")
