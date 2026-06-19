from typing import Any, Dict

from generated_tools.common import client


def upload_file(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, "rb") as f:
            return client.request("POST", "/user_uploads", files={"file": f})
    except OSError as exc:
        return {"error": str(exc), "file_path": file_path}
