import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira-cloud-rest-v3")


def _base_url() -> str:
    return os.environ.get("JIRA_BASE_URL", "").rstrip("/") + "/rest/api/3"


def _auth() -> tuple[str, str]:
    return (os.environ.get("JIRA_EMAIL", ""), os.environ.get("JIRA_API_TOKEN", ""))


def _request(method: str, path: str, *, params: Optional[dict] = None, json_body: Any = None, headers: Optional[dict] = None) -> Dict[str, Any]:
    url = _base_url() + path
    hdrs = {"Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    try:
        resp = requests.request(method, url, params=params, json=json_body, headers=hdrs, auth=_auth(), timeout=60)
        if resp.status_code == 204:
            return {"status": 204, "result": "No Content"}
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        if resp.status_code >= 400:
            return {"error": data if isinstance(data, str) else data, "status": resp.status_code}
        return data if isinstance(data, (dict, list, str)) else {"result": data}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_issue(issue_id_or_key: str, expand: Optional[str] = None):
    return _request("GET", f"/issue/{issue_id_or_key}", params={k: v for k, v in {"expand": expand}.items() if v is not None})


@mcp.tool()
def create_issue(payload: dict, update_history: Optional[bool] = None):
    return _request("POST", "/issue", params={k: v for k, v in {"updateHistory": update_history}.items() if v is not None}, json_body=payload)


@mcp.tool()
def edit_issue(issue_id_or_key: str, payload: dict):
    return _request("PUT", f"/issue/{issue_id_or_key}", json_body=payload)


@mcp.tool()
def delete_issue(issue_id_or_key: str):
    return _request("DELETE", f"/issue/{issue_id_or_key}")


@mcp.tool()
def assign_issue(issue_id_or_key: str, payload: dict):
    return _request("PUT", f"/issue/{issue_id_or_key}/assignee", json_body=payload)


@mcp.tool()
def get_issue_transitions(issue_id_or_key: str, expand: Optional[str] = None):
    return _request("GET", f"/issue/{issue_id_or_key}/transitions", params={k: v for k, v in {"expand": expand}.items() if v is not None})


@mcp.tool()
def transition_issue(issue_id_or_key: str, payload: dict, transition: Optional[str] = None):
    return _request("POST", f"/issue/{issue_id_or_key}/transitions", params={k: v for k, v in {"transition": transition}.items() if v is not None}, json_body=payload)


@mcp.tool()
def get_issue_comments(issue_id_or_key: str, start_index: Optional[int] = None, page_size: Optional[int] = None, order_by: Optional[str] = None, expand: Optional[str] = None):
    params = {k: v for k, v in {"start_index": start_index, "page_size": page_size, "orderBy": order_by, "expand": expand}.items() if v is not None}
    return _request("GET", f"/issue/{issue_id_or_key}/comment", params=params)


@mcp.tool()
def add_issue_comment(issue_id_or_key: str, payload: dict, expand: Optional[str] = None):
    return _request("POST", f"/issue/{issue_id_or_key}/comment", params={k: v for k, v in {"expand": expand}.items() if v is not None}, json_body=payload)


@mcp.tool()
def update_issue_comment(issue_id_or_key: str, comment_id: str, payload: dict, notify_users: Optional[bool] = None, override_editable_flag: Optional[bool] = None, expand: Optional[str] = None):
    params = {k: v for k, v in {"notifyUsers": notify_users, "overrideEditableFlag": override_editable_flag, "expand": expand}.items() if v is not None}
    return _request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params, json_body=payload)


@mcp.tool()
def delete_issue_comment(issue_id_or_key: str, comment_id: str):
    return _request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")


@mcp.tool()
def get_issue_worklogs(issue_id_or_key: str, start_index: Optional[int] = None, page_size: Optional[int] = None, started_after: Optional[int] = None, started_before: Optional[int] = None, expand: Optional[str] = None):
    params = {k: v for k, v in {"start_index": start_index, "page_size": page_size, "startedAfter": started_after, "startedBefore": started_before, "expand": expand}.items() if v is not None}
    return _request("GET", f"/issue/{issue_id_or_key}/worklog", params=params)


@mcp.tool()
def add_issue_worklog(issue_id_or_key: str, payload: dict, notify_users: Optional[bool] = None, adjust_estimate: Optional[str] = None, new_estimate: Optional[str] = None, reduce_by: Optional[str] = None, expand: Optional[str] = None, override_editable_flag: Optional[bool] = None):
    params = {k: v for k, v in {"notifyUsers": notify_users, "adjustEstimate": adjust_estimate, "newEstimate": new_estimate, "reduceBy": reduce_by, "expand": expand, "overrideEditableFlag": override_editable_flag}.items() if v is not None}
    return _request("POST", f"/issue/{issue_id_or_key}/worklog", params=params, json_body=payload)


@mcp.tool()
def get_worklog(issue_id_or_key: str, worklog_id: str, expand: Optional[str] = None):
    return _request("GET", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params={k: v for k, v in {"expand": expand}.items() if v is not None})


@mcp.tool()
def update_worklog(issue_id_or_key: str, worklog_id: str, payload: dict, notify_users: Optional[bool] = None, adjust_estimate: Optional[str] = None, new_estimate: Optional[str] = None, expand: Optional[str] = None, override_editable_flag: Optional[bool] = None):
    params = {k: v for k, v in {"notifyUsers": notify_users, "adjustEstimate": adjust_estimate, "newEstimate": new_estimate, "expand": expand, "overrideEditableFlag": override_editable_flag}.items() if v is not None}
    return _request("PUT", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params, json_body=payload)


@mcp.tool()
def delete_worklog(issue_id_or_key: str, worklog_id: str, notify_users: Optional[bool] = None, adjust_estimate: Optional[str] = None, new_estimate: Optional[str] = None, expand: Optional[str] = None, override_editable_flag: Optional[bool] = None):
    params = {k: v for k, v in {"notifyUsers": notify_users, "adjustEstimate": adjust_estimate, "newEstimate": new_estimate, "expand": expand, "overrideEditableFlag": override_editable_flag}.items() if v is not None}
    return _request("DELETE", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params)


@mcp.tool()
def get_attachment_metadata(attachment_id: str):
    return _request("GET", f"/attachment/{attachment_id}")


@mcp.tool()
def delete_attachment(attachment_id: str):
    return _request("DELETE", f"/attachment/{attachment_id}")


@mcp.tool()
def get_attachment_content(attachment_id: str, redirect: Optional[bool] = None):
    return _request("GET", f"/attachment/content/{attachment_id}", params={k: v for k, v in {"redirect": redirect}.items() if v is not None})


@mcp.tool()
def get_attachment_thumbnail(attachment_id: str, redirect: Optional[bool] = None, fallback_to_default: Optional[bool] = None, width: Optional[int] = None, height: Optional[int] = None):
    params = {k: v for k, v in {"redirect": redirect, "fallbackToDefault": fallback_to_default, "width": width, "height": height}.items() if v is not None}
    return _request("GET", f"/attachment/thumbnail/{attachment_id}", params=params)


@mcp.tool()
def add_attachment(issue_id_or_key: str, file_path: str):
    url = _base_url() + f"/issue/{issue_id_or_key}/attachments"
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            resp = requests.post(url, files=files, headers={"X-Atlassian-Token": "no-check", "Accept": "application/json"}, auth=_auth(), timeout=60)
            if resp.status_code >= 400:
                return {"error": resp.text, "status": resp.status_code}
            return resp.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_issues_jql(jql: str, start_at: Optional[int] = None, max_results: Optional[int] = None, fields: Optional[list] = None):
    payload = {"jql": jql}
    if start_at is not None:
        payload["startAt"] = start_at
    if max_results is not None:
        payload["maxResults"] = max_results
    if fields is not None:
        payload["fields"] = fields
    return _request("POST", "/search", json_body=payload)


@mcp.tool()
def create_project(payload: dict):
    return _request("POST", "/project", json_body=payload)


@mcp.tool()
def get_project(project_id_or_key: str):
    return _request("GET", f"/project/{project_id_or_key}")


@mcp.tool()
def update_project(project_id_or_key: str, payload: dict):
    return _request("PUT", f"/project/{project_id_or_key}", json_body=payload)


@mcp.tool()
def delete_project(project_id_or_key: str):
    return _request("DELETE", f"/project/{project_id_or_key}")


@mcp.tool()
def get_project_components(project_id_or_key: str):
    return _request("GET", f"/project/{project_id_or_key}/components")


@mcp.tool()
def create_project_component(payload: dict):
    return _request("POST", "/component", json_body=payload)


@mcp.tool()
def update_project_component(component_id: str, payload: dict):
    return _request("PUT", f"/component/{component_id}", json_body=payload)


@mcp.tool()
def delete_project_component(component_id: str):
    return _request("DELETE", f"/component/{component_id}")


@mcp.tool()
def get_project_versions(project_id_or_key: str):
    return _request("GET", f"/project/{project_id_or_key}/versions")


@mcp.tool()
def create_project_version(payload: dict):
    return _request("POST", "/version", json_body=payload)


@mcp.tool()
def update_project_version(version_id: str, payload: dict):
    return _request("PUT", f"/version/{version_id}", json_body=payload)


@mcp.tool()
def delete_project_version(version_id: str):
    return _request("DELETE", f"/version/{version_id}")


if __name__ == "__main__":
    mcp.run()
