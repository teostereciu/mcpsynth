from .core import jira_request


def issue_picker(query=None, currentJQL=None, currentIssueKey=None, currentProjectId=None, showSubTasks=None, showSubTaskParent=None):
    return jira_request('GET', '/issue/picker', query={'query': query, 'currentJQL': currentJQL, 'currentIssueKey': currentIssueKey, 'currentProjectId': currentProjectId, 'showSubTasks': showSubTasks, 'showSubTaskParent': showSubTaskParent})


def jql_match(issueIds, jqls):
    return jira_request('POST', '/jql_query/match', body={'issueIds': issueIds, 'jqls': jqls})


def search_issues_get(jql_query=None, start_index=None, page_size=None, validateQuery=None, include_fields=None, expand=None, properties=None, fieldsByKeys=None, failFast=None):
    return jira_request('GET', '/search', query={'jql': jql_query, 'startAt': start_index, 'maxResults': page_size, 'validateQuery': validateQuery, 'fields': include_fields, 'expand': expand, 'properties': properties, 'fieldsByKeys': fieldsByKeys, 'failFast': failFast})


def search_issues_post(payload):
    return jira_request('POST', '/search', body=payload)
