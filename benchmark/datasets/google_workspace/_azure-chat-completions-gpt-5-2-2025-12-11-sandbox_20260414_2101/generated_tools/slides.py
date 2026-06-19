from typing import Any, Dict, Optional

from .http import request_json
from .server import mcp

SLIDES_BASE = "https://slides.googleapis.com/v1/presentations"


@mcp.tool()
def slides_presentations_create(title: str = "") -> Dict[str, Any]:
    url = f"{SLIDES_BASE}"
    body = {"title": title} if title else {}
    return request_json("POST", url, json_body=body)


@mcp.tool()
def slides_presentations_get(presentationId: str = "") -> Dict[str, Any]:
    url = f"{SLIDES_BASE}/{presentationId}"
    return request_json("GET", url)


@mcp.tool()
def slides_presentations_batchUpdate(presentationId: str = "", requests: Optional[list] = None, writeControl: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{SLIDES_BASE}/{presentationId}:batchUpdate"
    body: Dict[str, Any] = {"requests": requests or []}
    if writeControl is not None:
        body["writeControl"] = writeControl
    return request_json("POST", url, json_body=body)


@mcp.tool()
def slides_presentations_pages_get(presentationId: str = "", pageObjectId: str = "") -> Dict[str, Any]:
    url = f"{SLIDES_BASE}/{presentationId}/pages/{pageObjectId}"
    return request_json("GET", url)


@mcp.tool()
def slides_presentations_pages_getThumbnail(presentationId: str = "", pageObjectId: str = "", thumbnailProperties_mimeType: Optional[str] = None, thumbnailProperties_thumbnailSize: Optional[str] = None) -> Dict[str, Any]:
    url = f"{SLIDES_BASE}/{presentationId}/pages/{pageObjectId}/thumbnail"
    params: Dict[str, Any] = {}
    if thumbnailProperties_mimeType is not None:
        params["thumbnailProperties.mimeType"] = thumbnailProperties_mimeType
    if thumbnailProperties_thumbnailSize is not None:
        params["thumbnailProperties.thumbnailSize"] = thumbnailProperties_thumbnailSize
    return request_json("GET", url, params=params)
