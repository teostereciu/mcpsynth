from typing import Any, Dict, List, Optional

from .common import mastodon_request


def get_lists() -> Any:
    return mastodon_request("GET", "/lists")


def get_list(list_id: str) -> Any:
    return mastodon_request("GET", f"/lists/{list_id}")


def create_list(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = str(exclusive).lower()
    return mastodon_request("POST", "/lists", data=data)


def update_list(list_id: str, title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = str(exclusive).lower()
    return mastodon_request("PUT", f"/lists/{list_id}", data=data)


def delete_list(list_id: str) -> Any:
    return mastodon_request("DELETE", f"/lists/{list_id}")


def get_list_accounts(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}
    return mastodon_request("GET", f"/lists/{list_id}/accounts", params={k: v for k, v in params.items() if v is not None})


def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Any:
    data = {f"account_ids[{idx}]": value for idx, value in enumerate(account_ids)}
    return mastodon_request("POST", f"/lists/{list_id}/accounts", data=data)


def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Any:
    data = {f"account_ids[{idx}]": value for idx, value in enumerate(account_ids)}
    return mastodon_request("DELETE", f"/lists/{list_id}/accounts", data=data)
