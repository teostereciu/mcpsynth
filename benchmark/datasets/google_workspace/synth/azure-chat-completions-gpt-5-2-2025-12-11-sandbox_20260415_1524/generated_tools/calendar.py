from typing import Any, Dict, Optional

from .http import request_json

CAL_BASE = "https://www.googleapis.com/calendar/v3"


def calendar_events_list(calendarId: str = "primary", *, timeMin: Optional[str] = None, timeMax: Optional[str] = None, q: Optional[str] = None, maxResults: Optional[int] = None, pageToken: Optional[str] = None, singleEvents: Optional[bool] = None, orderBy: Optional[str] = None, showDeleted: Optional[bool] = None, timeZone: Optional[str] = None, syncToken: Optional[str] = None) -> Any:
    url = f"{CAL_BASE}/calendars/{calendarId}/events"
    params: Dict[str, Any] = {}
    for k, v in {
        "timeMin": timeMin,
        "timeMax": timeMax,
        "q": q,
        "maxResults": maxResults,
        "pageToken": pageToken,
        "singleEvents": singleEvents,
        "orderBy": orderBy,
        "showDeleted": showDeleted,
        "timeZone": timeZone,
        "syncToken": syncToken,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", url, params=params)
