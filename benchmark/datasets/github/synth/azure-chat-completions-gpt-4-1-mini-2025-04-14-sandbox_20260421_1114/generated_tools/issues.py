import os
import requests

BASE_URL = os.getenv('GITHUB_API_BASE_URL', 'https://api.github.com')
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2026-03-10'
}


def list_issues_assigned_to_authenticated_user(filter='assigned', state='open', labels=None, sort='created', direction='desc', since=None, per_page=30, page=1):
    """List issues assigned to the authenticated user across all visible repositories."""
    url = f'{BASE_URL}/issues'
    params = {
        'filter': filter,
        'state': state,
        'sort': sort,
        'direction': direction,
        'per_page': per_page,
        'page': page
    }
    if labels:
        params['labels'] = labels
    if since:
        params['since'] = since
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def get_issue(owner, repo, issue_number):
    """Get a single issue."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def create_issue(owner, repo, title, body=None, assignees=None, milestone=None, labels=None):
    """Create an issue."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/issues'
    data = {'title': title}
    if body:
        data['body'] = body
    if assignees:
        data['assignees'] = assignees
    if milestone:
        data['milestone'] = milestone
    if labels:
        data['labels'] = labels
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def update_issue(owner, repo, issue_number, title=None, body=None, assignees=None, state=None, milestone=None, labels=None):
    """Update an issue."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}'
    data = {}
    if title is not None:
        data['title'] = title
    if body is not None:
        data['body'] = body
    if assignees is not None:
        data['assignees'] = assignees
    if state is not None:
        data['state'] = state
    if milestone is not None:
        data['milestone'] = milestone
    if labels is not None:
        data['labels'] = labels
    try:
        response = requests.patch(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def lock_issue(owner, repo, issue_number, lock_reason=None):
    """Lock an issue."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}/lock'
    data = {}
    if lock_reason:
        data['lock_reason'] = lock_reason
    try:
        response = requests.put(url, headers=HEADERS, json=data if data else None)
        if response.status_code == 204:
            return {'result': 'Issue locked successfully'}
        else:
            return {'error': 'Failed to lock issue', 'status_code': response.status_code}
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def unlock_issue(owner, repo, issue_number):
    """Unlock an issue."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}/lock'
    try:
        response = requests.delete(url, headers=HEADERS)
        if response.status_code == 204:
            return {'result': 'Issue unlocked successfully'}
        else:
            return {'error': 'Failed to unlock issue', 'status_code': response.status_code}
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}
