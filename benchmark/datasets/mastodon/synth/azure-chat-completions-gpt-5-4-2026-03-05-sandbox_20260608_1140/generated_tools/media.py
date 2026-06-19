from typing import Optional

from generated_tools.common import mastodon_request


def upload_media(file_path: str, description: Optional[str] = None, focus: Optional[str] = None, thumbnail_path: Optional[str] = None):
    data = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus
    files = {"file": open(file_path, "rb")}
    if thumbnail_path is not None:
        files["thumbnail"] = open(thumbnail_path, "rb")
    try:
        return mastodon_request("POST", "/api/v2/media", data=data, files=files)
    finally:
        for f in files.values():
            f.close()


def get_media(media_id: str):
    return mastodon_request("GET", f"/api/v1/media/{media_id}")


def update_media(media_id: str, description: Optional[str] = None, focus: Optional[str] = None, thumbnail_path: Optional[str] = None):
    data = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus
    files = None
    thumb = None
    if thumbnail_path is not None:
        thumb = open(thumbnail_path, "rb")
        files = {"thumbnail": thumb}
    try:
        return mastodon_request("PUT", f"/api/v1/media/{media_id}", data=data, files=files)
    finally:
        if thumb is not None:
            thumb.close()


def delete_media(media_id: str):
    return mastodon_request("DELETE", f"/api/v1/media/{media_id}")
