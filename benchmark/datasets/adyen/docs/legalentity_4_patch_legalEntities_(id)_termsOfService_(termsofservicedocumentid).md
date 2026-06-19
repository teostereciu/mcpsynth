# legalentity/4/patch/legalEntities/(id)/termsOfService/(termsofservicedocumentid)

*Source: https://docs.adyen.com/api-explorer/legalentity/4/patch/legalEntities/(id)/termsOfService/(termsofservicedocumentid)*

---

# Accept Terms of Service
Accepts Terms of Service.
Requests to this endpoint are subject to rate limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.
The unique identifier of the Terms of Service document.
The unique identifier of the legal entity.
For sole proprietorships, this is the individual legal entity ID of the owner.
For organizations, this is the ID of the organization.
For legal representatives of individuals, this is the ID of the individual.
The legal entity ID of the user accepting the Terms of Service.
For organizations, this must be the individual legal entity ID of an authorized signatory for the organization.
For sole proprietorships, this must be the individual legal entity ID of the owner.
For individuals, this must be the individual legal entity id of either the individual, parent, or guardian.
The IP address of the user accepting the Terms of Service.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessacceptedBystringThe unique identifier of the user that accepted the Terms of Service.idstringThe unique identifier of the Terms of Service acceptance.ipAddressstringThe IP address of the user that accepted the Terms of Service.languagestringThe language used for the Terms of Service document, specified by the two-letterISO 639-1language code. Possible value:enfor English orfrfor French.Note that French is only available for some integration types in certain countries/regions. Reach out to your Adyen contact for more information.termsOfServiceDocumentIdstringThe unique identifier of the Terms of Service document.typestringThe type of Terms of Service.Possible values:adyenForPlatformsManageadyenIssuingadyenForPlatformsAdvancedadyenCapitaladyenAccountadyenCardadyenFranchiseeadyenPccradyenChargeCardkycOnInvite
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