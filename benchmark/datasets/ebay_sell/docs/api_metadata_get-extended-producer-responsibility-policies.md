# getExtendedProducerResponsibilityPolicies

This method returns the Extended Producer Responsibility policies for one, multiple, or all eBay categories in an eBay marketplace.<br><br>The identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay category IDs are passed in through the filter query parameter, this method will return metadata on every applicable category for the specified marketplace.<br><br><span class="tablenote"><span style="color:#004680"><strong>Note:</strong></span> Currently, the Extended Producer Responsibility policies are only applicable to a limited number of categories.</span><br><span class="tablenote"><span style="color:#004680"><strong>Note: </strong></span>Extended Producer Responsibility IDs are no longer set at the listing level so category-level metadata is no longer returned. Instead, sellers will provide/manage these IDs at the account level by going to <a href="https://accountsettings.ebay.fr/epr-fr " target="_blank">Account Settings</a>.</span><br><span class="tablenote"><span style="color:#478415"><strong>Tip:</strong></span> This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the <b>Accept-Encoding</b> request header and setting the value to <code>gzip</code>.</span>

## Endpoint

```
GET /marketplace/{marketplace_id}/get_extended_producer_responsibility_policies
```

## API

Metadata API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **marketplace_id** (required): This path parameter specifies the eBay marketplace for which policy information shall be retrieved.<br><br>See <a href="/api-docs/static/rest-request-components.html#marketpl" target="_blank">HTTP Request Headers</a> for a list of supported eBay marketplace ID values. (Type: `string`)

## Query Parameters

- **filter**: A query parameter that can be used to limit the response by returning policy information for only the selected sections of the category tree. Supply <b>categoryId</b> values for the sections of the tree that should be returned.<br><br>When a <b>categoryId</b> value is specified, the returned category tree includes the policies for that parent node, as well as the policies for any child nodes below that parent node.<br><br>Pass in the <b>categoryId</b> values using a URL-encoded, pipe-separated ('|') list. For example:<br><br><code>filter=categoryIds%3A%7B100%7C101%7C102%7D</code><br><br><b>Maximum:</b> 50 (Type: `string`)

## Headers

- **Accept-Encoding**: This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set to <code>gzip</code>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)
- **Accept-Language**: This header is required to retrieve metadata for the French Canada, French Belgium, and Dutch Belgium marketplaces.<br><br>Follow the instructions below to retrieve metadata for these three marketplaces:<ul><li><b>French Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li><li><b>Dutch Belgium</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_BE</code>, and include the <b>Accept-Language</b> header with a value of <code>nl-BE</code>.</li><li><b>French Canada</b>: Set the <b>marketplace_id</b> path parameter value to <code>EBAY_CA</code>, and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li></ul><span class="tablenote"><b>Note:</b> If <code>EBAY_CA</code> is set as the <b>marketplace_id</b> path parameter and the <b>Accept-Language</b> header is not used, the marketplace will default to the English Canada marketplace.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/ExtendedProducerResponsibilityPolicyResponse`

**204**: No content

## Example

```bash
curl -X GET \
  https://api.ebay.com/marketplace/{marketplace_id}/get_extended_producer_responsibility_policies \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

marketplace

## Reference

- [eBay Metadata API Documentation](https://developer.ebay.com/api-docs/sell/metadata/overview.html)
