from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

SLIDES_BASE = "https://slides.googleapis.com/v1/presentations"


def slides_presentations_create(*, title: str) -> Dict[str, Any]:
    url = f"{SLIDES_BASE}"
    return request_json("POST", url, json_body={"title": title})


def slides_presentations_get(presentationId: str) -> Dict[str, Any]:
    url = f"{SLIDES_BASE}/{presentationId}"
    return request_json("GET", url)


def slides_presentations_batch_update(
    presentationId: str,
    *,
    requests: list[Dict[str, Any]],
    writeControl: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    url = f"{SLIDES_BASE}/{presentationId}:batchUpdate"
    body: Dict[str, Any] = {"requests": requests}
    if writeControl is not None:
        body["writeControl"] = writeControl
    return request_json("POST", url, json_body=body)
