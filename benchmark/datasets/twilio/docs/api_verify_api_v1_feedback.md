# Twilio Verify Feedback API

*Source: https://www.twilio.com/docs/verify/api/v1/feedback*

---

# Twilio Verify Feedback API

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

(information)

## Info

The Verify Feedback API is intended for customers who use the optional '_custom_code_ ' feature, where they generate their own **One-Time-Passcode** (OTP) that Verify sends. Contact [Twilio Sales(link takes you to an external page)](https://www.twilio.com/help/sales "Twilio Sales") and we'll help you enable this feature.

If you're not using '_custom_code_ ', the Feedback functionality is already provided by the standard workflow of the Verify API.

Twilio Verify, when used with our code generation and validation, uses Twilio's route intelligence engine to optimize SMS and Voice deliverability. This means that we will automatically retry with different routes if users request multiple verification codes without validating codes or if we notice performance is worse than our baseline. Customers who use pin verification through the Verify API get these benefits of deliverability tuning and monitoring feedback of Twilio's system.

When customers use our `custom_code` feature to send and validate their own codes, we don't get the same transparency. In order to achieve insights into possible deliverability issues, we built a proxy to the Twilio Feedback API that customers can use to send us this data. This allows us to optimize routing and ensure that your verification codes are sent as quickly and reliably as possible.

By using the Feedback API, we'll be able to proactively address potential issues caused by interruptions in telecom routes that affect deliverability. This API will help ensure your user gets a verification code regardless of the telecom infrastructure circumstances.

* * *

## Send Message Feedback

send-message-feedback page anchor

Positive FeedbackNegative Feedback

This call will report the status of a message.

Copy code block


    POST https://api.authy.com/2010-04-01/Accounts/Messages/SMS/Messages/{SMSMessageSid}/Feedback

### URL

url page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
ApiKey| String| The [API Key](/docs/verify/api "API Key") for your Verify Application.
SMSMessageSid| String| The `sms_id` found in the response of a [phone verification start](/docs/verify/api/verification#fetch-a-verification "phone verification start").

### Parameters

parameters page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
Outcome| String (optional)| `received` if the customer correctly entered the code provided in the message or `not-received` if the customer took no action within 2 minutes. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )

* * *

## Examples

examples page anchor

Positive FeedbackNegative Feedback

### Custom Code Feedback

custom-code-feedback page anchor

Positive FeedbackNegative Feedback

Start by sending a verification code to a user's phone number.

Copy code block


    1

    curl 'https://api.authy.com/protected/json/phones/verification/start' \


    2

    -H "X-Authy-API-Key: d57d919d11e6b221c9bf6f7c882028f9" \


    3

    -d via='sms' \


    4

    -d phone_number='111-111-1111' \


    5

    -d country_code=1 \


    6

    -d locale='en' \


    7

    -d custom_code=12345

Sample response:

Copy code block


    1

    {


    2

      "carrier": "AT&T Wireless",


    3

      "is_cellphone": true,


    4

      "message": "Text message sent to +1 111-111-1111.",


    5

      "seconds_to_expire": 599,


    6

      "uuid": "caf8eb00-6d03-1234-5678-0eb34144aeb2",


    7

      "sms_id": "cafd7a60-6d03-1234-5678-0eb34144aeb2", // You'll use this ID to send feedback


    8

      "success": true


    9

    }

This will send an SMS to the user.

If the user correctly enters the code in your application send the following:

Copy code block


    1

    curl -XPOST 'https://api.authy.com/2010-04-01/Accounts/d57d919d11e6b221c9bf6f7c882028f9/SMS/Messages/cafd7a60-6d03-1234-5678-0eb34144aeb2/Feedback.json' \


    2

    -d Outcome='received'

If the user takes no action within 2 minutes send the following:

Copy code block


    1

    curl -XPOST 'https://api.authy.com/2010-04-01/Accounts/d57d919d11e6b221c9bf6f7c882028f9/SMS/Messages/cafd7a60-6d03-1234-5678-0eb34144aeb2/Feedback.json' \


    2

    -d Outcome='not-received'

Response

Copy code block


    1

    {


    2

      "account_sid": "",


    3

      "message_sid": "cafd7a60-6d03-1234-5678-0eb34144aeb2",


    4

      "outcome": "received",


    5

      "date_created": "Wed, 18 Jul 2018 21:59:40 +0000",


    6

      "date_updated": "Wed, 18 Jul 2018 22:02:29 +0000",


    7

      "uri": "",


    8

      "success": true


    9

    }

Your `account_sid` and `uri` will be empty in this response.