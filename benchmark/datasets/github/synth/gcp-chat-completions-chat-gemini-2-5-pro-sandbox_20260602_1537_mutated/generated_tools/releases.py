from .utils import _github_api_request

def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1):
    """
    List releases.
    https://docs.github.com/en/rest/releases/releases#list-releases
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/releases", params={"per_page": per_page, "page": page})

def create_release(owner: str, repo: str, tag_name: str, target_commitish: str = None, name: str = None, body: str = None, draft: bool = None, prerelease: bool = None, generate_release_notes: bool = None):
    """
    Create a release.
    https://docs.github.com/en/rest/releases/releases#create-a-release
    """
    json_data = {"tag_name": tag_name, "target_commitish": target_commitish, "name": name, "body": body, "draft": draft, "prerelease": prerelease, "generate_release_notes": generate_release_notes}
    return _github_api_request("POST", f"/repos/{owner}/{repo}/releases", json_data=json_data)

def get_release(owner: str, repo: str, release_id: int):
    """
    Get a release.
    https://docs.github.com/en/rest/releases/releases#get-a-release
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")

def update_release(owner: str, repo: str, release_id: int, tag_name: str = None, target_commitish: str = None, name: str = None, body: str = None, draft: bool = None, prerelease: bool = None):
    """
    Update a release.
    https://docs.github.com/en/rest/releases/releases#update-a-release
    """
    json_data = {"tag_name": tag_name, "target_commitish": target_commitish, "name": name, "body": body, "draft": draft, "prerelease": prerelease}
    return _github_api_request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json_data=json_data)

def delete_release(owner: str, repo: str, release_id: int):
    """
    Delete a release.
    https://docs.github.com/en/rest/releases/releases#delete-a-release
    """
    return _github_api_request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")

def get_latest_release(owner: str, repo: str):
    """
    Get the latest release.
    https://docs.github.com/en/rest/releases/releases#get-the-latest-release
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/releases/latest")

def get_release_by_tag(owner: str, repo: str, tag: str):
    """
    Get a release by tag name.
    https://docs.github.com/en/rest/releases/releases#get-a-release-by-tag-name
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/releases/tags/{tag}")
