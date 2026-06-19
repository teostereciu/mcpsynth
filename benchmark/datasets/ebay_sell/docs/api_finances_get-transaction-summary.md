# getTransactionSummary

<div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including all <b>Finances API</b> methods. Please refer to <a href="/develop/guides/digital-signatures-for-apis " target="_blank">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><<br><span class="tablenote"><b>Note:</b>  The <b>Finances API</b> does not support <a href="https://www.ebay.com/sellercenter/ebay-for-business/multi-user-account-access" target="_blank">Team Access</a>. Financial information, such as payouts or transactions, is only returned for the user that makes the call. You cannot use any of the methods in this API to return financial information for another user.</span><br>The <b>getTransactionSummary</b> method retrieves cumulative information for monetary transactions. If applicable, the number of payments with a <code>transactionStatus</code> equal to <code>FUNDS_ON_HOLD</code> and the total monetary amount of these on-hold payments are also returned.<br><br><span class="tablenote"><b>Note:</b> For a complete list of transaction types, refer to <a href="/api-docs/sell/finances/types/pay:TransactionTypeEnum " target="_blank ">TransactionTypeEnum</a>.</span><br>Refer to the <a href="#uri.filter ">filter</a> field for additional information about each filter and its use.<br><br><span class="tablenote"><b>Note:</b> Unless a <code>transactionType</code> filter is used to retrieve a specific type of transaction (e.g., <code>SALE</code>, <code>REFUND</code>, etc.,) the <a href="#response.creditCount">creditCount</a> and <a href="#response.creditAmount">creditAmount</a> response fields both include <i>order sales</i> and <i>seller credits</i> information. That is, the <b>count</b> and <b>value</b> fields do not distinguish between these two types monetary transactions.</span> <br><br><b>Note:</b> getTransactionSummary will only return data on transactions that occurred less than five years in the past.

## Endpoint

```
GET /transaction_summary
```

## API

Finances API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **filter**: Numerous filters are available for the <strong>getTransactionSummary</strong> method, and these filters are discussed below. One or more of these filter types can be used. The <b>transactionStatus</b> filter must be used. All other filters are optional. <ul><li><b>transactionStatus</b>: the data returned in the response pertains to the sales, payouts, and transfer status set. For supported <b>transactionStatus</b> values, see <a href="/api-docs/sell/finances/types/pay:TransactionStatusEnum" target="_blank ">TransactionStatusEnum</a>. <br><br>Below is the proper syntax to use when setting up the <b>transactionStatus</b> filter: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction_summary?filter=transactionStatus:&#123;PAYOUT&#125;</code></li><li><b>transactionDate</b>: only consider monetary transactions that occurred within a specific range of dates.<br><br><span class="tablenote"><strong>Note:</strong> All dates must be input using UTC format (<code>YYYY-MM-DDTHH:MM:SS.SSSZ</code>) and should be adjusted accordingly for the local timezone of the user.</span><br><br>Below is the proper syntax to use if filtering by a date range: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction_summary?filter=transactionDate:&#91;2024-10-23T00:00:01.000Z..2024-11-09T00:00:01.000Z&#93;</code><br><br><b>Note:</b>Only monetary transactions from the last five years can be retrieved, so make sure the starting date is less than five years in the past from the present time. Also, the maximum date range that can be specified through this date filter is 36 months, so make sure your specified date range is no more than 36 months.</li>  <li><b>transactionType</b>: only consider a specific type of monetary transaction. For supported <b>transactionType</b> values, see <a href="/api-docs/sell/finances/types/pay:TransactionTypeEnum" target="_blank ">TransactionTypeEnum</a>.<br><br>Below is the proper syntax to use if filtering by a monetary transaction type: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction_summary?filter=transactionType:{SALE}</code></li><li><b>buyerUsername</b>: only consider monetary transactions involving a specific buyer (specified with the buyer's eBay username or user ID). Below is the proper syntax to use if filtering by a specific eBay buyer: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction_summary?filter=buyerUsername:&#123;buyer1234&#125;</code> </li><li><b>payoutId</b>: only consider monetary transactions related to a specific seller payout (identified with a Payout ID). This value is auto-generated by eBay once the seller payout is set to be processed. Below is the proper syntax to use if filtering by a specific Payout ID: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction_summary?filter=payoutId:&#123;5********8&#125;</code>  </li><li><b>transactionId</b>: the unique identifier of a monetary transaction. For a sales order, the <b>orderId</b> filter should be used instead. Only the monetary transaction(s) associated with this <b>transactionId</b> value are returned.<br><br><span class="tablenote"><strong>Note:</strong> This filter cannot be used alone; the <b>transactionType</b> must also be specified when filtering by transaction ID.</span><br><br>Below is the proper syntax to use if filtering by a specific transaction ID: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction_summary?filter=transactionId:{0*-0***0-3***3}&filter=transactionType:{SALE}</code> </li><li><b>orderId</b>: the unique identifier of a sales order. For any other monetary transaction, the <b>transactionId</b> filter should be used instead. Only the monetary transaction(s) associated with this <b>orderId</b> value are returned. Below is the proper syntax to use if filtering by a specific order ID: <br><br><code>https://apiz.ebay.com/sell/finances/v1/transaction_summary?filter=orderId:{0*-0***0-3***3}</code> </li></ul> For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/finances/types/cos:FilterField (Type: `string`)

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace.<br><br>See <a href="/api-docs/static/rest-request-components.html#marketpl " target="_blank ">HTTP request headers</a> for the marketplace ID values.<br><br><span class="tablenote"><b>Note:</b> If a marketplace ID value is not provided, the default value of <code>EBAY_US</code> is used.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/TransactionSummaryResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/transaction_summary \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

transaction

## Reference

- [eBay Finances API Documentation](https://developer.ebay.com/api-docs/sell/finances/overview.html)
