from typing import Any, Dict, Optional

from .http import request_json

DOCS_BASE = "https://docs.googleapis.com/v1/documents"


def docs_documents_create(*, title: str) -> Any:
    return request_json("POST", f"{DOCS_BASE}", json_body={"title": title})


def docs_documents_get(documentId: str, *, suggestionsViewMode: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if suggestionsViewMode is not None:
        params["suggestionsViewMode"] = suggestionsViewMode
    return request_json("GET", f"{DOCS_BASE}/{documentId}", params=params)


def docs_documents_batchUpdate(documentId: str, *, requests: list, writeControl: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"requests": requests}
    if writeControl is not None:
        body["writeControl"] = writeControl
    return request_json("POST", f"{DOCS_BASE}/{documentId}:batchUpdate", json_body=body)
