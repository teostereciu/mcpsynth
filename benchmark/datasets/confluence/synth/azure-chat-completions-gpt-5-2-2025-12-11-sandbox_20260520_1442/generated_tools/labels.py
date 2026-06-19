from typing import Any, Dict, List, Optional, Union

from .http_client import ConfluenceClient


def add_labels_to_content(*, content_id: str, labels: Union[List[Dict[str, str]], Dict[str, str]]) -> Dict[str, Any]:
    """POST /wiki/rest/api/content/{id}/label"""
    return ConfluenceClient().request(
        "POST",
        f"/rest/api/content/{content_id}/label",
        json=labels if isinstance(labels, list) else [labels],
    )  # type: ignore[return-value]


def remove_label_from_content_by_query(*, content_id: str, name: str) -> Dict[str, Any]:
    """DELETE /wiki/rest/api/content/{id}/label?name={name}"""
    return ConfluenceClient().request(
        "DELETE",
        f"/rest/api/content/{content_id}/label",
        params={"name": name},
    )  # type: ignore[return-value]


def remove_label_from_content(*, content_id: str, label: str) -> Dict[str, Any]:
    """DELETE /wiki/rest/api/content/{id}/label/{label}"""
    return ConfluenceClient().request(
        "DELETE",
        f"/rest/api/content/{content_id}/label/{label}",
    )  # type: ignore[return-value]
