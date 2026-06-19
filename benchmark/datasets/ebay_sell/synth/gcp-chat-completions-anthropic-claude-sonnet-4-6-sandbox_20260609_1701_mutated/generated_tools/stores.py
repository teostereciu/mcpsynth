"""eBay Sell Stores API tools."""
from typing import Optional
from .client import get_client


def get_store() -> dict:
    """Retrieve information for an eBay user's store (name, URL, description)."""
    client = get_client()
    return client.request("GET", "/sell/stores/v1/store")


def get_store_categories() -> dict:
    """Retrieve the category hierarchy for an eBay user's store."""
    client = get_client()
    return client.request("GET", "/sell/stores/v1/store/categories")


def add_store_category(body: dict) -> dict:
    """Add a new custom category to the seller's eBay store (async operation)."""
    client = get_client()
    return client.request("POST", "/sell/stores/v1/store/categories", json=body)


def delete_store_category(category_id: str, body: Optional[dict] = None) -> dict:
    """Delete a custom category from the seller's eBay store (async operation)."""
    client = get_client()
    return client.request("DELETE", f"/sell/stores/v1/store/categories/{category_id}", json=body)


def rename_store_category(category_id: str, body: dict) -> dict:
    """Rename a custom category in the seller's eBay store (async operation)."""
    client = get_client()
    return client.request("PUT", f"/sell/stores/v1/store/categories/{category_id}", json=body)


def move_store_category(body: dict) -> dict:
    """Move a store category to a different position in the category hierarchy."""
    client = get_client()
    return client.request("POST", "/sell/stores/v1/store/categories/move_category", json=body)


def get_store_task(task_id: str) -> dict:
    """Retrieve the current status of a recent store operation by task ID."""
    client = get_client()
    return client.request("GET", f"/sell/stores/v1/store/tasks/{task_id}")


def get_store_tasks() -> dict:
    """Retrieve the status of all recent store operations."""
    client = get_client()
    return client.request("GET", "/sell/stores/v1/store/tasks")
