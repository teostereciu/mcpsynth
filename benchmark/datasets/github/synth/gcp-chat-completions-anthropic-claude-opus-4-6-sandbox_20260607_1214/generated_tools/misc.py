"""GitHub miscellaneous tools (deploy keys, markdown, licenses, rate limit, etc.)."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_put, github_delete


# Deploy Keys
def list_deploy_keys(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List deploy keys for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/keys", {"per_page": per_page, "page": page})


def create_deploy_key(owner: str, repo: str, title: str, key: str,
                      read_only: bool = True) -> Any:
    """Create a deploy key.

    Args:
        owner: Repository owner
        repo: Repository name
        title: Key title
        key: Public SSH key
        read_only: Whether the key is read-only
    """
    return github_post(f"/repos/{owner}/{repo}/keys", {"title": title, "key": key, "read_only": read_only})


def get_deploy_key(owner: str, repo: str, key_id: int) -> Any:
    """Get a deploy key.

    Args:
        owner: Repository owner
        repo: Repository name
        key_id: Key ID
    """
    return github_get(f"/repos/{owner}/{repo}/keys/{key_id}")


def delete_deploy_key(owner: str, repo: str, key_id: int) -> Any:
    """Delete a deploy key.

    Args:
        owner: Repository owner
        repo: Repository name
        key_id: Key ID
    """
    return github_delete(f"/repos/{owner}/{repo}/keys/{key_id}")


# Actions Secrets
def list_repository_secrets(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List repository secrets for GitHub Actions.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/actions/secrets", {"per_page": per_page, "page": page})


def get_repository_public_key(owner: str, repo: str) -> Any:
    """Get a repository public key for encrypting secrets.

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_get(f"/repos/{owner}/{repo}/actions/secrets/public-key")


def get_repository_secret(owner: str, repo: str, secret_name: str) -> Any:
    """Get a repository secret (metadata only, not the value).

    Args:
        owner: Repository owner
        repo: Repository name
        secret_name: Secret name
    """
    return github_get(f"/repos/{owner}/{repo}/actions/secrets/{secret_name}")


def create_or_update_repository_secret(owner: str, repo: str, secret_name: str,
                                        encrypted_value: str, key_id: str) -> Any:
    """Create or update a repository secret.

    Args:
        owner: Repository owner
        repo: Repository name
        secret_name: Secret name
        encrypted_value: Value encrypted with the repository public key
        key_id: ID of the public key used for encryption
    """
    return github_put(f"/repos/{owner}/{repo}/actions/secrets/{secret_name}",
                      {"encrypted_value": encrypted_value, "key_id": key_id})


def delete_repository_secret(owner: str, repo: str, secret_name: str) -> Any:
    """Delete a repository secret.

    Args:
        owner: Repository owner
        repo: Repository name
        secret_name: Secret name
    """
    return github_delete(f"/repos/{owner}/{repo}/actions/secrets/{secret_name}")


# Actions Variables
def list_repository_variables(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List repository variables for GitHub Actions.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/actions/variables", {"per_page": per_page, "page": page})


def get_repository_variable(owner: str, repo: str, name: str) -> Any:
    """Get a repository variable.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Variable name
    """
    return github_get(f"/repos/{owner}/{repo}/actions/variables/{name}")


def create_repository_variable(owner: str, repo: str, name: str, value: str) -> Any:
    """Create a repository variable.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Variable name
        value: Variable value
    """
    return github_post(f"/repos/{owner}/{repo}/actions/variables", {"name": name, "value": value})


def update_repository_variable(owner: str, repo: str, name: str, value: str) -> Any:
    """Update a repository variable.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Variable name
        value: New variable value
    """
    from generated_tools.github_client import github_patch
    return github_patch(f"/repos/{owner}/{repo}/actions/variables/{name}", {"name": name, "value": value})


def delete_repository_variable(owner: str, repo: str, name: str) -> Any:
    """Delete a repository variable.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Variable name
    """
    return github_delete(f"/repos/{owner}/{repo}/actions/variables/{name}")


# Rate Limit
def get_rate_limit() -> Any:
    """Get the current rate limit status for the authenticated user."""
    return github_get("/rate_limit")


# Licenses
def list_licenses() -> Any:
    """List commonly used open source licenses."""
    return github_get("/licenses")


def get_license(license_key: str) -> Any:
    """Get a license by key.

    Args:
        license_key: License key (e.g. 'mit', 'apache-2.0')
    """
    return github_get(f"/licenses/{license_key}")


# Markdown
def render_markdown(text: str, mode: str = "markdown", context: Optional[str] = None) -> Any:
    """Render a Markdown document.

    Args:
        text: Markdown text to render
        mode: Rendering mode (markdown, gfm)
        context: Repository context for gfm mode (owner/repo)
    """
    data = {"text": text, "mode": mode}
    if context:
        data["context"] = context
    return github_post("/markdown", data)


# Meta
def get_meta() -> Any:
    """Get GitHub meta information (IP addresses, SSH keys, etc.)."""
    return github_get("/meta")


# Repo Rules
def list_repository_rulesets(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List repository rulesets.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/rulesets", {"per_page": per_page, "page": page})


def get_repository_ruleset(owner: str, repo: str, ruleset_id: int) -> Any:
    """Get a repository ruleset.

    Args:
        owner: Repository owner
        repo: Repository name
        ruleset_id: Ruleset ID
    """
    return github_get(f"/repos/{owner}/{repo}/rulesets/{ruleset_id}")
