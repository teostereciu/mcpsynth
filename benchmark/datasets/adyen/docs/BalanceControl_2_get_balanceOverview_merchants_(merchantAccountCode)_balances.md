# BalanceControl/2/get/balanceOverview/merchants/(merchantAccountCode)/balances

*Source: https://docs.adyen.com/api-explorer/BalanceControl/2/get/balanceOverview/merchants/(merchantAccountCode)/balances*

---

# View all balances available for your merchant account
Returns an overview of the different balances available for the merchant account. This includes details about the following:
- Available funds: The funds in the merchant account that have been settled and are available for use.
- Pending balance: The funds in the merchant account that have not been settled yet.
- Next payout amount: The amount that will be settled to your bank account with the next payout.
- Reserve: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that cannot be covered by your in-process funds.
- Deposit: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.
The currency for which you want a balances overview.
The unique identifier of your merchant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessavailableFundobjectShow childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.depositobjectShow childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.merchantAccountstringnextPayoutobjectShow childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.pendingBalanceobjectShow childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.reserveobjectShow childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable ContentA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Content