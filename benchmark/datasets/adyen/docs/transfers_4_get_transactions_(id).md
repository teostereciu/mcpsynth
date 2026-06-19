# transfers/4/get/transactions/(id)

*Source: https://docs.adyen.com/api-explorer/transfers/4/get/transactions/(id)*

---

# Get a transaction
Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.
Returns a transaction.
The unique identifier of the transaction.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessaccountHolderobjectContains information about the account holder associated with thebalanceAccount.Show childrenHide childrendescriptionstringThe description of the resource.idstringThe unique identifier of the resource.referencestringThe reference for the resource.amountobjectContains information about the amount of the transaction.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.balanceAccountobjectContains information about the balance account involved in the transaction.Show childrenHide childrendescriptionstringThe description of the resource.idstringThe unique identifier of the resource.referencestringThe reference for the resource.balancePlatformstringThe unique identifier of the balance platform.bookingDatestringThe date the transaction was booked into the balance account.creationDatestringThe date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.descriptionstringThedescriptionfrom the/transfersrequest.idstringThe unique identifier of the transaction.paymentInstrumentobjectContains information about the payment instrument that was used for the transaction.Show childrenHide childrendescriptionstringThe description of the resource.idstringThe unique identifier of the resource.referencestringThe reference for the resource.tokenTypestringThe type of wallet that the network token is associated with.referenceForBeneficiarystringThe reference sent to or received from the counterparty.For outgoing funds, this is thereferenceForBeneficiaryfrom the/transfersrequest.For incoming funds, this is the reference from the sender.statusstringThe status of the transaction.Possible values:pending: The transaction is still pending.booked: The transaction has been booked to the balance account.transferobjectContains information about the transfer related to the transaction.Show childrenHide childrencategoryDataThe relevant data according to the transfer category.Select categoryDataBankCategoryDataInternalCategoryDataIssuedCardPlatformPaymentidstringThe ID of the resource.referencestringThereferencefrom the/transfersrequest. If you haven't provided any, Adyen generates a unique reference.valueDatestringThe date the transfer amount becomes available in the balance account.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- For outgoing funds, this is thereferenceForBeneficiaryfrom the/transfersrequest.
- For incoming funds, this is the reference from the sender.

```
referenceForBeneficiary
```
- pending: The transaction is still pending.
- booked: The transaction has been booked to the balance account.

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error