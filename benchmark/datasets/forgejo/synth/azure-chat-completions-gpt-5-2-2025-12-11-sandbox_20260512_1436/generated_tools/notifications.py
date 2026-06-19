from typing import Any, Dict, Optional, List

from .http_client import request


def notifications_list(
    *,
    all: Optional[bool] = None,
    status_types: Optional[List[str]] = None,
    subject_type: Optional[List[str]] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if all is not None:
        params["all"] = all
    if status_types is not None:
        params["status-types"] = status_types
    if subject_type is not None:
        params["subject-type"] = subject_type
    if since is not None:
        params["since"] = since
    if before is not None:
        params["before"] = before
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", "/notifications", params=params or None)


def notifications_check_new() -> Any:
    return request("GET", "/notifications/new")


def notifications_mark(*, last_read_at: Optional[str] = None, all: Optional[bool] = None, status_types: Optional[List[str]] = None, to_status: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if last_read_at is not None:
        params["last_read_at"] = last_read_at
    if all is not None:
        params["all"] = all
    if status_types is not None:
        params["status-types"] = status_types
    if to_status is not None:
        params["to-status"] = to_status
    return request("PUT", "/notifications", params=params or None)
