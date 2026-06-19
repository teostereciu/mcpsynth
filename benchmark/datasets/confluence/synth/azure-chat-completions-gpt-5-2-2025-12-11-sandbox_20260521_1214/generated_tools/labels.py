from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http_client import ConfluenceClient


def add_labels_to_content(*, content_id: str, labels: List[Dict[str, str]]) -> Dict[str, Any]:
    """POST /wiki/rest/api/content/{id}/label"""
    client = ConfluenceClient.from_env()
    return client.request(
        "POST",
        f"/rest/api/content/{content_id}/label",
        json_body=labels,
        content_type="application/json",
    )


def remove_label_from_content(*, content_id: str, label: str) -> Dict[str, Any]:
    """DEL /wiki/rest/api/content/{id}/label/{label}"""
    client = ConfluenceClient.from_env()
    return client.request("DELETE", f"/rest/api/content/{content_id}/label/{label}")


def remove_label_from_content_by_query(*, content_id: str, name: str) -> Dict[str, Any]:
    """DEL /wiki/rest/api/content/{id}/label"""
    client = ConfluenceClient.from_env()
    return client.request("DELETE", f"/rest/api/content/{content_id}/label", params={"name": name})
