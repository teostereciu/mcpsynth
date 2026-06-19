# Programmable Voice API Overview

*Source: https://www.twilio.com/docs/voice/api*

---

# Programmable Voice API Overview

Positive FeedbackNegative Feedback

* * *

Twilio's [Voice API(link takes you to an external page)](https://www.twilio.com/en-us/voice "Voice API") helps you to make, receive, and monitor calls around the world.

Using this REST API, you can [make outbound phone calls](/docs/voice/tutorials/how-to-make-outbound-phone-calls "make outbound phone calls"), [modify calls in progress](/docs/voice/tutorials/how-to-modify-calls-in-progress "modify calls in progress"), and [query metadata](/docs/voice/tutorials/how-to-retrieve-call-logs "query metadata") about calls you've created. More advanced call features like [programmatic call control](/docs/voice/api#programmatic-call-control "programmatic call control"), creating [conference calls and call queues](/docs/voice/api "conference calls and call queues"), [call recordings](/docs/voice/api#record-calls "call recordings"), and [conversational IVRs](/docs/voice/api "conversational IVRs") are at your fingertips with Twilio's Programmable Voice.

You can also use the API to route voice calls with global reach to phones, [browsers](/docs/voice/sdks/javascript "browsers"), [SIP domains](/docs/voice/api/sip-interface "SIP domains"), and [mobile applications](/docs/voice/sdks "mobile applications").

(information)

## Info

You can obtain numbers by using the [Phone Numbers API](/docs/phone-numbers "Phone Numbers API")

* * *

## Base URL

base-url page anchor

Positive FeedbackNegative Feedback

The Twilio REST API is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.

`https://api.twilio.com/2010-04-01` is the base URL for the following resources:

  * [Calls resource](/docs/voice/api/call-resource "Calls resource")
    * [Events subresource](/docs/voice/api/call-event-resource "Events subresource")
    * [Calls Transcriptions subresource](/docs/voice/api/realtime-transcription-resource "Calls Transcriptions subresource")
    * [Streams subresource](/docs/voice/api/stream-resource "Streams subresource")
    * [UserDefinedMessages subresource](/docs/voice/api/userdefinedmessage-resource "UserDefinedMessages subresource")
    * [UserDefinedMessageSubscription subresource](/docs/voice/api/userdefinedmessagesubscription-resource "UserDefinedMessageSubscription subresource")
    * [SIPREC subresource](/docs/voice/api/siprec "SIPREC subresource")
    * [Payments subresource](/docs/voice/api/payment-resource "Payments subresource")
  * [Recordings resource](/docs/voice/api/recording "Recordings resource")
  * [Transcriptions resource](/docs/voice/api/recording-transcription "Transcriptions resource")
  * [OutgoingCallerIds resource](/docs/voice/api/outgoing-caller-ids "OutgoingCallerIds resource")
  * [Conferences resource](/docs/voice/api/conference-resource "Conferences resource")
    * [Participant subresource](/docs/voice/api/conference-participant-resource "Participant subresource")
  * [Queues resource](/docs/voice/api/queue-resource "Queues resource")
    * [Members subresource](/docs/voice/api/member-resource "Members subresource")


`https://voice.twilio.com/v1` is the base URL for the following resources:

  * [Countries resource](/docs/voice/api/dialingpermissions-country-resource "Countries resource")
    * [HighRiskSpecialPrefixes subresource](/docs/voice/api/dialingpermissions-highriskspecialprefix-resource "HighRiskSpecialPrefixes subresource")
  * [BulkCountryUpdates resource](/docs/voice/api/dialingpermissions-bulkcountryupdate-resource "BulkCountryUpdates resource")
  * [Settings resource](/docs/voice/api/dialingpermissions-settings-resource "Settings resource")


`https://voice.twilio.com/v2` is the base URL for the following resources:

  * [Client resource](/docs/voice/api/clientconfiguration-resource "Client resource")


(information)

## Info

You can control your connectivity into Twilio's platform by including your specific [edge location](/docs/global-infrastructure/edge-locations "edge location") in the subdomain. This will allow you to bring Twilio's public or private network connectivity closer to your applications for improved performance.

For instance, customers with infrastructure in Australia can make use of the `sydney` edge location by using the base URL of:

Copy code block


    https://api.sydney.us1.twilio.com/2010-04-01

* * *

## Voice API Authentication

voice-api-authentication page anchor

Positive FeedbackNegative Feedback

To authenticate requests to the Twilio APIs, Twilio supports [HTTP Basic authentication(link takes you to an external page)](https://en.wikipedia.org/wiki/Basic_access_authentication "HTTP Basic authentication"). Use your _API key_ as the username and your _API key secret_ as the password. You can create an API key either [in the Twilio Console](/docs/iam/api-keys/keys-in-console "in the Twilio Console") or [using the API](/docs/iam/api-keys/key-resource-v1 "using the API").

**Note** : Twilio recommends using API keys for authentication in production apps. For local testing, you can use your Account SID as the username and your Auth token as the password. You can find your Account SID and Auth Token in the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console").

Learn more about [Twilio API authentication](/docs/usage/requests-to-twilio "Twilio API authentication").

Copy code block


    1

    curl -G https://api.twilio.com/2010-04-01/Accounts \


    2

        -u $TWILIO_API_KEY:$TWILIO_API_KEY_SECRET

* * *

## Make and manage calls with the Voice API

make-and-manage-calls-with-the-voice-api page anchor

Positive FeedbackNegative Feedback

Twilio's Voice API lets you make and manage calls programmatically.

To make an outbound call with the API, make a `POST` to the [Calls resource](/docs/voice/api/call-resource "Calls resource").

You can also leverage the REST API to query metadata and manage state for:

  * [Call quality feedback](/docs/voice/api/call-resource "Call quality feedback")
  * [Conferences](/docs/voice/api/conference-resource "Conferences") and [Participants](/docs/voice/api/conference-participant-resource "Participants")
  * [Outgoing caller IDs](/docs/voice/api/outgoing-caller-ids "Outgoing caller IDs")
  * [Queues](/docs/voice/api/queue-resource "Queues") and [Members](/docs/voice/api/member-resource "Members")
  * [Recordings](/docs/voice/api/recording "Recordings") and [Transcriptions](/docs/voice/api/recording-transcription "Transcriptions")


### Leverage the Voice SDKs to make or receive calls

leverage-the-voice-sdks-to-make-or-receive-calls page anchor

Positive FeedbackNegative Feedback

Make, receive, or manage calls from any web interface or mobile application.

For step-by-step instructions on how to do this with one of our supported SDKs, check out the quickstarts for:

  * [C#/.NET](/docs/voice/quickstart/server "C#/.NET")
  * [Java](/docs/voice/quickstart/server "Java")
  * [Node.js](/docs/voice/quickstart/server "Node.js")
  * [PHP](/docs/voice/quickstart/server "PHP")
  * [Python](/docs/voice/quickstart/server "Python")
  * [Ruby](/docs/voice/quickstart/server "Ruby")
  * [Go](/docs/voice/quickstart/server "Go")
  * [iOS - Swift(link takes you to an external page)](https://github.com/twilio/voice-quickstart-swift#quickstart "iOS - Swift")
  * [iOS - Objective-C(link takes you to an external page)](https://github.com/twilio/voice-quickstart-objc#quickstart "iOS - Objective-C")
  * [Android(link takes you to an external page)](https://github.com/twilio/voice-quickstart-android#quickstart "Android")
  * [Voice JavaScript SDK](/docs/voice/sdks/javascript/get-started "Voice JavaScript SDK") (using Twilio [Functions](/docs/serverless/functions-assets/functions "Functions"))


### Programmatic call control

programmatic-call-control page anchor

Positive FeedbackNegative Feedback

The basics of most call flows start with the ability to say strings of text and gather DTMF keypad input.

You can use the Voice API directly to [create outbound calls](/docs/voice/api/call-resource "create outbound calls") and query and manage state for [conferences](/docs/voice/conference "conferences"), [queues](/docs/voice/api/queue-resource "queues"), and [recordings](/docs/voice/api/recording "recordings").

Twilio's markup language, [TwiML](/docs/glossary/what-is-twilio-markup-language-twiml "TwiML"), is the primary language used to control actions on Twilio. For instance, you'll need to use [TwiML's <Say>](/docs/voice/twiml/say "TwiML's <Say>") to read some text to a person on a Twilio call.

Twilio provides SDKs in 6 supported web programming languages: [C#/.NET(link takes you to an external page)](https://github.com/twilio/twilio-csharp "C#/.NET"), [Java(link takes you to an external page)](https://github.com/twilio/twilio-java "Java"), [Node.js(link takes you to an external page)](https://github.com/twilio/twilio-node "Node.js"), [PHP(link takes you to an external page)](https://github.com/twilio/twilio-php "PHP"), [Python(link takes you to an external page)](https://github.com/twilio/twilio-python "Python"), and [Ruby(link takes you to an external page)](https://github.com/twilio/twilio-ruby "Ruby"). These SDKs make including TwiML in your web application a seamless process.

For instance, you can use one of our SDKs to read some text to a caller and gather their input via keypad: [select your language of choice to get started](/docs/voice/tutorials/how-to-gather-user-input-via-keypad "select your language of choice to get started").

### Conference calls & Queueing

conference-calls--queueing page anchor

Positive FeedbackNegative Feedback

Twilio's TwiML provides intelligent [Conference](/docs/voice/conference "Conference") and [Queue](/docs/voice/twiml/queue "Queue") primitives to take the heavy lifting out of building seamless call experiences:

  * Create a Conference by leveraging TwiML's [<Dial>](/docs/voice/twiml/dial "<Dial>") with [<Conference>](/docs/voice/twiml/conference "<Conference>"). When you add a caller to a conference this way, Twilio creates a [Conference resource](/docs/voice/api/conference-resource "Conference resource") and a [Participant subresource](/docs/voice/api/conference-participant-resource "Participant subresource") to represent the caller who joined.
  * Use the Conference resource to list the conferences in your account, update a conference's status, and query information about participants in a given conference.
  * Learn how to [create and manage conference calls from your web applications](/docs/voice/tutorials/how-to-create-conference-calls "create and manage conference calls from your web applications") using Twilio's SDKs.
  * You can create a new Queue by making a `POST` request to the [Queues resource](/docs/voice/api/queue-resource "Queues resource") or by leveraging the [<Enqueue>](/docs/voice/twiml/enqueue "<Enqueue>") verb in your TwiML document. Learn how to [use Twilio's Queue feature to create a call queueing system](/docs/voice/queue-calls "use Twilio's Queue feature to create a call queueing system").


### Record calls

record-calls page anchor

Positive FeedbackNegative Feedback

With Twilio's Voice API, you can record, store, and transcribe calls with a little bit of code:

  * If you're using the REST API to create your call, set [`Record=true`](/docs/voice/api/call-resource#create-a-call-resource).
  * You can also generate a recording with [TwiML](/docs/voice/twiml/dial#record "TwiML") or by making a `POST` request to the [Recordings resource](/docs/voice/api/recording#create-a-recording-resource "Recordings resource") of a live call.
  * Learn how to record calls made from your web application, by taking a spin through this[tutorial on recording outgoing and inbound calls with the server-side SDKs](/docs/voice/tutorials/how-to-record-phone-calls "tutorial on recording outgoing and inbound calls with the server-side SDKs").
  * Review our [support article(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/223133027-Transcribe-entire-phone-calls-with-Twilio "support article") for options to transcribe your call recording.


* * *

## Manage SIP calls with Twilio's API

manage-sip-calls-with-twilios-api page anchor

Positive FeedbackNegative Feedback

Route calls from your existing VoIP infrastructure to Twilio for programmatic call control - without migrating hardware or carriers with SIP interface.

[Programmable Voice SIP](/docs/voice/api/sip-interface "Programmable Voice SIP") lets you route your voice calls with global reach to any landline phone, mobile phone, browser, mobile app, or any other SIP endpoint.

* * *

## Explore rich communications

explore-rich-communications page anchor

Positive FeedbackNegative Feedback

Explore the power of Twilio's Voice API with our [quickstarts](/docs/voice/quickstart "quickstarts"), see how to [make calls](/docs/voice/tutorials/how-to-make-outbound-phone-calls "make calls") or [respond to incoming calls](/docs/voice/tutorials/how-to-respond-to-incoming-phone-calls "respond to incoming calls"), [modify calls](/docs/voice/tutorials/how-to-modify-calls-in-progress "modify calls"), and more by diving into our [collection of tutorials for Programmable Voice](/docs/voice/tutorials "collection of tutorials for Programmable Voice").

* * *

## Get help integrating the Voice API

get-help-integrating-the-voice-api page anchor

Positive FeedbackNegative Feedback

Twilio's Voice API is a flexible building block that can take you from making your first phone call.

While we hope this page gives a good overview of what you can do with the API, we're only scratching the surface: check out our [troubleshooting tips](/docs/voice/troubleshooting "troubleshooting tips") to learn about Twilio's debugging tools, common issues, and other tools and add-ons like [Voice Insights(link takes you to an external page)](https://www.twilio.com/en-us/voice/insights "Voice Insights").

If you need any help integrating the Programmable Voice API or want to talk best practices, get in touch. You can give us feedback by using the rating widget on this page, [talking to support(link takes you to an external page)](https://help.twilio.com "talking to support"), [talking to sales(link takes you to an external page)](https://www.twilio.com/en-us/help/sales "talking to sales"), or [reaching out on Twitter(link takes you to an external page)](https://www.twitter.com/twilio "reaching out on Twitter").

Let's build something amazing.