"""Google Calendar API v3 tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

CAL_BASE = "https://www.googleapis.com/calendar/v3"


def calendar_events_list(
    calendar_id: str = "primary",
    *,
    time_min: Optional[str] = None,
    time_max: Optional[str] = None,
    max_results: int = 250,
    single_events: bool = True,
    order_by: Optional[str] = "startTime",
    q: Optional[str] = None,
    page_token: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "maxResults": max_results,
        "singleEvents": single_events,
    }
    if order_by:
        params["orderBy"] = order_by
    if time_min:
        params["timeMin"] = time_min
    if time_max:
        params["timeMax"] = time_max
    if q:
        params["q"] = q
    if page_token:
        params["pageToken"] = page_token
    return request_json("GET", f"{CAL_BASE}/calendars/{calendar_id}/events", params=params)


def calendar_events_insert(calendar_id: str = "primary", *, event: Dict[str, Any]) -> Any:
    return request_json("POST", f"{CAL_BASE}/calendars/{calendar_id}/events", json=event)


def calendar_events_get(calendar_id: str = "primary", event_id: str = "") -> Any:
    return request_json("GET", f"{CAL_BASE}/calendars/{calendar_id}/events/{event_id}")


def calendar_events_delete(calendar_id: str = "primary", event_id: str = "") -> Any:
    return request_json("DELETE", f"{CAL_BASE}/calendars/{calendar_id}/events/{event_id}")


def calendar_events_patch(calendar_id: str = "primary", event_id: str = "", *, event_patch: Dict[str, Any]) -> Any:
    return request_json("PATCH", f"{CAL_BASE}/calendars/{calendar_id}/events/{event_id}", json=event_patch)


def calendar_events_update(calendar_id: str = "primary", event_id: str = "", *, event: Dict[str, Any]) -> Any:
    return request_json("PUT", f"{CAL_BASE}/calendars/{calendar_id}/events/{event_id}", json=event)


def calendar_freebusy_query(*, body: Dict[str, Any]) -> Any:
    return request_json("POST", f"{CAL_BASE}/freeBusy", json=body)


def calendar_calendarlist_list(*, max_results: int = 250, page_token: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"maxResults": max_results}
    if page_token:
        params["pageToken"] = page_token
    return request_json("GET", f"{CAL_BASE}/users/me/calendarList", params=params)


def calendar_calendars_insert(*, calendar: Dict[str, Any]) -> Any:
    return request_json("POST", f"{CAL_BASE}/calendars", json=calendar)


def calendar_calendars_get(calendar_id: str) -> Any:
    return request_json("GET", f"{CAL_BASE}/calendars/{calendar_id}")
