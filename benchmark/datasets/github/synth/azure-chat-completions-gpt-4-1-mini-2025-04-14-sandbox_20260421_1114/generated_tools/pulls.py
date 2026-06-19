import os
import requests

BASE_URL = os.getenv('GITHUB_API_BASE_URL', 'https://api.github.com')
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2026-03-10'
}


def list_pull_requests(owner, repo, state='open', head=None, base=None, sort='created', direction=None, per_page=30, page=1):
    """List pull requests in a specified repository."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/pulls'
    params = {
        'state': state,
        'sort': sort,
        'per_page': per_page,
        'page': page
    }
    if head:
        params['head'] = head
    if base:
        params['base'] = base
    if direction:
        params['direction'] = direction
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def get_pull_request(owner, repo, pull_number):
    """Get a single pull request."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/pulls/{pull_number}'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def create_pull_request(owner, repo, title, head, base, body=None, draft=False):
    """Create a pull request."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/pulls'
    data = {
        'title': title,
        'head': head,
        'base': base,
        'draft': draft
    }
    if body:
        data['body'] = body
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def update_pull_request(owner, repo, pull_number, title=None, body=None, state=None):
    """Update a pull request."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/pulls/{pull_number}'
    data = {}
    if title is not None:
        data['title'] = title
    if body is not None:
        data['body'] = body
    if state is not None:
        data['state'] = state
    try:
        response = requests.patch(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def merge_pull_request(owner, repo, pull_number, commit_title=None, commit_message=None, merge_method=None):
    """Merge a pull request."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/pulls/{pull_number}/merge'
    data = {}
    if commit_title:
        data['commit_title'] = commit_title
    if commit_message:
        data['commit_message'] = commit_message
    if merge_method:
        data['merge_method'] = merge_method
    try:
        response = requests.put(url, headers=HEADERS, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Failed to merge pull request', 'status_code': response.status_code}
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}
