# Messages resource

*Source: https://www.twilio.com/docs/messaging/api/message-resource*

---

# Messages resource

Positive FeedbackNegative Feedback

* * *

A Message resource represents an inbound or outbound message. Twilio creates a Message when any of the following occur:

  * You create a Message resource (i.e., send an outbound message) via the [REST API](/docs/messaging/api "REST API")
  * Twilio executes a [<Message>](/docs/messaging/twiml/message "<Message>") TwiML instruction
  * Someone sends a message to one of your Twilio numbers or messaging channel addresses


With the Messages resource, you can:

  * [Create new messages](/docs/messaging/api/message-resource#create-a-message-resource "Create new messages") (i.e., send outbound messages)
  * [Fetch a specific message](/docs/messaging/api/message-resource#fetch-a-message-resource "Fetch a specific message")
  * [Read a list of messages](/docs/messaging/api/message-resource#read-multiple-message-resources "Read a list of messages")
  * [Update or redact the content of an existing message](/docs/messaging/api/message-resource#update-a-message-resource "Update or redact the content of an existing message")
  * [Delete messages from your account](/docs/messaging/api/message-resource#delete-a-message-resource "Delete messages from your account")


If you're using [Messaging Services](/docs/messaging/services "Messaging Services"), you can also use the Messages resource to:

  * [Schedule a message](/docs/messaging/features/message-scheduling "Schedule a message")
  * [Create a message with a shortened link](/docs/messaging/features/link-shortening "Create a message with a shortened link")


A Message resource can also have a [Media sub-resource](/docs/messaging/api/media-resource "Media sub-resource") and/or a [MessageFeedback](/docs/messaging/api/message-feedback-resource "MessageFeedback") sub-resource.

(information)

## Info

For step-by-step instructions for sending your first SMS with Twilio, check out one of the [SMS quickstarts](/docs/messaging/quickstart "SMS quickstarts").

Looking to [send WhatsApp messages with Twilio](/docs/whatsapp "send WhatsApp messages with Twilio")? Try one of the [WhatsApp quickstarts](/docs/whatsapp/quickstart "WhatsApp quickstarts").

If you're looking for how to **respond to incoming messages** , check out the [How to Receive and Reply to SMS Messages tutorial](/docs/messaging/tutorials/how-to-receive-and-reply "How to Receive and Reply to SMS Messages tutorial").

* * *

## Message Properties

message-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

bodystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The text content of the message

* * *

numSegmentsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of segments that make up the complete message. SMS message bodies that exceed the [character limit](/docs/glossary/what-sms-character-limit "character limit") are segmented and charged as multiple messages. Note: For messages sent via a Messaging Service, `num_segments` is initially `0`, since a sender hasn't yet been assigned.

* * *

directionenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The direction of the message. Can be: `inbound` for incoming messages, `outbound-api` for messages created by the REST API, `outbound-call` for messages created during a call, or `outbound-reply` for messages created in response to an incoming message.

Possible values:

`inbound``outbound-api``outbound-call``outbound-reply`

* * *

fromstring<phone-number>

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The sender's phone number (in [E.164(link takes you to an external page)](https://en.wikipedia.org/wiki/E.164 "E.164") format), [alphanumeric sender ID](/docs/sms/quickstart "alphanumeric sender ID"), [Wireless SIM](/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands "Wireless SIM"), [short code(link takes you to an external page)](https://www.twilio.com/en-us/messaging/channels/sms/short-codes "short code"), or [channel address](/docs/messaging/channels "channel address") (e.g., `whatsapp:+15554449999`). For incoming messages, this is the number or channel address of the sender. For outgoing messages, this value is a Twilio phone number, alphanumeric sender ID, short code, or channel address from which the message is sent.

* * *

tostring

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The recipient's phone number (in [E.164(link takes you to an external page)](https://en.wikipedia.org/wiki/E.164 "E.164") format) or [channel address](/docs/messaging/channels "channel address") (e.g. `whatsapp:+15552229999`)

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [RFC 2822(link takes you to an external page)](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3 "RFC 2822") timestamp (in GMT) of when the Message resource was last updated

* * *

pricestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The amount billed for the message in the currency specified by `price_unit`. The `price` is populated after the message has been sent/received, and may not be immediately availalble. View the [Pricing page(link takes you to an external page)](https://www.twilio.com/en-us/pricing "Pricing page") for more details.

* * *

errorMessagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The description of the `error_code` if the Message `status` is `failed` or `undelivered`. If no error was encountered, the value is `null`. The value returned in this field for a specific error cause is subject to change as Twilio improves errors. Users should not use the `error_code` and `error_message` fields programmatically.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the Message resource, relative to `https://api.twilio.com`.

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") associated with the Message resource

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

numMediastring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of media files associated with the Message resource.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the Message. Possible values: `accepted`, `scheduled`, `canceled`, `queued`, `sending`, `sent`, `failed`, `delivered`, `undelivered`, `receiving`, `received`, or `read` (WhatsApp only). For more information, See [detailed descriptions](/docs/sms/api/message-resource#message-status-values "detailed descriptions").

Possible values:

`queued``sending``sent``failed``delivered``undelivered``receiving``received``accepted``scheduled`Show 3 more

* * *

messagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") associated with the Message resource. A unique default value is assigned if a Messaging Service is not used.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<SM|MM>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique, Twilio-provided string that identifies the Message resource.

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateSentstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [RFC 2822(link takes you to an external page)](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3 "RFC 2822") timestamp (in GMT) of when the Message was sent. For an outgoing message, this is when Twilio sent the message. For an incoming message, this is when Twilio sent the HTTP request to your incoming message webhook URL.

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [RFC 2822(link takes you to an external page)](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3 "RFC 2822") timestamp (in GMT) of when the Message resource was created

* * *

errorCodeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [error code](/docs/api/errors "error code") returned if the Message `status` is `failed` or `undelivered`. If no error was encountered, the value is `null`. The value returned in this field for a specific error cause is subject to change as Twilio improves errors. Users should not use the `error_code` and `error_message` fields programmatically.

* * *

priceUnitstring<currency>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The currency in which `price` is measured, in [ISO 4127(link takes you to an external page)](https://www.iso.org/iso/home/standards/currency_codes.htm "ISO 4127") format (e.g. `usd`, `eur`, `jpy`).

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to process the Message

* * *

subresourceUrisobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of related resources identified by their URIs relative to `https://api.twilio.com`

* * *

## Message Status values

message-status-values page anchor

Positive FeedbackNegative Feedback

The table below lists possible values of a Message resource's `Status`. As messages can be either outbound or inbound, each status description explicitly indicates to which message direction the status applies.

| ENUM:STATUS possible values in REST API format
---|---
`'queued'`| The API request to send an outbound message was successful and the message is queued to be sent out by a specific `From` sender. For messages sent without a [Messaging Service](/docs/messaging/services "Messaging Service") this is the initial `Status` value of the Message resource.
`'sending'`| Twilio is in the process of dispatching the outbound message to the nearest upstream carrier in the network.
`'sent'`| The nearest upstream carrier accepted the outbound message.
`'failed'`| The outbound message failed to send. This can happen for [various reasons](/docs/messaging/guides/debugging-tools#error-codes "various reasons") including queue overflows, Account suspensions and media errors.
`'delivered'`| Twilio has received confirmation of outbound message delivery from the upstream carrier, and, where available, the destination handset.
`'undelivered'`| Twilio received a delivery receipt indicating that the outbound message was _not_ delivered. This can happen for [many reasons](/docs/messaging/guides/debugging-tools#error-codes "many reasons") including carrier content filtering and the availability of the destination handset.
`'receiving'`| The inbound message was received by Twilio and is currently being processed.
`'received'`| The inbound message was received and processing is complete.
`'accepted'`| _[Messaging Service only]_ Twilio has received your API request to immediately send an outbound message with a [Messaging Service](/docs/messaging/services "Messaging Service"). If you did not provide a specific `From` sender in the service's Sender Pool to use, the service is dynamically selecting a `From` sender. For unscheduled messages to be sent with a Messaging Service, this is the initial `Status` value of the Message resource.
`'scheduled'`| _[Messaging Service only]_ The Message resource is scheduled to be sent with a [Messaging Service](/docs/messaging/services "Messaging Service"). If you [schedule a message](/docs/messaging/features/message-scheduling "schedule a message") with a Messaging Service, this is the initial `Status` value of the Message resource.
`'read'`| Channels supported: RCS and WhatsApp. The recipient opened the outbound message. Recipient must have read receipts enabled.
`'partially_delivered'`| _[Deprecated]_
`'canceled'`| _[Messaging Service only]_ The message scheduled with a [Messaging Service](/docs/messaging/services "Messaging Service") has been canceled.

* * *

## NumSegments property

numsegments-property page anchor

Positive FeedbackNegative Feedback

The `NumSegments` property is relevant for SMS messages only.

For **outbound SMS messages** , this property indicates the number of SMS messages it took to deliver the body of the message.

If the body of a message is more than 160 [GSM-7](/docs/glossary/what-is-gsm-7-character-encoding "GSM-7") characters (or 70 [UCS-2](/docs/glossary/what-is-ucs-2-character-encoding "UCS-2") characters), Twilio segments and annotates your messages to attempt proper reassembly on the recipient's handset (not supported by all carriers and handsets). This ensures your body text transmits with the highest fidelity.

On **inbound SMS messages** , this property indicates the number of SMS messages that make up the message received.

If the body of a message is more than 160 [GSM-7](/docs/glossary/what-is-gsm-7-character-encoding "GSM-7") characters (or 70 [UCS-2](/docs/glossary/what-is-ucs-2-character-encoding "UCS-2") characters), Twilio attempts to reassemble the message received by your Twilio phone number. All carriers and handsets do not necessarily support this.

Your account is charged for each segment sent or received.

Learn more on the [SMS Character Limit Glossary page](/docs/glossary/what-sms-character-limit "SMS Character Limit Glossary page").

* * *

## Create a Message resource

create-a-message-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages.json`

To send a new outgoing message, send an HTTP `POST` request to your Account's Messages list resource URI.

(warning)

## Warning

If you want to send messages while in trial mode, you must first [verify your 'To' phone number with Twilio(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/223135427-What-s-the-difference-between-a-verified-phone-number-and-a-Twilio-phone-number- "verify your 'To' phone number with Twilio"). You can verify your phone number by adding it to your [Verified Caller IDs(link takes you to an external page)](https://www.twilio.com/console/phone-numbers/verified "Verified Caller IDs") in the Console.

(warning)

## Warning

Twilio queues messages for delivery at your [prescribed rate limit(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/223183648-Sending-and-Receiving-Limitations-on-Calls-and-SMS-Messages "prescribed rate limit"). API requests for messages that exceed the [specified rates(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/223183648-Sending-and-Receiving-Limitations-on-Calls-and-SMS-Messages "specified rates") will be queued and executed as capacity is available.

If you need to enqueue a large number of messages, you may want to use [Messaging Services](/docs/messaging/services "Messaging Services").

Every request to create a new Message resource requires a **recipient** , a **sender** , and **content**.

A **recipient** is specified via the `To` parameter.

The **sender** is specified via one of the following parameters:

  * `From`
  * `MessagingServiceSid`


The message **content** is specified via one of the following parameters:

  * `MediaUrl`
  * `Body`
  * `ContentSid`


The table below describes these parameters in more detail.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") creating the Message resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

tostring<phone-number>

required

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The recipient's phone number in [E.164](/docs/glossary/what-e164 "E.164") format (for SMS/MMS) or [channel address](/docs/messaging/channels "channel address"), e.g. `whatsapp:+15552229999`.

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of the endpoint to which Twilio sends [Message status callback requests](/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url "Message status callback requests"). URL must contain a valid hostname and underscores are not allowed. If you include this parameter with the `messaging_service_sid`, Twilio uses this URL instead of the Status Callback URL of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service").

* * *

applicationSidSID<AP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the associated [TwiML Application](/docs/usage/api/applications "TwiML Application"). [Message status callback requests](/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url "Message status callback requests") are sent to the TwiML App's `message_status_callback` URL. Note that the `status_callback` parameter of a request takes priority over the `application_sid` parameter; if both are included `application_sid` is ignored.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

maxPricenumber

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[OBSOLETE] This parameter will no longer have any effect as of 2024-06-03.

* * *

provideFeedbackboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Boolean indicating whether or not you intend to provide delivery confirmation feedback to Twilio (used in conjunction with the [Message Feedback subresource](/docs/sms/api/message-feedback-resource "Message Feedback subresource")). Default value is `false`.

* * *

attemptinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Total number of attempts made (including this request) to send the message regardless of the provider used

* * *

validityPeriodinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The maximum length in seconds that the Message can remain in Twilio's outgoing message queue. If a queued Message exceeds the `validity_period`, the Message is not sent. Accepted values are integers from `1` to `36000`. Default value is `36000`. A `validity_period` greater than `5` is recommended. [Learn more about the validity period(link takes you to an external page)](https://www.twilio.com/blog/take-more-control-of-outbound-messages-using-validity-period-html "Learn more about the validity period")

* * *

forceDeliveryboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reserved

* * *

contentRetentionenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Determines if the message content can be stored or redacted based on privacy settings

Possible values:

`retain``discard`

* * *

addressRetentionenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Determines if the address can be stored or obfuscated based on privacy settings

Possible values:

`retain``obfuscate`

* * *

smartEncodedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to detect Unicode characters that have a similar GSM-7 character and replace them. Can be: `true` or `false`.

* * *

persistentActionarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Rich actions for non-SMS/MMS channels. Used for [sending location in WhatsApp messages](/docs/whatsapp/message-features#location-messages-with-whatsapp "sending location in WhatsApp messages").

* * *

trafficTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`free`

* * *

shortenUrlsboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For Messaging Services with [Link Shortening configured](/docs/messaging/features/link-shortening "Link Shortening configured") only: A Boolean indicating whether or not Twilio should shorten links in the `body` of the Message. Default value is `false`. If `true`, the `messaging_service_sid` parameter must also be provided.

* * *

scheduleTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For Messaging Services only: Include this parameter with a value of `fixed` in conjuction with the `send_time` parameter in order to [schedule a Message](/docs/messaging/features/message-scheduling "schedule a Message").

Possible values:

`fixed`

* * *

sendAtstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The time that Twilio will send the message. Must be in ISO 8601 format.

* * *

sendAsMmsboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

If set to `true`, Twilio delivers the message as a single MMS message, regardless of the presence of media.

* * *

contentVariablesstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For [Content Editor/API](/docs/content "Content Editor/API") only: Key-value pairs of [Template variables](/docs/content/using-variables-with-content-api "Template variables") and their substitution values. `content_sid` parameter must also be provided. If values are not defined in the `content_variables` parameter, the [Template's default placeholder values](/docs/content/content-api-resources#create-templates "Template's default placeholder values") are used.

* * *

riskCheckenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Include this parameter with a value of `disable` to skip any kind of risk check on the respective message request.

Possible values:

`enable``disable`

* * *

fromstring<phone-number>

required if MessagingServiceSid is not passed

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The sender's Twilio phone number (in [E.164(link takes you to an external page)](https://en.wikipedia.org/wiki/E.164 "E.164") format), [alphanumeric sender ID](/docs/sms/quickstart "alphanumeric sender ID"), [Wireless SIM](/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands "Wireless SIM"), [short code(link takes you to an external page)](https://www.twilio.com/en-us/messaging/channels/sms/short-codes "short code"), or [channel address](/docs/messaging/channels "channel address") (e.g., `whatsapp:+15554449999`). The value of the `from` parameter must be a sender that is hosted within Twilio and belongs to the Account creating the Message. If you are using `messaging_service_sid`, this parameter can be empty (Twilio assigns a `from` value from the Messaging Service's Sender Pool) or you can provide a specific sender from your Sender Pool.

* * *

messagingServiceSidSID<MG>

required if From is not passed

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/services "Messaging Service") you want to associate with the Message. When this parameter is provided and the `from` parameter is omitted, Twilio selects the optimal sender from the Messaging Service's Sender Pool. You may also provide a `from` parameter if you want to use a specific Sender from the Sender Pool.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

bodystring

required if MediaUrl or ContentSid is not passed

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the `body` contains more than 160 [GSM-7](/docs/glossary/what-is-gsm-7-character-encoding "GSM-7") characters (or 70 [UCS-2](/docs/glossary/what-is-ucs-2-character-encoding "UCS-2") characters), the message is segmented and charged accordingly. For long `body` text, consider using the [send_as_mms parameter(link takes you to an external page)](https://www.twilio.com/blog/mms-for-long-text-messages "send_as_mms parameter").

* * *

mediaUrlarray[string<uri>]

required if Body or ContentSid is not passed

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of media to include in the Message content. `jpeg`, `jpg`, `gif`, and `png` file types are fully supported by Twilio and content is formatted for delivery on destination devices. The media size limit is 5 MB for supported file types (`jpeg`, `jpg`, `png`, `gif`) and 500 KB for [other types](/docs/messaging/guides/accepted-mime-types "other types") of accepted media. To send more than one image in the message, provide multiple `media_url` parameters in the POST request. You can include up to ten `media_url` parameters per message. [International(link takes you to an external page)](https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages "International") and [carrier(link takes you to an external page)](https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada- "carrier") limits apply.

* * *

contentSidSID<HX>

required if Body or MediaUrl is not passed

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For [Content Editor/API](/docs/content "Content Editor/API") only: The SID of the Content Template to be used with the Message, e.g., `HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`. If this parameter is not provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For Content API users, the SID is found in Twilio's response when [creating the Template](/docs/content/content-api-resources#create-templates "creating the Template") or by [fetching your Templates](/docs/content/content-api-resources#fetch-all-content-resources "fetching your Templates").

Pattern: `^HX[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Select from available examples

Copy code block


    {


      "ApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "Body": "Hello! 👍",


      "From": "+14155552345",


      "MediaUrl": [


        "https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg"


      ],


      "PersistentAction": [


        "mailto:test@example.com"


      ],


      "StatusCallback": "https://example.com",


      "To": "+14155552345",


      "Tags": "{\"campaign_name\": \"Spring Sale 2022\",\"message_type\": \"cart_abandoned\"}"


    }

* * *

## Twilio's request to the StatusCallback URL

twilios-request-to-the-statuscallback-url page anchor

Positive FeedbackNegative Feedback

Whenever a Message resource's `Status` changes, Twilio sends a `POST` request to the Message resource's `StatusCallback` URL.

In a status callback request, Twilio provides a subset of the [standard request properties](/docs/messaging/twiml#twilios-request-to-your-application "standard request properties"), and additionally `MessageStatus` and `ErrorCode`. These properties are described in the table below.

Property| Description
---|---
`MessageStatus`| The [status](/docs/messaging/api/message-resource#message-status-values "status") of the Message resource at the time the status callback request was sent.
`ErrorCode`| If an error occurred (i.e. the `MessageStatus` is `failed` or `undelivered`), this property provides additional information about the failure.

(warning)

## Warning

The properties included in Twilio's request to the StatusCallback URL vary by messaging channel and event type and are subject to change.

Twilio occasionally adds new properties without advance notice.

When integrating with status callback requests, it is important that your implementation is able to accept and correctly run [signature validation](/docs/usage/webhooks/webhooks-security "signature validation") on an evolving set of parameters.

Twilio strongly recommends using the signature validation methods provided in the SDKs and not implementing your own signature validation.

Learn more about status callbacks:

  * [Outbound Message Status in Status Callbacks](/docs/messaging/guides/outbound-message-status-in-status-callbacks "Outbound Message Status in Status Callbacks")
  * [Track the Message Status of Outbound Messages](/docs/messaging/guides/track-outbound-message-status "Track the Message Status of Outbound Messages")


### SMS/MMS

smsmms page anchor

Positive FeedbackNegative Feedback

For most SMS/MMS Messages that have a `Status` of `delivered` or `undelivered`, Twilio's request to the `StatusCallback` URL contains an additional property:

Property| Description
---|---
`RawDlrDoneDate`| This property is a passthrough of the Done Date included in the DLR (Delivery Receipt) that Twilio received from the carrier.

The value is in `YYMMDDhhmm` format.

  * `YY` is last two digits of the year (00-99)
  * `MM` is the two-digit month (01-12)
  * `DD` is the two-digit day (01-31)
  * `hh` is the two-digit hour (00-23)
  * `mm` is the two-digit minute (00-59).

Learn more on the ["Addition of RawDlrDoneDate to Delivered and Undelivered Status Webhooks" Changelog page(link takes you to an external page)](https://www.twilio.com/en-us/changelog/addition-of-rawdlrdonedate-to-delivered-and-undelivered-status-webhooks ""Addition of RawDlrDoneDate to Delivered and Undelivered Status Webhooks" Changelog page").

### WhatsApp and other messaging channels

whatsapp-and-other-messaging-channels page anchor

Positive FeedbackNegative Feedback

If the Message resource uses RCS, WhatsApp, or another messaging channel, Twilio's request to the `StatusCallback` URL contains additional properties. These properties are listed in the table below.

Property| Description
---|---
`ChannelInstallSid`| The [Installed Channel](/docs/messaging/channels "Installed Channel") SID that was used to send this message
`ChannelStatusMessage`| The error message returned by the underlying messaging channel if Message delivery failed. This property is present only if the Message delivery failed.
`ChannelPrefix`| The channel-specific prefix identifying the messaging channel associated with this Message
`EventType`| This property contains information about post-delivery events. If the channel supports read receipts (currently RCS and WhatsApp), this property's value is `READ` after the recipient has read the message.

* * *

## Send an SMS message

send-an-sms-message page anchor

Positive FeedbackNegative Feedback

The example below shows how to create a Message resource with an SMS **recipient**.

Sending this `POST` request causes Twilio to send a text message from `+15557122661` (a Twilio phone number belonging to the Account sending the request) to `+15558675310`. The **content** of the text message is `Hi there`.

Send an SMS messageLink to code sample: Send an SMS message

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

    async function createMessage() {


    11

      const message = await client.messages.create({


    12

        body: "Hi there",


    13

        from: "+15557122661",


    14

        to: "+15558675310",


    15

      });


    16




    17

      console.log(message.body);


    18

    }


    19




    20

    createMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "api_version": "2010-04-01",


    4

      "body": "Hi there",


    5

      "date_created": "Thu, 24 Aug 2023 05:01:45 +0000",


    6

      "date_sent": "Thu, 24 Aug 2023 05:01:45 +0000",


    7

      "date_updated": "Thu, 24 Aug 2023 05:01:45 +0000",


    8

      "direction": "outbound-api",


    9

      "error_code": null,


    10

      "error_message": null,


    11

      "from": "+15557122661",


    12

      "num_media": "0",


    13

      "num_segments": "1",


    14

      "price": null,


    15

      "price_unit": null,


    16

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "status": "queued",


    19

      "subresource_uris": {


    20

        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json"


    21

      },


    22

      "to": "+15558675310",


    23

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    24

    }

* * *

## Send an RCS message

send-an-rcs-message page anchor

Positive FeedbackNegative Feedback

After completing the setup and configuration steps in the [Programmable Messaging RCS Onboarding Guide ](/docs/rcs/onboarding "Programmable Messaging RCS Onboarding Guide
"), you can send a [Rich Communication Services (RCS)](/docs/rcs "Rich Communication Services \(RCS\)") message by creating a new Message resource. Set the `MessageServiceSid` or `From` parameter to the SID of the Messaging Service associated with your RCS Sender. To find your Messaging Service's SID, check the **Sid** column on the [Messaging Services page(link takes you to an external page)](https://www.twilio.com/console/sms/services "Messaging Services page") in the Console.

Programmable Messaging proactively checks if the recipient's device can support RCS, and will send the message using SMS as a fallback if needed.

Send an RCS message using the MessageServiceSid parameterLink to code sample: Send an RCS message using the MessageServiceSid parameter

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

    async function createMessage() {


    11

      const message = await client.messages.create({


    12

        body: "My first RCS message. Hello, world!",


    13

        messagingServiceSid: "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

        to: "+155XXXXXXXX",


    15

      });


    16




    17

      console.log(message.body);


    18

    }


    19




    20

    createMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "api_version": "2010-04-01",


    4

      "body": "My first RCS message. Hello, world!",


    5

      "date_created": "Thu, 24 Aug 2023 05:01:45 +0000",


    6

      "date_sent": "Thu, 24 Aug 2023 05:01:45 +0000",


    7

      "date_updated": "Thu, 24 Aug 2023 05:01:45 +0000",


    8

      "direction": "outbound-api",


    9

      "error_code": null,


    10

      "error_message": null,


    11

      "from": "+14155552345",


    12

      "num_media": "0",


    13

      "num_segments": "1",


    14

      "price": null,


    15

      "price_unit": null,


    16

      "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    17

      "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "status": "queued",


    19

      "subresource_uris": {


    20

        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json"


    21

      },


    22

      "to": "+155XXXXXXXX",


    23

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    24

    }

Send an RCS message using the From parameterLink to code sample: Send an RCS message using the From parameter

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

    async function createMessage() {


    11

      const message = await client.messages.create({


    12

        body: "My first RCS message. Hello, world!",


    13

        from: "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

        to: "+155XXXXXXXX",


    15

      });


    16




    17

      console.log(message.body);


    18

    }


    19




    20

    createMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "api_version": "2010-04-01",


    4

      "body": "My first RCS message. Hello, world!",


    5

      "date_created": "Thu, 24 Aug 2023 05:01:45 +0000",


    6

      "date_sent": "Thu, 24 Aug 2023 05:01:45 +0000",


    7

      "date_updated": "Thu, 24 Aug 2023 05:01:45 +0000",


    8

      "direction": "outbound-api",


    9

      "error_code": null,


    10

      "error_message": null,


    11

      "from": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    12

      "num_media": "0",


    13

      "num_segments": "1",


    14

      "price": null,


    15

      "price_unit": null,


    16

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "status": "queued",


    19

      "subresource_uris": {


    20

        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json"


    21

      },


    22

      "to": "+155XXXXXXXX",


    23

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    24

    }

* * *

## Send a WhatsApp message

send-a-whatsapp-message page anchor

Positive FeedbackNegative Feedback

If you have a [Twilio-approved WhatsApp sender](/docs/whatsapp#whatsapp-sender-registration "Twilio-approved WhatsApp sender"), you can send WhatsApp messages by creating a new Message resource. ([WhatsApp session limitations](/docs/whatsapp/key-concepts "WhatsApp session limitations") apply.)

The `From` parameter value must be your approved WhatsApp sender address (e.g., `whatsapp:+15552221111`).

The `To` parameter value must be a WhatsApp recipient address (e.g., `whatsapp:+15553334444`).

You must also provide message content via the `Body` and/or `MediaUrl` parameters.

If you're using [Messaging Services](/docs/messaging/services "Messaging Services") with [Content API/Content Editor](/docs/content "Content API/Content Editor"), you can provide message content via the `contentSid` and `contentVariables` parameters.

**Note:** WhatsApp does not support including a text body in the same message as a video, audio file, document, contact (vCard), or location. If you pass the `Body` parameter on a message with one of these media types, the body is ignored and not delivered to the recipient.

Send a WhatsApp MessageLink to code sample: Send a WhatsApp Message

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

    async function createMessage() {


    11

      const message = await client.messages.create({


    12

        body: "This is a WhatsApp message sent with Twilio!",


    13

        from: "whatsapp:+15555238886",


    14

        to: "whatsapp:+15557770006",


    15

      });


    16




    17

      console.log(message.body);


    18

    }


    19




    20

    createMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "api_version": "2010-04-01",


    4

      "body": "This is a WhatsApp message sent with Twilio!",


    5

      "date_created": "Thu, 24 Aug 2023 05:01:45 +0000",


    6

      "date_sent": "Thu, 24 Aug 2023 05:01:45 +0000",


    7

      "date_updated": "Thu, 24 Aug 2023 05:01:45 +0000",


    8

      "direction": "outbound-api",


    9

      "error_code": null,


    10

      "error_message": null,


    11

      "from": "whatsapp:+15555238886",


    12

      "num_media": "0",


    13

      "num_segments": "1",


    14

      "price": null,


    15

      "price_unit": null,


    16

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "status": "queued",


    19

      "subresource_uris": {


    20

        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json"


    21

      },


    22

      "to": "whatsapp:+15557770006",


    23

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    24

    }

* * *

## Send a message with a Messaging Service

send-a-message-with-a-messaging-service page anchor

Positive FeedbackNegative Feedback

When sending a message with a [Messaging Service](/docs/messaging/services "Messaging Service"), you must provide a **recipient** via the `To` parameter and **content** via the `Body`, `ContentSid`, or `MediaUrl` parameters. In addition, you must provide the `MessagingServiceSid`.

If you provide a `MessagingServiceSid` and no `From` parameter, Twilio determines the optimal `From` value from your Sender Pool. In this case, the Message resource's initial `Status` value is `accepted`.

Optionally, you can provide a `MessagingServiceSid` _and_ a `From` parameter. The `From` parameter must be a sender from your Messaging Service's Sender Pool. In this case, the Message resource's initial `Status` value is `queued`.

With Messaging Services, you can also [schedule messages to be sent in the future](/docs/messaging/features/message-scheduling "schedule messages to be sent in the future") and [send messages with shortened links](/docs/messaging/features/link-shortening "send messages with shortened links").

Send a message with a Messaging ServiceLink to code sample: Send a message with a Messaging Service

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

    async function createMessage() {


    11

      const message = await client.messages.create({


    12

        body: "Hello! This is a message sent from a Messaging Service.",


    13

        messagingServiceSid: "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

        to: "+15551212121",


    15

      });


    16




    17

      console.log(message.body);


    18

    }


    19




    20

    createMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "api_version": "2010-04-01",


    4

      "body": "Hello! This is a message sent from a Messaging Service.",


    5

      "date_created": "Thu, 24 Aug 2023 05:01:45 +0000",


    6

      "date_sent": "Thu, 24 Aug 2023 05:01:45 +0000",


    7

      "date_updated": "Thu, 24 Aug 2023 05:01:45 +0000",


    8

      "direction": "outbound-api",


    9

      "error_code": null,


    10

      "error_message": null,


    11

      "from": "+14155552345",


    12

      "num_media": "0",


    13

      "num_segments": "1",


    14

      "price": null,


    15

      "price_unit": null,


    16

      "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    17

      "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "status": "queued",


    19

      "subresource_uris": {


    20

        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json"


    21

      },


    22

      "to": "+15551212121",


    23

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    24

    }

* * *

## Fetch a Message resource

fetch-a-message-resource page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json`

Returns a single Message resource specified by the provided Message `SID`.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") associated with the Message resource

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<SM|MM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource to be fetched

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a MessageLink to code sample: Fetch a Message

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

    async function fetchMessage() {


    11

      const message = await client


    12

        .messages("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(message.body);


    16

    }


    17




    18

    fetchMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "api_version": "2010-04-01",


    4

      "body": "testing",


    5

      "date_created": "Fri, 24 May 2019 17:18:27 +0000",


    6

      "date_sent": "Fri, 24 May 2019 17:18:28 +0000",


    7

      "date_updated": "Fri, 24 May 2019 17:18:28 +0000",


    8

      "direction": "outbound-api",


    9

      "error_code": 30007,


    10

      "error_message": "Carrier violation",


    11

      "from": "+12019235161",


    12

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "num_media": "0",


    14

      "num_segments": "1",


    15

      "price": "-0.00750",


    16

      "price_unit": "USD",


    17

      "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "status": "sent",


    19

      "subresource_uris": {


    20

        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5/Media.json",


    21

        "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5/Feedback.json"


    22

      },


    23

      "to": "+18182008801",


    24

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5.json"


    25

    }

* * *

## Read multiple Message resources

read-multiple-message-resources page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages.json`

Read multiple Message resources by sending a `GET` request to your Account's Messages list URI.

Results are sorted by the `DateSent` field, with the most recent messages appearing first.

(warning)

## Warning

If you are using the Twilio REST API and plan on requesting more records than will fit on a single page, you may want to use the response's [nextpageuri](/docs/usage/twilios-response#pagination "nextpageuri") property. Requesting this URI ensures that your next request picks up where it left off and can prevent you from retrieving duplicate data if you are actively sending or receiving messages.

This is not necessary if you are using one of the SDKs, which automatically handle pagination. Take a look at the [SDK documentation](/docs/libraries "SDK documentation") for more information.

You can also filter the Messages list by providing the following query string parameters to the listing resource:

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") associated with the Message resources.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

tostring<phone-number>

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Filter by recipient. For example: Set this parameter to `+15558881111` to retrieve a list of Message resources sent to `+15558881111`.

* * *

fromstring<phone-number>

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Filter by sender. For example: Set this parameter to `+15552229999` to retrieve a list of Message resources sent by `+15552229999`.

* * *

dateSentstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter by Message `sent_date`. Accepts GMT dates in the following formats: `YYYY-MM-DD` (to find Messages with a specific `sent_date`), `<=YYYY-MM-DD` (to find Messages with `sent_date`s on and before a specific date), and `>=YYYY-MM-DD` (to find Messages with `sent_dates` on and after a specific date).

* * *

dateSentBeforestring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter by Message `sent_date`. Accepts GMT dates in the following formats: `YYYY-MM-DD` (to find Messages with a specific `sent_date`), `<=YYYY-MM-DD` (to find Messages with `sent_date`s on and before a specific date), and `>=YYYY-MM-DD` (to find Messages with `sent_dates` on and after a specific date).

* * *

dateSentAfterstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter by Message `sent_date`. Accepts GMT dates in the following formats: `YYYY-MM-DD` (to find Messages with a specific `sent_date`), `<=YYYY-MM-DD` (to find Messages with `sent_date`s on and before a specific date), and `>=YYYY-MM-DD` (to find Messages with `sent_dates` on and after a specific date).

* * *

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

List all Message resourcesLink to code sample: List all Message resources

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

    async function listMessage() {


    11

      const messages = await client.messages.list({ limit: 20 });


    12




    13

      messages.forEach((m) => console.log(m.body));


    14

    }


    15




    16

    listMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 1,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0",


    4

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=1&PageToken=PAMMc26223853f8c46b4ab7dfaa6abba0a26",


    5

      "page": 0,


    6

      "page_size": 2,


    7

      "previous_page_uri": null,


    8

      "messages": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "body": "testing",


    13

          "date_created": "Fri, 24 May 2019 17:44:46 +0000",


    14

          "date_sent": "Fri, 24 May 2019 17:44:50 +0000",


    15

          "date_updated": "Fri, 24 May 2019 17:44:50 +0000",


    16

          "direction": "outbound-api",


    17

          "error_code": null,


    18

          "error_message": null,


    19

          "from": "+12019235161",


    20

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "num_media": "0",


    22

          "num_segments": "1",


    23

          "price": "-0.00750",


    24

          "price_unit": "USD",


    25

          "sid": "SMded05904ccb347238880ca9264e8fe1c",


    26

          "status": "sent",


    27

          "subresource_uris": {


    28

            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Media.json",


    29

            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Feedback.json"


    30

          },


    31

          "to": "+18182008801",


    32

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c.json"


    33

        },


    34

        {


    35

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

          "api_version": "2010-04-01",


    37

          "body": "look mom I have media!",


    38

          "date_created": "Fri, 24 May 2019 17:44:46 +0000",


    39

          "date_sent": "Fri, 24 May 2019 17:44:49 +0000",


    40

          "date_updated": "Fri, 24 May 2019 17:44:49 +0000",


    41

          "direction": "inbound",


    42

          "error_code": 30004,


    43

          "error_message": "Message blocked",


    44

          "from": "+12019235161",


    45

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    46

          "num_media": "3",


    47

          "num_segments": "1",


    48

          "price": "-0.00750",


    49

          "price_unit": "USD",


    50

          "sid": "MMc26223853f8c46b4ab7dfaa6abba0a26",


    51

          "status": "received",


    52

          "subresource_uris": {


    53

            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Media.json",


    54

            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Feedback.json"


    55

          },


    56

          "to": "+18182008801",


    57

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26.json"


    58

        }


    59

      ],


    60

      "start": 0,


    61

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0"


    62

    }

List Message resources matching filter criteriaLink to code sample: List Message resources matching filter criteria

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

    async function listMessage() {


    11

      const messages = await client.messages.list({


    12

        dateSent: new Date("2016-08-31 00:00:00"),


    13

        from: "+15017122661",


    14

        to: "+15558675310",


    15

        limit: 20,


    16

      });


    17




    18

      messages.forEach((m) => console.log(m.body));


    19

    }


    20




    21

    listMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 1,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0",


    4

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=1&PageToken=PAMMc26223853f8c46b4ab7dfaa6abba0a26",


    5

      "page": 0,


    6

      "page_size": 2,


    7

      "previous_page_uri": null,


    8

      "messages": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "body": "testing",


    13

          "date_created": "Fri, 24 May 2019 17:44:46 +0000",


    14

          "date_sent": "Fri, 24 May 2019 17:44:50 +0000",


    15

          "date_updated": "Fri, 24 May 2019 17:44:50 +0000",


    16

          "direction": "outbound-api",


    17

          "error_code": null,


    18

          "error_message": null,


    19

          "from": "+12019235161",


    20

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "num_media": "0",


    22

          "num_segments": "1",


    23

          "price": "-0.00750",


    24

          "price_unit": "USD",


    25

          "sid": "SMded05904ccb347238880ca9264e8fe1c",


    26

          "status": "sent",


    27

          "subresource_uris": {


    28

            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Media.json",


    29

            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Feedback.json"


    30

          },


    31

          "to": "+18182008801",


    32

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c.json"


    33

        },


    34

        {


    35

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

          "api_version": "2010-04-01",


    37

          "body": "look mom I have media!",


    38

          "date_created": "Fri, 24 May 2019 17:44:46 +0000",


    39

          "date_sent": "Fri, 24 May 2019 17:44:49 +0000",


    40

          "date_updated": "Fri, 24 May 2019 17:44:49 +0000",


    41

          "direction": "inbound",


    42

          "error_code": 30004,


    43

          "error_message": "Message blocked",


    44

          "from": "+12019235161",


    45

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    46

          "num_media": "3",


    47

          "num_segments": "1",


    48

          "price": "-0.00750",


    49

          "price_unit": "USD",


    50

          "sid": "MMc26223853f8c46b4ab7dfaa6abba0a26",


    51

          "status": "received",


    52

          "subresource_uris": {


    53

            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Media.json",


    54

            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Feedback.json"


    55

          },


    56

          "to": "+18182008801",


    57

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26.json"


    58

        }


    59

      ],


    60

      "start": 0,


    61

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0"


    62

    }

List Messages that were sent before a specific dateLink to code sample: List Messages that were sent before a specific date

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

    async function listMessage() {


    11

      const messages = await client.messages.list({


    12

        dateSentBefore: new Date("2009-07-06 20:30:00"),


    13

        limit: 20,


    14

      });


    15




    16

      messages.forEach((m) => console.log(m.body));


    17

    }


    18




    19

    listMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 1,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0",


    4

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=1&PageToken=PAMMc26223853f8c46b4ab7dfaa6abba0a26",


    5

      "page": 0,


    6

      "page_size": 2,


    7

      "previous_page_uri": null,


    8

      "messages": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "body": "testing",


    13

          "date_created": "Fri, 24 May 2019 17:44:46 +0000",


    14

          "date_sent": "Fri, 24 May 2019 17:44:50 +0000",


    15

          "date_updated": "Fri, 24 May 2019 17:44:50 +0000",


    16

          "direction": "outbound-api",


    17

          "error_code": null,


    18

          "error_message": null,


    19

          "from": "+12019235161",


    20

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "num_media": "0",


    22

          "num_segments": "1",


    23

          "price": "-0.00750",


    24

          "price_unit": "USD",


    25

          "sid": "SMded05904ccb347238880ca9264e8fe1c",


    26

          "status": "sent",


    27

          "subresource_uris": {


    28

            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Media.json",


    29

            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Feedback.json"


    30

          },


    31

          "to": "+18182008801",


    32

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c.json"


    33

        },


    34

        {


    35

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

          "api_version": "2010-04-01",


    37

          "body": "look mom I have media!",


    38

          "date_created": "Fri, 24 May 2019 17:44:46 +0000",


    39

          "date_sent": "Fri, 24 May 2019 17:44:49 +0000",


    40

          "date_updated": "Fri, 24 May 2019 17:44:49 +0000",


    41

          "direction": "inbound",


    42

          "error_code": 30004,


    43

          "error_message": "Message blocked",


    44

          "from": "+12019235161",


    45

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    46

          "num_media": "3",


    47

          "num_segments": "1",


    48

          "price": "-0.00750",


    49

          "price_unit": "USD",


    50

          "sid": "MMc26223853f8c46b4ab7dfaa6abba0a26",


    51

          "status": "received",


    52

          "subresource_uris": {


    53

            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Media.json",


    54

            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Feedback.json"


    55

          },


    56

          "to": "+18182008801",


    57

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26.json"


    58

        }


    59

      ],


    60

      "start": 0,


    61

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0"


    62

    }

List Messages within a specific time periodLink to code sample: List Messages within a specific time period

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

    async function listMessage() {


    11

      const messages = await client.messages.list({


    12

        dateSentBefore: new Date("2021-01-17 01:23:45"),


    13

        dateSentAfter: new Date("2021-01-15 01:23:45"),


    14

        limit: 20,


    15

      });


    16




    17

      messages.forEach((m) => console.log(m.body));


    18

    }


    19




    20

    listMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 1,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0",


    4

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=1&PageToken=PAMMc26223853f8c46b4ab7dfaa6abba0a26",


    5

      "page": 0,


    6

      "page_size": 2,


    7

      "previous_page_uri": null,


    8

      "messages": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "body": "testing",


    13

          "date_created": "Fri, 24 May 2019 17:44:46 +0000",


    14

          "date_sent": "Fri, 24 May 2019 17:44:50 +0000",


    15

          "date_updated": "Fri, 24 May 2019 17:44:50 +0000",


    16

          "direction": "outbound-api",


    17

          "error_code": null,


    18

          "error_message": null,


    19

          "from": "+12019235161",


    20

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "num_media": "0",


    22

          "num_segments": "1",


    23

          "price": "-0.00750",


    24

          "price_unit": "USD",


    25

          "sid": "SMded05904ccb347238880ca9264e8fe1c",


    26

          "status": "sent",


    27

          "subresource_uris": {


    28

            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Media.json",


    29

            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Feedback.json"


    30

          },


    31

          "to": "+18182008801",


    32

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c.json"


    33

        },


    34

        {


    35

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

          "api_version": "2010-04-01",


    37

          "body": "look mom I have media!",


    38

          "date_created": "Fri, 24 May 2019 17:44:46 +0000",


    39

          "date_sent": "Fri, 24 May 2019 17:44:49 +0000",


    40

          "date_updated": "Fri, 24 May 2019 17:44:49 +0000",


    41

          "direction": "inbound",


    42

          "error_code": 30004,


    43

          "error_message": "Message blocked",


    44

          "from": "+12019235161",


    45

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    46

          "num_media": "3",


    47

          "num_segments": "1",


    48

          "price": "-0.00750",


    49

          "price_unit": "USD",


    50

          "sid": "MMc26223853f8c46b4ab7dfaa6abba0a26",


    51

          "status": "received",


    52

          "subresource_uris": {


    53

            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Media.json",


    54

            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Feedback.json"


    55

          },


    56

          "to": "+18182008801",


    57

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26.json"


    58

        }


    59

      ],


    60

      "start": 0,


    61

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0"


    62

    }

* * *

## Update a Message resource

update-a-message-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json`

Updates the body of a Message resource. Send a `POST` request to a Message resource's URI containing the updated parameters.

This action is primarily used to redact Message content. To redact a Message resource's `Body`, send a `POST` request to the Message resource's URI and set the `Body` parameter as an empty string: `""`. This redacts the `Body` of a message while keeping the other [Message resource properties](/docs/messaging/api/message-resource#message-properties "Message resource properties") intact.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Message resources to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<SM|MM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource to be updated

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

bodystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The new `body` of the Message resource. To redact the text content of a Message, this parameter's value must be an empty string

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`canceled`

Select from available examples

Copy code block


    {


      "Body": ""


    }

Redact the body of a Message resourceLink to code sample: Redact the body of a Message resource

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

    async function updateMessage() {


    11

      const message = await client


    12

        .messages("SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .update({ body: "" });


    14




    15

      console.log(message.body);


    16

    }


    17




    18

    updateMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "api_version": "2010-04-01",


    4

      "body": "",


    5

      "date_created": "Fri, 24 May 2019 17:18:27 +0000",


    6

      "date_sent": "Fri, 24 May 2019 17:18:28 +0000",


    7

      "date_updated": "Fri, 24 May 2019 17:18:28 +0000",


    8

      "direction": "outbound-api",


    9

      "error_code": null,


    10

      "error_message": null,


    11

      "from": "+12019235161",


    12

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "num_media": "0",


    14

      "num_segments": "1",


    15

      "price": null,


    16

      "price_unit": "USD",


    17

      "sid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    18

      "status": "sent",


    19

      "subresource_uris": {


    20

        "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5/Media.json",


    21

        "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5/Feedback.json"


    22

      },


    23

      "to": "+18182008801",


    24

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5.json"


    25

    }

* * *

## Delete a Message resource

delete-a-message-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json`

To delete a Message resource, send a `DELETE` request to the Message resource's URI.

If the `DELETE` request is successful, Twilio's response status code is `HTTP 204 (No Content)`.

A deleted Message resource no longer appears in your Account's Messaging logs. Deleted messages cannot be recovered.

Deleting a Message resource also deletes any associated Media and/or MessageFeedback sub-resources. Any associated media file is also deleted unless the same media file is associated with another Message resource in your Account. For example, if you send 1,000 messages with the same media file (e.g., a `.jpeg` file), that media file remains accessible until all 1,000 associated Message resources (and/or the associated Media sub-resources) are deleted.

(warning)

## Warning

Message bodies may persist for up to 30 days after an HTTP `DELETE` request in our database backups.

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") associated with the Message resource

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<SM|MM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource you wish to delete

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a MessageLink to code sample: Delete a Message

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

    async function deleteMessage() {


    11

      await client.messages("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").remove();


    12

    }


    13




    14

    deleteMessage();