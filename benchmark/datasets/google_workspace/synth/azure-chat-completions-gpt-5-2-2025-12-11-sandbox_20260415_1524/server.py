from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.gmail import gmail_messages_get, gmail_messages_list
from generated_tools.calendar import calendar_events_list
from generated_tools.drive import drive_files_list
from generated_tools.docs_api import docs_documents_get
from generated_tools.slides import slides_presentations_get
from generated_tools.sheets import sheets_values_get

mcp = FastMCP("google-workspace")


@mcp.tool()
def gmail_messages_list_tool(userId: str = "me", maxResults: Optional[int] = None, pageToken: Optional[str] = None, q: Optional[str] = None, labelIds: Optional[list[str]] = None, includeSpamTrash: Optional[bool] = None) -> Any:
    return gmail_messages_list(userId, maxResults=maxResults, pageToken=pageToken, q=q, labelIds=labelIds, includeSpamTrash=includeSpamTrash)


@mcp.tool()
def gmail_messages_get_tool(userId: str = "me", id: str = "", format: Optional[str] = None, metadataHeaders: Optional[list[str]] = None) -> Any:
    if not id:
        return {"error": "id is required"}
    return gmail_messages_get(userId, id=id, format=format, metadataHeaders=metadataHeaders)


@mcp.tool()
def calendar_events_list_tool(calendarId: str = "primary", timeMin: Optional[str] = None, timeMax: Optional[str] = None, q: Optional[str] = None, maxResults: Optional[int] = None, pageToken: Optional[str] = None, singleEvents: Optional[bool] = None, orderBy: Optional[str] = None, showDeleted: Optional[bool] = None, timeZone: Optional[str] = None, syncToken: Optional[str] = None) -> Any:
    return calendar_events_list(calendarId, timeMin=timeMin, timeMax=timeMax, q=q, maxResults=maxResults, pageToken=pageToken, singleEvents=singleEvents, orderBy=orderBy, showDeleted=showDeleted, timeZone=timeZone, syncToken=syncToken)


@mcp.tool()
def drive_files_list_tool(q: Optional[str] = None, pageSize: Optional[int] = None, pageToken: Optional[str] = None, corpora: Optional[str] = None, driveId: Optional[str] = None, includeItemsFromAllDrives: Optional[bool] = None, supportsAllDrives: Optional[bool] = None, orderBy: Optional[str] = None, spaces: Optional[str] = None, fields: Optional[str] = None) -> Any:
    return drive_files_list(q=q, pageSize=pageSize, pageToken=pageToken, corpora=corpora, driveId=driveId, includeItemsFromAllDrives=includeItemsFromAllDrives, supportsAllDrives=supportsAllDrives, orderBy=orderBy, spaces=spaces, fields=fields)


@mcp.tool()
def docs_documents_get_tool(documentId: str = "", suggestionsViewMode: Optional[str] = None, includeTabsContent: Optional[bool] = None) -> Any:
    if not documentId:
        return {"error": "documentId is required"}
    return docs_documents_get(documentId=documentId, suggestionsViewMode=suggestionsViewMode, includeTabsContent=includeTabsContent)


@mcp.tool()
def slides_presentations_get_tool(presentationId: str = "") -> Any:
    if not presentationId:
        return {"error": "presentationId is required"}
    return slides_presentations_get(presentationId=presentationId)


@mcp.tool()
def sheets_values_get_tool(spreadsheetId: str = "", range: str = "", majorDimension: Optional[str] = None, valueRenderOption: Optional[str] = None, dateTimeRenderOption: Optional[str] = None) -> Any:
    if not spreadsheetId or not range:
        return {"error": "spreadsheetId and range are required"}
    return sheets_values_get(spreadsheetId=spreadsheetId, range=range, majorDimension=majorDimension, valueRenderOption=valueRenderOption, dateTimeRenderOption=dateTimeRenderOption)


if __name__ == "__main__":
    mcp.run()
