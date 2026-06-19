from typing import Any, Dict

from .client import ZulipClient


def upload_file(path: str) -> Dict[str, Any]:
    """POST /user_uploads"""
    try:
        with open(path, "rb") as f:
            files = {"filename": f}
            return ZulipClient().request("POST", "/user_uploads", files=files)
    except OSError as e:
        return {"error": str(e)}


def get_file_temporary_url(realm_id_str: str, filename: str) -> Dict[str, Any]:
    """GET /user_uploads/{realm_id_str}/{filename}"""
    return ZulipClient().request("GET", f"/user_uploads/{realm_id_str}/{filename}")
