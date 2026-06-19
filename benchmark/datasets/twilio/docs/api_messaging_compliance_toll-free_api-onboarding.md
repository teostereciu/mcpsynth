# Get started with toll-free verification using the API

*Source: https://www.twilio.com/docs/messaging/compliance/toll-free/api-onboarding*

---

# Get started with toll-free verification using the API

Positive FeedbackNegative Feedback

* * *

(information)

## ISVs: Compliance Embeddable for Toll-Free Verification

By adding the [Compliance Embeddable](/docs/messaging/compliance/toll-free/compliance-embeddable-onboarding "Compliance Embeddable") to their website, an independent software vendor (ISV) can onboard customers without using the Toll-Free Verification (TFV) API. The Compliance Embeddable lets customers submit compliance information through a self-service workflow. To learn more, see the [blog post(link takes you to an external page)](https://www.twilio.com/en-us/blog/ISV-Compliance-Embeddable "blog post") introducing the Compliance Embeddable for Toll-Free verification. To get additional guidance, see our support article for guidance on [TFV for ISVs(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/13263383206299-Toll-Free-Verification-for-ISVs "TFV for ISVs").

Toll-free phone numbers for the US and Canada use the North American Numbering Plan (NANP). NANP toll-free numbers begin with `800`, `888`, `877`, `866`, `855`, `844`, or `833`. To use these numbers to send SMS messages, your organization must comply with federal regulations. Compliance requires verifying how you plan to use your phone number to send texts. To verify your NANP toll-free phone number for regulatory compliance, use the Toll-Free Verification API.

(information)

## Business Registration Number required and optional properties

Registration includes properties for a business registration number and related compliance information.

To reduce review times and minimize the risk of rejection, provide your business registration number and related details. To learn more, see [Toll-Free Verification Policy for Collecting Business Registration Number(link takes you to an external page)](https://help.twilio.com/articles/38266268244507-Toll-Free-Verification-Policy-for-Collecting-Business-Registration-Number "Toll-Free Verification Policy for Collecting Business Registration Number").

(warning)

## Campaign Verify Token Required for Political Organizations

If your organization is a **527 political organization** and you are registering for the **POLITICAL_ELECTION_CAMPAIGNS** use case, you MUST provide a Campaign Verify (CV) token during toll-free verification. Failure to provide a valid CV token will result in rejection of your verification request.

Read the [Campaign Verify section](/docs/messaging/compliance/toll-free/api-onboarding#campaign-verify-for-political-messaging "Campaign Verify section") below before starting the TFV process.

* * *

## Create a Trust Hub Primary Customer Profile

create-a-trust-hub-primary-customer-profile page anchor

Positive FeedbackNegative Feedback

TFV requests with Twilio require your business to have a [Trust Hub Primary Customer Profile](/docs/trust-hub/trusthub-rest-api/customer-profiles "Trust Hub Primary Customer Profile"). A _Primary Customer Profile_ is also known as a _Primary Business Profile_.

  1. Open the [Trust Hub in the Twilio Console(link takes you to an external page)](https://console.twilio.com/us1/account/trust-hub/overview "Trust Hub in the Twilio Console").
  2. [Create your Trust Hub Primary Customer Profile](/docs/trust-hub/trusthub-rest-api/console-create-a-primary-customer-profile "Create your Trust Hub Primary Customer Profile").
  3. When you reach the **Business Information** step of the **Create Profile** workflow, set the value of **Select business identity**.
     * If you plan to use Twilio in a product you sell to customers, Twilio considers you an ISV. Choose **ISV Reseller or Partner**.
     * If you plan to use Twilio to communicate directly with customers or staff, Twilio considers you a direct customer. Choose **Direct Customer**.
  4. At the **Notification settings** step, provide an email address at which Twilio can contact you about the status of your request.
  5. After you submit your request to Twilio, Twilio reviews it and sends a notification of approval or rejection to the email address you provided.
  6. After you receive notification of your profile status, open the [Trust Hub in the Twilio Console(link takes you to an external page)](https://console.twilio.com/us1/account/trust-hub/overview "Trust Hub in the Twilio Console"). Twilio approved your Primary Customer Profile.
Your **Profile Details** page displays a **Status** of **Twilio-Approved**.
  7. Copy the **Business Profile SID** value of your parent account. This SID begins with `BU` with 32 hexadecimal digits. To [Create a TFV request](/docs/messaging/compliance/toll-free/api-onboarding#create-a-tfv-request "Create a TFV request"), you need this Business Profile SID. The Create TFV resource names this parameter `CustomerProfileSid`. These refer to the same value.


Trust Hub Customer Profiles can link to a _parent_ account or a [subaccount](/docs/iam/api/subaccounts "subaccount"). Think of a parent account as the main organization and subaccounts as departments or subsidiaries. To create a parent account, you must use the [Twilio Console(link takes you to an external page)](https://console.twilio.com/us1/account/trust-hub/overview "Twilio Console"). You can create subaccounts using the [Twilio TrustHub API](/docs/trust-hub/trusthub-rest-api/customer-profiles "Twilio TrustHub API").

To keep customers separate, production ISV parent accounts should link Trust Hub customer profiles to subaccounts.

* * *

## Create a TFV request

create-a-tfv-request page anchor

Positive FeedbackNegative Feedback

To use an NANP toll-free phone number for messaging, submit a verification request for the related business. As you have an approved Primary Customer Profile, your request only needs the parameters for the TFV. To learn more, see [Required Information for Toll-Free Verification(link takes you to an external page)](https://help.twilio.com/articles/13264118705051 "Required Information for Toll-Free Verification") in the Twilio Help Center.

### Provide business and compliance data

provide-business-and-compliance-data page anchor

Positive FeedbackNegative Feedback

To support changes to toll-free messaging policy when submitting a TFV request, include additional metadata about your business. To avoid rejection and accelerate vetting, provide this information before its required. To learn more, see [Toll-Free Verification Policy for Collecting Business Registration Number(link takes you to an external page)](https://help.twilio.com/articles/38266268244507 "Toll-Free Verification Policy for Collecting Business Registration Number") in the Twilio Help Center.

  1. Make a `POST` request to the `https://messaging.twilio.com/v1/Tollfree/Verifications` resource.
All parameters for this request are request body parameters.

Click to review the request body parameters

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

(information)

## Info

**Note about Campaign Verify parameters:** The `VettingId` and `VettingProvider` parameters shown in this example are **REQUIRED** if your organization is a 527 political organization and if you are registering for the POLITICAL_ELECTION_CAMPAIGNS use case. For all other organizations and use cases, these parameters are optional. See the [Campaign Verify section](/docs/messaging/compliance/toll-free/api-onboarding#campaign-verify-for-political-messaging "Campaign Verify section") for details.

Submit a TFV Request using your Customer ProfileLink to code sample: Submit a TFV Request using your Customer Profile

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

               additionalInformation: "privacy policy is geo-locked to NAMER region",


         14

               businessName: "Owl, Inc.",


         15

               businessWebsite: "http://www.example.com",


         16

               customerProfileSid: "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


         17

               messageVolume: "10",


         18

               notificationEmail: "support@example.com",


         19

               optInImageUrls: [


         20

                 "https://example.com/images/image1.jpg",


         21

                 "https://example.com/images/image2.jpg",


         22

               ],


         23

               optInType: "VERBAL",


         24

               productionMessageSample: "lorem ipsum",


         25

               tollfreePhoneNumberSid: "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


         26

               useCaseCategories: ["TWO_FACTOR_AUTHENTICATION", "MARKETING"],


         27

               useCaseSummary:


         28

                 "This number is used to send out promotional offers and coupons to the customers of Owl, Inc.",


         29

               vettingId:


         30

                 "cv|1.0|mno|tfree|b344a16f-b435-4a39-bf91-df9b8e4e0a0d|E5eh-rOPHCr_lrgHDYEZP45FzuJSHS1fkFTmVPD8GQ4",


         31

               vettingProvider: "CAMPAIGN_VERIFY",


         32

             });


         33




         34

           console.log(tollfreeVerification.sid);


         35

         }


         36




         37

         createTollfreeVerification();

Twilio reviews TFV requests within three business days.

  2. Check the status of your TFV request.

Check one TFV requestLink to code sample: Check one TFV request

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

If you don't have your TFV request SID, use the API to get a list of TFV SIDs for your related toll-free number.

Click to review the get list of TFV SIDs API request

Get list of TFV requestsLink to code sample: Get list of TFV requests

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

         async function listTollfreeVerification() {


         11

           const tollfreeVerifications =


         12

             await client.messaging.v1.tollfreeVerifications.list({


         13

               tollfreePhoneNumberSid: "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


         14

               limit: 20,


         15

             });


         16




         17

           tollfreeVerifications.forEach((t) => console.log(t.sid));


         18

         }


         19




         20

         listTollfreeVerification();

  3. Look for the `status` property in the response.

#### Response to a Check TFV request

response-to-a-check-tfv-request page anchor

Copy code block

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

             "https://testbusiness.com/images/image1.jpg",


         31

             "https://testbusiness.com/images/image2.jpg"


         32

           ],


         33

           "opt_in_type": "VERBAL",


         34

           "message_volume": "10",


         35

           "additional_information": "privacy policy is geo-locked to NAMER region",


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




         46

             // New response fields for the 2026 update


         47

            "business_registration_number": "123456789",


         48

            "business_registration_authority": "EIN",


         49

            "business_registration_country": "US",


         50

            "doing_business_as": "Other Company",


         51

            "business_type": "PRIVATE_PROFIT",


         52

            "opt_in_confirmation_sample": "Opt in sample message",


         53

            "help_message_sample": "Help sample",


         54

            "privacy_policy_url": "http://www.example.com/privacy",


         55

            "terms_and_condition_url": "http://www.example.com/terms",


         56

            "age_gated_content": false,


         57

            "opt_in_keywords": "STOP",


         58




         59

            // New response fields for CV Token update


         60

            "vetting_id": "cv|1.0|mno|tfree|b344a16f-b435-4a39-bf91-df9b8e4e0a0d|E5eh-rOPHCr_lrgHDYEZP45FzuJSHS1fkFTmVPD8GQ4",


         61

            "vetting_provider": "CAMPAIGN_VERIFY",


         62

            "vetting_id_expiration": "2027-01-31T23:59:59Z"


         63




         64

         }

If Twilio approved your TFV request, `status` reads as `"status": "TWILIO_APPROVED"`. The verified toll-free number can send Application to Person (A2P) SMS messages with minimal traffic filtering.


If you don't have a Trust Hub Customer Profile, you can create one at the same time as submitting your TFV request. To learn how to perform both tasks at once, see [this variation on the Create TFV request](/docs/messaging/api/tollfree-verification-resource#submit-one-tfv-request-without-an-existing-customer-profile "this variation on the Create TFV request").

* * *

## Fix a rejected TFV request

fix-a-rejected-tfv-request page anchor

Positive FeedbackNegative Feedback

If Twilio rejected your TFV request, your check request displays `"status": "TWILIO_REJECTED"`. The toll-free number isn't verified and you [can't use it to send messages(link takes you to an external page)](https://help.twilio.com/articles/5377174717595-Toll-Free-Message-Verification-for-US-Canada#h_01GTCNPTVZFNCK8FFNYRDD2TZR "can't use it to send messages"). To review common rejection reasons, see [Why Was My Toll-Free Verification Rejected?(link takes you to an external page)](https://help.twilio.com/articles/9321443984155 "Why Was My Toll-Free Verification Rejected?") in the Twilio Help Center.

If the response includes `"edit_allowed": true`, you can resubmit your TFV request.

  1. Check the status of your [TFV request](/docs/messaging/compliance/toll-free/api-onboarding#response-to-a-check-tfv-request "TFV request").

  2. In the response, find two properties:

     * The `edit_allowed` property
       * If this value is set to `true`, you can edit the TFV request and resubmit it.
       * You must submit the TFV request before the timestamp provided in the `edit_expiration` property. Twilio sets this property value to seven days from the initial request. After that date, the TFV request expires and you need to create another.
     * The `rejection_reasons` property array
       * This array returns the list of reasons why Twilio rejected your TFV as a human-readable `reason` and a `code` that links to details on this error.
  3. To correct any errors in your TFV request, use the [**Edit a TFV Request** resource](/docs/messaging/api/tollfree-verification-resource#edit-one-tfv-request).

Edit a TFV RequestLink to code sample: Edit a TFV Request

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

  4. Check your [TFV request status](/docs/messaging/compliance/toll-free/api-onboarding#code-check-one-tfv-request "TFV request status").


* * *

## Delete a failed TFV request

delete-a-failed-tfv-request page anchor

Positive FeedbackNegative Feedback

If you can't edit your TFV request, delete it. The delete resource requires the SID for the Verification record to delete. This SID starts with `HH` followed by 32 other hexadecimal digits.

If you don't have your TFV request SID, use the API to get a list of TFV SIDs for your related toll-free number.

Click to review the get list of TFV SIDs API request

Get list of TFV requestsLink to code sample: Get list of TFV requests

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

    async function listTollfreeVerification() {


    11

      const tollfreeVerifications =


    12

        await client.messaging.v1.tollfreeVerifications.list({


    13

          tollfreePhoneNumberSid: "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          limit: 20,


    15

        });


    16




    17

      tollfreeVerifications.forEach((t) => console.log(t.sid));


    18

    }


    19




    20

    listTollfreeVerification();

Delete a TFV request recordLink to code sample: Delete a TFV request record

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

* * *

## Campaign Verify for Political Messaging

campaign-verify-for-political-messaging page anchor

Positive FeedbackNegative Feedback

(information)

## Info

This section applies to 527 political organizations registering for the POLITICAL_ELECTION_CAMPAIGNS use case for toll-free messaging.

Campaign Verify is a secure, non-partisan verification solution for US political organizations who wish to engage with voters via toll-free messaging.

All organizations sending political communications on behalf of a federal, state, or local political campaign must [be verified by Campaign Verify(link takes you to an external page)](https://www.campaignverify.org/#signup "be verified by Campaign Verify") to complete toll-free verification for political use cases.

(warning)

## Warning

You should read the Campaign Verify [FAQ(link takes you to an external page)](https://www.campaignverify.org/faq "FAQ") before continuing with this guide, as this process involves fees and identity verification.

### When Campaign Verify tokens are required

when-campaign-verify-tokens-are-required page anchor

Positive FeedbackNegative Feedback

A Campaign Verify token is **REQUIRED** for toll-free verification when:

  1. **Your organization is a 527 political organization**
  2. **And you select POLITICAL_ELECTION_CAMPAIGNS** as a use case category.


Without a valid CV token, your toll-free verification will be rejected if you meet these criterias.

### Obtaining a Campaign Verify token

obtaining-a-campaign-verify-token page anchor

Positive FeedbackNegative Feedback

Verification involves submitting information about your political organization to Campaign Verify, as well as verifying your identity as an authorized person associated with the political organization.

  1. Visit [Campaign Verify(link takes you to an external page)](https://www.campaignverify.org/#signup "Campaign Verify") to begin the verification process
  2. Complete identity verification and provide required organization information
  3. After approval, Campaign Verify issues you a CV token
  4. Provide this CV token during TFV registration using the `VettingId` and `VettingProvider` parameters


### Campaign Verify token format

campaign-verify-token-format page anchor

Positive FeedbackNegative Feedback

A full CV token is composed of 6 pipe (|) delimited fields, for example:

..`cv|1.0|mno|tfree|b344a16f-b435-4a39-bf91-df9b8e4e0a0d|E5eh-rOPHCr_lrgHDYEZP45FzuJSHS1fkFTmVPD8GQ4`

When submitting your TFV request:

  * Set `VettingProvider` to `CAMPAIGN_VERIFY`
  * Set `VettingId` to your full CV token (all 6 fields, including the pipes)
  * The token is case-sensitive and must match the format provided by Campaign Verify exactly


### Token expiration and management

token-expiration-and-management page anchor

Positive FeedbackNegative Feedback

  * CV tokens expire after a period of time (expiration date provided by Campaign Verify)
  * The `vetting_id_expiration` field in the TFV response shows when your token expires
  * The CV token must be registered for the organization entity listed on the token. If your TFV request is rejected with an error code related to Campaign Verify, check that the token is valid and registered to the correct organization.
  * If you are ISV and multiple customers sending political messaging, each customer needs a separate CV token.
  * To update an expired token, edit your existing TFV request with a new CV token


(warning)

## Warning

An organization that does not provide a Campaign Verify token when required will have their toll-free verification rejected. Even if approved without a token initially, carriers may block political messaging traffic that is not properly verified through Campaign Verify.