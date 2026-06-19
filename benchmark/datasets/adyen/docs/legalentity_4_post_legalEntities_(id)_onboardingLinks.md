# legalentity/4/post/legalEntities/(id)/onboardingLinks

*Source: https://docs.adyen.com/api-explorer/legalentity/4/post/legalEntities/(id)/onboardingLinks*

---

# Get a link to an Adyen-hosted onboarding page
Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.
Requests to this endpoint are subject to rate limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.
The unique identifier of the legal entity
The language that will be used for the page, specified by a combination of two letterISO 639-1language andISO 3166-1 alpha-2country codes. See possible valuesformarketplacesorplatforms.
If not specified in the request or if the language is not supported, the page uses the browser language. If the browser language is not supported, the page usesen-USby default.
The URL where the user is redirected after they complete hosted onboarding.
Key-value pairs indicating the settings for the hosted onboarding page. The key represents a specific setting.
The list of countries the user can choose from in hosted onboarding wheneditPrefilledCountryis allowed.
The value must be in the two-characterISO 3166-1 alpha-2country code format.
The array is empty by default, allowing allcountries and regions supported by hosted onboarding.
Default value:false
Indicates if the user can select the format for their payout account (if applicable).
Default value:true
Indicates whether the debug user interface (UI) is enabled. The debug UI provides information for your support staff to diagnose and resolve user issues during onboarding. It can be accessed using a keyboard shortcut.
Default value:false
Indicates if the user can select a payout account in a different EU/EEA location (including Switzerland and the UK) than the location of their legal entity.
Default value:true
Indicates if the user can change their legal entity type.
Default value:true
Indicates if the user can change the country of their legal entity's address, for example the registered address of an organization.
Default value:false
Indicates if only users above the age of 18 can be onboarded.
Default value:true
Indicates whether the introduction screen is hidden for the user of the individual legal entity type.
The introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process.
Default value:true
Indicates whether the introduction screen is hidden for the user of the organization legal entity type.
The introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process.
Default value:true
Indicates whether the introduction screen is hidden for the user of the sole proprietorship legal entity type.
The introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process.
Default value:true
Indicates whether the introduction screen is hidden for the user of the trust legal entity type.
The introduction screen provides brief instructions for the subsequent steps in the hosted onboarding process.
Default value:true
Indicates if the user can initiate the verification process through open banking providers, like Plaid or Tink.
Default value:false
Indicates if the user is required to sign a PCI questionnaires for theecomMotosales channel type.
Default value:false
Indicates if the user is required to sign a PCI questionnaires for theeCommercesales channel type.
Default value:false
Indicates if the user is required to sign a PCI questionnaires for thepossales channel type.
Default value:false
Indicates if the user is required to sign a PCI questionnaires for theposMotosales channel type.
The maximum number of transfer instruments the user can create.
The unique identifier of the hosted onboarding theme.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessurlstringThe URL of the hosted onboarding page where you need to redirect your user. This URL:Expires after 4 minutes.Can only be used once.Can only be clicked once by the user.If the link expires, you need to create a new link.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- Expires after 4 minutes.
- Can only be used once.
- Can only be clicked once by the user.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error