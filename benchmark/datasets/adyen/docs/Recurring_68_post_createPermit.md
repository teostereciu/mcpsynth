# Recurring/68/post/createPermit

*Source: https://docs.adyen.com/api-explorer/Recurring/68/post/createPermit*

---

# Create new permits linked to a recurring contract
Create permits for a recurring contract, including support for defining restrictions.
The merchant account identifier, with which you want to process the transaction.
The permits to create for this recurring contract.
Partner ID (when using the permit-per-partner token sharing model).
The profile to apply to this permit (when using the shared permits model).
Permit level restriction overrides.
The total sum amount of one or more payments made using this permit may not exceed this amount if set.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The amount of any single payment using this permit may not exceed this amount if set.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Only a single payment can be made using this permit if set to true, otherwise multiple payments are allowed.
The key to link permit requests to permit results.
The expiry date for this permit.
The recurring contract the new permits will use.
The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID).
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesspermitResultListarray[object]List of new permits.Show childrenHide childrenresultKeystringThe key to link permit requests to permit results.tokenstringThe permit token which is used to make payments by the partner company.pspReferencestringA unique reference associated with the request. This value is globally unique; quote it when communicating with us about this request.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error