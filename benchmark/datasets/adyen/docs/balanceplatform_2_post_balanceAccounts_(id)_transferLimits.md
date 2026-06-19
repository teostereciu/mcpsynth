# balanceplatform/2/post/balanceAccounts/(id)/transferLimits

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/post/balanceAccounts/(id)/transferLimits*

---

# Create a transfer limit
Create a transfer limit for your balance account using the uniqueidof your balance account.
Header for authenticating through SCA
The unique identifier of the balance account.
The amount for the transfer limit. This is the maximum amount allowed per transfer or per day based on thescopeof the limit.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays active until you override it with a new limit.
FormatISO 8601:YYYY-MM-DDThh:mm:ss.sssTZD
Your reference for the transfer limit.
Information for the Strong Customer Authentication (SCA)
The type of exemption for Strong Customer Authentication (SCA). Possible values:
- lowerLimit: the newly created limit is lower than the existing limit.
- notRegulated: the limit is created in a country, region, or industry where it is not mandated by law to use SCA.
- setByPlatform: you set a limit for one of your user's balance accounts, or for your balance platform.
- initialLimit: there are no existing transfer limits set on the balance account or balance platform.
- alreadyPerformed: you are confident about your user's identity and do not need to verify this using SCA.
Indicates whether to initiate Strong Customer Authentication (SCA) later, during approval, or immediately after you submit this request. Possible values:
- true: you can initiate SCA later, during approval, for all pending transfer limits.
- false(default): you initiate SCA immediately after submitting the transfer limit request.
The scope to which the transfer limit applies. Possible values:
- perTransaction: you set a maximum amount for each transfer made from the balance account or balance platform.
- perDay: you set a maximum total amount for all transfers made from the balance account or balance platform in a day.
The date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a transfer limit.
FormatISO 8601:YYYY-MM-DDThh:mm:ss.sssTZD
The type of transfer to which the limit applies. Possible values:
- instant: the limit applies to transfers with aninstantpriority.
- all: the limit applies to all transfers, regardless of priority.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessamountobjectThe amount for the transfer limit. This is the maximum amount allowed per transfer or per day based on thescopeof the limit.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.endsAtstringThe date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays active until you override it with a new limit.FormatISO 8601:YYYY-MM-DDThh:mm:ss.sssTZDidstringThe unique identifier of the transfer limit.limitStatusstringThe status of the transfer limit. Possible values:active: the limit is currently active.inactive: the limit is currently inactive.pendingSCA: the limit is pending until your user performs SCA.scheduled: the limit is scheduled to become active at a future date.referencestringYour reference for the transfer limit.scaInformationobjectInformation for the Strong Customer Authentication (SCA)Show childrenHide childrenexemptionstringThe type of exemption for Strong Customer Authentication (SCA). Possible values:lowerLimit: the newly created limit is lower than the existing limit.notRegulated: the limit is created in a country, region, or industry where it is not mandated by law to use SCA.setByPlatform: you set a limit for one of your user's balance accounts, or for your balance platform.initialLimit: there are no existing transfer limits set on the balance account or balance platform.alreadyPerformed: you are confident about your user's identity and do not need to verify this using SCA.statusstringThe status of Strong Customer Authentication (SCA). Possible values:notPerformed: the requester was unable to successfully authenticate the request using SCA, or has an SCA exemption.pending: the request is pending SCA authentication.performed: the request is successfully authenticated using SCA.scopestringThe scope to which the transfer limit applies. Possible values:perTransaction: you set a maximum amount for each transfer made from the balance account or balance platform.perDay: you set a maximum total amount for all transfers made from the balance account or balance platform in a day.startsAtstringThe date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a transfer limit.FormatISO 8601:YYYY-MM-DDThh:mm:ss.sssTZDtransferTypestringThe type of transfer to which the limit applies. Possible values:instant: the limit applies to transfers with aninstantpriority.all: the limit applies to all transfers, regardless of priority.
- 400 - Bad RequestThe input is invalid, or no registered device for SCA was found.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 401 - UnauthorizedAuthentication required via Strong Customer Authentication (SCA). The client must resolve the provided challenge.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable ContentA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK
- active: the limit is currently active.
- inactive: the limit is currently inactive.
- pendingSCA: the limit is pending until your user performs SCA.
- scheduled: the limit is scheduled to become active at a future date.
- lowerLimit: the newly created limit is lower than the existing limit.
- notRegulated: the limit is created in a country, region, or industry where it is not mandated by law to use SCA.
- setByPlatform: you set a limit for one of your user's balance accounts, or for your balance platform.
- initialLimit: there are no existing transfer limits set on the balance account or balance platform.
- alreadyPerformed: you are confident about your user's identity and do not need to verify this using SCA.
- notPerformed: the requester was unable to successfully authenticate the request using SCA, or has an SCA exemption.
- pending: the request is pending SCA authentication.
- performed: the request is successfully authenticated using SCA.
- perTransaction: you set a maximum amount for each transfer made from the balance account or balance platform.
- perDay: you set a maximum total amount for all transfers made from the balance account or balance platform in a day.
- instant: the limit applies to transfers with aninstantpriority.
- all: the limit applies to all transfers, regardless of priority.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 422 - Unprocessable Content