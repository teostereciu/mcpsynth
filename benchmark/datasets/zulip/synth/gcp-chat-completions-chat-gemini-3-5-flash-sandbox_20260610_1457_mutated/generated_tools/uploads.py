import base64
import io
import os
from typing import Any, Dict, Optional
from generated_tools.client import client

def upload_file_from_path(file_path: str) -> Dict[str, Any]:
    """
    Upload a file to Zulip from a local file path.
    
    Args:
        file_path: The local path to the file to upload.
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
        
    filename = os.path.basename(file_path)
    try:
        with open(file_path, "rb") as f:
            files = {"file": (filename, f)}
            return client.request("POST", "user_uploads", files=files)
    except Exception as e:
        return {"error": f"Failed to read or upload file: {str(e)}"}

def upload_file_from_content(
    filename: str,
    content_base64: str,
) -> Dict[str, Any]:
    """
    Upload a file to Zulip by passing its base64-encoded content.
    
    Args:
        filename: The name of the file (e.g., "image.png").
        content_base64: The base64-encoded content of the file.
    """
    try:
        file_data = base64.b64decode(content_base64)
        file_like = io.BytesIO(file_data)
        files = {"file": (filename, file_like)}
        return client.request("POST", "user_uploads", files=files)
    except Exception as e:
        return {"error": f"Failed to decode or upload file: {str(e)}"}
