from typing import Any, Dict

from .client import ZulipClient


def upload_file(*, file_path: str) -> Dict[str, Any]:
    """POST /user_uploads

    Upload a single file from local disk.
    """
    client = ZulipClient()
    try:
        with open(file_path, "rb") as f:
            files = {"filename": f}
            return client.request("POST", "/user_uploads", files=files)
    except OSError as e:
        return {"error": str(e)}


def get_file_temporary_url(*, realm_id_str: int, filename: str) -> Dict[str, Any]:
    """GET /user_uploads/{realm_id_str}/{filename}"""
    client = ZulipClient()
    return client.request("GET", f"/user_uploads/{realm_id_str}/{filename}")
