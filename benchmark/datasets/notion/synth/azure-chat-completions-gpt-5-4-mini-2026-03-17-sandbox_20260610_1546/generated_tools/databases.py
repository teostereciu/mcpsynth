from typing import Any, Dict

from .notion_client import NotionClient


client = NotionClient()


def create_database(body: Dict[str, Any]) -> Any:
    return client.request("POST", "/databases", json=body)


def retrieve_database(database_id: str) -> Any:
    return client.request("GET", f"/databases/{database_id}")


def update_database(database_id: str, body: Dict[str, Any]) -> Any:
    return client.request("PATCH", f"/databases/{database_id}", json=body)


def query_database(database_id: str, body: Dict[str, Any]) -> Any:
    return client.request("POST", f"/databases/{database_id}/query", json=body)
