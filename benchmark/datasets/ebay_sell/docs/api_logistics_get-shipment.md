# getShipment

This method retrieves the shipment details for the specified shipment ID. Call <b>createFromShippingQuote</b> to generate a shipment ID.

## Endpoint

```
GET /shipment/{shipmentId}
```

## API

Logistics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **shipmentId** (required): This path parameter specifies the unique eBay-assigned identifier of the shipment you want to retrieve.<br><br>The <b>shipmentId</b> value is generated and returned by the <a href="/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote" target="_blank">createFromShippingQuote</a> method. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/Shipment`

## Example

```bash
curl -X GET \
  https://api.ebay.com/shipment/{shipmentId} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

shipment

## Reference

- [eBay Logistics API Documentation](https://developer.ebay.com/api-docs/sell/logistics/overview.html)
