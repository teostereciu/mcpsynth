# getPayout

<div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including all <b>Finances API</b> methods. Please refer to <a href="/develop/guides/digital-signatures-for-apis " target="_blank">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br><span class="tablenote"><b>Note:</b>  The <b>Finances API</b> does not support <a href="https://www.ebay.com/sellercenter/ebay-for-business/multi-user-account-access" target="_blank">Team Access</a>. Financial information, such as payouts or transactions, is only returned for the user that makes the call. You cannot use any of the methods in this API to return financial information for another user.</span><br>This method retrieves details on a specific seller payout. The unique identifier of the payout is passed in as a path parameter at the end of the call URI. <br><br>The <b>getPayouts</b> method can be used to retrieve the unique identifier of a payout, or the user can check Seller Hub.<br><br>For split-payout cases, which are <b>only</b> available to sellers in mainland China, this method will return the <b>payoutPercentage</b> for the specified payout. This value indicates the current payout percentage allocated to a payment instrument. This method will also return the <b>convertedToCurrency</b> and <b>convertedToValue</b> response fields in CNY value. <br><br><span class="tablenote"><b>Note:</b> In split-payout cases, this method will only return details on an individual payout, also known as a true(actual) payoutid. If a user inputs a <b>payoutReference</b> id as a path parameter, the call will fail and the <b>404 not found</b> status code will be returned.<br>For more information on split payouts, see <a href="/api-docs/split-payout/playbook.html" target="_blank">Mainland China Split Payout Playbook</a>.</span>

## Endpoint

```
GET /payout/{payout_Id}
```

## API

Finances API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **payout_Id** (required): This path parameter is used to specify the unique identifier of the payout being retrieved. <br><br>Use the <a href="/api-docs/sell/finances/resources/payout/methods/getPayouts" target="_blank ">getPayouts</a> method to retrieve payout IDs, or check Seller Hub to get the payout ID.  (Type: `string`)

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace.<br><br>See <a href="/api-docs/static/rest-request-components.html#marketpl " target="_blank ">HTTP request headers</a> for the marketplace ID values.<br><br><span class="tablenote"><b>Note:</b> If a marketplace ID value is not provided, the default value of <code>EBAY_US</code> is used.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/Payout`

## Example

```bash
curl -X GET \
  https://api.ebay.com/payout/{payout_Id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

payout

## Reference

- [eBay Finances API Documentation](https://developer.ebay.com/api-docs/sell/finances/overview.html)
