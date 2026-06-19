"""Wrapper to launch the zulipchat-mcp reference implementation.

Source: https://github.com/akougkas/zulipchat-mcp (v0.6.2)
A community-maintained, professionally written Zulip MCP server.
Used as a human-quality reference implementation for benchmark comparison.

Credentials read from env: ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE
"""
from zulipchat_mcp.server import main

main()
