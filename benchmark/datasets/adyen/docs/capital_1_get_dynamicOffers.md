# capital/1/get/dynamicOffers

*Source: https://docs.adyen.com/api-explorer/capital/1/get/dynamicOffers*

---

# Get all available dynamic offers
Returns a list of alldynamic offersavailable foraccountHolderIdspecified as a query parameter.
The type of financing that the offer is for. If the value is not specified, returns all available types.
Possible values:businessFinancing
The unique identifier of the account holder that the dynamic offer is for.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdynamicOffersarray[object]Contains a list of available dynamic offers for the specified account holder.Show childrenHide childrenaccountHolderIdstringThe unique identifier of the account holder that the dynamic offer is for.contractTypestringThe contract type of the offer.Possible values:loancashAdvanceexpiresAtstringThe expiration date and time of the offer validity period.financingTypestringThe type of financing that the offer is for.Possible values:businessFinancing.idstringThe unique identifier of the dynamic offer.maximumAmountobjectThe maximum financing amount available to the account holder under this offer.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.minimumAmountobjectThe minimum financing amount available to the account holder under this offer.Show childrenHide childrencurrencystringThe three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.repaymentobjectContains information about the repayment configuration of the grant.Show childrenHide childrentermobjectContains information about the time period in which your user must repay the total amount of the grant.Show childrenHide childrenestimatedDaysintegerThe estimated duration of the repayment term, in days.maximumDaysintegerThe maximum duration of the repayment term, in days. Only applies whencontractTypeisloan.startsAtstringThe starting date and time of the offer validity period.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK
- loan
- cashAdvance

#### 422 - Unprocessable Entity