import os
import requests

BASE_URL = os.getenv('GITHUB_API_BASE_URL', 'https://api.github.com')
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2026-03-10'
}


def list_workflows(owner, repo, per_page=30, page=1):
    """List the workflows in a repository."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/actions/workflows'
    params = {
        'per_page': per_page,
        'page': page
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def get_workflow(owner, repo, workflow_id):
    """Get a specific workflow."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/actions/workflows/{workflow_id}'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def disable_workflow(owner, repo, workflow_id):
    """Disable a workflow."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable'
    try:
        response = requests.put(url, headers=HEADERS)
        if response.status_code == 204:
            return {'result': 'Workflow disabled successfully'}
        else:
            return {'error': 'Failed to disable workflow', 'status_code': response.status_code}
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def create_workflow_dispatch_event(owner, repo, workflow_id, ref, inputs=None):
    """Create a workflow dispatch event to manually trigger a workflow run."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches'
    data = {
        'ref': ref
    }
    if inputs is not None:
        data['inputs'] = inputs
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
        else:
            return {'result': 'Workflow dispatch event created'}
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def enable_workflow(owner, repo, workflow_id):
    """Enable a workflow."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable'
    try:
        response = requests.put(url, headers=HEADERS)
        if response.status_code == 204:
            return {'result': 'Workflow enabled successfully'}
        else:
            return {'error': 'Failed to enable workflow', 'status_code': response.status_code}
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def get_workflow_usage(owner, repo, workflow_id):
    """Get the number of billable minutes used by a specific workflow during the current billing cycle."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}
