"""eBay Sell Stores API tools."""
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
    """Add a single new custom category to a user's eBay store (async)."""
    client = get_client()
    return client.request("POST", "/sell/stores/v1/store/categories", json=body)
