# Setup Checklist

Use this checklist to verify your eBay Buy API MCP Server is properly installed and configured.

## Pre-Installation

- [ ] Python 3.8+ installed (`python --version`)
- [ ] pip installed (`pip --version`)
- [ ] eBay Developer Account created
- [ ] Application ID (EBAY_APP_ID) obtained
- [ ] Application Secret (EBAY_CERT_ID) obtained

## Installation

- [ ] Clone or download the project
- [ ] Navigate to project directory
- [ ] Run `pip install -r requirements.txt`
- [ ] Verify installation: `pip list | grep fastmcp`
- [ ] Verify installation: `pip list | grep requests`

## Configuration

- [ ] Set EBAY_APP_ID environment variable
  ```bash
  export EBAY_APP_ID="your_app_id"
  ```
- [ ] Set EBAY_CERT_ID environment variable
  ```bash
  export EBAY_CERT_ID="your_cert_id"
  ```
- [ ] Set EBAY_ENVIRONMENT to SANDBOX (for testing)
  ```bash
  export EBAY_ENVIRONMENT="SANDBOX"
  ```
- [ ] Verify environment variables are set:
  ```bash
  echo $EBAY_APP_ID
  echo $EBAY_CERT_ID
  echo $EBAY_ENVIRONMENT
  ```

## File Verification

- [ ] server.py exists and is readable
- [ ] requirements.txt exists and contains fastmcp and requests
- [ ] grounding.json exists and contains 27 tool mappings
- [ ] README.md exists
- [ ] QUICKSTART.md exists
- [ ] docs/ directory exists with 27 API documentation files

## Server Startup

- [ ] Run `python server.py`
- [ ] Server starts without errors
- [ ] Server listens on stdio (no output should appear)
- [ ] Server can be stopped with Ctrl+C

## Tool Verification

- [ ] All 27 tools are registered
- [ ] Tools are discoverable via `list_tools()`
- [ ] Tool names follow naming convention (namespace_action)
- [ ] Each tool has a docstring

### Browse API Tools (7)
- [ ] browse_get_item
- [ ] browse_get_items
- [ ] browse_get_item_by_legacy_id
- [ ] browse_get_items_by_item_group
- [ ] browse_check_compatibility
- [ ] browse_search_items
- [ ] browse_search_by_image

### Deal API Tools (4)
- [ ] deal_get_deal_items
- [ ] deal_get_events
- [ ] deal_get_event
- [ ] deal_get_event_items

### Feed API Tools (4)
- [ ] feed_get_item_feed
- [ ] feed_get_item_group_feed
- [ ] feed_get_item_snapshot_feed
- [ ] feed_get_item_priority_feed

### Marketing API Tools (1)
- [ ] marketing_get_merchandised_products

### Offer API Tools (2)
- [ ] offer_get_bidding
- [ ] offer_place_proxy_bid

### Order API Tools (7)
- [ ] order_initiate_guest_checkout
- [ ] order_get_guest_checkout_session
- [ ] order_update_guest_quantity
- [ ] order_update_guest_shipping_address
- [ ] order_update_guest_shipping_option
- [ ] order_apply_guest_coupon
- [ ] order_remove_guest_coupon
- [ ] order_get_guest_purchase_order

## Authentication Testing

- [ ] OAuth token is generated successfully
- [ ] Token is cached (second request uses cached token)
- [ ] Token expires and is refreshed automatically
- [ ] Invalid credentials return error dict

## API Testing

### Browse API
- [ ] browse_search_items returns results
- [ ] browse_get_item returns item details
- [ ] browse_check_compatibility returns compatibility status

### Deal API
- [ ] deal_get_events returns event list
- [ ] deal_get_deal_items returns deals

### Feed API
- [ ] feed_get_item_feed returns feed data
- [ ] feed_get_item_group_feed returns group feed

### Marketing API
- [ ] marketing_get_merchandised_products returns products

### Offer API
- [ ] offer_get_bidding returns bidding info

### Order API
- [ ] order_initiate_guest_checkout creates session
- [ ] order_get_guest_checkout_session retrieves session

## Error Handling

- [ ] Invalid item ID returns error dict
- [ ] Missing required parameter returns error dict
- [ ] Network error returns error dict
- [ ] No unhandled exceptions are raised

## Documentation

- [ ] README.md is readable and complete
- [ ] QUICKSTART.md provides working examples
- [ ] IMPLEMENTATION_SUMMARY.md explains architecture
- [ ] grounding.json maps all 27 tools
- [ ] Each tool has clear documentation

## Integration Testing

- [ ] Server works with MCP client
- [ ] Tools are callable from MCP client
- [ ] Results are JSON-serializable
- [ ] Error responses are properly formatted

## Performance

- [ ] Server starts in < 1 second
- [ ] API calls complete in < 30 seconds
- [ ] Token generation completes in < 10 seconds
- [ ] Token caching reduces latency

## Security

- [ ] Credentials are not hardcoded
- [ ] Credentials come from environment variables
- [ ] Tokens are cached securely
- [ ] No sensitive data in logs

## Environment Switching

- [ ] SANDBOX environment works
- [ ] PRODUCTION environment works
- [ ] Switching environments works correctly
- [ ] Correct base URLs are used

## Documentation Completeness

- [ ] All tools have docstrings
- [ ] All parameters are documented
- [ ] All return values are documented
- [ ] All error cases are documented

## Final Verification

- [ ] All 27 tools are implemented
- [ ] All 6 API namespaces are covered
- [ ] All documentation is complete
- [ ] All tests pass
- [ ] Server is ready for production

## Troubleshooting

If any checks fail:

1. **Installation Issues**
   - Verify Python version: `python --version`
   - Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

2. **Configuration Issues**
   - Verify environment variables: `env | grep EBAY`
   - Check credentials in eBay Developer Portal

3. **Authentication Issues**
   - Verify EBAY_APP_ID and EBAY_CERT_ID are correct
   - Check EBAY_ENVIRONMENT is set to SANDBOX or PRODUCTION
   - Verify credentials haven't been revoked

4. **API Issues**
   - Check item IDs are in correct format
   - Verify endpoint is available in your marketplace
   - Check API documentation for required parameters

5. **Server Issues**
   - Check server.py is syntactically correct
   - Verify all imports are available
   - Check for port conflicts

## Support

For additional help:
1. Read QUICKSTART.md
2. Check README.md
3. Review IMPLEMENTATION_SUMMARY.md
4. Consult eBay API documentation

## Sign-Off

- [ ] All checks completed
- [ ] All checks passed
- [ ] Server is ready for use
- [ ] Documentation is complete

**Date Completed**: _______________
**Verified By**: _______________
