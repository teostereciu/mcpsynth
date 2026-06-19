# Checkout/71/post/donationCampaigns

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/donationCampaigns*

---

# Get a list of donation campaigns
Queries the available donation campaigns for a donation based on the donation context (like merchant account, currency, and locale). The response contains active donation campaigns.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
The three-characterISO currency code.
Locale on the shopper interaction device.
Your merchant account identifier.
Required for Adyen for Platforms integrations if you are a platform model. This is yourreference(onbalance platform) or thestoreReference(in theclassic integration) for the ecommerce or point-of-sale store that is processing the payment.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdonationCampaignsarray[object]List of active donation campaigns for your merchant account.Show childrenHide childrenamountsobjectThe object that contains the fixed donation amounts that the shopper can select from.Show childrenHide childrencurrencystringThe three-characterISO currency code.valuesarray[integer]The amounts of the donation (inminor units).bannerUrlstringThe URL for the banner of the nonprofit or campaign.campaignNamestringThe name of the donation campaign..causeNamestringThe cause of the nonprofit.donationobjectThe object that contains the details of the donation.Show childrenHide childrencurrencystringThe three-characterISO currency code.donationTypestringThetype of donation.Possible values:roundup: a donation where the original transaction amount is rounded up as a donation.fixedAmounts: a donation where you show fixed donations amounts that the shopper can select from.maxRoundupAmountintegerThe maximum amount a transaction can be rounded up to make a donation. This field is only present whendonationTypeisroundup.typestringThetype of donation.Possible values:roundup: a donation where the original transaction amount is rounded up as a donation.fixedAmounts: a donation where you show fixed donation amounts that the shopper can select from.valuesarray[integer]The fixed donation amounts inminor units. This field is only present whendonationTypeisfixedAmounts.idstringThe unique campaign ID of the donation campaign.logoUrlstringThe URL for the logo of the nonprofit.nonprofitDescriptionstringThe description of the nonprofit.nonprofitNamestringThe name of the nonprofit organization that receives the donation.nonprofitUrlstringThe website URL of the nonprofit.termsAndConditionsUrlstringThe URL of the terms and conditions page of the nonprofit and the campaign.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- roundup: a donation where the original transaction amount is rounded up as a donation.
- fixedAmounts: a donation where you show fixed donations amounts that the shopper can select from.
- roundup: a donation where the original transaction amount is rounded up as a donation.
- fixedAmounts: a donation where you show fixed donation amounts that the shopper can select from.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error