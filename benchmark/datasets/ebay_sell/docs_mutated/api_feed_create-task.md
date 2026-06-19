# createTask

This method creates an upload task or a download task without filter criteria. When using this method, specify the <b> feedType</b> and the feed file <b> schemaVersion</b>. The feed type specified sets the task as a download or an upload task.  <p>For details about the upload and download flows, see <a href="/api-docs/sell/static/orders/generating-and-retrieving-order-reports.html">Working with Order Feeds</a> in the Selling Integration Guide.</p><p> <span class="tablenote"><strong>Note:</strong> The scope depends on the feed type. An error message results when an unsupported scope or feed type is specified.</span></p><p>The following list contains this method's authorization scopes and their corresponding feed types:</p><ul><li>https://api.ebay.com/oauth/api_scope/sell.inventory: See <a href="/api-docs/sell/static/feed/lms-feeds-quick-reference.html#Availabl" target="_blank">LMS FeedTypes</a></li><li>https://api.ebay.com/oauth/api_scope/sell.fulfillment: LMS_ORDER_ACK (specify for upload tasks). Also see <a href="/api-docs/sell/static/feed/lms-feeds-quick-reference.html#Availabl" target="_blank">LMS FeedTypes</a></li><li>https://api.ebay.com/oauth/api_scope/sell.marketing: None*</li><li>https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly: None*</li></ul><p>* Reserved for future release</p>

## Endpoint

```
POST /task
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): The ID of the eBay marketplace where the item is hosted. <br><br>For example:<br><br><code>X-EBAY-C-MARKETPLACE-ID:EBAY_US</code><br><br>This identifies the eBay marketplace that applies to this task. See <a href="/api-docs/sell/feed/types/bas:MarketplaceIdEnum">MarketplaceIdEnum</a> for supported values.<br><br><span class="tablenote"><b>Note:</b> When listing the items in the feed file on the French Canada and French Belgium marketplaces, also set the <b>Accept-Language</b> header as needed.</span> (Type: `string`)
- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)
- **Accept-Language**: The Accept-Language header is required for listing items in the French Canada and French Belgium marketplaces. Set the following headers to list items on these marketplaces:<br><ul><li><b>French Canada</b>: Set the <b>X-EBAY-C-MARKETPLACE-ID</b> header value to <code>EBAY_CA</code> and include the <b>Accept-Language</b> header with a value of <code>fr-CA</code>.</li><li><b>French Belgium</b>: Set the <b>X-EBAY-C-MARKETPLACE-ID</b> header value to <code>EBAY_BE</code> and include the <b>Accept-Language</b> header with a value of <code>fr-BE</code>.</li></ul> (Type: `string`)

### Request Body

See schema: `#/components/schemas/CreateTaskRequest`


## Response

**202**: Accepted

## Example

```bash
curl -X POST \
  https://api.ebay.com/task \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

task

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
