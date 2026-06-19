# Messaging API Overview

*Source: https://www.twilio.com/docs/messaging/api*

---

# Messaging API Overview

Positive FeedbackNegative Feedback

* * *

With the Programmable Messaging REST API, you can add messaging capabilities to your application.

* * *

## Base URLs

base-urls page anchor

Positive FeedbackNegative Feedback

To ensure data privacy, Twilio serves its APIs over HTTPS.

Messaging-related APIs use three base URLs:

### Twilio API base URL

twilio-api-base-url page anchor

Positive FeedbackNegative Feedback

The following API resources that process SMS messages point to the Base URL of `https://api.twilio.com/2010-04-01`:

  * [Messages resource](/docs/messaging/api/message-resource "Messages resource")
    * [Feedback subresource](/docs/messaging/api/message-feedback-resource "Feedback subresource")
    * [Media subresource](/docs/messaging/api/media-resource "Media subresource")


The following API resources that manage [Messaging Services](/docs/messaging/services "Messaging Services") point to `https://messaging.twilio.com/v1`:

  * [Services resource](/docs/messaging/api/service-resource "Services resource")
    * [PhoneNumbers subresource](/docs/messaging/api/phonenumber-resource "PhoneNumbers subresource")
    * [Shortcodes subresource](/docs/messaging/api/services-shortcode-resource "Shortcodes subresource")
    * [AlphaSenders subresource](/docs/messaging/api/alphasender-resource "AlphaSenders subresource")
    * [DestinationAlphaSenders subresource](/docs/messaging/api/destination-alphasender-resource "DestinationAlphaSenders subresource")
    * [ChannelSenders subresource](/docs/messaging/api/messaging-service-channelsender-resource "ChannelSenders subresource")


The following API resources that report on deactivated phone numbers and process toll-free verification requests also point to `https://messaging.twilio.com/v1`:

  * [Deactivations resource](/docs/messaging/api/deactivations-resource "Deactivations resource")
  * [Verifications resource](/docs/messaging/api/tollfree-verification-resource "Verifications resource")


The API resource that reports on [per-country SMS pricing](/docs/messaging/api/pricing "per-country SMS pricing") points to the `https://pricing.twilio.com/v1` base URL.

* * *

## Authentication

authentication page anchor

Positive FeedbackNegative Feedback

To authenticate requests to the Twilio APIs, Twilio supports [HTTP Basic authentication(link takes you to an external page)](https://en.wikipedia.org/wiki/Basic_access_authentication "HTTP Basic authentication"). Use your _API key_ as the username and your _API key secret_ as the password. You can create an API key either [in the Twilio Console](/docs/iam/api-keys/keys-in-console "in the Twilio Console") or [using the API](/docs/iam/api-keys/key-resource-v1 "using the API").

**Note** : Twilio recommends using API keys for authentication in production apps. For local testing, you can use your Account SID as the username and your Auth token as the password. You can find your Account SID and Auth Token in the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console").

Learn more about [Twilio API authentication](/docs/usage/requests-to-twilio "Twilio API authentication").

Here's an example of authenticating with the API:

Copy code block


    1

    curl -G https://api.twilio.com/2010-04-01/Accounts \


    2

         -u $TWILIO_API_KEY:$TWILIO_API_KEY_SECRET

* * *

## Use the Programmable Messaging API

use-the-programmable-messaging-api page anchor

Positive FeedbackNegative Feedback

(information)

## Info

Twilio monitors messages to prevent content violating the [Acceptable Use Policy(link takes you to an external page)](https://www.twilio.com/en-us/legal/aup "Acceptable Use Policy") (AUP)_._ This helps to ensure that Twilio Messaging is seen as a trustworthy, high engagement channel and will not slow down the delivery of messages.

If a message you send has violated the AUP, it will be returned and you will receive an error code which identifies the necessary changes you need to make before sending it again.

### Send messages

send-messages page anchor

Positive FeedbackNegative Feedback

To send an outbound message, send a `POST` request to the [Messages resource](/docs/messaging/api/message-resource "Messages resource").

  * To [send media messages](/docs/messaging/tutorials/how-to-send-sms-messages "send media messages"), use the `MediaUrl` parameter in the request.
  * To [schedule an outbound Message](/docs/messaging/features/message-scheduling "schedule an outbound Message") to be sent in the future, use the `ScheduleType` and `SendAt` parameters in the request.
  * To [send messages with shortened links](/docs/messaging/features/link-shortening "send messages with shortened links"), use the `ShortenUrls` parameter in the request.
    * **Note** : This feature is available only if you use a [Messaging Service](/docs/messaging/services "Messaging Service").


To learn more about how to receive and reply to messages, see [Receive and Reply to Messages Guide](/docs/messaging/tutorials/how-to-receive-and-reply "Receive and Reply to Messages Guide").

### Fetch, list, update, and delete messages

fetch-list-update-and-delete-messages page anchor

Positive FeedbackNegative Feedback

Use the [Messages resources](/docs/messaging/api/message-resource "Messages resources") to fetch, list, and delete Messages associated with your account.

Redact messages by updating a Message resource.

### Fetch, list, and delete media

fetch-list-and-delete-media page anchor

Positive FeedbackNegative Feedback

Twilio creates a [Media subresource](/docs/messaging/api/media-resource "Media subresource") when an incoming or outgoing Message resource contains media.

You can fetch, list, and delete Media subresources.

### Manage your short codes

manage-your-short-codes page anchor

Positive FeedbackNegative Feedback

Fetch, list, and update your Account's short codes with the [ShortCodes subresource](/docs/messaging/api/short-code-resource "ShortCodes subresource").

### Track message feedback

track-message-feedback page anchor

Positive FeedbackNegative Feedback

Track user-reported outcomes of Messages with the [Feedback subresource](/docs/messaging/api/message-feedback-resource "Feedback subresource").

### Manage your Messaging Services

manage-your-messaging-services page anchor

Positive FeedbackNegative Feedback

Create, fetch, read, update, and delete Messaging Services with the [Services resource](/docs/messaging/api/service-resource "Services resource").

Manage your Messaging Services' senders with the following subresources:

  * [ShortCodes subresource](/docs/messaging/api/services-shortcode-resource "ShortCodes subresource")
  * [AlphaSenders subresource](/docs/messaging/api/alphasender-resource "AlphaSenders subresource")
  * [DestinationAlphaSenders subresource](/docs/messaging/api/destination-alphasender-resource "DestinationAlphaSenders subresource")
  * [PhoneNumbers subresource](/docs/messaging/api/phonenumber-resource "PhoneNumbers subresource")
  * [ChannelSenders subresource](/docs/messaging/api/messaging-service-channelsender-resource "ChannelSenders subresource")


### Check SMS pricing by country

check-sms-pricing-by-country page anchor

Positive FeedbackNegative Feedback

Check inbound and outbound SMS message pricing with the [Messaging Countries subresources](/docs/messaging/api/pricing "Messaging Countries subresources") of the Pricing API.

### Retrieve a list of deactivated US phone numbers

retrieve-a-list-of-deactivated-us-phone-numbers page anchor

Positive FeedbackNegative Feedback

Fetch a list of all US phone numbers that were deactivated on a given day with the [Deactivations resource](/docs/messaging/api/deactivations-resource "Deactivations resource").

### Verify that your toll-free number complies with regulations

verify-that-your-toll-free-number-complies-with-regulations page anchor

Positive FeedbackNegative Feedback

Demonstrate that your toll-free number complies with US and Canadian SMS regulations. Submit, update, or delete toll-free verification (TFV) requests with the [Verifications resource](/docs/messaging/api/tollfree-verification-resource "Verifications resource").

* * *

## Additional resources

additional-resources page anchor

Positive FeedbackNegative Feedback

  * [SMS developer quickstart](/docs/messaging/quickstart "SMS developer quickstart")
  * For inspiration, read the [Twilio Blog(link takes you to an external page)](https://www.twilio.com/blog/search-results?search=sms "Twilio Blog") on building messaging applications with various languages and tools.
  * Get started with [toll-free verification](/docs/messaging/compliance/toll-free/api-onboarding "toll-free verification").
  * For help troubleshooting your Programmable Messaging application, check out the docs on [Debugging Common Issues](/docs/messaging/guides/debugging-common-issues "Debugging Common Issues") and [Debugging Tools](/docs/messaging/guides/debugging-tools "Debugging Tools").
  * [Learn more about Twilio's Global Infrastructure](/docs/global-infrastructure "Learn more about Twilio's Global Infrastructure"), which allows you to control where your application's Twilio-related data is routed, processed, and stored.