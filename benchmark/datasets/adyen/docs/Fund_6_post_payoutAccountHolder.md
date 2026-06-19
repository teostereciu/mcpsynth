# Fund/6/post/payoutAccountHolder

*Source: https://docs.adyen.com/api-explorer/Fund/6/post/payoutAccountHolder*

---

# Pay out from an account to the account holder
Pays out a specified amount from an account to the bank account of account holder.
The code of the account from which the payout is to be made.
The code of the Account Holder who owns the account from which the payout is to be made.
The Account Holder is the party to which the payout will be made.
An object containing the currency and value of the payout.
If the account has multiple currencies, specify the currency to be used.
If thebankAccountUUIDis provided in the request, the currency supported by the bank is used.
If thepayoutMethodCodeis provided in the request, the specified payout method is selected.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The unique ID of the Bank Account held by the Account Holder to which the payout is to be made.
If left blank, a bank account is automatically selected.
A description of the payout. Maximum 200 characters.
Allowed:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/?:().,'+ ";
A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.
The unique ID of the payout method held by the Account Holder to which the payout is to be made.
If left blank, a payout instrument is automatically selected.
Speed with which payouts for this account are processed. Permitted values:STANDARD,SAME_DAY.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessbankAccountUUIDstringThe unique ID of the Bank Account to which the payout was made.invalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.merchantReferencestringThe value supplied by the executing user when initiating the transfer; may be used to link multiple transactions.payoutSpeedstringSpeed with which payouts for this account are processed. Permitted values:STANDARD,SAME_DAY.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 202 - AcceptedThe request has been accepted for processing, but the processing has not been completed.Show moreShow lessbankAccountUUIDstringThe unique ID of the Bank Account to which the payout was made.invalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.merchantReferencestringThe value supplied by the executing user when initiating the transfer; may be used to link multiple transactions.payoutSpeedstringSpeed with which payouts for this account are processed. Permitted values:STANDARD,SAME_DAY.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error