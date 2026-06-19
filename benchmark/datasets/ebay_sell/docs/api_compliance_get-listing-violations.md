# getListingViolations

This call returns specific listing violations for the supported listing compliance types. Only one compliance type can be passed in per call, and the response will include all the listing violations for this compliance type, and listing violations are grouped together by eBay listing ID. See <a href="/api-docs/sell/compliance/types/com:ComplianceTypeEnum">ComplianceTypeEnum</a> for more information on the supported listing compliance types. This method also has pagination control. <br /><br /> <span class="tablenote"><strong>Note:</strong> A maximum of 2000 listing violations will be returned in a result set. If the seller has more than 2000 listing violations, some/all of those listing violations must be corrected before additional listing violations will be retrieved. The user should pay attention to the <strong>total</strong> value in the response. If this value is '2000', it is possible that the seller has more than 2000 listing violations, but this field maxes out at 2000. </span> <br /><span class="tablenote"><strong>Note:</strong> In a future release of this API, the seller will be able to pass in a specific eBay listing ID as a query parameter to see if this specific listing has any violations. </span><br /> <span class="tablenote"><strong>Note:</strong> Only mocked non-compliant listing data will be returned for this call in the Sandbox environment, and not specific to the seller. However, the user can still use this mock data to experiment with the compliance type filters and pagination control.</span>

## Endpoint

```
GET /listing_violation
```

## API

Compliance API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Query Parameters

- **compliance_type** (required): <span class="tablenote"><b>Note:</b> The <a href="https://developer.ebay.com/api-docs/sell/compliance/types/com:ComplianceTypeEnum" target="_blank" rel="noopener">ASPECTS_ADOPTION</a> compliance type has been deprecated and will be decommissioned on September 9th, 2025.</span><br>This query parameter specifies the compliance type of the listing violations being retrieved. Only one compliance type value can be specified. <br> <br>See <a href="/api-docs/sell/compliance/types/com:ComplianceTypeEnum">ComplianceTypeEnum</a> for more information on supported compliance types. (Type: `string`)
- **offset**: The integer value input into this field controls the first listing violation in the result set that will be displayed at the top of the response. The <strong>offset</strong> and <strong>limit</strong> query parameters are used to control the pagination of the output. For example, if <strong>offset</strong> is set to <code>10</code> and <strong>limit</strong> is set to <code>10</code>, the call retrieves listing violations 11 thru 20 from the resulting set of violations. <br /><br /> <span class="tablenote"><strong>Note:</strong> This feature employs a zero-based index, where the first item in the list has an offset of <code>0</code>. If the <strong>listing_id</strong> parameter is included in the request, this parameter will be ignored.</span><br/><br/> <strong>Default: </strong> <code>0</code> {zero) (Type: `string`)
- **listing_id**: <span class="tablenote"><strong>Note:</strong> This query parameter is not yet supported for the Compliance API.</span> (Type: `string`)
- **limit**: This query parameter is used if the user wants to set a limit on the number of listing violations that are returned on one page of the result set. This parameter is used in conjunction with the <strong>offset</strong> parameter to control the pagination of the output.<br /><br />For example, if <strong>offset</strong> is set to <code>10</code> and <strong>limit</strong> is set to <code>10</code>, the call retrieves listing violations 11 thru 20 from the collection of listing violations that match the value set in the <strong>compliance_type</strong> parameter.<br /><br /><span class="tablenote"><strong>Note:</strong> This feature employs a zero-based index, where the first item in the list has an offset of <code>0</code>. If the <strong>listing_id</strong> parameter is included in the request, this parameter will be ignored.</span><br/><br/><strong>Default:</strong> <code>100</code><br/> <strong>Maximum:</strong> <code>200</code> (Type: `string`)
- **filter**: This filter allows a user to retrieve only listings that are currently out of compliance, or only listings that are at risk of becoming out of compliance.<br><br> Although other filters may be added in the future, <code>complianceState</code> is the only supported filter type at this time. See the <a href="/api-docs/sell/compliance/types/com:ComplianceStateEnum">ComplianceStateEnum</a> type for a list of supported values.<br><br>Below is an example of how to set up this compliance state filter. Notice that the filter type and filter value are separated with a colon (:) character, and the filter value is wrapped with curly brackets.<br><br> <code>filter=complianceState:{OUT_OF_COMPLIANCE}</code> (Type: `string`)

## Headers

- **X-EBAY-C-MARKETPLACE-ID** (required): This header identifies the seller's eBay marketplace. <br><br>Supported values for this header can be found in the <a href="/api-docs/sell/compliance/types/bas:MarketplaceIdEnum">MarketplaceIdEnum</a> type definition. (Type: `string`)

## Response

**200**: Success

**204**: No Content

## Example

```bash
curl -X GET \
  https://api.ebay.com/listing_violation \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

listing_violation

## Reference

- [eBay Compliance API Documentation](https://developer.ebay.com/api-docs/sell/compliance/overview.html)
