"""Google Sheets API tools for the Google Workspace MCP Server."""

from typing import Any, Optional

import requests

from generated_tools import mcp
from generated_tools.auth import (
    SHEETS_BASE,
    api_get,
    api_post,
    api_put,
    handle_http_error,
)


# ---------------------------------------------------------------------------
# Spreadsheet CRUD
# ---------------------------------------------------------------------------


@mcp.tool()
def sheets_create_spreadsheet(
    title: str,
    sheet_titles: Optional[list] = None,
) -> dict:
    """Create a new Google Spreadsheet.

    Args:
        title: The title of the new spreadsheet.
        sheet_titles: Optional list of sheet tab titles to create (default creates 'Sheet1').
    """
    try:
        payload: dict[str, Any] = {
            "properties": {"title": title},
        }
        if sheet_titles:
            payload["sheets"] = [
                {"properties": {"title": t}} for t in sheet_titles
            ]
        return api_post(SHEETS_BASE, payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_get_spreadsheet(
    spreadsheet_id: str,
    ranges: Optional[list] = None,
    include_grid_data: bool = False,
) -> dict:
    """Get metadata and optionally data for a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet to retrieve.
        ranges: Optional list of A1 notation ranges to retrieve data from.
        include_grid_data: Whether to include grid data in the response.
    """
    try:
        params: dict[str, Any] = {"includeGridData": include_grid_data}
        if ranges:
            params["ranges"] = ranges
        return api_get(f"{SHEETS_BASE}/{spreadsheet_id}", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_batch_update(
    spreadsheet_id: str,
    sheet_requests: list,
    include_spreadsheet_in_response: bool = False,
) -> dict:
    """Apply one or more structural updates to a Google Spreadsheet.

    Common request types:
    - addSheet: {'addSheet': {'properties': {'title': 'New Sheet'}}}
    - deleteSheet: {'deleteSheet': {'sheetId': 123456}}
    - updateSheetProperties: {'updateSheetProperties': {'properties': {'sheetId': 0, 'title': 'Renamed'}, 'fields': 'title'}}
    - duplicateSheet: {'duplicateSheet': {'sourceSheetId': 0, 'insertSheetIndex': 1, 'newSheetName': 'Copy'}}
    - updateSpreadsheetProperties: {'updateSpreadsheetProperties': {'properties': {'title': 'New Title'}, 'fields': 'title'}}
    - mergeCells: {'mergeCells': {'range': {'sheetId': 0, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 3}, 'mergeType': 'MERGE_ALL'}}
    - repeatCell: {'repeatCell': {'range': {'sheetId': 0, 'startRowIndex': 0, 'endRowIndex': 1}, 'cell': {'userEnteredFormat': {'backgroundColor': {'red': 0.2, 'green': 0.6, 'blue': 1.0}}}, 'fields': 'userEnteredFormat.backgroundColor'}}
    - sortRange: {'sortRange': {'range': {'sheetId': 0, 'startRowIndex': 1, 'endRowIndex': 10, 'startColumnIndex': 0, 'endColumnIndex': 3}, 'sortSpecs': [{'dimensionIndex': 0, 'sortOrder': 'ASCENDING'}]}}
    - insertDimension: {'insertDimension': {'range': {'sheetId': 0, 'dimension': 'ROWS', 'startIndex': 0, 'endIndex': 1}, 'inheritFromBefore': False}}
    - deleteDimension: {'deleteDimension': {'range': {'sheetId': 0, 'dimension': 'ROWS', 'startIndex': 0, 'endIndex': 1}}}
    - findReplace: {'findReplace': {'find': 'old', 'replacement': 'new', 'allSheets': True}}

    Args:
        spreadsheet_id: The ID of the spreadsheet to update.
        sheet_requests: List of request objects to apply to the spreadsheet.
        include_spreadsheet_in_response: Whether to include the updated spreadsheet in the response.
    """
    try:
        payload: dict[str, Any] = {
            "requests": sheet_requests,
            "includeSpreadsheetInResponse": include_spreadsheet_in_response,
        }
        return api_post(f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Values - Read
# ---------------------------------------------------------------------------


@mcp.tool()
def sheets_get_values(
    spreadsheet_id: str,
    range: str,
    major_dimension: str = "ROWS",
    value_render_option: str = "FORMATTED_VALUE",
    date_time_render_option: str = "SERIAL_NUMBER",
) -> dict:
    """Read values from a range in a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        range: The A1 notation range to read (e.g. 'Sheet1!A1:C5').
        major_dimension: The major dimension of the values: 'ROWS' or 'COLUMNS'.
        value_render_option: How values are rendered: 'FORMATTED_VALUE', 'UNFORMATTED_VALUE', or 'FORMULA'.
        date_time_render_option: How dates are rendered: 'SERIAL_NUMBER' or 'FORMATTED_STRING'.
    """
    try:
        params: dict[str, Any] = {
            "majorDimension": major_dimension,
            "valueRenderOption": value_render_option,
            "dateTimeRenderOption": date_time_render_option,
        }
        return api_get(
            f"{SHEETS_BASE}/{spreadsheet_id}/values/{range}",
            params=params,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_batch_get_values(
    spreadsheet_id: str,
    ranges: list,
    major_dimension: str = "ROWS",
    value_render_option: str = "FORMATTED_VALUE",
) -> dict:
    """Read values from multiple ranges in a Google Spreadsheet in a single request.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        ranges: List of A1 notation ranges to read (e.g. ['Sheet1!A1:B2', 'Sheet1!C1:D2']).
        major_dimension: The major dimension of the values: 'ROWS' or 'COLUMNS'.
        value_render_option: How values are rendered: 'FORMATTED_VALUE', 'UNFORMATTED_VALUE', or 'FORMULA'.
    """
    try:
        params: dict[str, Any] = {
            "ranges": ranges,
            "majorDimension": major_dimension,
            "valueRenderOption": value_render_option,
        }
        return api_get(
            f"{SHEETS_BASE}/{spreadsheet_id}/values:batchGet",
            params=params,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Values - Write
# ---------------------------------------------------------------------------


@mcp.tool()
def sheets_update_values(
    spreadsheet_id: str,
    range: str,
    values: list,
    value_input_option: str = "RAW",
    include_values_in_response: bool = False,
) -> dict:
    """Write values to a range in a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        range: The A1 notation range to write to (e.g. 'Sheet1!A1:C3').
        values: 2D list of values to write (rows of columns).
            Example: [['Name', 'Score'], ['Alice', 95], ['Bob', 82]]
        value_input_option: How input is interpreted:
            'RAW' - stored as-is,
            'USER_ENTERED' - evaluates formulas and detects types.
        include_values_in_response: Whether to include updated values in the response.
    """
    try:
        params: dict[str, Any] = {
            "valueInputOption": value_input_option,
            "includeValuesInResponse": include_values_in_response,
        }
        payload: dict[str, Any] = {
            "range": range,
            "majorDimension": "ROWS",
            "values": values,
        }
        return api_put(
            f"{SHEETS_BASE}/{spreadsheet_id}/values/{range}",
            payload=payload,
            params=params,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_append_values(
    spreadsheet_id: str,
    range: str,
    values: list,
    value_input_option: str = "RAW",
    insert_data_option: str = "INSERT_ROWS",
    include_values_in_response: bool = False,
) -> dict:
    """Append values to a table in a Google Spreadsheet.

    Values are appended after the last row of the detected table in the range.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        range: The A1 notation range to search for a table (e.g. 'Sheet1!A:A').
        values: 2D list of values to append.
            Example: [['Charlie', 78], ['Diana', 91]]
        value_input_option: How input is interpreted: 'RAW' or 'USER_ENTERED'.
        insert_data_option: How data is inserted: 'INSERT_ROWS' or 'OVERWRITE'.
        include_values_in_response: Whether to include appended values in the response.
    """
    try:
        params: dict[str, Any] = {
            "valueInputOption": value_input_option,
            "insertDataOption": insert_data_option,
            "includeValuesInResponse": include_values_in_response,
        }
        payload: dict[str, Any] = {
            "range": range,
            "majorDimension": "ROWS",
            "values": values,
        }
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}/values/{range}:append",
            payload=payload,
            params=params,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_batch_update_values(
    spreadsheet_id: str,
    data: list,
    value_input_option: str = "RAW",
    include_values_in_response: bool = False,
) -> dict:
    """Write values to multiple ranges in a Google Spreadsheet in a single request.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        data: List of ValueRange objects, each with 'range' and 'values' keys.
            Example: [
                {'range': 'Sheet1!A1:A2', 'values': [['Name'], ['Alice']]},
                {'range': 'Sheet1!B1:B2', 'values': [['Score'], [95]]}
            ]
        value_input_option: How input is interpreted: 'RAW' or 'USER_ENTERED'.
        include_values_in_response: Whether to include updated values in the response.
    """
    try:
        payload: dict[str, Any] = {
            "valueInputOption": value_input_option,
            "data": data,
            "includeValuesInResponse": include_values_in_response,
        }
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}/values:batchUpdate",
            payload=payload,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Values - Clear
# ---------------------------------------------------------------------------


@mcp.tool()
def sheets_clear_values(spreadsheet_id: str, range: str) -> dict:
    """Clear values from a range in a Google Spreadsheet.

    Only values are cleared; formatting and data validation are preserved.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        range: The A1 notation range to clear (e.g. 'Sheet1!A1:C5').
    """
    try:
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}/values/{range}:clear",
            payload={},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_batch_clear_values(spreadsheet_id: str, ranges: list) -> dict:
    """Clear values from multiple ranges in a Google Spreadsheet in a single request.

    Only values are cleared; formatting and data validation are preserved.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        ranges: List of A1 notation ranges to clear (e.g. ['Sheet1!A1:A3', 'Sheet1!B1:B3']).
    """
    try:
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}/values:batchClear",
            payload={"ranges": ranges},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Sheet Management (via batchUpdate)
# ---------------------------------------------------------------------------


@mcp.tool()
def sheets_add_sheet(
    spreadsheet_id: str,
    title: str,
    index: Optional[int] = None,
    row_count: int = 1000,
    column_count: int = 26,
) -> dict:
    """Add a new sheet tab to a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        title: The title of the new sheet.
        index: The zero-based index where the sheet will be inserted.
        row_count: Number of rows in the new sheet (default 1000).
        column_count: Number of columns in the new sheet (default 26).
    """
    try:
        properties: dict[str, Any] = {
            "title": title,
            "gridProperties": {
                "rowCount": row_count,
                "columnCount": column_count,
            },
        }
        if index is not None:
            properties["index"] = index
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={"requests": [{"addSheet": {"properties": properties}}]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_delete_sheet(spreadsheet_id: str, sheet_id: int) -> dict:
    """Delete a sheet tab from a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        sheet_id: The integer ID of the sheet to delete (not the title).
    """
    try:
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={"requests": [{"deleteSheet": {"sheetId": sheet_id}}]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_rename_sheet(
    spreadsheet_id: str,
    sheet_id: int,
    new_title: str,
) -> dict:
    """Rename a sheet tab in a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        sheet_id: The integer ID of the sheet to rename (not the title).
        new_title: The new title for the sheet.
    """
    try:
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={
                "requests": [
                    {
                        "updateSheetProperties": {
                            "properties": {
                                "sheetId": sheet_id,
                                "title": new_title,
                            },
                            "fields": "title",
                        }
                    }
                ]
            },
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_duplicate_sheet(
    spreadsheet_id: str,
    source_sheet_id: int,
    insert_sheet_index: Optional[int] = None,
    new_sheet_name: Optional[str] = None,
) -> dict:
    """Duplicate a sheet within a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        source_sheet_id: The integer ID of the sheet to duplicate.
        insert_sheet_index: The zero-based index where the new sheet will be inserted.
        new_sheet_name: The name for the duplicated sheet.
    """
    try:
        request: dict[str, Any] = {"sourceSheetId": source_sheet_id}
        if insert_sheet_index is not None:
            request["insertSheetIndex"] = insert_sheet_index
        if new_sheet_name:
            request["newSheetName"] = new_sheet_name
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={"requests": [{"duplicateSheet": request}]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_copy_sheet_to(
    spreadsheet_id: str,
    sheet_id: int,
    destination_spreadsheet_id: str,
) -> dict:
    """Copy a sheet from one Google Spreadsheet to another.

    Args:
        spreadsheet_id: The ID of the source spreadsheet.
        sheet_id: The integer ID of the sheet to copy.
        destination_spreadsheet_id: The ID of the destination spreadsheet.
    """
    try:
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}/sheets/{sheet_id}:copyTo",
            payload={"destinationSpreadsheetId": destination_spreadsheet_id},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Formatting helpers (via batchUpdate)
# ---------------------------------------------------------------------------


@mcp.tool()
def sheets_format_cells(
    spreadsheet_id: str,
    sheet_id: int,
    start_row_index: int,
    end_row_index: int,
    start_column_index: int,
    end_column_index: int,
    bold: Optional[bool] = None,
    italic: Optional[bool] = None,
    font_size: Optional[int] = None,
    background_color_red: Optional[float] = None,
    background_color_green: Optional[float] = None,
    background_color_blue: Optional[float] = None,
    horizontal_alignment: Optional[str] = None,
    number_format_type: Optional[str] = None,
    number_format_pattern: Optional[str] = None,
) -> dict:
    """Apply formatting to a range of cells in a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        sheet_id: The integer ID of the sheet.
        start_row_index: Start row index (0-based, inclusive).
        end_row_index: End row index (0-based, exclusive).
        start_column_index: Start column index (0-based, inclusive).
        end_column_index: End column index (0-based, exclusive).
        bold: Whether to make text bold.
        italic: Whether to make text italic.
        font_size: Font size in points.
        background_color_red: Red component of background color (0.0-1.0).
        background_color_green: Green component of background color (0.0-1.0).
        background_color_blue: Blue component of background color (0.0-1.0).
        horizontal_alignment: Text alignment: 'LEFT', 'CENTER', or 'RIGHT'.
        number_format_type: Number format type: 'TEXT', 'NUMBER', 'PERCENT', 'CURRENCY', 'DATE', 'TIME', 'DATE_TIME', 'SCIENTIFIC'.
        number_format_pattern: Custom number format pattern (e.g. '#,##0.00').
    """
    try:
        cell_format: dict[str, Any] = {}
        fields_list = []

        text_format: dict[str, Any] = {}
        if bold is not None:
            text_format["bold"] = bold
            fields_list.append("userEnteredFormat.textFormat.bold")
        if italic is not None:
            text_format["italic"] = italic
            fields_list.append("userEnteredFormat.textFormat.italic")
        if font_size is not None:
            text_format["fontSize"] = font_size
            fields_list.append("userEnteredFormat.textFormat.fontSize")
        if text_format:
            cell_format["textFormat"] = text_format

        if any(v is not None for v in [background_color_red, background_color_green, background_color_blue]):
            cell_format["backgroundColor"] = {
                "red": background_color_red or 0.0,
                "green": background_color_green or 0.0,
                "blue": background_color_blue or 0.0,
            }
            fields_list.append("userEnteredFormat.backgroundColor")

        if horizontal_alignment is not None:
            cell_format["horizontalAlignment"] = horizontal_alignment
            fields_list.append("userEnteredFormat.horizontalAlignment")

        if number_format_type is not None:
            nf: dict[str, Any] = {"type": number_format_type}
            if number_format_pattern:
                nf["pattern"] = number_format_pattern
            cell_format["numberFormat"] = nf
            fields_list.append("userEnteredFormat.numberFormat")

        request = {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": start_row_index,
                    "endRowIndex": end_row_index,
                    "startColumnIndex": start_column_index,
                    "endColumnIndex": end_column_index,
                },
                "cell": {"userEnteredFormat": cell_format},
                "fields": ",".join(fields_list) if fields_list else "userEnteredFormat",
            }
        }
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_auto_resize_columns(
    spreadsheet_id: str,
    sheet_id: int,
    start_column_index: int = 0,
    end_column_index: int = 26,
) -> dict:
    """Auto-resize columns in a Google Spreadsheet to fit their content.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        sheet_id: The integer ID of the sheet.
        start_column_index: Start column index (0-based, inclusive).
        end_column_index: End column index (0-based, exclusive).
    """
    try:
        request = {
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": start_column_index,
                    "endIndex": end_column_index,
                }
            }
        }
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_freeze_rows_columns(
    spreadsheet_id: str,
    sheet_id: int,
    frozen_row_count: int = 0,
    frozen_column_count: int = 0,
) -> dict:
    """Freeze rows and/or columns in a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        sheet_id: The integer ID of the sheet.
        frozen_row_count: Number of rows to freeze (0 to unfreeze).
        frozen_column_count: Number of columns to freeze (0 to unfreeze).
    """
    try:
        request = {
            "updateSheetProperties": {
                "properties": {
                    "sheetId": sheet_id,
                    "gridProperties": {
                        "frozenRowCount": frozen_row_count,
                        "frozenColumnCount": frozen_column_count,
                    },
                },
                "fields": "gridProperties.frozenRowCount,gridProperties.frozenColumnCount",
            }
        }
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_sort_range(
    spreadsheet_id: str,
    sheet_id: int,
    start_row_index: int,
    end_row_index: int,
    start_column_index: int,
    end_column_index: int,
    sort_specs: list,
) -> dict:
    """Sort a range of cells in a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        sheet_id: The integer ID of the sheet.
        start_row_index: Start row index (0-based, inclusive).
        end_row_index: End row index (0-based, exclusive).
        start_column_index: Start column index (0-based, inclusive).
        end_column_index: End column index (0-based, exclusive).
        sort_specs: List of sort specifications, each with 'dimensionIndex' and 'sortOrder'
            (e.g. [{'dimensionIndex': 0, 'sortOrder': 'ASCENDING'}]).
    """
    try:
        request = {
            "sortRange": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": start_row_index,
                    "endRowIndex": end_row_index,
                    "startColumnIndex": start_column_index,
                    "endColumnIndex": end_column_index,
                },
                "sortSpecs": sort_specs,
            }
        }
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_find_replace(
    spreadsheet_id: str,
    find: str,
    replacement: str,
    all_sheets: bool = True,
    sheet_id: Optional[int] = None,
    match_case: bool = False,
    match_entire_cell: bool = False,
    search_by_regex: bool = False,
    include_formulas: bool = False,
) -> dict:
    """Find and replace text in a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        find: The text to find.
        replacement: The replacement text.
        all_sheets: Whether to search all sheets (default True).
        sheet_id: Specific sheet ID to search (used if all_sheets is False).
        match_case: Whether the search is case-sensitive.
        match_entire_cell: Whether to match the entire cell value.
        search_by_regex: Whether to treat find as a regular expression.
        include_formulas: Whether to search in formula text.
    """
    try:
        find_replace: dict[str, Any] = {
            "find": find,
            "replacement": replacement,
            "matchCase": match_case,
            "matchEntireCell": match_entire_cell,
            "searchByRegex": search_by_regex,
            "includeFormulas": include_formulas,
        }
        if all_sheets:
            find_replace["allSheets"] = True
        elif sheet_id is not None:
            find_replace["sheetId"] = sheet_id

        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}:batchUpdate",
            payload={"requests": [{"findReplace": find_replace}]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Developer Metadata
# ---------------------------------------------------------------------------


@mcp.tool()
def sheets_get_developer_metadata(
    spreadsheet_id: str,
    metadata_id: int,
) -> dict:
    """Get developer metadata by ID from a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        metadata_id: The integer ID of the developer metadata.
    """
    try:
        return api_get(
            f"{SHEETS_BASE}/{spreadsheet_id}/developerMetadata/{metadata_id}"
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def sheets_search_developer_metadata(
    spreadsheet_id: str,
    data_filters: list,
) -> dict:
    """Search for developer metadata in a Google Spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        data_filters: List of DataFilter objects to match developer metadata.
    """
    try:
        return api_post(
            f"{SHEETS_BASE}/{spreadsheet_id}/developerMetadata:search",
            payload={"dataFilters": data_filters},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)
