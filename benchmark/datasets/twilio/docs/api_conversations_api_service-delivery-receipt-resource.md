# Service-Scoped Delivery Receipt Resource

*Source: https://www.twilio.com/docs/conversations/api/service-delivery-receipt-resource*

---

# Service-Scoped Delivery Receipt Resource

Positive FeedbackNegative Feedback

* * *

**Service-Scoped Delivery Receipts** in Conversations provide visibility into the status of Service-Scoped [Conversation Messages](/docs/conversations/api/service-conversation-message-resource "Conversation Messages") sent across different Conversations within a **non-default** Conversation Service.

Using Service-Scoped Delivery Receipts, you can verify that Messages have been sent, delivered, or even read (for OTT) by Conversations Participants within a **non-default, service-scoped** Conversation Service.

* * *

## API Base URL

api-base-url page anchor

Positive FeedbackNegative Feedback

All URLs in the reference documentation use the following base URL:

Copy code block


    1

    https://conversations.twilio.com/v1


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    1

    GET /v1/Services/ISxx/Conversations/CHxx/Messages


    2

* * *

## Receipt Properties

receipt-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this participant.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Message resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidSID<CH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messageSidSID<IM>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the message within a [Conversation](/docs/conversations/api/conversation-resource "Conversation") the delivery receipt belongs to

Pattern: `^IM[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<DY>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^DY[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

channelMessageSidSID

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A messaging channel-specific identifier for the message delivered to participant e.g. `SMxx` for SMS, `WAxx` for Whatsapp etc.

Pattern: `^[a-zA-Z]{2}[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

participantSidSID<MB>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the participant the delivery receipt belongs to.

Pattern: `^MB[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The message delivery status, can be `read`, `failed`, `delivered`, `undelivered`, `sent` or null.

Possible values:

`read``failed``delivered``undelivered``sent`

* * *

errorCodeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The message [delivery error code](/docs/sms/api/message-resource#delivery-related-errors "delivery error code") for a `failed` status,

Default: `0`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was last updated. `null` if the delivery receipt has not been updated.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this delivery receipt.