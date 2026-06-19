# downloadLabelFile

This method returns the shipping label file that was generated for the <b>shipmentId</b> value specified in the request. Call <b>createFromShippingQuote</b> to generate a shipment ID.<br><br><span class="tablenote"><b>Note:</b> The Logistics API only supports USPS shipping rates and labels.</span><br>Use the <code>Accept</code> HTTP header to specify the format of the returned file. The default file format is a PDF file. <!-- Are other options available? -->

## Endpoint

```
GET /shipment/{shipmentId}/download_label_file
```

## API

Logistics API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **shipmentId** (required): This path parameter specifies the unique eBay-assigned identifier of the shipment associated with the shipping label you want to download.<br><br> The <b>shipmentId</b> value is generated and returned by the <a href="/api-docs/sell/logistics/resources/shipment/methods/createFromShippingQuote" target="_blank">createFromShippingQuote</a> method. (Type: `string`)

## Headers

- **Accept** (required): This header specifies the format of the returned file. For this method, the value of the header should be <code>Accept: application/pdf</code>.  (Type: `string`)

## Response

**200**: Success

## Example

```bash
curl -X GET \
  https://api.ebay.com/shipment/{shipmentId}/download_label_file \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

shipment

## Reference

- [eBay Logistics API Documentation](https://developer.ebay.com/api-docs/sell/logistics/overview.html)
