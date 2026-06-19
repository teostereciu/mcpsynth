# A2P 10DLC - UsAppToPerson (Usa2p) resource

*Source: https://www.twilio.com/docs/messaging/api/usapptoperson-resource*

---

# A2P 10DLC - UsAppToPerson (Usa2p) resource

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

This API reference page supplements the [ISV API onboarding guides](/docs/messaging/compliance/a2p-10dlc/onboarding-isv "ISV API onboarding guides"). Don't use this API resource without following the appropriate guide, or you might experience **delays in registration and unintended fees**.

A UsAppToPerson (Usa2p) resource represents an A2P 10DLC Campaign within a Messaging Service. This resource contains information about the Campaign such as message contents, opt-in and opt-out behavior, and the purpose of the messages.

This resource is part of the A2P 10DLC registration process and is intended only for use by Independent Software Vendors (ISVs).

Not an ISV? Check out the [Standard and Low-Volume Brand Onboarding Guide](/docs/messaging/compliance/a2p-10dlc/direct-standard-onboarding "Standard and Low-Volume Brand Onboarding Guide") or the [Sole Proprietor Brand Onboarding Guide](/docs/messaging/compliance/a2p-10dlc/direct-sole-proprietor-registration-overview "Sole Proprietor Brand Onboarding Guide").

* * *

## Usa2p Properties

usa2p-properties page anchor

Positive FeedbackNegative Feedback

Select from possible schemas[View the Swagger documentation for oneOf](https://swagger.io/docs/specification/data-models/oneof-anyof-allof-not/#oneof)

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<QE>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that identifies a US A2P Compliance resource `QE2c6890da8086d771620e9b13fadeba0b`.

Pattern: `^QE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that the Campaign belongs to.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

brandRegistrationSidSID<BN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string to identify the A2P brand.

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") that the resource is associated with.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

descriptionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.

* * *

messageSamplesarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars.

* * *

usAppToPersonUsecasestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING, SOLE_PROPRIETOR...]. SOLE_PROPRIETOR campaign use cases can only be created by SOLE_PROPRIETOR Brands, and there can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR Brand.

* * *

hasEmbeddedLinksboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicate that this SMS campaign will send messages that contain links.

* * *

hasEmbeddedPhoneboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates that this SMS campaign will send messages that contain phone numbers.

* * *

subscriberOptInboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether campaign has Subscriber Optin or not.

* * *

ageGatedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether campaign is age gated or not.

* * *

directLendingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether campaign allows direct lending or not.

* * *

campaignStatusstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Campaign status. Examples: IN_PROGRESS, VERIFIED, FAILED.

* * *

campaignIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Campaign Registry (TCR) Campaign ID.

* * *

isExternallyRegisteredboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates whether the campaign was registered externally or not.

* * *

rateLimits

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Rate limit and/or classification set by each carrier, Ex. AT&T or T-Mobile.

* * *

messageFlowstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.

* * *

optInMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.

* * *

optOutMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.

* * *

helpMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.

* * *

optInKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.

* * *

optOutKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

* * *

helpKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

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

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the US App to Person resource.

* * *

mockboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether campaign is a mock or not. Mock campaigns will be automatically created if using a mock brand. Mock campaigns should only be used for testing purposes.

* * *

errorsarray

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Details indicating why a campaign registration failed. These errors can indicate one or more fields that were incorrect or did not meet review requirements.

* * *

## Create a Usa2p resource

create-a-usa2p-resource page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/Compliance/Usa2p`

This request creates a Usa2p resource, which represents an A2P 10DLC Campaign. Creating this resource submits the Campaign for review and incurs fees.

Learn more about the formats and contents of each parameter in the [Gather the Required Business Information doc](/docs/messaging/compliance/a2p-10dlc/collect-business-info "Gather the Required Business Information doc").

### Headers

headers page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

x-Twilio-Api-Versionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The version of the Messaging API to use for this request

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") to create the resources from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

brandRegistrationSidSID<BN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A2P Brand Registration SID

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

descriptionstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.

* * *

messageFlowstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.

* * *

messageSamplesarray[string]

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars.

* * *

usAppToPersonUsecasestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]

* * *

hasEmbeddedLinksboolean

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates that this SMS campaign will send messages that contain links.

* * *

hasEmbeddedPhoneboolean

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates that this SMS campaign will send messages that contain phone numbers.

* * *

optInMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.

* * *

optOutMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.

* * *

helpMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.

* * *

optInKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.

* * *

optOutKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

* * *

helpKeywordsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

* * *

subscriberOptInboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether campaign has Subscriber Optin or not.

* * *

ageGatedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether campaign is age gated or not.

* * *

directLendingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether campaign allows direct lending or not.

* * *

privacyPolicyUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of the privacy policy for the campaign.

* * *

termsAndConditionsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of the terms and conditions for the campaign.

Select from available examples

Copy code block


    {


      "BrandRegistrationSid": "BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "Description": "Send marketing messages about sales to opted in customers.",


      "MessageSamples": [


        "EXPRESS: Denim Days Event is ON",


        "LAST CHANCE: Book your next flight for just 1 (ONE) EUR"


      ],


      "UsAppToPersonUsecase": "MARKETING",


      "MessageFlow": "End users opt-in by visiting www.example.com and adding their phone number. They then check a box agreeing to receive text messages from Example Brand. Additionally, end users can also opt-in by texting START to (111) 222-3333 to opt in.",


      "OptInMessage": "Acme Corporation: You are now opted-in. For help, reply HELP. To opt-out, reply STOP",


      "OptOutMessage": "You have successfully been unsubscribed from Acme Corporation. You will not receive any more messages from this number.",


      "HelpMessage": "Acme Corporation: Please visit www.example.com to get support. To opt-out, reply STOP.",


      "OptInKeywords": [


        "START"


      ],


      "OptOutKeywords": [


        "STOP"


      ],


      "HelpKeywords": [


        "HELP"


      ],


      "HasEmbeddedLinks": true,


      "HasEmbeddedPhone": false,


      "SubscriberOptIn": false,


      "AgeGated": false,


      "DirectLending": false


    }

(information)

## Info

If you use Twilio's [default opt-out or advanced opt-out(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/223134027-Twilio-support-for-opt-out-keywords-SMS-STOP-filtering- "default opt-out or advanced opt-out"), you do not need to submit opt-out and help keywords and messages when creating a Campaign. Twilio will automatically complete those fields for you with the default or your advanced opt-out and help messaging.

If you manage opt-out and help yourself, you must pass the opt-out and help parameters when creating a Campaign.

Create a Usa2p resourceLink to code sample: Create a Usa2p resource

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

    async function createUsAppToPerson() {


    11

      const usAppToPerson = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .usAppToPerson.create({


    14

          brandRegistrationSid: "BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          description: "Description",


    16

          hasEmbeddedLinks: false,


    17

          hasEmbeddedPhone: false,


    18

          messageFlow:


    19

            "End users opt-in by visiting www.example.com and adding their phone number. They then check a box agreeing to receive text messages from Example Brand. Additionally, end users can also opt-in by texting START to (111) 222-3333 to opt in. Term and Conditions at www.example.com/tc. Privacy Policy at www.example.com/privacy",


    20

          messageSamples: [


    21

            "EXPRESS: Denim Days Event is ON. Reply STOP to unsubscribe.",


    22

            "LAST CHANCE: Book your next flight for just 1 (ONE) EUR",


    23

          ],


    24

          usAppToPersonUsecase: "UsAppToPersonUsecase",


    25

        });


    26




    27

      console.log(usAppToPerson.brandRegistrationSid);


    28

    }


    29




    30

    createUsAppToPerson();

* * *

## Retrieve a Usa2p resource

retrieve-a-usa2p-resource page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}`

This request returns a Usa2p resource. The Usa2p resource represents an A2P 10DLC Campaign.

The value of `Sid` is always the US A2P Compliance resource identifier: `QE2c6890da8086d771620e9b13fadeba0b`.

### Headers

headers-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

x-Twilio-Api-Versionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The version of the Messaging API to use for this request

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") to fetch the resource from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<QE>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.

Pattern: `^QE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve a US A2P CampaignLink to code sample: Retrieve a US A2P Campaign

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

    async function fetchUsAppToPerson() {


    11

      const usAppToPerson = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .usAppToPerson("QEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .fetch();


    15




    16

      console.log(usAppToPerson.brandRegistrationSid);


    17

    }


    18




    19

    fetchUsAppToPerson();

You can use this request to check the `campaign_status` of the Campaign represented by this Usa2p resource. Possible statuses are listed below:

  * `PENDING` \- The Campaign has not yet been viewed by TCR.
  * `IN_PROGRESS` \- TCR has begun the review process for the Campaign.
  * `FAILED` \- The Campaign has failed the verification process.
  * `VERIFIED` \- TCR has approved the Campaign.


If `campaign_status` is `FAILED`, the `errors` property of the Usa2p resource is populated with a list of reasons why the Campaign was not approved. See the [Troubleshooting Campaigns guide](/docs/messaging/compliance/a2p-10dlc/troubleshooting-a2p-brands/troubleshooting-and-rectifying-a2p-campaigns-1 "Troubleshooting Campaigns guide") for more information.

* * *

## Retrieve a list of Usa2p resources

retrieve-a-list-of-usa2p-resources page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/Compliance/Usa2p`

This request retrieves all Usa2p resources associated with a specific Messaging Service.

### Headers

headers-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

x-Twilio-Api-Versionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The version of the Messaging API to use for this request

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") to fetch the resource from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

Retrieve a list of Usa2p resources for a Messaging ServiceLink to code sample: Retrieve a list of Usa2p resources for a Messaging Service

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

    async function listUsAppToPerson() {


    11

      const usAppToPeople = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .usAppToPerson.list({ limit: 20 });


    14




    15

      usAppToPeople.forEach((u) => console.log(u.brandRegistrationSid));


    16

    }


    17




    18

    listUsAppToPerson();

### Response

Note about this response

Copy response


    1

    {


    2

      "compliance": [


    3

        {


    4

          "sid": "QE2c6890da8086d771620e9b13fadeba0b",


    5

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

          "brand_registration_sid": "BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

          "description": "Send marketing messages about sales to opted in customers.",


    9

          "message_samples": [


    10

            "EXPRESS: Denim Days Event is ON",


    11

            "LAST CHANCE: Book your next flight for just 1 (ONE) EUR"


    12

          ],


    13

          "us_app_to_person_usecase": "MARKETING",


    14

          "has_embedded_links": true,


    15

          "has_embedded_phone": false,


    16

          "subscriber_opt_in": true,


    17

          "age_gated": false,


    18

          "direct_lending": false,


    19

          "campaign_status": "PENDING",


    20

          "campaign_id": "CFOOBAR",


    21

          "is_externally_registered": false,


    22

          "rate_limits": {


    23

            "att": {


    24

              "mps": 600,


    25

              "msg_class": "A"


    26

            },


    27

            "tmobile": {


    28

              "brand_tier": "TOP"


    29

            }


    30

          },


    31

          "message_flow": "End users opt-in by visiting www.example.com and adding their phone number. They then check a box agreeing to receive text messages from Example Brand. Additionally, end users can also opt-in by texting START to (111) 222-3333 to opt in.",


    32

          "opt_in_message": "Acme Corporation: You are now opted-in. For help, reply HELP. To opt-out, reply STOP",


    33

          "opt_out_message": "You have successfully been unsubscribed from Acme Corporation. You will not receive any more messages from this number.",


    34

          "help_message": "Acme Corporation: Please visit www.example.com to get support. To opt-out, reply STOP.",


    35

          "opt_in_keywords": [


    36

            "START"


    37

          ],


    38

          "opt_out_keywords": [


    39

            "STOP"


    40

          ],


    41

          "help_keywords": [


    42

            "HELP"


    43

          ],


    44

          "date_created": "2021-02-18T14:48:52Z",


    45

          "date_updated": "2021-02-18T14:48:52Z",


    46

          "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p/QE2c6890da8086d771620e9b13fadeba0b",


    47

          "mock": false,


    48

          "errors": []


    49

        }


    50

      ],


    51

      "meta": {


    52

        "page": 0,


    53

        "page_size": 20,


    54

        "first_page_url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p?PageSize=20&Page=0",


    55

        "previous_page_url": null,


    56

        "next_page_url": null,


    57

        "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p?PageSize=20&Page=0",


    58

        "key": "compliance"


    59

      }


    60

    }

* * *

## Delete a Usa2p resource

delete-a-usa2p-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid}`

This request deletes a Usa2p resource.

(error)

## Danger

Deleting an approved Usa2p resource blocks all A2P 10DLC messaging from the Messaging Service.

You must create a new Usa2p resource and wait for the associated Campaign to be approved by TCR in order to send A2P 10DLC messages from the Messaging Service again. This can take several days.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") to delete the resource from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<QE>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the US A2P Compliance resource to delete `QE2c6890da8086d771620e9b13fadeba0b`.

Pattern: `^QE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

The value of `Sid` is always the US A2P Compliance resource identifier: `QE2c6890da8086d771620e9b13fadeba0b`.

Delete a Usa2p resourceLink to code sample: Delete a Usa2p resource

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

    async function deleteUsAppToPerson() {


    11

      await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .usAppToPerson("QEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .remove();


    15

    }


    16




    17

    deleteUsAppToPerson();