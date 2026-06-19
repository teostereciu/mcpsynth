from .core import jira_request


def create_issue(payload):
    return jira_request('POST', '/issue', body=payload)


def get_issue(issue_id_or_key, fields=None, expand=None):
    q = {'fields': fields, 'expand': expand}
    return jira_request('GET', f'/issue/{issue_id_or_key}', query=q)


def update_issue(issue_id_or_key, payload):
    return jira_request('PUT', f'/issue/{issue_id_or_key}', body=payload)


def delete_issue(issue_id_or_key):
    return jira_request('DELETE', f'/issue/{issue_id_or_key}')


def assign_issue(issue_id_or_key, payload):
    return jira_request('PUT', f'/issue/{issue_id_or_key}/assignee', body=payload)


def get_issue_transitions(issue_id_or_key):
    return jira_request('GET', f'/issue/{issue_id_or_key}/transitions')


def transition_issue(issue_id_or_key, payload):
    return jira_request('POST', f'/issue/{issue_id_or_key}/transitions', body=payload)
