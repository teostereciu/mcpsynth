# balanceplatform/2/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/get/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings/(settingId)*

---

# Get a balance webhook setting by id
Returns the details of a specific balance webhook setting configured for triggeringbalance webhooks.
The unique identifier of the balance webhook setting.
The unique identifier of the balance webhook.
The unique identifier of the balance platform.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesscurrencystringMin length:1The three-characterISO currency codeof the balance.idstringThe unique identifier of the webhook setting.statusstringThe status of the webhook setting. Possible values:active: You receive a balance webhook if any of the conditions in this setting are met.inactive: You do not receive a balance webhook even if the conditions in this settings are met.targetobjectThe resource about whose balance change you want to get notified.Show childrenHide childrenidstringMin length:1The unique identifier of thetarget.type. This can be the ID of your:balance platformaccount holderaccount holder's balance accounttypestringThe resource for which you want to receive notifications. Possible values:balancePlatform: receive notifications about balance changes in your entire balance platform.accountHolder: receive notifications about balance changes of a specific user.balanceAccount: receive notifications about balance changes in a specific balance account.typestringThe type of the webhook setting.Select typebalance
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 404 - Not FoundThe payment was not foundShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK
- active: You receive a balance webhook if any of the conditions in this setting are met.
- inactive: You do not receive a balance webhook even if the conditions in this settings are met.
- balance platform
- account holder
- account holder's balance account
- balancePlatform: receive notifications about balance changes in your entire balance platform.
- accountHolder: receive notifications about balance changes of a specific user.
- balanceAccount: receive notifications about balance changes in a specific balance account.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error