# eBay Buy API MCP Server

A comprehensive Model Context Protocol (MCP) server providing access to the eBay Buy API. This server exposes 27 tools covering all major eBay Buy API namespaces: Browse, Deal, Feed, Marketing, Offer, and Order.

## Features

- **27 Tools** covering all major eBay Buy API operations
- **Browse API**: Item search, details, compatibility checking
- **Deal API**: Deals, events, and promotions
- **Feed API**: Item feeds, snapshots, and priority feeds
- **Marketing API**: Merchandised products
- **Offer API**: Bidding and proxy bids
- **Order API**: Guest checkout workflow
- **OAuth 2.0 Authentication**: Automatic token management with caching
- **Error Handling**: Graceful error responses without exceptions
- **JSON Serialization**: All responses are JSON-serializable

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Set the following environment variables:

```bash
export EBAY_APP_ID="your_app_id"
export EBAY_CERT_ID="your_cert_id"
export EBAY_ENVIRONMENT="SANDBOX"  # or "PRODUCTION"
```

## Running the Server

```bash
python server.py
```

The server runs over stdio and is compatible with any MCP client.

## Tools Overview

### Browse API (7 tools)
- `browse_get_item` - Get item details
- `browse_get_items` - Get multiple items
- `browse_get_item_by_legacy_id` - Convert legacy item IDs
- `browse_get_items_by_item_group` - Get items in a group
- `browse_check_compatibility` - Check product compatibility
- `browse_search_items` - Search by keyword/category
- `browse_search_by_image` - Search by image

### Deal API (4 tools)
- `deal_get_deal_items` - Get current deals
- `deal_get_events` - Get deal events
- `deal_get_event` - Get event details
- `deal_get_event_items` - Get items in events

### Feed API (4 tools)
- `feed_get_item_feed` - Get item feed
- `feed_get_item_group_feed` - Get item group feed
- `feed_get_item_snapshot_feed` - Get item changes
- `feed_get_item_priority_feed` - Get priority items

### Marketing API (1 tool)
- `marketing_get_merchandised_products` - Get featured products

### Offer API (2 tools)
- `offer_get_bidding` - Get auction bidding info
- `offer_place_proxy_bid` - Place a proxy bid

### Order API (7 tools)
- `order_initiate_guest_checkout` - Start checkout
- `order_get_guest_checkout_session` - Get checkout details
- `order_update_guest_quantity` - Update item quantity
- `order_update_guest_shipping_address` - Update address
- `order_update_guest_shipping_option` - Update shipping
- `order_apply_guest_coupon` - Apply coupon
- `order_remove_guest_coupon` - Remove coupon
- `order_get_guest_purchase_order` - Get order details

## Architecture

### Authentication
- Uses OAuth 2.0 Client Credentials flow
- Automatic token caching with expiration tracking
- Tokens refreshed 60 seconds before expiration

### Request Handling
- Unified `make_request()` function for all API calls
- Automatic JSON serialization/deserialization
- Support for both standard and APIX endpoints
- Comprehensive error handling

### Error Handling
- Returns error dicts instead of raising exceptions
- Graceful handling of network errors
- Proper HTTP status code propagation

## Documentation

See `grounding.json` for mapping of tools to API documentation files.

## Requirements

- Python 3.8+
- fastmcp 3.2.4
- requests 2.32.3

## License

MIT
