# eBay Commerce API MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the eBay Commerce API, enabling autonomous agents to interact with eBay's commerce services.

## Features

This MCP server provides tools for interacting with the following eBay Commerce APIs:

- **Catalog API**: Search and retrieve product information
- **Charity API**: Access charitable organization data
- **Identity API**: Retrieve authenticated user information
- **Media API**: Upload and manage images, videos, and documents
- **Notification API**: Configure and manage event subscriptions
- **Taxonomy API**: Access category trees and item aspects
- **Translation API**: Translate listing content

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export EBAY_APP_ID="your_app_id"
export EBAY_CERT_ID="your_cert_id"
export EBAY_REFRESH_TOKEN="your_refresh_token"
export EBAY_ENVIRONMENT="SANDBOX"  # or "PRODUCTION"
```

## Running the Server

```bash
python server.py
```

The server will start and listen on stdio for MCP protocol messages.

## Authentication

The server implements OAuth 2.0 authentication with two token types:

### App Token (Client Credentials)
Used for public APIs that don't require user identity:
- Taxonomy API
- Catalog API
- Charity API
- Translation API

### User Token (Refresh Token)
Used for user-scoped APIs:
- Identity API
- Media API
- Notification API

Tokens are automatically obtained and cached by the server.

## Available Tools

### Catalog API
- `search_products` - Search for products by keyword, category, GTIN, or MPN
- `get_product` - Get detailed product information by ePID

### Charity API
- `get_charity_org` - Get details about a charitable organization
- `search_charity_orgs` - Search for charitable organizations

### Identity API
- `get_user` - Get authenticated user's account information

### Media API
- `create_image_from_url` - Upload an image from a URL
- `get_image` - Get image details
- `create_video` - Create a video resource
- `get_video` - Get video details
- `upload_video` - Upload a video file
- `create_document_from_url` - Create a document from a URL
- `get_document` - Get document details
- `upload_document` - Upload a document file

### Notification API
- `get_notification_config` - Get notification configuration
- `update_notification_config` - Update notification configuration
- `create_destination` - Create a notification destination
- `get_destinations` - Get all destinations
- `get_destination` - Get a specific destination
- `update_destination` - Update a destination
- `delete_destination` - Delete a destination
- `get_topics` - Get available notification topics
- `get_topic` - Get topic details
- `create_subscription` - Create a subscription
- `get_subscriptions` - Get all subscriptions
- `get_subscription` - Get subscription details
- `update_subscription` - Update a subscription
- `delete_subscription` - Delete a subscription
- `enable_subscription` - Enable a subscription
- `disable_subscription` - Disable a subscription
- `test_subscription` - Send a test notification
- `get_subscription_filter` - Get a subscription filter
- `create_subscription_filter` - Create a subscription filter
- `delete_subscription_filter` - Delete a subscription filter
- `get_public_key` - Get public key for signature verification

### Taxonomy API
- `get_default_category_tree_id` - Get default category tree for a marketplace
- `get_category_tree` - Get complete category tree
- `get_category_subtree` - Get a category subtree
- `get_category_suggestions` - Get category suggestions based on keywords
- `get_item_aspects_for_category` - Get item aspects for a category
- `fetch_item_aspects` - Fetch all item aspects for a marketplace
- `get_compatibility_properties` - Get vehicle compatibility properties
- `get_compatibility_property_values` - Get compatibility property values
- `get_expired_categories` - Get expired categories

### Translation API
- `translate_text` - Translate text between languages

## Configuration

### Environment Variables

- `EBAY_APP_ID` - Your eBay application ID (client ID)
- `EBAY_CERT_ID` - Your eBay application secret (client secret)
- `EBAY_REFRESH_TOKEN` - Your eBay refresh token for user-scoped APIs
- `EBAY_ENVIRONMENT` - Either "SANDBOX" (default) or "PRODUCTION"

### Base URLs

The server automatically selects the correct base URLs based on the environment:

- **Sandbox**: 
  - Standard APIs: `https://api.sandbox.ebay.com`
  - Media API: `https://apim.sandbox.ebay.com`
  - Identity API: `https://apiz.sandbox.ebay.com`

- **Production**:
  - Standard APIs: `https://api.ebay.com`
  - Media API: `https://apim.ebay.com`
  - Identity API: `https://apiz.ebay.com`

## Grounding

The `grounding.json` file maps each tool to its corresponding API documentation file, enabling the MCP server to provide context-aware assistance to autonomous agents.

## Error Handling

The server returns errors in the following format:
```json
{
  "error": "Error message describing what went wrong"
}
```

Common error scenarios:
- Authentication failures (invalid credentials)
- API errors (4xx/5xx responses)
- File not found (for file upload operations)
- Network errors

## Rate Limiting

Be aware of eBay API rate limits:
- Media API POST methods: 50 requests per 5 seconds per user
- Other APIs: Refer to eBay API documentation

## Development

### Adding New Tools

To add a new tool:

1. Create a function decorated with `@mcp.tool()`
2. Add appropriate docstring
3. Implement the tool logic using `make_request()`
4. Update `grounding.json` with the tool mapping

Example:
```python
@mcp.tool()
def my_new_tool(param1: str, param2: int = 10) -> Dict[str, Any]:
    """Description of what this tool does."""
    url = f"{BASE_URL}/api/endpoint"
    return make_request("GET", url, token_type="app", params={"param1": param1})
```

## License

This implementation is provided as-is for use with the eBay Commerce API.

## Support

For issues or questions:
1. Check the eBay API documentation
2. Review the grounding.json file for endpoint mappings
3. Consult the error messages returned by the API
