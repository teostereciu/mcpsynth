"""MCP tools for GitHub Code Scanning, Secret Scanning, and Dependabot."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete

def register(mcp: FastMCP):

    # --- Code Scanning ---

    @mcp.tool()
    def list_code_scanning_alerts(
        owner: str,
        repo: str,
        tool_name: str = "",
        tool_guid: str = "",
        ref: str = "",
        state: str = "open",
        severity: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List code scanning alerts for a repository."""
        params: dict = {"state": state, "per_page": per_page, "page": page}
        if tool_name:
            params["tool_name"] = tool_name
        if tool_guid:
            params["tool_guid"] = tool_guid
        if ref:
            params["ref"] = ref
        if severity:
            params["severity"] = severity
        return gh_get(f"/repos/{owner}/{repo}/code-scanning/alerts", params=params)

    @mcp.tool()
    def get_code_scanning_alert(owner: str, repo: str, alert_number: int) -> dict | list:
        """Get a code scanning alert by number."""
        return gh_get(f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}")

    @mcp.tool()
    def update_code_scanning_alert(
        owner: str, repo: str, alert_number: int, state: str, dismissed_reason: str = "", dismissed_comment: str = ""
    ) -> dict | list:
        """Update a code scanning alert. state: open|dismissed."""
        payload: dict = {"state": state}
        if dismissed_reason:
            payload["dismissed_reason"] = dismissed_reason
        if dismissed_comment:
            payload["dismissed_comment"] = dismissed_comment
        return gh_patch(f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}", json=payload)

    @mcp.tool()
    def list_code_scanning_analyses(
        owner: str, repo: str, tool_name: str = "", ref: str = "",
        sarif_id: str = "", per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List code scanning analyses for a repository."""
        params: dict = {"per_page": per_page, "page": page}
        if tool_name:
            params["tool_name"] = tool_name
        if ref:
            params["ref"] = ref
        if sarif_id:
            params["sarif_id"] = sarif_id
        return gh_get(f"/repos/{owner}/{repo}/code-scanning/analyses", params=params)

    @mcp.tool()
    def get_code_scanning_analysis(owner: str, repo: str, analysis_id: int) -> dict | list:
        """Get a code scanning analysis."""
        return gh_get(f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}")

    @mcp.tool()
    def delete_code_scanning_analysis(
        owner: str, repo: str, analysis_id: int, confirm_delete: str = ""
    ) -> dict | list:
        """Delete a code scanning analysis."""
        params: dict = {}
        if confirm_delete:
            params["confirm_delete"] = confirm_delete
        return gh_delete(f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}")

    # --- Secret Scanning ---

    @mcp.tool()
    def list_secret_scanning_alerts(
        owner: str,
        repo: str,
        state: str = "open",
        secret_type: str = "",
        resolution: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List secret scanning alerts for a repository."""
        params: dict = {"state": state, "per_page": per_page, "page": page}
        if secret_type:
            params["secret_type"] = secret_type
        if resolution:
            params["resolution"] = resolution
        return gh_get(f"/repos/{owner}/{repo}/secret-scanning/alerts", params=params)

    @mcp.tool()
    def get_secret_scanning_alert(owner: str, repo: str, alert_number: int) -> dict | list:
        """Get a secret scanning alert by number."""
        return gh_get(f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}")

    @mcp.tool()
    def update_secret_scanning_alert(
        owner: str, repo: str, alert_number: int, state: str, resolution: str = "", resolution_comment: str = ""
    ) -> dict | list:
        """Update a secret scanning alert. state: open|resolved."""
        payload: dict = {"state": state}
        if resolution:
            payload["resolution"] = resolution
        if resolution_comment:
            payload["resolution_comment"] = resolution_comment
        return gh_patch(f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}", json=payload)

    @mcp.tool()
    def list_secret_scanning_alert_locations(
        owner: str, repo: str, alert_number: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List locations for a secret scanning alert."""
        return gh_get(f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations",
                      params={"per_page": per_page, "page": page})

    # --- Dependabot ---

    @mcp.tool()
    def list_dependabot_alerts(
        owner: str,
        repo: str,
        state: str = "open",
        severity: str = "",
        ecosystem: str = "",
        package: str = "",
        scope: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List Dependabot alerts for a repository."""
        params: dict = {"state": state, "per_page": per_page, "page": page}
        if severity:
            params["severity"] = severity
        if ecosystem:
            params["ecosystem"] = ecosystem
        if package:
            params["package"] = package
        if scope:
            params["scope"] = scope
        return gh_get(f"/repos/{owner}/{repo}/dependabot/alerts", params=params)

    @mcp.tool()
    def get_dependabot_alert(owner: str, repo: str, alert_number: int) -> dict | list:
        """Get a Dependabot alert by number."""
        return gh_get(f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}")

    @mcp.tool()
    def update_dependabot_alert(
        owner: str, repo: str, alert_number: int, state: str,
        dismissed_reason: str = "", dismissed_comment: str = ""
    ) -> dict | list:
        """Update a Dependabot alert. state: open|dismissed|auto_dismissed."""
        payload: dict = {"state": state}
        if dismissed_reason:
            payload["dismissed_reason"] = dismissed_reason
        if dismissed_comment:
            payload["dismissed_comment"] = dismissed_comment
        return gh_patch(f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}", json=payload)

    @mcp.tool()
    def list_dependabot_secrets(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List Dependabot secrets for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/dependabot/secrets",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_dependabot_public_key(owner: str, repo: str) -> dict | list:
        """Get the public key for encrypting Dependabot secrets."""
        return gh_get(f"/repos/{owner}/{repo}/dependabot/secrets/public-key")

    @mcp.tool()
    def delete_dependabot_secret(owner: str, repo: str, secret_name: str) -> dict | list:
        """Delete a Dependabot secret."""
        return gh_delete(f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}")
