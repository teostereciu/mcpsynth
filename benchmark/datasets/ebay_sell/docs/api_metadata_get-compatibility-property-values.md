# getCompatibilityPropertyValues

This method is used to retrieve product compatibility property values associated with a single property name, in the specified category.<br><br>Compatibility property values can be used alongside the corresponding compatibility property name (retrieved using the <a href="/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyNames" target="_blank ">getCompatibilityPropertyNames</a> method) to describe the assembly for which an item is compatible.<br><br>The <b>categoryId</b> of the compatibility-enabled category for which to retrieve compatibility property values is required in the request body, as well as the <b>propertyName</b> for which you wish to retrieve associated values.<br><br>By default, all property values associated with the specified <b>propertyName</b> are returned. You can limit the size of the result set by using the <b>propertyFilter</b> array. Only property values associated with the specified name-value pairs will be returned.

## Endpoint

```
POST /compatibilities/get_compatibility_property_values
```

## API

Metadata API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace.<br><br>See <a href="/api-docs/sell/metadata/overview.html#requirements" target="_blank ">Metadata API requirements and restrictions</a> for supported values. (Type: `string`)
- **Content-Type** (required): This header indicates the format of the request body provided by the client.<br><br>Its value should be set to <code>application/json</code>.<br><br>For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a> in the <a href="/api-docs/static/ebay-rest-landing.html" target="_blank">Using eBay RESTful APIs</a> guide. (Type: `string`)

### Request Body

See schema: `#/components/schemas/PropertyValuesRequest`


## Response

**200**: Success

Response schema: `#/components/schemas/PropertyValuesResponse`

**204**: No Content

## Example

```bash
curl -X POST \
  https://api.ebay.com/compatibilities/get_compatibility_property_values \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

compatibilities

## Reference

- [eBay Metadata API Documentation](https://developer.ebay.com/api-docs/sell/metadata/overview.html)
