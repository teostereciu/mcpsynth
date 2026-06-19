from typing import Optional

from generated_tools.common import clean_params, mastodon_request


def create_status(status: Optional[str] = None, in_reply_to_id: Optional[str] = None, sensitive: Optional[bool] = None, spoiler_text: Optional[str] = None, visibility: Optional[str] = None, language: Optional[str] = None, scheduled_at: Optional[str] = None, media_ids: Optional[list[str]] = None, poll_options: Optional[list[str]] = None, poll_expires_in: Optional[int] = None, poll_multiple: Optional[bool] = None, poll_hide_totals: Optional[bool] = None, quoted_status_id: Optional[str] = None, quote_approval_policy: Optional[str] = None):
    data = clean_params(status=status, in_reply_to_id=in_reply_to_id, sensitive=sensitive, spoiler_text=spoiler_text, visibility=visibility, language=language, scheduled_at=scheduled_at, quoted_status_id=quoted_status_id, quote_approval_policy=quote_approval_policy)
    if media_ids is not None:
        data["media_ids[]"] = media_ids
    if poll_options is not None:
        data["poll[options][]"] = poll_options
    if poll_expires_in is not None:
        data["poll[expires_in]"] = poll_expires_in
    if poll_multiple is not None:
        data["poll[multiple]"] = poll_multiple
    if poll_hide_totals is not None:
        data["poll[hide_totals]"] = poll_hide_totals
    return mastodon_request("POST", "/api/v1/statuses", data=data)


def get_status(status_id: str):
    return mastodon_request("GET", f"/api/v1/statuses/{status_id}")


def delete_status(status_id: str, delete_media: Optional[bool] = None):
    return mastodon_request("DELETE", f"/api/v1/statuses/{status_id}", params=clean_params(delete_media=delete_media))


def get_status_context(status_id: str):
    return mastodon_request("GET", f"/api/v1/statuses/{status_id}/context")


def favourite_status(status_id: str):
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str):
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/unfavourite")


def boost_status(status_id: str, visibility: Optional[str] = None):
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/reblog", data=clean_params(visibility=visibility))


def unboost_status(status_id: str):
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/unreblog")


def bookmark_status(status_id: str):
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/bookmark")


def unbookmark_status(status_id: str):
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/unbookmark")
