from typing import Any, Dict, List

from .client import ConfluenceClient


def v1_get_content_labels(content_id: str, *, prefix: str = "global", limit: int = 200, start: int = 0) -> Any:
    """GET /rest/api/content/{id}/label"""
    c = ConfluenceClient()
    return c.request(
        "GET",
        f"/rest/api/content/{content_id}/label",
        params={"prefix": prefix, "limit": limit, "start": start},
    )


def v1_add_content_labels(content_id: str, *, labels: List[str], prefix: str = "global") -> Any:
    """POST /rest/api/content/{id}/label"""
    c = ConfluenceClient()
    payload = [{"prefix": prefix, "name": name} for name in labels]
    return c.request("POST", f"/rest/api/content/{content_id}/label", json=payload, expected=(200, 201))


def v1_remove_content_label(content_id: str, *, name: str, prefix: str = "global") -> Any:
    """DELETE /rest/api/content/{id}/label"""
    c = ConfluenceClient()
    return c.request(
        "DELETE",
        f"/rest/api/content/{content_id}/label",
        params={"name": name, "prefix": prefix},
        expected=(204,),
    )
