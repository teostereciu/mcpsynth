# Feedback subresource

*Source: https://www.twilio.com/docs/messaging/api/message-feedback-resource*

---

# Feedback subresource

Positive FeedbackNegative Feedback

* * *

Feedback is a subresource of [Messages](/docs/messaging/api/message-resource "Messages") and represents the reported outcome of tracking the performance of a user action taken by the recipient of the message.

You can [create Feedback](/docs/messaging/api/message-feedback-resource#create-feedback "create Feedback") to confirm that the recipient of the associated Message performed a tracked user action.

(information)

## Info

For more information on why, when and how to send Feedback, see our guide [How to Optimize Message Deliverability with Message Feedback](/docs/messaging/guides/send-message-feedback-to-twilio "How to Optimize Message Deliverability with Message Feedback"). It explains what suitable tracked user actions of message recipients are and how they relate to the [Message Insights One-time Password (OTP) Conversion Report](/docs/messaging/features/messaging-insights/dashboards#otp-conversion-dashboard "Message Insights One-time Password \(OTP\) Conversion Report").

(information)

## Info

Looking for step-by-step instructions on tracking the delivery of your sent messages based on Twilio- and carrier-captured status data? Follow our guide to [Tracking the Message Status of Outbound Messages](/docs/messaging/guides/track-outbound-message-status "Tracking the Message Status of Outbound Messages") in the programming language of your choice.

* * *

## Feedback Properties

feedback-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") associated with this MessageFeedback resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messageSidSID<SM|MM>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource associated with this MessageFeedback resource.

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

outcomeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reported outcome indicating whether there is confirmation that the Message recipient performed a tracked user action. Can be: `unconfirmed` or `confirmed`. For more details see [How to Optimize Message Deliverability with Message Feedback](/docs/messaging/guides/send-message-feedback-to-twilio "How to Optimize Message Deliverability with Message Feedback").

Possible values:

`confirmed``unconfirmed`

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when this MessageFeedback resource was created, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when this MessageFeedback resource was last updated, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

## Outcome Values

outcome-values page anchor

Positive FeedbackNegative Feedback

The following are the possible values for the `Outcome` parameter:

| ENUM:OUTCOME possible values in REST API format
---|---
`confirmed`| The recipient of a Message performed a tracked user action and confirmation was reported by creating a Feedback subresource with the outcome set to confirmed. For more details see How to Optimize Message Deliverability with Message Feedback.
`unconfirmed`| The initial value for a Message created with ProvideFeedback=True. The reported outcome is unconfirmed until a Feedback subresource is created with an outcome property of confirmed.

* * *

## Create Feedback

create-feedback page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Feedback.json`

(warning)

## Warning

To track and provide Message Feedback for a Message, you must set the `ProvideFeedback` parameter to `true` when you first [create the Message](/docs/messaging/api/message-resource#create-a-message-resource "create the Message"). Upon Message creation, the `outcome` of the Message Feedback will then initially be treated as `unconfirmed`.

For more information on why, when and how to send Message Feedback, see our guide [How to Optimize Message Deliverability with Message Feedback](/docs/messaging/guides/send-message-feedback-to-twilio "How to Optimize Message Deliverability with Message Feedback").

You can use this action to create Message Feedback confirming the performance of a tracked user action.

Pass the `Outcome` parameter with value `confirmed` to update the Message Feedback once the associated Message was received and the message recipient performed the tracked user action based on the received message.

(information)

## Info

Update the Message Feedback even if the Message is received with a delay once the conditions for confirmation are met. This ensures the Messaging Insights are current and message delivery optimizations are based on complete information.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") associated with the Message resource for which to create MessageFeedback.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messageSidSID<SM|MM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource for which to create MessageFeedback.

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

outcomeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reported outcome indicating whether there is confirmation that the Message recipient performed a tracked user action. Can be: `unconfirmed` or `confirmed`. For more details see [How to Optimize Message Deliverability with Message Feedback](/docs/messaging/guides/send-message-feedback-to-twilio "How to Optimize Message Deliverability with Message Feedback").

Possible values:

`confirmed``unconfirmed`

Copy code block


    {


      "Outcome": "confirmed"


    }

Create Feedback to confirm the performance of the tracked user actionLink to code sample: Create Feedback to confirm the performance of the tracked user action

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

    async function createMessageFeedback() {


    11

      const feedback = await client


    12

        .messages("SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .feedback.create({ outcome: "confirmed" });


    14




    15

      console.log(feedback.accountSid);


    16

    }


    17




    18

    createMessageFeedback();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "date_created": "Thu, 30 Jul 2015 20:00:00 +0000",


    4

      "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000",


    5

      "message_sid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    6

      "outcome": "confirmed",


    7

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json"


    8

    }

* * *

## What's next?

whats-next page anchor

Positive FeedbackNegative Feedback

Now that you know how to work with the Feedback subresource, you should check out the following:

  * View your reported Message Feedback information in the [Console(link takes you to an external page)](https://www.twilio.com/console/sms/insights/feedback "Console") to help you monitor and understand your message deliverability.