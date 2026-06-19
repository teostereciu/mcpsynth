# SIP and TwiML Interaction

*Source: https://www.twilio.com/docs/voice/api/sip-twiml*

---

# SIP and TwiML Interaction

Positive FeedbackNegative Feedback

* * *

SIP calls interact with TwiML in virtually the same way as [inbound phone calls and Client](/docs/quickstart "inbound phone calls and Client"). When Twilio receives an incoming INVITE to your Twilio SIP domain and authenticates it, it passes a 180 Ringing SIP response code to your SIP endpoint. Twilio then looks up the URLs associated with your SIP domain and makes an HTTP request to the VoiceUrl.

When requesting your TwiML, Twilio will pass several parameters to your application from the original SIP call:

Parameter Name| Description|
---|---|---
To| The URI of the INVITE|
From| "From" header passed in the INVITE|
SipDomain| The Twilio SIP Domain to which the INVITE was sent|
SipDomainSid| The Originating Twilio SIP Domain SID|
SipCallId| The Call-Id of the incoming INVITE|
SipSourceIp| The IP Address the incoming INVITE came from.|
SipHeader_<name>| X- headers in the incoming INVITE are passed as SipHeader_<name> parameters, where <name> is the header key. You can receive multiple of these.|

Upon receiving a response with valid TwiML, Twilio begins executing the instructions contained within the TwiML. If the instructions are <Say>, <Play>, <Record>, <Dial>, or <Gather>, Twilio sends a `200 OK` SIP response code to your endpoint and establishes the call.

If your application passes back a `<Redirect>` verb, the redirect document is requested and Twilio continues in the 180 Ringing state.

If your application sends back a `<Reject reason="busy">`, Twilio returns a _486 Busy_ SIP response code and the call setup is denied. If your application sends back a `<Reject reason="rejected">`, Twilio returns a `404 Not Found` response code and the call setup is denied.

* * *

## SIP Refer From Twilio

sip-refer-from-twilio page anchor

Positive FeedbackNegative Feedback

If your TwiML instructions use `<Refer>`, Twilio will generate a SIP REFER toward the customer's PBX and handle any NOTIFY messages. The transfer is entirely handled by the customer's PBX.

Note: If `<Refer>` is the last verb and has no action URL the call leg will be ended, otherwise, TwiML execution continues as normal.

Interested in learning more about SIP REFER see [here](/docs/voice/twiml/refer "here").

* * *

## Passing SIP Headers to your TwiML application

passing-sip-headers-to-your-twiml-application page anchor

Positive FeedbackNegative Feedback

In order to better integrate with remote SIP applications, Twilio's SIP connections can read headers in the initial INVITE and pass them to your application. Twilio will read any headers beginning with the X- prefix and pass them in the TwiML HTTP callback in the format **SipHeader_X-headername=headervalue**. This allows your application to make programmatic decisions about what to do with a call.