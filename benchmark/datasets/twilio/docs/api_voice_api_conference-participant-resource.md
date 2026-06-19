# Conferences Participants subresource

*Source: https://www.twilio.com/docs/voice/api/conference-participant-resource*

---

# Conferences Participants subresource

Positive FeedbackNegative Feedback

* * *

Participants is a subresource of [Conferences](/docs/voice/api/conference-resource "Conferences") and represents a participant who is either connecting to, or actively connected to, a [Conference](/docs/voice/api/conference-resource "Conference") that is not in [completed](/docs/voice/api/conference-resource#conference-properties "completed") status. This means that the Participants endpoint will not return results for participants whose call has ended, whose associated conference has ended, or whose call has been modified to use new TwiML; i.e. this resource does not return historical participant logs. For post-call participant details, use the [Participants resource](/docs/voice/voice-insights/api/conference/participant-summary-resource "Participants resource") of the Voice Insights API.

The Participants subresource allows you to:

  * Manipulate a conference's current participants by muting or removing them from the conference.
  * List of all the participants in an active conference.
  * Get information about a particular participant in an active conference.
  * Add participants to a conference.


(information)

## Info

Tracking updates to all conference participants over the course of a conference can be done by using the [Conference's statusCallback webhook](/docs/voice/twiml/conference "Conference's statusCallback webhook").

* * *

## Participant Properties

participant-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Participant resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Participant resource is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

labelstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The user-specified label of this participant, if one was given when the participant was created. This may be used to fetch, update or delete the participant.

* * *

callSidToCoachSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

coachingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined.

* * *

conferenceSidSID<CF>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the conference the participant is in.

Pattern: `^CF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the resource was last updated specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

endConferenceOnExitboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the conference ends when the participant leaves. Can be: `true` or `false` and the default is `false`. If `true`, the conference ends and all other participants drop out when the participant leaves.

* * *

mutedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the participant is muted. Can be `true` or `false`.

* * *

holdboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the participant is on hold. Can be `true` or `false`.

* * *

startConferenceOnEnterboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the conference starts when the participant joins the conference, if it has not already started. Can be: `true` or `false` and the default is `true`. If `false` and the conference has not started, the participant is muted and hears background music until another participant starts the conference.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the participant's call in a session. Can be: `queued`, `connecting`, `ringing`, `connected`, `complete`, or `failed`.

Possible values:

`queued``connecting``ringing``connected``complete``failed`

* * *

queueTimestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The wait time in milliseconds before participant's call is placed. Only available in the response to a create participant request.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

## Create a Participant

create-a-participant page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json`

Creates a Participant subresource with either a `ConferenceSid` or `FriendlyName` initiates an outbound call and adds a new participant to the active [Conference](/docs/voice/api/conference-resource "Conference") with that `ConferenceSid` or `FriendlyName`.

If an active conference does not exist with your `FriendlyName`, we create a new conference with that name and add the participant.

If a conference specified by `ConferenceSid` is not active, the request fails.

(information)

## Calls Per Second (CPS)

By default, each account is granted one CPS for calls created via `POST` requests to the `/Participants` endpoint. Inbound calls and `<Dial>` calls are not limited by CPS. Accounts with an approved [Business Profile(link takes you to an external page)](https://console.twilio.com/us1/account/trust-hub/customer-profiles "Business Profile") can update their CPS up to 30 in the Twilio Console. In aggregate, calls are executed at the rate defined by the CPS. Individual calls may not execute at the anticipated rate — you may see individual seconds with more or fewer CPS, especially for inconsistent traffic — but over a month, the call execution rate will average the CPS rate set for that account.

(error)

## Danger

Do not use [personally identifiable information (PII)](/docs/glossary/what-is-personally-identifiable-information-pii "personally identifiable information \(PII\)") such as phone numbers, email addresses, a person's name, or any other sensitive information when assigning a `FriendlyName` to your conferences.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that will create the resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conferenceSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the participant's conference.

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

fromstring<endpoint>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](/docs/glossary/what-e164 "E.164") format (e.g., +16175551212). Client identifiers are formatted `client:name`. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](/docs/voice/api/outgoing-caller-ids "outgoing caller id") for your account. If the `to` parameter is a phone number, `from` must also be a phone number. If `to` is sip address, this value of `from` should be a username portion to be used to populate the P-Asserted-Identity header that is passed to the SIP endpoint.

* * *

tostring<endpoint>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number, SIP address, Client, TwiML App identifier that received this call. Phone numbers are in [E.164](/docs/glossary/what-e164 "E.164") format (e.g., +16175551212). SIP addresses are formatted as `sip:name@company.com`. Client identifiers are formatted `client:name`. TwiML App identifiers are formatted `app:<APP_SID>`. [Custom parameters](/docs/voice/api/conference-participant-resource#custom-parameters "Custom parameters") may also be specified.

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `status_callback_method` to send status information to your application.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `status_callback`. Can be: `GET` and `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

statusCallbackEventarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The conference state changes that should generate a call to `status_callback`. Can be: `initiated`, `ringing`, `answered`, and `completed`. Separate multiple values with a space. The default value is `completed`.

* * *

labelstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A label for this participant. If one is supplied, it may subsequently be used to fetch, update or delete the participant.

* * *

timeoutinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of seconds that we should allow the phone to ring before assuming there is no answer. Can be an integer between `5` and `600`, inclusive. The default value is `60`. We always add a 5-second timeout buffer to outgoing calls, so value of 10 would result in an actual timeout that was closer to 15 seconds.

* * *

recordboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to record the participant and their conferences, including the time between conferences. Can be `true` or `false` and the default is `false`.

* * *

mutedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the agent is muted in the conference. Can be `true` or `false` and the default is `false`.

* * *

beepstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to play a notification beep to the conference when the participant joins. Can be: `true`, `false`, `onEnter`, or `onExit`. The default value is `true`.

* * *

startConferenceOnEnterboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to start the conference when the participant joins, if it has not already started. Can be: `true` or `false` and the default is `true`. If `false` and the conference has not started, the participant is muted and hears background music until another participant starts the conference.

* * *

endConferenceOnExitboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to end the conference when the participant leaves. Can be: `true` or `false` and defaults to `false`.

* * *

waitUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that Twilio calls using the `wait_method` before the conference has started. The URL may return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold music. If you do not want anything to play while waiting for the conference to start, specify an empty string by setting `wait_url` to `''`. For more details on the allowable verbs within the `waitUrl`, see the `waitUrl` attribute in the [<Conference> TwiML instruction](/docs/voice/twiml/conference#attributes-waiturl).

* * *

waitMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file.

Possible values:

`GET``POST`

* * *

earlyMediaboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. Can be: `true` or `false` and defaults to `true`.

* * *

maxParticipantsinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The maximum number of participants in the conference. Can be a positive integer from `2` to `250`. The default value is `250`.

* * *

conferenceRecordstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to record the conference the participant is joining. Can be: `true`, `false`, `record-from-start`, and `do-not-record`. The default value is `false`.

* * *

conferenceTrimstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to trim leading and trailing silence from the conference recording. Can be: `trim-silence` or `do-not-trim` and defaults to `trim-silence`.

* * *

conferenceStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `conference_status_callback_method` when the conference events in `conference_status_callback_event` occur. Only the value set by the first participant to join the conference is used. Subsequent `conference_status_callback` values are ignored.

* * *

conferenceStatusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `conference_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

conferenceStatusCallbackEventarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The conference state changes that should generate a call to `conference_status_callback`. Can be: `start`, `end`, `join`, `leave`, `mute`, `hold`, `modify`, `speaker`, and `announcement`. Separate multiple values with a space. Defaults to `start end`.

* * *

recordingChannelsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The recording channels for the final recording. Can be: `mono` or `dual` and the default is `mono`.

* * *

recordingStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call using the `recording_status_callback_method` when the recording status changes.

* * *

recordingStatusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when we call `recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

sipAuthUsernamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SIP username used for authentication.

* * *

sipAuthPasswordstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SIP password for authentication.

* * *

regionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [region(link takes you to an external page)](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls "region") where we should mix the recorded audio. Can be:`us1`, `us2`, `ie1`, `de1`, `sg1`, `br1`, `au1`, or `jp1`.

* * *

conferenceRecordingStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `conference_recording_status_callback_method` when the conference recording is available.

* * *

conferenceRecordingStatusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `conference_recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

recordingStatusCallbackEventarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The recording state changes that should generate a call to `recording_status_callback`. Can be: `started`, `in-progress`, `paused`, `resumed`, `stopped`, `completed`, `failed`, and `absent`. Separate multiple values with a space, ex: `'in-progress completed failed'`.

* * *

conferenceRecordingStatusCallbackEventarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The conference recording state changes that generate a call to `conference_recording_status_callback`. Can be: `in-progress`, `completed`, `failed`, and `absent`. Separate multiple values with a space, ex: `'in-progress completed failed'`

* * *

coachingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined.

* * *

callSidToCoachSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

jitterBufferSizestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Jitter buffer size for the connecting participant. Twilio will use this setting to apply Jitter Buffer before participant's audio is mixed into the conference. Can be: `off`, `small`, `medium`, and `large`. Default to `large`.

* * *

byocSID<BY>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that `byoc` is only meaningful when `to` is a phone number; it will otherwise be ignored. (Beta)

Pattern: `^BY[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callerIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](/docs/glossary/what-e164 "E.164") format (e.g., +16175551212). Client identifiers are formatted `client:name`. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](/docs/voice/api/outgoing-caller-ids "outgoing caller id") for your account. If the `to` parameter is a phone number, `callerId` must also be a phone number. If `to` is sip address, this value of `callerId` should be a username portion to be used to populate the From header that is passed to the SIP endpoint.

* * *

callReasonstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party's phone. (Branded Calls Beta)

* * *

recordingTrackstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is sent from Twilio. `both` records the audio that is received and sent by Twilio.

* * *

timeLimitinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The maximum duration of the call in seconds. Constraints depend on account and configuration.

* * *

machineDetectionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to detect if a human, answering machine, or fax has picked up the call. Can be: `Enable` or `DetectMessageEnd`. Use `Enable` if you would like us to return `AnsweredBy` as soon as the called party is identified. Use `DetectMessageEnd`, if you would like to leave a message on an answering machine. For more information, see [Answering Machine Detection](/docs/voice/answering-machine-detection "Answering Machine Detection").

* * *

machineDetectionTimeoutinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of seconds that we should attempt to detect an answering machine before timing out and sending a voice request with `AnsweredBy` of `unknown`. The default timeout is 30 seconds.

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

amdStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call using the `amd_status_callback_method` to notify customer application whether the call was answered by human, machine or fax.

* * *

amdStatusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when calling the `amd_status_callback` URL. Can be: `GET` or `POST` and the default is `POST`.

Possible values:

`GET``POST`

* * *

trimstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to trim any leading and trailing silence from the participant recording. Can be: `trim-silence` or `do-not-trim` and the default is `trim-silence`.

* * *

callTokenstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A token string needed to invoke a forwarded call. A call_token is generated when an incoming call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the original incoming call.

* * *

clientNotificationUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should use to deliver `push call notification`.

* * *

callerDisplayNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name that populates the display name in the From header. Must be between 2 and 255 characters. Only applicable for calls to sip address.

Select from available examples

Copy code block


    {


      "From": "+17736774757",


      "To": "+14157663747",


      "Label": "customer",


      "EarlyMedia": true,


      "Beep": "onEnter",


      "Muted": false,


      "StatusCallback": "https://myapp.com/events",


      "StatusCallbackMethod": "POST",


      "StatusCallbackEvent": "ringing",


      "Record": true,


      "Trim": "do-not-trim",


      "TimeLimit": 3600,


      "CallToken": "call-token-string",


      "MachineDetection": "enable",


      "MachineDetectionTimeout": 15,


      "MachineDetectionSpeechThreshold": 3000,


      "MachineDetectionSpeechEndThreshold": 3000,


      "MachineDetectionSilenceTimeout": 3000,


      "AmdStatusCallback": "http://statuscallback.com",


      "AmdStatusCallbackMethod": "POST",


      "MachineDetectionEngine": "Lumenvox",


      "MachineDetectionMinWordLength": 100,


      "MachineDetectionMaxWordLength": 5000,


      "MachineDetectionWordsSilence": 50,


      "MachineDetectionMaxNumOfWords": 5,


      "MachineDetectionSilenceThreshold": 256,


      "ClientNotificationUrl": "https://clientnotification.com",


      "CallerDisplayName": "John Doe"


    }

Create a Participant for an active ConferenceLink to code sample: Create a Participant for an active Conference

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

    async function createParticipant() {


    11

      const participant = await client


    12

        .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .participants.create({


    14

          beep: "onEnter",


    15

          earlyMedia: true,


    16

          from: "+15017122661",


    17

          label: "customer",


    18

          record: true,


    19

          statusCallback: "https://myapp.com/events",


    20

          statusCallbackEvent: ["ringing"],


    21

          to: "+15558675310",


    22

        });


    23




    24

      console.log(participant.accountSid);


    25

    }


    26




    27

    createParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "label": "customer",


    5

      "conference_sid": "CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    6

      "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",


    7

      "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",


    8

      "end_conference_on_exit": false,


    9

      "muted": false,


    10

      "hold": false,


    11

      "status": "queued",


    12

      "start_conference_on_enter": true,


    13

      "coaching": false,


    14

      "call_sid_to_coach": null,


    15

      "queue_time": "1000",


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    17

    }

### Custom Parameters

custom-parameters page anchor

Positive FeedbackNegative Feedback

(warning)

## Warning

Only applies to Twilio Voice Client IDs, SIP endpoints, or TwiML applications.

Custom parameters can be passed to the specified Client ID, SIP endpoint, or TwiML application in the `to` field using query string notation. For example: `client:alice?mycustomparam1=foo&mycustomparam2=bar`.

* * *

## Retrieve a Participant

retrieve-a-participant page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json`

Returns a Participant from an active Conference, specified by the Conference SID and the Participant's [Call SID(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/223180488-What-is-a-Call-SID- "Call SID") or label.

(warning)

## Warning

The Participant subresource only manages _active participants of in-progress Conferences_.

If you want to get a list of all Participants over the course of a Conference, use the Conference's `statusCallback` [to receive webhooks for each participant joining the conference](/docs/voice/twiml/conference "to receive webhooks for each participant joining the conference") and store the details in your application.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Participant resource to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conferenceSidSID<CF>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the conference with the participant to fetch.

Pattern: `^CF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [Call](/docs/voice/api/call-resource "Call") SID or label of the participant to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.

Retrieve a ParticipantLink to code sample: Retrieve a Participant

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

    async function fetchParticipant() {


    11

      const participant = await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants("CallSid")


    14

        .fetch();


    15




    16

      console.log(participant.accountSid);


    17

    }


    18




    19

    fetchParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CallSid",


    4

      "label": null,


    5

      "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",


    7

      "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",


    8

      "end_conference_on_exit": false,


    9

      "muted": false,


    10

      "hold": false,


    11

      "status": "connected",


    12

      "start_conference_on_enter": true,


    13

      "coaching": true,


    14

      "call_sid_to_coach": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    15

      "queue_time": null,


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    17

    }

Retrieve a Participant by labelLink to code sample: Retrieve a Participant by label

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

    async function fetchParticipant() {


    11

      const participant = await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants("customer")


    14

        .fetch();


    15




    16

      console.log(participant.label);


    17

    }


    18




    19

    fetchParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "customer",


    4

      "label": "customer",


    5

      "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",


    7

      "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",


    8

      "end_conference_on_exit": false,


    9

      "muted": false,


    10

      "hold": false,


    11

      "status": "connected",


    12

      "start_conference_on_enter": true,


    13

      "coaching": true,


    14

      "call_sid_to_coach": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    15

      "queue_time": null,


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    17

    }

* * *

## Retrieve a list of Participants

retrieve-a-list-of-participants page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json`

Returns the list of active Participants in the Conference identified by `ConferenceSid`.

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Participant resources to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conferenceSidSID<CF>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the conference with the participants to read.

Pattern: `^CF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

mutedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to return only participants that are muted. Can be: `true` or `false`.

* * *

holdboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to return only participants that are on hold. Can be: `true` or `false`.

* * *

coachingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to return only participants who are coaching another call. Can be: `true` or `false`.

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

Retrieve a list of ParticipantsLink to code sample: Retrieve a list of Participants

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

    async function listParticipant() {


    11

      const participants = await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants.list({


    14

          muted: true,


    15

          limit: 20,


    16

        });


    17




    18

      participants.forEach((p) => console.log(p.accountSid));


    19

    }


    20




    21

    listParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "participants": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

          "label": null,


    7

          "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

          "date_created": "Sat, 19 Feb 2011 21:07:19 +0000",


    9

          "date_updated": "Sat, 19 Feb 2011 21:07:19 +0000",


    10

          "end_conference_on_exit": false,


    11

          "muted": true,


    12

          "hold": false,


    13

          "status": "connected",


    14

          "start_conference_on_enter": true,


    15

          "coaching": true,


    16

          "call_sid_to_coach": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    17

          "queue_time": null,


    18

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    19

        },


    20

        {


    21

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "call_sid": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    23

          "label": null,


    24

          "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    25

          "date_created": "Sat, 19 Feb 2011 21:07:19 +0000",


    26

          "date_updated": "Sat, 19 Feb 2011 21:07:19 +0000",


    27

          "end_conference_on_exit": false,


    28

          "muted": true,


    29

          "hold": false,


    30

          "status": "connected",


    31

          "start_conference_on_enter": true,


    32

          "coaching": false,


    33

          "call_sid_to_coach": null,


    34

          "queue_time": null,


    35

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json"


    36

        }


    37

      ],


    38

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=0",


    39

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=1&PageToken=PACPbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    40

      "previous_page_uri": null,


    41

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json?Muted=true&PageSize=2&Page=0",


    42

      "page": 0,


    43

      "page_size": 2,


    44

      "start": 0,


    45

      "end": 1


    46

    }

* * *

## Update a Participant

update-a-participant page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json`

Updates the status of a Participant in an active Conference.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Participant resources to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conferenceSidSID<CF>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the conference with the participant to update.

Pattern: `^CF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [Call](/docs/voice/api/call-resource "Call") SID or label of the participant to update. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

mutedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the participant should be muted. Can be `true` or `false`. `true` will mute the participant, and `false` will un-mute them. Anything value other than `true` or `false` is interpreted as `false`.

* * *

holdboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the participant should be on hold. Can be: `true` or `false`. `true` puts the participant on hold, and `false` lets them rejoin the conference.

* * *

holdUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using the `hold_method` for music that plays when the participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.

* * *

holdMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `hold_url`. Can be: `GET` or `POST` and the default is `GET`.

Possible values:

`GET``POST`

* * *

announceUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using the `announce_method` for an announcement to the participant. The URL may return an MP3 file, a WAV file, or a TwiML document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.

* * *

announceMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `announce_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

waitUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that Twilio calls using the `wait_method` before the conference has started. The URL may return an MP3 file, a WAV file, or a TwiML document. The default value is the URL of our standard hold music. If you do not want anything to play while waiting for the conference to start, specify an empty string by setting `wait_url` to `''`. For more details on the allowable verbs within the `waitUrl`, see the `waitUrl` attribute in the [<Conference> TwiML instruction](/docs/voice/twiml/conference#attributes-waiturl).

* * *

waitMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file.

Possible values:

`GET``POST`

* * *

beepOnExitboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to play a notification beep to the conference when the participant exits. Can be: `true` or `false`.

* * *

endConferenceOnExitboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to end the conference when the participant leaves. Can be: `true` or `false` and defaults to `false`.

* * *

coachingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined.

* * *

callSidToCoachSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Select from available examples

Copy code block


    {


      "Muted": "true"


    }

Update a Participant: Mute a participantLink to code sample: Update a Participant: Mute a participant

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

    async function updateParticipant() {


    11

      const participant = await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants("CallSid")


    14

        .update({ muted: true });


    15




    16

      console.log(participant.accountSid);


    17

    }


    18




    19

    updateParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CallSid",


    4

      "label": null,


    5

      "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",


    7

      "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",


    8

      "end_conference_on_exit": false,


    9

      "muted": true,


    10

      "hold": false,


    11

      "status": "connected",


    12

      "start_conference_on_enter": true,


    13

      "coaching": false,


    14

      "call_sid_to_coach": null,


    15

      "queue_time": null,


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    17

    }

Update a Participant: Mute a participant by labelLink to code sample: Update a Participant: Mute a participant by label

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

    async function updateParticipant() {


    11

      const participant = await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants("customer")


    14

        .update({ muted: true });


    15




    16

      console.log(participant.label);


    17

    }


    18




    19

    updateParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "customer",


    4

      "label": "customer",


    5

      "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",


    7

      "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",


    8

      "end_conference_on_exit": false,


    9

      "muted": true,


    10

      "hold": false,


    11

      "status": "connected",


    12

      "start_conference_on_enter": true,


    13

      "coaching": false,


    14

      "call_sid_to_coach": null,


    15

      "queue_time": null,


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    17

    }

Place a participant on hold with musicLink to code sample: Place a participant on hold with music

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

    async function updateParticipant() {


    11

      const participant = await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants("CallSid")


    14

        .update({


    15

          hold: true,


    16

          holdUrl: "http://www.myapp.com/hold_music",


    17

        });


    18




    19

      console.log(participant.accountSid);


    20

    }


    21




    22

    updateParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CallSid",


    4

      "label": null,


    5

      "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",


    7

      "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",


    8

      "end_conference_on_exit": false,


    9

      "muted": false,


    10

      "hold": true,


    11

      "status": "connected",


    12

      "start_conference_on_enter": true,


    13

      "coaching": false,


    14

      "call_sid_to_coach": null,


    15

      "queue_time": null,


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    17

    }

Update a Participant: Make an announcement to the participantLink to code sample: Update a Participant: Make an announcement to the participant

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

    async function updateParticipant() {


    11

      const participant = await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants("CallSid")


    14

        .update({ announceUrl: "http://www.myapp.com/announce" });


    15




    16

      console.log(participant.accountSid);


    17

    }


    18




    19

    updateParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CallSid",


    4

      "label": null,


    5

      "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "date_created": "Fri, 18 Feb 2011 21:07:19 +0000",


    7

      "date_updated": "Fri, 18 Feb 2011 21:07:19 +0000",


    8

      "end_conference_on_exit": false,


    9

      "muted": false,


    10

      "hold": false,


    11

      "status": "connected",


    12

      "start_conference_on_enter": true,


    13

      "coaching": false,


    14

      "call_sid_to_coach": null,


    15

      "queue_time": null,


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    17

    }

* * *

## Delete a Participant

delete-a-participant page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json`

Deletes the Participant subresource to remove the participant from the conference. Returns HTTP 204 (No Content) with no body if the participant was successfully removed from the conference.

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Participant resources to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conferenceSidSID<CF>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the conference with the participants to delete.

Pattern: `^CF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [Call](/docs/voice/api/call-resource "Call") SID or label of the participant to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.

Delete a ParticipantLink to code sample: Delete a Participant

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

    async function deleteParticipant() {


    11

      await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants("CallSid")


    14

        .remove();


    15

    }


    16




    17

    deleteParticipant();

Delete a Participant by labelLink to code sample: Delete a Participant by label

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

    async function deleteParticipant() {


    11

      await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .participants("customer")


    14

        .remove();


    15

    }


    16




    17

    deleteParticipant();

* * *

## Tips and best practices

tips-and-best-practices page anchor

Positive FeedbackNegative Feedback

  * Long audio files for conference announcements delay playback. For example, a 25-minute file can take about 13–15 seconds to begin after you send the API request.
  * Conference announcements that are 30 minutes or longer can trigger a request timeout and cause the announcement to fail. When this happens, the conference and all calls stay connected, but participants hear "An application error has occurred." The 30-minute limit is approximate. Factors such as file size, HTTP method, and your server's processing or response time can also cause timeouts.
  * For announcements longer than 30 minutes, divide the audio into shorter segments and play them sequentially.


* * *

## What's next?

whats-next page anchor

Positive FeedbackNegative Feedback

Explore [Voice Insights](/docs/voice/voice-insights "Voice Insights") with its [Conference Insights Event Stream](/docs/voice/voice-insights/event-streams/conference-insights-event "Conference Insights Event Stream") and [Conference Insights REST API](/docs/voice/voice-insights/api/conference "Conference Insights REST API") which allow you to see conference parameters, investigate participant event timelines, and understand detected quality issues.