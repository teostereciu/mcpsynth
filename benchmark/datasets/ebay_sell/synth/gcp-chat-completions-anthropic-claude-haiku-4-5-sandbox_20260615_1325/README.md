# eBay Sell API MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the eBay Sell API, enabling autonomous agents to interact with eBay's seller tools.

## Features

This server provides 120+ tools covering the major eBay Sell API namespaces:

- **Inventory API**: Create, read, update, delete inventory items, offers, and locations
- **Fulfillment API**: Manage orders, shipping fulfillments, refunds, and payment disputes
- **Account API**: Manage fulfillment, payment, return, and custom policies; handle sales tax and programs
- **Marketing API**: Create and manage advertising campaigns and ads
- **Finances API**: Access transactions, payouts, and financial summaries
- **Feed API**: Create and manage bulk upload/download tasks and schedules
- **Metadata API**: Retrieve category policies, item conditions, listing types, and currencies
- **Compliance API**: Check listing violations
- **Analytics API**: Access traffic reports and seller standards profiles
- **Stores API**: Manage store categories
- **Negotiation API**: Find eligible items and send offers to interested buyers
- **Recommendation API**: Get listing recommendations

## Installation

### Prerequisites

- Python 3.8+
- pip

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

The server will start and listen on stdio for MCP protocol messages.

## Authentication

The server uses OAuth 2.0 Refresh Token authentication. All requests are automatically authenticated using:

- **Token Endpoint**: `POST /identity/v1/oauth2/token`
- **Grant Type**: `refresh_token`
- **Refresh Token**: From `EBAY_REFRESH_TOKEN` environment variable

Tokens are cached and automatically refreshed when expired.

## Tool Categories

### Inventory Management
- `create_inventory_item` - Create or replace an inventory item
- `get_inventory_item` - Get a specific inventory item
- `get_inventory_items` - List all inventory items
- `delete_inventory_item` - Delete an inventory item
- `create_offer` - Create an offer for an inventory item
- `get_offer` - Get a specific offer
- `get_offers` - List offers
- `update_offer` - Update an offer
- `delete_offer` - Delete an offer
- `publish_offer` - Publish an offer to create a listing
- `withdraw_offer` - Withdraw an offer
- `get_listing_fees` - Get estimated fees for offers
- `bulk_create_offer` - Create multiple offers at once
- `bulk_publish_offer` - Publish multiple offers at once
- `bulk_update_price_quantity` - Update price/quantity for multiple offers

### Inventory Locations
- `create_inventory_location` - Create a new inventory location
- `get_inventory_location` - Get a specific location
- `get_inventory_locations` - List all locations
- `update_inventory_location` - Update a location
- `delete_inventory_location` - Delete a location
- `enable_inventory_location` - Enable a location
- `disable_inventory_location` - Disable a location

### Order Management
- `get_orders` - List orders with filtering
- `get_order` - Get a specific order
- `create_shipping_fulfillment` - Create a shipping fulfillment
- `get_shipping_fulfillments` - List fulfillments for an order
- `get_shipping_fulfillment` - Get a specific fulfillment
- `issue_refund` - Issue a refund
- `get_fulfillment_activities` - Get fulfillment activities

### Payment Disputes
- `get_payment_disputes` - List payment disputes
- `get_payment_dispute` - Get a specific dispute
- `accept_payment_dispute` - Accept a dispute
- `contest_payment_dispute` - Contest a dispute
- `add_evidence` - Add evidence to a dispute
- `update_evidence` - Update evidence in a dispute

### Business Policies
- `create_fulfillment_policy` - Create a fulfillment policy
- `get_fulfillment_policy` - Get a specific policy
- `get_fulfillment_policies` - List all fulfillment policies
- `get_fulfillment_policy_by_name` - Get policy by name
- `update_fulfillment_policy` - Update a policy
- `delete_fulfillment_policy` - Delete a policy
- `create_payment_policy` - Create a payment policy
- `get_payment_policy` - Get a specific policy
- `get_payment_policies` - List all payment policies
- `get_payment_policy_by_name` - Get policy by name
- `update_payment_policy` - Update a policy
- `delete_payment_policy` - Delete a policy
- `create_return_policy` - Create a return policy
- `get_return_policy` - Get a specific policy
- `get_return_policies` - List all return policies
- `get_return_policy_by_name` - Get policy by name
- `update_return_policy` - Update a policy
- `delete_return_policy` - Delete a policy
- `create_custom_policy` - Create a custom policy
- `get_custom_policy` - Get a specific policy
- `get_custom_policies` - List all custom policies
- `update_custom_policy` - Update a policy

### Sales Tax
- `get_sales_tax` - Get sales tax for a jurisdiction
- `get_sales_taxes` - List all sales tax configurations
- `create_or_replace_sales_tax` - Create or update sales tax
- `delete_sales_tax` - Delete sales tax configuration

### Account Management
- `get_privileges` - Get seller privileges
- `get_opted_in_programs` - List opted-in programs
- `opt_in_to_program` - Opt into a program
- `opt_out_of_program` - Opt out of a program
- `get_rate_tables` - Get shipping rate tables

### Marketing & Advertising
- `create_campaign` - Create an advertising campaign
- `get_campaign` - Get a specific campaign
- `get_campaigns` - List campaigns
- `update_campaign` - Update a campaign
- `delete_campaign` - Delete a campaign
- `clone_campaign` - Clone a campaign
- `create_ad` - Create an ad
- `get_ad` - Get a specific ad
- `get_ads` - List ads
- `update_ad` - Update an ad
- `delete_ad` - Delete an ad
- `update_bid` - Update bid for an ad
- `suggest_bids` - Get suggested bids
- `suggest_keywords` - Get suggested keywords
- `suggest_budget` - Get suggested budget

### Financial Management
- `get_transactions` - List transactions
- `get_transaction_summary` - Get transaction summary
- `get_payouts` - List payouts
- `get_payout` - Get a specific payout
- `get_payout_summary` - Get payout summary
- `get_seller_funds_summary` - Get funds summary
- `get_billing_activities` - List billing activities

### Feed Management
- `create_task` - Create a feed task
- `get_task` - Get a specific task
- `get_tasks` - List tasks
- `create_inventory_task` - Create an inventory task
- `get_inventory_task` - Get an inventory task
- `get_inventory_tasks` - List inventory tasks
- `create_order_task` - Create an order task
- `get_order_task` - Get an order task
- `get_order_tasks` - List order tasks
- `create_schedule` - Create a feed schedule
- `get_schedule` - Get a specific schedule
- `get_schedules` - List schedules
- `update_schedule` - Update a schedule
- `delete_schedule` - Delete a schedule

### Metadata
- `get_category_policies` - Get category policies
- `get_item_condition_policies` - Get item condition policies
- `get_listing_type_policies` - Get listing type policies
- `get_currencies` - Get supported currencies

### Compliance
- `get_listing_violations` - Get listing violations
- `get_listing_violations_summary` - Get violations summary

### Analytics
- `get_traffic_report` - Get traffic report
- `get_seller_standards_profile` - Get seller standards profile
- `find_seller_standards_profiles` - Find seller standards profiles

### Store Management
- `get_store` - Get store information
- `get_store_categories` - List store categories
- `add_store_category` - Add a store category
- `rename_store_category` - Rename a store category
- `delete_store_category` - Delete a store category
- `move_store_category` - Move a store category

### Negotiation
- `find_eligible_items` - Find items eligible for best offer
- `send_offer_to_interested_buyers` - Send offer to interested buyers

### Recommendations
- `find_listing_recommendations` - Get listing recommendations

## Error Handling

All tools return JSON-serializable results. Errors are returned as dictionaries with an "error" key:

```json
{
  "error": "Error message describing what went wrong"
}
```

Expected errors (like 404 Not Found, 400 Bad Request) are handled gracefully and returned as error dictionaries rather than raising exceptions.

## Configuration

### Environment Variables

- `EBAY_APP_ID` - Your eBay application ID (client ID)
- `EBAY_CERT_ID` - Your eBay application secret (client secret)
- `EBAY_REFRESH_TOKEN` - Your eBay refresh token for user authentication
- `EBAY_ENVIRONMENT` - Either `SANDBOX` (default) or `PRODUCTION`

### Base URLs

- Sandbox: `https://api.sandbox.ebay.com`
- Production: `https://api.ebay.com`

## Grounding

The `grounding.json` file provides a mapping of all tools to their source documentation, including:
- Tool name and description
- HTTP endpoint and method
- API namespace
- Source documentation file

This enables agents to understand the relationship between tools and their underlying API documentation.

## Development

### Adding New Tools

To add a new tool:

1. Create a function decorated with `@mcp.tool()`
2. Add parameters with type hints and docstrings
3. Call `make_request()` with the appropriate HTTP method and endpoint
4. Return JSON-serializable results
5. Add an entry to `grounding.json`

Example:

```python
@mcp.tool()
def my_new_tool(param1: str, param2: int = 10) -> dict:
    """Description of what this tool does."""
    return make_request("GET", "/api/endpoint", params={"param1": param1, "param2": param2})
```

## Testing

To test the server with a sample MCP client:

```bash
python server.py
```

Then use an MCP client to call tools. For example, using the official MCP client:

```python
from mcp.client.stdio import StdioMCPClient

async with StdioMCPClient("python server.py") as client:
    tools = await client.list_tools()
    result = await client.call_tool("get_inventory_items", {"limit": 10})
```

## API Documentation

For detailed information about each endpoint, refer to the official eBay Sell API documentation:
- https://developer.ebay.com/api-docs/sell/overview.html

## License

This implementation is provided as-is for use with the eBay Sell API.

## Support

For issues with the MCP server implementation, check the error messages returned by tools. For issues with the eBay API itself, refer to the official eBay developer documentation.
