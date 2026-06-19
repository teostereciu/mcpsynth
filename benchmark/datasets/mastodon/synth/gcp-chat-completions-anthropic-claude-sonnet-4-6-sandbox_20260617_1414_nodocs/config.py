"""
Shared configuration for the Mastodon MCP server.
Reads MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL from environment variables.
"""

import os

ACCESS_TOKEN: str = os.environ.get("MASTODON_ACCESS_TOKEN", "")
_base: str = os.environ.get("MASTODON_BASE_URL", "https://mastodon.social").rstrip("/")
BASE_URL: str = f"{_base}/api/v1"

HEADERS: dict = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Accept": "application/json",
}
