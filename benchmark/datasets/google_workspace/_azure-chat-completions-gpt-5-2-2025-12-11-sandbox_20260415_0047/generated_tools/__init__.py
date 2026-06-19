from __future__ import annotations

from fastmcp import FastMCP

from .gmail import (
    gmail_get_profile,
    gmail_messages_get,
    gmail_messages_list,
    gmail_labels_create,
    gmail_drafts_create,
)
from .calendar import (
    calendar_events_get,
    calendar_events_insert,
    calendar_events_list,
)
from .drive import (
    drive_files_create,
    drive_files_get,
    drive_files_list,
    drive_permissions_create,
)
from .docs import (
    docs_documents_batch_update,
    docs_documents_create,
    docs_documents_get,
)
from .slides import (
    slides_presentations_batch_update,
    slides_presentations_create,
    slides_presentations_get,
)
from .sheets import (
    sheets_sheets_copy_to,
    sheets_spreadsheets_batch_update,
    sheets_spreadsheets_create,
    sheets_spreadsheets_get,
    sheets_values_append,
    sheets_values_batch_clear,
    sheets_values_batch_get,
    sheets_values_batch_update,
    sheets_values_clear,
    sheets_values_get,
    sheets_values_update,
)

mcp = FastMCP("google-workspace")

# Gmail
mcp.tool()(gmail_get_profile)
mcp.tool()(gmail_messages_list)
mcp.tool()(gmail_messages_get)
mcp.tool()(gmail_labels_create)
mcp.tool()(gmail_drafts_create)

# Calendar
mcp.tool()(calendar_events_list)
mcp.tool()(calendar_events_get)
mcp.tool()(calendar_events_insert)

# Drive
mcp.tool()(drive_files_create)
mcp.tool()(drive_files_list)
mcp.tool()(drive_files_get)
mcp.tool()(drive_permissions_create)

# Docs
mcp.tool()(docs_documents_create)
mcp.tool()(docs_documents_get)
mcp.tool()(docs_documents_batch_update)

# Slides
mcp.tool()(slides_presentations_create)
mcp.tool()(slides_presentations_get)
mcp.tool()(slides_presentations_batch_update)

# Sheets
mcp.tool()(sheets_spreadsheets_create)
mcp.tool()(sheets_spreadsheets_get)
mcp.tool()(sheets_spreadsheets_batch_update)
mcp.tool()(sheets_values_get)
mcp.tool()(sheets_values_update)
mcp.tool()(sheets_values_append)
mcp.tool()(sheets_values_batch_get)
mcp.tool()(sheets_values_batch_update)
mcp.tool()(sheets_values_clear)
mcp.tool()(sheets_values_batch_clear)
mcp.tool()(sheets_sheets_copy_to)
