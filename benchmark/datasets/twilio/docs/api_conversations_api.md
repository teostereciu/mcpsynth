# The Conversations API Overview

*Source: https://www.twilio.com/docs/conversations/api*

---

# The Conversations API Overview

Positive FeedbackNegative Feedback

* * *

The Conversations API allows you to create conversational (back-and-forth) messaging across multiple channels: Chat, WhatsApp, and SMS.

* * *

## API Base URL

api-base-url page anchor

Positive FeedbackNegative Feedback

All URLs in the reference documentation use the following base URL:

Copy code block


    1

    https://conversations.twilio.com/v1


    2

(information)

## Info

You can control your connectivity into Twilio's platform by including your specific [edge location](/docs/global-infrastructure/edge-locations "edge location") in the subdomain. This will allow you to bring Twilio's public or private network connectivity closer to your applications for improved performance.

For instance customers with infrastructure in Australia can make use of the `sydney` edge location by using the base url of:

Copy code block


    https://conversations.sydney.us1.twilio.com/v1

* * *

## Authentication

authentication page anchor

Positive FeedbackNegative Feedback

To authenticate requests to the Twilio APIs, Twilio supports [HTTP Basic authentication(link takes you to an external page)](https://en.wikipedia.org/wiki/Basic_access_authentication "HTTP Basic authentication"). Use your _API key_ as the username and your _API key secret_ as the password. You can create an API key either [in the Twilio Console](/docs/iam/api-keys/keys-in-console "in the Twilio Console") or [using the API](/docs/iam/api-keys/key-resource-v1 "using the API").

**Note** : Twilio recommends using API keys for authentication in production apps. For local testing, you can use your Account SID as the username and your Auth token as the password. You can find your Account SID and Auth Token in the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console").

Learn more about [Twilio API authentication](/docs/usage/requests-to-twilio "Twilio API authentication").

* * *

## Resources

resources page anchor

Positive FeedbackNegative Feedback

The [Conversation resource](/docs/conversations/api/conversation-resource "Conversation resource") is the primary resource, representing a unique thread of a conversation.

A Conversation has the following sub-resources:

  * [Conversation Participants](/docs/conversations/api/conversation-participant-resource "Conversation Participants")
  * [Conversation Messages](/docs/conversations/api/conversation-message-resource "Conversation Messages")
  * [Conversation-Scoped Webhooks](/docs/conversations/api/conversation-scoped-webhook-resource "Conversation-Scoped Webhooks").


The [Conversation Webhook resource](/docs/conversations/api/conversation-scoped-webhook-resource "Conversation Webhook resource") covers webhook configurations for all Conversations.

* * *

## Getting started

getting-started page anchor

Positive FeedbackNegative Feedback

Refer to our [quickstart guide](/docs/conversations/quickstart "quickstart guide") for a step by step introduction to Conversations and an overview of commonly used features.