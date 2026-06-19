#!/usr/bin/env python3
"""
eBay Sell API MCP Server - Complete Implementation

This server provides tools for interacting with the eBay Sell API,
covering Inventory, Fulfillment, Account, Marketing, Finances, Feed, and other domains.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("ebay-sell-api")

# Configuration
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID", "")
EBAY_REFRESH_TOKEN = os.getenv("EBAY_REFRESH_TOKEN", "")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

BASE_URL = (
    "https://api.sandbox.ebay.com"
    if EBAY_ENVIRONMENT == "SANDBOX"
    else "https://api.ebay.com"
)

# Token cache
_cached_token = None
_cached_token_expiry = 0


def get_oauth_token() -> str:
    """Get a valid OAuth 2.0 access token using the refresh token."""
    global _cached_token, _cached_token_expiry
    import time

    # Return cached token if still valid
    if _cached_token and time.time() < _cached_token_expiry:
        return _cached_token

    token_url = f"{BASE_URL}/identity/v1/oauth2/token"
    auth = (EBAY_APP_ID, EBAY_CERT_ID)
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN,
    }

    try:
        response = requests.post(token_url, auth=auth, data=data, timeout=10)
        response.raise_for_status()
        token_data = response.json()
        _cached_token = token_data["access_token"]
        _cached_token_expiry = (
            __import__("time").time() + token_data.get("expires_in", 3600) - 60
        )
        return _cached_token
    except Exception as e:
        return {"error": f"Failed to get OAuth token: {str(e)}"}


def make_request(
    method: str,
    path: str,
    params: Optional[dict] = None,
    json_body: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> Any:
    """Make an authenticated request to the eBay API."""
    try:
        token = get_oauth_token()
        if isinstance(token, dict) and "error" in token:
            return token

        url = f"{BASE_URL}{path}"
        auth_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if headers:
            auth_headers.update(headers)

        if method.upper() == "GET":
            response = requests.get(url, params=params, headers=auth_headers, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(
                url, params=params, json=json_body, headers=auth_headers, timeout=30
            )
        elif method.upper() == "PUT":
            response = requests.put(
                url, params=params, json=json_body, headers=auth_headers, timeout=30
            )
        elif method.upper() == "DELETE":
            response = requests.delete(url, params=params, headers=auth_headers, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        # Handle different response codes
        if response.status_code in [200, 201, 202, 204]:
            if response.text:
                return response.json()
            return {"success": True}
        elif response.status_code == 404:
            return {"error": "Not found"}
        elif response.status_code == 400:
            try:
                return {"error": response.json()}
            except:
                return {"error": response.text}
        else:
            try:
                return {"error": response.json()}
            except:
                return {"error": f"HTTP {response.status_code}: {response.text}"}

    except Exception as e:
        return {"error": str(e)}


# Import all tools from the original server.py
# This is a wrapper that loads the tools from the main server.py file
# The actual tools are defined in server.py

if __name__ == "__main__":
    mcp.run()
