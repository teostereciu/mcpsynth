from .core import jira_request


def list_comments_by_ids(ids, expand=None):
    return jira_request('POST', '/comment/list', query={'expand': expand}, body={'ids': ids})


def get_issue_comments(issue_id_or_key, start_index=None, page_size=None, orderBy=None, expand=None):
    q = {'startAt': start_index, 'maxResults': page_size, 'orderBy': orderBy, 'expand': expand}
    return jira_request('GET', f'/issue/{issue_id_or_key}/comment', query=q)


def add_comment(issue_id_or_key, body, properties=None, visibility=None, expand=None):
    payload = {'body': body}
    if properties is not None:
        payload['properties'] = properties
    if visibility is not None:
        payload['visibility'] = visibility
    return jira_request('POST', f'/issue/{issue_id_or_key}/comment', query={'expand': expand}, body=payload)


def get_comment(issue_id_or_key, comment_id, expand=None):
    return jira_request('GET', f'/issue/{issue_id_or_key}/comment/{comment_id}', query={'expand': expand})


def update_comment(issue_id_or_key, comment_id, body, properties=None, visibility=None, notifyUsers=None, overrideEditableFlag=None, expand=None):
    payload = {'body': body}
    if properties is not None:
        payload['properties'] = properties
    if visibility is not None:
        payload['visibility'] = visibility
    q = {'notifyUsers': notifyUsers, 'overrideEditableFlag': overrideEditableFlag, 'expand': expand}
    return jira_request('PUT', f'/issue/{issue_id_or_key}/comment/{comment_id}', query=q, body=payload)


def delete_comment(issue_id_or_key, comment_id):
    return jira_request('DELETE', f'/issue/{issue_id_or_key}/comment/{comment_id}')
