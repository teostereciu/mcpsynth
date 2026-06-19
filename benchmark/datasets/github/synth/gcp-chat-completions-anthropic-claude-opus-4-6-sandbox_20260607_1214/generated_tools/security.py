"""GitHub Security tools (code scanning, secret scanning, Dependabot)."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_patch


def list_code_scanning_alerts(owner: str, repo: str, state: Optional[str] = None,
                              ref: Optional[str] = None, severity: Optional[str] = None,
                              tool_name: Optional[str] = None,
                              per_page: int = 30, page: int = 1) -> Any:
    """List code scanning alerts for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        state: Filter by state (open, closed, dismissed, fixed)
        ref: Git reference
        severity: Filter by severity (critical, high, medium, low, warning, note, error)
        tool_name: Filter by tool name
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if state:
        params["state"] = state
    if ref:
        params["ref"] = ref
    if severity:
        params["severity"] = severity
    if tool_name:
        params["tool_name"] = tool_name
    return github_get(f"/repos/{owner}/{repo}/code-scanning/alerts", params)


def get_code_scanning_alert(owner: str, repo: str, alert_number: int) -> Any:
    """Get a code scanning alert.

    Args:
        owner: Repository owner
        repo: Repository name
        alert_number: Alert number
    """
    return github_get(f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}")


def update_code_scanning_alert(owner: str, repo: str, alert_number: int, state: str,
                               dismissed_reason: Optional[str] = None,
                               dismissed_comment: Optional[str] = None) -> Any:
    """Update a code scanning alert.

    Args:
        owner: Repository owner
        repo: Repository name
        alert_number: Alert number
        state: New state (open, dismissed)
        dismissed_reason: Reason for dismissal (false positive, won't fix, used in tests, null)
        dismissed_comment: Dismissal comment
    """
    data = {"state": state}
    if dismissed_reason:
        data["dismissed_reason"] = dismissed_reason
    if dismissed_comment:
        data["dismissed_comment"] = dismissed_comment
    return github_patch(f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}", data)


def list_secret_scanning_alerts(owner: str, repo: str, state: Optional[str] = None,
                                secret_type: Optional[str] = None, resolution: Optional[str] = None,
                                per_page: int = 30, page: int = 1) -> Any:
    """List secret scanning alerts for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        state: Filter by state (open, resolved)
        secret_type: Filter by secret type
        resolution: Filter by resolution (false_positive, wont_fix, revoked, pattern_edited, pattern_deleted, used_in_tests)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if state:
        params["state"] = state
    if secret_type:
        params["secret_type"] = secret_type
    if resolution:
        params["resolution"] = resolution
    return github_get(f"/repos/{owner}/{repo}/secret-scanning/alerts", params)


def get_secret_scanning_alert(owner: str, repo: str, alert_number: int) -> Any:
    """Get a secret scanning alert.

    Args:
        owner: Repository owner
        repo: Repository name
        alert_number: Alert number
    """
    return github_get(f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}")


def update_secret_scanning_alert(owner: str, repo: str, alert_number: int, state: str,
                                 resolution: Optional[str] = None,
                                 resolution_comment: Optional[str] = None) -> Any:
    """Update a secret scanning alert.

    Args:
        owner: Repository owner
        repo: Repository name
        alert_number: Alert number
        state: New state (open, resolved)
        resolution: Resolution (false_positive, wont_fix, revoked, pattern_edited, pattern_deleted, used_in_tests)
        resolution_comment: Resolution comment
    """
    data = {"state": state}
    if resolution:
        data["resolution"] = resolution
    if resolution_comment:
        data["resolution_comment"] = resolution_comment
    return github_patch(f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}", data)


def list_dependabot_alerts(owner: str, repo: str, state: Optional[str] = None,
                           severity: Optional[str] = None, ecosystem: Optional[str] = None,
                           package: Optional[str] = None, scope: Optional[str] = None,
                           per_page: int = 30, page: int = 1) -> Any:
    """List Dependabot alerts for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        state: Filter by state (auto_dismissed, dismissed, fixed, open)
        severity: Filter by severity (low, medium, high, critical)
        ecosystem: Filter by ecosystem (composer, go, maven, npm, nuget, pip, pub, rubygems, rust)
        package: Filter by package name
        scope: Filter by scope (development, runtime)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if state:
        params["state"] = state
    if severity:
        params["severity"] = severity
    if ecosystem:
        params["ecosystem"] = ecosystem
    if package:
        params["package"] = package
    if scope:
        params["scope"] = scope
    return github_get(f"/repos/{owner}/{repo}/dependabot/alerts", params)


def get_dependabot_alert(owner: str, repo: str, alert_number: int) -> Any:
    """Get a Dependabot alert.

    Args:
        owner: Repository owner
        repo: Repository name
        alert_number: Alert number
    """
    return github_get(f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}")


def update_dependabot_alert(owner: str, repo: str, alert_number: int, state: str,
                            dismissed_reason: Optional[str] = None,
                            dismissed_comment: Optional[str] = None) -> Any:
    """Update a Dependabot alert.

    Args:
        owner: Repository owner
        repo: Repository name
        alert_number: Alert number
        state: New state (dismissed, open)
        dismissed_reason: Reason for dismissal (fix_started, inaccurate, no_bandwidth, not_used, tolerable_risk)
        dismissed_comment: Dismissal comment
    """
    data = {"state": state}
    if dismissed_reason:
        data["dismissed_reason"] = dismissed_reason
    if dismissed_comment:
        data["dismissed_comment"] = dismissed_comment
    return github_patch(f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}", data)
