# payments-app/1/post/merchants/(merchantId)/paymentsApps/(installationId)/revoke

*Source: https://docs.adyen.com/api-explorer/payments-app/1/post/merchants/(merchantId)/paymentsApps/(installationId)/revoke*

---

# Revoke Payments App instance authentication
Revokes the authentication of the Payments App instance for theinstallationIdand merchant account identified in the path. This call revokes the authentication of the Payments App instance with theinstallationIdidentified in the path for both merchant accounts and stores.
To make this request, your API credential must have the followingrole:
- Adyen Payments App role
The unique identifier of the Payments App instance on a device.
The unique identifier of the merchant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 500 - Internal Server Error