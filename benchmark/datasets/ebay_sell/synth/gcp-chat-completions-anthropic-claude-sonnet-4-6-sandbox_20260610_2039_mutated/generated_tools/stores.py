"""eBay Sell Stores API tools."""
from typing import Any, Optional
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
    """Add a new custom category to a user's eBay store (asynchronous)."""
    client = get_client()
    return client.request("POST", "/sell/stores/v1/store/categories", json=body)


def delete_store_category(category_id: str) -> dict:
    """Delete a store category by category ID."""
    client = get_client()
    return client.request("DELETE", f"/sell/stores/v1/store/categories/{category_id}")


def rename_store_category(category_id: str, body: dict) -> dict:
    """Rename a store category."""
    client = get_client()
    return client.request("PUT", f"/sell/stores/v1/store/categories/{category_id}", json=body)


def move_store_category(body: dict) -> dict:
    """Move a store category to a new position in the hierarchy."""
    client = get_client()
    return client.request("POST", "/sell/stores/v1/store/categories/move_category", json=body)


def get_store_task(task_id: str) -> dict:
    """Retrieve the status of a specific async store task."""
    client = get_client()
    return client.request("GET", f"/sell/stores/v1/store/tasks/{task_id}")


def get_store_tasks() -> dict:
    """Retrieve the status of all async store tasks."""
    client = get_client()
    return client.request("GET", "/sell/stores/v1/store/tasks")
