from typing import Any, Dict, Optional

from .client import MastodonClient


def upload_media(client: MastodonClient, file_path: str, description: Optional[str] = None, focus: Optional[str] = None) -> Any:
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data: Dict[str, Any] = {}
            if description is not None:
                data["description"] = description
            if focus is not None:
                data["focus"] = focus
            # Mastodon expects multipart form; requests uses 'data' not 'json'
            return client.request("POST", "/api/v2/media", params=data or None, files=files)
    except Exception as e:
        return {"error": str(e)}
