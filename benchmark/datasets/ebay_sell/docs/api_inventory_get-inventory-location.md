# getInventoryLocation

This call retrieves all defined details of the inventory location that is specified by the <b>merchantLocationKey</b> path parameter.<p>A successful call will return an HTTP status value of <i>200 OK</i>.</p>

## Endpoint

```
GET /location/{merchantLocationKey}
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **merchantLocationKey** (required): This path parameter specifies the unique merchant-defined key (ID) for an inventory location that is being retrieved. <br><br>Use the <a href="/api-docs/sell/inventory/resources/location/methods/getInventoryLocations">getInventoryLocations</a> method to retrieve merchant location keys. <br><br><b>Max length</b>: 36 (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/InventoryLocationResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/location/{merchantLocationKey} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

location

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
