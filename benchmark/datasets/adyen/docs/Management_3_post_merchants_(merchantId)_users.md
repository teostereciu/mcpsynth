# Management/3/post/merchants/(merchantId)/users

*Source: https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/users*

---

# Create a new user
Creates a user for themerchantIdspecified in the path.
To make this request, your API credential must have the followingrole:
- Management API—Users read and write
Unique identifier of the merchant.
The list ofaccount groupsassociated with this user.
The email address of the user.
The requested login method for the user. To use SSO, you must already have SSO configured with Adyen before creating the user.
Possible values:Username & account,Email, orSSO
The user's full name.
Allowed length: 1—80 characters.
The first name.
The last name.
The list ofrolesfor this user.
Thetz database nameof the time zone of the user. For example,Europe/Amsterdam.
The user's email address that will be their username. Must be the same as the one in theemailfield.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow less_linksobjectReferences to resources connected with this user.Show childrenHide childrenselfobjectLink to the resource itself.Show childrenHide childrenhrefstringaccountGroupsarray[string]The list ofaccount groupsassociated with this user.activebooleanIndicates whether this user is active.appsarray[string]Set of apps available to this useremailstringThe email address of the user.idstringThe unique identifier of the user.nameobjectThe user's full name.Show childrenHide childrenfirstNamestringMax length:80The first name.lastNamestringMax length:80The last name.rolesarray[string]The list ofrolesfor this user.timeZoneCodestringThetz database nameof the time zone of the user. For example,Europe/Amsterdam.usernamestringMin length:1Max length:255The username for this user.
- 204 - No ContentThe request has been successfully processed, but there is no additional content.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error