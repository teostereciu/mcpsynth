from typing import Any, Dict, List, Optional

from .http_client import ConfluenceClient


def add_labels_to_content(content_id: str, labels: List[Dict[str, str]]) -> Dict[str, Any]:
    """POST /wiki/rest/api/content/{id}/label"""
    client = ConfluenceClient()
    return client.request("POST", f"/rest/api/content/{content_id}/label", json=labels)


def remove_label_from_content_by_query(content_id: str, name: str) -> Dict[str, Any]:
    """DEL /wiki/rest/api/content/{id}/label?name=..."""
    client = ConfluenceClient()
    return client.request("DELETE", f"/rest/api/content/{content_id}/label", params={"name": name})


def remove_label_from_content(content_id: str, label: str) -> Dict[str, Any]:
    """DEL /wiki/rest/api/content/{id}/label/{label}"""
    client = ConfluenceClient()
    return client.request("DELETE", f"/rest/api/content/{content_id}/label/{label}")
