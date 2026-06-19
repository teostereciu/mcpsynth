# balanceplatform/2/get/mandates

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/get/mandates*

---

# Get a list of mandates
Returns a list of alldirect debit mandatescreated for a business account.
The pagination cursor returned in a previous GET/mandatesrequest.
The unique identifier of the payment instrument linked to the mandate.
The unique identifier of the balance account linked to the payment instrument.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeededShow moreShow lesslinkobjectContains links to the next and previous page whenever applicable.Show childrenHide childrenfirstobjectThe link to the first page of the list.Show childrenHide childrenhrefstringlastobjectThe link to the last page of the list.Show childrenHide childrenhrefstringnextobjectThe link to the next page of the list.Show childrenHide childrenhrefstringpreviousobjectThe link to the previous page of the list.Show childrenHide childrenhrefstringselfobjectThe link to the list page you are currently viewing.Show childrenHide childrenhrefstringmandatesarray[object]Contains a list of the mandates.Show childrenHide childrenbalanceAccountIdstringThe unique identifier of the balance account linked to the payment instrument.counterpartyobjectContains information to identify the counterparty.Show childrenHide childrenaccountHolderobjectContains information about the owner of the counterparty bank account.Show childrenHide childrenfullNamestringThe full name of the entity that owns the bank account.Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.accountIdentificationobjectContains the bank account details of the counterparty. The fields required in this object depend on the country of the bank account and the currency of the transfer.Show childrenHide childrentypestringSelect typeukLocalcreatedAtstringThe date when the mandate was created.idstringThe unique identifier of the mandate.paymentInstrumentIdstringThe unique identifier of the payment instrument linked to the mandate.statusstringThe status of the mandate.Possible values:pending,approved,cancelled.typestringThe type of mandate. Possible value:bacs.updatedAtstringThe date when the mandate was updated.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error