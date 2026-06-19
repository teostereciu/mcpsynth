from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        "/v1/customers",
        {
            "email": email,
            "name": name,
            "phone": phone,
            "description": description,
            "metadata": metadata,
        },
    )


def retrieve_customer(customer_id: str) -> Any:
    return stripe_request("GET", f"/v1/customers/{customer_id}")


def update_customer(
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Any:
    return stripe_request(
        "POST",
        f"/v1/customers/{customer_id}",
        {
            "email": email,
            "name": name,
            "phone": phone,
            "description": description,
            "metadata": metadata,
        },
    )


def list_customers(email: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/customers", {"email": email, "limit": limit})


def delete_customer(customer_id: str) -> Any:
    return stripe_request("DELETE", f"/v1/customers/{customer_id}")


def search_customers(query: str, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/customers/search", {"query": query, "limit": limit})
