# capital/1/get/grantOffers

*Source: https://docs.adyen.com/api-explorer/capital/1/get/grantOffers*

---

# Get all available static offers
Returns a list of allstatic offersavailable foraccountHolderIdspecified as a query parameter. This also includes static offers created for financing amounts that the user selected fromdynamic offers.
The unique identifier of the account holder for which you want to get the available static offers.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessgrantOffersarray[object]Contains a list of available offers for the specified account holder.Show childrenHide childrenaccountHolderIdstringThe unique identifier of the account holder to which the grant is offered.amountobjectThe amount that would be paid out to the user for business financing.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.contractTypestringThe contract type of the offer.Possible values:loancashAdvanceexpiresAtstringThe expiration date and time of the offer validity period.feeobjectContains information about the fee that your user would pay for the grant.Show childrenHide childrenamountobjectContains the amount of the offer fee.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.aprBasisPointsintegerAnnual Percentage Rate (APR) of the offer. The percentage is expressed inbasis points.idstringThe unique identifier of the offer.repaymentobjectContains information about the repayment configuration of the grant.Show childrenHide childrenbasisPointsintegerThe percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed inbasis points.termobjectContains information about the time period in which your user must repay the total amount of the grant.Show childrenHide childrenestimatedDaysintegerThe estimated duration of the repayment term, in days.maximumDaysintegerThe maximum duration of the repayment term, in days. Only applies whencontractTypeisloan.thresholdobjectContains the minimum threshold amount that your user must repay every 30-day period.Show childrenHide childrenamountobjectThe minimum threshold amount that your user must repay on every 30-day period.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.startsAtstringThe starting date and time of the offer validity period.
- 404 - Not FoundThe entity was not found.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK
- loan
- cashAdvance

#### 404 - Not Found

#### 422 - Unprocessable Entity