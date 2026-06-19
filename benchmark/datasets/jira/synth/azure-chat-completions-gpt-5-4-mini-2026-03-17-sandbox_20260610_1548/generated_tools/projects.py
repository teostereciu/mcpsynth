from __future__ import annotations

from typing import Any, Dict, Optional
from urllib.parse import quote

from server import jira_request, mcp


@mcp.tool()
def get_project(projectIdOrKey: str) -> Any:
    return jira_request("GET", f"/project/{quote(projectIdOrKey, safe='')}")


@mcp.tool()
def create_project(body: Dict[str, Any]) -> Any:
    return jira_request("POST", "/project", body=body)


@mcp.tool()
def update_project(projectIdOrKey: str, body: Dict[str, Any]) -> Any:
    return jira_request("PUT", f"/project/{quote(projectIdOrKey, safe='')}", body=body)
