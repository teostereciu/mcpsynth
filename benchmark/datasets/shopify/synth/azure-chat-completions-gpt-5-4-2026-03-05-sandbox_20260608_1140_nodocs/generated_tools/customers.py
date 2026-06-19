from typing import Any, Dict, List, Optional

from generated_tools.common import clean_params, shopify_request


def list_customers(limit: Optional[int] = None, page_info: Optional[str] = None, query: Optional[str] = None, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(limit=limit, page_info=page_info, query=query, fields=",".join(fields) if fields else None)
    return shopify_request("GET", "/customers.json", params=params)


def search_customers(query: str, limit: Optional[int] = None, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(query=query, limit=limit, fields=",".join(fields) if fields else None)
    return shopify_request("GET", "/customers/search.json", params=params)


def get_customer(customer_id: int, fields: Optional[List[str]] = None) -> Any:
    params = clean_params(fields=",".join(fields) if fields else None)
    return shopify_request("GET", f"/customers/{customer_id}.json", params=params)


def create_customer(customer: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/customers.json", json_body={"customer": customer})


def update_customer(customer_id: int, customer: Dict[str, Any]) -> Any:
    body = {"customer": {"id": customer_id, **customer}}
    return shopify_request("PUT", f"/customers/{customer_id}.json", json_body=body)


def delete_customer(customer_id: int) -> Any:
    return shopify_request("DELETE", f"/customers/{customer_id}.json")


def list_customer_addresses(customer_id: int) -> Any:
    return shopify_request("GET", f"/customers/{customer_id}/addresses.json")


def create_customer_address(customer_id: int, address: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/customers/{customer_id}/addresses.json", json_body={"address": address})
