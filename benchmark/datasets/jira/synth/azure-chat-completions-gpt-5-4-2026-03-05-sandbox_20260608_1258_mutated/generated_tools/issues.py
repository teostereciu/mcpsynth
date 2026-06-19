from typing import Any, Optional

from .common import JiraClient, compact_dict


def create_issue(
    fields: dict,
    update: Optional[dict] = None,
    transition: Optional[dict] = None,
    properties: Optional[list] = None,
    history_metadata: Optional[dict] = None,
    update_history: Optional[bool] = None,
) -> Any:
    client = JiraClient()
    body = compact_dict(
        {
            "fields": fields,
            "update": update,
            "transition": transition,
            "properties": properties,
            "historyMetadata": history_metadata,
        }
    )
    return client.request("POST", "/rest/api/3/issue", params=compact_dict({"updateHistory": update_history}), json_body=body)


def get_issue(issue_id_or_key: str, fields: Optional[str] = None, expand: Optional[str] = None, properties: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request(
        "GET",
        f"/rest/api/3/issue/{issue_id_or_key}",
        params=compact_dict({"fields": fields, "expand": expand, "properties": properties}),
    )


def update_issue(
    issue_id_or_key: str,
    fields: Optional[dict] = None,
    update: Optional[dict] = None,
    history_metadata: Optional[dict] = None,
    properties: Optional[list] = None,
    notify_users: Optional[bool] = None,
    override_screen_security: Optional[bool] = None,
    override_editable_flag: Optional[bool] = None,
    return_issue: Optional[bool] = None,
) -> Any:
    client = JiraClient()
    body = compact_dict(
        {
            "fields": fields,
            "update": update,
            "historyMetadata": history_metadata,
            "properties": properties,
        }
    )
    return client.request(
        "PUT",
        f"/rest/api/3/issue/{issue_id_or_key}",
        params=compact_dict(
            {
                "notifyUsers": notify_users,
                "overrideScreenSecurity": override_screen_security,
                "overrideEditableFlag": override_editable_flag,
                "returnIssue": return_issue,
            }
        ),
        json_body=body,
    )


def delete_issue(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}", params=compact_dict({"deleteSubtasks": delete_subtasks}))


def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("PUT", f"/rest/api/3/issue/{issue_id_or_key}/assignee", json_body=compact_dict({"accountId": account_id}))


def get_issue_changelog(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    client = JiraClient()
    return client.request(
        "GET",
        f"/rest/api/3/issue/{issue_id_or_key}/changelog",
        params=compact_dict({"startAt": start_at, "maxResults": max_results}),
    )


def get_edit_metadata(issue_id_or_key: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/issue/{issue_id_or_key}/editmeta")


def get_transitions(issue_id_or_key: str, expand: Optional[str] = None, transition_id: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request(
        "GET",
        f"/rest/api/3/issue/{issue_id_or_key}/transitions",
        params=compact_dict({"expand": expand, "transitionId": transition_id}),
    )


def transition_issue(issue_id_or_key: str, transition: dict, fields: Optional[dict] = None, update: Optional[dict] = None, history_metadata: Optional[dict] = None) -> Any:
    client = JiraClient()
    return client.request(
        "POST",
        f"/rest/api/3/issue/{issue_id_or_key}/transitions",
        json_body=compact_dict({"transition": transition, "fields": fields, "update": update, "historyMetadata": history_metadata}),
    )


def get_create_metadata(project_ids_or_keys: Optional[str] = None, issuetype_ids: Optional[str] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request(
        "GET",
        "/rest/api/3/issue/createmeta",
        params=compact_dict({"projectIdsOrKeys": project_ids_or_keys, "issuetypeIds": issuetype_ids, "expand": expand}),
    )


def get_comments_by_ids(ids: list[int], expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/comment/list", params=compact_dict({"expand": expand}), json_body={"ids": ids})


def get_issue_comments(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request(
        "GET",
        f"/rest/api/3/issue/{issue_id_or_key}/comment",
        params=compact_dict({"startAt": start_at, "maxResults": max_results, "orderBy": order_by, "expand": expand}),
    )


def add_comment(issue_id_or_key: str, body: Any, visibility: Optional[dict] = None, properties: Optional[list] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request(
        "POST",
        f"/rest/api/3/issue/{issue_id_or_key}/comment",
        params=compact_dict({"expand": expand}),
        json_body=compact_dict({"body": body, "visibility": visibility, "properties": properties}),
    )


def get_comment(issue_id_or_key: str, comment_id: str, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/issue/{issue_id_or_key}/comment/{comment_id}", params=compact_dict({"expand": expand}))


def update_comment(issue_id_or_key: str, comment_id: str, body: Any, visibility: Optional[dict] = None, properties: Optional[list] = None, notify_users: Optional[bool] = None, override_editable_flag: Optional[bool] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request(
        "PUT",
        f"/rest/api/3/issue/{issue_id_or_key}/comment/{comment_id}",
        params=compact_dict({"notifyUsers": notify_users, "overrideEditableFlag": override_editable_flag, "expand": expand}),
        json_body=compact_dict({"body": body, "visibility": visibility, "properties": properties}),
    )


def delete_comment(issue_id_or_key: str, comment_id: str) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/comment/{comment_id}")


def get_issue_worklogs(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None, started_after: Optional[int] = None, started_before: Optional[int] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request(
        "GET",
        f"/rest/api/3/issue/{issue_id_or_key}/worklog",
        params=compact_dict({"startAt": start_at, "maxResults": max_results, "startedAfter": started_after, "startedBefore": started_before, "expand": expand}),
    )


def add_worklog(issue_id_or_key: str, time_spent_seconds: Optional[int] = None, time_spent: Optional[str] = None, started: Optional[str] = None, comment: Optional[Any] = None, visibility: Optional[dict] = None, properties: Optional[list] = None, notify_users: Optional[bool] = None, adjust_estimate: Optional[str] = None, new_estimate: Optional[str] = None, reduce_by: Optional[str] = None, expand: Optional[str] = None, override_editable_flag: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request(
        "POST",
        f"/rest/api/3/issue/{issue_id_or_key}/worklog",
        params=compact_dict({"notifyUsers": notify_users, "adjustEstimate": adjust_estimate, "newEstimate": new_estimate, "reduceBy": reduce_by, "expand": expand, "overrideEditableFlag": override_editable_flag}),
        json_body=compact_dict({"timeSpentSeconds": time_spent_seconds, "timeSpent": time_spent, "started": started, "comment": comment, "visibility": visibility, "properties": properties}),
    )


def bulk_delete_worklogs(issue_id_or_key: str, ids: list[int], adjust_estimate: Optional[str] = None, override_editable_flag: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request(
        "DELETE",
        f"/rest/api/3/issue/{issue_id_or_key}/worklog",
        params=compact_dict({"adjustEstimate": adjust_estimate, "overrideEditableFlag": override_editable_flag}),
        json_body={"ids": ids},
    )


def move_worklogs(issue_id_or_key: str, ids: list[int], destination_issue_id_or_key: str, adjust_estimate: Optional[str] = None, override_editable_flag: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request(
        "POST",
        f"/rest/api/3/issue/{issue_id_or_key}/worklog/move",
        params=compact_dict({"adjustEstimate": adjust_estimate, "overrideEditableFlag": override_editable_flag}),
        json_body={"ids": ids, "issueIdOrKey": destination_issue_id_or_key},
    )


def get_worklog(issue_id_or_key: str, worklog_id: str, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}", params=compact_dict({"expand": expand}))


def update_worklog(issue_id_or_key: str, worklog_id: str, time_spent_seconds: Optional[int] = None, time_spent: Optional[str] = None, started: Optional[str] = None, comment: Optional[Any] = None, visibility: Optional[dict] = None, properties: Optional[list] = None, notify_users: Optional[bool] = None, adjust_estimate: Optional[str] = None, new_estimate: Optional[str] = None, expand: Optional[str] = None, override_editable_flag: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request(
        "PUT",
        f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}",
        params=compact_dict({"notifyUsers": notify_users, "adjustEstimate": adjust_estimate, "newEstimate": new_estimate, "expand": expand, "overrideEditableFlag": override_editable_flag}),
        json_body=compact_dict({"timeSpentSeconds": time_spent_seconds, "timeSpent": time_spent, "started": started, "comment": comment, "visibility": visibility, "properties": properties}),
    )


def delete_worklog(issue_id_or_key: str, worklog_id: str, notify_users: Optional[bool] = None, adjust_estimate: Optional[str] = None, new_estimate: Optional[str] = None, increase_by: Optional[str] = None, override_editable_flag: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request(
        "DELETE",
        f"/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}",
        params=compact_dict({"notifyUsers": notify_users, "adjustEstimate": adjust_estimate, "newEstimate": new_estimate, "increaseBy": increase_by, "overrideEditableFlag": override_editable_flag}),
    )


def get_is_watching_issue_bulk(issue_ids: list[str]) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/issue/watching", json_body={"issueIds": issue_ids})


def get_issue_watchers(issue_id_or_key: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/issue/{issue_id_or_key}/watchers")


def add_watcher(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("POST", f"/rest/api/3/issue/{issue_id_or_key}/watchers", json_body=account_id)


def remove_watcher(issue_id_or_key: str, account_id: Optional[str] = None, username: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/issue/{issue_id_or_key}/watchers", params=compact_dict({"accountId": account_id, "username": username, "user_id": account_id}))


def get_attachment_settings() -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/attachment/meta")


def get_attachment(attachment_id: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/attachment/{attachment_id}")


def delete_attachment(attachment_id: str) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/attachment/{attachment_id}")


def get_attachment_content(attachment_id: str, redirect: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/attachment/content/{attachment_id}", params=compact_dict({"redirect": redirect}))


def get_attachment_thumbnail(attachment_id: str, redirect: Optional[bool] = None, fallback_to_default: Optional[bool] = None, width: Optional[int] = None, height: Optional[int] = None) -> Any:
    client = JiraClient()
    return client.request(
        "GET",
        f"/rest/api/3/attachment/thumbnail/{attachment_id}",
        params=compact_dict({"redirect": redirect, "fallbackToDefault": fallback_to_default, "width": width, "height": height}),
    )


def get_attachment_expanded_human(attachment_id: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/attachment/{attachment_id}/expand/human")


def get_attachment_expanded_raw(attachment_id: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/attachment/{attachment_id}/expand/raw")


def add_attachment(issue_id_or_key: str, file_paths: list[str]) -> Any:
    client = JiraClient()
    files = []
    handles = []
    try:
        for path in file_paths:
            handle = open(path, "rb")
            handles.append(handle)
            files.append(("file", (path.split("/")[-1], handle)))
        return client.request(
            "POST",
            f"/rest/api/3/issue/{issue_id_or_key}/attachments",
            headers={"X-Atlassian-Token": "no-check"},
            files=files,
        )
    finally:
        for handle in handles:
            handle.close()
