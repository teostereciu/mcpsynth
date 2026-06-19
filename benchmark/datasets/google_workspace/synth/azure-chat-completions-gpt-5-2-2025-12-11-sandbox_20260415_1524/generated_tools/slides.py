from typing import Any

from .http import request_json

SLIDES_BASE = "https://slides.googleapis.com/v1/presentations"


def slides_presentations_get(*, presentationId: str) -> Any:
    url = f"{SLIDES_BASE}/{presentationId}"
    return request_json("GET", url)
