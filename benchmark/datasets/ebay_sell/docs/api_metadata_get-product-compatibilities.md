# getProductCompatibilities

This method is used to retrieve all available item compatibility details for the specified product.<br><br>Item compatibility details can be used to see the properties for which an item is compatible. For example, if you are searching for a part for a specific vehicle, you can use this method to see the years, engine, and/or trim for which the part is compatible. Item compatibility details are returned as name-value pairs.<br><br>The product for which to retrieve item compatibility details must be provided through the <b>productIdentifier</b> field. This value can be either an eBay specific identifier (such as an ePID) or an external identifier (such as a UPC).<br><br>By default, all available item compatibility details for the specified product are returned. You can limit the size of the result set using the <b>dataset</b> or <b>datasetPropertyName</b> fields to specify the types of properties you want returned in the response. The <b>applicationPropertyFilter</b> array can also be used so that only parts compatible with the specified name-value pairs are returned.

## Endpoint

```
POST /compatibilities/get_product_compatibilities
```

## API

Metadata API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace.<br><br>See <a href="/api-docs/sell/metadata/overview.html#requirements" target="_blank ">Metadata API requirements and restrictions</a> for supported values. (Type: `string`)
- **Content-Type** (required): This header indicates the format of the request body provided by the client.<br><br>Its value should be set to <code>application/json</code>.<br><br>For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a> in the <a href="/api-docs/static/ebay-rest-landing.html" target="_blank">Using eBay RESTful APIs</a> guide. (Type: `string`)

### Request Body

See schema: `#/components/schemas/ProductRequest`


## Response

**200**: Success

Response schema: `#/components/schemas/ProductResponse`

**204**: No Content

## Example

```bash
curl -X POST \
  https://api.ebay.com/compatibilities/get_product_compatibilities \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

compatibilities

## Reference

- [eBay Metadata API Documentation](https://developer.ebay.com/api-docs/sell/metadata/overview.html)
