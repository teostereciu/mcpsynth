"""eBay Commerce Identity API tools."""
from mcp.server.fastmcp import FastMCP
from .auth import get_user_token, get_base_url

def register(mcp: FastMCP):

    @mcp.tool()
    def get_user() -> dict:
        """Retrieve the account profile information for the authenticated eBay user.

        Returns account type (BUSINESS or INDIVIDUAL), user ID, username, status,
        registration marketplace, and account details (business or individual).
        Requires a valid EBAY_REFRESH_TOKEN.
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        # Identity API uses apiz subdomain
        env = __import__("os").environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
        if env == "PRODUCTION":
            url = "https://apiz.ebay.com/commerce/identity/v1/user/"
        else:
            url = "https://apiz.sandbox.ebay.com/commerce/identity/v1/user/"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
        }
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
