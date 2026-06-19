# legalentity/4/post/legalEntities/(id)/termsOfService

*Source: https://docs.adyen.com/api-explorer/legalentity/4/post/legalEntities/(id)/termsOfService*

---

# Get Terms of Service document
Returns the Terms of Service document for a legal entity.
Requests to this endpoint are subject to rate limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.
The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. For organizations, this is the ID of the organization.
The language to be used for the Terms of Service document, specified by the two-letterISO 639-1language code. Possible values:enfor English orfrfor French.
The requested format for the Terms of Service document. Default value: JSON. Possible values:JSON,PDF, orTXT.
The type of Terms of Service.
Possible values:
- adyenForPlatformsManage
- adyenIssuing
- adyenForPlatformsAdvanced
- adyenCapital
- adyenAccount
- adyenCard
- adyenFranchisee
- adyenPccr
- adyenChargeCard
- kycOnInvite
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdocumentstringThe Terms of Service document in Base64-encoded format.idstringThe unique identifier of the legal entity.languagestringThe language used for the Terms of Service document, specified by the two-letterISO 639-1language code. Possible value:enfor English orfrfor French.Note that French is only available for some integration types in certain countries/regions. Reach out to your Adyen contact for more information.termsOfServiceDocumentFormatstringThe format of the Terms of Service document.termsOfServiceDocumentIdstringThe unique identifier of the Terms of Service document.typestringThe type of Terms of Service.Possible values:adyenForPlatformsManageadyenIssuingadyenForPlatformsAdvancedadyenCapitaladyenAccountadyenCardadyenFranchiseeadyenPccradyenChargeCardkycOnInvite
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- adyenForPlatformsManage
- adyenIssuing
- adyenForPlatformsAdvanced
- adyenCapital
- adyenAccount
- adyenCard
- adyenFranchisee
- adyenPccr
- adyenChargeCard
- kycOnInvite

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error