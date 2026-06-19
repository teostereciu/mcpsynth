# payments-app/1/get/merchants/(merchantId)/paymentsApps

*Source: https://docs.adyen.com/api-explorer/payments-app/1/get/merchants/(merchantId)/paymentsApps*

---

# Get a list of Payments Apps - merchant level
Returns the list of Payments App instances for the merchant account identified in the path.
To make this request, your API credential must have the followingrole:
- Adyen Payments App role
The number of items to skip.
The number of items to return.
The status of the Payments App. Comma-separated list of one or more values. If no value is provided, the list returns all statuses.
Possible values:
- BOARDING
- BOARDED
- REVOKED
The unique identifier of the merchant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesspaymentsAppsarray[object]List of Payments Apps.Show childrenHide childreninstallationIdstringThe unique identifier of the Payments App instance.merchantAccountCodestringThe account code associated with the Payments App instance.merchantStoreCodestringThe store code associated with the Payments App instance.statusstringThe status of the Payments App instance.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error