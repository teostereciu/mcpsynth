# getAutomotivePartsCompatibilityPolicies

This method returns the eBay policies that define how to list automotive parts compatibility items in the categories of the specified marketplace.  <br><br>By default, this method returns all categories that support parts compatibility. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the category IDs you want to review.<br><br><span class="tablenote"><b>Note: </b>To return policy information for the eBay US marketplace, specify <code>EBAY_MOTORS_US</code> as the path parameter for <b>market_id</b>.</span><br><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span><br>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a <b>204 No content</b> status code is returned with an empty response body.

## Endpoint

```
GET /marketplace/{market_id}/get_automotive_parts_compatibility_policies
```

## API

Metadata API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **market_id** (required): This path parameter specifies the eBay marketplace for which policy information is retrieved.  <br><br><span class="tablenote"><b>Note: </b>Only the following eBay marketplaces support automotive parts compatibility: <ul> <li>EBAY_MOTORS_US</li> <li>EBAY_AU</li> <li>EBAY_CA</li> <li>EBAY_DE</li> <li>EBAY_ES</li> <li>EBAY_FR</li> <li>EBAY_GB</li> <li>EBAY_IT</li></ul></span> (Type: `string`)

## Query Parameters

- **filter**: This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree you want returned. Use the <a href="/api-docs/commerce/taxonomy/overview.html" target="_blank ">Taxonomy API</a> to retrieve category ID values.<br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  <br><br><b>Example:</b> <code>filter=categoryIds:{183521|183523|183524}</code>  <br><br><span class="tablenote"><b>Note: </b>URL-encoding of the parameter list is no longer required.</span> (Type: `string`)

## Headers

- **Accept-Encoding**: This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/AutomotivePartsCompatibilityPolicyResponse`

**204**: No content

## Example

```bash
curl -X GET \
  https://api.ebay.com/marketplace/{market_id}/get_automotive_parts_compatibility_policies \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

marketplace

## Reference

- [eBay Metadata API Documentation](https://developer.ebay.com/api-docs/sell/metadata/overview.html)
