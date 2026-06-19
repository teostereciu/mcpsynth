# disableInventoryLocation

<p>This call disables the inventory location that is specified in the <code>merchantLocationKey</code> path parameter. Sellers can not load/modify inventory to disabled locations. Note that disabling a location will not affect any active eBay listings associated with the disabled location, but the seller will not be able modify the offers associated with a disabled location.</p><p>A successful call will return an HTTP status value of <i>200 OK</i>.</p>

## Endpoint

```
POST /location/{merchantLocationKey}/disable
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **merchantLocationKey** (required): This path parameter specifies the unique merchant-defined key (ID) for an inventory location that is to be disabled. <br><br>Use the <a href="/api-docs/sell/inventory/resources/location/methods/getInventoryLocations">getInventoryLocations</a> method to retrieve merchant location keys.<br><br><b>Max length</b>: 36 (Type: `string`)

## Response

**200**: Success

Response includes JSON with relevant data.

## Example

```bash
curl -X POST \
  https://api.ebay.com/location/{merchantLocationKey}/disable \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

location

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
