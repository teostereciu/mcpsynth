# balanceplatform/2/get/scaAssociations

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/get/scaAssociations*

---

# Get a list of devices associated with an entity
Returns a paginated list of the SCA devices associated with a specific entity.
The index of the page to retrieve. The index of the first page is0(zero).
Default:0.
The number of items to have on a page.
Default:5.
The unique identifier of the entity.
The type of entity you want to retrieve a list of associations for.
Possible values:accountHolderorpaymentInstrument.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow less_linksobjectA list of hyperlinks to resources related to this response.Show childrenHide childrenfirstobjectThe link to the first page of the list.Show childrenHide childrenhrefstringlastobjectThe link to the last page of the list.Show childrenHide childrenhrefstringnextobjectThe link to the next page of the list.Show childrenHide childrenhrefstringpreviousobjectThe link to the previous page of the list.Show childrenHide childrenhrefstringselfobjectThe link to the list page you are currently viewing.Show childrenHide childrenhrefstringdataarray[object]Contains a list of associations and their corresponding details.Show childrenHide childrencreatedAtstringThe date and time when the association was created.entityIdstringMin length:1Max length:100The unique identifier of the entity.entityTypestringThe type of the entity.Possible values:accountHolderorpaymentInstrument.scaDeviceIdstringMin length:30Max length:30The unique identifier of the SCA device.scaDeviceNamestringMax length:64The human-readable name for the SCA device that was registered.scaDeviceTypestringThe type of the device.statusstringThe status of the association.Possible values:activeorpendingApproval.itemsTotalintegerThe total number of items available.pagesTotalintegerThe total number of pages available.
- 400 - Bad requestThe request contains invalid input and fails validation.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 500 - Internal Server Error