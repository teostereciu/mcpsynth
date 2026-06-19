from typing import Any, List, Optional

from generated_tools.common import mastodon_request


def get_lists() -> Any:
    return mastodon_request("GET", "/api/v1/lists")


def create_list(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    return mastodon_request("POST", "/api/v1/lists", data={"title": title, "replies_policy": replies_policy, "exclusive": exclusive})


def get_list(list_id: str) -> Any:
    return mastodon_request("GET", f"/api/v1/lists/{list_id}")


def update_list(list_id: str, title: Optional[str] = None, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    return mastodon_request("PUT", f"/api/v1/lists/{list_id}", data={"title": title, "replies_policy": replies_policy, "exclusive": exclusive})


def delete_list(list_id: str) -> Any:
    return mastodon_request("DELETE", f"/api/v1/lists/{list_id}")


def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Any:
    data = {}
    for idx, account_id in enumerate(account_ids):
        data[f"account_ids[{idx}]"] = account_id
    return mastodon_request("POST", f"/api/v1/lists/{list_id}/accounts", data=data)


def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Any:
    data = {}
    for idx, account_id in enumerate(account_ids):
        data[f"account_ids[{idx}]"] = account_id
    return mastodon_request("DELETE", f"/api/v1/lists/{list_id}/accounts", data=data)
