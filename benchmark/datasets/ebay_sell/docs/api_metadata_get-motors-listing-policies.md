# getMotorsListingPolicies

This method returns eBay Motors policy metadata for all leaf categories on the specified marketplace. <p>By default, this method returns metadata on all leaf categories. You can limit the size of the result set by using the <b>filter</b> query parameter to specify only the leaf category IDs you want to review.</p><p>If you specify a valid marketplace ID but that marketplace does not contain policy information, or if you filter out all results, a successful call returns a <b>204 No content</b> status code with an empty response body.</p><p><span class="tablenote"><span style="color:#004680"><strong>Note:</strong></span> To return policy information for eBay US Motors categories, specify <b>marketplace_id</b> as <code>EBAY_MOTORS_US</code>.</span></p>

## Endpoint

```
GET /marketplace/{marketplace_id}/get_motors_listing_policies
```

## API

Metadata API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **marketplace_id** (required): This path parameter specifies the eBay marketplace for which policy information is retrieved.<br><br>See <a href="/api-docs/static/rest-request-components.html#marketpl" target="_blank">HTTP Request Headers</a> for a list of supported eBay marketplace ID values. (Type: `string`)

## Query Parameters

- **filter**: This query parameter limits the response by only returning metadata for the specified leaf categories. Supply the <b>categoryId</b> for one or more leaf categories. You can verify if a category is a leaf category by using the <a href="/api-docs/commerce/taxonomy/overview.html" target="_blank ">Taxonomy API</a> and looking for a <code>"leafCategory": true</code> tag. <br><br>The parameter takes a list of <b>categoryId</b> values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character ('|'). If you specify more than 50 <code>categoryId</code> values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.<br><br><b>Example:</b> <code>filter=categoryIds:{3767|171784}</code> (Type: `string`)

## Headers

- **Accept-Language**: This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class="tablenote"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/MotorsListingPoliciesResponse`

**204**: No content

## Example

```bash
curl -X GET \
  https://api.ebay.com/marketplace/{marketplace_id}/get_motors_listing_policies \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

marketplace

## Reference

- [eBay Metadata API Documentation](https://developer.ebay.com/api-docs/sell/metadata/overview.html)
