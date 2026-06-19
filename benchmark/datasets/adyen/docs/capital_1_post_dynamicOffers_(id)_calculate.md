# capital/1/post/dynamicOffers/(id)/calculate

*Source: https://docs.adyen.com/api-explorer/capital/1/post/dynamicOffers/(id)/calculate*

---

# Calculate a preliminary offer for a selected financing amount
Calculates a preliminary offer for the financing amount that the user selected from adynamic offer. The preliminary offer is for informational purposes only and cannot be used to initiate a grant.
Requests to this endpoint are subject to rate limits:
- Live environments: 120 requests per minute.
- Test environments: 120 requests per minute.
The unique identifier of the dynamic offer from which the user selected the financing amount.
The financing amount that the user selected from a dynamic offer. Adyen uses this amount to calculate a preliminary offer.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessaccountHolderIdstringThe unique identifier of the account holder that the dynamic offer is for.amountobjectThe financing amount that would be paid out to your user.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.contractTypestringThe contract type of the offer.Possible values:loancashAdvanceexpiresAtstringThe expiration date and time of the offer validity period.feeobjectContains information about the fee that your user would pay for the grant.Show childrenHide childrenamountobjectContains the amount of the offer fee.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.aprBasisPointsintegerAnnual Percentage Rate (APR) of the offer. The percentage is expressed inbasis points.repaymentobjectContains information about the repayment configuration of the grant.Show childrenHide childrenbasisPointsintegerThe percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed inbasis points.termobjectContains information about the time period in which your user must repay the total amount of the grant.Show childrenHide childrenestimatedDaysintegerThe estimated duration of the repayment term, in days.maximumDaysintegerThe maximum duration of the repayment term, in days. Only applies whencontractTypeisloan.thresholdobjectContains the minimum threshold amount that your user must repay every 30-day period.Show childrenHide childrenamountobjectThe minimum threshold amount that your user must repay on every 30-day period.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.startsAtstringThe starting date and time of the offer validity period.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK
- loan
- cashAdvance

#### 422 - Unprocessable Entity