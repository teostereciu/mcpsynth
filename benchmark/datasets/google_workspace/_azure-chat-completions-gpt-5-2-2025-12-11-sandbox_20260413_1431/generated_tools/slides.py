"""Google Slides API v1 tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

SLIDES_BASE = "https://slides.googleapis.com/v1/presentations"


def slides_presentations_create(*, title: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    return request_json("POST", f"{SLIDES_BASE}", json=payload)


def slides_presentations_get(presentation_id: str) -> Any:
    return request_json("GET", f"{SLIDES_BASE}/{presentation_id}")


def slides_presentations_batch_update(presentation_id: str, *, requests: list, write_control: Optional[Dict[str, Any]] = None) -> Any:
    payload: Dict[str, Any] = {"requests": requests}
    if write_control:
        payload["writeControl"] = write_control
    return request_json("POST", f"{SLIDES_BASE}/{presentation_id}:batchUpdate", json=payload)


def slides_pages_get(presentation_id: str, page_object_id: str) -> Any:
    return request_json("GET", f"{SLIDES_BASE}/{presentation_id}/pages/{page_object_id}")


def slides_pages_get_thumbnail(
    presentation_id: str,
    page_object_id: str,
    *,
    thumbnail_size: Optional[str] = None,
    mime_type: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if thumbnail_size:
        params["thumbnailSize"] = thumbnail_size
    if mime_type:
        params["mimeType"] = mime_type
    return request_json("GET", f"{SLIDES_BASE}/{presentation_id}/pages/{page_object_id}/thumbnail", params=params)
