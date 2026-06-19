from typing import Any, Optional

from generated_tools.common import mastodon_request


def verify_credentials() -> Any:
    return mastodon_request("GET", "/api/v1/accounts/verify_credentials")


def get_account(account_id: str) -> Any:
    return mastodon_request("GET", f"/api/v1/accounts/{account_id}")


def follow_account(account_id: str, reblogs: Optional[bool] = None, notify: Optional[bool] = None) -> Any:
    return mastodon_request("POST", f"/api/v1/accounts/{account_id}/follow", data={"reblogs": reblogs, "notify": notify})


def unfollow_account(account_id: str) -> Any:
    return mastodon_request("POST", f"/api/v1/accounts/{account_id}/unfollow")


def get_account_followers(account_id: str, limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", f"/api/v1/accounts/{account_id}/followers", params={"limit": limit})


def get_account_following(account_id: str, limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", f"/api/v1/accounts/{account_id}/following", params={"limit": limit})
