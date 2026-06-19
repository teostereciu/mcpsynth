from typing import Any, Dict, Optional

from .http import request_json

SHEETS_BASE = "https://sheets.googleapis.com/v4/spreadsheets"


def sheets_values_get(*, spreadsheetId: str, range: str, majorDimension: Optional[str] = None, valueRenderOption: Optional[str] = None, dateTimeRenderOption: Optional[str] = None) -> Any:
    url = f"{SHEETS_BASE}/{spreadsheetId}/values/{range}"
    params: Dict[str, Any] = {}
    if majorDimension is not None:
        params["majorDimension"] = majorDimension
    if valueRenderOption is not None:
        params["valueRenderOption"] = valueRenderOption
    if dateTimeRenderOption is not None:
        params["dateTimeRenderOption"] = dateTimeRenderOption
    return request_json("GET", url, params=params)
