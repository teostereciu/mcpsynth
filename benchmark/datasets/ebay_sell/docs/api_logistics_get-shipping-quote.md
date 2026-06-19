# getShippingQuote

This method retrieves the complete details of the shipping quote associated with the specified <b>shippingQuoteId</b> value.  <br><br>A "shipping quote" pertains to a single specific package and contains a set of shipping "rates" that quote the cost to ship the package by different shipping carriers and services. The quotes are based on the package's origin, destination, and size.  <br><br>Call <b>createShippingQuote</b> to create a <b>shippingQuoteId</b>.

## Endpoint

```
GET /shipping_quote/{shippingQuoteId}
```

## API

Logistics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **shippingQuoteId** (required): This path parameter specifies the unique eBay-assigned ID of the shipping quote you want to retrieve.<br><br>The <b>shippingQuoteId</b> value is generated and returned by the <a href="/api-docs/sell/logistics/resources/shipping_quote/methods/createShippingQuote" target="_blank">createShippingQuote</a> method. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/ShippingQuote`

## Example

```bash
curl -X GET \
  https://api.ebay.com/shipping_quote/{shippingQuoteId} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

shipping_quote

## Reference

- [eBay Logistics API Documentation](https://developer.ebay.com/api-docs/sell/logistics/overview.html)
