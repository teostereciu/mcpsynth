# Management/3/get/merchants

*Source: https://docs.adyen.com/api-explorer/Management/3/get/merchants*

---

# Get a list of merchant accounts
Returns the list of merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query parameters.
To make this request, your API credential must have the followingroles:
- Management API—Account read
The number of items to have on a page, maximum 100. The default is 10 items on a page.
The number of the page to fetch.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow less_linksobjectPagination references.Show childrenHide childrenfirstobjectThe first page.Show childrenHide childrenhrefstringlastobjectThe last page.Show childrenHide childrenhrefstringnextobjectThe next page. Only present if there is a next page.Show childrenHide childrenhrefstringprevobjectThe previous page. Only present if there is a previous page.Show childrenHide childrenhrefstringselfobjectThe current page.Show childrenHide childrenhrefstringdataarray[object]The list of merchant accounts.Show childrenHide children_linksobjectReferences to resources connected with this merchant.Show childrenHide childrenapiCredentialsobjectShow childrenHide childrenhrefstringselfobjectLink to the resource itself.Show childrenHide childrenhrefstringusersobjectShow childrenHide childrenhrefstringwebhooksobjectShow childrenHide childrenhrefstringcaptureDelaystringThecapture delayset for the merchant account.Possible values:ImmediateManualNumber of days from1to29companyIdstringThe unique identifier of the company account this merchant belongs todataCentersarray[object]List of available data centers.Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers.Show childrenHide childrenlivePrefixstringThe uniquelive URL prefixfor your live endpoint. Each data center has its own live URL prefix.This field is empty for requests made in the test environment.namestringThe name assigned to a data center, for exampleEUfor the European data center. Possible values are:default: the European data center. This value is always returned in the test environment.AUEUUSdefaultShopperInteractionstringThe defaultshopperInteractionvalue used when processing payments through this merchant account.descriptionstringYour description for the merchant account, maximum 300 charactersidstringThe unique identifier of the merchant account.merchantCitystringThe city where the legal entity of this merchant account is registered.namestringThe name of the legal entity associated with the merchant account.pricingPlanstringOnly applies to merchant accounts managed by Adyen's partners. The name of the pricing plan assigned to the merchant account.primarySettlementCurrencystringThe currency of the country where the legal entity of this merchant account is registered. Format:ISO currency code. For example, a legal entity based in the United States has USD as the primary settlement currency.referencestringReference of the merchant account.shopWebAddressstringThe URL for the ecommerce website used with this merchant account.statusstringThe status of the merchant account.Possible values:PreActive: The merchant account has been created. Users cannot access the merchant account in the Customer Area. The account cannot process payments.Active: Users can access the merchant account in the Customer Area. If the company account is alsoActive, then payment processing and payouts are enabled.InactiveWithModifications: Users can access the merchant account in the Customer Area. You cannot process new payments but you can still modify payments, for example issue refunds. You can still receive payouts.Inactive: Users can access the merchant account in the Customer Area. Payment processing and payouts are disabled.Closed: The account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled.itemsTotalintegerTotal number of items.pagesTotalintegerTotal number of pages.
- 204 - No ContentThe request has been successfully processed, but there is no additional content.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- Immediate
- Manual
- Number of days from1to29
- default: the European data center. This value is always returned in the test environment.
- AU
- EU
- US

```
shopperInteraction
```
- PreActive: The merchant account has been created. Users cannot access the merchant account in the Customer Area. The account cannot process payments.
- Active: Users can access the merchant account in the Customer Area. If the company account is alsoActive, then payment processing and payouts are enabled.
- InactiveWithModifications: Users can access the merchant account in the Customer Area. You cannot process new payments but you can still modify payments, for example issue refunds. You can still receive payouts.
- Inactive: Users can access the merchant account in the Customer Area. Payment processing and payouts are disabled.
- Closed: The account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled.

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error