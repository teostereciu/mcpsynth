from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import request_json

SHEETS_BASE = "https://sheets.googleapis.com/v4/spreadsheets"


def sheets_spreadsheets_create(*, title: str) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}"
    body = {"properties": {"title": title}}
    return request_json("POST", url, json_body=body)


def sheets_spreadsheets_get(
    spreadsheetId: str,
    *,
    includeGridData: Optional[bool] = None,
    ranges: Optional[List[str]] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}"
    params: Dict[str, Any] = {}
    if includeGridData is not None:
        params["includeGridData"] = includeGridData
    if ranges is not None:
        params["ranges"] = ranges
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", url, params=params)


def sheets_values_get(
    spreadsheetId: str,
    range: str,
    *,
    majorDimension: Optional[str] = None,
    valueRenderOption: Optional[str] = None,
    dateTimeRenderOption: Optional[str] = None,
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values/{range}"
    params: Dict[str, Any] = {}
    if majorDimension is not None:
        params["majorDimension"] = majorDimension
    if valueRenderOption is not None:
        params["valueRenderOption"] = valueRenderOption
    if dateTimeRenderOption is not None:
        params["dateTimeRenderOption"] = dateTimeRenderOption
    return request_json("GET", url, params=params)


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
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values/{range}"
    params: Dict[str, Any] = {"valueInputOption": valueInputOption}
    if includeValuesInResponse is not None:
        params["includeValuesInResponse"] = includeValuesInResponse
    if responseValueRenderOption is not None:
        params["responseValueRenderOption"] = responseValueRenderOption
    if responseDateTimeRenderOption is not None:
        params["responseDateTimeRenderOption"] = responseDateTimeRenderOption
    body = {"range": range, "majorDimension": majorDimension, "values": values}
    return request_json("PUT", url, params=params, json_body=body)


def sheets_values_append(
    spreadsheetId: str,
    range: str,
    *,
    values: List[List[Any]],
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
    body = {"range": range, "majorDimension": "ROWS", "values": values}
    return request_json("POST", url, params=params, json_body=body)


def sheets_values_batch_get(
    spreadsheetId: str,
    *,
    ranges: List[str],
    majorDimension: Optional[str] = None,
    valueRenderOption: Optional[str] = None,
    dateTimeRenderOption: Optional[str] = None,
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchGet"
    params: Dict[str, Any] = {"ranges": ranges}
    if majorDimension is not None:
        params["majorDimension"] = majorDimension
    if valueRenderOption is not None:
        params["valueRenderOption"] = valueRenderOption
    if dateTimeRenderOption is not None:
        params["dateTimeRenderOption"] = dateTimeRenderOption
    return request_json("GET", url, params=params)


def sheets_values_batch_update(
    spreadsheetId: str,
    *,
    data: List[Dict[str, Any]],
    valueInputOption: str = "RAW",
    includeValuesInResponse: Optional[bool] = None,
    responseValueRenderOption: Optional[str] = None,
    responseDateTimeRenderOption: Optional[str] = None,
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchUpdate"
    params: Dict[str, Any] = {"valueInputOption": valueInputOption}
    if includeValuesInResponse is not None:
        params["includeValuesInResponse"] = includeValuesInResponse
    if responseValueRenderOption is not None:
        params["responseValueRenderOption"] = responseValueRenderOption
    if responseDateTimeRenderOption is not None:
        params["responseDateTimeRenderOption"] = responseDateTimeRenderOption
    body: Dict[str, Any] = {"valueInputOption": valueInputOption, "data": data}
    return request_json("POST", url, params=params, json_body=body)


def sheets_values_clear(spreadsheetId: str, range: str) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values/{range}:clear"
    return request_json("POST", url, json_body={})


def sheets_values_batch_clear(spreadsheetId: str, *, ranges: List[str]) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values:batchClear"
    return request_json("POST", url, json_body={"ranges": ranges})


def sheets_spreadsheets_batch_update(
    spreadsheetId: str,
    *,
    requests: List[Dict[str, Any]],
    includeSpreadsheetInResponse: Optional[bool] = None,
    responseIncludeGridData: Optional[bool] = None,
    responseRanges: Optional[List[str]] = None,
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}:batchUpdate"
    params: Dict[str, Any] = {}
    if includeSpreadsheetInResponse is not None:
        params["includeSpreadsheetInResponse"] = includeSpreadsheetInResponse
    if responseIncludeGridData is not None:
        params["responseIncludeGridData"] = responseIncludeGridData
    if responseRanges is not None:
        params["responseRanges"] = responseRanges
    body: Dict[str, Any] = {"requests": requests}
    return request_json("POST", url, params=params, json_body=body)


def sheets_sheets_copy_to(
    spreadsheetId: str,
    sheetId: int,
    *,
    destinationSpreadsheetId: str,
) -> Dict[str, Any]:
    url = f"{SHEETS_BASE}/{spreadsheetId}/sheets/{sheetId}/copyTo"
    return request_json("POST", url, json_body={"destinationSpreadsheetId": destinationSpreadsheetId})
