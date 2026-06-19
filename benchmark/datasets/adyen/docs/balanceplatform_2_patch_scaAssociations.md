# balanceplatform/2/patch/scaAssociations

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/patch/scaAssociations*

---

# Approve a pending approval association
Approves a previously created association that is in a pending state.
The header for authenticating through SCA.
The unique identifier of the entity.
The type of the entity.
Possible values:accountHolderorpaymentInstrument.
List of device ids associated to the entity that will be approved.
The status of the association.
Possible values:activeorpendingApproval.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKSuccessful approvalShow moreShow lessscaAssociationsarray[object]The list of associations.Show childrenHide childrenentityIdstringMin length:1Max length:100The unique identifier of the entity.entityTypestringThe type of entity you are associating the device with.Possible values:accountHolderorpaymentInstrument.scaDeviceIdstringMin length:30Max length:30The unique identifier for the SCA device.statusstringThe status of the association.Possible values:activeorpendingApproval.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 401 - Unauthorized

#### 403 - Forbidden

#### 500 - Internal Server Error