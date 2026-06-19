from typing import Any, Optional

from .client import MastodonClient


def media_upload(
    client: MastodonClient,
    file_path: str,
    *,
    description: Optional[str] = None,
    focus: Optional[str] = None,
) -> Any:
    try:
        f = open(file_path, "rb")
    except Exception as e:
        return {"error": str(e)}

    files = {"file": f}
    try:
        return client.request(
            "POST",
            "/api/v1/media",
            params={"description": description, "focus": focus},
            files=files,
        )
    finally:
        try:
            f.close()
        except Exception:
            pass


def media_get(client: MastodonClient, media_id: str) -> Any:
    return client.request("GET", f"/api/v1/media/{media_id}")
