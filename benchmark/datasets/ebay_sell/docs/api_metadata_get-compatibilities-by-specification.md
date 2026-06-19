# getCompatibilitiesBySpecification

This method is used to retrieve all compatible application name-value pairs for a part based on the provided specification(s).<br><br>The part's relevant dimensions and/or characteristics can be provided through the <b>specifications</b> container. For example, when retrieving compatible application name-value pairs for a tire, the tire's dimensions (such as the section width or rim diameter) should be provided.<br><br>By default, all compatible application name-value pairs for the specifications are returned. You can limit the size of the result set by using the <b>compatibilityPropertyFilters</b> array to specify the properties (such as make, model, year, or trim) you wish to be included in the response.<br><br><span class="tablenote"><b>Note:</b> The <a href="/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyNames" target="_blank ">getCompatibilityPropertyNames</a> and <a href="/api-docs/sell/metadata/resources/compatibilities/methods/getCompatibilityPropertyValues" target="_blank ">getCompatibilityPropertyValues</a> methods can be used to retrieve valid property names and values that can be used as the name-value pairs to define specifications.</span>

## Endpoint

```
POST /compatibilities/get_compatibilities_by_specification
```

## API

Metadata API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace.<br><br>See <a href="/api-docs/sell/metadata/overview.html#requirements" target="_blank ">Metadata API requirements and restrictions</a> for supported values. (Type: `string`)
- **Content-Type** (required): This header indicates the format of the request body provided by the client.<br><br>Its value should be set to <code>application/json</code>.<br><br>For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a> in the <a href="/api-docs/static/ebay-rest-landing.html" target="_blank">Using eBay RESTful APIs</a> guide. (Type: `string`)

### Request Body

See schema: `#/components/schemas/SpecificationRequest`


## Response

**200**: Success

Response schema: `#/components/schemas/SpecificationResponse`

**204**: No Content

## Example

```bash
curl -X POST \
  https://api.ebay.com/compatibilities/get_compatibilities_by_specification \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

compatibilities

## Reference

- [eBay Metadata API Documentation](https://developer.ebay.com/api-docs/sell/metadata/overview.html)
