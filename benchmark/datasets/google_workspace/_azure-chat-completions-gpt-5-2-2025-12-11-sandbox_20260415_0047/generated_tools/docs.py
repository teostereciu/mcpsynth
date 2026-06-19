from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

DOCS_BASE = "https://docs.googleapis.com/v1/documents"


def docs_documents_create(*, title: str) -> Dict[str, Any]:
    url = f"{DOCS_BASE}"
    return request_json("POST", url, json_body={"title": title})


def docs_documents_get(documentId: str, *, suggestionsViewMode: Optional[str] = None) -> Dict[str, Any]:
    url = f"{DOCS_BASE}/{documentId}"
    params: Dict[str, Any] = {}
    if suggestionsViewMode is not None:
        params["suggestionsViewMode"] = suggestionsViewMode
    return request_json("GET", url, params=params)


def docs_documents_batch_update(
    documentId: str,
    *,
    requests: list[Dict[str, Any]],
    writeControl: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    url = f"{DOCS_BASE}/{documentId}:batchUpdate"
    body: Dict[str, Any] = {"requests": requests}
    if writeControl is not None:
        body["writeControl"] = writeControl
    return request_json("POST", url, json_body=body)
