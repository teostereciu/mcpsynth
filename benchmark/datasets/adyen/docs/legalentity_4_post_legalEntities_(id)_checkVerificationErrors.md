# legalentity/4/post/legalEntities/(id)/checkVerificationErrors

*Source: https://docs.adyen.com/api-explorer/legalentity/4/post/legalEntities/(id)/checkVerificationErrors*

---

# Check a legal entity's verification errors
Returns the verification errors for a legal entity and its supporting entities.
Requests to this endpoint are subject to rate limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.
The unique identifier of the legal entity.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessproblemsarray[object]List of the verification errors.Show childrenHide childrenentityobjectShow childrenHide childrendocumentsarray[string]List of document IDs corresponding to the verification errors from capabilities.idstringownerobjectShow childrenHide childrendocumentsarray[string]List of document IDs corresponding to the verification errors from capabilities.idstringtypestringtypestringverificationErrorsarray[object]Show childrenHide childrencapabilitiesarray[string]Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing.The value is an object containing the settings for the capability.codestringThe general error code.messagestringThe general error message.remediatingActionsarray[object]An object containing possible solutions to fix a verification error.Show childrenHide childrencodestringmessagestringsubErrorsarray[object]An array containing more granular information about the cause of the verification error.Show childrenHide childrencapabilitiesarray[string]Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing.The value is an object containing the settings for the capability.codestringThe general error code.messagestringThe general error message.typestringThe type of error.Possible values:invalidInputdataMissingpendingStatusrejecteddataReviewremediatingActionsarray[object]An object containing possible solutions to fix a verification error.Show childrenHide childrencodestringmessagestringtypestringThe type of error.Possible values:invalidInputdataMissingpendingStatusrejecteddataReview
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
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