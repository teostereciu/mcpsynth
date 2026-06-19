# eBay Buy API MCP Server - Quick Start Guide

Get up and running with the eBay Buy API MCP server in 5 minutes.

## Prerequisites

- Python 3.8+
- eBay Developer Account
- eBay API credentials (App ID and Cert ID)

## Step 1: Get eBay API Credentials

1. Go to [eBay Developer Program](https://developer.ebay.com/)
2. Sign in or create an account
3. Create an application to get:
   - **App ID** (Client ID)
   - **Cert ID** (Client Secret)
4. Note these credentials for the next step

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Set Environment Variables

```bash
export EBAY_APP_ID="your_app_id_here"
export EBAY_CERT_ID="your_cert_id_here"
export EBAY_ENVIRONMENT="SANDBOX"
```

Or create a `.env` file:
```
EBAY_APP_ID=your_app_id_here
EBAY_CERT_ID=your_cert_id_here
EBAY_ENVIRONMENT=SANDBOX
```

## Step 4: Start the Server

```bash
python server.py
```

You should see output indicating the server is running and listening on stdio.

## Step 5: Test a Tool

In another terminal, test the server with a simple search:

```python
# Example using Python
import requests
import json

# The server listens on stdio, so you'd use your MCP client
# For testing, you can make direct API calls through the server

# Example: Search for items
# This would be called through your MCP client
```

## Common Use Cases

### 1. Search for Items

```python
search_items(
    q="laptop",
    limit=20,
    filter="price:[500..1500]"
)
```

### 2. Get Item Details

```python
get_item(
    item_id="v1|123456789|0",
    fieldgroups="PRODUCT,ADDITIONAL_SELLER_DETAILS"
)
```

### 3. Browse Deals

```python
# Get current deals
deals = get_deal_items(limit=50)

# Get items for a specific event
event_items = get_event_items(event_ids="event123", limit=20)
```

### 4. Complete a Checkout

```python
# 1. Initiate checkout
session = initiate_guest_checkout_session(items_payload='''
{
  "contactEmail": "buyer@example.com",
  "lineItemInputs": [
    {"itemId": "v1|123456789|0", "quantity": 1}
  ],
  "shippingAddress": {
    "addressLine1": "123 Main St",
    "city": "San Jose",
    "stateOrProvince": "CA",
    "postalCode": "95131",
    "country": "US",
    "firstName": "John",
    "lastName": "Doe",
    "phoneNumber": "+14155551234"
  }
}
''')

# 2. Get session ID
session_id = session["checkoutSessionId"]

# 3. Apply coupon
apply_guest_coupon(
    checkout_session_id=session_id,
    coupon_code="SAVE10"
)

# 4. Get final details
final = get_guest_checkout_session(checkout_session_id=session_id)
print(f"Total: {final['pricing']['total']}")
```

### 5. Place a Bid

```python
# Get bidding info
bidding = get_bidding(item_id="v1|123456789|0")

# Place a proxy bid
result = place_proxy_bid(
    item_id="v1|123456789|0",
    bid_amount="150.00"
)
```

## Troubleshooting

### "Failed to get access token"

**Problem**: Authentication failed
**Solution**:
1. Verify `EBAY_APP_ID` and `EBAY_CERT_ID` are set correctly
2. Check that credentials are for the correct environment (SANDBOX vs PRODUCTION)
3. Ensure your eBay application is active

### "Invalid item ID"

**Problem**: Item not found
**Solution**:
1. Verify the item ID format (should be like `v1|123456789|0`)
2. Check that the item exists and is available
3. Try searching for items first to get valid IDs

### "Unauthorized" or "Forbidden"

**Problem**: API scope or permission issue
**Solution**:
1. Verify your eBay application has the required scopes
2. Check that your credentials have the necessary permissions
3. Review eBay API documentation for scope requirements

### "Rate limit exceeded"

**Problem**: Too many requests
**Solution**:
1. Implement exponential backoff in your client
2. Reduce request frequency
3. Check eBay API rate limit documentation

## Environment Switching

### Sandbox (Testing)
```bash
export EBAY_ENVIRONMENT="SANDBOX"
```

### Production (Live)
```bash
export EBAY_ENVIRONMENT="PRODUCTION"
```

**Warning**: Use PRODUCTION only when ready for real transactions!

## Available Tools

The server provides 28 tools across 6 API namespaces:

- **Browse API** (7 tools): Search, get items, check compatibility
- **Deal API** (4 tools): Get deals and events
- **Feed API** (4 tools): Download item feeds
- **Marketing API** (1 tool): Get merchandised products
- **Offer API** (2 tools): Bidding and proxy bids
- **Order API** (7 tools): Guest checkout workflow

See `TOOLS_REFERENCE.md` for complete tool documentation.

## Next Steps

1. **Read the full documentation**: See `README.md` for comprehensive guide
2. **Review tool reference**: Check `TOOLS_REFERENCE.md` for all available tools
3. **Explore examples**: See `README.md` for detailed usage examples
4. **Check implementation details**: See `IMPLEMENTATION_SUMMARY.md` for architecture

## API Documentation

For detailed API information:
- [eBay Buy API Docs](https://developer.ebay.com/api-docs/buy/overview)
- [Browse API](https://developer.ebay.com/api-docs/buy/browse)
- [Deal API](https://developer.ebay.com/api-docs/buy/deal)
- [Feed API](https://developer.ebay.com/api-docs/buy/feed)
- [Marketing API](https://developer.ebay.com/api-docs/buy/marketing)
- [Offer API](https://developer.ebay.com/api-docs/buy/offer)
- [Order API](https://developer.ebay.com/api-docs/buy/order)

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review eBay API documentation
3. Verify your credentials and environment
4. Check API rate limits
5. Review error messages in the response

## Tips for Success

1. **Start with Sandbox**: Always test in SANDBOX environment first
2. **Use valid item IDs**: Get item IDs from search results
3. **Handle errors gracefully**: Check for `error` field in responses
4. **Implement rate limiting**: Add delays between requests if needed
5. **Cache results**: Store frequently accessed data locally
6. **Monitor usage**: Track API calls in eBay developer dashboard

## Example: Complete Search-to-Checkout Flow

```python
# 1. Search for items
results = search_items(q="laptop", limit=5)
if "error" in results:
    print(f"Search failed: {results['error']}")
    exit(1)

# 2. Get first item
item_id = results["itemSummaries"][0]["itemId"]
item = get_item(item_id=item_id)

# 3. Start checkout
session = initiate_guest_checkout_session(items_payload=f'''
{{
  "contactEmail": "buyer@example.com",
  "lineItemInputs": [{{"itemId": "{item_id}", "quantity": 1}}],
  "shippingAddress": {{
    "addressLine1": "123 Main St",
    "city": "San Jose",
    "stateOrProvince": "CA",
    "postalCode": "95131",
    "country": "US",
    "firstName": "John",
    "lastName": "Doe",
    "phoneNumber": "+14155551234"
  }}
}}
''')

if "error" in session:
    print(f"Checkout failed: {session['error']}")
    exit(1)

# 4. Get final details
session_id = session["checkoutSessionId"]
final = get_guest_checkout_session(checkout_session_id=session_id)
print(f"Order total: {final['pricing']['total']}")
```

## Performance Tips

1. **Batch requests**: Use `get_items()` instead of multiple `get_item()` calls
2. **Limit results**: Use `limit` parameter to reduce data transfer
3. **Cache tokens**: Tokens are cached automatically (1 hour)
4. **Reuse sessions**: Keep checkout sessions open for multiple operations
5. **Use pagination**: Use `offset` and `limit` for large result sets

## Security Best Practices

1. **Never hardcode credentials**: Always use environment variables
2. **Use HTTPS**: All API calls use HTTPS
3. **Protect tokens**: Tokens are cached in memory only
4. **Validate input**: Validate user input before passing to API
5. **Use SANDBOX first**: Test thoroughly before going to PRODUCTION
6. **Monitor usage**: Check API usage regularly
7. **Rotate credentials**: Periodically rotate your API credentials

## Getting Help

- **eBay Developer Support**: https://developer.ebay.com/support
- **API Documentation**: https://developer.ebay.com/api-docs
- **Community Forums**: https://forums.ebay.com/
- **GitHub Issues**: Check the repository for known issues

---

**Ready to start?** Run `python server.py` and begin using the eBay Buy API!
