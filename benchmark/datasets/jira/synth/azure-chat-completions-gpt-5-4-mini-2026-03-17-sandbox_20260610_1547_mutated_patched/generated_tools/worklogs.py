from .core import jira_request


def get_issue_worklogs(issue_id_or_key, start_index=None, page_size=None, startedAfter=None, startedBefore=None, expand=None):
    return jira_request('GET', f'/issue/{issue_id_or_key}/worklog', query={'startAt': start_index, 'maxResults': page_size, 'startedAfter': startedAfter, 'startedBefore': startedBefore, 'expand': expand})


def add_worklog(issue_id_or_key, payload, notifyUsers=None, adjustEstimate=None, newEstimate=None, reduceBy=None, expand=None, overrideEditableFlag=None):
    return jira_request('POST', f'/issue/{issue_id_or_key}/worklog', query={'notifyUsers': notifyUsers, 'adjustEstimate': adjustEstimate, 'newEstimate': newEstimate, 'reduceBy': reduceBy, 'expand': expand, 'overrideEditableFlag': overrideEditableFlag}, body=payload)
