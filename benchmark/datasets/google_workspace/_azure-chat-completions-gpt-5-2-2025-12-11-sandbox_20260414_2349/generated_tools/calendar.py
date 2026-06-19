from typing import Any, Dict, Optional

from .http import request_json

CAL_BASE = "https://www.googleapis.com/calendar/v3"


def calendar_calendars_insert(*, body: Dict[str, Any]) -> Any:
    return request_json("POST", f"{CAL_BASE}/calendars", json_body=body)


def calendar_calendars_get(calendarId: str) -> Any:
    return request_json("GET", f"{CAL_BASE}/calendars/{calendarId}")


def calendar_calendars_update(calendarId: str, *, body: Dict[str, Any]) -> Any:
    return request_json("PUT", f"{CAL_BASE}/calendars/{calendarId}", json_body=body)


def calendar_calendars_delete(calendarId: str) -> Any:
    return request_json("DELETE", f"{CAL_BASE}/calendars/{calendarId}")


def calendar_calendarList_list(*, maxResults: int = 250, pageToken: Optional[str] = None, showDeleted: Optional[bool] = None, showHidden: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {"maxResults": maxResults}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if showDeleted is not None:
        params["showDeleted"] = showDeleted
    if showHidden is not None:
        params["showHidden"] = showHidden
    return request_json("GET", f"{CAL_BASE}/users/me/calendarList", params=params)


def calendar_calendarList_get(calendarId: str) -> Any:
    return request_json("GET", f"{CAL_BASE}/users/me/calendarList/{calendarId}")


def calendar_calendarList_insert(*, body: Dict[str, Any]) -> Any:
    return request_json("POST", f"{CAL_BASE}/users/me/calendarList", json_body=body)


def calendar_events_list(
    calendarId: str = "primary",
    *,
    timeMin: Optional[str] = None,
    timeMax: Optional[str] = None,
    maxResults: int = 250,
    singleEvents: Optional[bool] = None,
    orderBy: Optional[str] = None,
    q: Optional[str] = None,
    pageToken: Optional[str] = None,
) -> Any:
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
    return request_json("GET", f"{CAL_BASE}/calendars/{calendarId}/events", params=params)


def calendar_events_get(calendarId: str = "primary", eventId: str = "") -> Any:
    return request_json("GET", f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}")


def calendar_events_insert(calendarId: str = "primary", *, body: Dict[str, Any]) -> Any:
    return request_json("POST", f"{CAL_BASE}/calendars/{calendarId}/events", json_body=body)


def calendar_events_update(calendarId: str = "primary", eventId: str = "", *, body: Dict[str, Any]) -> Any:
    return request_json("PUT", f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}", json_body=body)


def calendar_events_patch(calendarId: str = "primary", eventId: str = "", *, body: Dict[str, Any]) -> Any:
    return request_json("PATCH", f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}", json_body=body)


def calendar_events_delete(calendarId: str = "primary", eventId: str = "") -> Any:
    return request_json("DELETE", f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}")


def calendar_events_move(calendarId: str = "primary", eventId: str = "", destination: str = "") -> Any:
    return request_json("POST", f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}/move", params={"destination": destination})


def calendar_acl_list(calendarId: str = "primary", *, maxResults: int = 100, pageToken: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"maxResults": maxResults}
    if pageToken is not None:
        params["pageToken"] = pageToken
    return request_json("GET", f"{CAL_BASE}/calendars/{calendarId}/acl", params=params)


def calendar_acl_insert(calendarId: str = "primary", *, body: Dict[str, Any]) -> Any:
    return request_json("POST", f"{CAL_BASE}/calendars/{calendarId}/acl", json_body=body)


def calendar_acl_delete(calendarId: str = "primary", ruleId: str = "") -> Any:
    return request_json("DELETE", f"{CAL_BASE}/calendars/{calendarId}/acl/{ruleId}")


def calendar_freebusy_query(*, body: Dict[str, Any]) -> Any:
    return request_json("POST", f"{CAL_BASE}/freeBusy", json_body=body)


def calendar_settings_list(*, maxResults: int = 250, pageToken: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"maxResults": maxResults}
    if pageToken is not None:
        params["pageToken"] = pageToken
    return request_json("GET", f"{CAL_BASE}/users/me/settings", params=params)


def calendar_settings_get(setting: str) -> Any:
    return request_json("GET", f"{CAL_BASE}/users/me/settings/{setting}")
