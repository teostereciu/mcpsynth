# A2P 10DLC - Vettings subresource

*Source: https://www.twilio.com/docs/messaging/api/brand-vetting-resource*

---

# A2P 10DLC - Vettings subresource

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

This API reference page supplements the [A2P 10DLC government and nonprofit onboarding guide](/docs/messaging/compliance/a2p-10dlc/onboarding-for-government-and-non-profit-agencies "A2P 10DLC government and nonprofit onboarding guide"). Don't use this API resource without following the appropriate guide, or you might experience **delays in registration and unintended fees**.

Vettings is a subresource of [BrandRegistrations](/docs/messaging/api/brand-registration-resource "BrandRegistrations") and represents the association between a [Campaign Verify(link takes you to an external page)](https://www.campaignverify.org/ "Campaign Verify") token and a BrandRegistration resource.

* * *

## Vetting Properties

vetting-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the vetting record.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

brandSidSID<BN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string to identify Brand Registration.

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

brandVettingSidSID<VT>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio SID of the third-party vetting record.

Pattern: `^VT[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

vettingIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique identifier of the vetting from the third-party provider.

* * *

vettingClassstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of vetting that has been conducted. One of “STANDARD” (Aegis) or “POLITICAL” (Campaign Verify).

* * *

vettingStatusstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the import vetting attempt. One of “PENDING,” “SUCCESS,” or “FAILED”.

* * *

vettingProviderenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign Verify tokens) or “AEGIS” (Secondary Vetting).

Possible values:

`campaign-verify``aegis`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the Brand Vetting resource.

* * *

## Create a Vetting

create-a-vetting page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/a2p/BrandRegistrations/{BrandSid}/Vettings`

Create a Vetting subresource. This associates a BrandRegistration resource and a Campaign Verify token.

The `VettingProvider` is `campaign-verify`, and the Campaign Verify token is provided in the `VettingId` parameter.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

brandSidSID<BN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Brand Registration resource of the vettings to create .

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

vettingProviderenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign Verify tokens) or “AEGIS” (Secondary Vetting).

Possible values:

`campaign-verify``aegis`

* * *

vettingIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the vetting

Select from available examples

Copy code block


    {


      "VettingProvider": "campaign-verify",


      "VettingId": "cv|1.0|tcr|10dlc|9975c339-d46f-49b7-a399-EXAMPLETOKEN|GQ3EXAMPLETOKENAXXBUNBT2AgL-LdQuPveFhEyY"


    }

Create a Vettings for a 527 political organizationLink to code sample: Create a Vettings for a 527 political organization

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

    async function createBrandVetting() {


    11

      const brandVetting = await client.messaging.v1


    12

        .brandRegistrations("BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .brandVettings.create({


    14

          vettingId:


    15

            "cv|1.0|tcr|10dlc|9975c339-d46f-49b7-a399-2e6d5ebac66d|EXAMPLEjEd8xSlaAgRXAXXBUNBT2AgL-LdQuPveFhEyY",


    16

          vettingProvider: "campaign-verify",


    17

        });


    18




    19

      console.log(brandVetting.accountSid);


    20

    }


    21




    22

    createBrandVetting();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",


    3

      "brand_sid": "BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    4

      "brand_vetting_sid": "VT12445353",


    5

      "vetting_provider": "campaign-verify",


    6

      "vetting_id": "cv|1.0|tcr|10dlc|9975c339-d46f-49b7-a399-2e6d5ebac66d|EXAMPLEjEd8xSlaAgRXAXXBUNBT2AgL-LdQuPveFhEyY",


    7

      "vetting_class": "POLITICAL",


    8

      "vetting_status": "IN_PROGRESS",


    9

      "date_created": "2021-01-27T14:18:35Z",


    10

      "date_updated": "2021-01-27T14:18:35Z",


    11

      "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings/VT12445353"


    12

    }

(warning)

## Warning

Don't create a [UsAppToPerson resource](/docs/messaging/api/usapptoperson-resource "UsAppToPerson resource") until the `vetting_status` is `SUCCESS`.

You can check the `vetting_status` with a [`GET` request](/docs/messaging/api/brand-vetting-resource#retrieve-a-vetting).

If the `vetting_status` is `SUCCESS`, the Campaign Verify token is successfully associated with your Brand. This allows you to use the `POLITICAL` special use case.

* * *

## Retrieve a Vetting

retrieve-a-vetting page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/a2p/BrandRegistrations/{BrandSid}/Vettings/{BrandVettingSid}`

Retrieve a Vetting using a `BrandVettingSid`.

You can use this request to check the `vetting_status`.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

brandSidSID<BN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Brand Registration resource of the vettings to read .

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

brandVettingSidSID<VT>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio SID of the third-party vetting record.

Pattern: `^VT[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve a VettingLink to code sample: Retrieve a Vetting

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

    async function fetchBrandVetting() {


    11

      const brandVetting = await client.messaging.v1


    12

        .brandRegistrations("BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .brandVettings("VTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .fetch();


    15




    16

      console.log(brandVetting.accountSid);


    17

    }


    18




    19

    fetchBrandVetting();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",


    3

      "brand_sid": "BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    4

      "brand_vetting_sid": "VTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "vetting_provider": "campaign-verify",


    6

      "vetting_id": "cv|1.0|tcr|10dlc|9975c339-d46f-49b7-a399-EXAMPLETOKEN|GQ3EXAMPLETOKENAXXBUNBT2AgL-LdQuPveFhEyY",


    7

      "vetting_class": "POLITICAL",


    8

      "vetting_status": "IN_PROGRESS",


    9

      "date_created": "2021-01-27T14:18:35Z",


    10

      "date_updated": "2021-01-27T14:18:35Z",


    11

      "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings/VT12445353"


    12

    }

* * *

## Retrieve a list of Vettings

retrieve-a-list-of-vettings page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/a2p/BrandRegistrations/{BrandSid}/Vettings`

This request returns all Vettings associated with a [BrandRegistrations resource](/docs/messaging/api/brand-registration-resource "BrandRegistrations resource").

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

brandSidSID<BN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Brand Registration resource of the vettings to read .

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

vettingProviderenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The third-party provider of the vettings to read

Possible values:

`campaign-verify``aegis`

Retrieve a list of Vettings for a BrandRegistrationLink to code sample: Retrieve a list of Vettings for a BrandRegistration

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

    async function listBrandVetting() {


    11

      const brandVettings = await client.messaging.v1


    12

        .brandRegistrations("BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .brandVettings.list({ limit: 20 });


    14




    15

      brandVettings.forEach((b) => console.log(b.accountSid));


    16

    }


    17




    18

    listBrandVetting();

### Response

Note about this response

Copy response


    1

    {


    2

      "meta": {


    3

        "page": 0,


    4

        "page_size": 50,


    5

        "first_page_url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings",


    6

        "previous_page_url": null,


    7

        "next_page_url": null,


    8

        "key": "data",


    9

        "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings"


    10

      },


    11

      "data": [


    12

        {


    13

          "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",


    14

          "brand_sid": "BN0044409f7e067e279523808d267e2d85",


    15

          "brand_vetting_sid": "VT12445353",


    16

          "vetting_provider": "campaign-verify",


    17

          "vetting_id": "cv|1.0|tcr|10dlc|9975c339-d46f-49b7-a399-EXAMPLETOKEN|GQ3EXAMPLETOKENAXXBUNBT2AgL-LdQuPveFhEyY",


    18

          "vetting_class": "POLITICAL",


    19

          "vetting_status": "IN_PROGRESS",


    20

          "date_created": "2021-01-27T14:18:35Z",


    21

          "date_updated": "2021-01-27T14:18:35Z",


    22

          "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings/VT12445353"


    23

        }


    24

      ]


    25

    }