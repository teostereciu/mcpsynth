# getHazardousMaterialsLabels

This method returns hazardous materials label information for the specified eBay marketplace. The information includes IDs, descriptions, and URLs (as applicable) for the available signal words, statements, and pictograms. The returned statements are localized for the default language of the marketplace. If a marketplace does not support hazardous materials label information, no response payload is returned, but only a <b>204 No content</b> status code.<p>This information is used by the seller to add hazardous materials label related information to their listings (see <a href='/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html'>Specifying hazardous material related information</a>).</p>

## Endpoint

```
GET /marketplace/{market_id}/get_hazardous_materials_labels
```

## API

Metadata API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **market_id** (required): This path parameter specifies the eBay marketplace for which hazardous materials label information shall be retrieved.<br><br>See <a href="/api-docs/static/rest-request-components.html#marketpl" target="_blank">HTTP Request Headers</a> for a list of supported eBay marketplace ID values. (Type: `string`)

## Headers

- **Accept-Language**: This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>market_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>market_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>market_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class="tablenote"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>market_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/HazardousMaterialDetailsResponse`

**204**: No content

## Example

```bash
curl -X GET \
  https://api.ebay.com/marketplace/{market_id}/get_hazardous_materials_labels \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

marketplace

## Reference

- [eBay Metadata API Documentation](https://developer.ebay.com/api-docs/sell/metadata/overview.html)
