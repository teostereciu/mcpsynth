import os
import requests

BASE_URL = os.getenv('GITHUB_API_BASE_URL', 'https://api.github.com')
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2026-03-10'
}


def list_org_repos(org, type='all', sort='created', direction='desc', per_page=30, page=1):
    """List repositories for the specified organization."""
    url = f'{BASE_URL}/orgs/{org}/repos'
    params = {
        'type': type,
        'sort': sort,
        'direction': direction,
        'per_page': per_page,
        'page': page
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def create_org_repo(org, name, description=None, homepage=None, private=False, has_issues=True, has_projects=True, has_wiki=True, has_downloads=True, is_template=False, team_id=None, auto_init=False, gitignore_template=None, license_template=None, allow_squash_merge=True, allow_merge_commit=True, allow_rebase_merge=True, allow_auto_merge=False, delete_branch_on_merge=False, squash_merge_commit_title=None, squash_merge_commit_message=None, merge_commit_title=None, merge_commit_message=None, custom_properties=None):
    """Create a new repository in the specified organization."""
    url = f'{BASE_URL}/orgs/{org}/repos'
    data = {
        'name': name,
        'private': private,
        'has_issues': has_issues,
        'has_projects': has_projects,
        'has_wiki': has_wiki,
        'has_downloads': has_downloads,
        'is_template': is_template,
        'auto_init': auto_init
    }
    if description is not None:
        data['description'] = description
    if homepage is not None:
        data['homepage'] = homepage
    if team_id is not None:
        data['team_id'] = team_id
    if gitignore_template is not None:
        data['gitignore_template'] = gitignore_template
    if license_template is not None:
        data['license_template'] = license_template
    if allow_squash_merge is not None:
        data['allow_squash_merge'] = allow_squash_merge
    if allow_merge_commit is not None:
        data['allow_merge_commit'] = allow_merge_commit
    if allow_rebase_merge is not None:
        data['allow_rebase_merge'] = allow_rebase_merge
    if allow_auto_merge is not None:
        data['allow_auto_merge'] = allow_auto_merge
    if delete_branch_on_merge is not None:
        data['delete_branch_on_merge'] = delete_branch_on_merge
    if squash_merge_commit_title is not None:
        data['squash_merge_commit_title'] = squash_merge_commit_title
    if squash_merge_commit_message is not None:
        data['squash_merge_commit_message'] = squash_merge_commit_message
    if merge_commit_title is not None:
        data['merge_commit_title'] = merge_commit_title
    if merge_commit_message is not None:
        data['merge_commit_message'] = merge_commit_message
    if custom_properties is not None:
        data['custom_properties'] = custom_properties
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}
