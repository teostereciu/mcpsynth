# getTransactions

<div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including all <b>Finances API</b> methods. Please refer to <a href="/develop/guides/digital-signatures-for-apis " target="_blank">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br><span class="tablenote"><b>Note:</b>  The <b>Finances API</b> does not support <a href="https://www.ebay.com/sellercenter/ebay-for-business/multi-user-account-access" target="_blank">Team Access</a>. Financial information, such as payouts or transactions, is only returned for the user that makes the call. You cannot use any of the methods in this API to return financial information for another user.</span><br>The <b>getTransactions</b> method allows a seller to retrieve information about one or more of their monetary transactions.<br><br><span class="tablenote"><b>Note:</b> For a complete list of transaction types, refer to <a href="/api-docs/sell/finances/types/pay:TransactionTypeEnum " target="_blank ">TransactionTypeEnum</a>.</span><br>Numerous input filters are available which can be used individually or combined to refine the data that are returned. For example:<ul><li><code>SALE</code> transactions for August 15, 2022;</li><li><code>RETURN</code> transactions for the month of January, 2021;</li><li>Transactions currently in a <code>transactionStatus</code> equal to <code>FUNDS_ON_HOLD</code>.</li></ul>Refer to the <a href="#uri.filter ">filter</a> field for additional information about each filter and its use.<br><br>Pagination and sort query parameters are also provided that allow users to further control how monetary transactions are displayed in the response.<br><br>If no monetary transactions match the input criteria, an http status code of <em>204 No Content</em> is returned with no response payload. <br><br><b>Note:</b> Only monetary transactions that have occurred within the last five years can be retrieved.

## Endpoint

```
GET /transaction
```

## API

Finances API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **filter**: Numerous filters are available for the <strong>getTransactions</strong> method, and these filters are discussed below. One or more of these filter types can be used. If none of these filters are used, all monetary transactions occurring within the last five years are returned:<ul><li><b>transactionDate</b>: search for monetary transactions that occurred within a specific range of dates.<br><br><span class="tablenote"><strong>Note:</strong> All dates must be input using UTC format (<code>YYYY-MM-DDTHH:MM:SS.SSSZ</code>) and should be adjusted accordingly for the local timezone of the user.</span><br>Below is the proper syntax to use if filtering by a date range: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=transactionDate:[2024-10-23T00:00:01.000Z..2024-11-09T00:00:01.000Z]</code><br><br>Only payouts from the last five years can be retrieved, so make sure the starting date is less than five years in the past from the present time. Also, the maximum date range that can be specified through this date filter is 36 months, so make sure your specified date range is no more than 36 months.</li>  <li><b>transactionType</b>: search for a specific type of monetary transaction. For supported <b>transactionType</b> values, see <a href="/api-docs/sell/finances/types/pay:TransactionTypeEnum" target="_blank ">TransactionTypeEnum</a>.<br><br>Below is the proper syntax to use if filtering by a monetary transaction type: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=transactionType:{SALE}</code></li><li><b>transactionStatus</b>: this filter type is only applicable for sales orders, and allows the user to filter seller payouts in a particular state. For supported <b>transactionStatus</b> values, see <a href="/api-docs/sell/finances/types/pay:TransactionStatusEnum" target="_blank ">TransactionStatusEnum</a>.<br><br>Below is the proper syntax to use if filtering by transaction status: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=transactionStatus:{PAYOUT}</code></li><li><b>buyerUsername</b>: the eBay username or user ID of the buyer involved in the monetary transaction. Only monetary transactions involving this buyer are returned. Below is the proper syntax to use if filtering by a specific eBay buyer: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=buyerUsername:{buyer1234}</code> </li><li><b>payoutId</b>: the unique identifier of a seller payout. This value is auto-generated by eBay once the seller payout is set to be processed. Only monetary transactions involving this Payout ID are returned. Below is the proper syntax to use if filtering by a specific Payout ID: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=payoutId:{5********8}</code>  </li><li><b>transactionId</b>: use this field  <b>transactionId</b> and also <b>transactionType</b> to filter for a unique identifier of a monetary transaction, or an error will occur. For a sales order, the <b>orderId</b> filter should be used instead. Only the monetary transaction defined by the identifier is returned.<br><br><span class="tablenote"><strong>Note:</strong> This filter cannot be used alone; the <b>transactionType</b> must also be specified when filtering by transaction ID.</span><br>Below is the proper syntax to use if filtering by a specific transaction ID: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=transactionId:{0*-0***0-3***3}&filter=transactionType:{SALE}</code> </li><li><b>orderId</b>: the unique identifier of a sales order. Only monetary transaction(s) associated with this <b>orderId</b> value are returned.<br><br>For any other monetary transaction, the <b>transactionId</b> filter should be used instead.<br><br>Below is the proper syntax to use if filtering by a specific order ID:<br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=orderId:{0*-0***0-3***3}</code> </li><li><b>payoutReference</b>: returns the monetary transactions associated with the <b>payoutReference</b>. By using this ID as a filter parameter, the user will be able to track all monetary transactions associated with both sibling payouts, including sales and refunds, if any. This filter is <b>only</b> supported for sellers in Mainland China. Below is the proper syntax to use if filtering by <b>payoutReference</b>: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=payoutReference:{5*******3}</code></li></ul> For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/finances/types/cos:FilterField (Type: `string`)
- **limit**: The number of monetary transactions to return per page of the result set. Use this parameter in conjunction with the <b>offset</b> parameter to control the pagination of the output. <br><br> For example, if <b>offset</b> is set to <code>10</code> and <b>limit</b> is set to <code>10</code>, the method retrieves monetary transactions 11 thru 20 from the result set. <br><br> <span class="tablenote"><strong>Note:</strong> This feature employs a zero-based list, where the first item in the list has an offset of <code>0</code>.</span> <br><br> <b>Maximum:</b><code> 1000</code> <br> <b>Default:</b><code> 20</code> (Type: `string`)
- **offset**: This integer value indicates the actual position that the first monetary transaction returned on the current page has in the results set. So, if you wanted to view the 11th monetary transaction of the result set, you would set the <strong>offset</strong> value in the request to <code>10</code>. <br><br>In the request, you can use the <b>offset</b> parameter in conjunction with the <b>limit</b> parameter to control the pagination of the output. For example, if <b>offset</b> is set to <code>30</code> and <b>limit</b> is set to <code>10</code>, the method retrieves transactions 31 thru 40 from the resulting collection of transactions. <br><br> To avoid poor response time, use <b>offset</b> values of less than <code>5000</code>. <br><br> <span class="tablenote"><strong>Note:</strong> This feature employs a zero-based list, where the first item in the list has an offset of <code>0</code>.</span><br><b>Default:</b> <code>0</code> (zero) (Type: `string`)
- **sort**: By default, monetary transactions that match the input criteria are sorted in descending order according to the transaction date (i.e, most recent transactions returned first).<br><br>To view transactions in ascending order instead (i.e., oldest transactions first), you would include the <b>sort</b> query parameter and set its value to <code>transactionDate</code>. Below is the proper syntax to use if filtering by a transaction date range in ascending order:<br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction?filter=transactionDate:[2023-10-01T00:00:01.000Z..2023-10-12T00:00:01.000Z]&sort=transactionDate</code><br><br>Transactions can only be sorted according to transaction date. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/finances/types/cos:SortField (Type: `string`)

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace.<br><br>See <a href="/api-docs/static/rest-request-components.html#marketpl " target="_blank ">HTTP request headers</a> for the marketplace ID values.<br><br><span class="tablenote"><b>Note:</b> If a marketplace ID value is not provided, the default value of <code>EBAY_US</code> is used.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/Transactions`

**204**: No Content

## Example

```bash
curl -X GET \
  https://api.ebay.com/transaction \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

transaction

## Reference

- [eBay Finances API Documentation](https://developer.ebay.com/api-docs/sell/finances/overview.html)
