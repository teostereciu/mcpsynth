from typing import Optional

from generated_tools.common import clean_params, mastodon_request


def verify_account_credentials():
    return mastodon_request("GET", "/api/v1/accounts/verify_credentials")


def get_account(account_id: str):
    return mastodon_request("GET", f"/api/v1/accounts/{account_id}")


def follow_account(account_id: str, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages: Optional[list[str]] = None):
    data = clean_params(reblogs=reblogs, notify=notify)
    if languages is not None:
        data["languages[]"] = languages
    return mastodon_request("POST", f"/api/v1/accounts/{account_id}/follow", data=data)


def unfollow_account(account_id: str):
    return mastodon_request("POST", f"/api/v1/accounts/{account_id}/unfollow")


def get_account_followers(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    return mastodon_request("GET", f"/api/v1/accounts/{account_id}/followers", params=clean_params(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id))


def get_account_following(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    return mastodon_request("GET", f"/api/v1/accounts/{account_id}/following", params=clean_params(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id))
