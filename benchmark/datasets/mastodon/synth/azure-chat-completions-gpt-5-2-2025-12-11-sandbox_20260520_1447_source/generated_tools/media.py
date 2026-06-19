from typing import Any, Dict, Optional

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
        return {"error": f"Could not open file: {e}"}

    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus

    try:
        return client.request("POST", "/api/v1/media", data=data or None, files={"file": f})
    finally:
        try:
            f.close()
        except Exception:
            pass


def media_get(client: MastodonClient, media_id: str) -> Any:
    return client.request("GET", f"/api/v1/media/{media_id}")


def media_update(client: MastodonClient, media_id: str, *, description: Optional[str] = None, focus: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {}
    if description is not None:
        payload["description"] = description
    if focus is not None:
        payload["focus"] = focus
    return client.request("PUT", f"/api/v1/media/{media_id}", json=payload)


def media_delete(client: MastodonClient, media_id: str) -> Any:
    return client.request("DELETE", f"/api/v1/media/{media_id}")
