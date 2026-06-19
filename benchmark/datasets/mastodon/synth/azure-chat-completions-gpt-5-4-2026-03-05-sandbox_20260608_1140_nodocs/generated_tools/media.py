from typing import Any, Optional

from generated_tools.common import mastodon_request


def upload_media(file_path: str, description: Optional[str] = None, focus: Optional[str] = None) -> Any:
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {"description": description, "focus": focus}
            return mastodon_request("POST", "/api/v2/media", data=data, files=files)
    except Exception as e:
        return {"error": str(e)}
