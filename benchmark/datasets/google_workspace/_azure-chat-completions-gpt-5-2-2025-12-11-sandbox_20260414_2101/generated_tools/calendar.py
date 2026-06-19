from typing import Any, Dict, Optional

from .http import request_json
from .server import mcp

CAL_BASE = "https://www.googleapis.com/calendar/v3"


@mcp.tool()
def calendar_events_list(
    calendarId: str = "primary",
    maxResults: int = 10,
    timeMin: Optional[str] = None,
    timeMax: Optional[str] = None,
    singleEvents: Optional[bool] = True,
    orderBy: Optional[str] = "startTime",
    q: Optional[str] = None,
    pageToken: Optional[str] = None,
    showDeleted: Optional[bool] = False,
    timeZone: Optional[str] = None,
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
    if showDeleted is not None:
        params["showDeleted"] = showDeleted
    if timeZone is not None:
        params["timeZone"] = timeZone
    return request_json("GET", url, params=params)


@mcp.tool()
def calendar_events_get(calendarId: str = "primary", eventId: str = "", maxAttendees: Optional[int] = None, timeZone: Optional[str] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}"
    params: Dict[str, Any] = {}
    if maxAttendees is not None:
        params["maxAttendees"] = maxAttendees
    if timeZone is not None:
        params["timeZone"] = timeZone
    return request_json("GET", url, params=params)


@mcp.tool()
def calendar_events_insert(calendarId: str = "primary", event: Optional[Dict[str, Any]] = None, sendUpdates: Optional[str] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events"
    params: Dict[str, Any] = {}
    if sendUpdates is not None:
        params["sendUpdates"] = sendUpdates
    return request_json("POST", url, params=params, json_body=event or {})


@mcp.tool()
def calendar_events_update(calendarId: str = "primary", eventId: str = "", event: Optional[Dict[str, Any]] = None, sendUpdates: Optional[str] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}"
    params: Dict[str, Any] = {}
    if sendUpdates is not None:
        params["sendUpdates"] = sendUpdates
    return request_json("PUT", url, params=params, json_body=event or {})


@mcp.tool()
def calendar_events_patch(calendarId: str = "primary", eventId: str = "", eventPatch: Optional[Dict[str, Any]] = None, sendUpdates: Optional[str] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}"
    params: Dict[str, Any] = {}
    if sendUpdates is not None:
        params["sendUpdates"] = sendUpdates
    return request_json("PATCH", url, params=params, json_body=eventPatch or {})


@mcp.tool()
def calendar_events_delete(calendarId: str = "primary", eventId: str = "", sendUpdates: Optional[str] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}"
    params: Dict[str, Any] = {}
    if sendUpdates is not None:
        params["sendUpdates"] = sendUpdates
    return request_json("DELETE", url, params=params)


@mcp.tool()
def calendar_events_move(calendarId: str = "primary", eventId: str = "", destination: str = "") -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/events/{eventId}/move"
    params = {"destination": destination}
    return request_json("POST", url, params=params, json_body={})


@mcp.tool()
def calendar_calendars_insert(calendar: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars"
    return request_json("POST", url, json_body=calendar or {})


@mcp.tool()
def calendar_calendars_get(calendarId: str = "primary") -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}"
    return request_json("GET", url)


@mcp.tool()
def calendar_calendars_update(calendarId: str = "", calendar: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}"
    return request_json("PUT", url, json_body=calendar or {})


@mcp.tool()
def calendar_calendars_delete(calendarId: str = "") -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}"
    return request_json("DELETE", url)


@mcp.tool()
def calendar_calendarList_list(maxResults: int = 100, pageToken: Optional[str] = None, minAccessRole: Optional[str] = None, showHidden: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/users/me/calendarList"
    params: Dict[str, Any] = {"maxResults": maxResults}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if minAccessRole is not None:
        params["minAccessRole"] = minAccessRole
    if showHidden is not None:
        params["showHidden"] = showHidden
    return request_json("GET", url, params=params)


@mcp.tool()
def calendar_calendarList_get(calendarId: str = "") -> Dict[str, Any]:
    url = f"{CAL_BASE}/users/me/calendarList/{calendarId}"
    return request_json("GET", url)


@mcp.tool()
def calendar_calendarList_insert(calendarListEntry: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/users/me/calendarList"
    return request_json("POST", url, json_body=calendarListEntry or {})


@mcp.tool()
def calendar_acl_list(calendarId: str = "primary", maxResults: int = 100, pageToken: Optional[str] = None, showDeleted: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/acl"
    params: Dict[str, Any] = {"maxResults": maxResults}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if showDeleted is not None:
        params["showDeleted"] = showDeleted
    return request_json("GET", url, params=params)


@mcp.tool()
def calendar_acl_insert(calendarId: str = "primary", rule: Optional[Dict[str, Any]] = None, sendNotifications: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/acl"
    params: Dict[str, Any] = {}
    if sendNotifications is not None:
        params["sendNotifications"] = sendNotifications
    return request_json("POST", url, params=params, json_body=rule or {})


@mcp.tool()
def calendar_acl_delete(calendarId: str = "primary", ruleId: str = "") -> Dict[str, Any]:
    url = f"{CAL_BASE}/calendars/{calendarId}/acl/{ruleId}"
    return request_json("DELETE", url)


@mcp.tool()
def calendar_freebusy_query(body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/freeBusy"
    return request_json("POST", url, json_body=body or {})


@mcp.tool()
def calendar_settings_list(maxResults: int = 100, pageToken: Optional[str] = None, syncToken: Optional[str] = None) -> Dict[str, Any]:
    url = f"{CAL_BASE}/users/me/settings"
    params: Dict[str, Any] = {"maxResults": maxResults}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if syncToken is not None:
        params["syncToken"] = syncToken
    return request_json("GET", url, params=params)


@mcp.tool()
def calendar_settings_get(setting: str = "") -> Dict[str, Any]:
    url = f"{CAL_BASE}/users/me/settings/{setting}"
    return request_json("GET", url)
