"""eBay Commerce API MCP Server.

Exposes tools for all eBay Commerce namespaces:
  - Catalog (products)
  - Charity (charitable organizations)
  - Identity (user account info)
  - Media (images, videos, documents)
  - Notification (webhooks, subscriptions, destinations, topics)
  - Taxonomy (category trees, aspects, compatibility)
  - Translation (listing text translation)

Authentication:
  - App token (client_credentials): used for Catalog, Charity, Taxonomy, Translation, Notification
  - User token (refresh_token): used for Identity, Media

Environment variables required:
  EBAY_APP_ID        — application client ID
  EBAY_CERT_ID       — application client secret
  EBAY_REFRESH_TOKEN — user refresh token (for Identity and Media APIs)
  EBAY_ENVIRONMENT   — SANDBOX (default) or PRODUCTION
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("eBay Commerce API")

# Register all domain tool modules
from generated_tools import catalog, charity, identity, media, notification, taxonomy, translation

catalog.register(mcp)
charity.register(mcp)
identity.register(mcp)
media.register(mcp)
notification.register(mcp)
taxonomy.register(mcp)
translation.register(mcp)

if __name__ == "__main__":
    mcp.run()
