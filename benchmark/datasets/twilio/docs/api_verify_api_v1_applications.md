# Verify Applications

*Source: https://www.twilio.com/docs/verify/api/v1/applications*

---

# Verify Applications

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

Verify v1 API has reached End of Sale. It is now closed to new customers and will be fully deprecated in the future.

For new development, we encourage you to use the [Verify v2 API](/docs/verify/api "Verify v2 API"). v2 has an improved developer experience and new features, including:

  * Twilio server-side SDKs in multiple languages
  * [PSD2](/docs/verify/verifying-transactions-psd2 "PSD2") Secure Customer Authentication Support
  * [Improved Visibility and Insights](/docs/verify/migrating-1x-2x#improved-visibility-and-insights "Improved Visibility and Insights")


Existing customers will not be impacted at this time until Verify v1 API has reached End of Life. For more information about migration, see [Migrating from 1.x to 2.x](/docs/verify/migrating-1x-2x "Migrating from 1.x to 2.x").

Twilio Verify API applications are created through the [Verify section of the console(link takes you to an external page)](https://www.twilio.com/console/verify/applications "Verify section of the console"). You may have many applications in one Twilio account, but each Application you create will be isolated with a separate application name and separate API key.

* * *

## Create New Application

create-new-application page anchor

Positive FeedbackNegative Feedback

To create a new Verify application, click the red plus ('+') button from the [console(link takes you to an external page)](https://www.twilio.com/console/verify/applications "console"):

Expand image

You will be taken to your application's Settings page, where you can find your Application ID:

Expand image

It is also possible to get information about a Verify API Application via the API itself.

* * *

## Get Application Details

get-application-details page anchor

Positive FeedbackNegative Feedback

This call will retrieve the application details:

  1. Name:
  2. Plan:
  3. SMS-enabled


Copy code block


    GET https://api.authy.com/protected/{FORMAT}/app/details

### Parameters

parameters page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
user_ip| String (optional)| IP of the user requesting to see the application details. ([📇 PII](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields "📇 PII") )

### Response

response page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
app| App| Object with information about the application. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
success| Boolean| True if the request was successful. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
message| String| A message indicating the result of the operation. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )

### Example

example page anchor

Positive FeedbackNegative Feedback

Copy code block


    1

    curl 'https://api.authy.com/protected/json/app/details' \


    2

    -H "X-Authy-API-Key: d57d919d11e6b221c9bf6f7c882028f9"

Sample response:

Copy code block


    1

    {


    2

      "app": {


    3

        "name": "Verify Sample",


    4

        "plan": "pay_as_you_go",


    5

        "sms_enabled": true,


    6

        "phone_calls_enabled": true,


    7

        "app_id": 11111,


    8

        "onetouch_enabled": true


    9

      },


    10

      "message": "Application information.",


    11

      "success": true


    12

    }