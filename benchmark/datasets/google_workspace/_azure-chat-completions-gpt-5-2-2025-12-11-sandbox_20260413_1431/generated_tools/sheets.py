"""Google Sheets API v4 tools."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import request_json

SHEETS_BASE = "https://sheets.googleapis.com/v4/spreadsheets"


def sheets_spreadsheets_create(*, spreadsheet: Optional[Dict[str, Any]] = None) -> Any:
    return request_json("POST", f"{SHEETS_BASE}", json=spreadsheet or {})


def sheets_spreadsheets_get(spreadsheet_id: str, *, include_grid_data: bool = False, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"includeGridData": include_grid_data}
    if fields:
        params["fields"] = fields
    return request_json("GET", f"{SHEETS_BASE}/{spreadsheet_id}", params=params)


def sheets_spreadsheets_batch_update(spreadsheet_id: str, *, requests: List[Dict[str, Any]], include_spreadsheet_in_response: bool = False) -> Any:
    payload: Dict[str, Any] = {
        "requests": requests,
        "includeSpreadsheetInResponse": include_spreadsheet_in_response,
    }
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate", json=payload)


def sheets_values_get(
    spreadsheet_id: str,
    range_a1: str,
    *,
    major_dimension: Optional[str] = None,
    value_render_option: Optional[str] = None,
    date_time_render_option: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if major_dimension:
        params["majorDimension"] = major_dimension
    if value_render_option:
        params["valueRenderOption"] = value_render_option
    if date_time_render_option:
        params["dateTimeRenderOption"] = date_time_render_option
    return request_json("GET", f"{SHEETS_BASE}/{spreadsheet_id}/values/{range_a1}", params=params)


def sheets_values_update(
    spreadsheet_id: str,
    range_a1: str,
    *,
    values: List[List[Any]],
    value_input_option: str = "RAW",
    major_dimension: str = "ROWS",
    include_values_in_response: bool = False,
) -> Any:
    params: Dict[str, Any] = {
        "valueInputOption": value_input_option,
        "includeValuesInResponse": include_values_in_response,
    }
    body = {"range": range_a1, "majorDimension": major_dimension, "values": values}
    return request_json("PUT", f"{SHEETS_BASE}/{spreadsheet_id}/values/{range_a1}", params=params, json=body)


def sheets_values_append(
    spreadsheet_id: str,
    range_a1: str,
    *,
    values: List[List[Any]],
    value_input_option: str = "RAW",
    insert_data_option: str = "INSERT_ROWS",
) -> Any:
    params: Dict[str, Any] = {
        "valueInputOption": value_input_option,
        "insertDataOption": insert_data_option,
    }
    body = {"range": range_a1, "majorDimension": "ROWS", "values": values}
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheet_id}/values/{range_a1}:append", params=params, json=body)


def sheets_values_batch_get(spreadsheet_id: str, *, ranges: List[str], major_dimension: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"ranges": ranges}
    if major_dimension:
        params["majorDimension"] = major_dimension
    return request_json("GET", f"{SHEETS_BASE}/{spreadsheet_id}/values:batchGet", params=params)


def sheets_values_batch_update(
    spreadsheet_id: str,
    *,
    data: List[Dict[str, Any]],
    value_input_option: str = "RAW",
) -> Any:
    params: Dict[str, Any] = {"valueInputOption": value_input_option}
    body = {"valueInputOption": value_input_option, "data": data}
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheet_id}/values:batchUpdate", params=params, json=body)


def sheets_values_clear(spreadsheet_id: str, range_a1: str) -> Any:
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheet_id}/values/{range_a1}:clear", json={})


def sheets_values_batch_clear(spreadsheet_id: str, *, ranges: List[str]) -> Any:
    body = {"ranges": ranges}
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheet_id}/values:batchClear", json=body)


def sheets_sheets_copy_to(spreadsheet_id: str, sheet_id: int, *, destination_spreadsheet_id: str) -> Any:
    body = {"destinationSpreadsheetId": destination_spreadsheet_id}
    return request_json("POST", f"{SHEETS_BASE}/{spreadsheet_id}/sheets/{sheet_id}:copyTo", json=body)
