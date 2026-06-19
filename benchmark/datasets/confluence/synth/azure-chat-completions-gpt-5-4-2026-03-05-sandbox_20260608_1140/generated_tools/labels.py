from typing import Any

from confluence_client import client


def add_labels_to_content(content_id: int, labels: list[dict[str, str]]) -> Any:
    return client.request("POST", f"/rest/api/content/{content_id}/label", json_body=labels)


def remove_label_from_content_by_query(content_id: int, name: str) -> Any:
    return client.request("DELETE", f"/rest/api/content/{content_id}/label", params={"name": name})


def remove_label_from_content(content_id: int, label: str) -> Any:
    return client.request("DELETE", f"/rest/api/content/{content_id}/label/{label}")
