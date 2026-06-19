# relayed-authorisation-webhooks/4/post/balancePlatform.authorisation.relayed

*Source: https://docs.adyen.com/api-explorer/relayed-authorisation-webhooks/4/post/balancePlatform.authorisation.relayed*

---

# Relayed authorization requested
Adyen sends this webhook to allow you to providerelayed authorizationfor a transaction.
To complete a relayed authorization, respond to this webhook with anHTTP 200response. Include theauthorisationDecisionin the response body.
If we do not receive the response within two seconds, we apply yourfallback logic.
The reference of the account holder.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The amount of the transaction.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The amount adjustments in the transaction.
The adjustment amount.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The type of markup that is applied to an authorised payment.
Possible values:exchange,forexMarkup,authHoldReserve,atmMarkup.
The basepoints associated with the applied markup.
The specific amount of the adjustment.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The minimum amount of the adjustment.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The maximum amount of the adjustment.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The authorization code for the payment.
The decision of the authorization.
The reason of the authorization decision.
The status of the authorization decision. Possible values:AuthorisedorRefused.
The code of the authorization decision.
The authorization type.
Possible values:
- finalAuthorisation
- preAuthorisation
- defaultAuthorisation
The reference of the balance account.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The list of balance mutations per event.
The balance amount after the mutation.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The balance amount before the mutation.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The three-characterISO currency code.
The amount of the mutation.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The type of the mutation.
The unique identifier of the balance platform.
The entry mode of the information of the payment instrument. For example:contactless,chip,magstripe.
The environment from which the webhook originated.
Possible values:test,live.
The unique identifier of the transfer.
The information about the merchant.
The unique identifier of the merchant's acquirer.
The merchant category code.
The unique identifier of the merchant.
Contains the name and location of the merchant.
The city where the merchant is located.
The country where the merchant is located inthree-letter country codeformat.
The home country inthree-digit country codeformat, used for government-controlled merchants such as embassies.
The name of the merchant's shop or service.
The raw data.
The state where the merchant is located.
The postal code of the merchant.
The amount in the original currency.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Contains information about the payment instrument.
Please usebankAccountobject instead
Contains optional, additional business account details. Returned when you create a payment instrument withtypebankAccount.
The unique identifier of thebalance accountassociated with the payment instrument.
Contains the business account details. Returned when you create a payment instrument withtypebankAccount.
The bank account number, without separators or whitespace.
The bank account type.
Possible values:checkingorsavings. Defaults tochecking.
The bank account branch number, without separators or whitespace
Business accounts with aformFactorvalue ofphysicalare business accounts issued under the central bank of that country. The default value isphysicalfor NL, US, and UK business accounts.
Adyen creates a local IBAN for business accounts when theformFactorvalue is set tovirtual. The local IBANs that are supported are for DE and FR, which reference a physical NL account, with funds being routed through the central bank of NL.
The international bank account number as defined in theISO-13616standard.
Therouting number, without separators or whitespace.
Thesort code, without separators or whitespace.
ibanorusLocalorukLocal
Contains information about the card payment instrument. Returned when you create a payment instrument withtypecard.
Contains the card user's password and mobile phone number. This is required when you issue cards that can be used to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to3D Secure and digital walletsfor more information.
The email address where the one-time password (OTP) is sent.
The password used for 3D Secure password-based authentication. The value must be between 1 to 30 characters and must only contain the following supported characters.
- Characters betweena-z,A-Z, and0-9
- Special characters:äöüßÄÖÜ+-*/ç%()=?!~#'",;:$&àùòâôûáúó
The phone number where the one-time password (OTP) is sent.
This object must have:
- Atypeset tomobile.
- Anumberwith a valid country code.
- Anumberwith more than 4 digits, excluding the country code.
Make sure to verify that the card user owns the phone number.
The full phone number provided as a single string.
For example,"0031 6 11 22 33 44","+316/1122-3344",
or"(0031) 611223344".
Type of phone number.
Possible values:Landline,Mobile.
The bank identification number (BIN) of the card number.
The brand of the physical or the virtual card.
Possible values:visa,mc.
The brand variant of the physical or the virtual card. For example,visadebitormcprepaid.
Reach out to your Adyen contact to get the values relevant for your integration.
The name of the cardholder.
Maximum length: 26 characters.
Contains information about the configuration profile for your cards. The configuration profile consists of settings required when creating a physical or a virtual card. You identify a configuration profile with itsconfigurationProfileId.
When you provide this field in a request, you can override the settings of an existing configuration profile.
Reach out to your Adyen contact to get the values that you can send in this object.
The activation label attached to the card that contains the activation instructions.
This field overrides the activation label design ID defined in the card configuration profile.
Your app's URL, if you want to activate cards through your app. For example,my-app://ref1236a7d. A QR code is created based on this URL, and is included in the carrier. Before you use this field, reach out to your Adyen contact to set up the QR code process.
Maximum length: 255 characters.
Overrides the shipment bulk address defined in the card configuration profile.
The name of the city.
The name of the company.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
The email address.
The house number or name.
The name of the street and the number of the building.
For example:Simon Carmiggeltstraat 6-50.
Additional information about the delivery address. For example, an apartment number.
Additional information about the delivery address.
The full telephone number.
The recipient’s name (person or contact), for example ‘John Doe’.
The postal code.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The two-letter ISO 3166-2 state or province code.
Maximum length: 2 characters for addresses in the US.
The streetname of the house.
The unique identifier of the card image. This image is printed on the full front of the card.
The letter or packaging to which the card is attached.
This field overrides the carrier design ID defined in the card configuration profile.
The unique identifier of the carrier image. This image is printed on the letter to which the card is attached.
The unique identifier of the card configuration profile that contains the settings that are applied to the card. For example, the envelope and PIN mailer designs or the logistics company handling the shipment.
You can override some of the existing settings in the configuration profile by providing the corresponding fields in theconfigurationobject. For example, send theshipmentMethodto override the logistics company defined in the card configuration profile.
The three-letterISO-4217currency code of the card. For example,EUR.
This field overrides the existing currency setting on the card configuration profile.
Overrides the envelope design ID defined in the card configuration profile.
Any additional material, such as marketing material, that is shipped together with the card.
This field overrides the insert design ID defined in the card configuration profile.
A list of two-letterISO-639-1language codes of the card. For example,[en,es].
The unique identifier of the logo image. This image is printed on the partial front of the card, for example, a logo on the upper right corner.
The letter on which the PIN of the card is printed.
This field overrides the PIN mailer design ID defined in the card configuration profile.
The logistics company that ships the card.
This field overrides the logistics company defined in the card configuration profile.
The CVC2 value of the card.
The CVC2 is not sent by default. This is only returned in thePOSTresponse for single-use virtual cards.
The delivery contact (name and address) for physical card delivery.
The address of the contact.
The name of the city.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The name of the street and the number of the building.
For example:Simon Carmiggeltstraat 6-50.
Additional information about the delivery address. For example, an apartment number.
Additional information about the delivery address.
The postal code.
Maximum length:
- 5 digits for an address in the US.
- 10 characters for an address in all other countries.
The state or province code, maximum 3 characters. For example,CAfor California in the US orONfor Ontario in Canada.
Required for the US and Canada.
The company name of the contact.
The email address of the contact.
The name of the contact.
The first name.
The last name.
The phone of the contact.
The full phone number provided as a single string.
For example,"0031 6 11 22 33 44","+316/1122-3344",
or"(0031) 611223344".
Type of phone number.
Possible values:Landline,Mobile.
The URL of the contact's website.
The expiration date of the card.
The month in which the card will expire.
The year in which the card will expire.
The form factor of the card.
Possible values:virtual,physical.
Last last four digits of the card number.
The primary account number (PAN) of the card.
The PAN is masked by default and returned only for single-use virtual cards.
The 3DS configuration of the physical or the virtual card. Possible values:fullySupported,secureCorporate.
Reach out to your Adyen contact to get the values relevant for your integration.
Specifies how many times the card can be used. Possible values:singleUse,multiUse.
Reach out to your Adyen contact to determine the value relevant for your integration.
Your description for the payment instrument, maximum 300 characters.
The unique identifier of the payment instrument.
The two-characterISO 3166-1 alpha-2country code where the payment instrument is issued. For example,NLorUS.
The unique identifier of thepayment instrument groupto which the payment instrument belongs.
Your reference for the payment instrument, maximum 150 characters.
The unique identifier of the payment instrument that replaced this payment instrument.
The unique identifier of the payment instrument that is replaced by this payment instrument.
The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set toactiveby default. However, there can be exceptions for cards based on thecard.formFactorand theissuingCountryCode. For example, when issuing physical cards in the US, the default status isinactive.
Possible values:
- active:  The payment instrument is active and can be used to make payments.
- inactive: The payment instrument is inactive and cannot be used to make payments.
- suspended: The payment instrument is suspended, either because it was stolen or lost.
- closed: The payment instrument is permanently closed. This action cannot be undone.
The status comment provides additional information for the statusReason of the payment instrument.
The reason for the status of the payment instrument.
Possible values:accountClosure,damaged,endOfLife,expired,lost,stolen,suspectedFraud,transactionRule,other.
If the reason isother, you must also send thestatusCommentparameter describing the status change.
The type of payment instrument.
Possible values:card,bankAccount.
The processing type used for this payment. For example:ecommerce,pos,moto.
The reference of the payment.
The risk score provided by the card schemes.
The identifier of the original payment. This ID is provided by the scheme and can be alphanumeric or numeric, depending on the scheme.
The unique identifier created by the scheme. This ID can be alphanumeric or numeric depending on the scheme.
The list of transaction scores.
The type of score.
The value of the score.
The data of the result from the 3DS authentication.
The transaction identifier for the Access Control Server
The result from the performed authentication
The type of the performed authentication
The transaction identifier for the Directory server
Contains the results of the evaluation of the transaction rules.
The advice given by the Risk analysis.
Indicates whether the transaction passed the evaluation for all hardblock rules
The score of the Risk analysis.
Array containing all the transaction rules that the transaction triggered.
An explanation about why the transaction rule failed.
Contains information about the transaction rule.
The description of the resource.
The unique identifier of the resource.
The outcome type of the rule.
The reference for the resource.
The transaction score determined by the rule. Returned only whenoutcomeTypeisscoreBased.
Contains information about the resource to which the transaction rule applies.
ID of the resource, when applicable.
Indicates the type of resource for which the transaction rule is defined.
Possible values:
- PaymentInstrumentGroup
- PaymentInstrument
- BalancePlatform
- EntityUsageConfiguration
- PlatformRule: The transaction rule is a platform-wide rule imposed by Adyen.
Type of notification.
Contains the checks that Adyen performed to validate the payment and the result of each.
The result of the check.
Possible values:
- valid: The validation was successful.
- invalid: The validation failed.
- notValidated: The validation was not performed because some services were unreachable or Adyen does not have the information needed to perform the check.
- notApplicable: The validation is not applicable.
Type of check.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessauthorisationDecisionobjectObject representing the authorization decision.Show childrenHide childrenrefusalReasonstringThe reason for refusing the authorization.statusstringThe status of the authorization.Possible values:AuthorisedRefusedFor more information, refer toUse relayed authorization.metadataobjectObject that contains key-value pairs that you can use in your reporting or other business process.referencestringReference of the payment.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- Authorised
- Refused

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error