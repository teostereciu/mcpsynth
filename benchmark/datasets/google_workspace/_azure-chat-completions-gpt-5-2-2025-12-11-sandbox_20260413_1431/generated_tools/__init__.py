"""Generated Google Workspace MCP tools package."""

from __future__ import annotations

from fastmcp import FastMCP

from . import calendar as _calendar
from . import docs as _docs
from . import drive as _drive
from . import gmail as _gmail
from . import sheets as _sheets
from . import slides as _slides

mcp = FastMCP("google-workspace")

# Gmail
mcp.tool()(_gmail.gmail_get_profile)
mcp.tool()(_gmail.gmail_messages_list)
mcp.tool()(_gmail.gmail_messages_get)
mcp.tool()(_gmail.gmail_messages_send)
mcp.tool()(_gmail.gmail_drafts_create)
mcp.tool()(_gmail.gmail_labels_create)

# Calendar
mcp.tool()(_calendar.calendar_events_list)
mcp.tool()(_calendar.calendar_events_insert)
mcp.tool()(_calendar.calendar_events_get)
mcp.tool()(_calendar.calendar_events_delete)
mcp.tool()(_calendar.calendar_events_patch)
mcp.tool()(_calendar.calendar_events_update)
mcp.tool()(_calendar.calendar_freebusy_query)
mcp.tool()(_calendar.calendar_calendarlist_list)
mcp.tool()(_calendar.calendar_calendars_insert)
mcp.tool()(_calendar.calendar_calendars_get)

# Drive
mcp.tool()(_drive.drive_files_create)
mcp.tool()(_drive.drive_files_list)
mcp.tool()(_drive.drive_files_get)
mcp.tool()(_drive.drive_permissions_create)
mcp.tool()(_drive.drive_permissions_list)
mcp.tool()(_drive.drive_permissions_delete)

# Docs
mcp.tool()(_docs.docs_documents_create)
mcp.tool()(_docs.docs_documents_get)
mcp.tool()(_docs.docs_documents_batch_update)

# Slides
mcp.tool()(_slides.slides_presentations_create)
mcp.tool()(_slides.slides_presentations_get)
mcp.tool()(_slides.slides_presentations_batch_update)
mcp.tool()(_slides.slides_pages_get)
mcp.tool()(_slides.slides_pages_get_thumbnail)

# Sheets
mcp.tool()(_sheets.sheets_spreadsheets_create)
mcp.tool()(_sheets.sheets_spreadsheets_get)
mcp.tool()(_sheets.sheets_spreadsheets_batch_update)
mcp.tool()(_sheets.sheets_values_get)
mcp.tool()(_sheets.sheets_values_update)
mcp.tool()(_sheets.sheets_values_append)
mcp.tool()(_sheets.sheets_values_batch_get)
mcp.tool()(_sheets.sheets_values_batch_update)
mcp.tool()(_sheets.sheets_values_clear)
mcp.tool()(_sheets.sheets_values_batch_clear)
mcp.tool()(_sheets.sheets_sheets_copy_to)
