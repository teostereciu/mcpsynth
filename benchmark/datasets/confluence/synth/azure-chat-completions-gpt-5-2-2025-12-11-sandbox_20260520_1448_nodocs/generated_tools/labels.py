from typing import Any, Dict, List

from .http import confluence_request


def list_labels(content_id: int, prefix: str = "global") -> Dict[str, Any]:
    return confluence_request("GET", f"/rest/api/content/{content_id}/label", params={"prefix": prefix})


def add_labels(content_id: int, labels: List[str], prefix: str = "global") -> Dict[str, Any]:
    payload = [{"prefix": prefix, "name": name} for name in labels]
    return confluence_request("POST", f"/rest/api/content/{content_id}/label", json=payload)


def remove_label(content_id: int, label: str) -> Dict[str, Any]:
    return confluence_request("DELETE", f"/rest/api/content/{content_id}/label/{label}")
