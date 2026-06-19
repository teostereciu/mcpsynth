# balanceplatform/2/get/cardorders

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/get/cardorders*

---

# Get a list of card orders
Returns a paginated list of card orders.
The number of card orders returned per page.Default:10.
Specifies the position of an element in a list of card orders. The response includes a list of card orders that starts at the specified offset.
Default:0, which means that the response contains all the elements in the list of card orders.
The service center at which the card is issued. The value is case-sensitive.
Only include card orders that have been locked on or before this point in time. The value must be in ISO 8601 format. For example,2021-05-30T15:07:40Z.
Only include card orders that have been locked on or after this point in time. The value must be in ISO 8601 format. For example,2021-05-30T15:07:40Z.
Only include card orders that have been created on or before this point in time. The value must be in ISO 8601 format. For example,2021-05-30T15:07:40Z.
Only include card orders that have been created on or after this point in time. The value must be in ISO 8601 format. For example,2021-05-30T15:07:40Z.
The unique code of the card manufacturer profile.
Possible values:mcmaestro,mc,visa,mcdebit.
The status of the card order.
The unique identifier of the card manufacturer profile.
The unique identifier of the card order.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesscardOrdersarray[object]Contains objects with information about card orders.Show childrenHide childrenbeginDatestringThe date when the card order is created.cardManufacturingProfileIdstringThe unique identifier of the card manufacturer profile.closedDatestringThe date when the card order processing ends.endDatestringThe date when you manually closed the card order.Card orders are automatically closed by the end of the day it was created. If you manually closed it beforehand, the closing date is shown as theendDate.idstringThe unique identifier of the card order.lockDatestringThe date when the card order processing begins.serviceCenterstringThe service center.statusstringThe status of the card order.Possible values:Open,Closed.hasNextbooleanIndicates whether there are more items on the next page.hasPreviousbooleanIndicates whether there are more items on the previous page.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error