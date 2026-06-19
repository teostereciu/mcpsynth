# eBay Buy API MCP Server

A comprehensive Model Context Protocol (MCP) server for the eBay Buy API, enabling autonomous agents to search, browse, and purchase items on eBay.

## Features

This server provides tools across all major eBay Buy API namespaces:

### Browse API (7 tools)
- **search_items**: Search for items by keyword or category with filtering and sorting
- **search_items_by_image**: Find items using image-based search
- **get_item**: Get detailed information about a specific item
- **get_item_by_legacy_id**: Retrieve items using legacy eBay item IDs
- **get_items**: Get details for multiple items in a single request
- **get_items_by_item_group**: Get all variations of an item
- **check_item_compatibility**: Check if an item is compatible with specified parts/vehicles

### Deal API (4 tools)
- **get_deal_items**: Get current deal items with optional category filtering
- **get_event_items**: Get items associated with specific events
- **get_event**: Get details about a specific event
- **get_events**: Get all current events

### Feed API (4 tools)
- **get_item_feed**: Download daily or weekly item feed files
- **get_item_group_feed**: Download item group feed files
- **get_item_priority_feed**: Download item priority feed files
- **get_item_snapshot_feed**: Download item snapshot feed files

### Marketing API (1 tool)
- **get_merchandised_products**: Get merchandised products for a category

### Offer API (2 tools)
- **get_bidding**: Get bidding information for auction items
- **place_proxy_bid**: Place a proxy bid on an auction item

### Order API - Guest Checkout (7 tools)
- **initiate_guest_checkout_session**: Start a guest checkout session
- **get_guest_checkout_session**: Get checkout session details
- **apply_guest_coupon**: Apply a coupon code
- **remove_guest_coupon**: Remove a coupon
- **update_guest_quantity**: Update item quantities in cart
- **update_guest_shipping_address**: Update shipping address
- **update_guest_shipping_option**: Select a shipping option
- **get_guest_purchase_order**: Get purchase order details

**Total: 28 tools** covering the most important operations across all Buy API namespaces.

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Set the following environment variables:

```bash
export EBAY_APP_ID="your_app_id"
export EBAY_CERT_ID="your_app_secret"
export EBAY_ENVIRONMENT="SANDBOX"  # or "PRODUCTION"
```

### Getting eBay API Credentials

1. Go to [eBay Developer Program](https://developer.ebay.com/)
2. Create an application to get your App ID (Client ID) and Cert ID (Client Secret)
3. Use the Sandbox environment for testing

## Running the Server

```bash
python server.py
```

The server will start and listen on stdio, ready to accept MCP protocol messages.

## Usage Examples

### Search for Items
```python
# Search for laptops under $500
search_items(
    q="laptop",
    filter="price:[0..500]",
    limit=20
)
```

### Get Item Details
```python
# Get comprehensive details about an item
get_item(
    item_id="v1|123456789|0",
    fieldgroups="PRODUCT,ADDITIONAL_SELLER_DETAILS"
)
```

### Browse Deals
```python
# Get current deals
get_deal_items(limit=50)

# Get items for a specific event
get_event_items(event_ids="event123", limit=20)
```

### Guest Checkout Workflow
```python
# 1. Initiate checkout
session = initiate_guest_checkout_session(
    items_payload='{"items": [{"item_id": "v1|123|0", "quantity": 1}]}'
)
session_id = session["checkout_session_id"]

# 2. Update shipping address
update_guest_shipping_address(
    checkout_session_id=session_id,
    address_payload='{"address": {"address_line1": "123 Main St", "city": "San Jose", "state_or_province": "CA", "postal_code": "95131", "country": "US"}}'
)

# 3. Select shipping option
update_guest_shipping_option(
    checkout_session_id=session_id,
    shipping_option_id="STANDARD_SHIPPING"
)

# 4. Apply coupon if available
apply_guest_coupon(
    checkout_session_id=session_id,
    coupon_code="SAVE10"
)

# 5. Get final order details
get_guest_checkout_session(checkout_session_id=session_id)
```

### Bidding on Auctions
```python
# Get bidding info for an item
bidding_info = get_bidding(item_id="v1|123456789|0")

# Place a proxy bid
place_proxy_bid(
    item_id="v1|123456789|0",
    bid_amount="150.00"
)
```

## API Response Format

All tools return JSON-serializable responses:

### Success Response
```json
{
  "itemSummaries": [
    {
      "itemId": "v1|123456789|0",
      "title": "Item Title",
      "price": {
        "value": "99.99",
        "currency": "USD"
      },
      "condition": "NEW",
      "seller": {
        "username": "seller_name",
        "feedbackScore": 1000
      }
    }
  ]
}
```

### Error Response
```json
{
  "error": "Error message or API error details"
}
```

## Error Handling

The server handles errors gracefully:
- **Authentication errors**: Returns error if credentials are invalid
- **API errors**: Returns the eBay API error response
- **Network errors**: Returns connection error details
- **Invalid parameters**: Returns validation error messages

All errors are returned as JSON objects with an `error` field, never as exceptions.

## Supported Marketplaces

The server is configured for the US marketplace (EBAY_US) by default. To use other marketplaces, modify the `X-EBAY-C-MARKETPLACE-ID` header in the `make_request` function.

Supported marketplace IDs:
- EBAY_US (United States)
- EBAY_GB (United Kingdom)
- EBAY_DE (Germany)
- EBAY_FR (France)
- EBAY_IT (Italy)
- EBAY_ES (Spain)
- EBAY_CA (Canada)
- EBAY_AU (Australia)
- And others...

## Rate Limiting

The eBay API has rate limits. The server does not implement rate limiting internally, but you should be aware of:
- Standard rate limits vary by API and endpoint
- Implement exponential backoff in your client if needed
- Monitor API usage in your eBay developer dashboard

## Limitations

- **Feed files**: Feed API returns metadata about feed files; actual file downloads require additional handling
- **Marketplace**: Currently hardcoded to EBAY_US; modify for other marketplaces
- **Authentication**: Uses OAuth 2.0 Client Credentials flow (application token)
- **Guest checkout**: Limited to guest checkout flow; registered user checkout not supported

## Architecture

### Token Management
- Tokens are cached in memory with automatic refresh
- Refresh happens 60 seconds before expiry to avoid race conditions
- Each request checks token validity before making API calls

### Request Flow
1. Tool receives parameters
2. Validates and formats parameters
3. Gets/refreshes access token
4. Makes authenticated HTTP request to eBay API
5. Handles response or error
6. Returns JSON-serializable result

### Error Handling Strategy
- Expected errors (404, validation) return error dict
- Unexpected errors are caught and returned as error dicts
- No unhandled exceptions propagate to MCP protocol

## Development

### Adding New Tools

To add a new tool:

1. Create a function decorated with `@server.tool()`
2. Add docstring with description and args
3. Use `make_request()` helper for API calls
4. Return JSON-serializable dict

Example:
```python
@server.tool()
def my_new_tool(param1: str, param2: int = 10) -> dict:
    """
    Brief description.
    
    Args:
        param1: Description
        param2: Description
    
    Returns:
        Result description
    """
    params = {"param1": param1, "param2": param2}
    return make_request("GET", "/api/v1/endpoint", params=params)
```

### Testing

Test with curl or any HTTP client that supports MCP:

```bash
# Start the server
python server.py

# In another terminal, test a tool
# (MCP protocol details depend on your client)
```

## Documentation

For detailed API documentation, see:
- [eBay Buy API Documentation](https://developer.ebay.com/api-docs/buy/overview)
- [Browse API](https://developer.ebay.com/api-docs/buy/browse)
- [Deal API](https://developer.ebay.com/api-docs/buy/deal)
- [Feed API](https://developer.ebay.com/api-docs/buy/feed)
- [Marketing API](https://developer.ebay.com/api-docs/buy/marketing)
- [Offer API](https://developer.ebay.com/api-docs/buy/offer)
- [Order API](https://developer.ebay.com/api-docs/buy/order)

## License

This MCP server is provided as-is for use with the eBay Buy API.

## Support

For issues or questions:
1. Check the eBay API documentation
2. Verify your credentials and environment
3. Check API rate limits and quotas
4. Review error messages in the response

## Changelog

### Version 1.0.0
- Initial release
- 28 tools across 6 API namespaces
- Full guest checkout workflow support
- Browse, search, and deal functionality
- Bidding and offer support
- Feed file access
