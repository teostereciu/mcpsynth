# balanceplatform/2/patch/balanceAccounts/(id)

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/patch/balanceAccounts/(id)*

---

# Update a balance account
Updates a balance account.
The unique identifier of the balance account.
The unique identifier of theaccount holderassociated with the balance account.
A human-readable description of the balance account. You can use this parameter to distinguish between multiple balance accounts under an account holder.
A set of key and value pairs for general use.
The keys do not have specific names and may be used for storing miscellaneous data as desired.
Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs.
Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account.
Specifies at what time a sales day ends for this account.
Possible values: Time in"HH:MM"format.HHranges from00to07.MMmust be00.
Default value:"00:00".
Specifies after how many business days the funds in a settlement batch are made available in this balance account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or implementation manager to enable this.
Possible values:1to20, ornull.
Default value:null.
Your reference to the balance account.
The status of the balance account. Payment instruments linked to the balance account can only be used if the balance account status isactive.
Possible values:active,closed,suspended.
The time zone of the balance account. For example,Europe/Amsterdam.
Defaults to the time zone of the account holder if no time zone is set. For possible values, see thelist of time zone codes.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessaccountHolderIdstringThe unique identifier of theaccount holderassociated with the balance account.balancesarray[object]List of balances with the amount and currency.Show childrenHide childrenavailableintegerThe balance available for use.balanceintegerThe sum of the transactions that have already been settled.currencystringThe three-characterISO currency codeof the balance.pendingintegerThe sum of the transactions that will be settled in the future.reservedintegerThe balance currently held in reserve.defaultCurrencyCodestringThe default three-characterISO currency codeof the balance account. This is the currency displayed on the Balance Account overview page in your Customer Area.
The default value isEUR.After a balance account is created, you cannot change its default currency.descriptionstringMax length:300A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder.idstringThe unique identifier of the balance account.metadataobjectA set of key and value pairs for general use.
The keys do not have specific names and may be used for storing miscellaneous data as desired.Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs.migratedAccountCodestringThe unique identifier of the account of the migrated account holder in the classic integration.platformPaymentConfigurationobjectContains key-value pairs to configure the sales day closing time and settlement delay for a balance account.Show childrenHide childrensalesDayClosingTimestringSpecifies at what time a sales day ends for this account.Possible values: Time in"HH:MM"format.HHranges from00to07.MMmust be00.Default value:"00:00".settlementDelayDaysintegerSpecifies after how many business days the funds in a settlement batch are made available in this balance account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or implementation manager to enable this.Possible values:1to20, ornull.Default value:null.referencestringMax length:150Your reference for the balance account, maximum 150 characters.statusstringThe status of the balance account, set toactiveby default.timeZonestringThe time zone of the balance account. For example,Europe/Amsterdam.
Defaults to the time zone of the account holder if no time zone is set. For possible values, see thelist of time zone codes.
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