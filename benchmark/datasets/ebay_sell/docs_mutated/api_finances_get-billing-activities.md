# getBillingActivities

<div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including all <b>Finances API</b> methods. Please refer to <a href="/develop/guides/digital-signatures-for-apis " target="_blank">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br><span class="tablenote"><b>Note:</b>  The <b>Finances API</b> does not support <a href="https://www.ebay.com/sellercenter/ebay-for-business/multi-user-account-access" target="_blank">Team Access</a>. Financial information, such as payouts or transactions, is only returned for the user that makes the call. You cannot use any of the methods in this API to return financial information for another user.</span><br>This method retrieves filtered billing activities of the seller. Returned results are filtered through query parameters such as date range, activity ID, listing ID, or order ID. Sorting and pagination features help organize and navigate returned activities efficiently.

## Endpoint

```
GET /billing_activity
```

## API

Finances API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **filter**: This required field specifies which results to return in the response. Only one of the following four filter values must be used. A user can either retrieve all billing activity within a date range, or they can retrieve billing activity related to a specific eBay order, eBay listing, or they can retrieve information on a specific billing activity.<br /><ul><li><b>activityId</b>: If this filter is used, only information on a specific billing activity is returned. The <a href="#response.billingActivities.billingTransactionId">billingTransactionId</a> returned in the response can be used as the <b>activityId</b>.</li><li><b>listingId</b>: If this filter is used, only billing activity associated with the specified listing is returned.</li><li><b>orderId</b>: If this filter is used, only billing activity associated with the specified order is returned.</li><li><b>transactionDate</b>: If a date range filter is used, only billing activity that occurred within the specified date range is returned. The starting date cannot be set back further than 120 days in the past. Use UTC date values in the following order: <code>[<em>start</em>..<em>end</em>]</code></li></ul><br /><b>Examples</b><br /><br />IDs:<br /> <code>filter=activityID:{12**56}</code><br /><br />Date range:<br />  <code>filter=transactionDate:[2025-10-01T00:00:00Z..2025-10-31T23:59:59Z]</code> For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/finances/types/cos:FilterField (Type: `string`)
- **limit**: Sets the maximum number of records to return per page of data.<br><p>Use this parameter in conjunction with the <b>offset</b> parameter to control the pagination of the output. For example, with offset set to <code>20</code> and limit set to <code>10</code>, the call retrieves entries 21 through 30 from the result set.</p><p>Although this field is optional, if omitted the default value of <code>100</code> is used.</p><br> <b>Minimum:</b> <code>1</code><br><b>Maximum:</b> <code>200</code><br><b>Default:</b> <code>100</code> (Type: `string`)
- **offset**: Specifies the number of records to skip in the result set. This is used with the <code>limit</code> field to control the pagination of the output. For example:<br><ul><li>If <b>offset</b> is <code>0</code> and <b>limit</b> is <code>10</code>, the method will retrieve records 1-10 from the list of records returned</li><li>If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>10</code>, the method will retrieve records 11-20 from the list of records returned.</li></ul><p>If this parameter is not set, its value defaults to <code>0</code> which returns the first page of records.</p><p><span class="tablenote"><span style="color:#004680"><strong>Note: </strong>This feature employs a zero-based list, where the first activity in the list has an offset of 0.</span></p><p><b>Default:</b> <code>0</code> (zero, returns the first page)</p> (Type: `string`)
- **sort_by**: By default, transactions that match the input criteria are sorted in descending order according to the transaction date (most recent transactions returned first).<br><br>To view transactions in ascending order instead (oldest transactions first), include the <b>sort_by</b> query parameter and set its value to <code>sort_by=transactionDate</code>. For example (ascending order):<br><br><code>filter=transactionDate:[2025-11-01T00:00:01.000Z..2025-11-12T00:00:01.000Z]&sort_by=transactionDate</code><br><br>Transactions can only be sorted according to transaction date. If omitted, defaults to descending order (most recent transactions returned first). For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/finances/types/cos:SortField (Type: `string`)

## Headers

- **Accept-Language**: This header indicates the natural language and locale preferred by the user for the response.<br><br>For more information, see the <b>Accept-Language</b> header in <a href="/api-docs/static/rest-request-components.html#headers" target="_blank ">HTTP request headers</a> and <a href="/api-docs/static/rest-request-components.html#marketpl"  target="_blank">Marketplace ID values</a>. If not provided, defaults to <code>en-US</code>. (Type: `string`)

## Response

**200**: OK

Response schema: `#/components/schemas/BillingActivityResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/billing_activity \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

billing_activity

## Reference

- [eBay Finances API Documentation](https://developer.ebay.com/api-docs/sell/finances/overview.html)
