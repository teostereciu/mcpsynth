from typing import Any, Dict, List, Optional

from .common import mastodon_request


def verify_account_credentials() -> Any:
    return mastodon_request("GET", "/accounts/verify_credentials")


def get_account(account_id: str) -> Any:
    return mastodon_request("GET", f"/accounts/{account_id}")


def follow_account(account_id: str, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages: Optional[List[str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if reblogs is not None:
        data["reblogs"] = str(reblogs).lower()
    if notify is not None:
        data["notify"] = str(notify).lower()
    if languages is not None:
        for idx, value in enumerate(languages):
            data[f"languages[{idx}]"] = value
    return mastodon_request("POST", f"/accounts/{account_id}/follow", data=data)


def unfollow_account(account_id: str) -> Any:
    return mastodon_request("POST", f"/accounts/{account_id}/unfollow")


def get_account_followers(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}
    return mastodon_request("GET", f"/accounts/{account_id}/followers", params={k: v for k, v in params.items() if v is not None})


def get_account_following(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}
    return mastodon_request("GET", f"/accounts/{account_id}/following", params={k: v for k, v in params.items() if v is not None})
