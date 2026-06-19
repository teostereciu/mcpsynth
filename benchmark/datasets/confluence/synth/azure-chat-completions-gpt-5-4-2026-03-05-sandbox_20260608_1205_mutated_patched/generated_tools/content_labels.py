from typing import Any, List, Optional

from generated_tools.core import client


def add_labels_to_content(content_id: str, labels: List[dict] | dict) -> Any:
    return client.request("POST", f"/rest/api/content/{content_id}/label", json=labels)


def remove_label_from_content_by_query(content_id: str, name: str) -> Any:
    return client.request("DELETE", f"/rest/api/content/{content_id}/label", params={"name": name})


def remove_label_from_content(content_id: str, label: str) -> Any:
    return client.request("DELETE", f"/rest/api/content/{content_id}/label/{label}")
