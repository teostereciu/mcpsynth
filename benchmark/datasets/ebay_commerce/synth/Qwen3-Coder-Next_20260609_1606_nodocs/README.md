# eBay Commerce API MCP Server

An MCP (Model Context Protocol) server providing comprehensive access to the eBay Commerce API for autonomous agents.

## Features

- **Taxonomy API**: Category trees, aspects, compatibility information
- **Catalog API**: Product search, product details, variants, EAN/ISBN/UPC lookup
- **Identity API**: User profile, account information, disputes
- **Media API**: Image/video/document uploads and management (separate base URL)
- **Notification API**: Webhook subscriptions for eBay events
- **Charity API**: Charity organization search, campaigns, donations
- **Translation API**: Text translation and language detection

## Prerequisites

- Python 3.8+
- eBay Developer Account with API credentials

## Setup

1. Set environment variables:
```bash
export EBAY_APP_ID="your_app_id"
export EBAY_CERT_ID="your_client_secret"
export EBAY_REFRESH_TOKEN="your_refresh_token"
export EBAY_ENVIRONMENT="SANDBOX"  # or "PRODUCTION"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python server.py
```

## Authentication

The server automatically manages OAuth2 tokens:

- **App tokens** (Client Credentials): For public APIs (Taxonomy, Catalog)
- **User tokens** (Refresh Token): For user-scoped APIs (Identity, Media, Notification, Charity, Translation)

## Usage with MCP Clients

The server exposes tools that can be called by any MCP-compatible client:

```python
from mcp.client.stdio import stdio_client

# Connect to the server and call tools
# Tools are automatically discovered via list_tools()
```

## API Reference

### Taxonomy API
- `get_taxonomy_categories()` - Get category tree for a country
- `get_taxonomy_category(category_id)` - Get category details
- `get_taxonomy_aspects(category_id)` - Get category attributes
- `get_taxonomy_compatibility(category_id)` - Get compatibility properties
- `search_taxonomy_categories(name)` - Search categories by name

### Catalog API
- `get_catalog_product(product_id)` - Get product details
- `search_catalog_products(query)` - Search catalog products
- `get_catalog_product_variants(product_id)` - Get product variants
- `get_catalog_eans(product_id)` - Get EANs for a product
- `get_catalog_isbns(product_id)` - Get ISBNs for a product
- `get_catalog_upcs(product_id)` - Get UPCs for a product

### Identity API
- `get_user_profile()` - Get user profile information
- `get_user_account()` - Get account information
- `get_user_disputes()` - Get user's disputes

### Media API
- `upload_media_from_url(media_type, content_type, content_url)` - Upload media by URL
- `get_media_status(media_id)` - Check upload status
- `create_media_repository(media_type, title)` - Create media folder
- `list_media_repositories()` - List media repositories

### Notification API
- `create_webhook_subscription(topic, callback_url)` - Create webhook
- `list_webhook_subscriptions()` - List all webhooks
- `get_webhook_subscription(subscription_id)` - Get webhook details
- `delete_webhook_subscription(subscription_id)` - Remove webhook
- `get_notification_events(subscription_id)` - Get delivered events

### Charity API
- `get_charity_organizations(organization_id, name, category)` - Search charities
- `get_charity_campaigns(organization_id)` - Get charity campaigns
- `create_charity_donation(organization_id, amount)` - Create donation

### Translation API
- `translate_text(text, source_language, target_language)` - Translate text
- `detect_language(text)` - Detect language of text

## Error Handling

All API errors are returned as JSON objects with an `error` key. The server handles HTTP errors gracefully and returns meaningful error messages.

## Development

The server is built with:
- FastMCP (Python)
- requests for HTTP calls
- OAuth2 for eBay authentication

## License

MIT
