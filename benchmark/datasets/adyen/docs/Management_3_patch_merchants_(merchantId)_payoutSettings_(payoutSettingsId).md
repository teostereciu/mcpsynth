# Management/3/patch/merchants/(merchantId)/payoutSettings/(payoutSettingsId)

*Source: https://docs.adyen.com/api-explorer/Management/3/patch/merchants/(merchantId)/payoutSettings/(payoutSettingsId)*

---

# Update a payout setting
Updates the payout setting identified in the path. You can enable or disable the payout setting.
Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.
To make this request, your API credential must have the followingroles:
- Management API—Payout account settings read and write
The unique identifier of the payout setting.
The unique identifier of the merchant account.
Indicates if payouts to this bank account are enabled. Default:true.
To receive payouts into this bank account, bothenabledandallowedmust betrue.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessallowedbooleanIndicates if payouts to the bank account are allowed. This value is set automatically based on the status of the verification process. The value is:trueifverificationStatusisvalid.falsefor all other values.enabledbooleanIndicates if payouts to this bank account are enabled. Default:true.To receive payouts into this bank account, bothenabledandallowedmust betrue.enabledFromDatestringThe date when Adyen starts paying out to this bank account.Format:ISO 8601, for example,2019-11-23T12:25:28Zor2020-05-27T20:25:28+08:00.If not specified, theenabledfield indicates if payouts are enabled for this bank account.If a date is specified and:enabled:true, payouts are enabled starting the specified date.enabled:false, payouts are disabled until the specified date. On the specified date,enabledchanges totrueand this field is reset tonull.idstringThe unique identifier of the payout setting.prioritystringDetermines how long it takes for the funds to reach the bank account. Adyen pays out based on thepayout frequency. Depending on the currencies and banks involved in transferring the money, it may take up to three days for the payout funds to arrive in the bank account.Possible values:first: same day.urgent: the next day.normal: between 1 and 3 days.transferInstrumentIdstringThe unique identifier of thetransfer instrumentthat contains the details of the bank account.verificationStatusstringThe status of the verification process for the bank account.Possible values:valid: the verification was successful.pending: the verification is in progress.invalid: the information provided is not complete.rejected:  there are reasons to refuse working with this entity.
- 204 - No ContentThe request has been successfully processed, but there is no additional content.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- trueifverificationStatusisvalid.
- falsefor all other values.
- enabled:true, payouts are enabled starting the specified date.
- enabled:false, payouts are disabled until the specified date. On the specified date,enabledchanges totrueand this field is reset tonull.
- first: same day.
- urgent: the next day.
- normal: between 1 and 3 days.
- valid: the verification was successful.
- pending: the verification is in progress.
- invalid: the information provided is not complete.
- rejected:  there are reasons to refuse working with this entity.

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error