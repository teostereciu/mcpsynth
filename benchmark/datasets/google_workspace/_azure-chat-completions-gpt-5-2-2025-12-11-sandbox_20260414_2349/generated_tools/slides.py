from typing import Any, Dict, Optional

from .http import request_json

SLIDES_BASE = "https://slides.googleapis.com/v1/presentations"


def slides_presentations_create(*, title: str) -> Any:
    return request_json("POST", f"{SLIDES_BASE}", json_body={"title": title})


def slides_presentations_get(presentationId: str) -> Any:
    return request_json("GET", f"{SLIDES_BASE}/{presentationId}")


def slides_presentations_batchUpdate(presentationId: str, *, requests: list, writeControl: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"requests": requests}
    if writeControl is not None:
        body["writeControl"] = writeControl
    return request_json("POST", f"{SLIDES_BASE}/{presentationId}:batchUpdate", json_body=body)


def slides_presentations_pages_get(presentationId: str, pageObjectId: str) -> Any:
    return request_json("GET", f"{SLIDES_BASE}/{presentationId}/pages/{pageObjectId}")


def slides_presentations_pages_getThumbnail(presentationId: str, pageObjectId: str, *, thumbnailProperties_mimeType: Optional[str] = None, thumbnailProperties_thumbnailSize: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if thumbnailProperties_mimeType is not None:
        params["thumbnailProperties.mimeType"] = thumbnailProperties_mimeType
    if thumbnailProperties_thumbnailSize is not None:
        params["thumbnailProperties.thumbnailSize"] = thumbnailProperties_thumbnailSize
    return request_json("GET", f"{SLIDES_BASE}/{presentationId}/pages/{pageObjectId}/thumbnail", params=params)
