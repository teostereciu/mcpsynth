from typing import Any, Dict, Optional

from .http import request_json
from .server import mcp

DOCS_BASE = "https://docs.googleapis.com/v1/documents"


@mcp.tool()
def docs_documents_create(title: str = "") -> Dict[str, Any]:
    url = f"{DOCS_BASE}"
    body = {"title": title} if title else {}
    return request_json("POST", url, json_body=body)


@mcp.tool()
def docs_documents_get(documentId: str = "") -> Dict[str, Any]:
    url = f"{DOCS_BASE}/{documentId}"
    return request_json("GET", url)


@mcp.tool()
def docs_documents_batchUpdate(documentId: str = "", requests: Optional[list] = None, writeControl: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{DOCS_BASE}/{documentId}:batchUpdate"
    body: Dict[str, Any] = {"requests": requests or []}
    if writeControl is not None:
        body["writeControl"] = writeControl
    return request_json("POST", url, json_body=body)
