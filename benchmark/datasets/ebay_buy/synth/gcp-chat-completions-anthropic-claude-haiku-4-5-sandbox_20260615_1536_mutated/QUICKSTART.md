# Quick Start Guide

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Set Environment Variables

```bash
export EBAY_APP_ID="your_application_id"
export EBAY_CERT_ID="your_application_secret"
export EBAY_ENVIRONMENT="SANDBOX"  # Use PRODUCTION for live API
```

## 3. Run the Server

```bash
python server.py
```

The server will start and listen on stdio, ready to accept MCP protocol messages.

## 4. Common Use Cases

### Search for Items
```python
# Call browse_search_items with keyword
browse_search_items(q="laptop", limit=10)
```

### Get Item Details
```python
# Call browse_get_item with item ID
browse_get_item(item_id="v1|123456789|0")
```

### Check Product Compatibility
```python
# Call browse_check_compatibility
browse_check_compatibility(
    item_id="v1|123456789|0",
    compatibility_properties={"Make": "BMW", "Model": "R1200GS"}
)
```

### Get Current Deals
```python
# Call deal_get_deal_items
deal_get_deal_items(max_results=20)
```

### Start Guest Checkout
```python
# Call order_initiate_guest_checkout
order_initiate_guest_checkout(
    contact_email="buyer@example.com",
    line_items=[{"itemId": "v1|123456789|0", "quantity": 1}],
    shipping_address={
        "addressLine1": "123 Main St",
        "city": "San Jose",
        "country": "US",
        "postalCode": "95131",
        "stateOrProvince": "CA",
        "recipient": {
            "firstName": "John",
            "lastName": "Doe",
            "phoneNumber": "4085551234"
        }
    }
)
```

## 5. Available Tools

Run `list_tools()` to see all 27 available tools:

**Browse API** (7 tools)
- browse_get_item
- browse_get_items
- browse_get_item_by_legacy_id
- browse_get_items_by_item_group
- browse_check_compatibility
- browse_search_items
- browse_search_by_image

**Deal API** (4 tools)
- deal_get_deal_items
- deal_get_events
- deal_get_event
- deal_get_event_items

**Feed API** (4 tools)
- feed_get_item_feed
- feed_get_item_group_feed
- feed_get_item_snapshot_feed
- feed_get_item_priority_feed

**Marketing API** (1 tool)
- marketing_get_merchandised_products

**Offer API** (2 tools)
- offer_get_bidding
- offer_place_proxy_bid

**Order API** (7 tools)
- order_initiate_guest_checkout
- order_get_guest_checkout_session
- order_update_guest_quantity
- order_update_guest_shipping_address
- order_update_guest_shipping_option
- order_apply_guest_coupon
- order_remove_guest_coupon
- order_get_guest_purchase_order

## 6. Error Handling

All tools return error responses as dictionaries:

```python
{
    "error": "Failed to get OAuth token: ..."
}
```

No exceptions are raised for expected errors (404s, invalid IDs, etc.).

## 7. Troubleshooting

### "Failed to get OAuth token"
- Check EBAY_APP_ID and EBAY_CERT_ID are set correctly
- Verify credentials are valid in eBay Developer Portal
- Check EBAY_ENVIRONMENT is set to SANDBOX or PRODUCTION

### "404 Not Found"
- Verify item IDs are in correct format (e.g., v1|123|0)
- Check endpoint is available in your marketplace
- Ensure you're using the correct environment (SANDBOX vs PRODUCTION)

### "401 Unauthorized"
- Token may have expired (server will auto-refresh)
- Check OAuth scope is correct
- Verify credentials haven't been revoked

## 8. Next Steps

- Read README.md for detailed documentation
- Check IMPLEMENTATION_SUMMARY.md for architecture details
- Review grounding.json for tool-to-documentation mapping
- See VERIFICATION.md for compliance checklist

## 9. Integration with MCP Clients

This server is compatible with any MCP-compliant client. Example configuration:

```json
{
  "mcpServers": {
    "ebay-buy-api": {
      "command": "python",
      "args": ["server.py"],
      "env": {
        "EBAY_APP_ID": "your_app_id",
        "EBAY_CERT_ID": "your_cert_id",
        "EBAY_ENVIRONMENT": "SANDBOX"
      }
    }
  }
}
```

## 10. Support

For issues or questions:
1. Check the documentation files
2. Review the grounding.json for endpoint details
3. Consult eBay API documentation at https://developer.ebay.com/api-docs/buy
