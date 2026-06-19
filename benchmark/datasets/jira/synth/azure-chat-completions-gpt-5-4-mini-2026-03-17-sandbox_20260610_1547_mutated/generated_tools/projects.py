from .core import jira_request


def get_projects():
    return jira_request('GET', '/project')


def create_project(payload):
    return jira_request('POST', '/project', body=payload)


def search_projects(start_index=None, page_size=None, orderBy=None, id=None, keys=None, query=None, typeKey=None, categoryId=None, action=None, expand=None):
    q = {'start_index': start_index, 'page_size': page_size, 'orderBy': orderBy, 'id': id, 'keys': keys, 'query': query, 'typeKey': typeKey, 'categoryId': categoryId, 'action': action, 'expand': expand}
    return jira_request('GET', '/project/search', query=q)


def get_project(project_id_or_key, expand=None, properties=None):
    return jira_request('GET', f'/project/{project_id_or_key}', query={'expand': expand, 'properties': properties})


def update_project(project_id_or_key, payload):
    return jira_request('PUT', f'/project/{project_id_or_key}', body=payload)


def delete_project(project_id_or_key):
    return jira_request('DELETE', f'/project/{project_id_or_key}')
