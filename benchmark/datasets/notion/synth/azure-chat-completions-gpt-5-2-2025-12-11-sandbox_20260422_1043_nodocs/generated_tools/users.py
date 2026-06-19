from typing import Any

from .notion_client import NotionClient


def users_list(*, notion_version: str = "2022-06-28") -> Any:
    client = NotionClient(notion_version=notion_version)
    return client.request("GET", "/users")


def users_retrieve(user_id: str, *, notion_version: str = "2022-06-28") -> Any:
    client = NotionClient(notion_version=notion_version)
    return client.request("GET", f"/users/{user_id}")


def users_me(*, notion_version: str = "2022-06-28") -> Any:
    client = NotionClient(notion_version=notion_version)
    return client.request("GET", "/users/me")
