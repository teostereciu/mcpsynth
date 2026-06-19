# balanceplatform/2/post/transferRoutes/calculate

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/post/transferRoutes/calculate*

---

# Calculate transfer routes
Returns available transfer routes based on a combination of transfercountry,currency,counterparty, andpriorities. Use this endpoint to find optimal transfer priorities and associated requirements before youmake a transfer.
The unique identifier of the sourcebalance account.
Required ifcounterpartyistransferInstrumentId.
The unique identifier assigned to the balance platform associated with the account holder.
The type of transfer. Possible values:
- bank: Transfer to atransfer instrumentor a bank account.
The recipient of the funds transfer. A bank account or a transfer instrument.
Contains information about the bank account.
Contains the bank account details. The fields required in this object depend on the country of the bank account and the currency of the transfer.
The unique identifier of thetransfer instrument.
The two-character ISO-3166-1 alpha-2 country code of the counterparty. For example,USorNL.
Eithercounterpartyorcountryfield must be provided in a transfer route request.
The three-character ISO currency code of transfer. For example,USDorEUR.
The list of priorities for the bank transfer. Priorities set the speed at which the transfer is sent and the fees that you have to pay. Multiple values can be provided.
Possible values:
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesstransferRoutesarray[object]List of available priorities for a transfer, along with requirements. Use this information to initiate a transfer.Show childrenHide childrencategorystringThe type of transfer.Possible values:bank: Transfer to atransfer instrumentor a bank account.countrystringThe two-character ISO-3166-1 alpha-2 country code of the counterparty. For example,USorNL.currencystringThe three-character ISO currency code of transfer. For example,USDorEUR.prioritystringThe priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Possible values:regular: For normal, low-value transactions.fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.instant: For instant funds transfers within the United States and inSEPA locations.crossBorder: For high-value transfers to a recipient in a different country.internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).requirementsarrayA set of rules defined by clearing houses and banking partners. Your transfer request must adhere to these rules to ensure successful initiation of transfer. Based on the priority, one or more requirements may be returned. Each requirement is defined with atypeanddescription.Select requirementsAdditionalBankIdentificationRequirementAddressRequirementAmountMinMaxRequirementAmountNonZeroDecimalsRequirementBankAccountIdentificationTypeRequirementIbanAccountIdentificationRequirementPaymentInstrumentRequirementUSInstantPayoutAddressRequirementUSInternationalAchAddressRequirementUSInternationalAchPriorityRequirement
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- bank: Transfer to atransfer instrumentor a bank account.
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error