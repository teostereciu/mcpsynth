import os
import requests

BASE_URL = os.getenv('GITHUB_API_BASE_URL', 'https://api.github.com')
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2026-03-10'
}


def search_code(q, sort=None, order=None, per_page=30, page=1):
    """Search code with a query string."""
    url = f'{BASE_URL}/search/code'
    params = {
        'q': q,
        'per_page': per_page,
        'page': page
    }
    if sort:
        params['sort'] = sort
    if order:
        params['order'] = order
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def search_commits(q, sort=None, order=None, per_page=30, page=1):
    """Search commits with a query string."""
    url = f'{BASE_URL}/search/commits'
    params = {
        'q': q,
        'per_page': per_page,
        'page': page
    }
    if sort:
        params['sort'] = sort
    if order:
        params['order'] = order
    headers = HEADERS.copy()
    headers['Accept'] = 'application/vnd.github.cloak-preview'
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def search_issues_and_pull_requests(q, sort=None, order=None, per_page=30, page=1):
    """Search issues and pull requests with a query string."""
    url = f'{BASE_URL}/search/issues'
    params = {
        'q': q,
        'per_page': per_page,
        'page': page
    }
    if sort:
        params['sort'] = sort
    if order:
        params['order'] = order
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def search_labels(q, sort=None, order=None, per_page=30, page=1):
    """Search labels with a query string."""
    url = f'{BASE_URL}/search/labels'
    params = {
        'q': q,
        'per_page': per_page,
        'page': page
    }
    if sort:
        params['sort'] = sort
    if order:
        params['order'] = order
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def search_repositories(q, sort=None, order=None, per_page=30, page=1):
    """Search repositories with a query string."""
    url = f'{BASE_URL}/search/repositories'
    params = {
        'q': q,
        'per_page': per_page,
        'page': page
    }
    if sort:
        params['sort'] = sort
    if order:
        params['order'] = order
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def search_topics(q, sort=None, order=None, per_page=30, page=1):
    """Search topics with a query string."""
    url = f'{BASE_URL}/search/topics'
    params = {
        'q': q,
        'per_page': per_page,
        'page': page
    }
    if sort:
        params['sort'] = sort
    if order:
        params['order'] = order
    headers = HEADERS.copy()
    headers['Accept'] = 'application/vnd.github.mercy-preview+json'
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}


def search_users(q, sort=None, order=None, per_page=30, page=1):
    """Search users with a query string."""
    url = f'{BASE_URL}/search/users'
    params = {
        'q': q,
        'per_page': per_page,
        'page': page
    }
    if sort:
        params['sort'] = sort
    if order:
        params['order'] = order
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {'error': str(e), 'status_code': response.status_code}
