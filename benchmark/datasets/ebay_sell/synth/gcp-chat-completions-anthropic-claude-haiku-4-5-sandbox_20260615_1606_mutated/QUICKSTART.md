# Quick Start Guide - eBay Sell API MCP Server

## 5-Minute Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Environment Variables
```bash
export EBAY_APP_ID="your_app_id_here"
export EBAY_CERT_ID="your_cert_id_here"
export EBAY_REFRESH_TOKEN="your_refresh_token_here"
export EBAY_ENVIRONMENT="SANDBOX"  # Use SANDBOX for testing, PRODUCTION for live
```

### Step 3: Start the Server
```bash
python server.py
```

The server is now running and ready to accept MCP protocol requests!

## Common Tasks

### Create an Inventory Item
```python
create_inventory_item(
    sku="MY-SKU-001",
    title="My Product",
    condition="NEW",
    brand="My Brand"
)
```

### Create and Publish an Offer
```python
# Step 1: Create the offer
offer_response = create_offer(
    seller_sku="MY-SKU-001",
    marketplace_id="EBAY_US",
    format="FIXED_PRICE",
    price=29.99,
    currency_code="USD",
    available_quantity=10
)
offer_id = offer_response.get("offerId")

# Step 2: Publish the offer
publish_offer(offer_id=offer_id)
```

### Retrieve Orders
```python
orders = get_orders(
    order_creation_date_range_from="2024-01-01T00:00:00Z",
    order_creation_date_range_to="2024-01-31T23:59:59Z"
)
```

### Create a Marketing Campaign
```python
campaign = create_campaign(
    campaign_name="Summer Sale",
    marketplace_id="EBAY_US",
    budget_allocation=100.00
)
campaign_id = campaign.get("campaignId")

# Add an ad to the campaign
create_ad(
    campaign_id=campaign_id,
    listing_id="listing-123",
    bid_amount=0.50
)
```

### Check Seller Privileges
```python
privileges = get_privileges()
```

### Get Financial Summary
```python
payout_summary = get_payout_summary()
transactions = get_transactions()
```

## Available Tool Categories

| Category | Tools | Purpose |
|----------|-------|---------|
| Inventory | 40+ | Manage items, offers, locations |
| Fulfillment | 15+ | Manage orders, shipments, disputes |
| Account | 30+ | Configure policies, programs, taxes |
| Marketing | 25+ | Create campaigns, manage ads |
| Finances | 6+ | Track payouts and transactions |
| Feed | 10+ | Bulk upload/download operations |
| Metadata | 8+ | Access marketplace information |
| Compliance | 2+ | Check listing violations |
| Analytics | 3+ | View performance metrics |
| Logistics | 6+ | Manage shipping |
| Stores | 5+ | Manage store categories |
| Negotiation | 2+ | Send offers to buyers |
| Recommendation | 1+ | Get listing recommendations |

## Error Handling

All tools return JSON responses. Check for errors:

```python
response = create_offer(...)
if "error" in response:
    print(f"Error: {response['error']}")
else:
    print(f"Success: {response}")
```

## Environment Variables Reference

| Variable | Required | Example | Notes |
|----------|----------|---------|-------|
| EBAY_APP_ID | Yes | abc123def456 | Your eBay application client ID |
| EBAY_CERT_ID | Yes | xyz789uvw012 | Your eBay application client secret |
| EBAY_REFRESH_TOKEN | Yes | AgEBBQA... | Your eBay user refresh token |
| EBAY_ENVIRONMENT | No | SANDBOX | SANDBOX (default) or PRODUCTION |

## Getting eBay Credentials

1. Go to [eBay Developer Portal](https://developer.ebay.com/)
2. Create an application
3. Get your Client ID (App ID) and Client Secret (Cert ID)
4. Generate a refresh token using the OAuth flow
5. Set the environment variables

## Testing Your Setup

```bash
# Test that the server starts
python server.py &

# In another terminal, verify it's running
curl http://localhost:8000/tools  # If using HTTP transport
```

## Common Issues

### "Error getting access token"
- Check that EBAY_APP_ID and EBAY_CERT_ID are correct
- Verify EBAY_REFRESH_TOKEN is valid and not expired
- Check that EBAY_ENVIRONMENT is set correctly

### "Not found" errors
- Verify the resource ID (offer_id, order_id, etc.) exists
- Check that you're using the correct marketplace_id
- Ensure the resource belongs to your seller account

### "Unauthorized" errors
- Refresh token may have expired
- Check that your eBay account has the required permissions
- Verify you're using the correct environment (SANDBOX vs PRODUCTION)

## Next Steps

1. Read the full [README.md](README.md) for detailed documentation
2. Check [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for complete API coverage
3. Review the `docs/` directory for specific endpoint documentation
4. Check `grounding.json` for tool-to-endpoint mappings

## Support

For detailed information about specific tools:
1. Check the tool's docstring in server.py
2. Look up the endpoint in docs/
3. Review the grounding.json mapping

## Example: Complete Workflow

```python
# 1. Create inventory item
item = create_inventory_item(
    sku="WORKFLOW-001",
    title="Test Product",
    condition="NEW"
)

# 2. Create offer
offer = create_offer(
    seller_sku="WORKFLOW-001",
    marketplace_id="EBAY_US",
    format="FIXED_PRICE",
    price=49.99,
    available_quantity=5
)

# 3. Publish offer
publish_response = publish_offer(offer_id=offer["offerId"])

# 4. Check orders
orders = get_orders()

# 5. Create fulfillment for first order
if orders.get("orders"):
    order_id = orders["orders"][0]["orderId"]
    fulfillment = create_shipping_fulfillment(
        order_id=order_id,
        line_items=[{"lineItemId": "item-1"}],
        carrier_code="USPS",
        tracking_number="1234567890"
    )

# 6. Check financial summary
payout = get_payout_summary()
```

Happy selling! 🚀
