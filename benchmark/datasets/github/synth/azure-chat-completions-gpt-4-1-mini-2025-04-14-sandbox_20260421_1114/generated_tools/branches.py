import os
import requests

BASE_URL = os.getenv('GITHUB_API_BASE_URL', 'https://api.github.com')
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2026-03-10'
}


def get_branch_protection(owner, repo, branch):
    """Get branch protection for a branch."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/branches/{branch}/protection'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def update_branch_protection(owner, repo, branch, required_status_checks=None, enforce_admins=None, required_pull_request_reviews=None, restrictions=None, required_linear_history=None, allow_force_pushes=None, allow_deletions=None, required_conversation_resolution=None, lock_branch=None, allow_fork_syncing=None):
    """Update branch protection for a branch."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/branches/{branch}/protection'
    data = {}
    if required_status_checks is not None:
        data['required_status_checks'] = required_status_checks
    if enforce_admins is not None:
        data['enforce_admins'] = enforce_admins
    if required_pull_request_reviews is not None:
        data['required_pull_request_reviews'] = required_pull_request_reviews
    if restrictions is not None:
        data['restrictions'] = restrictions
    if required_linear_history is not None:
        data['required_linear_history'] = required_linear_history
    if allow_force_pushes is not None:
        data['allow_force_pushes'] = allow_force_pushes
    if allow_deletions is not None:
        data['allow_deletions'] = allow_deletions
    if required_conversation_resolution is not None:
        data['required_conversation_resolution'] = required_conversation_resolution
    if lock_branch is not None:
        data['lock_branch'] = lock_branch
    if allow_fork_syncing is not None:
        data['allow_fork_syncing'] = allow_fork_syncing
    try:
        response = requests.put(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def delete_branch_protection(owner, repo, branch):
    """Delete branch protection for a branch."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/branches/{branch}/protection'
    try:
        response = requests.delete(url, headers=HEADERS)
        if response.status_code == 204:
            return {'result': 'Branch protection deleted successfully'}
        else:
            return {'error': 'Failed to delete branch protection', 'status_code': response.status_code}
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}
