# Call resource

*Source: https://www.twilio.com/docs/voice/api/call-resource*

---

# Call resource

Positive FeedbackNegative Feedback

* * *

A Call resource represents a connection between a telephone and Twilio.

Using this resource, you can initiate a call, fetch information about a completed call, fetch a list of calls made to and from your account, redirect or end a call that is in progress, and delete records of past calls from your account.

An _inbound call_ occurs when a person calls one of your Twilio phone numbers, client connections, or SIP-enabled endpoints. An _outbound call_ happens when you initiate a call from a Twilio phone number to an outside phone number, client, or SIP domain.

You can initiate an outbound call by sending an HTTP `POST` request to the [Calls resource](/docs/voice/api/call-resource "Calls resource"). Calls are rate limited at the account level by Calls Per Second (CPS). Calls beyond your account's CPS limit will be queued and will execute at the CPS rate.

The `queue_time` parameter provides an estimate for how long before the call is executed. You can reduce `queue_time` by increasing the CPS value on your account.

(information)

## Calls Per Second (CPS)

By default, each account is granted one CPS for calls created via `POST` requests to the `/Calls` endpoint. Inbound calls and `<Dial>` calls are not limited by CPS.

Accounts with an approved [Business Profile(link takes you to an external page)](https://console.twilio.com/us1/account/trust-hub/customer-profiles "Business Profile") can update their CPS up to 5 in the Twilio Console.

In aggregate, calls are executed at the rate defined by the CPS. Individual calls may not execute at the anticipated rate — you may see individual seconds with more or fewer CPS, especially for inconsistent traffic — but over a month, the call execution rate will average the CPS rate set for that account or trunk.

You can also initiate a call from an active call (e.g., forwarding to another number or dialing into a conference) by including [TwiML's <Dial>](/docs/voice/twiml/dial "TwiML's <Dial>") verb in your [TwiML](/docs/voice/twiml "TwiML") application. However, the only way to initiate a call directly from Twilio is with an API request.

(information)

## Info

Are you looking for step-by-step instructions for making your first call with Twilio using the SDKs? Check out [our server-side quickstart for Programmable Voice](/docs/voice/quickstart/server "our server-side quickstart for Programmable Voice").

* * *

## Call Properties

call-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify this Call resource.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in UTC that this resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in UTC that this resource was last updated, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

parentCallSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID that identifies the call that created this leg.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this Call resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

tostring

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number, SIP address, Client identifier or SIM SID that received this call. Phone numbers are in [E.164](/docs/glossary/what-e164 "E.164") format (e.g., +16175551212). SIP addresses are formatted as `name@company.com`. Client identifiers are formatted `client:name`. SIM SIDs are formatted as `sim:sid`.

* * *

toFormattedstring

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number, SIP address or Client identifier that received this call. Formatted for display. Non-North American phone numbers are in [E.164](/docs/glossary/what-e164 "E.164") format (e.g., +442071838750).

* * *

fromstring

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number, SIP address, Client identifier or SIM SID that made this call. Phone numbers are in [E.164](/docs/glossary/what-e164 "E.164") format (e.g., +16175551212). SIP addresses are formatted as `name@company.com`. Client identifiers are formatted `client:name`. SIM SIDs are formatted as `sim:sid`.

* * *

fromFormattedstring

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The calling phone number, SIP address, or Client identifier formatted for display. Non-North American phone numbers are in [E.164](/docs/glossary/what-e164 "E.164") format (e.g., +442071838750).

* * *

phoneNumberSidSID<PN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

If the call was inbound, this is the SID of the IncomingPhoneNumber resource that received the call. If the call was outbound, it is the SID of the OutgoingCallerId resource from which the call was placed.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of this call. Can be: `queued`, `ringing`, `in-progress`, `canceled`, `completed`, `failed`, `busy` or `no-answer`. See [Call Status Values](/docs/voice/api/call-resource#call-status-values "Call Status Values") below for more information.

Possible values:

`queued``ringing``in-progress``completed``busy``failed``no-answer``canceled`

* * *

startTimestring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The start time of the call, given as UTC in [RFC 2822(link takes you to an external page)](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822 "RFC 2822") format. Empty if the call has not yet been dialed.

* * *

endTimestring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The time the call ended, given as UTC in [RFC 2822(link takes you to an external page)](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822 "RFC 2822") format. Empty if the call did not complete successfully.

* * *

durationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The length of the call in seconds. This value is empty for busy, failed, unanswered, or ongoing calls.

* * *

pricestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The charge for this call, in the currency associated with the account. Populated after the call is completed. May not be immediately available. The price associated with a call only reflects the charge for connectivity. Charges for other call-related features such as Answering Machine Detection, Text-To-Speech, and SIP REFER are not included in this value.

* * *

priceUnitstring<currency>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The currency in which `Price` is measured, in [ISO 4127(link takes you to an external page)](https://www.iso.org/iso/home/standards/currency_codes.htm "ISO 4127") format (e.g., `USD`, `EUR`, `JPY`). Always capitalized for calls.

* * *

directionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string describing the direction of the call. Can be: `inbound` for inbound calls, `outbound-api` for calls initiated via the REST API or `outbound-dial` for calls initiated by a `<Dial>` verb. Using [Elastic SIP Trunking](/docs/sip-trunking "Elastic SIP Trunking"), the values can be [`trunking-terminating`](/docs/sip-trunking#termination) for outgoing calls from your communications infrastructure to the PSTN or [`trunking-originating`](/docs/sip-trunking#origination) for incoming calls to your communications infrastructure from the PSTN.

* * *

answeredBystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Either `human` or `machine` if this call was initiated with answering machine detection. Empty otherwise.

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to create the call.

* * *

forwardedFromstring

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The forwarding phone number if this call was an incoming call forwarded from another number (depends on carrier supporting forwarding). Otherwise, empty.

* * *

groupSidSID<GP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Group SID associated with this call. If no Group is associated with the call, the field is empty.

Pattern: `^GP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callerNamestring

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The caller's name if this call was an incoming call to a phone number with caller ID Lookup enabled. Otherwise, empty.

* * *

queueTimestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The wait time in milliseconds before the call is placed.

* * *

trunkSidSID<TK>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique identifier of the trunk resource that was used for this call. The field is empty if the call was not made using a SIP trunk or if the call is not terminated.

Pattern: `^TK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of this resource, relative to `https://api.twilio.com`.

* * *

subresourceUrisobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of subresources available to this call, identified by their URIs relative to `https://api.twilio.com`.

* * *

## Call Status values

call-status-values page anchor

Positive FeedbackNegative Feedback

The following are the possible values for the `Status` parameter:

Status| Description
---|---
`queued`| The call is ready and waiting in line before dialing.
`ringing`| The call is currently ringing.
`in-progress`| The call was answered and is currently in progress.
`canceled`| The call was canceled via the REST API while it was ringing. If the call is canceled while still in `queued` status, no status callbacks are fired. See [StatusCallbackEvent](/docs/voice/api/call-resource#statuscallbackevent "StatusCallbackEvent") for details.
`completed`| The call was answered and has ended normally.
`busy`| The caller received a busy signal.
`no-answer`| There was no answer or the call was [rejected](/docs/voice/twiml/reject "rejected").
`failed`| The call could not be completed as dialed, most likely because the provided number was invalid.

(information)

## Notice about completed calls

A completed call indicates that a connection was established, and audio data was transferred. This can occur when a call is answered by a person, an IVR phone tree menu, or even a voicemail. Completed calls, regardless of the outcome, are charged against your project balance.

* * *

## Create a Call

create-a-call page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls.json`

You can make calls through the REST API to phone numbers, SIP addresses, or client identifiers. To place an outbound call, send a `POST` request to the Calls resource.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that will create the resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

tostring<endpoint>

required

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number, SIP address, or client identifier to call.

* * *

fromstring<endpoint>

required

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number or client identifier to use as the caller id. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](/docs/voice/api/outgoing-caller-ids "outgoing caller id") for your account. If the `to` parameter is a phone number, `From` must also be a phone number.

* * *

methodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when calling the `url` parameter's value. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored.

Possible values:

`GET``POST`

* * *

fallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call using the `fallback_method` if an error occurs when requesting or executing the TwiML at `url`. If an `application_sid` parameter is present, this parameter is ignored.

* * *

fallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to request the `fallback_url`. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored.

Possible values:

`GET``POST`

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `status_callback_method` to send status information to your application. If no `status_callback_event` is specified, we will send the `completed` status. If an `application_sid` parameter is present, this parameter is ignored. URLs must contain a valid hostname (underscores are not permitted).

* * *

statusCallbackEventarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The call progress events that we will send to the `status_callback` URL. Can be: `initiated`, `ringing`, `answered`, and `completed`. If no event is specified, we send the `completed` status. If you want to receive multiple events, specify each one in a separate `status_callback_event` parameter. See the code sample for [monitoring call progress](/docs/voice/api/call-resource?code-sample=code-create-a-call-resource-and-specify-a-statuscallbackevent&code-sdk-version=json "monitoring call progress"). If an `application_sid` is present, this parameter is ignored.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when calling the `status_callback` URL. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored.

Possible values:

`GET``POST`

* * *

sendDigitsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The string of keys to dial after connecting to the number, with a maximum length of 32 digits. Valid digits in the string include any digit (`0`-`9`), '`A`', '`B`', '`C`', '`D`', '`#`', and '`*`'. You can also use '`w`' to insert a half-second pause and '`W`' to insert a one-second pause. For example, to pause for one second after connecting and then dial extension 1234 followed by the # key, set this parameter to `W1234#`. Be sure to URL-encode this string because the '`#`' character has special meaning in a URL. If both `SendDigits` and `MachineDetection` parameters are provided, then `MachineDetection` will be ignored.

* * *

timeoutinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The integer number of seconds that we should allow the phone to ring before assuming there is no answer. The default is `60` seconds and the maximum is `600` seconds. For some call flows, we will add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as `15` seconds, to hang up before reaching an answering machine or voicemail.

* * *

recordboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to record the call. Can be `true` to record the phone call, or `false` to not. The default is `false`. The `recording_url` is sent to the `status_callback` URL.

* * *

recordingChannelsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of channels in the final recording. Can be: `mono` or `dual`. The default is `mono`. `mono` records both legs of the call in a single channel of the recording file. `dual` records each leg to a separate channel of the recording file. The first channel of a dual-channel recording contains the parent call and the second channel contains the child call.

* * *

recordingStatusCallbackstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call when the recording is available to be accessed.

* * *

recordingStatusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when calling the `recording_status_callback` URL. Can be: `GET` or `POST` and the default is `POST`.

Possible values:

`GET``POST`

* * *

sipAuthUsernamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The username used to authenticate the caller making a SIP call.

* * *

sipAuthPasswordstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The password required to authenticate the user account specified in `sip_auth_username`.

* * *

machineDetectionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to detect if a human, answering machine, or fax has picked up the call. Can be: `Enable` or `DetectMessageEnd`. Use `Enable` if you would like us to return `AnsweredBy` as soon as the called party is identified. Use `DetectMessageEnd`, if you would like to leave a message on an answering machine. If `send_digits` is provided, this parameter is ignored. For more information, see [Answering Machine Detection](/docs/voice/answering-machine-detection "Answering Machine Detection").

* * *

machineDetectionTimeoutinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of seconds that we should attempt to detect an answering machine before timing out and sending a voice request with `AnsweredBy` of `unknown`. The default timeout is 30 seconds.

* * *

recordingStatusCallbackEventarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The recording status events that will trigger calls to the URL specified in `recording_status_callback`. Can be: `in-progress`, `completed` and `absent`. Defaults to `completed`. Separate multiple values with a space.

* * *

trimstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to trim any leading and trailing silence from the recording. Can be: `trim-silence` or `do-not-trim` and the default is `trim-silence`.

* * *

callerIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number, SIP address, or Client identifier that made this call. Phone numbers are in [E.164 format(link takes you to an external page)](https://wwnw.twilio.com/docs/glossary/what-e164 "E.164 format") (e.g., +16175551212). SIP addresses are formatted as `name@company.com`.

* * *

machineDetectionSpeechThresholdinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of milliseconds that is used as the measuring stick for the length of the speech activity, where durations lower than this value will be interpreted as a human and longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.

* * *

machineDetectionSpeechEndThresholdinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.

* * *

machineDetectionSilenceTimeoutinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of milliseconds of initial silence after which an `unknown` AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.

* * *

asyncAmdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Select whether to perform answering machine detection in the background. Default, blocks the execution of the call until Answering Machine Detection is completed. Can be: `true` or `false`.

* * *

asyncAmdStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call using the `async_amd_status_callback_method` to notify customer application whether the call was answered by human, machine or fax.

* * *

asyncAmdStatusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when calling the `async_amd_status_callback` URL. Can be: `GET` or `POST` and the default is `POST`.

Possible values:

`GET``POST`

* * *

byocSID<BY>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that `byoc` is only meaningful when `to` is a phone number; it will otherwise be ignored. (Beta)

Pattern: `^BY[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callReasonstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party's phone. (Branded Calls Beta)

* * *

callTokenstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A token string needed to invoke a forwarded call. A call_token is generated when an incoming call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the original incoming call.

* * *

recordingTrackstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is generated from Twilio. `both` records the audio that is received and generated by Twilio.

* * *

timeLimitinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The maximum duration of the call in seconds. Constraints depend on account and configuration.

* * *

clientNotificationUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should use to deliver `push call notification`.

* * *

urlstring<uri>

required if Twiml or ApplicationSid is not passed

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL that returns the TwiML instructions for the call. We will call this URL using the `method` when the call connects. For more information, see the [Url Parameter](/docs/voice/make-calls#specify-a-url-parameter "Url Parameter") section in [Making Calls](/docs/voice/make-calls "Making Calls").

* * *

twimlstring<twiml>

required if Url or ApplicationSid is not passed

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both `twiml` and `url` are provided then `twiml` parameter will be ignored. Max 4000 characters.

* * *

applicationSidSID<AP>

required if Url or Twiml is not passed

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Application resource that will handle the call, if the call will be handled by an application.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Select from available examples

Copy code block


    {


      "ApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "FallbackMethod": "GET",


      "FallbackUrl": "https://example.com",


      "From": "+987654321",


      "IfMachine": "if_machine",


      "MachineDetection": "enable",


      "MachineDetectionTimeout": 15,


      "Method": "GET",


      "Record": "true",


      "RecordingTrack": "both",


      "Trim": "do-not-trim",


      "SendDigits": "send_digits",


      "StatusCallback": "https://example.com",


      "StatusCallbackMethod": "GET",


      "Timeout": 1,


      "To": "+123456789",


      "Url": "https://example.com",


      "CallerId": "Caller",


      "MachineDetectionSpeechThreshold": 3000,


      "MachineDetectionSpeechEndThreshold": 3000,


      "MachineDetectionSilenceTimeout": 3000,


      "AsyncAmd": "true",


      "AsyncAmdStatusCallback": "http://statuscallback.com",


      "AsyncAmdStatusCallbackMethod": "POST",


      "MachineDetectionEngine": "Lumenvox",


      "MachineDetectionMinWordLength": 100,


      "MachineDetectionMaxWordLength": 5000,


      "MachineDetectionWordsSilence": 50,


      "MachineDetectionMaxNumOfWords": 5,


      "MachineDetectionSilenceThreshold": 256,


      "Byoc": "BYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "CallReason": "Reason for the call (Beta)",


      "TimeLimit": 3600,


      "CallToken": "call-token-string",


      "Transcribe": "true",


      "TranscriptionConfiguration": "JVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "ClientNotificationUrl": "https://clientnotification.com"


    }

(warning)

## Warning

The use of the record attribute is subject to the same obligations and requirements as the [Recordings resource](/docs/voice/api/recording "Recordings resource") and the [`<Record>` TwiML verb](/docs/voice/twiml/record). For workflows subject to [PCI](/docs/voice/pci-workflows "PCI") or the Health Insurance Portability and the Accountability Act (HIPAA), see the applicable documentation.

Create a Call with TwiMLLink to code sample: Create a Call with TwiML

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

    async function createCall() {


    11

      const call = await client.calls.create({


    12

        from: "+15552223214",


    13

        to: "+15558675310",


    14

        twiml: "<Response><Say>Ahoy there!</Say></Response>",


    15

      });


    16




    17

      console.log(call.sid);


    18

    }


    19




    20

    createCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "+15552223214",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+15558675310",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

Create a Call with a URLLink to code sample: Create a Call with a URL

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

    async function createCall() {


    11

      const call = await client.calls.create({


    12

        from: "+15017122661",


    13

        to: "+15558675310",


    14

        url: "http://demo.twilio.com/docs/voice.xml",


    15

      });


    16




    17

      console.log(call.sid);


    18

    }


    19




    20

    createCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "+15017122661",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+15558675310",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

Create a Call and specify a StatusCallback URLLink to code sample: Create a Call and specify a StatusCallback URL

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

    async function createCall() {


    11

      const call = await client.calls.create({


    12

        from: "+18668675310",


    13

        method: "GET",


    14

        statusCallback: "https://www.myapp.com/events",


    15

        statusCallbackMethod: "POST",


    16

        to: "+14155551212",


    17

        url: "http://demo.twilio.com/docs/voice.xml",


    18

      });


    19




    20

      console.log(call.sid);


    21

    }


    22




    23

    createCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "+18668675310",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+14155551212",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

Create a Call and specify a StatusCallbackEventLink to code sample: Create a Call and specify a StatusCallbackEvent

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

    async function createCall() {


    11

      const call = await client.calls.create({


    12

        from: "+18668675310",


    13

        method: "GET",


    14

        statusCallback: "https://www.myapp.com/events",


    15

        statusCallbackEvent: ["initiated", "answered"],


    16

        statusCallbackMethod: "POST",


    17

        to: "+14155551212",


    18

        url: "http://demo.twilio.com/docs/voice.xml",


    19

      });


    20




    21

      console.log(call.sid);


    22

    }


    23




    24

    createCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "+18668675310",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+14155551212",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

### StatusCallback

statuscallback page anchor

Positive FeedbackNegative Feedback

After completing an outbound call, Twilio will make an asynchronous HTTP request to the `StatusCallback` URL you specified in your request (if any).

#### Parameters sent to your StatusCallback URL

parameters-sent-to-your-statuscallback-url page anchor

When Twilio sends its asynchronous request to your `StatusCallback` URL, it includes all of the following parameters:

Parameter| Description
---|---
`CallSid`| A unique identifier for this call, generated by Twilio.
`AccountSid`| Your Twilio account ID. It is 34 characters long, and always starts with the letters `AC`.
`From`| The phone number or client identifier of the party that initiated the call.

Phone numbers use [E.164](/docs/glossary/what-e164 "E.164") formatting, meaning they start with a + and country code, e.g. `+16175551212`.

Client identifiers begin with the `client:` URI scheme; for example, on a call from a client named 'charlie' the `From` parameter will be `client:charlie`.
`To`| The phone number or client identifier of the called party.

Phone numbers use [E.164](/docs/glossary/what-e164 "E.164") formatting, meaning they start with a `+` and country code, e.g. `+16175551212`.

Client identifiers begin with the `client:` URI scheme; for example, for a call to a client named 'joey', the `To` parameter will be `client:joey`.
`CallStatus`| A descriptive status for the call.

The value is one of the following: `queued`, `initiated`, `ringing`, `in-progress`, `completed`, `busy`, `failed`, `no-answer`, or `canceled`.
`ApiVersion`| The version of the Twilio API used to handle this call.

For incoming calls, this is determined by the API version set on the dialed number.

For outgoing calls, this is the version used in the REST API request of the outgoing call.
`Direction`| A string describing the direction of the call:


  * `inbound` for inbound calls
  * `outbound-api` for calls initiated via the REST API
  * `outbound-dial` for calls initiated by a `<Dial>` verb.


`ForwardedFrom`| This parameter may be set when Twilio receives a forwarded call. The carrier who forwards the call determines the contents of the parameter.

Not all carriers support passing this information.

Some carriers provide this information when making a direct call to a Twilio number.
`CallerName`| This parameter is set when the IncomingPhoneNumber that received the call has set its `VoiceCallerIdLookup` value to `true`. Learn about [Lookup pricing(link takes you to an external page)](https://www.twilio.com/en-us/user-authentication-identity/pricing/lookup "Lookup pricing").
`ParentCallSid`| A unique identifier for the call that created this leg.

If this is the first leg of a call, this parameter is not included.
`Caller`| The phone number of the party that initiated the call (same value as `From`).
`Called`| The phone number of the called party (same value as `To`).

Twilio looks up geographic data based on the `To` and `From` phone numbers. If available, Twilio will include the following parameters:

Parameter| Description
---|---
`CalledCity`| The city of the called party.
`CalledState`| The state or province of the called party.
`CalledZip`| The postal code of the called party.
`CalledCountry`| The country of the called party.
`ToCity`| The city of the called party.
`ToState`| The state or province of the called party.
`ToZip`| The postal code of the called party.
`ToCountry`| The country of the called party.

### StatusCallbackEvent

statuscallbackevent page anchor

Positive FeedbackNegative Feedback

If you specify any **call progress events** in the `StatusCallbackEvent` parameter, Twilio will make an asynchronous request to the `StatusCallback` URL you provided in your `POST` request.

The call progress events you can specify are:

Event| Description
---|---
`initiated`| Twilio removes your call from the queue and starts dialing.
`ringing`| The call starts ringing.
`answered`| The call is answered. If this event is specified, Twilio will send an `in-progress` status.
`completed`| The call is completed, regardless of the termination status (which can be `busy`, `canceled`, `completed`, `failed`, or `no-answer`). If no `StatusCallbackEvent` is specified, completed is fired by default.

When these events occur, Twilio's `StatusCallback` request will also include these additional parameters:

Parameter| Description
---|---
`CallStatus`| A descriptive status for the call. The value is one of `queued`, `initiated`, `ringing`, `in-progress`, `completed`, `busy`, `failed`, `no-answer`, or `canceled`. For more details, see the [CallStatus values in our TwiML introduction](/docs/voice/twiml#callstatus-values "CallStatus values in our TwiML introduction").
`Duration`| The duration in minutes of the just-completed call; calls are billed by the minute. Only present in the `completed` event.
`CallDuration`| The duration in seconds of the just-completed call. Only present in terminal events (`completed`, `busy`, `failed`, `no-answer`, or `canceled`).
`SipResponseCode`| The SIP response code for the call. Only present in terminal events (`completed`, `busy`, `failed`, `no-answer`, or `canceled`). For example, if the destination phone number is unreachable, the API returns `404`. If the call doesn't connect before the specified `Timeout` value elapses, the API returns `487`.
`RecordingUrl`| The URL of the phone call's recorded audio. This parameter is included only if `Record=true` is set on the REST API request and does not include recordings initiated in other ways. `RecordingUrl` is only present in the `completed` event. The recording file may not yet be accessible when the Status Callback is sent.

_**Note:**_ _Use RecordingStatusCallback for reliable notification on when the recording is available for access._
`RecordingSid`| The unique ID of the [Recording](/docs/voice/api/recording "Recording") from this call. `RecordingSid` is only present with the `completed` event.
`RecordingDuration`| The duration of the recorded audio (in seconds). `RecordingDuration` is only present in the `completed` event. To get a final accurate recording duration after any trimming of silence, use `RecordingStatusCallback`.
`Timestamp`| The timestamp when the event fired, given as UTC in [RFC 2822(link takes you to an external page)](https://php.net/manual/en/class.datetime.php#datetime.constants.rfc2822 "RFC 2822") format.
`CallbackSource`| A string that describes the source of the webhook. This is provided to help disambiguate why the webhook was made. On Status Callbacks, this value is always `call-progress-events`.
`SequenceNumber`| The order in which the events were fired, starting from `0`. Although events are fired in order, they are made as separate HTTP requests, and there is no guarantee they will arrive in the same order.
`StirStatus`| The [STIR/SHAKEN](/docs/voice/trusted-calling-with-shakenstir "STIR/SHAKEN") attestation status for the call. Present in `ringing` and `in-progress` events. Possible values include `A` (full attestation), `B` (partial attestation), `C` (gateway attestation), or `null` if unavailable.

(information)

## Info

You can use the `StatusCallback` and `StatusCallbackEvent` features to track the call status of Programmable Voice calls only.

(information)

## Info

To learn more about the `StatusCallbackEvent` parameter and what you can expect from Twilio during and after an outbound call, see [Make outbound phone calls](/docs/voice/tutorials/how-to-make-outbound-phone-calls "Make outbound phone calls").

### RecordingStatusCallback

recordingstatuscallback page anchor

Positive FeedbackNegative Feedback

If you requested a recording of your outbound call and you specified a `RecordingStatusCallback` URL, Twilio will make a `GET` or `POST` request to that URL when the recording is available.

#### Parameters sent to your RecordingStatusCallback URL

parameters-sent-to-your-recordingstatuscallback-url page anchor

Twilio will pass along the following parameters to your `RecordingStatusCallback` URL:

Parameter| Description
---|---
`AccountSid`| The unique identifier of the Account responsible for this recording.
`CallSid`| A unique identifier for the call associated with the recording. CallSid will always refer to the parent leg of a two-leg call.
`RecordingSid`| The unique identifier for the recording.
`RecordingUrl`| The URL of the recorded audio.
`RecordingStatus`| The status of the recording. Possible values are: `in-progress`, `completed`, `absent`.
`RecordingDuration`| The length of the recording, in seconds.
`RecordingChannels`| The number of channels in the final recording file as an integer. Possible values are `1`, `2`.
`RecordingStartTime`| The timestamp of when the recording started.
`RecordingSource`| The initiation method used to create this recording. For recordings initiated when `Record=true` is set on the REST API, `OutboundAPI` will be returned.
`RecordingTrack`| The audio track recorded. Possible values are `inbound`, `outbound`, or `both`.

### RecordingStatusCallbackEvent

recordingstatuscallbackevent page anchor

Positive FeedbackNegative Feedback

Just as you can specify call progress events with `StatusCallbackEvent`, you can also specify which recording status changes should trigger a callback to your application.

Available recording status values are:

Parameter| Description
---|---
`in-progress`| The recording has started.
`completed`| The recording is complete and available for access.
`absent`| The recording is absent and inaccessible.

This parameter defaults to `completed`. To specify multiple values, separate them with a space.

(information)

## Info

To pause, resume, or stop recordings, see the [Recordings subresource](/docs/voice/api/recording "Recordings subresource").

* * *

## Retrieve a Call

retrieve-a-call page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json`

This API call returns a Call resource of an individual call, identified by its `CallSid`. This resource is [eventually consistent(link takes you to an external page)](https://en.wikipedia.org/wiki/Eventual_consistency "eventually consistent").

(warning)

## Warning

To get real-time call status updates, we recommend using the [StatusCallbackEvent](/docs/voice/tutorials/how-to-make-outbound-phone-calls#receive-call-status-updates "StatusCallbackEvent") or the [TwiML `<Dial>` verb statusCallbackEvent attribute](/docs/voice/twiml/number#attributes-status-callback-event) for the case of child calls.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Call resource(s) to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Call resource to fetch.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve a CallLink to code sample: Retrieve a Call

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

    async function fetchCall() {


    11

      const call = await client.calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch();


    12




    13

      console.log(call.sid);


    14

    }


    15




    16

    fetchCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": "machine_start",


    4

      "api_version": "2010-04-01",


    5

      "caller_name": "callerid",


    6

      "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",


    7

      "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",


    8

      "direction": "outbound-api",


    9

      "duration": "4",


    10

      "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",


    11

      "forwarded_from": "calledvia",


    12

      "from": "+13051416799",


    13

      "from_formatted": "(305) 141-6799",


    14

      "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",


    15

      "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",


    16

      "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",


    17

      "price": "-0.200",


    18

      "price_unit": "USD",


    19

      "sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    20

      "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+13051913581",


    35

      "to_formatted": "(305) 191-3581",


    36

      "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

### Recordings

recordings page anchor

Positive FeedbackNegative Feedback

You can access the Recordings subresource on any given Call.

The following will return a list of all of the recordings generated with a given call (identified by its `CallSid`):

Copy code block


    /2010-04-01/Accounts/{YourAccountSid}/Calls/{CallSid}/Recordings

Learn more about the [Recordings resource](/docs/voice/api/recording "Recordings resource").

* * *

## Retrieve a list of Calls

retrieve-a-list-of-calls page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls.json`

Return a list of phone calls made to and from an account, identified by its `AccountSid`.

The following query string parameters allow you to filter and limit the list returned to you by the REST API. **These parameters are case-sensitive.**

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Call resource(s) to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

tostring<phone-number>

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Only show calls made to this phone number, SIP address, Client identifier or SIM SID.

* * *

fromstring<phone-number>

Optional

[PII MTL: 120 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Only include calls from this phone number, SIP address, Client identifier or SIM SID.

* * *

parentCallSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include calls spawned by calls with this SID.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the calls to include. Can be: `queued`, `ringing`, `in-progress`, `canceled`, `completed`, `failed`, `busy`, or `no-answer`.

Possible values:

`queued``ringing``in-progress``completed``busy``failed``no-answer``canceled`

* * *

startTimestring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include calls that started on this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only calls that started on this date.

* * *

startTimeBeforestring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include calls that started before this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only calls that started before this date.

* * *

startTimeAfterstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include calls that started on or after this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only calls that started on or after this date.

* * *

endTimestring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include calls that ended on this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only calls that ended on this date.

* * *

endTimeBeforestring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include calls that ended before this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only calls that ended before this date.

* * *

endTimeAfterstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include calls that ended on or after this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only calls that ended on or after this date.

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

Retrieve a list of CallsLink to code sample: Retrieve a list of Calls

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

    async function listCall() {


    11

      const calls = await client.calls.list({ limit: 20 });


    12




    13

      calls.forEach((c) => console.log(c.sid));


    14

    }


    15




    16

    listCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "calls": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "answered_by": "machine_start",


    6

          "api_version": "2010-04-01",


    7

          "caller_name": "callerid1",


    8

          "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",


    9

          "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",


    10

          "direction": "outbound-api",


    11

          "duration": "4",


    12

          "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",


    13

          "forwarded_from": "calledvia1",


    14

          "from": "+13051416799",


    15

          "from_formatted": "(305) 141-6799",


    16

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",


    17

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",


    18

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",


    19

          "price": "-0.200",


    20

          "price_unit": "USD",


    21

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",


    23

          "status": "completed",


    24

          "subresource_uris": {


    25

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    26

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    27

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    28

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    29

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    30

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    31

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    32

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    33

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    34

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    35

          },


    36

          "to": "+13051913581",


    37

          "to_formatted": "(305) 191-3581",


    38

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    39

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    40

          "queue_time": "1000"


    41

        },


    42

        {


    43

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

          "answered_by": "human",


    45

          "api_version": "2010-04-01",


    46

          "caller_name": "callerid2",


    47

          "date_created": "Fri, 18 Oct 2019 16:00:00 +0000",


    48

          "date_updated": "Fri, 18 Oct 2019 16:01:00 +0000",


    49

          "direction": "inbound",


    50

          "duration": "3",


    51

          "end_time": "Fri, 18 Oct 2019 16:03:00 +0000",


    52

          "forwarded_from": "calledvia2",


    53

          "from": "+13051416798",


    54

          "from_formatted": "(305) 141-6798",


    55

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeee",


    56

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeee",


    57

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeee",


    58

          "price": "-0.100",


    59

          "price_unit": "JPY",


    60

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    61

          "start_time": "Fri, 18 Oct 2019 16:02:00 +0000",


    62

          "status": "completed",


    63

          "subresource_uris": {


    64

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Notifications.json",


    65

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Recordings.json",


    66

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Payments.json",


    67

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Events.json",


    68

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Siprec.json",


    69

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Streams.json",


    70

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Transcriptions.json",


    71

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/TwimlSessions.json",


    72

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessageSubscriptions.json",


    73

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessages.json"


    74

          },


    75

          "to": "+13051913580",


    76

          "to_formatted": "(305) 191-3580",


    77

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    78

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0.json",


    79

          "queue_time": "1000"


    80

        }


    81

      ],


    82

      "end": 1,


    83

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0",


    84

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=1&PageToken=PACAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    85

      "page": 0,


    86

      "page_size": 2,


    87

      "previous_page_uri": null,


    88

      "start": 0,


    89

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0"


    90

    }

Retrieve a list of Calls and filter by start dateLink to code sample: Retrieve a list of Calls and filter by start date

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

    async function listCall() {


    11

      const calls = await client.calls.list({


    12

        startTime: new Date("2009-07-06 00:00:00"),


    13

        status: "completed",


    14

        limit: 20,


    15

      });


    16




    17

      calls.forEach((c) => console.log(c.sid));


    18

    }


    19




    20

    listCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "calls": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "answered_by": "machine_start",


    6

          "api_version": "2010-04-01",


    7

          "caller_name": "callerid1",


    8

          "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",


    9

          "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",


    10

          "direction": "outbound-api",


    11

          "duration": "4",


    12

          "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",


    13

          "forwarded_from": "calledvia1",


    14

          "from": "+13051416799",


    15

          "from_formatted": "(305) 141-6799",


    16

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",


    17

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",


    18

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",


    19

          "price": "-0.200",


    20

          "price_unit": "USD",


    21

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",


    23

          "status": "completed",


    24

          "subresource_uris": {


    25

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    26

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    27

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    28

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    29

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    30

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    31

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    32

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    33

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    34

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    35

          },


    36

          "to": "+13051913581",


    37

          "to_formatted": "(305) 191-3581",


    38

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    39

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    40

          "queue_time": "1000"


    41

        },


    42

        {


    43

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

          "answered_by": "human",


    45

          "api_version": "2010-04-01",


    46

          "caller_name": "callerid2",


    47

          "date_created": "Fri, 18 Oct 2019 16:00:00 +0000",


    48

          "date_updated": "Fri, 18 Oct 2019 16:01:00 +0000",


    49

          "direction": "inbound",


    50

          "duration": "3",


    51

          "end_time": "Fri, 18 Oct 2019 16:03:00 +0000",


    52

          "forwarded_from": "calledvia2",


    53

          "from": "+13051416798",


    54

          "from_formatted": "(305) 141-6798",


    55

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeee",


    56

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeee",


    57

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeee",


    58

          "price": "-0.100",


    59

          "price_unit": "JPY",


    60

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    61

          "start_time": "Fri, 18 Oct 2019 16:02:00 +0000",


    62

          "status": "completed",


    63

          "subresource_uris": {


    64

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Notifications.json",


    65

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Recordings.json",


    66

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Payments.json",


    67

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Events.json",


    68

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Siprec.json",


    69

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Streams.json",


    70

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Transcriptions.json",


    71

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/TwimlSessions.json",


    72

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessageSubscriptions.json",


    73

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessages.json"


    74

          },


    75

          "to": "+13051913580",


    76

          "to_formatted": "(305) 191-3580",


    77

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    78

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0.json",


    79

          "queue_time": "1000"


    80

        }


    81

      ],


    82

      "end": 1,


    83

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0",


    84

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=1&PageToken=PACAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    85

      "page": 0,


    86

      "page_size": 2,


    87

      "previous_page_uri": null,


    88

      "start": 0,


    89

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0"


    90

    }

Retrieve a list of Calls and filter by 'after start' dateLink to code sample: Retrieve a list of Calls and filter by 'after start' date

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

    async function listCall() {


    11

      const calls = await client.calls.list({


    12

        startTimeAfter: new Date("2009-07-06 00:00:00"),


    13

        status: "completed",


    14

        limit: 20,


    15

      });


    16




    17

      calls.forEach((c) => console.log(c.sid));


    18

    }


    19




    20

    listCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "calls": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "answered_by": "machine_start",


    6

          "api_version": "2010-04-01",


    7

          "caller_name": "callerid1",


    8

          "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",


    9

          "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",


    10

          "direction": "outbound-api",


    11

          "duration": "4",


    12

          "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",


    13

          "forwarded_from": "calledvia1",


    14

          "from": "+13051416799",


    15

          "from_formatted": "(305) 141-6799",


    16

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",


    17

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",


    18

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",


    19

          "price": "-0.200",


    20

          "price_unit": "USD",


    21

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",


    23

          "status": "completed",


    24

          "subresource_uris": {


    25

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    26

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    27

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    28

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    29

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    30

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    31

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    32

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    33

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    34

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    35

          },


    36

          "to": "+13051913581",


    37

          "to_formatted": "(305) 191-3581",


    38

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    39

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    40

          "queue_time": "1000"


    41

        },


    42

        {


    43

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

          "answered_by": "human",


    45

          "api_version": "2010-04-01",


    46

          "caller_name": "callerid2",


    47

          "date_created": "Fri, 18 Oct 2019 16:00:00 +0000",


    48

          "date_updated": "Fri, 18 Oct 2019 16:01:00 +0000",


    49

          "direction": "inbound",


    50

          "duration": "3",


    51

          "end_time": "Fri, 18 Oct 2019 16:03:00 +0000",


    52

          "forwarded_from": "calledvia2",


    53

          "from": "+13051416798",


    54

          "from_formatted": "(305) 141-6798",


    55

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeee",


    56

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeee",


    57

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeee",


    58

          "price": "-0.100",


    59

          "price_unit": "JPY",


    60

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    61

          "start_time": "Fri, 18 Oct 2019 16:02:00 +0000",


    62

          "status": "completed",


    63

          "subresource_uris": {


    64

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Notifications.json",


    65

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Recordings.json",


    66

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Payments.json",


    67

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Events.json",


    68

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Siprec.json",


    69

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Streams.json",


    70

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Transcriptions.json",


    71

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/TwimlSessions.json",


    72

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessageSubscriptions.json",


    73

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessages.json"


    74

          },


    75

          "to": "+13051913580",


    76

          "to_formatted": "(305) 191-3580",


    77

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    78

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0.json",


    79

          "queue_time": "1000"


    80

        }


    81

      ],


    82

      "end": 1,


    83

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0",


    84

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=1&PageToken=PACAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    85

      "page": 0,


    86

      "page_size": 2,


    87

      "previous_page_uri": null,


    88

      "start": 0,


    89

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0"


    90

    }

Retrieve a list of Calls and filter by a period of timeLink to code sample: Retrieve a list of Calls and filter by a period of time

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

    async function listCall() {


    11

      const calls = await client.calls.list({


    12

        startTimeBefore: new Date("2009-07-06 00:00:00"),


    13

        startTimeAfter: new Date("2009-07-04 00:00:00"),


    14

        status: "in-progress",


    15

        limit: 20,


    16

      });


    17




    18

      calls.forEach((c) => console.log(c.sid));


    19

    }


    20




    21

    listCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "calls": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "answered_by": "machine_start",


    6

          "api_version": "2010-04-01",


    7

          "caller_name": "callerid1",


    8

          "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",


    9

          "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",


    10

          "direction": "outbound-api",


    11

          "duration": "4",


    12

          "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",


    13

          "forwarded_from": "calledvia1",


    14

          "from": "+13051416799",


    15

          "from_formatted": "(305) 141-6799",


    16

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",


    17

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",


    18

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",


    19

          "price": "-0.200",


    20

          "price_unit": "USD",


    21

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",


    23

          "status": "completed",


    24

          "subresource_uris": {


    25

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    26

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    27

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    28

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    29

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    30

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    31

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    32

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    33

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    34

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    35

          },


    36

          "to": "+13051913581",


    37

          "to_formatted": "(305) 191-3581",


    38

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    39

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    40

          "queue_time": "1000"


    41

        },


    42

        {


    43

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

          "answered_by": "human",


    45

          "api_version": "2010-04-01",


    46

          "caller_name": "callerid2",


    47

          "date_created": "Fri, 18 Oct 2019 16:00:00 +0000",


    48

          "date_updated": "Fri, 18 Oct 2019 16:01:00 +0000",


    49

          "direction": "inbound",


    50

          "duration": "3",


    51

          "end_time": "Fri, 18 Oct 2019 16:03:00 +0000",


    52

          "forwarded_from": "calledvia2",


    53

          "from": "+13051416798",


    54

          "from_formatted": "(305) 141-6798",


    55

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeee",


    56

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeee",


    57

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeee",


    58

          "price": "-0.100",


    59

          "price_unit": "JPY",


    60

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    61

          "start_time": "Fri, 18 Oct 2019 16:02:00 +0000",


    62

          "status": "completed",


    63

          "subresource_uris": {


    64

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Notifications.json",


    65

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Recordings.json",


    66

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Payments.json",


    67

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Events.json",


    68

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Siprec.json",


    69

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Streams.json",


    70

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Transcriptions.json",


    71

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/TwimlSessions.json",


    72

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessageSubscriptions.json",


    73

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessages.json"


    74

          },


    75

          "to": "+13051913580",


    76

          "to_formatted": "(305) 191-3580",


    77

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    78

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0.json",


    79

          "queue_time": "1000"


    80

        }


    81

      ],


    82

      "end": 1,


    83

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0",


    84

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=1&PageToken=PACAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    85

      "page": 0,


    86

      "page_size": 2,


    87

      "previous_page_uri": null,


    88

      "start": 0,


    89

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0"


    90

    }

Retrieve a list of Calls and filter by call status and phone numberLink to code sample: Retrieve a list of Calls and filter by call status and phone number

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

    async function listCall() {


    11

      const calls = await client.calls.list({


    12

        status: "busy",


    13

        to: "+15558675310",


    14

        limit: 20,


    15

      });


    16




    17

      calls.forEach((c) => console.log(c.sid));


    18

    }


    19




    20

    listCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "calls": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "answered_by": "machine_start",


    6

          "api_version": "2010-04-01",


    7

          "caller_name": "callerid1",


    8

          "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",


    9

          "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",


    10

          "direction": "outbound-api",


    11

          "duration": "4",


    12

          "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",


    13

          "forwarded_from": "calledvia1",


    14

          "from": "+13051416799",


    15

          "from_formatted": "(305) 141-6799",


    16

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",


    17

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",


    18

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",


    19

          "price": "-0.200",


    20

          "price_unit": "USD",


    21

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",


    23

          "status": "completed",


    24

          "subresource_uris": {


    25

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    26

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    27

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    28

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    29

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    30

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    31

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    32

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    33

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    34

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    35

          },


    36

          "to": "+13051913581",


    37

          "to_formatted": "(305) 191-3581",


    38

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    39

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    40

          "queue_time": "1000"


    41

        },


    42

        {


    43

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

          "answered_by": "human",


    45

          "api_version": "2010-04-01",


    46

          "caller_name": "callerid2",


    47

          "date_created": "Fri, 18 Oct 2019 16:00:00 +0000",


    48

          "date_updated": "Fri, 18 Oct 2019 16:01:00 +0000",


    49

          "direction": "inbound",


    50

          "duration": "3",


    51

          "end_time": "Fri, 18 Oct 2019 16:03:00 +0000",


    52

          "forwarded_from": "calledvia2",


    53

          "from": "+13051416798",


    54

          "from_formatted": "(305) 141-6798",


    55

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeee",


    56

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeee",


    57

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeee",


    58

          "price": "-0.100",


    59

          "price_unit": "JPY",


    60

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    61

          "start_time": "Fri, 18 Oct 2019 16:02:00 +0000",


    62

          "status": "completed",


    63

          "subresource_uris": {


    64

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Notifications.json",


    65

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Recordings.json",


    66

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Payments.json",


    67

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Events.json",


    68

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Siprec.json",


    69

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Streams.json",


    70

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Transcriptions.json",


    71

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/TwimlSessions.json",


    72

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessageSubscriptions.json",


    73

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessages.json"


    74

          },


    75

          "to": "+13051913580",


    76

          "to_formatted": "(305) 191-3580",


    77

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    78

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0.json",


    79

          "queue_time": "1000"


    80

        }


    81

      ],


    82

      "end": 1,


    83

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0",


    84

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=1&PageToken=PACAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    85

      "page": 0,


    86

      "page_size": 2,


    87

      "previous_page_uri": null,


    88

      "start": 0,


    89

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0"


    90

    }

Retrieve a list of Calls and filter by calls made from a specific deviceLink to code sample: Retrieve a list of Calls and filter by calls made from a specific device

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

    async function listCall() {


    11

      const calls = await client.calls.list({


    12

        from: "client:charlie",


    13

        limit: 20,


    14

      });


    15




    16

      calls.forEach((c) => console.log(c.sid));


    17

    }


    18




    19

    listCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "calls": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "answered_by": "machine_start",


    6

          "api_version": "2010-04-01",


    7

          "caller_name": "callerid1",


    8

          "date_created": "Fri, 18 Oct 2019 17:00:00 +0000",


    9

          "date_updated": "Fri, 18 Oct 2019 17:01:00 +0000",


    10

          "direction": "outbound-api",


    11

          "duration": "4",


    12

          "end_time": "Fri, 18 Oct 2019 17:03:00 +0000",


    13

          "forwarded_from": "calledvia1",


    14

          "from": "+13051416799",


    15

          "from_formatted": "(305) 141-6799",


    16

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeef",


    17

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeef",


    18

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeef",


    19

          "price": "-0.200",


    20

          "price_unit": "USD",


    21

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "start_time": "Fri, 18 Oct 2019 17:02:00 +0000",


    23

          "status": "completed",


    24

          "subresource_uris": {


    25

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    26

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    27

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    28

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    29

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    30

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    31

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    32

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    33

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    34

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    35

          },


    36

          "to": "+13051913581",


    37

          "to_formatted": "(305) 191-3581",


    38

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    39

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    40

          "queue_time": "1000"


    41

        },


    42

        {


    43

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

          "answered_by": "human",


    45

          "api_version": "2010-04-01",


    46

          "caller_name": "callerid2",


    47

          "date_created": "Fri, 18 Oct 2019 16:00:00 +0000",


    48

          "date_updated": "Fri, 18 Oct 2019 16:01:00 +0000",


    49

          "direction": "inbound",


    50

          "duration": "3",


    51

          "end_time": "Fri, 18 Oct 2019 16:03:00 +0000",


    52

          "forwarded_from": "calledvia2",


    53

          "from": "+13051416798",


    54

          "from_formatted": "(305) 141-6798",


    55

          "group_sid": "GPdeadbeefdeadbeefdeadbeefdeadbeee",


    56

          "parent_call_sid": "CAdeadbeefdeadbeefdeadbeefdeadbeee",


    57

          "phone_number_sid": "PNdeadbeefdeadbeefdeadbeefdeadbeee",


    58

          "price": "-0.100",


    59

          "price_unit": "JPY",


    60

          "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    61

          "start_time": "Fri, 18 Oct 2019 16:02:00 +0000",


    62

          "status": "completed",


    63

          "subresource_uris": {


    64

            "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Notifications.json",


    65

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Recordings.json",


    66

            "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Payments.json",


    67

            "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Events.json",


    68

            "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Siprec.json",


    69

            "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Streams.json",


    70

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/Transcriptions.json",


    71

            "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/TwimlSessions.json",


    72

            "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessageSubscriptions.json",


    73

            "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0/UserDefinedMessages.json"


    74

          },


    75

          "to": "+13051913580",


    76

          "to_formatted": "(305) 191-3580",


    77

          "trunk_sid": "TKdeadbeefdeadbeefdeadbeefdeadbeef",


    78

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0.json",


    79

          "queue_time": "1000"


    80

        }


    81

      ],


    82

      "end": 1,


    83

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0",


    84

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=1&PageToken=PACAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0",


    85

      "page": 0,


    86

      "page_size": 2,


    87

      "previous_page_uri": null,


    88

      "start": 0,


    89

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls.json?Status=completed&To=%2B123456789&From=%2B987654321&StartTime=2008-01-02&ParentCallSid=CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&EndTime=2009-01-02&PageSize=2&Page=0"


    90

    }

(information)

## Info

You can append a `.csv` extension to any resource URI to get CSV (Comma Separated Values) representation. Specifying CSV may be especially useful for call logs. Try this:

Copy code block


    GET /2010-04-01/Accounts/{AccountSid}/Calls.csv

Learn more about [API response formats](/docs/usage/twilios-response "API response formats").

### Paging

paging page anchor

Positive FeedbackNegative Feedback

If you are using the Twilio REST API, the list returned to you includes [paging information](/docs/usage/twilios-response#pagination "paging information").

If you plan to request more records than will fit on a single page, you can use the provided `nextpageuri` rather than incrementing through pages by page number.

Using `nextpageuri` for paging ensures that your next request will pick up where you left off. This can help keep you from retrieving duplicate data if you are actively making or receiving calls.

(information)

## Info

All of the [Twilio SDKs](/docs/libraries "Twilio SDKs") handle paging automatically. You do not need to explicitly request individual pages when using an SDK to fetch lists of resources.

* * *

## Update a Call

update-a-call page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json`

Updating a Call allows you to modify an active call.

Real-time call modification allows you to interrupt an in-progress call and terminate it or have it begin processing TwiML from either a new URL or from the TwiML provided with modification. Call modification is useful for any application where you want to change the behavior of a running call asynchronously, e.g., hold music, call queues, transferring calls, or forcing a hangup.

By sending an HTTP `POST` request to a specific Call instance, you can redirect a call that is in progress or you can terminate a call.

(information)

## Info

For step-by-step guidance on modifying in-progress calls, check out the tutorial [Modify Calls in Progress](/docs/voice/tutorials/how-to-modify-calls-in-progress "Modify Calls in Progress") in your web language of choice.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Call resource(s) to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Call resource to update

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL that returns the TwiML instructions for the call. We will call this URL using the `method` when the call connects. For more information, see the [Url Parameter](/docs/voice/make-calls#specify-a-url-parameter "Url Parameter") section in [Making Calls](/docs/voice/make-calls "Making Calls").

* * *

methodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when calling the `url`. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored.

Possible values:

`GET``POST`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`canceled``completed`

* * *

fallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call using the `fallback_method` if an error occurs when requesting or executing the TwiML at `url`. If an `application_sid` parameter is present, this parameter is ignored.

* * *

fallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to request the `fallback_url`. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored.

Possible values:

`GET``POST`

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `status_callback_method` to send status information to your application. If no `status_callback_event` is specified, we will send the `completed` status. If an `application_sid` parameter is present, this parameter is ignored. URLs must contain a valid hostname (underscores are not permitted).

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when requesting the `status_callback` URL. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored.

Possible values:

`GET``POST`

* * *

twimlstring<twiml>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

TwiML instructions for the call Twilio will use without fetching Twiml from url. Twiml and url parameters are mutually exclusive

* * *

timeLimitinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The maximum duration of the call in seconds. Constraints depend on account and configuration.

Select from available examples

Copy code block


    {


      "FallbackMethod": "GET",


      "FallbackUrl": "https://example.com",


      "Method": "GET",


      "Status": "completed",


      "StatusCallback": "https://example.com",


      "StatusCallbackUrl": "https://example.com",


      "StatusCallbackMethod": "GET",


      "Url": "https://example.com"


    }

Update a Call in progress with TwiMLLink to code sample: Update a Call in progress with TwiML

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

    async function updateCall() {


    11

      const call = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ twiml: "<Response><Say>Ahoy there</Say></Response>" });


    14




    15

      console.log(call.sid);


    16

    }


    17




    18

    updateCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "+14158675308",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+14158675309",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

Update a Call in progress with URLLink to code sample: Update a Call in progress with URL

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

    async function updateCall() {


    11

      const call = await client.calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update({


    12

        method: "POST",


    13

        url: "http://demo.twilio.com/docs/voice.xml",


    14

      });


    15




    16

      console.log(call.sid);


    17

    }


    18




    19

    updateCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "+14158675308",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+14158675309",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

Update a Call: End the callLink to code sample: Update a Call: End the call

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

    async function updateCall() {


    11

      const call = await client


    12

        .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .update({ status: "completed" });


    14




    15

      console.log(call.sid);


    16

    }


    17




    18

    updateCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "+14158675308",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+14158675309",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

When you redirect an active call to another phone number, Twilio creates an entirely new Call instance for that new phone number. The original call is the **parent call** , and any additional number dialed establishes a **child call**. Parent and child calls will have uniquely identifying Call SIDs.

Note that any parent call currently executing a [<Dial>](/docs/voice/twiml/dial "<Dial>") is considered in-progress by Twilio. Even if you've re-directed your initial call to a new number, the parent call is still active, and thus you must use `Status=completed` to end it.

Update the StatusCallback of an active CallLink to code sample: Update the StatusCallback of an active Call

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

    async function updateCall() {


    11

      const call = await client.calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update({


    12

        statusCallback: "https://example.com/status-changed",


    13

        url: "https://example.com/twiml",


    14

      });


    15




    16

      console.log(call.sid);


    17

    }


    18




    19

    updateCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "+14158675308",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "+14158675309",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

(warning)

## Warning

To update a `StatusCallback` on a Call, it is required to set the `Url` in the same statement.

* * *

## Delete a Call

delete-a-call page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json`

This will delete a call record from your account. Once the record is deleted, it will no longer appear in the API and Account Portal logs.

If successful, this `DELETE` returns an HTTP 204 (No Content) with no body.

`DELETE` on a call record will also delete any associated [call events](/docs/voice/api/call-event-resource "call events"), but will not delete associated [recordings](/docs/voice/api/recording "recordings") and [transcription](/docs/voice/api/recording-transcription "transcription") records.

(warning)

## Warning

Note that an error will occur if you attempt to remove a call record for a call that is actively in progress.

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Call resource(s) to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided Call SID that uniquely identifies the Call resource to delete

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

(error)

## Danger

**Note:** For calls less than 13 months old, resources deleted from this endpoint will also be deleted in Log Archives. Calls older than 13 months can _only_ be deleted via the Bulk Export API.

Delete a Call resourceLink to code sample: Delete a Call resource

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

    async function deleteCall() {


    11

      await client.calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").remove();


    12

    }


    13




    14

    deleteCall();

* * *

## Call resource retention

call-resource-retention page anchor

Positive FeedbackNegative Feedback

You are able to retrieve resources via `GET` to the `/Calls` endpoint for 13 months after the resource is created. Records older than thirteen months can only be retrieved via Bulk Export.

We provide a Bulk Export utility in [Console(link takes you to an external page)](https://www.twilio.com/console/voice/settings/calls-archives "Console") and via [API](/docs/usage/bulkexport "API"). Bulk Export will generate S3 files containing one day of data per file and deliver the download link via webhook, email, or Console.

* * *

## What's next?

whats-next page anchor

Positive FeedbackNegative Feedback

Explore [Voice Insights](/docs/voice/voice-insights "Voice Insights") with its [Call Insights Event Stream](/docs/voice/voice-insights/event-streams/call-insights-events "Call Insights Event Stream") and [Call Insights REST API](/docs/voice/voice-insights/api/call "Call Insights REST API") which allow you to see call parameters, investigate call metrics and event timelines, and understand detected quality issues.