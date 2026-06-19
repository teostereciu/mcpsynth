"""Google Docs API v1 tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

DOCS_BASE = "https://docs.googleapis.com/v1/documents"


def docs_documents_create(*, title: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    return request_json("POST", f"{DOCS_BASE}", json=payload)


def docs_documents_get(document_id: str, *, suggestions_view_mode: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if suggestions_view_mode:
        params["suggestionsViewMode"] = suggestions_view_mode
    return request_json("GET", f"{DOCS_BASE}/{document_id}", params=params)


def docs_documents_batch_update(document_id: str, *, requests: list, write_control: Optional[Dict[str, Any]] = None) -> Any:
    payload: Dict[str, Any] = {"requests": requests}
    if write_control:
        payload["writeControl"] = write_control
    return request_json("POST", f"{DOCS_BASE}/{document_id}:batchUpdate", json=payload)
