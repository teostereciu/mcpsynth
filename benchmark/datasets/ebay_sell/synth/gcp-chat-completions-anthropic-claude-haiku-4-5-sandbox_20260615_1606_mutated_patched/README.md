# eBay Sell API MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the eBay Sell API, enabling autonomous agents to manage eBay seller operations including inventory, orders, fulfillment, marketing campaigns, and financial transactions.

## Features

- **Inventory Management**: Create, read, update, and delete inventory items, offers, and locations
- **Order Fulfillment**: Manage orders, shipping fulfillments, and payment disputes
- **Account Policies**: Configure fulfillment, payment, and return policies
- **Marketing**: Create and manage advertising campaigns and ads
- **Financial Operations**: Access payouts, transactions, and financial summaries
- **Feed Management**: Create and manage bulk upload/download tasks
- **Metadata & Compliance**: Access marketplace policies and listing violations
- **Analytics**: Track seller performance and standards
- **Logistics**: Create shipping quotes and manage shipments

## Installation

### Prerequisites

- Python 3.8+
- eBay Sell API credentials:
  - `EBAY_APP_ID` (application client ID)
  - `EBAY_CERT_ID` (application client secret)
  - `EBAY_REFRESH_TOKEN` (user refresh token)

### Setup

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set environment variables:
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

The server will start and listen on stdio, ready to receive MCP protocol messages.

## API Coverage

### Inventory API (40+ tools)
- Offers: create, read, update, delete, publish, withdraw
- Inventory Items: create, read, update, delete
- Inventory Locations: create, read, update, delete, enable, disable
- Bulk Operations: bulk create offers, bulk publish, bulk update prices
- Item Groups: create, read, delete multi-variation listings
- Product Compatibility: manage compatibility information
- SKU Location Mapping: map SKUs to inventory locations
- Listing Fees: estimate fees for offers

### Fulfillment API (15+ tools)
- Orders: retrieve orders with optional tax breakdown
- Shipping Fulfillments: create and manage shipments
- Payment Disputes: retrieve, accept, contest, and add evidence
- Refunds: issue refunds for orders or line items

### Account API (30+ tools)
- Fulfillment Policies: create, read, update, delete
- Payment Policies: create, read, update, delete
- Return Policies: create, read, update, delete
- Custom Policies: create, read, update, delete
- Sales Tax: manage sales tax by jurisdiction
- Programs: opt in/out of seller programs
- Privileges: check seller privileges
- Rate Tables: access seller rate tables
- Subscription: check subscription status
- Payments Program: manage payments program enrollment

### Marketing API (25+ tools)
- Campaigns: create, read, update, delete, clone
- Ads: create, read, update, delete
- Ad Groups: create, read, update
- Bulk Ad Operations: bulk create, delete, and update ads
- Bid Management: suggest bids and update bid amounts
- Keywords: suggest keywords for campaigns
- Budget: get budget suggestions

### Finances API (6+ tools)
- Payouts: retrieve payout summaries and individual payouts
- Transactions: retrieve financial transactions
- Seller Funds: access seller funds summary

### Feed API (10+ tools)
- Inventory Tasks: create and manage inventory feed tasks
- Order Tasks: create and manage order feed tasks
- Schedules: create, read, update, delete feed schedules
- Schedule Templates: access available schedule templates

### Metadata API (8+ tools)
- Category Policies: get policies for specific categories
- Currencies: get supported currencies by marketplace
- Item Conditions: get item condition policies
- Listing Types: get listing type policies
- Listing Structure: get listing structure policies
- Hazardous Materials: get hazardous materials labels
- Automotive Compatibility: get automotive parts compatibility policies

### Compliance API (2+ tools)
- Listing Violations: get violation summaries and details

### Analytics API (3+ tools)
- Traffic Reports: get traffic data for specific dates
- Seller Standards: get seller standards profile
- Customer Service Metrics: get customer service metrics

### Recommendation API (1+ tools)
- Listing Recommendations: get recommendations for listings

### Negotiation API (2+ tools)
- Eligible Items: find items eligible for best offer
- Send Offers: send offers to interested buyers

### Stores API (5+ tools)
- Store Information: get store details
- Store Categories: create, read, delete, rename categories

### Logistics API (6+ tools)
- Shipping Quotes: create and retrieve shipping quotes
- Shipments: create from quotes, retrieve, cancel
- Labels: download shipping labels

## Tool Categories

All tools are organized by API domain and follow consistent naming conventions:

- **Create/Update operations**: `create_*`, `update_*`
- **Read operations**: `get_*`, `find_*`
- **Delete operations**: `delete_*`
- **Action operations**: `publish_*`, `withdraw_*`, `enable_*`, `disable_*`

## Authentication

The server uses OAuth 2.0 Refresh Token authentication. The refresh token is automatically exchanged for an access token on each request, with token caching to minimize API calls.

### Token Management

- Tokens are cached and reused until expiration
- Automatic token refresh when expired
- No manual token management required

## Error Handling

All tools return JSON-serializable results:
- **Success**: Returns the API response as a dictionary
- **Error**: Returns `{"error": "error message"}` dictionary

Expected errors (4xx, 5xx responses) are caught and returned as error dictionaries rather than raising exceptions, allowing agents to handle errors gracefully.

## Configuration

### Environment Variables

- `EBAY_APP_ID`: Your eBay application client ID
- `EBAY_CERT_ID`: Your eBay application client secret
- `EBAY_REFRESH_TOKEN`: Your eBay user refresh token
- `EBAY_ENVIRONMENT`: Either `SANDBOX` (default) or `PRODUCTION`

### Base URLs

- Sandbox: `https://api.sandbox.ebay.com`
- Production: `https://api.ebay.com`

## Grounding

The `grounding.json` file maps each tool to its corresponding API documentation file in the `docs/` directory, enabling agents to access detailed endpoint information.

## Example Usage

```python
# Create an inventory item
create_inventory_item(
    sku="SKU-12345",
    title="Sample Product",
    condition="NEW",
    brand="Sample Brand"
)

# Create an offer
create_offer(
    seller_sku="SKU-12345",
    marketplace_id="EBAY_US",
    format="FIXED_PRICE",
    price=29.99,
    currency_code="USD",
    available_quantity=10
)

# Publish the offer
publish_offer(offer_id="offer-123")

# Get orders
get_orders(
    order_creation_date_range_from="2024-01-01T00:00:00Z",
    order_creation_date_range_to="2024-01-31T23:59:59Z"
)

# Create a campaign
create_campaign(
    campaign_name="Summer Sale",
    marketplace_id="EBAY_US",
    budget_allocation=100.00
)
```

## Limitations

- Bulk operations support up to 25 items per request
- Some endpoints may have rate limits
- File upload/download operations are not fully implemented
- Some advanced filtering options may not be exposed

## Support

For issues or questions:
1. Check the eBay Sell API documentation in the `docs/` directory
2. Review the tool docstrings for parameter details
3. Check the grounding.json for endpoint mappings

## License

This MCP server is provided as-is for use with the eBay Sell API.
