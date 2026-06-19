"""eBay Commerce Charity API tools."""
from mcp.server.fastmcp import FastMCP
from .auth import get_app_token, get_base_url

def register(mcp: FastMCP):

    @mcp.tool()
    def get_charity_org(charity_org_id: str, marketplace_id: str = "EBAY_US") -> dict:
        """Retrieve detailed information about a specific charitable organization by its ID.

        Args:
            charity_org_id: The unique ID of the charitable organization.
            marketplace_id: eBay marketplace ID. Valid values: EBAY_US, EBAY_GB.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/charity/v1/charity_org/{charity_org_id}"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        }
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_charity_orgs(
        q: str = "",
        registration_ids: str = "",
        limit: str = "20",
        offset: str = "0",
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Search for charitable organizations by keyword or registration IDs.

        Args:
            q: Query string matching name, mission statement, or description.
            registration_ids: Comma-separated list of registration IDs (do not combine with q).
            limit: Number of results per page (1-100, default 20).
            offset: Number of results to skip (default 0).
            marketplace_id: eBay marketplace ID. Valid values: EBAY_US, EBAY_GB.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/charity/v1/charity_org"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        }
        params = {}
        if q:
            params["q"] = q
        if registration_ids:
            params["registration_ids"] = registration_ids
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
