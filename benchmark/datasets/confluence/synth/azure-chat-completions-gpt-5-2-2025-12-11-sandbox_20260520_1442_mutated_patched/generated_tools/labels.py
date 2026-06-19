from typing import Any, Dict, List

from .http_client import ConfluenceClient, ok_or_error


def add_labels_to_content(content_id: str, labels: List[Dict[str, str]]) -> Dict[str, Any]:
    """POST /rest/api/content/{id}/label"""
    c = ConfluenceClient()
    status, body, headers = c.request(
        "POST",
        f"/rest/api/content/{content_id}/label",
        json_body=labels,
    )
    return ok_or_error(status, body, headers)


def remove_label_from_content_by_name(content_id: str, name: str) -> Dict[str, Any]:
    """DELETE /rest/api/content/{id}/label?name=..."""
    c = ConfluenceClient()
    status, body, headers = c.request(
        "DELETE",
        f"/rest/api/content/{content_id}/label",
        params={"name": name},
    )
    return ok_or_error(status, body, headers)


def remove_label_from_content(content_id: str, label: str) -> Dict[str, Any]:
    """DELETE /rest/api/content/{id}/label/{label}"""
    c = ConfluenceClient()
    status, body, headers = c.request(
        "DELETE",
        f"/rest/api/content/{content_id}/label/{label}",
    )
    return ok_or_error(status, body, headers)
