from typing import Any, Dict, List, Optional

from generated_tools.common import mastodon_request


def create_status(
    status: str,
    visibility: Optional[str] = None,
    in_reply_to_id: Optional[str] = None,
    spoiler_text: Optional[str] = None,
    sensitive: Optional[bool] = None,
    language: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    poll_options: Optional[List[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = None,
    poll_hide_totals: Optional[bool] = None,
) -> Any:
    data: Dict[str, Any] = {
        "status": status,
        "visibility": visibility,
        "in_reply_to_id": in_reply_to_id,
        "spoiler_text": spoiler_text,
        "sensitive": sensitive,
        "language": language,
    }
    if media_ids:
        for idx, media_id in enumerate(media_ids):
            data[f"media_ids[{idx}]"] = media_id
    if poll_options:
        for idx, option in enumerate(poll_options):
            data[f"poll[options][{idx}]"] = option
        data["poll[expires_in]"] = poll_expires_in
        data["poll[multiple]"] = poll_multiple
        data["poll[hide_totals]"] = poll_hide_totals
    return mastodon_request("POST", "/api/v1/statuses", data=data)


def get_status(status_id: str) -> Any:
    return mastodon_request("GET", f"/api/v1/statuses/{status_id}")


def delete_status(status_id: str) -> Any:
    return mastodon_request("DELETE", f"/api/v1/statuses/{status_id}")


def reblog_status(status_id: str, visibility: Optional[str] = None) -> Any:
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/reblog", data={"visibility": visibility})


def unreblog_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/unreblog")


def favourite_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/favourite")


def unfavourite_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/unfavourite")


def get_status_context(status_id: str) -> Any:
    return mastodon_request("GET", f"/api/v1/statuses/{status_id}/context")
