# Management/3/post/terminals/scheduleActions

*Source: https://docs.adyen.com/api-explorer/Management/3/post/terminals/scheduleActions*

---

# Create a terminal action
Schedules aterminal actionby specifying the action and the terminals that the action must be applied to.
The following restrictions apply:
- You can schedule only one action at a time. For example, to install a new app version and remove an old app version, you have to make two API requests.
- The maximum number of terminals in a request is100. For example, to apply an action to 250 terminals, you have to divide the terminals over three API requests.
- If there is an error with one or more terminal IDs in the request, the action is scheduled for none of the terminals. You need to fix the error and try again.
To make this request, your API credential must have the followingrole:
- Management API—Terminal actions read and write
In the live environment, requests to this endpoint are subject torate limits.
Information about the action to take.
The date and time when the action should happen.
Format:RFC 3339, but without theZbefore the time offset. For example,2021-11-15T12:16:21+0100The action is sent with the firstmaintenance callafter the specified date and time in the time zone of the terminal.
An empty value causes the action to be sent as soon as possible: at the next maintenance call.
The unique ID of thestore. If present, all terminals in theterminalIdslist must be assigned to this store.
A list of unique IDs of the terminals to apply the action to. You can extract the IDs from theGET/terminalsresponse. Maximum length: 100 IDs.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessactionDetailsInformation about the action to take.Select actionDetailsForceRebootDetailsInstallAndroidAppDetailsInstallAndroidCertificateDetailsReleaseUpdateDetailsUninstallAndroidAppDetailsUninstallAndroidCertificateDetailsitemsarray[object]A list containing a terminal ID and an action ID for each terminal that the action was scheduled for.Show childrenHide childrenidstringThe ID of the action on the specified terminal.terminalIdstringThe unique ID of the terminal that the action applies to.scheduledAtstringThe date and time when the action should happen.
Format:RFC 3339, but without theZbefore the time offset. For example,2021-11-15T12:16:21+0100The action is sent with the firstmaintenance callafter the specified date and time in the time zone of the terminal.
An empty value causes the action to be sent as soon as possible: at the next maintenance call.storeIdstringThe unique ID of thestore. If present, all terminals in theterminalIdslist must be assigned to this store.terminalsWithErrorsobjectThe validation errors that occurred in the list of terminals, and for each error the IDs of the terminals that the error applies to.totalErrorsintegerThe number of terminals for which scheduling the action failed.totalScheduledintegerThe number of terminals for which the action was successfully scheduled. This doesn't mean the action has happened yet.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error