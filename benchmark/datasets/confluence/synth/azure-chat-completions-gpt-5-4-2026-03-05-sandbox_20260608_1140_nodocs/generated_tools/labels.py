from typing import Any, Dict

from generated_tools.confluence_client import client


def list_labels(page_id: str, prefix: str = "global") -> Dict[str, Any]:
    return client.request("GET", f"/api/v2/pages/{page_id}/labels", params={"prefix": prefix})


def add_label(page_id: str, name: str, prefix: str = "global") -> Dict[str, Any]:
    payload = [{"name": name, "prefix": prefix}]
    return client.request("POST", f"/api/v2/pages/{page_id}/labels", json_body=payload)


def remove_label(page_id: str, label_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/api/v2/pages/{page_id}/labels/{label_id}")
