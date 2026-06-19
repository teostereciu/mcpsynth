from typing import Any, Dict

from .client import ZulipClient


def upload_file(file_path: str, filename: str | None = None) -> Dict[str, Any]:
    """Upload a file from local disk.

    Note: The MCP host must have access to file_path.
    """
    c = ZulipClient()
    try:
        with open(file_path, "rb") as f:
            files: Any
            if filename:
                files = {"file": (filename, f)}
            else:
                files = {"file": f}
            return c.request("POST", "/user_uploads", files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}
