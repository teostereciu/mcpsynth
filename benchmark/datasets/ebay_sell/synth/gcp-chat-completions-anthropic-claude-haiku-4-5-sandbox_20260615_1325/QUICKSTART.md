# Quick Start Guide - eBay Sell API MCP Server

## 5-Minute Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get Your eBay Credentials
1. Go to https://developer.ebay.com/
2. Create an application to get:
   - `EBAY_APP_ID` (Client ID)
   - `EBAY_CERT_ID` (Client Secret)
3. Generate a refresh token using the OAuth flow

### Step 3: Set Environment Variables
```bash
export EBAY_APP_ID="your_client_id"
export EBAY_CERT_ID="your_client_secret"
export EBAY_REFRESH_TOKEN="your_refresh_token"
export EBAY_ENVIRONMENT="SANDBOX"  # Use SANDBOX for testing
```

### Step 4: Run the Server
```bash
python server.py
```

You should see the server start and listen on stdio.

## Common Tasks

### List All Inventory Items
```python
# Using an MCP client
result = await client.call_tool("get_inventory_items", {"limit": 25})
```

### Create an Inventory Item
```python
result = await client.call_tool("create_inventory_item", {
    "sku": "MY-SKU-001",
    "marketplace_id": "EBAY_US",
    "availability": {
        "quantity": 100
    }
})
```

### Create and Publish an Offer
```python
# Step 1: Create the offer
offer = await client.call_tool("create_offer", {
    "sku": "MY-SKU-001",
    "marketplace_id": "EBAY_US",
    "format": "FIXED_PRICE",
    "pricing_summary": {
        "price": "29.99"
    }
})

# Step 2: Publish the offer
published = await client.call_tool("publish_offer", {
    "offer_id": offer["offerId"]
})
```

### Get Orders
```python
orders = await client.call_tool("get_orders", {
    "limit": 50,
    "offset": 0
})
```

### Create a Fulfillment Policy
```python
policy = await client.call_tool("create_fulfillment_policy", {
    "name": "My Fulfillment Policy",
    "marketplaceId": "EBAY_US",
    "fulfillmentCenterCode": "WAREHOUSE",
    "shipToLocations": {
        "regionIncluded": [
            {
                "regionName": "DOMESTIC"
            }
        ]
    },
    "shippingOptions": [
        {
            "optionType": "STANDARD",
            "costType": "FLAT_RATE",
            "shippingCost": {
                "currency": "USD",
                "value": "5.00"
            }
        }
    ]
})
```

### Get Transactions
```python
transactions = await client.call_tool("get_transactions", {
    "limit": 25,
    "offset": 0
})
```

### Create an Advertising Campaign
```python
campaign = await client.call_tool("create_campaign", {
    "name": "My Campaign",
    "marketplaceId": "EBAY_US",
    "fundingModel": "COST_PER_SALE",
    "campaignStatus": "ACTIVE",
    "dailyBudget": {
        "currency": "USD",
        "value": "50.00"
    }
})
```

## Troubleshooting

### "Failed to get OAuth token"
- Check that `EBAY_APP_ID`, `EBAY_CERT_ID`, and `EBAY_REFRESH_TOKEN` are set correctly
- Verify the refresh token hasn't expired
- Make sure you're using the correct environment (SANDBOX vs PRODUCTION)

### "Not found" Error
- Verify the resource ID (SKU, offer ID, order ID, etc.) is correct
- Check that the resource exists in your account
- Ensure you're using the correct marketplace ID

### "Bad Request" Error
- Check the request body format matches the API documentation
- Verify all required fields are provided
- Ensure field values are in the correct format (e.g., prices as strings)

### Connection Issues
- Verify your internet connection
- Check that the eBay API is accessible
- Try switching between SANDBOX and PRODUCTION to test connectivity

## Environment Variables Reference

| Variable | Required | Example | Notes |
|----------|----------|---------|-------|
| `EBAY_APP_ID` | Yes | `abc123def456` | Your application client ID |
| `EBAY_CERT_ID` | Yes | `xyz789uvw012` | Your application client secret |
| `EBAY_REFRESH_TOKEN` | Yes | `v^1.1#i^1#p^3#...` | User refresh token |
| `EBAY_ENVIRONMENT` | No | `SANDBOX` | Default: SANDBOX, use PRODUCTION for live |

## Tool Categories Quick Reference

### Inventory Management
- `create_inventory_item` - Create/update inventory
- `get_inventory_items` - List inventory
- `delete_inventory_item` - Delete inventory
- `create_offer` - Create an offer
- `publish_offer` - Publish offer to create listing
- `withdraw_offer` - End a listing

### Order Management
- `get_orders` - List orders
- `get_order` - Get order details
- `create_shipping_fulfillment` - Create fulfillment
- `issue_refund` - Issue refund

### Policies
- `create_fulfillment_policy` - Create fulfillment policy
- `create_payment_policy` - Create payment policy
- `create_return_policy` - Create return policy

### Marketing
- `create_campaign` - Create ad campaign
- `create_ad` - Create ad
- `update_bid` - Update ad bid

### Finances
- `get_transactions` - Get transactions
- `get_payouts` - Get payouts
- `get_seller_funds_summary` - Get funds summary

## API Documentation

For detailed information about each tool and its parameters, see:
- `README.md` - Full tool reference
- `grounding.json` - Tool-to-documentation mapping
- https://developer.ebay.com/api-docs/sell/overview.html - Official eBay API docs

## Next Steps

1. **Explore the Tools**: Use `list_tools()` to see all available tools
2. **Read the README**: Check `README.md` for detailed tool documentation
3. **Check grounding.json**: See which documentation file each tool comes from
4. **Test in Sandbox**: Always test in SANDBOX environment first
5. **Move to Production**: Once tested, switch to PRODUCTION environment

## Support

For issues:
1. Check the error message returned by the tool
2. Verify your environment variables are set correctly
3. Consult the official eBay API documentation
4. Check the tool's docstring for parameter requirements

## Example: Complete Workflow

```python
# 1. Create an inventory item
item = await client.call_tool("create_inventory_item", {
    "sku": "PRODUCT-001",
    "marketplace_id": "EBAY_US"
})

# 2. Create an offer
offer = await client.call_tool("create_offer", {
    "sku": "PRODUCT-001",
    "marketplace_id": "EBAY_US",
    "format": "FIXED_PRICE",
    "pricing_summary": {"price": "19.99"},
    "quantity_available": 10
})

# 3. Publish the offer
listing = await client.call_tool("publish_offer", {
    "offer_id": offer["offerId"]
})

# 4. Check orders
orders = await client.call_tool("get_orders", {"limit": 10})

# 5. Create fulfillment for an order
fulfillment = await client.call_tool("create_shipping_fulfillment", {
    "order_id": orders["orders"][0]["orderId"],
    "fulfillment_data": {
        "lineItems": [
            {
                "lineItemId": orders["orders"][0]["lineItems"][0]["lineItemId"],
                "quantity": 1
            }
        ],
        "shippingFulfillment": {
            "shippingCarrier": "USPS",
            "shippingServiceCode": "USPS_PRIORITY_MAIL"
        }
    }
})

print("Workflow complete!")
```

Happy selling! 🚀
