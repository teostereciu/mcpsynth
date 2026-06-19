from __future__ import annotations

from typing import Any, Dict, Optional
from urllib.parse import quote

from server import jira_request, mcp


@mcp.tool()
def bulk_fetch_changelogs(issueIdsOrKeys: list[str], fieldIds: Optional[list[str]] = None, maxResults: Optional[int] = None, nextPageToken: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"issueIdsOrKeys": issueIdsOrKeys}
    if fieldIds is not None:
        body["fieldIds"] = fieldIds
    if maxResults is not None:
        body["maxResults"] = maxResults
    if nextPageToken is not None:
        body["nextPageToken"] = nextPageToken
    return jira_request("POST", "/changelog/bulkfetch", body=body)


@mcp.tool()
def get_issue(issueIdOrKey: str, fields: Optional[str] = None, expand: Optional[str] = None) -> Any:
    return jira_request("GET", f"/issue/{quote(issueIdOrKey, safe='')}", {"fields": fields, "expand": expand})


@mcp.tool()
def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, transition: Optional[Dict[str, Any]] = None, properties: Optional[list] = None, historyMetadata: Optional[Dict[str, Any]] = None, updateHistory: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {"fields": fields}
    if update is not None:
        body["update"] = update
    if transition is not None:
        body["transition"] = transition
    if properties is not None:
        body["properties"] = properties
    if historyMetadata is not None:
        body["historyMetadata"] = historyMetadata
    return jira_request("POST", "/issue", {"updateHistory": updateHistory}, body)
