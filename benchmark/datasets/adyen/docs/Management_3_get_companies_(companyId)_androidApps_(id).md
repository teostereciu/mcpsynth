# Management/3/get/companies/(companyId)/androidApps/(id)

*Source: https://docs.adyen.com/api-explorer/Management/3/get/companies/(companyId)/androidApps/(id)*

---

# Get Android app
Returns the details of the Android app identified in the path.
These apps have been uploaded to Adyen and can be installed or uninstalled on Android payment terminals throughterminal actions.
To make this request, your API credential must have one of the followingroles:
- Management API—Android files read
- Management API—Android files read and write
In the live environment, requests to this endpoint are subject torate limits.
The unique identifier of the app.
The unique identifier of the company account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdescriptionstringThe description that was provided when uploading the app. The description is not shown on the terminal.errorCodestringDeprecated in version 3Useerrorsinstead.The error code of the Android app with thestatusof eithererrororinvalid.errorsarray[object]The list of errors of the Android app.Show childrenHide childrenerrorCodestringThe error code of the Android app with thestatusof eithererrororinvalid.terminalModelsarray[string]The list of payment terminal models to which the returnederrorCodeapplies.idstringThe unique identifier of the app.labelstringThe app name that is shown on the terminal.packageNamestringThe package name that uniquely identifies the Android app.statusstringThe status of the app. Possible values:processing: the app is being signed and converted to a format that the terminal can handle.error: something went wrong. Check that the app matches therequirements.invalid: there is something wrong with the APK file of the app.ready: the app has been signed and converted.archived: the app is no longer available.versionCodeintegerThe version number of the app.versionNamestringThe app version number that is shown on the terminal.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- processing: the app is being signed and converted to a format that the terminal can handle.
- error: something went wrong. Check that the app matches therequirements.
- invalid: there is something wrong with the APK file of the app.
- ready: the app has been signed and converted.
- archived: the app is no longer available.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error