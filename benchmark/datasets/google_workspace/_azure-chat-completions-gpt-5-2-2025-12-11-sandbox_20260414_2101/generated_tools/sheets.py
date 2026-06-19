from typing import Any, Dict, List, Optional

from .http import request_json
from .server import mcp

SHEETS_BASE = "https://sheets.googleapis.com/v4/spreadsheets"


@mcp.tool()
def sheets_spreadsheets_create(spreadsheet: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}"
    return request_json("POST", url, json_body=spreadsheet or {})


@mcp.tool()
def sheets_spreadsheets_get(spreadsheetId: str = "", includeGridData: Optional[bool] = None, ranges: Optional[List[str]] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}"
    params: Dict[str, Any] = {}
    if includeGridData is not None:
        params["includeGridData"] = includeGridData
    if ranges:
        params["ranges"] = ranges
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", url, params=params)


@mcp.tool()
def sheets_spreadsheets_batchUpdate(spreadsheetId: str = "", requests: Optional[list] = None, includeSpreadsheetInResponse: Optional[bool] = None, responseIncludeGridData: Optional[bool] = None, responseRanges: Optional[List[str]] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}:batchUpdate"
    body: Dict[str, Any] = {"requests": requests or []}
    params: Dict[str, Any] = {}
    if includeSpreadsheetInResponse is not None:
        params["includeSpreadsheetInResponse"] = includeSpreadsheetInResponse
    if responseIncludeGridData is not None:
        params["responseIncludeGridData"] = responseIncludeGridData
    if responseRanges:
        params["responseRanges"] = responseRanges
    return request_json("POST", url, params=params, json_body=body)


@mcp.tool()
def sheets_spreadsheets_getByDataFilter(spreadsheetId: str = "", dataFilters: Optional[list] = None, includeGridData: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}:getByDataFilter"
    body: Dict[str, Any] = {"dataFilters": dataFilters or []}
    if includeGridData is not None:
        body["includeGridData"] = includeGridData
    return request_json("POST", url, json_body=body)


@mcp.tool()
def sheets_values_get(spreadsheetId: str = "", range: str = "", majorDimension: Optional[str] = None, valueRenderOption: Optional[str] = None, dateTimeRenderOption: Optional[str] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values/{range}"
    params: Dict[str, Any] = {}
    if majorDimension is not None:
        params["majorDimension"] = majorDimension
    if valueRenderOption is not None:
        params["valueRenderOption"] = valueRenderOption
    if dateTimeRenderOption is not None:
        params["dateTimeRenderOption"] = dateTimeRenderOption
    return request_json("GET", url, params=params)


@mcp.tool()
def sheets_values_update(
    spreadsheetId: str = "",
    range: str = "",
    values: Optional[List[List[Any]]] = None,
    valueInputOption: str = "RAW",
    majorDimension: str = "ROWS",
    includeValuesInResponse: Optional[bool] = None,
    responseValueRenderOption: Optional[str] = None,
    responseDateTimeRenderOption: Optional[str] = None,
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values/{range}"
    params: Dict[str, Any] = {"valueInputOption": valueInputOption}
    if includeValuesInResponse is not None:
        params["includeValuesInResponse"] = includeValuesInResponse
    if responseValueRenderOption is not None:
        params["responseValueRenderOption"] = responseValueRenderOption
    if responseDateTimeRenderOption is not None:
        params["responseDateTimeRenderOption"] = responseDateTimeRenderOption
    body = {"range": range, "majorDimension": majorDimension, "values": values or []}
    return request_json("PUT", url, params=params, json_body=body)


@mcp.tool()
def sheets_values_append(
    spreadsheetId: str = "",
    range: str = "",
    values: Optional[List[List[Any]]] = None,
    valueInputOption: str = "RAW",
    insertDataOption: Optional[str] = None,
    includeValuesInResponse: Optional[bool] = None,
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values/{range}:append"
    params: Dict[str, Any] = {"valueInputOption": valueInputOption}
    if insertDataOption is not None:
        params["insertDataOption"] = insertDataOption
    if includeValuesInResponse is not None:
        params["includeValuesInResponse"] = includeValuesInResponse
    body = {"range": range, "majorDimension": "ROWS", "values": values or []}
    return request_json("POST", url, params=params, json_body=body)


@mcp.tool()
def sheets_values_clear(spreadsheetId: str = "", range: str = "") -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values/{range}:clear"
    return request_json("POST", url, json_body={})


@mcp.tool()
def sheets_values_batchGet(spreadsheetId: str = "", ranges: Optional[List[str]] = None, majorDimension: Optional[str] = None, valueRenderOption: Optional[str] = None, dateTimeRenderOption: Optional[str] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchGet"
    params: Dict[str, Any] = {}
    if ranges:
        params["ranges"] = ranges
    if majorDimension is not None:
        params["majorDimension"] = majorDimension
    if valueRenderOption is not None:
        params["valueRenderOption"] = valueRenderOption
    if dateTimeRenderOption is not None:
        params["dateTimeRenderOption"] = dateTimeRenderOption
    return request_json("GET", url, params=params)


@mcp.tool()
def sheets_values_batchUpdate(spreadsheetId: str = "", data: Optional[list] = None, valueInputOption: str = "RAW", includeValuesInResponse: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchUpdate"
    params: Dict[str, Any] = {"valueInputOption": valueInputOption}
    if includeValuesInResponse is not None:
        params["includeValuesInResponse"] = includeValuesInResponse
    body: Dict[str, Any] = {"valueInputOption": valueInputOption, "data": data or []}
    return request_json("POST", url, params=params, json_body=body)


@mcp.tool()
def sheets_values_batchClear(spreadsheetId: str = "", ranges: Optional[List[str]] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchClear"
    body = {"ranges": ranges or []}
    return request_json("POST", url, json_body=body)


@mcp.tool()
def sheets_values_batchGetByDataFilter(spreadsheetId: str = "", dataFilters: Optional[list] = None, majorDimension: Optional[str] = None, valueRenderOption: Optional[str] = None, dateTimeRenderOption: Optional[str] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchGetByDataFilter"
    body: Dict[str, Any] = {"dataFilters": dataFilters or []}
    if majorDimension is not None:
        body["majorDimension"] = majorDimension
    if valueRenderOption is not None:
        body["valueRenderOption"] = valueRenderOption
    if dateTimeRenderOption is not None:
        body["dateTimeRenderOption"] = dateTimeRenderOption
    return request_json("POST", url, json_body=body)


@mcp.tool()
def sheets_values_batchUpdateByDataFilter(spreadsheetId: str = "", data: Optional[list] = None, valueInputOption: str = "RAW", includeValuesInResponse: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchUpdateByDataFilter"
    body: Dict[str, Any] = {"valueInputOption": valueInputOption, "data": data or []}
    if includeValuesInResponse is not None:
        body["includeValuesInResponse"] = includeValuesInResponse
    return request_json("POST", url, json_body=body)


@mcp.tool()
def sheets_values_batchClearByDataFilter(spreadsheetId: str = "", dataFilters: Optional[list] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchClearByDataFilter"
    body: Dict[str, Any] = {"dataFilters": dataFilters or []}
    return request_json("POST", url, json_body=body)


@mcp.tool()
def sheets_spreadsheets_sheets_copyTo(spreadsheetId: str = "", sheetId: int = 0, destinationSpreadsheetId: str = "") -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/sheets/{sheetId}:copyTo"
    body = {"destinationSpreadsheetId": destinationSpreadsheetId}
    return request_json("POST", url, json_body=body)


@mcp.tool()
def sheets_developerMetadata_get(spreadsheetId: str = "", metadataId: int = 0) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/developerMetadata/{metadataId}"
    return request_json("GET", url)


@mcp.tool()
def sheets_developerMetadata_search(spreadsheetId: str = "", dataFilters: Optional[list] = None) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/developerMetadata:search"
    body = {"dataFilters": dataFilters or []}
    return request_json("POST", url, json_body=body)
