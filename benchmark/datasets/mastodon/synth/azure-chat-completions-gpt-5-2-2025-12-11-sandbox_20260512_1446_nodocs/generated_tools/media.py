from typing import Any, Dict, Optional

from ._client import request_json


def upload_media(
    file_path: str,
    *,
    description: Optional[str] = None,
    focus: Optional[str] = None,
) -> Any:
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data: Dict[str, Any] = {}
            if description is not None:
                data["description"] = description
            if focus is not None:
                data["focus"] = focus
            return request_json("POST", "/api/v2/media", data=data or None, files=files)
    except Exception as e:
        return {"error": "file_open_failed", "details": str(e)}
