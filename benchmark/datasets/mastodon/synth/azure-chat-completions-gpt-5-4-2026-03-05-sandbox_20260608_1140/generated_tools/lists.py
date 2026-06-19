from typing import Optional

from generated_tools.common import clean_params, mastodon_request


def list_lists():
    return mastodon_request("GET", "/api/v1/lists")


def get_list(list_id: str):
    return mastodon_request("GET", f"/api/v1/lists/{list_id}")


def create_list(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None):
    return mastodon_request("POST", "/api/v1/lists", data=clean_params(title=title, replies_policy=replies_policy, exclusive=exclusive))


def update_list(list_id: str, title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None):
    return mastodon_request("PUT", f"/api/v1/lists/{list_id}", data=clean_params(title=title, replies_policy=replies_policy, exclusive=exclusive))


def delete_list(list_id: str):
    return mastodon_request("DELETE", f"/api/v1/lists/{list_id}")


def get_list_accounts(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    return mastodon_request("GET", f"/api/v1/lists/{list_id}/accounts", params=clean_params(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id))


def add_accounts_to_list(list_id: str, account_ids: list[str]):
    return mastodon_request("POST", f"/api/v1/lists/{list_id}/accounts", data={"account_ids[]": account_ids})


def remove_accounts_from_list(list_id: str, account_ids: list[str]):
    return mastodon_request("DELETE", f"/api/v1/lists/{list_id}/accounts", data={"account_ids[]": account_ids})
