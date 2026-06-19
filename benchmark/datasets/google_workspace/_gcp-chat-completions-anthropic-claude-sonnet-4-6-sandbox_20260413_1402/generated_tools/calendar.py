"""Google Calendar API tools for the Google Workspace MCP Server."""

from typing import Any, Optional

import requests

from generated_tools import mcp
from generated_tools.auth import (
    CALENDAR_BASE,
    api_delete,
    api_get,
    api_patch,
    api_post,
    api_put,
    handle_http_error,
)


# ---------------------------------------------------------------------------
# Events
# ---------------------------------------------------------------------------


@mcp.tool()
def calendar_list_events(
    calendar_id: str = "primary",
    max_results: int = 250,
    time_min: Optional[str] = None,
    time_max: Optional[str] = None,
    q: Optional[str] = None,
    order_by: Optional[str] = None,
    single_events: bool = False,
    page_token: Optional[str] = None,
    show_deleted: bool = False,
    time_zone: Optional[str] = None,
) -> dict:
    """List events on a Google Calendar.

    Args:
        calendar_id: Calendar identifier. Use 'primary' for the user's primary calendar.
        max_results: Maximum number of events to return (default 250, max 2500).
        time_min: Lower bound for event end time (RFC3339, e.g. '2026-01-01T00:00:00Z').
        time_max: Upper bound for event start time (RFC3339).
        q: Free text search query.
        order_by: Sort order: 'startTime' or 'updated'.
        single_events: Expand recurring events into instances.
        page_token: Page token for pagination.
        show_deleted: Include deleted events.
        time_zone: Time zone for the response.
    """
    try:
        params: dict[str, Any] = {
            "maxResults": max_results,
            "showDeleted": show_deleted,
            "singleEvents": single_events,
        }
        if time_min:
            params["timeMin"] = time_min
        if time_max:
            params["timeMax"] = time_max
        if q:
            params["q"] = q
        if order_by:
            params["orderBy"] = order_by
        if page_token:
            params["pageToken"] = page_token
        if time_zone:
            params["timeZone"] = time_zone
        return api_get(f"{CALENDAR_BASE}/calendars/{calendar_id}/events", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_get_event(event_id: str, calendar_id: str = "primary") -> dict:
    """Get a specific Google Calendar event by ID.

    Args:
        event_id: The event identifier.
        calendar_id: Calendar identifier. Use 'primary' for the user's primary calendar.
    """
    try:
        return api_get(f"{CALENDAR_BASE}/calendars/{calendar_id}/events/{event_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_create_event(
    summary: str,
    start_datetime: str,
    end_datetime: str,
    calendar_id: str = "primary",
    description: Optional[str] = None,
    location: Optional[str] = None,
    attendees: Optional[list] = None,
    time_zone: Optional[str] = None,
    recurrence: Optional[list] = None,
    color_id: Optional[str] = None,
    visibility: Optional[str] = None,
    reminders_use_default: bool = True,
    reminder_overrides: Optional[list] = None,
    all_day: bool = False,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> dict:
    """Create a new event on a Google Calendar.

    Args:
        summary: Title of the event.
        start_datetime: Start time in RFC3339 format (e.g. '2026-01-15T10:00:00-05:00').
        end_datetime: End time in RFC3339 format.
        calendar_id: Calendar identifier. Use 'primary' for the user's primary calendar.
        description: Description of the event (can contain HTML).
        location: Geographic location as free-form text.
        attendees: List of attendee dicts with 'email' key (e.g. [{'email': 'user@example.com'}]).
        time_zone: IANA time zone name (e.g. 'America/New_York').
        recurrence: List of RRULE strings for recurring events.
        color_id: Color ID for the event.
        visibility: Event visibility: 'default', 'public', 'private', or 'confidential'.
        reminders_use_default: Whether to use the calendar's default reminders.
        reminder_overrides: List of reminder dicts with 'method' and 'minutes' keys.
        all_day: If True, use date-only format (requires start_date and end_date).
        start_date: Start date for all-day events (YYYY-MM-DD format).
        end_date: End date for all-day events (YYYY-MM-DD format).
    """
    try:
        if all_day and start_date and end_date:
            start = {"date": start_date}
            end = {"date": end_date}
        else:
            start = {"dateTime": start_datetime}
            end = {"dateTime": end_datetime}
            if time_zone:
                start["timeZone"] = time_zone
                end["timeZone"] = time_zone

        payload: dict[str, Any] = {"summary": summary, "start": start, "end": end}
        if description:
            payload["description"] = description
        if location:
            payload["location"] = location
        if attendees:
            payload["attendees"] = attendees
        if recurrence:
            payload["recurrence"] = recurrence
        if color_id:
            payload["colorId"] = color_id
        if visibility:
            payload["visibility"] = visibility

        reminders: dict[str, Any] = {"useDefault": reminders_use_default}
        if reminder_overrides:
            reminders["overrides"] = reminder_overrides
            reminders["useDefault"] = False
        payload["reminders"] = reminders

        return api_post(
            f"{CALENDAR_BASE}/calendars/{calendar_id}/events", payload=payload
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_update_event(
    event_id: str,
    summary: str,
    start_datetime: str,
    end_datetime: str,
    calendar_id: str = "primary",
    description: Optional[str] = None,
    location: Optional[str] = None,
    attendees: Optional[list] = None,
    time_zone: Optional[str] = None,
    status: Optional[str] = None,
) -> dict:
    """Update (replace) an existing Google Calendar event.

    Args:
        event_id: The event identifier.
        summary: Title of the event.
        start_datetime: Start time in RFC3339 format.
        end_datetime: End time in RFC3339 format.
        calendar_id: Calendar identifier. Use 'primary' for the user's primary calendar.
        description: Description of the event.
        location: Geographic location as free-form text.
        attendees: List of attendee dicts with 'email' key.
        time_zone: IANA time zone name.
        status: Event status: 'confirmed', 'tentative', or 'cancelled'.
    """
    try:
        start: dict[str, str] = {"dateTime": start_datetime}
        end: dict[str, str] = {"dateTime": end_datetime}
        if time_zone:
            start["timeZone"] = time_zone
            end["timeZone"] = time_zone

        payload: dict[str, Any] = {"summary": summary, "start": start, "end": end}
        if description is not None:
            payload["description"] = description
        if location is not None:
            payload["location"] = location
        if attendees is not None:
            payload["attendees"] = attendees
        if status is not None:
            payload["status"] = status

        return api_put(
            f"{CALENDAR_BASE}/calendars/{calendar_id}/events/{event_id}",
            payload=payload,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_patch_event(
    event_id: str,
    calendar_id: str = "primary",
    summary: Optional[str] = None,
    description: Optional[str] = None,
    location: Optional[str] = None,
    start_datetime: Optional[str] = None,
    end_datetime: Optional[str] = None,
    time_zone: Optional[str] = None,
    status: Optional[str] = None,
    attendees: Optional[list] = None,
) -> dict:
    """Partially update a Google Calendar event (patch semantics).

    Args:
        event_id: The event identifier.
        calendar_id: Calendar identifier. Use 'primary' for the user's primary calendar.
        summary: New title for the event.
        description: New description for the event.
        location: New location for the event.
        start_datetime: New start time in RFC3339 format.
        end_datetime: New end time in RFC3339 format.
        time_zone: IANA time zone name.
        status: Event status: 'confirmed', 'tentative', or 'cancelled'.
        attendees: New list of attendee dicts.
    """
    try:
        payload: dict[str, Any] = {}
        if summary is not None:
            payload["summary"] = summary
        if description is not None:
            payload["description"] = description
        if location is not None:
            payload["location"] = location
        if start_datetime is not None:
            start: dict[str, str] = {"dateTime": start_datetime}
            if time_zone:
                start["timeZone"] = time_zone
            payload["start"] = start
        if end_datetime is not None:
            end: dict[str, str] = {"dateTime": end_datetime}
            if time_zone:
                end["timeZone"] = time_zone
            payload["end"] = end
        if status is not None:
            payload["status"] = status
        if attendees is not None:
            payload["attendees"] = attendees

        return api_patch(
            f"{CALENDAR_BASE}/calendars/{calendar_id}/events/{event_id}",
            payload=payload,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_delete_event(
    event_id: str,
    calendar_id: str = "primary",
    send_updates: str = "none",
) -> dict:
    """Delete a Google Calendar event.

    Args:
        event_id: The event identifier.
        calendar_id: Calendar identifier. Use 'primary' for the user's primary calendar.
        send_updates: Who to notify: 'all', 'externalOnly', or 'none'.
    """
    try:
        return api_delete(
            f"{CALENDAR_BASE}/calendars/{calendar_id}/events/{event_id}",
            params={"sendUpdates": send_updates},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_move_event(
    event_id: str,
    destination_calendar_id: str,
    source_calendar_id: str = "primary",
) -> dict:
    """Move a Google Calendar event to another calendar.

    Args:
        event_id: The event identifier.
        destination_calendar_id: Target calendar identifier.
        source_calendar_id: Source calendar identifier (default 'primary').
    """
    try:
        return api_post(
            f"{CALENDAR_BASE}/calendars/{source_calendar_id}/events/{event_id}/move",
            params={"destination": destination_calendar_id},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Calendars (secondary calendar management)
# ---------------------------------------------------------------------------


@mcp.tool()
def calendar_create_calendar(
    summary: str,
    description: Optional[str] = None,
    time_zone: Optional[str] = None,
    location: Optional[str] = None,
) -> dict:
    """Create a new secondary Google Calendar.

    Args:
        summary: Title of the calendar.
        description: Description of the calendar.
        time_zone: IANA time zone name (e.g. 'America/New_York').
        location: Geographic location of the calendar.
    """
    try:
        payload: dict[str, Any] = {"summary": summary}
        if description:
            payload["description"] = description
        if time_zone:
            payload["timeZone"] = time_zone
        if location:
            payload["location"] = location
        return api_post(f"{CALENDAR_BASE}/calendars", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_get_calendar(calendar_id: str) -> dict:
    """Get metadata for a Google Calendar.

    Args:
        calendar_id: Calendar identifier. Use 'primary' for the user's primary calendar.
    """
    try:
        return api_get(f"{CALENDAR_BASE}/calendars/{calendar_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_update_calendar(
    calendar_id: str,
    summary: Optional[str] = None,
    description: Optional[str] = None,
    time_zone: Optional[str] = None,
    location: Optional[str] = None,
) -> dict:
    """Update a Google Calendar's metadata.

    Args:
        calendar_id: Calendar identifier.
        summary: New title for the calendar.
        description: New description for the calendar.
        time_zone: New IANA time zone name.
        location: New geographic location.
    """
    try:
        payload: dict[str, Any] = {}
        if summary is not None:
            payload["summary"] = summary
        if description is not None:
            payload["description"] = description
        if time_zone is not None:
            payload["timeZone"] = time_zone
        if location is not None:
            payload["location"] = location
        return api_put(f"{CALENDAR_BASE}/calendars/{calendar_id}", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_delete_calendar(calendar_id: str) -> dict:
    """Delete a secondary Google Calendar.

    Args:
        calendar_id: Calendar identifier (cannot be 'primary').
    """
    try:
        return api_delete(f"{CALENDAR_BASE}/calendars/{calendar_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Calendar List
# ---------------------------------------------------------------------------


@mcp.tool()
def calendar_list_calendars(
    max_results: int = 100,
    min_access_role: Optional[str] = None,
    show_hidden: bool = False,
    page_token: Optional[str] = None,
) -> dict:
    """List all calendars on the user's calendar list.

    Args:
        max_results: Maximum number of entries to return (default 100, max 250).
        min_access_role: Minimum access role: 'freeBusyReader', 'reader', 'writer', or 'owner'.
        show_hidden: Whether to show hidden entries.
        page_token: Page token for pagination.
    """
    try:
        params: dict[str, Any] = {
            "maxResults": max_results,
            "showHidden": show_hidden,
        }
        if min_access_role:
            params["minAccessRole"] = min_access_role
        if page_token:
            params["pageToken"] = page_token
        return api_get(f"{CALENDAR_BASE}/users/me/calendarList", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_get_calendar_list_entry(calendar_id: str) -> dict:
    """Get a specific calendar from the user's calendar list.

    Args:
        calendar_id: Calendar identifier.
    """
    try:
        return api_get(f"{CALENDAR_BASE}/users/me/calendarList/{calendar_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# ACL (Access Control)
# ---------------------------------------------------------------------------


@mcp.tool()
def calendar_list_acl(calendar_id: str = "primary") -> dict:
    """List access control rules for a Google Calendar.

    Args:
        calendar_id: Calendar identifier. Use 'primary' for the user's primary calendar.
    """
    try:
        return api_get(f"{CALENDAR_BASE}/calendars/{calendar_id}/acl")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_insert_acl(
    calendar_id: str,
    role: str,
    scope_type: str,
    scope_value: Optional[str] = None,
) -> dict:
    """Create an access control rule for a Google Calendar.

    Args:
        calendar_id: Calendar identifier.
        role: Access role: 'none', 'freeBusyReader', 'reader', 'writer', or 'owner'.
        scope_type: Scope type: 'default', 'user', 'group', or 'domain'.
        scope_value: Email address or domain name (omit for 'default' scope).
    """
    try:
        scope: dict[str, str] = {"type": scope_type}
        if scope_value:
            scope["value"] = scope_value
        return api_post(
            f"{CALENDAR_BASE}/calendars/{calendar_id}/acl",
            payload={"role": role, "scope": scope},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_delete_acl(calendar_id: str, rule_id: str) -> dict:
    """Delete an access control rule from a Google Calendar.

    Args:
        calendar_id: Calendar identifier.
        rule_id: The ACL rule identifier.
    """
    try:
        return api_delete(f"{CALENDAR_BASE}/calendars/{calendar_id}/acl/{rule_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Free/Busy
# ---------------------------------------------------------------------------


@mcp.tool()
def calendar_query_freebusy(
    time_min: str,
    time_max: str,
    calendar_ids: list,
    time_zone: str = "UTC",
) -> dict:
    """Query free/busy information for a set of calendars.

    Args:
        time_min: Start of the interval (RFC3339 format, e.g. '2026-01-15T09:00:00Z').
        time_max: End of the interval (RFC3339 format).
        calendar_ids: List of calendar IDs to query (e.g. ['primary', 'user@example.com']).
        time_zone: Time zone for the response (default 'UTC').
    """
    try:
        items = [{"id": cal_id} for cal_id in calendar_ids]
        return api_post(
            f"{CALENDAR_BASE}/freeBusy",
            payload={
                "timeMin": time_min,
                "timeMax": time_max,
                "timeZone": time_zone,
                "items": items,
            },
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------


@mcp.tool()
def calendar_get_setting(setting: str) -> dict:
    """Get a specific Google Calendar user setting.

    Args:
        setting: The setting identifier (e.g. 'timezone', 'dateFieldOrder', 'weekStart').
    """
    try:
        return api_get(f"{CALENDAR_BASE}/users/me/settings/{setting}")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def calendar_list_settings() -> dict:
    """List all Google Calendar user settings.

    Returns all available calendar settings for the authenticated user.
    """
    try:
        return api_get(f"{CALENDAR_BASE}/users/me/settings")
    except requests.HTTPError as e:
        return handle_http_error(e)
