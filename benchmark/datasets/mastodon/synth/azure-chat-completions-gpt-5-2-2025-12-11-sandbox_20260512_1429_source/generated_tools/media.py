from typing import Any, Dict, Optional

from .http_client import MastodonClient


def upload_media(*, file_path: str, description: Optional[str] = None, focus: Optional[str] = None, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/media (multipart)."""
    client = client or MastodonClient()
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            form: Dict[str, Any] = {}
            if description is not None:
                form["description"] = description
            if focus is not None:
                form["focus"] = focus
            return client.request("POST", "/api/v1/media", data=form, files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Failed to upload media: {e}"}
