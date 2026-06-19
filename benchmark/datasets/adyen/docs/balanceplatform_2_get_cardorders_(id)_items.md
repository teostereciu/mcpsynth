# balanceplatform/2/get/cardorders/(id)/items

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/get/cardorders/(id)/items*

---

# Get card order items
Returns the item list of a specific card order.
The number of card order items returned per page.Default:10.
Specifies the position of an element in a list of card orders. The response includes a list of card order items that starts at the specified offset.
Default:0, which means that the response contains all the elements in the list of card order items.
The unique identifier of the card order.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdataarray[object]List of card order items in the card order batch.Show childrenHide childrenbalancePlatformstringThe unique identifier of the balance platform.cardobjectThe status of the card delivery.Possible values:created,rejected,processing,produced,shipped,delivered,notApplicable,unknown.Show childrenHide childrenerrorMessagestringAn error message.statusstringThe status of the PIN delivery.trackingNumberstringThe tracking number of the PIN delivery.cardOrderItemIdstringThe unique identifier of the card order item.creationDatestringThe date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.idstringThe ID of the resource.paymentInstrumentIdstringThe unique identifier of the payment instrument related to the card order item.pinobjectContains information about the status of the PIN delivery.Show childrenHide childrenerrorMessagestringAn error message.statusstringThe status of the PIN delivery.trackingNumberstringThe tracking number of the PIN delivery.shippingMethodstringThe shipping method used to deliver the card or the PIN.hasNextbooleanIndicates whether there are more items on the next page.hasPreviousbooleanIndicates whether there are more items on the previous page.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error