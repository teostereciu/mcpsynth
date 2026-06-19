# Toll-free verification resource

*Source: https://www.twilio.com/docs/messaging/api/tollfree-verification-resource*

---

# Toll-free verification resource

Positive FeedbackNegative Feedback

* * *

The **Verification** resource records your request to verify a toll-free number to comply with US and Canadian federal regulations for SMS messaging. The verification process is called toll-free verification (TFV).

Toll-free phone numbers for the US and Canada use the North American Numbering Plan (NANP). NANP toll-free numbers begin with 800, 888, 877, 866, 855, 844, or 833. To use these numbers to send SMS messages, your organization must comply with federal regulations. For the toll-free number to be compliant, provide data on how you plan to use your phone number to send texts.

To verify that a toll-free number meets these regulations, use this resource. To learn how to use this resource, see [Get started with toll-free verification using the API](/docs/messaging/compliance/toll-free/api-onboarding "Get started with toll-free verification using the API").

* * *

## Verification Properties

verification-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<HH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string to identify Tollfree Verification.

Pattern: `^HH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Tollfree Verification resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

customerProfileSidSID<BU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Customer's Profile Bundle BundleSid.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

trustProductSidSID<BU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Tollfree TrustProduct Bundle BundleSid.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

regulatedItemSidSID<RA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Regulated Item.

Pattern: `^RA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

businessNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the business or organization using the Tollfree number.

* * *

businessStreetAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the business or organization using the Tollfree number.

* * *

businessStreetAddress2string

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the business or organization using the Tollfree number.

* * *

businessCitystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The city of the business or organization using the Tollfree number.

* * *

businessStateProvinceRegionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The state/province/region of the business or organization using the Tollfree number.

* * *

businessPostalCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The postal code of the business or organization using the Tollfree number.

* * *

businessCountrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The country of the business or organization using the Tollfree number.

* * *

businessWebsitestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The website of the business or organization using the Tollfree number.

* * *

businessContactFirstNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The first name of the contact for the business or organization using the Tollfree number.

* * *

businessContactLastNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The last name of the contact for the business or organization using the Tollfree number.

* * *

businessContactEmailstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The email address of the contact for the business or organization using the Tollfree number.

* * *

businessContactPhonestring<phone-number>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.

* * *

notificationEmailstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The email address to receive the notification about the verification result. .

* * *

useCaseCategoriesarray[enum<string>]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The category of the use case for the Tollfree Number. List as many as are applicable.

Possible values:

`TWO_FACTOR_AUTHENTICATION``ACCOUNT_NOTIFICATIONS``CUSTOMER_CARE``CHARITY_NONPROFIT``DELIVERY_NOTIFICATIONS``FRAUD_ALERT_MESSAGING``EVENTS``HIGHER_EDUCATION``K12``MARKETING`Show 4 more

* * *

useCaseSummarystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Use this to further explain how messaging is used by the business or organization.

* * *

productionMessageSamplestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An example of message content, i.e. a sample message.

* * *

optInImageUrlsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.

* * *

optInTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Describe how a user opts-in to text messages.

Possible values:

`VERBAL``WEB_FORM``PAPER_FORM``VIA_TEXT``MOBILE_QR_CODE``IMPORT``IMPORT_PLEASE_REPLACE`

* * *

messageVolumestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Estimate monthly volume of messages from the Tollfree Number.

* * *

additionalInformationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Additional information to be provided for verification.

* * *

tollfreePhoneNumberSidSID<PN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Phone Number associated with the Tollfree Verification.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

tollfreePhoneNumberstring<phone-number>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The E.164 formatted toll-free phone number associated with the verification.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The compliance status of the Tollfree Verification record.

Possible values:

`PENDING_REVIEW``IN_REVIEW``TWILIO_APPROVED``TWILIO_REJECTED`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the Tollfree Verification resource.

* * *

rejectionReasonstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The rejection reason given when a Tollfree Verification has been rejected.

* * *

errorCodeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The error code given when a Tollfree Verification has been rejected.

* * *

editExpirationstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time when the ability to edit a rejected verification expires.

* * *

editAllowedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

If a rejected verification is allowed to be edited/resubmitted. Some rejection reasons allow editing and some do not.

* * *

businessRegistrationNumberstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A legally recognized business registration number

* * *

businessRegistrationAuthorityenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The organizational authority for business registrations. Required for all business types except SOLE_PROPRIETOR.

Possible values:

`EIN``CBN``CRN``PROVINCIAL_NUMBER``VAT``ACN``ABN``BRN``SIREN``SIRET`Show 8 more

* * *

businessRegistrationCountrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Country business is registered in

* * *

businessTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT, SOLE_PROPRIETOR, GOVERNMENT. Required field.

Possible values:

`PRIVATE_PROFIT``PUBLIC_PROFIT``SOLE_PROPRIETOR``NON_PROFIT``GOVERNMENT`

* * *

businessRegistrationPhoneNumberstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The E.164 formatted number associated with the business.

* * *

doingBusinessAsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Trade name, sub entity, or downstream business name of business being submitted for verification

* * *

optInConfirmationMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The confirmation message sent to users when they opt in to receive messages.

* * *

helpMessageSamplestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A sample help message provided to users.

* * *

privacyPolicyUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL to the privacy policy for the business or organization.

* * *

termsAndConditionsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of the terms and conditions for the business or organization.

* * *

ageGatedContentboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates if the content is age gated.

* * *

optInKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

List of keywords that users can send to opt in or out of messages.

* * *

rejectionReasonsarray

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of rejection reasons and codes describing why a Tollfree Verification has been rejected.

* * *

resourceLinks

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URLs of the documents associated with the Tollfree Verification resource.

* * *

externalReferenceIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An optional external reference ID supplied by customer and echoed back on status retrieval.

* * *

vettingIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Max length: `500`

* * *

vettingProviderenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The third-party political vetting provider.

Possible values:

`CAMPAIGN_VERIFY`

* * *

vettingIdExpirationstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

### Allowed enum values

allowed-enum-values page anchor

Positive FeedbackNegative Feedback

The following tables list the allowed values for enum fields used in TFV requests.

#### UseCaseCategories

usecasecategories page anchor

An array field. List as many categories as applicable.

Value| Description
---|---
`TWO_FACTOR_AUTHENTICATION`| Two-factor authentication
`ACCOUNT_NOTIFICATIONS`| Account notifications
`CUSTOMER_CARE`| Customer care
`CHARITY_NONPROFIT`| Charity / nonprofit
`DELIVERY_NOTIFICATIONS`| Delivery notifications
`FRAUD_ALERT_MESSAGING`| Fraud alert messaging
`EVENTS`| Events
`HIGHER_EDUCATION`| Higher education
`K12`| K-12 education
`MARKETING`| Marketing
`POLLING_AND_VOTING_NON_POLITICAL`| Polling and voting (non-political)
`POLITICAL_ELECTION_CAMPAIGNS`| Political election campaigns
`PUBLIC_SERVICE_ANNOUNCEMENT`| Public service announcement
`SECURITY_ALERT`| Security alert

#### BusinessRegistrationAuthority

businessregistrationauthority page anchor

Value| Description
---|---
`EIN`| Employer Identification Number (US)
`CBN`| Canadian Business Number (Canada)
`CRN`| Company Registration Number
`PROVINCIAL_NUMBER`| Provincial Number (Canada)
`VAT`| Value Added Tax Number
`ACN`| Australian Company Number
`ABN`| Australian Business Number
`BRN`| Business Registration Number (Hong Kong)
`SIREN`| Systeme d'Identification du Repertoire des Entreprises (France)
`SIRET`| Systeme d'Identification du Repertoire des Etablissements (France)
`NZBN`| New Zealand Business Number
`USt-IdNr`| Umsatzsteuer-Identifikationsnummer (Germany)
`CIF`| Certificado de Identificacion Fiscal (Spain)
`NIF`| Numero de Identificacion Fiscal (Spain/Portugal)
`CNPJ`| Cadastro Nacional da Pessoa Juridica (Brazil)
`UID`| Unternehmens-Identifikationsnummer (Switzerland/Austria)
`NEQ`| Numero d'entreprise du Quebec (Quebec, Canada)
`OTHER`| Other

#### MessageVolume

messagevolume page anchor

Estimated monthly volume of messages.

Value
---
`10`
`100`
`1,000`
`10,000`
`100,000`
`250,000`
`500,000`
`750,000`
`1,000,000`
`5,000,000`
`10,000,000+`

* * *

## Submit a TFV request

submit-a-tfv-request page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/Tollfree/Verifications`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

businessNamestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the business or organization using the Tollfree number.

* * *

businessWebsitestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The website of the business or organization using the Tollfree number.

* * *

notificationEmailstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The email address to receive the notification about the verification result. .

* * *

useCaseCategoriesarray[enum<string>]

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The category of the use case for the Tollfree Number. List as many as are applicable.

Possible values:

`TWO_FACTOR_AUTHENTICATION``ACCOUNT_NOTIFICATIONS``CUSTOMER_CARE``CHARITY_NONPROFIT``DELIVERY_NOTIFICATIONS``FRAUD_ALERT_MESSAGING``EVENTS``HIGHER_EDUCATION``K12``MARKETING`Show 4 more

* * *

useCaseSummarystring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Use this to further explain how messaging is used by the business or organization.

* * *

productionMessageSamplestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An example of message content, i.e. a sample message.

* * *

optInImageUrlsarray[string]

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.

* * *

optInTypeenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Describe how a user opts-in to text messages.

Possible values:

`VERBAL``WEB_FORM``PAPER_FORM``VIA_TEXT``MOBILE_QR_CODE``IMPORT``IMPORT_PLEASE_REPLACE`

* * *

messageVolumestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Estimate monthly volume of messages from the Tollfree Number.

* * *

tollfreePhoneNumberSidSID<PN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Phone Number associated with the Tollfree Verification.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

customerProfileSidSID<BU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Customer's Profile Bundle BundleSid.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

businessStreetAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the business or organization using the Tollfree number.

* * *

businessStreetAddress2string

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the business or organization using the Tollfree number.

* * *

businessCitystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The city of the business or organization using the Tollfree number.

* * *

businessStateProvinceRegionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The state/province/region of the business or organization using the Tollfree number.

* * *

businessPostalCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The postal code of the business or organization using the Tollfree number.

* * *

businessCountrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The country of the business or organization using the Tollfree number.

* * *

additionalInformationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Additional information to be provided for verification.

* * *

businessContactFirstNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The first name of the contact for the business or organization using the Tollfree number.

* * *

businessContactLastNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The last name of the contact for the business or organization using the Tollfree number.

* * *

businessContactEmailstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The email address of the contact for the business or organization using the Tollfree number.

* * *

businessContactPhonestring<phone-number>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.

* * *

externalReferenceIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An optional external reference ID supplied by customer and echoed back on status retrieval.

* * *

businessRegistrationNumberstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A legally recognized business registration number. Required for all business types except SOLE_PROPRIETOR.

* * *

businessRegistrationAuthorityenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The organizational authority for business registrations. Required for all business types except SOLE_PROPRIETOR.

Possible values:

`EIN``CBN``CRN``PROVINCIAL_NUMBER``VAT``ACN``ABN``BRN``SIREN``SIRET`Show 8 more

* * *

businessRegistrationCountrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The country where the business is registered. Required for all business types except SOLE_PROPRIETOR.

* * *

businessTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT, SOLE_PROPRIETOR, GOVERNMENT. Required field.

Possible values:

`PRIVATE_PROFIT``PUBLIC_PROFIT``SOLE_PROPRIETOR``NON_PROFIT``GOVERNMENT`

* * *

businessRegistrationPhoneNumberstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The E.164 formatted number associated with the business.

* * *

doingBusinessAsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Trade name, sub entity, or downstream business name of business being submitted for verification

* * *

optInConfirmationMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The confirmation message sent to users when they opt in to receive messages.

* * *

helpMessageSamplestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A sample help message provided to users.

* * *

privacyPolicyUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL to the privacy policy for the business or organization.

* * *

termsAndConditionsUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL to the terms and conditions for the business or organization.

* * *

ageGatedContentboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates if the content is age gated.

* * *

optInKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

List of keywords that users can text in to opt in to receive messages.

* * *

vettingProviderenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The third-party political vetting provider.

Possible values:

`CAMPAIGN_VERIFY`

* * *

vettingIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the vetting

Select from available examples

Copy code block


    {


      "BusinessName": "Owl, Inc.",


      "BusinessStreetAddress": "123 Main Street",


      "BusinessStreetAddress2": "Suite 101",


      "BusinessCity": "Anytown",


      "BusinessStateProvinceRegion": "AA",


      "BusinessPostalCode": "11111",


      "BusinessCountry": "US",


      "BusinessWebsite": "http://www.company.com",


      "BusinessContactFirstName": "firstname",


      "BusinessContactLastName": "lastname",


      "BusinessContactEmail": "email@company.com",


      "BusinessContactPhone": "+11231231234",


      "NotificationEmail": "support@company.com",


      "UseCaseCategories": [


        "POLITICAL_ELECTION_CAMPAIGNS"


      ],


      "UseCaseSummary": "This number is used to send out promotional offers and coupons to the customers of John's Coffee Shop",


      "ProductionMessageSample": "lorem ipsum",


      "OptInImageUrls": [


        "https://testbusiness.com/images/image1.jpg",


        "https://testbusiness.com/images/image2.jpg"


      ],


      "OptInType": "VERBAL",


      "MessageVolume": "10",


      "AdditionalInformation": "see our privacy policy here www.johnscoffeeshop.com/privacypolicy",


      "TollfreePhoneNumberSid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "ExternalReferenceId": "abc123xyz567",


      "BusinessRegistrationNumber": "123456789",


      "BusinessRegistrationAuthority": "EIN",


      "BusinessRegistrationCountry": "US",


      "BusinessType": "PRIVATE_PROFIT",


      "BusinessRegistrationPhoneNumber": "+13023334444",


      "DoingBusinessAs": "Toms Widgets",


      "AgeGatedContent": false,


      "HelpMessageSample": "For help, reply HELP or visit our website.",


      "OptInConfirmationMessage": "Thank you for opting in!",


      "OptInKeywords": [


        "START"


      ],


      "PrivacyPolicyUrl": "https://www.example.com/privacy",


      "TermsAndConditionsUrl": "https://www.example.com/terms",


      "VettingId": "cv|1.0|mno|tfree|a9792599-2156-457a-985b-f9045789b139|osfj78f1qrtue37",


      "VettingProvider": "CAMPAIGN_VERIFY"


    }

Submitting a TFV request requires a [Trust Hub Customer Profile](/docs/trust-hub/trusthub-rest-api/customer-profiles "Trust Hub Customer Profile").

### Submit a TFV request with an existing Customer Profile

submit-a-tfv-request-with-an-existing-customer-profile page anchor

Positive FeedbackNegative Feedback

If you have a Customer Profile, the following API request submits one TFV request associated with your Customer Profile SID.

Submit one TFV Request when you have a Customer ProfileLink to code sample: Submit one TFV Request when you have a Customer Profile

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function createTollfreeVerification() {


    11

      const tollfreeVerification =


    12

        await client.messaging.v1.tollfreeVerifications.create({


    13

          additionalInformation:


    14

            "see our privacy policy here www.example.com/privacypolicy",


    15

          businessName: "Owl, Inc.",


    16

          businessWebsite: "http://www.example.com",


    17

          customerProfileSid: "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

          externalReferenceId: "abc123xyz567",


    19

          messageVolume: "10",


    20

          notificationEmail: "support@example.com",


    21

          optInImageUrls: [


    22

            "https://example.com/images/image1.jpg",


    23

            "https://example.com/images/image2.jpg",


    24

          ],


    25

          optInType: "VERBAL",


    26

          productionMessageSample: "lorem ipsum",


    27

          tollfreePhoneNumberSid: "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    28

          useCaseCategories: ["TWO_FACTOR_AUTHENTICATION", "MARKETING"],


    29

          useCaseSummary:


    30

            "This number is used to send out promotional offers and coupons to the customers of Owl, Inc.",


    31

        });


    32




    33

      console.log(tollfreeVerification.sid);


    34

    }


    35




    36

    createTollfreeVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "customer_profile_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "regulated_item_sid": null,


    6

      "trust_product_sid": null,


    7

      "business_name": "Owl, Inc.",


    8

      "status": "PENDING_REVIEW",


    9

      "date_created": "2021-01-27T14:18:35Z",


    10

      "date_updated": "2021-01-27T14:18:36Z",


    11

      "business_street_address": "123 Main Street",


    12

      "business_street_address2": "Suite 101",


    13

      "business_city": "Anytown",


    14

      "business_state_province_region": "AA",


    15

      "business_postal_code": "11111",


    16

      "business_country": "US",


    17

      "business_website": "http://www.example.com",


    18

      "business_contact_first_name": "firstname",


    19

      "business_contact_last_name": "lastname",


    20

      "business_contact_email": "email@company.com",


    21

      "business_contact_phone": "+11231231234",


    22

      "notification_email": "support@example.com",


    23

      "use_case_categories": [


    24

        "TWO_FACTOR_AUTHENTICATION",


    25

        "MARKETING"


    26

      ],


    27

      "use_case_summary": "This number is used to send out promotional offers and coupons to the customers of Owl, Inc.",


    28

      "production_message_sample": "lorem ipsum",


    29

      "opt_in_image_urls": [


    30

        "https://example.com/images/image1.jpg",


    31

        "https://example.com/images/image2.jpg"


    32

      ],


    33

      "opt_in_type": "VERBAL",


    34

      "message_volume": "10",


    35

      "additional_information": "see our privacy policy here www.example.com/privacypolicy",


    36

      "tollfree_phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    37

      "rejection_reason": null,


    38

      "error_code": null,


    39

      "edit_expiration": null,


    40

      "edit_allowed": null,


    41

      "rejection_reasons": null,


    42

      "resource_links": {},


    43

      "url": "https://messaging.twilio.com/v1/Tollfree/Verifications/HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

      "external_reference_id": "abc123xyz567",


    45

      "business_registration_number": "123456789",


    46

      "business_registration_authority": "EIN",


    47

      "business_registration_country": "US",


    48

      "business_type": "PRIVATE_PROFIT",


    49

      "business_registration_phone_number": "+13023334444",


    50

      "doing_business_as": "Toms Widgets",


    51

      "age_gated_content": false,


    52

      "help_message_sample": "For help, reply HELP or visit our website.",


    53

      "opt_in_confirmation_message": "Thank you for opting in!",


    54

      "opt_in_keywords": [


    55

        "START"


    56

      ],


    57

      "privacy_policy_url": "https://www.example.com/privacy",


    58

      "terms_and_conditions_url": "https://www.example.com/terms",


    59

      "tollfree_phone_number": "+18003334444",


    60

      "vetting_id": null,


    61

      "vetting_id_expiration": null,


    62

      "vetting_provider": null


    63

    }

### Submit a TFV request without an existing Customer Profile

submit-a-tfv-request-without-an-existing-customer-profile page anchor

Positive FeedbackNegative Feedback

If you don't have a Trust Hub Customer Profile, the following API request creates a Customer Profile _and_ submits one TFV request for that profile.

Submit one TFV Request when you don't have a Customer ProfileLink to code sample: Submit one TFV Request when you don't have a Customer Profile

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function createTollfreeVerification() {


    11

      const tollfreeVerification =


    12

        await client.messaging.v1.tollfreeVerifications.create({


    13

          additionalInformation:


    14

            "see our privacy policy here www.example.com/privacypolicy",


    15

          businessCity: "Anytown",


    16

          businessContactEmail: "email@example.com",


    17

          businessContactFirstName: "firstname",


    18

          businessContactLastName: "lastname",


    19

          businessContactPhone: "+1231231234",


    20

          businessCountry: "US",


    21

          businessName: "Owl, Inc.",


    22

          businessPostalCode: "11111",


    23

          businessStateProvinceRegion: "AA",


    24

          businessStreetAddress: "123 Main Street",


    25

          businessStreetAddress2: "Suite 101",


    26

          businessWebsite: "http://www.example.com",


    27

          externalReferenceId: "abc123xyz567",


    28

          messageVolume: "10",


    29

          notificationEmail: "support@example.com",


    30

          optInImageUrls: [


    31

            "https://example.com/images/image1.jpg",


    32

            "https://example.com/images/image2.jpg",


    33

          ],


    34

          optInType: "VERBAL",


    35

          productionMessageSample: "lorem ipsum",


    36

          tollfreePhoneNumberSid: "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    37

          useCaseCategories: ["TWO_FACTOR_AUTHENTICATION", "MARKETING"],


    38

          useCaseSummary:


    39

            "This number is used to send out promotional offers and coupons to the customers of John's Coffee Shop",


    40

        });


    41




    42

      console.log(tollfreeVerification.sid);


    43

    }


    44




    45

    createTollfreeVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "regulated_item_sid": null,


    5

      "customer_profile_sid": null,


    6

      "trust_product_sid": null,


    7

      "status": "PENDING_REVIEW",


    8

      "date_created": "2021-01-27T14:18:35Z",


    9

      "date_updated": "2021-01-27T14:18:36Z",


    10

      "business_name": "Owl, Inc.",


    11

      "business_street_address": "123 Main Street",


    12

      "business_street_address2": "Suite 101",


    13

      "business_city": "Anytown",


    14

      "business_state_province_region": "AA",


    15

      "business_postal_code": "11111",


    16

      "business_country": "US",


    17

      "business_website": "http://www.example.com",


    18

      "business_contact_first_name": "firstname",


    19

      "business_contact_last_name": "lastname",


    20

      "business_contact_email": "email@example.com",


    21

      "business_contact_phone": "+1231231234",


    22

      "notification_email": "support@example.com",


    23

      "use_case_categories": [


    24

        "TWO_FACTOR_AUTHENTICATION",


    25

        "MARKETING"


    26

      ],


    27

      "use_case_summary": "This number is used to send out promotional offers and coupons to the customers of John's Coffee Shop",


    28

      "production_message_sample": "lorem ipsum",


    29

      "opt_in_image_urls": [


    30

        "https://example.com/images/image1.jpg",


    31

        "https://example.com/images/image2.jpg"


    32

      ],


    33

      "opt_in_type": "VERBAL",


    34

      "message_volume": "10",


    35

      "additional_information": "see our privacy policy here www.example.com/privacypolicy",


    36

      "tollfree_phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    37

      "rejection_reason": null,


    38

      "error_code": null,


    39

      "edit_expiration": null,


    40

      "edit_allowed": null,


    41

      "rejection_reasons": null,


    42

      "resource_links": {},


    43

      "url": "https://messaging.twilio.com/v1/Tollfree/Verifications/HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

      "external_reference_id": "abc123xyz567",


    45

      "business_registration_number": "123456789",


    46

      "business_registration_authority": "EIN",


    47

      "business_registration_country": "US",


    48

      "business_type": "PRIVATE_PROFIT",


    49

      "business_registration_phone_number": "+13023334444",


    50

      "doing_business_as": "Toms Widgets",


    51

      "age_gated_content": false,


    52

      "help_message_sample": "For help, reply HELP or visit our website.",


    53

      "opt_in_confirmation_message": "Thank you for opting in!",


    54

      "opt_in_keywords": [


    55

        "START"


    56

      ],


    57

      "privacy_policy_url": "https://www.example.com/privacy",


    58

      "terms_and_conditions_url": "https://www.example.com/terms",


    59

      "tollfree_phone_number": "+18003334444",


    60

      "vetting_id": null,


    61

      "vetting_id_expiration": null,


    62

      "vetting_provider": null


    63

    }

* * *

## Retrieve a TFV request

retrieve-a-tfv-request page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Tollfree/Verifications/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<HH>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A unique string identifying a Tollfree Verification.

Pattern: `^HH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve a TFV requestLink to code sample: Retrieve a TFV request

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function fetchTollfreeVerification() {


    11

      const tollfreeVerification = await client.messaging.v1


    12

        .tollfreeVerifications("HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(tollfreeVerification.sid);


    16

    }


    17




    18

    fetchTollfreeVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "customer_profile_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "trust_product_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "regulated_item_sid": "RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

      "date_created": "2021-01-27T14:18:35Z",


    8

      "date_updated": "2021-01-27T14:18:36Z",


    9

      "business_name": "Owl, Inc.",


    10

      "business_street_address": "123 Main Street",


    11

      "business_street_address2": "Suite 101",


    12

      "business_city": "Anytown",


    13

      "business_state_province_region": "AA",


    14

      "business_postal_code": "11111",


    15

      "business_country": "US",


    16

      "business_website": "http://www.company.com",


    17

      "business_contact_first_name": "firstname",


    18

      "business_contact_last_name": "lastname",


    19

      "business_contact_email": "email@company.com",


    20

      "business_contact_phone": "+11231231234",


    21

      "notification_email": "support@company.com",


    22

      "use_case_categories": [


    23

        "TWO_FACTOR_AUTHENTICATION",


    24

        "MARKETING"


    25

      ],


    26

      "use_case_summary": "This number is used to send out promotional offers and coupons to the customers of John's Coffee Shop",


    27

      "production_message_sample": "lorem ipsum",


    28

      "opt_in_image_urls": [


    29

        "https://testbusiness.com/images/image1.jpg",


    30

        "https://testbusiness.com/images/image2.jpg"


    31

      ],


    32

      "opt_in_type": "VERBAL",


    33

      "message_volume": "2000",


    34

      "additional_information": "see our privacy policy here www.johnscoffeeshop.com/privacypolicy",


    35

      "tollfree_phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

      "status": "TWILIO_APPROVED",


    37

      "rejection_reason": null,


    38

      "error_code": null,


    39

      "edit_expiration": null,


    40

      "edit_allowed": null,


    41

      "rejection_reasons": null,


    42

      "resource_links": {


    43

        "customer_profile": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

        "trust_product": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    45

        "channel_endpoint_assignment": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments/RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    46

      },


    47

      "url": "https://messaging.twilio.com/v1/Tollfree/Verifications/HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    48

      "external_reference_id": "abc123xyz567",


    49

      "business_registration_number": "123456789",


    50

      "business_registration_authority": "EIN",


    51

      "business_registration_country": "US",


    52

      "business_type": "PRIVATE_PROFIT",


    53

      "business_registration_phone_number": "+13023334444",


    54

      "doing_business_as": "Toms Widgets",


    55

      "age_gated_content": false,


    56

      "help_message_sample": "For help, reply HELP or visit our website.",


    57

      "opt_in_confirmation_message": "Thank you for opting in!",


    58

      "opt_in_keywords": [


    59

        "START"


    60

      ],


    61

      "privacy_policy_url": "https://www.example.com/privacy",


    62

      "terms_and_conditions_url": "https://www.example.com/terms",


    63

      "tollfree_phone_number": "+18003334444",


    64

      "vetting_id": null,


    65

      "vetting_id_expiration": null,


    66

      "vetting_provider": null


    67

    }

* * *

## Retrieve a list of TFV requests

retrieve-a-list-of-tfv-requests page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Tollfree/Verifications`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

tollfreePhoneNumberSidSID<PN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Phone Number associated with the Tollfree Verification.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The compliance status of the Tollfree Verification record.

Possible values:

`PENDING_REVIEW``IN_REVIEW``TWILIO_APPROVED``TWILIO_REJECTED`

* * *

externalReferenceIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Customer supplied reference id for the Tollfree Verification record.

* * *

includeSubAccountsboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to include Tollfree Verifications from sub accounts in list response.

* * *

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 50, and the maximum is 1000.

Minimum: `1`Maximum: `1000`

* * *

pageinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The page index. This value is simply for client state.

Minimum: `0`

* * *

pageTokenstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The page token. This is provided by the API.

* * *

trustProductSidarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The trust product sids / tollfree bundle sids of tollfree verifications

Retrieve a list of TFV requestsLink to code sample: Retrieve a list of TFV requests

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function fetchTollfreeVerification() {


    11

      const tollfreeVerification = await client.messaging.v1


    12

        .tollfreeVerifications("HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(tollfreeVerification.sid);


    16

    }


    17




    18

    fetchTollfreeVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "customer_profile_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "trust_product_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "regulated_item_sid": "RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

      "date_created": "2021-01-27T14:18:35Z",


    8

      "date_updated": "2021-01-27T14:18:36Z",


    9

      "business_name": "Owl, Inc.",


    10

      "business_street_address": "123 Main Street",


    11

      "business_street_address2": "Suite 101",


    12

      "business_city": "Anytown",


    13

      "business_state_province_region": "AA",


    14

      "business_postal_code": "11111",


    15

      "business_country": "US",


    16

      "business_website": "http://www.company.com",


    17

      "business_contact_first_name": "firstname",


    18

      "business_contact_last_name": "lastname",


    19

      "business_contact_email": "email@company.com",


    20

      "business_contact_phone": "+11231231234",


    21

      "notification_email": "support@company.com",


    22

      "use_case_categories": [


    23

        "TWO_FACTOR_AUTHENTICATION",


    24

        "MARKETING"


    25

      ],


    26

      "use_case_summary": "This number is used to send out promotional offers and coupons to the customers of John's Coffee Shop",


    27

      "production_message_sample": "lorem ipsum",


    28

      "opt_in_image_urls": [


    29

        "https://testbusiness.com/images/image1.jpg",


    30

        "https://testbusiness.com/images/image2.jpg"


    31

      ],


    32

      "opt_in_type": "VERBAL",


    33

      "message_volume": "2000",


    34

      "additional_information": "see our privacy policy here www.johnscoffeeshop.com/privacypolicy",


    35

      "tollfree_phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

      "status": "TWILIO_APPROVED",


    37

      "rejection_reason": null,


    38

      "error_code": null,


    39

      "edit_expiration": null,


    40

      "edit_allowed": null,


    41

      "rejection_reasons": null,


    42

      "resource_links": {


    43

        "customer_profile": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

        "trust_product": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    45

        "channel_endpoint_assignment": "https://trusthub.twilio.com/v1/TrustProducts/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments/RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    46

      },


    47

      "url": "https://messaging.twilio.com/v1/Tollfree/Verifications/HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    48

      "external_reference_id": "abc123xyz567",


    49

      "business_registration_number": "123456789",


    50

      "business_registration_authority": "EIN",


    51

      "business_registration_country": "US",


    52

      "business_type": "PRIVATE_PROFIT",


    53

      "business_registration_phone_number": "+13023334444",


    54

      "doing_business_as": "Toms Widgets",


    55

      "age_gated_content": false,


    56

      "help_message_sample": "For help, reply HELP or visit our website.",


    57

      "opt_in_confirmation_message": "Thank you for opting in!",


    58

      "opt_in_keywords": [


    59

        "START"


    60

      ],


    61

      "privacy_policy_url": "https://www.example.com/privacy",


    62

      "terms_and_conditions_url": "https://www.example.com/terms",


    63

      "tollfree_phone_number": "+18003334444",


    64

      "vetting_id": null,


    65

      "vetting_id_expiration": null,


    66

      "vetting_provider": null


    67

    }

* * *

## Update a TFV request

update-a-tfv-request page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/Tollfree/Verifications/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<HH>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string to identify Tollfree Verification.

Pattern: `^HH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

businessNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the business or organization using the Tollfree number.

* * *

businessWebsitestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The website of the business or organization using the Tollfree number.

* * *

notificationEmailstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The email address to receive the notification about the verification result. .

* * *

useCaseCategoriesarray[enum<string>]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The category of the use case for the Tollfree Number. List as many as are applicable.

Possible values:

`TWO_FACTOR_AUTHENTICATION``ACCOUNT_NOTIFICATIONS``CUSTOMER_CARE``CHARITY_NONPROFIT``DELIVERY_NOTIFICATIONS``FRAUD_ALERT_MESSAGING``EVENTS``HIGHER_EDUCATION``K12``MARKETING`Show 4 more

* * *

useCaseSummarystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Use this to further explain how messaging is used by the business or organization.

* * *

productionMessageSamplestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An example of message content, i.e. a sample message.

* * *

optInImageUrlsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Link to an image that shows the opt-in workflow. Multiple images allowed and must be a publicly hosted URL.

* * *

optInTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Describe how a user opts-in to text messages.

Possible values:

`VERBAL``WEB_FORM``PAPER_FORM``VIA_TEXT``MOBILE_QR_CODE``IMPORT``IMPORT_PLEASE_REPLACE`

* * *

messageVolumestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Estimate monthly volume of messages from the Tollfree Number.

* * *

businessStreetAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the business or organization using the Tollfree number.

* * *

businessStreetAddress2string

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the business or organization using the Tollfree number.

* * *

businessCitystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The city of the business or organization using the Tollfree number.

* * *

businessStateProvinceRegionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The state/province/region of the business or organization using the Tollfree number.

* * *

businessPostalCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The postal code of the business or organization using the Tollfree number.

* * *

businessCountrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The country of the business or organization using the Tollfree number.

* * *

additionalInformationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Additional information to be provided for verification.

* * *

businessContactFirstNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The first name of the contact for the business or organization using the Tollfree number.

* * *

businessContactLastNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The last name of the contact for the business or organization using the Tollfree number.

* * *

businessContactEmailstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The email address of the contact for the business or organization using the Tollfree number.

* * *

businessContactPhonestring<phone-number>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The E.164 formatted phone number of the contact for the business or organization using the Tollfree number.

* * *

editReasonstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Describe why the verification is being edited. If the verification was rejected because of a technical issue, such as the website being down, and the issue has been resolved this parameter should be set to something similar to 'Website fixed'.

* * *

businessRegistrationNumberstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A legally recognized business registration number

* * *

businessRegistrationAuthorityenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The organizational authority for business registrations. Required for all business types except SOLE_PROPRIETOR.

Possible values:

`EIN``CBN``CRN``PROVINCIAL_NUMBER``VAT``ACN``ABN``BRN``SIREN``SIRET`Show 8 more

* * *

businessRegistrationCountrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Country business is registered in

* * *

businessTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of business, valid values are PRIVATE_PROFIT, PUBLIC_PROFIT, NON_PROFIT, SOLE_PROPRIETOR, GOVERNMENT. Required field.

Possible values:

`PRIVATE_PROFIT``PUBLIC_PROFIT``SOLE_PROPRIETOR``NON_PROFIT``GOVERNMENT`

* * *

businessRegistrationPhoneNumberstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The E.164 formatted number associated with the business.

* * *

doingBusinessAsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Trade name, sub entity, or downstream business name of business being submitted for verification

* * *

optInConfirmationMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The confirmation message sent to users when they opt in to receive messages.

* * *

helpMessageSamplestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A sample help message provided to users.

* * *

privacyPolicyUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL to the privacy policy for the business or organization.

* * *

termsAndConditionsUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL to the terms and conditions for the business or organization.

* * *

ageGatedContentboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates if the content is age gated.

* * *

optInKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

List of keywords that users can text in to opt in to receive messages.

* * *

vettingProviderenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The third-party political vetting provider.

Possible values:

`CAMPAIGN_VERIFY`

* * *

vettingIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the vetting

Copy code block


    {


      "BusinessName": "Owl, Inc.",


      "BusinessStreetAddress": "123 Main Street",


      "BusinessStreetAddress2": "Suite 101",


      "BusinessCity": "Anytown",


      "BusinessStateProvinceRegion": "AA",


      "BusinessPostalCode": "11111",


      "BusinessCountry": "US",


      "BusinessWebsite": "http://www.company.com",


      "BusinessContactFirstName": "firstname",


      "BusinessContactLastName": "lastname",


      "BusinessContactEmail": "email@company.com",


      "BusinessContactPhone": "+11231231234",


      "NotificationEmail": "support@company.com",


      "UseCaseCategories": [


        "TWO_FACTOR_AUTHENTICATION",


        "MARKETING"


      ],


      "UseCaseSummary": "This number is used to send out promotional offers and coupons to the customers of John's Coffee Shop",


      "ProductionMessageSample": "lorem ipsum",


      "OptInImageUrls": [


        "https://testbusiness.com/images/image1.jpg",


        "https://testbusiness.com/images/image2.jpg"


      ],


      "OptInType": "VERBAL",


      "MessageVolume": "1,000",


      "AdditionalInformation": "see our privacy policy here www.johnscoffeeshop.com/privacypolicy",


      "EditReason": "Website fixed",


      "BusinessRegistrationNumber": "123456789",


      "BusinessRegistrationAuthority": "EIN",


      "BusinessRegistrationCountry": "US",


      "BusinessType": "PRIVATE_PROFIT",


      "BusinessRegistrationPhoneNumber": "+13023334444",


      "DoingBusinessAs": "Toms Widgets",


      "AgeGatedContent": false,


      "HelpMessageSample": "For help, reply HELP or visit our website.",


      "OptInConfirmationMessage": "Thank you for opting in!",


      "OptInKeywords": [


        "START"


      ],


      "PrivacyPolicyUrl": "https://www.example.com/privacy",


      "TermsAndConditionsUrl": "https://www.example.com/terms"


    }

Update a TFV requestLink to code sample: Update a TFV request

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function updateTollfreeVerification() {


    11

      const tollfreeVerification = await client.messaging.v1


    12

        .tollfreeVerifications("HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({


    14

          additionalInformation:


    15

            "See our privacy policy at www.example.com/privacypolicy",


    16

          editReason: "Updated the ProductionMessageSample",


    17

          messageVolume: "1,000",


    18

          optInImageUrls: [


    19

            "https://example.com/images/image1.jpg",


    20

            "https://example.com/images/image2.jpg",


    21

          ],


    22

          optInType: "VERBAL",


    23

          productionMessageSample:


    24

            "Get 10% off when you save this coupon: https://bit.ly/owlcoupon",


    25

          useCaseCategories: ["TWO_FACTOR_AUTHENTICATION", "MARKETING"],


    26

          useCaseSummary:


    27

            "This number is used to send out promotional offers and coupons to the customers of Owl, Inc.",


    28

        });


    29




    30

      console.log(tollfreeVerification.sid);


    31

    }


    32




    33

    updateTollfreeVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "regulated_item_sid": null,


    5

      "customer_profile_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "trust_product_sid": null,


    7

      "status": "PENDING_REVIEW",


    8

      "date_created": "2021-01-27T14:18:35Z",


    9

      "date_updated": "2021-01-27T14:18:36Z",


    10

      "business_name": "Owl, Inc.",


    11

      "business_street_address": "123 Main Street",


    12

      "business_street_address2": "Suite 101",


    13

      "business_city": "Anytown",


    14

      "business_state_province_region": "AA",


    15

      "business_postal_code": "11111",


    16

      "business_country": "US",


    17

      "business_website": "http://www.company.com",


    18

      "business_contact_first_name": "firstname",


    19

      "business_contact_last_name": "lastname",


    20

      "business_contact_email": "email@company.com",


    21

      "business_contact_phone": "+11231231234",


    22

      "notification_email": "support@company.com",


    23

      "use_case_categories": [


    24

        "TWO_FACTOR_AUTHENTICATION",


    25

        "MARKETING"


    26

      ],


    27

      "use_case_summary": "This number is used to send out promotional offers and coupons to the customers of Owl, Inc.",


    28

      "production_message_sample": "Get 10% off when you save this coupon: https://bit.ly/owlcoupon",


    29

      "opt_in_image_urls": [


    30

        "https://example.com/images/image1.jpg",


    31

        "https://example.com/images/image2.jpg"


    32

      ],


    33

      "opt_in_type": "VERBAL",


    34

      "message_volume": "1,000",


    35

      "additional_information": "See our privacy policy at www.example.com/privacypolicy",


    36

      "tollfree_phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    37

      "rejection_reason": null,


    38

      "error_code": null,


    39

      "edit_expiration": null,


    40

      "edit_allowed": null,


    41

      "rejection_reasons": null,


    42

      "resource_links": {},


    43

      "url": "https://messaging.twilio.com/v1/Tollfree/Verifications/HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

      "external_reference_id": null,


    45

      "business_registration_number": "123456789",


    46

      "business_registration_authority": "EIN",


    47

      "business_registration_country": "US",


    48

      "business_type": "PRIVATE_PROFIT",


    49

      "business_registration_phone_number": "+13023334444",


    50

      "doing_business_as": "Toms Widgets",


    51

      "age_gated_content": false,


    52

      "help_message_sample": "For help, reply HELP or visit our website.",


    53

      "opt_in_confirmation_message": "Thank you for opting in!",


    54

      "opt_in_keywords": [


    55

        "START"


    56

      ],


    57

      "privacy_policy_url": "https://www.example.com/privacy",


    58

      "terms_and_conditions_url": "https://www.example.com/terms",


    59

      "tollfree_phone_number": "+18003334444",


    60

      "vetting_id": null,


    61

      "vetting_id_expiration": null,


    62

      "vetting_provider": null


    63

    }

* * *

## Delete a TFV request

delete-a-tfv-request page anchor

Positive FeedbackNegative Feedback

`DELETE https://messaging.twilio.com/v1/Tollfree/Verifications/{Sid}`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<HH>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string to identify Tollfree Verification.

Pattern: `^HH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a TFV requestLink to code sample: Delete a TFV request

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function deleteTollfreeVerification() {


    11

      await client.messaging.v1


    12

        .tollfreeVerifications("HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .remove();


    14

    }


    15




    16

    deleteTollfreeVerification();