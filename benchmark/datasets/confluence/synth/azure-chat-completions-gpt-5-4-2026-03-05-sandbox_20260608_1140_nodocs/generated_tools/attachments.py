import base64
from typing import Any, Dict, Optional

from generated_tools.confluence_client import client


def list_attachments(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> Dict[str, Any]:
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return client.request("GET", f"/api/v2/pages/{page_id}/attachments", params=params)


def upload_attachment(page_id: str, filename: str, content_base64: str, content_type: str = "application/octet-stream", comment: Optional[str] = None) -> Dict[str, Any]:
    data = base64.b64decode(content_base64)
    files = {"file": (filename, data, content_type)}
    form = {}
    if comment:
        form["comment"] = comment
    return client.request(
        "POST",
        f"/rest/api/content/{page_id}/child/attachment",
        data=form,
        files=files,
        headers={"X-Atlassian-Token": "no-check"},
    )


def download_attachment(download_path: str) -> Dict[str, Any]:
    result = client.request("GET", download_path, stream=True)
    if result.get("error"):
        return result
    response = result["response"]
    content = response.content
    return {
        "content_base64": base64.b64encode(content).decode("ascii"),
        "content_type": response.headers.get("Content-Type"),
        "status_code": response.status_code,
    }
