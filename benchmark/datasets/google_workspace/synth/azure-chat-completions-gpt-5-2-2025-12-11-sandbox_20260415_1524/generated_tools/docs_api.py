from typing import Any, Dict, Optional

from .http import request_json

DOCS_BASE = "https://docs.googleapis.com/v1/documents"


def docs_documents_get(*, documentId: str, suggestionsViewMode: Optional[str] = None, includeTabsContent: Optional[bool] = None) -> Any:
    url = f"{DOCS_BASE}/{documentId}"
    params: Dict[str, Any] = {}
    if suggestionsViewMode is not None:
        params["suggestionsViewMode"] = suggestionsViewMode
    if includeTabsContent is not None:
        params["includeTabsContent"] = includeTabsContent
    return request_json("GET", url, params=params)
