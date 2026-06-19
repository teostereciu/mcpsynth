# legalentity/4/patch/transferInstruments/(id)

*Source: https://docs.adyen.com/api-explorer/legalentity/4/patch/transferInstruments/(id)*

---

# Update a transfer instrument
Updates a transfer instrument.
Requests to this endpoint are subject to rate limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.
Use the requested verification code 0_0001 to resolve any suberrors associated with the transfer instrument. Requested verification codes can only be used in your test environment.
The unique identifier of the transfer instrument.
Contains information about the legal entity's bank account.
Identification of the bank account.
The type of bank account.
The name of the banking institution where the bank account is held.
The two-characterISO 3166-1 alpha-2country code where the bank account is registered. For example,NL.
The unique identifier of thelegal entitythat owns the transfer instrument.
The type of transfer instrument.
Possible value:bankAccount.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessbankAccountobjectContains information about the legal entity's bank account.Show childrenHide childrenaccountIdentificationIdentification of the bank account.Select accountIdentificationAULocalAccountIdentificationCALocalAccountIdentificationCZLocalAccountIdentificationDKLocalAccountIdentificationHKLocalAccountIdentificationHULocalAccountIdentificationIbanAccountIdentificationNOLocalAccountIdentificationNZLocalAccountIdentificationNumberAndBicAccountIdentificationPLLocalAccountIdentificationSELocalAccountIdentificationSGLocalAccountIdentificationUKLocalAccountIdentificationUSLocalAccountIdentificationaccountTypestringDeprecated in version 2The type of bank account.bankNamestringThe name of the banking institution where the bank account is held.countryCodestringThe two-characterISO 3166-1 alpha-2country code where the bank account is registered. For example,NL.trustedSourcebooleanIdentifies if the bank account was created throughinstant bank verification.capabilitiesobjectList of capabilities for this transfer instrument.Show childrenHide childrenallowedbooleanIndicates whether the capability is allowed for the supporting entity.If a capability is allowed for a supporting entity but not for the parent legal entity, this means the legal entity has other supporting entities that failed verification.You can use the allowed supporting entityregardless of the verification status of other supporting entities.idstringSupporting entity referencerequestedbooleanIndicates whether the supporting entity capability is requested.verificationStatusstringThe status of the verification checks for the capability of the supporting entity.Possible values:pending: Adyen is running the verification.invalid: The verification failed. Check if theerrorsarray contains more information.valid: The verification has been successfully completed.rejected: Adyen has verified the information, but found reasons to not allow the capability.documentDetailsarray[object]List of documents uploaded for the transfer instrument.Show childrenHide childrenactivebooleanIdentifies whether the document is active and used for checks.descriptionstringYour description for the document.fileNamestringDocument name.idstringThe unique identifier of the resource.modificationDatestringThe modification date of the document.pagesarray[object]List of document pagesShow childrenHide childrenpageNamestringpageNumberintegertypestringtypestringType of document, used when providing an ID number or uploading a document.idstringThe unique identifier of the transfer instrument.legalEntityIdstringThe unique identifier of thelegal entitythat owns the transfer instrument.problemsarray[object]The verification errors related to capabilities for this transfer instrument.Show childrenHide childrenentityobjectShow childrenHide childrendocumentsarray[string]List of document IDs corresponding to the verification errors from capabilities.idstringownerobjectShow childrenHide childrendocumentsarray[string]List of document IDs corresponding to the verification errors from capabilities.idstringtypestringtypestringverificationErrorsarray[object]Show childrenHide childrencapabilitiesarray[string]Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing.The value is an object containing the settings for the capability.codestringThe general error code.messagestringThe general error message.remediatingActionsarray[object]An object containing possible solutions to fix a verification error.Show childrenHide childrencodestringmessagestringsubErrorsarray[object]An array containing more granular information about the cause of the verification error.Show childrenHide childrencapabilitiesarray[string]Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing.The value is an object containing the settings for the capability.codestringThe general error code.messagestringThe general error message.typestringThe type of error.Possible values:invalidInputdataMissingpendingStatusrejecteddataReviewremediatingActionsarray[object]An object containing possible solutions to fix a verification error.Show childrenHide childrencodestringmessagestringtypestringThe type of error.Possible values:invalidInputdataMissingpendingStatusrejecteddataReviewtypestringThe type of transfer instrument.Possible value:bankAccount.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- pending: Adyen is running the verification.
- invalid: The verification failed. Check if theerrorsarray contains more information.
- valid: The verification has been successfully completed.
- rejected: Adyen has verified the information, but found reasons to not allow the capability.
- invalidInput
- dataMissing
- pendingStatus
- rejected
- dataReview
- invalidInput
- dataMissing
- pendingStatus
- rejected
- dataReview

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error