# Management/3/get/companies/(companyId)

*Source: https://docs.adyen.com/api-explorer/Management/3/get/companies/(companyId)*

---

# Get a company account
Returns the company account specified in the path. Your API credential must have access to the company account.
To make this request, your API credential must have the followingroles:
- Management API—Account read
The unique identifier of the company account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow less_linksobjectReferences to resources connected with this company.Show childrenHide childrenapiCredentialsobjectShow childrenHide childrenhrefstringselfobjectLink to the resource itself.Show childrenHide childrenhrefstringusersobjectShow childrenHide childrenhrefstringwebhooksobjectShow childrenHide childrenhrefstringdataCentersarray[object]List of available data centers.Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers.Show childrenHide childrenlivePrefixstringThe uniquelive URL prefixfor your live endpoint. Each data center has its own live URL prefix.This field is empty for requests made in the test environment.namestringThe name assigned to a data center, for exampleEUfor the European data center. Possible values are:default: the European data center. This value is always returned in the test environment.AUEUUSdescriptionstringYour description for the company account, maximum 300 charactersidstringThe unique identifier of the company account.namestringThe legal or trading name of the company.referencestringYour reference to the accountstatusstringThe status of the company account.Possible values:Active: Users can log in. Processing and payout capabilities depend on the status of the merchant account.Inactive: Users can log in. Payment processing and payouts are disabled.Closed: The company account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- default: the European data center. This value is always returned in the test environment.
- AU
- EU
- US
- Active: Users can log in. Processing and payout capabilities depend on the status of the merchant account.
- Inactive: Users can log in. Payment processing and payouts are disabled.
- Closed: The company account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error