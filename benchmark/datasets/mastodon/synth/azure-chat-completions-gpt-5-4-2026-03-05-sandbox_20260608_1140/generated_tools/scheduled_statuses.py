from typing import Optional

from generated_tools.common import clean_params, mastodon_request


def list_scheduled_statuses(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    return mastodon_request("GET", "/api/v1/scheduled_statuses", params=clean_params(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id))


def get_scheduled_status(scheduled_status_id: str):
    return mastodon_request("GET", f"/api/v1/scheduled_statuses/{scheduled_status_id}")


def update_scheduled_status(scheduled_status_id: str, scheduled_at: str):
    return mastodon_request("PUT", f"/api/v1/scheduled_statuses/{scheduled_status_id}", data={"scheduled_at": scheduled_at})


def cancel_scheduled_status(scheduled_status_id: str):
    return mastodon_request("DELETE", f"/api/v1/scheduled_statuses/{scheduled_status_id}")
