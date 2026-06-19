from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

CAL_BASE = "https://www.googleapis.com/calendar/v3"


def calendar_events_list(
    calendarId: str = "primary",
    *,
    timeMin: Optional[str] = None,
    timeMax: Optional[str] = None,
    maxResults: int = 10,
    singleEvents: Optional[bool] = True,
    orderBy: Optional[str] = "startTime",
    q: Optional[str] = None,
    pageToken: Optional[str] = None,
) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events"
    params: Dict[str, Any] = {"maxResults": maxResults}
    if timeMin is not None:
        params["timeMin"] = timeMin
    if timeMax is not None:
        params["timeMax"] = timeMax
    if singleEvents is not None:
        params["singleEvents"] = singleEvents
    if orderBy is not None:
        params["orderBy"] = orderBy
    if q is not None:
        params["q"] = q
    if pageToken is not None:
        params["pageToken"] = pageToken
    return request_json("GET", url, params=params)


def calendar_events_get(calendarId: str = "primary", eventId: str = "") -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}"
    return request_json("GET", url)


def calendar_events_insert(calendarId: str = "primary", *, event: Dict[str, Any]) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events"
    return request_json("POST", url, json_body=event)
