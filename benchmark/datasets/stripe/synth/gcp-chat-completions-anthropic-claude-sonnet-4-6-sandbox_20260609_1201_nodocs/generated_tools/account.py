"""
Stripe Account (own account) tools.
Endpoints covered:
  GET    /v1/account
  POST   /v1/account_links
  POST   /v1/account_sessions
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def get_own_account() -> dict:
        """Retrieve the currently authenticated Stripe account."""
        return stripe_request("GET", "/v1/account")

    @mcp.tool()
    def create_account_link(
        account: str,
        refresh_url: str,
        return_url: str,
        type: str,
        collect: str = None,
    ) -> dict:
        """
        Create an Account Link for onboarding a connected account.
        type: account_onboarding | account_update
        collect: currently_due | eventually_due
        """
        data = {
            "account": account,
            "refresh_url": refresh_url,
            "return_url": return_url,
            "type": type,
        }
        if collect:
            data["collect"] = collect
        return stripe_request("POST", "/v1/account_links", data=data)

    @mcp.tool()
    def create_account_session(
        account: str,
        components: dict,
    ) -> dict:
        """
        Create an Account Session for embedded Connect components.
        components: dict of component names to their config, e.g.
          {"account_onboarding": {"enabled": True}}
        """
        data = {"account": account}
        for component, config in components.items():
            if isinstance(config, dict):
                for k, v in config.items():
                    data[f"components[{component}][{k}]"] = str(v).lower() if isinstance(v, bool) else v
            else:
                data[f"components[{component}]"] = str(config).lower()
        return stripe_request("POST", "/v1/account_sessions", data=data)
