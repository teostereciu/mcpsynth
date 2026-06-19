# Hop/6/post/getOnboardingUrl

*Source: https://docs.adyen.com/api-explorer/Hop/6/post/getOnboardingUrl*

---

# Get a link to a Adyen-hosted onboarding page
Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more information on how to use HOP, refer toHosted onboarding.
The account holder code you provided when you created the account holder.
Contains indicators whether the page should only collect information for specificKYC checks. By default, the page collects information for all KYC checks that apply to thelegal entity type.
Indicates whetherbank account detailsmust be collected. Default istrue.
Indicates whetherbusiness detailsmust be collected. Default istrue.
Indicates whetherindividual detailsmust be collected. Default istrue.
Indicates whetherlegal arrangement detailsmust be collected. Default istrue.
Indicates whether answers to aPCI questionnairemust be collected. Applies only to partner platforms. Default istrue.
Indicates whethershareholder detailsmust be collected. Defaults totrue.
Indicates if editing checks is allowed even if all the checks have passed.
The URL to which the account holder is redirected after completing an OAuth authentication with a bank through Trustly/PayMyBank.
The platform name which will show up in the welcome page.
The URL where the account holder will be redirected back to after they complete the onboarding, or if their session times out. Maximum length of 500 characters. If you don't provide this, the account holder will be redirected back to the default return URL configured in your platform account.
The language to be used in the page, specified by a combination of a language and country code. For example,pt-BR.
If not specified in the request or if the language is not supported, the page uses the browser language. If the browser language is not supported, the page usesen-USby default.
For a list of supported languages, refer toChange the page language.
Contains indicators whether specific pages must be shown to the account holder.
Indicates whether the page with bank account details must be shown. Defaults totrue.
Indicates whether the bank check instant verification' details must be shown. Defaults totrue.
Indicates whether the page with the company's or organization's details must be shown. Defaults totrue.
Indicates whether the checks overview page must be shown. Defaults tofalse.
Indicates whether the page with the individual's details must be shown. Defaults totrue.
Indicates whether the page with the legal arrangements' details must be shown. Defaults totrue.
Indicates whether the page to manually add bank account' details must be shown. Defaults totrue.
Indicates whether the page with the shareholders' details must be shown. Defaults totrue.
Indicates whether the welcome page must be shown. Defaults tofalse.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessinvalidFieldsarray[object]Information about any invalid fields.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.redirectUrlstringThe URL to the Hosted Onboarding Page where you should redirect your sub-merchant. This URL must be used within 30 seconds and can only be used once.resultCodestringThe result code.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error