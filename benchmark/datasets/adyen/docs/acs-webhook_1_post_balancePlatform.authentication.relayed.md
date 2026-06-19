# acs-webhook/1/post/balancePlatform.authentication.relayed

*Source: https://docs.adyen.com/api-explorer/acs-webhook/1/post/balancePlatform.authentication.relayed*

---

# Out-of-band authentication requested
Adyen sends this webhook when a cardholder must performout-of-band authentication.
To complete the authentication process, respond to this webhook with anHTTP 200response. Include theauthenticationDecisionin the response body.
If we do not receive the response within two seconds, the authentication process stops.
The environment from which the webhook originated.
Possible values:test,live.
The unique identifier of the challenge.
The unique identifier of thepayment instrumentused for the purchase.
The details of the purchase.
The time of the purchase.
The name of the merchant.
The amount of the purchase in the original currency.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
URL for auto-switching to the threeDS Requestor App. If not present, the threeDS Requestor App doesn't support auto-switching.
When the event was queued.
Type of notification.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessauthenticationDecisionobjectThe decision regarding the authentication.Show childrenHide childrenstatusstringThe status of the authentication.Possible values:refusedproceedFor more information, refer toAuthenticate cardholders using the Authentication SDK.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- refused
- proceed

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error