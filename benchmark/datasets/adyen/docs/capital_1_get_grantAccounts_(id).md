# capital/1/get/grantAccounts/(id)

*Source: https://docs.adyen.com/api-explorer/capital/1/get/grantAccounts/(id)*

---

# Get the information of your grant account
Returns the details of the specified grant account. This account tracks existing grants in your marketplace or platform.
The unique identifier of the grant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessbalancesarray[object]Contains the sum of the balances of all grants tracked by this grant account. The balances are separated by currency.Show childrenHide childrencurrencystringThe three-characterISO currency code.feeintegerThe amount of the grant fee.principalintegerThe grant amount that is paid out to the user for business financing.totalintegerThe total amount of the grant that the user must repay. It is the sum of the fee amount and the principal amount.fundingBalanceAccountIdstringThe unique identifier of the balance account used to fund the grant.idstringThe unique identifier of the grant account.limitsarray[object]Contains the maximum amount of funds that you can disburse for grants.Show childrenHide childrenamountobjectThe limit amount of the grant account.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.
- 404 - Not FoundThe entity was not found.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 404 - Not Found

#### 422 - Unprocessable Entity