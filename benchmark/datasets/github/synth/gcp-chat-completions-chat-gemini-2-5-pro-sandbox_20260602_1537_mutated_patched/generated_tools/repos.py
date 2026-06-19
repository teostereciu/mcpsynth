from .utils import _github_api_request

def get_repository(owner: str, repo: str):
    """
    Get a repository.
    https://docs.github.com/en/rest/repos/repos#get-a-repository
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}")
