# cancelShipment

This method cancels the shipment associated with the specified shipment ID and the associated shipping label is deleted. When you cancel a shipment, the <b>totalShippingCost</b> of the canceled shipment is refunded to the account established by the user's billing agreement.  <br><br>Note that you cannot cancel a shipment if you have used the associated shipping label.

## Endpoint

```
POST /shipment/{shipmentId}/cancel
```

## API

Logistics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **shipmentId** (required): This path parameter specifies the unique eBay-assigned ID of the shipment to be canceled.<br><br>The <b>shipmentId</b> value is generated and returned by the <a href="/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote" target="_blank">createFromShippingQuote</a> method. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/Shipment`

## Example

```bash
curl -X POST \
  https://api.ebay.com/shipment/{shipmentId}/cancel \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

shipment

## Reference

- [eBay Logistics API Documentation](https://developer.ebay.com/api-docs/sell/logistics/overview.html)
