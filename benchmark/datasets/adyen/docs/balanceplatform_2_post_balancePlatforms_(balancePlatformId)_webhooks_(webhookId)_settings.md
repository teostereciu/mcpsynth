# balanceplatform/2/post/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/post/balancePlatforms/(balancePlatformId)/webhooks/(webhookId)/settings*

---

# Create a balance webhook setting
Configures the criteria for triggeringbalance webhooks.
Adyen sends balance webhooks to notify you of balance changes in your balance platform. They can be triggered when the balance reaches, exceeds, or drops below a specific value in a specific currency.
You can get notified about balance changes in your entire balance platform, in the balance accounts of a specific user, or a specific balance account. The hierarchy between the webhook settings are based on the following business logic:
- Settings on a higher level apply to all lower level resources (balance platform > account holder > balance acocunt).
- The most granular setting overrides higher level settings (balance account > account holder > balance platform).
The unique identifier of the balance webhook.
The unique identifier of the balance platform.
The array of conditions a balance change must meet for Adyen to send the webhook.
Define the type of balance about which you want to get notified. Possible values:
- available: the balance available for use.
- balance: the sum of transactions that have already been settled.
- pending: the sum of transactions that will be settled in the future.
- reserved: the balance currently held in reserve.
Define when you want to get notified about a balance change. Possible values:
- greaterThan: the balance in the account(s) exceeds the specifiedvalue.
- greaterThanOrEqual: the balance in the account(s) reaches or exceeds the specifiedvalue.
- lessThan: the balance in the account(s) drops below the specifiedvalue.
- lessThanOrEqual: the balance in the account(s) reaches to drops below the specifiedvalue.
The value limit in the specified balance type and currency, in minor units.
The three-characterISO currency codeof the balance.
The status of the webhook setting. Possible values:
- active: You receive a balance webhook if any of the conditions in this setting are met.
- inactive: You do not receive a balance webhook even if the conditions in this settings are met.
The type and ID of the resource about whose balance changes you want to be notified.
The unique identifier of thetarget.type. This can be the ID of your:
- balance platform
- account holder
- account holder's balance account
The resource for which you want to receive notifications. Possible values:
- balancePlatform: receive notifications about balance changes in your entire balance platform.
- accountHolder: receive notifications about balance changes of a specific user.
- balanceAccount: receive notifications about balance changes in a specific balance account.
The type of the webhook you are configuring. Set tobalance.
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