# eBay Commerce API MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the eBay Commerce API, enabling autonomous agents to interact with eBay's commerce services.

## Overview

This MCP server provides 46 tools across 7 eBay Commerce API namespaces:

- **Catalog API** (2 tools): Product search and retrieval
- **Charity API** (2 tools): Charitable organization lookup
- **Identity API** (1 tool): User account information
- **Media API** (11 tools): Image, video, and document management
- **Notification API** (20 tools): Webhook configuration and subscriptions
- **Taxonomy API** (9 tools): Category trees and item aspects
- **Translation API** (1 tool): Multi-language text translation

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
export EBAY_ENVIRONMENT="SANDBOX"  # or PRODUCTION
```

## Running the Server

```bash
python server.py
```

The server will start and listen on stdio for MCP protocol messages.

## Authentication

The server implements OAuth 2.0 with two token types:

### App Token (Client Credentials)
- Used for public APIs: Catalog, Charity, Taxonomy, Translation
- Obtained via client ID and secret
- Automatically cached for performance

### User Token (Refresh Token)
- Used for user-scoped APIs: Identity, Media, Notification
- Obtained via refresh token grant
- Automatically cached for performance

## API Tools

### Catalog API

#### `catalog_get_product(epid, marketplace_id="EBAY_US")`
Get detailed product information by eBay Product ID (ePID).

#### `catalog_search_products(query, category_id, gtin, mpn, aspects, field_groups, page_size, offset, marketplace_id)`
Search for products in the eBay catalog with optional filtering.

### Charity API

#### `charity_get_charity_org(charity_org_id)`
Get details about a specific charitable organization.

#### `charity_search_charity_orgs(query, registration_id, page_size, offset)`
Search for charitable organizations by name or registration ID.

### Identity API

#### `identity_get_user()`
Get public information about the authenticated user.

### Media API

#### `media_create_image_from_file(content_type, file_data)`
Upload an image from base64-encoded file data.

#### `media_create_image_from_url(image_url)`
Create an image by downloading from a URL.

#### `media_get_image(image_id)`
Get details about an image.

#### `media_create_video(title, description)`
Create a video resource.

#### `media_get_video(video_id)`
Get details about a video.

#### `media_upload_video(video_id, content_type, file_data)`
Upload video content.

#### `media_create_document(document_type, content_language)`
Create a document resource.

#### `media_get_document(document_id)`
Get details about a document.

#### `media_upload_document(document_id, content_type, file_data)`
Upload document content.

#### `media_create_document_from_url(document_url)`
Create a document by downloading from a URL.

### Notification API

#### `notification_get_config()`
Get the notification configuration.

#### `notification_update_config(delivery_url, verification_token, disabled_subscriptions)`
Update the notification configuration.

#### `notification_create_destination(destination_status, name, delivery_url, verification_token)`
Create a notification destination (webhook endpoint).

#### `notification_get_destination(destination_id)`
Get details about a notification destination.

#### `notification_get_destinations()`
Get all notification destinations.

#### `notification_update_destination(destination_id, destination_status, name, delivery_url, verification_token)`
Update a notification destination.

#### `notification_delete_destination(destination_id)`
Delete a notification destination.

#### `notification_get_public_key()`
Get the public key for verifying notification signatures.

#### `notification_create_subscription(destination_id, topic_ids)`
Create a notification subscription.

#### `notification_get_subscription(subscription_id)`
Get details about a subscription.

#### `notification_get_subscriptions()`
Get all subscriptions.

#### `notification_update_subscription(subscription_id, destination_id, topic_ids)`
Update a subscription.

#### `notification_delete_subscription(subscription_id)`
Delete a subscription.

#### `notification_enable_subscription(subscription_id)`
Enable a subscription.

#### `notification_disable_subscription(subscription_id)`
Disable a subscription.

#### `notification_test_subscription(subscription_id)`
Send a test notification to a subscription.

#### `notification_get_topics()`
Get all available notification topics.

#### `notification_get_topic(topic_id)`
Get details about a notification topic.

#### `notification_create_subscription_filter(subscription_id, filter_type, filter_value)`
Create a filter for a subscription.

#### `notification_get_subscription_filter(subscription_id, filter_id)`
Get details about a subscription filter.

#### `notification_delete_subscription_filter(subscription_id, filter_id)`
Delete a subscription filter.

### Taxonomy API

#### `taxonomy_get_default_category_tree_id(marketplace_id="EBAY_US")`
Get the default category tree ID for a marketplace.

#### `taxonomy_get_category_tree(category_tree_id)`
Get the category tree structure.

#### `taxonomy_get_category_subtree(category_tree_id, category_id)`
Get a subtree of categories.

#### `taxonomy_get_category_suggestions(category_tree_id, keywords)`
Get category suggestions based on keywords.

#### `taxonomy_get_item_aspects_for_category(category_tree_id, category_id)`
Get item aspects for a category.

#### `taxonomy_fetch_item_aspects(category_tree_id, category_id)`
Fetch item aspects for a category.

#### `taxonomy_get_compatibility_properties(category_tree_id, category_id)`
Get compatibility properties for a category.

#### `taxonomy_get_compatibility_property_values(category_tree_id, category_id, property_name)`
Get values for a compatibility property.

#### `taxonomy_get_expired_categories(category_tree_id)`
Get expired categories in a category tree.

### Translation API

#### `translation_translate(text, from_language, to_language)`
Translate text from one language to another.

## Configuration

### Environment Variables

- `EBAY_APP_ID`: Your eBay application client ID
- `EBAY_CERT_ID`: Your eBay application client secret
- `EBAY_REFRESH_TOKEN`: Your eBay user refresh token
- `EBAY_ENVIRONMENT`: Either `SANDBOX` (default) or `PRODUCTION`

### Base URLs

The server automatically selects the correct base URL based on the environment:

- **Sandbox**: `https://api.sandbox.ebay.com` and `https://apim.sandbox.ebay.com`
- **Production**: `https://api.ebay.com` and `https://apim.ebay.com`

## Error Handling

All tools return a dictionary with either:
- Success response: The API response data
- Error response: `{"error": "error_message", "details": "additional_details"}`

## Rate Limiting

The Media API has rate limits:
- 50 POST requests per 5 seconds per user

The server does not implement client-side rate limiting; it relies on the eBay API to enforce limits.

## Documentation

Each tool includes comprehensive docstrings with:
- Description of functionality
- Parameter documentation
- Return value documentation

For detailed API documentation, see the `grounding.json` file which maps each tool to its corresponding eBay API documentation.

## Files

- `server.py`: Main MCP server implementation
- `requirements.txt`: Python dependencies
- `grounding.json`: Tool-to-documentation mapping
- `README.md`: This file

## License

This implementation is provided as-is for use with the eBay Commerce API.

## Support

For issues with the eBay API, refer to the official eBay developer documentation at https://developer.ebay.com/
