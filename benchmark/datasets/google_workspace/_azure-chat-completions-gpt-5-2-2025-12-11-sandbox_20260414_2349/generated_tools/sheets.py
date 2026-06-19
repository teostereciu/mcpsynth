from typing import Any, Dict, List, Optional

from .http import request_json

SHEETS_BASE = "https://sheets.googleapis.com/v4/spreadsheets"


def sheets_spreadsheets_create(*, title: str, sheets: Optional[List[Dict[str, Any]]] = None) -> Any:
    body: Dict[str, Any] = {"properties": {"title": title}}
    if sheets is not None:
        body["sheets"] = sheets
    return request_json("POST", f"{SHEETS_BASE}", json_body=body)


def sheets_spreadsheets_get(spreadsheetId: str, *, includeGridData: Optional[bool] = None, ranges: Optional[List[str]] = None, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if includeGridData is not None:
        params["includeGridData"] = includeGridData
    if ranges:
        params["ranges"] = ranges
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"{SHEETS_BASE}/{spreadsheetId}", params=params)


def sheets_spreadsheets_batchUpdate(spreadsheetId: str, *, requests: List[Dict[str, Any]], includeSpreadsheetInResponse: Optional[bool] = None, responseIncludeGridData: Optional[bool] = None, responseRanges: Optional[List[str]] = None) -> Any:
    params: Dict[str, Any] = {}
    if includeSpreadsheetInResponse is not None:
        params["includeSpreadsheetInResponse"] = includeSpreadsheetInResponse
    if responseIncludeGridData is not None:
        params["responseIncludeGridData"] = responseIncludeGridData
    if responseRanges is not None:
        params["responseRanges"] = responseRanges
    body: Dict[str, Any] = {"requests": requests}
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheetId}:batchUpdate", params=params, json_body=body)


def sheets_spreadsheets_getByDataFilter(spreadsheetId: str, *, dataFilters: List[Dict[str, Any]], includeGridData: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {"dataFilters": dataFilters}
    if includeGridData is not None:
        body["includeGridData"] = includeGridData
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheetId}:getByDataFilter", json_body=body)


def sheets_values_get(spreadsheetId: str, range: str, *, majorDimension: Optional[str] = None, valueRenderOption: Optional[str] = None, dateTimeRenderOption: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if majorDimension is not None:
        params["majorDimension"] = majorDimension
    if valueRenderOption is not None:
        params["valueRenderOption"] = valueRenderOption
    if dateTimeRenderOption is not None:
        params["dateTimeRenderOption"] = dateTimeRenderOption
    return request_json("GET", f"{SHEETS_BASE}/{spreadsheetId}/values/{range}", params=params)


def sheets_values_update(
    spreadsheetId: str,
    range: str,
    *,
    values: List[List[Any]],
    valueInputOption: str = "RAW",
    majorDimension: str = "ROWS",
    includeValuesInResponse: Optional[bool] = None,
    responseValueRenderOption: Optional[str] = None,
    responseDateTimeRenderOption: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"valueInputOption": valueInputOption}
    if includeValuesInResponse is not None:
        params["includeValuesInResponse"] = includeValuesInResponse
    if responseValueRenderOption is not None:
        params["responseValueRenderOption"] = responseValueRenderOption
    if responseDateTimeRenderOption is not None:
        params["responseDateTimeRenderOption"] = responseDateTimeRenderOption
    body: Dict[str, Any] = {"range": range, "majorDimension": majorDimension, "values": values}
    return request_json("PUT", f"{SHEETS_BASE}/{spreadsheetId}/values/{range}", params=params, json_body=body)


def sheets_values_append(
    spreadsheetId: str,
    range: str,
    *,
    values: List[List[Any]],
    valueInputOption: str = "RAW",
    insertDataOption: Optional[str] = None,
    includeValuesInResponse: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {"valueInputOption": valueInputOption}
    if insertDataOption is not None:
        params["insertDataOption"] = insertDataOption
    if includeValuesInResponse is not None:
        params["includeValuesInResponse"] = includeValuesInResponse
    body: Dict[str, Any] = {"range": range, "majorDimension": "ROWS", "values": values}
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheetId}/values/{range}:append", params=params, json_body=body)


def sheets_values_clear(spreadsheetId: str, range: str) -> Any:
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheetId}/values/{range}:clear", json_body={})


def sheets_values_batchGet(spreadsheetId: str, *, ranges: List[str], majorDimension: Optional[str] = None, valueRenderOption: Optional[str] = None, dateTimeRenderOption: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    params["ranges"] = ranges
    if majorDimension is not None:
        params["majorDimension"] = majorDimension
    if valueRenderOption is not None:
        params["valueRenderOption"] = valueRenderOption
    if dateTimeRenderOption is not None:
        params["dateTimeRenderOption"] = dateTimeRenderOption
    return request_json("GET", f"{SHEETS_BASE}/{spreadsheetId}/values:batchGet", params=params)


def sheets_values_batchUpdate(spreadsheetId: str, *, data: List[Dict[str, Any]], valueInputOption: str = "RAW", includeValuesInResponse: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {"valueInputOption": valueInputOption}
    if includeValuesInResponse is not None:
        params["includeValuesInResponse"] = includeValuesInResponse
    body: Dict[str, Any] = {"data": data, "valueInputOption": valueInputOption}
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheetId}/values:batchUpdate", params=params, json_body=body)


def sheets_values_batchClear(spreadsheetId: str, *, ranges: List[str]) -> Any:
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheetId}/values:batchClear", json_body={"ranges": ranges})


def sheets_sheets_copyTo(spreadsheetId: str, sheetId: int, *, destinationSpreadsheetId: str) -> Any:
    return request_json(
        "POST",
        f"{SHEETS_BASE}/{spreadsheetId}/sheets/{sheetId}/copyTo",
        json_body={"destinationSpreadsheetId": destinationSpreadsheetId},
    )


def sheets_developerMetadata_get(spreadsheetId: str, metadataId: int) -> Any:
    return request_json("GET", f"{SHEETS_BASE}/{spreadsheetId}/developerMetadata/{metadataId}")


def sheets_developerMetadata_search(spreadsheetId: str, *, dataFilters: List[Dict[str, Any]]) -> Any:
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheetId}/developerMetadata:search", json_body={"dataFilters": dataFilters})
