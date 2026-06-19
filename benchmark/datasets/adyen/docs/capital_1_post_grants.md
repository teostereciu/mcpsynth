# capital/1/post/grants

*Source: https://docs.adyen.com/api-explorer/capital/1/post/grants*

---

# Make a request for a grant
Make a request for a grant on behalf of an account holder.
Contains the details of the party that receives the grant.
The unique identifier of the balance account where the funds are disbursed. The balance account must belong to the specified account holder.
The unique identifier of the transfer instrument where the funds are disbursed. The transfer instrument must belong to the legal entity of the specified account holder.
The unique identifier of the grant account that tracks this grant.
The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessbalancesobjectContains information about the balances of the grant.Show childrenHide childrencurrencystringThe three-characterISO currency code.feeintegerThe amount of the grant fee.principalintegerThe grant amount that is paid out to the user for business financing.totalintegerThe total amount of the grant that the user must repay. It is the sum of the fee amount and the principal amount.counterpartyobjectContains the details of the party that receives the grant.Show childrenHide childrenaccountHolderIdstringThe unique identifier of the account holder that receives the grant.balanceAccountIdstringThe unique identifier of the balance account where the funds are disbursed. The balance account must belong to the specified account holder.transferInstrumentIdstringThe unique identifier of the transfer instrument where the funds are disbursed. The transfer instrument must belong to the legal entity of the specified account holder.grantAccountIdstringThe unique identifier of the grant account that tracks this grant.grantOfferIdstringThe unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.idstringThe unique identifier of the grant reference.statusobjectContains the status of the grant.Show childrenHide childrenactionsarray[object]A list of actions that need to be completed to proceed with the grant.Show childrenHide childrenactionCodestringThe code identifying the action that needs to be completed.resolvedbooleanIndicates whether this action has been successfully completed.codeThe code for the status of the grant. Possible values:PendingActiveRepaidWrittenOffFailedRevokedRequestedReviewingApprovedRejectedCancelled
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK
- Pending
- Active
- Repaid
- WrittenOff
- Failed
- Revoked
- Requested
- Reviewing
- Approved
- Rejected
- Cancelled

#### 422 - Unprocessable Entity