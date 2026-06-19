from typing import Any, Dict, Optional

import requests

from .common import ACCESS_TOKEN, BASE_URL, mastodon_request


def upload_media(file_path: str, description: Optional[str] = None, focus: Optional[str] = None, thumbnail_path: Optional[str] = None) -> Any:
    if not BASE_URL:
        return {"error": "MASTODON_BASE_URL is not set"}
    if not ACCESS_TOKEN:
        return {"error": "MASTODON_ACCESS_TOKEN is not set"}
    headers = {"Accept": "application/json", "Authorization": f"Bearer {ACCESS_TOKEN}"}
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus
    files: Dict[str, Any] = {"file": open(file_path, "rb")}
    if thumbnail_path is not None:
        files["thumbnail"] = open(thumbnail_path, "rb")
    try:
        response = requests.post(f"{BASE_URL}/api/v2/media", headers=headers, data=data, files=files, timeout=120)
        payload = response.json()
    except Exception as exc:
        return {"error": str(exc)}
    finally:
        for fh in files.values():
            try:
                fh.close()
            except Exception:
                pass
    if not response.ok:
        return {"error": f"HTTP {response.status_code}", "details": payload}
    return payload


def get_media(media_id: str) -> Any:
    return mastodon_request("GET", f"/media/{media_id}")


def update_media(media_id: str, description: Optional[str] = None, focus: Optional[str] = None) -> Any:
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus
    return mastodon_request("PUT", f"/media/{media_id}", data=data)


def delete_media(media_id: str) -> Any:
    return mastodon_request("DELETE", f"/media/{media_id}")
