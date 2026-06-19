# balanceplatform/2/patch/paymentInstruments/(id)

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/patch/paymentInstruments/(id)*

---

# Update a payment instrument
Updates a payment instrument. Once a payment instrument is already active, you can only update its status. However, for cards created withinactivestatus, you can still update the balance account associated with the card.
The unique identifier of the payment instrument.
The unique identifier of the balance account associated with this payment instrument.
You can only change the balance account ID if the payment instrument hasinactivestatus.
Object that contains information about the card payment instrument.
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
The two-letterISO-639-1language code of the card. For example,en.
The unique identifier of the logo image. This image is printed on the partial front of the card, for example, a logo on the upper right corner.
The letter on which the PIN of the card is printed.
This field overrides the PIN mailer design ID defined in the card configuration profile.
The logistics company that ships the card.
This field overrides the logistics company defined in the card configuration profile.
The delivery contact (name and address) for physical card delivery.
The address of the contact.
The name of the city.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The name of the street. Do not include the number of the building.
For example, if the address is Simon Carmiggeltstraat 6-50, provideSimon Carmiggeltstraat.
The number of the building.
For example, if the address is Simon Carmiggeltstraat 6-50, provide6-50.
Additional information about the delivery address.
The postal code.
Maximum length:
- 5 digits for an address in the US.
- 10 characters for an address in all other countries.
The state or province code, maximum 3 characters. For example,CAfor California in the US orONfor Ontario in Canada.
Required for the US and Canada.
The company name of the contact.
The email address of the contact.
The full phone number of the contact provided as a single string. It will be handled as a landline phone.Examples:"0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
The name of the contact.
The first name.
The last name.
The phone number of the contact.
The two-character ISO-3166-1 alpha-2 country code of the phone number.
For example,USorNL.
The phone number.
The inclusion of the phone number country code is not necessary.
The type of the phone number.
Possible values:Landline,Mobile,SIP,Fax.
The URL of the contact's website.
The form factor of the card.
Possible values:virtual,physical.
The 3DS configuration of the physical or the virtual card. Possible values:fullySupported,secureCorporate.
Reach out to your Adyen contact to get the values relevant for your integration.
Specifies how many times the card can be used. Possible values:singleUse,multiUse.
Reach out to your Adyen contact to determine the value relevant for your integration.
The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set toactiveby default. However, there can be exceptions for cards based on thecard.formFactorand theissuingCountryCode. For example, when issuing physical cards in the US, the default status isinactive.
Possible values:
- active:  The payment instrument is active and can be used to make payments.
- inactive: The payment instrument is inactive and cannot be used to make payments.
- suspended: The payment instrument is suspended, either because it was stolen or lost.
- closed: The payment instrument is permanently closed. This action cannot be undone.
Comment for the status of the payment instrument.
Required ifstatusReasonisother.
The reason for updating the status of the payment instrument.
Possible values:lost,stolen,damaged,suspectedFraud,expired,endOfLife,accountClosure,other.
If the reason isother, you must also send thestatusCommentparameter describing the status change.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessadditionalBankAccountIdentificationsarrayDeprecated in version 2Please usebankAccountobject insteadContains optional, additional business account details. Returned when you create a payment instrument withtypebankAccount.Select additionalBankAccountIdentificationsIbanAccountIdentificationbalanceAccountIdstringThe unique identifier of thebalance accountassociated with the payment instrument.bankAccountobjectContains the business account details. Returned when you create a payment instrument withtypebankAccount.Show childrenHide childrenaccountNumberstringThe bank account number, without separators or whitespace.accountTypestringThe bank account type.Possible values:checkingorsavings. Defaults tochecking.branchNumberstringThe bank account branch number, without separators or whitespaceformFactorstringBusiness accounts with aformFactorvalue ofphysicalare business accounts issued under the central bank of that country. The default value isphysicalfor NL, US, and UK business accounts.Adyen creates a local IBAN for business accounts when theformFactorvalue is set tovirtual. The local IBANs that are supported are for DE and FR, which reference a physical NL account, with funds being routed through the central bank of NL.ibanstringThe international bank account number as defined in theISO-13616standard.routingNumberstringTherouting number, without separators or whitespace.sortCodestringThesort code, without separators or whitespace.typestringibanorusLocalorukLocalcardobjectContains information about the card payment instrument. Returned when you create a payment instrument withtypecard.Show childrenHide childrenauthenticationobjectContains the card user's password and mobile phone number. This is required when you issue cards that can be used to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to3D Secure and digital walletsfor more information.Show childrenHide childrenemailstringThe email address where the one-time password (OTP) is sent.passwordstringMin length:1Max length:30The password used for 3D Secure password-based authentication. The value must be between 1 to 30 characters and must only contain the following supported characters.Characters betweena-z,A-Z, and0-9Special characters:äöüßÄÖÜ+-*/ç%()=?!~#'",;:$&àùòâôûáúóphoneobjectThe phone number where the one-time password (OTP) is sent.This object must have:Atypeset tomobile.Anumberwith a valid country code.Anumberwith more than 4 digits, excluding the country code.Make sure to verify that the card user owns the phone number.Show childrenHide childrennumberstringThe full phone number provided as a single string.
For example,"0031 6 11 22 33 44","+316/1122-3344",or"(0031) 611223344".typestringType of phone number.
Possible values:Landline,Mobile.binstringThe bank identification number (BIN) of the card number.brandstringThe brand of the physical or the virtual card.
Possible values:visa,mc.brandVariantstringThe brand variant of the physical or the virtual card. For example,visadebitormcprepaid.Reach out to your Adyen contact to get the values relevant for your integration.cardholderNamestringMax length:26The name of the cardholder.
Maximum length: 26 characters.configurationobjectContains information about the configuration profile for your cards. The configuration profile consists of settings required when creating a physical or a virtual card. You identify a configuration profile with itsconfigurationProfileId.When you provide this field in a request, you can override the settings of an existing configuration profile.Reach out to your Adyen contact to get the values that you can send in this object.Show childrenHide childrenactivationstringThe activation label attached to the card that contains the activation instructions.This field overrides the activation label design ID defined in the card configuration profile.activationUrlstringMax length:255Your app's URL, if you want to activate cards through your app. For example,my-app://ref1236a7d. A QR code is created based on this URL, and is included in the carrier. Before you use this field, reach out to your Adyen contact to set up the QR code process.Maximum length: 255 characters.bulkAddressobjectOverrides the shipment bulk address defined in the card configuration profile.Show childrenHide childrencitystringThe name of the city.companystringThe name of the company.countrystringThe two-character ISO-3166-1 alpha-2 country code. For example,US.emailstringThe email address.houseNumberOrNamestringThe house number or name.line1stringThe name of the street and the number of the building.For example:Simon Carmiggeltstraat 6-50.line2stringAdditional information about the delivery address. For example, an apartment number.line3stringAdditional information about the delivery address.mobilestringThe full telephone number.namestringThe recipient’s name (person or contact), for example ‘John Doe’.postalCodestringThe postal code.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe two-letter ISO 3166-2 state or province code.Maximum length: 2 characters for addresses in the US.streetstringThe streetname of the house.cardImageIdstringThe unique identifier of the card image. This image is printed on the full front of the card.carrierstringThe letter or packaging to which the card is attached.This field overrides the carrier design ID defined in the card configuration profile.carrierImageIdstringThe unique identifier of the carrier image. This image is printed on the letter to which the card is attached.configurationProfileIdstringThe unique identifier of the card configuration profile that contains the settings that are applied to the card. For example, the envelope and PIN mailer designs or the logistics company handling the shipment.You can override some of the existing settings in the configuration profile by providing the corresponding fields in theconfigurationobject. For example, send theshipmentMethodto override the logistics company defined in the card configuration profile.currencystringThe three-letterISO-4217currency code of the card. For example,EUR.This field overrides the existing currency setting on the card configuration profile.envelopestringOverrides the envelope design ID defined in the card configuration profile.insertstringAny additional material, such as marketing material, that is shipped together with the card.This field overrides the insert design ID defined in the card configuration profile.languagestringThe two-letterISO-639-1language code of the card. For example,en.logoImageIdstringThe unique identifier of the logo image. This image is printed on the partial front of the card, for example, a logo on the upper right corner.pinMailerstringThe letter on which the PIN of the card is printed.This field overrides the PIN mailer design ID defined in the card configuration profile.shipmentMethodstringThe logistics company that ships the card.This field overrides the logistics company defined in the card configuration profile.cvcstringThe CVC2 value of the card.The CVC2 is not sent by default. This is only returned in thePOSTresponse for single-use virtual cards.deliveryContactobjectThe delivery contact (name and address) for physical card delivery.Show childrenHide childrenaddressobjectThe address of the contact.Show childrenHide childrencitystringThe name of the city.countrystringThe two-character ISO-3166-1 alpha-2 country code. For example,US.If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.line1stringThe name of the street. Do not include the number of the building.For example, if the address is Simon Carmiggeltstraat 6-50, provideSimon Carmiggeltstraat.line2stringThe number of the building.For example, if the address is Simon Carmiggeltstraat 6-50, provide6-50.line3stringAdditional information about the delivery address.postalCodestringThe postal code.
Maximum length:5 digits for an address in the US.10 characters for an address in all other countries.stateOrProvincestringThe state or province code, maximum 3 characters. For example,CAfor California in the US orONfor Ontario in Canada.Required for the US and Canada.companystringThe company name of the contact.emailstringThe email address of the contact.fullPhoneNumberstringThe full phone number of the contact provided as a single string. It will be handled as a landline phone.Examples:"0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"nameobjectThe name of the contact.Show childrenHide childrenfirstNamestringMax length:80The first name.lastNamestringMax length:80The last name.phoneNumberobjectThe phone number of the contact.Show childrenHide childrenphoneCountryCodestringThe two-character ISO-3166-1 alpha-2 country code of the phone number.
For example,USorNL.phoneNumberstringThe phone number.
The inclusion of the phone number country code is not necessary.phoneTypestringThe type of the phone number.
Possible values:Landline,Mobile,SIP,Fax.webAddressstringThe URL of the contact's website.expirationobjectThe expiration date of the card.Show childrenHide childrenmonthstringThe month in which the card will expire.yearstringThe year in which the card will expire.formFactorstringThe form factor of the card.
Possible values:virtual,physical.lastFourstringLast last four digits of the card number.numberstringThe primary account number (PAN) of the card.The PAN is masked by default and returned only for single-use virtual cards.threeDSecurestringThe 3DS configuration of the physical or the virtual card. Possible values:fullySupported,secureCorporate.Reach out to your Adyen contact to get the values relevant for your integration.usagestringSpecifies how many times the card can be used. Possible values:singleUse,multiUse.Reach out to your Adyen contact to determine the value relevant for your integration.descriptionstringMax length:300Your description for the payment instrument, maximum 300 characters.idstringThe unique identifier of the payment instrument.issuingCountryCodestringThe two-characterISO 3166-1 alpha-2country code where the payment instrument is issued. For example,NLorUS.paymentInstrumentGroupIdstringThe unique identifier of thepayment instrument groupto which the payment instrument belongs.referencestringMax length:150Your reference for the payment instrument, maximum 150 characters.replacedByIdstringThe unique identifier of the payment instrument that replaced this payment instrument.replacementOfIdstringThe unique identifier of the payment instrument that is replaced by this payment instrument.statusstringThe status of the payment instrument. If a status is not specified when creating a payment instrument, it is set toactiveby default. However, there can be exceptions for cards based on thecard.formFactorand theissuingCountryCode. For example, when issuing physical cards in the US, the default status isinactive.Possible values:active:  The payment instrument is active and can be used to make payments.inactive: The payment instrument is inactive and cannot be used to make payments.suspended: The payment instrument is suspended, either because it was stolen or lost.closed: The payment instrument is permanently closed. This action cannot be undone.statusCommentstringComment for the status of the payment instrument.Required ifstatusReasonisother.statusReasonstringThe reason for the status of the payment instrument.Possible values:accountClosure,damaged,endOfLife,expired,lost,stolen,suspectedFraud,transactionRule,other.
If the reason isother, you must also send thestatusCommentparameter describing the status change.typestringThe type of payment instrument.Possible values:card,bankAccount.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- Characters betweena-z,A-Z, and0-9
- Special characters:äöüßÄÖÜ+-*/ç%()=?!~#'",;:$&àùòâôûáúó
- Atypeset tomobile.
- Anumberwith a valid country code.
- Anumberwith more than 4 digits, excluding the country code.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 5 digits for an address in the US.
- 10 characters for an address in all other countries.
- active:  The payment instrument is active and can be used to make payments.
- inactive: The payment instrument is inactive and cannot be used to make payments.
- suspended: The payment instrument is suspended, either because it was stolen or lost.
- closed: The payment instrument is permanently closed. This action cannot be undone.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error