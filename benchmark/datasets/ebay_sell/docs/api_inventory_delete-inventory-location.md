# deleteInventoryLocation

<p>This call deletes the inventory location that is specified in the <code>merchantLocationKey</code> path parameter. Note that deleting a location will not affect any active eBay listings associated with the deleted location, but the seller will not be able modify the offers associated with the location once it is deleted.</p><span class="tablenote"><b>Note:</b> Deletion is not currently supported for fulfillment center locations, as location mappings will still be retained despite the location being deleted. Instead, fulfillment center locations should be disabled using the <a href="/api-docs/sell/inventory/resources/location/methods/disableInventoryLocation" target="_blank">disableInventoryLocation</a> method.</span><p>Unless one or more errors and/or warnings occur with the call, there is no response payload for this call. A successful call will return an HTTP status value of <i>200 OK</i>.</p>

## Endpoint

```
DELETE /location/{merchantLocationKey}
```

## API

Inventory API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **merchantLocationKey** (required): This path parameter specifies the unique merchant-defined key (ID) for the inventory location that is to be deleted.<br><br>Use the <a href="/api-docs/sell/inventory/resources/location/methods/getInventoryLocations">getInventoryLocations</a> method to retrieve merchant location keys.<br><br><b>Max length</b>: 36 (Type: `string`)

## Response

**204**: Success

## Example

```bash
curl -X DELETE \
  https://api.ebay.com/location/{merchantLocationKey} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

location

## Reference

- [eBay Inventory API Documentation](https://developer.ebay.com/api-docs/sell/inventory/overview.html)
