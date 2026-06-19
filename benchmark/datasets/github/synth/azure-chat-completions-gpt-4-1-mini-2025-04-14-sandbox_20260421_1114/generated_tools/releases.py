import os
import requests

BASE_URL = os.getenv('GITHUB_API_BASE_URL', 'https://api.github.com')
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2026-03-10'
}


def list_releases(owner, repo, per_page=30, page=1):
    """List releases for a repository."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases'
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


def create_release(owner, repo, tag_name, target_commitish=None, name=None, body=None, draft=False, prerelease=False, discussion_category_name=None, generate_release_notes=False, make_latest=True):
    """Create a release."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases'
    data = {
        'tag_name': tag_name,
        'draft': draft,
        'prerelease': prerelease,
        'generate_release_notes': generate_release_notes,
        'make_latest': make_latest
    }
    if target_commitish is not None:
        data['target_commitish'] = target_commitish
    if name is not None:
        data['name'] = name
    if body is not None:
        data['body'] = body
    if discussion_category_name is not None:
        data['discussion_category_name'] = discussion_category_name
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def generate_release_notes(owner, repo, tag_name, target_commitish=None, previous_tag_name=None, configuration_file_path=None):
    """Generate release notes content for a release."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases/generate-notes'
    data = {
        'tag_name': tag_name
    }
    if target_commitish is not None:
        data['target_commitish'] = target_commitish
    if previous_tag_name is not None:
        data['previous_tag_name'] = previous_tag_name
    if configuration_file_path is not None:
        data['configuration_file_path'] = configuration_file_path
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def get_latest_release(owner, repo):
    """Get the latest release."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases/latest'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def get_release_by_tag(owner, repo, tag):
    """Get a release by tag name."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases/tags/{tag}'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def get_release(owner, repo, release_id):
    """Get a release by ID."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases/{release_id}'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def update_release(owner, repo, release_id, tag_name=None, target_commitish=None, name=None, body=None, draft=None, prerelease=None, make_latest=None):
    """Update a release."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases/{release_id}'
    data = {}
    if tag_name is not None:
        data['tag_name'] = tag_name
    if target_commitish is not None:
        data['target_commitish'] = target_commitish
    if name is not None:
        data['name'] = name
    if body is not None:
        data['body'] = body
    if draft is not None:
        data['draft'] = draft
    if prerelease is not None:
        data['prerelease'] = prerelease
    if make_latest is not None:
        data['make_latest'] = make_latest
    try:
        response = requests.patch(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def delete_release(owner, repo, release_id):
    """Delete a release."""
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases/{release_id}'
    try:
        response = requests.delete(url, headers=HEADERS)
        if response.status_code == 204:
            return {'result': 'Release deleted successfully'}
        else:
            return {'error': 'Failed to delete release', 'status_code': response.status_code}
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}
