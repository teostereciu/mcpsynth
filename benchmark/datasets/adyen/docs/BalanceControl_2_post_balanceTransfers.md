# BalanceControl/2/post/balanceTransfers

*Source: https://docs.adyen.com/api-explorer/BalanceControl/2/post/balanceTransfers*

---

# Performs a balance transfer
Performs a balance transfer between merchant accounts. The following conditions must be met before you can successfully transfer balances:
- The source and destination merchant accounts must be under the same company account and legal entity.
- The source merchant account must have sufficient funds.
- The source and destination merchant accounts must have at least one common processing currency.\n\n
When sending multiple API requests with the same source and destination merchant accounts, send the requests sequentially andnotin parallel. Some requests may not be processed if the requests are sent in parallel.
The amount of the transfer.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The unique identifier of the source merchant account from which funds are deducted.
A reference for the balance transfer. Maximum length: 80 characters.
The unique identifier of the destination merchant account to which funds are transferred.
The type of balance transfer. Possible values:tax,fee,terminalSale,credit,debit, andadjustment.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesscreatedAtstringThe date when the balance transfer was performed.pspReferencestringAdyen's 16-character string reference associated with the balance transfer.
- 401UnauthorizedShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable ContentA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 401

#### 422 - Unprocessable Content