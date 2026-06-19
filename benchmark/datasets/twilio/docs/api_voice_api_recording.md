# Recordings resource

*Source: https://www.twilio.com/docs/voice/api/recording*

---

# Recordings resource

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

For Customers building HIPAA-compliant workflows with [Recordings](/docs/voice/api/recording "Recordings"), we require customers to enforce at least HTTP Authentication. To learn more about building for HIPAA compliance, please visit the latest requirements [here(link takes you to an external page)](https://docs-resources.prod.twilio.com/documents/architecting-for-HIPAA.pdf "here").

(information)

## PCI compliance

Call recordings aren't Payment Card Industry (PCI) compliant by default. To use Voice Recordings in a [PCI workflow](/docs/voice/pci-workflows "PCI workflow"), [enable PCI Mode in the Twilio Console(link takes you to an external page)](https://www.twilio.com/console/voice/settings "enable PCI Mode in the Twilio Console").

To transcribe voice recordings, use the <Transcription> TwiML noun. Native and Marketplace transcriptions aren't available when PCI Mode is enabled.

A Recording resource represents the recording associated with a voice call, conference, or SIP Trunk. Using the Recordings resource, you can fetch, start, stop, pause, resume, and delete voice recordings.

You can start a recording for a call, conference, or trunk in any of the following ways:

  1. [<Record> in TwiML](/docs/voice/twiml/record "<Record> in TwiML")
  2. [<Dial record> in TwiML](/docs/voice/twiml/dial#record "<Dial record> in TwiML")
  3. [<Conference record> in TwiML](/docs/voice/twiml/conference#record "<Conference record> in TwiML")
  4. [`Record=true` in an outbound call via the REST API](/docs/voice/tutorials/how-to-make-outbound-phone-calls#record-your-call)
  5. [Enable recording on an elastic SIP Trunk in the Twilio Console(link takes you to an external page)](https://www.twilio.com/console/sip-trunking/trunks "Enable recording on an elastic SIP Trunk in the Twilio Console")
  6. [Post to Recording resource of an in-progress Call SID](/docs/voice/api/recording#create-a-recording "Post to Recording resource of an in-progress Call SID")
  7. [`<Start><Recording>` in TwiML](/docs/voice/twiml/recording)


After you start a recording, you can [pause, resume, or stop it](/docs/voice/api/recording#update-a-recording "pause, resume, or stop it").

* * *

## Recordings properties

recordings-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Recording resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used during the recording.

* * *

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Recording resource is associated with. This will always refer to the parent leg of a two-leg call.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conferenceSidSID<CF>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Conference SID that identifies the conference associated with the recording, if a conference recording.

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

startTimestring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The start time of the recording in GMT and in [RFC 2822(link takes you to an external page)](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822 "RFC 2822") format.

* * *

durationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The length of the recording in seconds.

* * *

sidSID<RE>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that that we created to identify the Recording resource.

Pattern: `^RE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

pricestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The one-time cost of creating the recording in the `price_unit` currency.

* * *

priceUnitstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The currency used in the `price` property. Example: `USD`.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the recording. Can be: `processing`, `completed`, `absent` or `deleted`. For information about more detailed statuses on in-progress recordings, check out how to [Update a Recording Resource](/docs/voice/api/recording#update-a-recording-resource "Update a Recording Resource").

Possible values:

`in-progress``paused``stopped``processing``completed``absent``deleted`

* * *

channelsinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of channels in the recording resource. For information on specifying the number of channels in the downloaded recording file, check out [Fetch a Recording’s media file](/docs/voice/api/recording#download-dual-channel-media-file "Fetch a Recording’s media file").

* * *

sourceenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How the recording was created. Can be: `DialVerb`, `Conference`, `OutboundAPI`, `Trunking`, `RecordVerb`, `StartCallRecordingAPI`, and `StartConferenceRecordingAPI`.

Possible values:

`DialVerb``Conference``OutboundAPI``Trunking``RecordVerb``StartCallRecordingAPI``StartConferenceRecordingAPI`

* * *

errorCodeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The error code that describes why the recording is `absent`. The error code is described in our [Error Dictionary](/docs/api/errors "Error Dictionary"). This value is null if the recording `status` is not `absent`.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

encryptionDetails

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How to decrypt the recording if it was encrypted using [Call Recording Encryption](/docs/voice/tutorials/voice-recording-encryption "Call Recording Encryption") feature.

* * *

subresourceUrisobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of related resources identified by their relative URIs.

* * *

mediaUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of the media file associated with this recording resource. When stored externally, this is the full URL location of the media file.

* * *

## Create a Recording

create-a-recording page anchor

Positive FeedbackNegative Feedback

Copy code block


    POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallsSid}/Recordings.json

To start a recording on a live call, make a `POST` request to the Recordings subresource of an in-progress Call.

A recording can be as long as the call.

(warning)

## Legal implications of call recording

If you choose to record voice or video calls, you need to comply with certain laws and regulations, including those regarding obtaining consent to record (such as California's Invasion of Privacy Act and similar laws in other jurisdictions). Additional information on the legal implications of call recording can be found [in the "Legal Considerations with Recording Voice and Video Communications" Help Center article(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/360011522553-Legal-Considerations-with-Recording-Voice-and-Video-Communications "in the "Legal Considerations with Recording Voice and Video Communications" Help Center article").

_Notice_ : Twilio recommends that you consult with your legal counsel to make sure that you are complying with all applicable laws in connection with communications you record or store using Twilio.

### Optional parameters

optional-parameters page anchor

Positive FeedbackNegative Feedback

The following optional parameters are available for you to `POST` when starting a recording on a live call:

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

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") to associate the resource with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

recordingStatusCallbackEventarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The recording status events on which we should call the `recording_status_callback` URL. Can be: `in-progress`, `completed` and `absent` and the default is `completed`. Separate multiple event values with a space.

* * *

recordingStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `recording_status_callback_method` on each recording event specified in `recording_status_callback_event`. For more information, see [RecordingStatusCallback parameters](/docs/voice/api/recording#recordingstatuscallback "RecordingStatusCallback parameters").

* * *

recordingStatusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `recording_status_callback`. Can be: `GET` or `POST` and the default is `POST`.

Possible values:

`GET``POST`

* * *

trimstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to trim any leading and trailing silence in the recording. Can be: `trim-silence` or `do-not-trim` and the default is `do-not-trim`. `trim-silence` trims the silence from the beginning and end of the recording and `do-not-trim` does not.

* * *

recordingChannelsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of channels used in the recording. Can be: `mono` or `dual` and the default is `mono`. `mono` records all parties of the call into one channel. `dual` records each party of a 2-party call into separate channels.

* * *

recordingTrackstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is generated from Twilio. `both` records the audio that is received and generated by Twilio.

Select from available examples

Copy code block


    {


      "RecordingStatusCallbackEvent": [


        "in-progress completed failed"


      ],


      "RecordingStatusCallback": "https://example.com",


      "RecordingStatusCallbackMethod": "GET",


      "Trim": "do-not-trim",


      "RecordingChannels": "dual",


      "RecordingTrack": "both",


      "PlayBeep": true,


      "Transcribe": true,


      "TranscriptionConfiguration": "JVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

### RecordingStatusCallback

recordingstatuscallback page anchor

Positive FeedbackNegative Feedback

Twilio will pass the following parameters with its request to your `RecordingStatusCallback` URL:

Parameter| Description
---|---
AccountSid| The unique identifier of the Account responsible for this recording.
CallSid| A unique identifier for the call associated with the recording.
RecordingSid| The unique identifier for the recording.
RecordingUrl| The URL of the recorded audio.
RecordingStatus| The status of the recording. Possible values are: `in-progress`, `completed`, `absent`.
RecordingDuration| The length of the recording, in seconds (only provided when `RecordingStatus` is `completed`).
RecordingChannels| The number of channels in the final recording file as an integer. Possible values are `1`, `2`.
RecordingStartTime| The timestamp of when the recording started.
RecordingSource| The initiation method used to create this recording. For recordings initiated with this API, the value will be `StartCallRecordingAPI`.
RecordingTrack| The audio track recorded. Possible values are `inbound`, `outbound` or `both`.

Create a Recording on a live callLink to code sample: Create a Recording on a live call

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

    async function createCallRecording() {


    11

      const recording = await client


    12

        .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .recordings.create();


    14




    15

      console.log(recording.accountSid);


    16

    }


    17




    18

    createCallRecording();

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

      "call_sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "conference_sid": null,


    6

      "channels": 2,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:34 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": null,


    11

      "price_unit": null,


    12

      "duration": null,


    13

      "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "source": "StartCallRecordingAPI",


    15

      "status": "in-progress",


    16

      "error_code": null,


    17

      "encryption_details": null,


    18

      "track": "both",


    19

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    20

    }

Create a dual-channel Recording with RecordingStatusCallbackLink to code sample: Create a dual-channel Recording with RecordingStatusCallback

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

    async function createCallRecording() {


    11

      const recording = await client


    12

        .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .recordings.create({


    14

          recordingChannels: "dual",


    15

          recordingStatusCallback: "https://myapp.com/recording-events",


    16

          recordingStatusCallbackEvent: ["in-progress completed"],


    17

        });


    18




    19

      console.log(recording.accountSid);


    20

    }


    21




    22

    createCallRecording();

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

      "call_sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "conference_sid": null,


    6

      "channels": 2,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:34 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": null,


    11

      "price_unit": null,


    12

      "duration": null,


    13

      "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "source": "StartCallRecordingAPI",


    15

      "status": "in-progress",


    16

      "error_code": null,


    17

      "encryption_details": null,


    18

      "track": "both",


    19

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    20

    }

* * *

## Retrieve a Recording

retrieve-a-recording page anchor

Positive FeedbackNegative Feedback

You can retrieve a Recording's metadata or you can retrieve a WAV or MP3 media file of the Recording.

### Retrieve a Recording's metadata

retrieve-a-recordings-metadata page anchor

Positive FeedbackNegative Feedback

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json

A Recording's metadata can be returned in JSON or XML format.

  * For JSON format, append `.json` to the Recording's URI.
  * For XML format, append `.xml` to the Recording's URI.


The table below lists the parameters for fetching a Recording's metadata.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Recording resource to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<RE>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Recording resource to fetch.

Pattern: `^RE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

includeSoftDeletedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.

Retrieve a Recording's metadata in JSON formatLink to code sample: Retrieve a Recording's metadata in JSON format

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

    async function fetchRecording() {


    11

      const recording = await client


    12

        .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .fetch();


    14




    15

      console.log(recording.accountSid);


    16

    }


    17




    18

    fetchRecording();

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

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "channels": 1,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:38 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": "-0.00250",


    11

      "price_unit": "USD",


    12

      "duration": "4",


    13

      "sid": "REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

      "source": "StartConferenceRecordingAPI",


    15

      "status": "completed",


    16

      "error_code": null,


    17

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    18

      "subresource_uris": {


    19

        "add_on_results": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json",


    20

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"


    21

      },


    22

      "encryption_details": {


    23

        "encryption_public_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

        "encryption_cek": "OV4h6zrsxMIW7h0Zfqwfn6TI2GCNl54KALlg8wn8YB8KYZhXt6HlgvBWAmQTlfYVeLWydMiCewY0YkDDT1xmNe5huEo9vjuKBS5OmYK4CZkSx1NVv3XOGrZHpd2Pl/5WJHVhUK//AUO87uh5qnUP2E0KoLh1nyCLeGcEkXU0RfpPn/6nxjof/n6m6OzZOyeIRK4Oed5+rEtjqFDfqT0EVKjs6JAxv+f0DCc1xYRHl2yV8bahUPVKs+bHYdy4PVszFKa76M/Uae4jFA9Lv233JqWcxj+K2UoghuGhAFbV/JQIIswY2CBYI8JlVSifSqNEl9vvsTJ8bkVMm3MKbG2P7Q==",


    25

        "encryption_iv": "8I2hhNIYNTrwxfHk"


    26

      },


    27

      "media_url": "http://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    28

    }

### Retrieve a Recording's media file

retrieve-a-recordings-media-file page anchor

Positive FeedbackNegative Feedback

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.mp3

You can fetch a Recording's media file by appending `.wav` or `.mp3` to the Recording's URI.

It's only possible to fetch a Recording's media file when the Recording's status is `completed` and the media is stored at Twilio.

If the media associated with a Recording resource is not available/was deleted/was uploaded to external storage, the request returns `Not Found`.

(warning)

## Authentication required

Twilio enforces [HTTP Basic Authentication](/docs/glossary/what-is-basic-authentication "HTTP Basic Authentication") for all media URLs. Authenticate using an [API key](/docs/iam/api-keys "API key") as the username and an API key secret as the password. You can also use your Account SID and Auth Token when testing locally.

#### WAV

wav page anchor

If you omit the extension or use `.wav`, Twilio returns a binary WAV file with MIME type `audio/x-wav`. For example:

Copy code block


    1

    GET https://api.twilio.com/2010-04-01/Accounts/ACXXXXX.../Recordings/RE557ce644e5ab84fa21cc21112e22c485


    2

WAV files have a bitrate of 128kbps.

#### MP3

mp3 page anchor

Appending `.mp3` to the URI returns a binary MP3 file with MIME type `audio/mpeg`. For example:

Copy code block


    1

    GET https://api.twilio.com/2010-04-01/Accounts/ACXXXXX.../Recordings/RE557ce644e5ab84fa21cc21112e22c485.mp3


    2

MP3 files have a bitrate of 32kbps.

#### Download dual-channel media file

download-dual-channel-media-file page anchor

Call and Conference Recordings are stored at Twilio in dual-channel format by default.

  * For a two-party Call, the Recording's dual-channel media file contains the audio from each call leg in separate channels.
  * For a Conference, the Recording's dual-channel media file contains the audio of the first participant that joined the Conference in the first channel and all other audio from the Call mixed in the second channel. **Note:** To access this feature, you need to enable Dual-channel Conference Recordings on the Voice Settings page in the [Console(link takes you to an external page)](https://console.twilio.com/ "Console"). Read the [Dual-channel Conference Recordings Changelog entry(link takes you to an external page)](https://www.twilio.com/en-us/changelog/dual-channel-voice-conference-recordings "Dual-channel Conference Recordings Changelog entry") for more information.


When sending the `GET` request to download a Recording's media file, the `RequestedChannels` query parameter can be used to specify whether the media file should be downmixed to a single channel or if the file should be downloaded in its original, dual-channel format.

  * If the `RequestedChannels` query parameter is not specified when requesting the media file for a **two-party Call Recording** , Twilio returns a media file in the format specified when the Recording was created.
  * If the `RequestedChannels` query parameter is not specified when requesting the media file for a **Conference Recording** , Twilio returns a media file in mono-channel format.


(warning)

## Warning

Attempting to download a dual-channel media file when the dual-channel format is not available results in a `400 Bad Request` error. This may happen in the following cases:

  * A Recording created with the `<Record>` verb. All audio from those Recordings are mixed and saved in a mono-channel media file.
  * Older Recordings from two-party Calls or Conferences prior to dual-channel support.


To prevent application errors while managing Recordings, you should implement retry logic when sending a `GET` request for a Recording's media file. If a request for a dual-channel media file fails, retry with a `GET` request for with `RequestedChannels=1`.

**Example: Download MP3 media in dual-channel format**

Append `.mp3?RequestedChannels=2` to your Recording's URL

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/ACXXXXX.../Recordings/RE557ce644e5ab84fa21cc21112e22c485.mp3?RequestedChannels=2

**Example: Download WAV media in dual-channel format**

Append `.wav?RequestedChannels=2` to your Recording's URL

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/ACXXXXX.../Recordings/RE557ce644e5ab84fa21cc21112e22c485.wav?RequestedChannels=2

### Retrieve a Transcription for a Recording

retrieve-a-transcription-for-a-recording page anchor

Positive FeedbackNegative Feedback

Each Recording has a Transcriptions subresource which represents the set of transcriptions generated from the recording (if any):

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions

This will return the set of transcriptions available for the recording identified by `{RecordingSid}`. Learn more about the [Transcriptions resource](/docs/voice/api/recording-transcription "Transcriptions resource").

* * *

## Retrieve a list of Recordings

retrieve-a-list-of-recordings page anchor

Positive FeedbackNegative Feedback

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Recordings.json

This API call returns a list of Recordings, each representing a recording generated during a call or conference for the given account. The list returned includes [paging information](/docs/usage/twilios-response#pagination "paging information").

(warning)

## Warning

The list of Recordings is protected by your account credentials like most parts of this API. You must use HTTP basic auth to access the Recordings resource.

You can also get a list of Recordings from a specific call or conference by including the call or conference SID in your request like so:

Copy code block


    1

    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json


    2

    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json

### Parameters

parameters page anchor

Positive FeedbackNegative Feedback

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Recording resources to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.

* * *

dateCreatedBeforestring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.

* * *

dateCreatedAfterstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.

* * *

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [Call](/docs/voice/api/call-resource "Call") SID of the resources to read.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conferenceSidSID<CF>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Conference SID that identifies the conference associated with the recording to read.

Pattern: `^CF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

includeSoftDeletedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.

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

Examples

Retrieve a list of Recordings for a callLink to code sample: Retrieve a list of Recordings for a call

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

    async function listRecording() {


    11

      const recordings = await client.recordings.list({


    12

        callSid: "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    13

        limit: 20,


    14

      });


    15




    16

      recordings.forEach((r) => console.log(r.accountSid));


    17

    }


    18




    19

    listRecording();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=1&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "recordings": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "channels": 1,


    15

          "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    16

          "date_updated": "Fri, 14 Oct 2016 21:56:38 +0000",


    17

          "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    18

          "price": "0.04",


    19

          "price_unit": "USD",


    20

          "duration": "4",


    21

          "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "source": "StartConferenceRecordingAPI",


    23

          "status": "completed",


    24

          "error_code": null,


    25

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    26

          "subresource_uris": {


    27

            "add_on_results": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json",


    28

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"


    29

          },


    30

          "encryption_details": {


    31

            "encryption_public_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    32

            "encryption_cek": "OV4h6zrsxMIW7h0Zfqwfn6TI2GCNl54KALlg8wn8YB8KYZhXt6HlgvBWAmQTlfYVeLWydMiCewY0YkDDT1xmNe5huEo9vjuKBS5OmYK4CZkSx1NVv3XOGrZHpd2Pl/5WJHVhUK//AUO87uh5qnUP2E0KoLh1nyCLeGcEkXU0RfpPn/6nxjof/n6m6OzZOyeIRK4Oed5+rEtjqFDfqT0EVKjs6JAxv+f0DCc1xYRHl2yV8bahUPVKs+bHYdy4PVszFKa76M/Uae4jFA9Lv233JqWcxj+K2UoghuGhAFbV/JQIIswY2CBYI8JlVSifSqNEl9vvsTJ8bkVMm3MKbG2P7Q==",


    33

            "encryption_iv": "8I2hhNIYNTrwxfHk"


    34

          },


    35

          "media_url": "http://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    36

        }


    37

      ],


    38

      "start": 0,


    39

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=1&Page=0"


    40

    }

Retrieve a list of Recordings for an accountLink to code sample: Retrieve a list of Recordings for an account

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

    async function listRecording() {


    11

      const recordings = await client.recordings.list({ limit: 20 });


    12




    13

      recordings.forEach((r) => console.log(r.accountSid));


    14

    }


    15




    16

    listRecording();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=1&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "recordings": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "channels": 1,


    15

          "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    16

          "date_updated": "Fri, 14 Oct 2016 21:56:38 +0000",


    17

          "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    18

          "price": "0.04",


    19

          "price_unit": "USD",


    20

          "duration": "4",


    21

          "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "source": "StartConferenceRecordingAPI",


    23

          "status": "completed",


    24

          "error_code": null,


    25

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    26

          "subresource_uris": {


    27

            "add_on_results": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json",


    28

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"


    29

          },


    30

          "encryption_details": {


    31

            "encryption_public_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    32

            "encryption_cek": "OV4h6zrsxMIW7h0Zfqwfn6TI2GCNl54KALlg8wn8YB8KYZhXt6HlgvBWAmQTlfYVeLWydMiCewY0YkDDT1xmNe5huEo9vjuKBS5OmYK4CZkSx1NVv3XOGrZHpd2Pl/5WJHVhUK//AUO87uh5qnUP2E0KoLh1nyCLeGcEkXU0RfpPn/6nxjof/n6m6OzZOyeIRK4Oed5+rEtjqFDfqT0EVKjs6JAxv+f0DCc1xYRHl2yV8bahUPVKs+bHYdy4PVszFKa76M/Uae4jFA9Lv233JqWcxj+K2UoghuGhAFbV/JQIIswY2CBYI8JlVSifSqNEl9vvsTJ8bkVMm3MKbG2P7Q==",


    33

            "encryption_iv": "8I2hhNIYNTrwxfHk"


    34

          },


    35

          "media_url": "http://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    36

        }


    37

      ],


    38

      "start": 0,


    39

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=1&Page=0"


    40

    }

Filter Recordings with exact matchLink to code sample: Filter Recordings with exact match

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

    async function listRecording() {


    11

      const recordings = await client.recordings.list({


    12

        dateCreated: new Date("2016-10-18 00:00:00"),


    13

        limit: 20,


    14

      });


    15




    16

      recordings.forEach((r) => console.log(r.accountSid));


    17

    }


    18




    19

    listRecording();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=1&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "recordings": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "channels": 1,


    15

          "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    16

          "date_updated": "Fri, 14 Oct 2016 21:56:38 +0000",


    17

          "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    18

          "price": "0.04",


    19

          "price_unit": "USD",


    20

          "duration": "4",


    21

          "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "source": "StartConferenceRecordingAPI",


    23

          "status": "completed",


    24

          "error_code": null,


    25

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    26

          "subresource_uris": {


    27

            "add_on_results": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json",


    28

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"


    29

          },


    30

          "encryption_details": {


    31

            "encryption_public_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    32

            "encryption_cek": "OV4h6zrsxMIW7h0Zfqwfn6TI2GCNl54KALlg8wn8YB8KYZhXt6HlgvBWAmQTlfYVeLWydMiCewY0YkDDT1xmNe5huEo9vjuKBS5OmYK4CZkSx1NVv3XOGrZHpd2Pl/5WJHVhUK//AUO87uh5qnUP2E0KoLh1nyCLeGcEkXU0RfpPn/6nxjof/n6m6OzZOyeIRK4Oed5+rEtjqFDfqT0EVKjs6JAxv+f0DCc1xYRHl2yV8bahUPVKs+bHYdy4PVszFKa76M/Uae4jFA9Lv233JqWcxj+K2UoghuGhAFbV/JQIIswY2CBYI8JlVSifSqNEl9vvsTJ8bkVMm3MKbG2P7Q==",


    33

            "encryption_iv": "8I2hhNIYNTrwxfHk"


    34

          },


    35

          "media_url": "http://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    36

        }


    37

      ],


    38

      "start": 0,


    39

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=1&Page=0"


    40

    }

Filter Recordings with range matchLink to code sample: Filter Recordings with range match

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

    async function listRecording() {


    11

      const recordings = await client.recordings.list({


    12

        dateCreatedBefore: new Date("2016-10-15 00:00:00"),


    13

        dateCreatedAfter: new Date("2016-10-12 00:00:00"),


    14

        limit: 20,


    15

      });


    16




    17

      recordings.forEach((r) => console.log(r.accountSid));


    18

    }


    19




    20

    listRecording();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=1&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "recordings": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "conference_sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "channels": 1,


    15

          "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    16

          "date_updated": "Fri, 14 Oct 2016 21:56:38 +0000",


    17

          "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    18

          "price": "0.04",


    19

          "price_unit": "USD",


    20

          "duration": "4",


    21

          "sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "source": "StartConferenceRecordingAPI",


    23

          "status": "completed",


    24

          "error_code": null,


    25

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    26

          "subresource_uris": {


    27

            "add_on_results": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json",


    28

            "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json"


    29

          },


    30

          "encryption_details": {


    31

            "encryption_public_key_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    32

            "encryption_cek": "OV4h6zrsxMIW7h0Zfqwfn6TI2GCNl54KALlg8wn8YB8KYZhXt6HlgvBWAmQTlfYVeLWydMiCewY0YkDDT1xmNe5huEo9vjuKBS5OmYK4CZkSx1NVv3XOGrZHpd2Pl/5WJHVhUK//AUO87uh5qnUP2E0KoLh1nyCLeGcEkXU0RfpPn/6nxjof/n6m6OzZOyeIRK4Oed5+rEtjqFDfqT0EVKjs6JAxv+f0DCc1xYRHl2yV8bahUPVKs+bHYdy4PVszFKa76M/Uae4jFA9Lv233JqWcxj+K2UoghuGhAFbV/JQIIswY2CBYI8JlVSifSqNEl9vvsTJ8bkVMm3MKbG2P7Q==",


    33

            "encryption_iv": "8I2hhNIYNTrwxfHk"


    34

          },


    35

          "media_url": "http://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    36

        }


    37

      ],


    38

      "start": 0,


    39

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json?PageSize=1&Page=0"


    40

    }

* * *

## Update a Recording

update-a-recording page anchor

Positive FeedbackNegative Feedback

Copy code block


    1

    POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json


    2

    POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json

An active Call or Conference Recording can be **paused** and **resumed**. Additionally, an active call recording can be **stopped** which will end the recording immediately. (The _stopped_ status isn't supported for conference recordings.)

### Parameters

parameters-2 page anchor

Positive FeedbackNegative Feedback

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Recording resource to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [Call](/docs/voice/api/call-resource "Call") SID of the resource to update.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Recording resource to update.

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

statusenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the recording. Can be: `processing`, `completed` and `absent`. For more detailed statuses on in-progress recordings, check out how to [Update a Recording Resource](/docs/voice/api/recording#update-a-recording-resource "Update a Recording Resource").

Possible values:

`in-progress``paused``stopped``processing``completed``absent`

* * *

pauseBehaviorstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`.

Copy code block


    {


      "Status": "paused",


      "PauseBehavior": "skip",


      "PlayBeep": true


    }

Examples:

(warning)

## Warning

Note in examples below that the API responses for updates to the Recording resource will provide a more detailed inflight 'status' including _**paused**_ , _**in-progress**_ , or _**stopped**_ but a fetch on the Recording resource will only show _**processing**_ or _**completed**_.

Update a Recording: Pause a Call Recording with skip optionLink to code sample: Update a Recording: Pause a Call Recording with skip option

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

    async function updateCallRecording() {


    11

      const recording = await client


    12

        .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .update({


    15

          pauseBehavior: "skip",


    16

          status: "paused",


    17

        });


    18




    19

      console.log(recording.accountSid);


    20

    }


    21




    22

    updateCallRecording();

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

      "call_sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "conference_sid": null,


    6

      "channels": 2,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:36 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": null,


    11

      "price_unit": null,


    12

      "duration": null,


    13

      "sid": "REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

      "source": "StartCallRecordingAPI",


    15

      "status": "paused",


    16

      "error_code": null,


    17

      "encryption_details": null,


    18

      "track": "both",


    19

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    20

    }

Update a Recording: Pause a Conference Recording with skip optionLink to code sample: Update a Recording: Pause a Conference Recording with skip option

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

    async function updateConferenceRecording() {


    11

      const recording = await client


    12

        .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .update({


    15

          pauseBehavior: "skip",


    16

          status: "paused",


    17

        });


    18




    19

      console.log(recording.accountSid);


    20

    }


    21




    22

    updateConferenceRecording();

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

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "conference_sid": "CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    6

      "channels": 1,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:39 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": null,


    11

      "price_unit": null,


    12

      "duration": null,


    13

      "sid": "REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

      "source": "StartConferenceRecordingAPI",


    15

      "status": "paused",


    16

      "error_code": null,


    17

      "encryption_details": null,


    18

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    19

    }

(information)

## Info

In the following two examples, note the use of `Twilio.CURRENT` to reference the currently active recording without requiring an explicit Recording SID.

`Twilio.CURRENT` can be used for _pause_ , _resume_ , or _stop_ actions on calls with only one active recording.

(warning)

## Warning

Note that if your use case has multiple or concurrent recordings for a call or conference, you will need to use the Recording SID to reference the correct one. Using `Twilio.CURRENT` to reference a recording on a resource that has multiple recordings will result in an error that the request failed because there is more than one recording for the given Call.

Update a Recording: Pause a Call Recording with Twilio.CURRENTLink to code sample: Update a Recording: Pause a Call Recording with Twilio.CURRENT

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

    async function updateCallRecording() {


    11

      const recording = await client


    12

        .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .recordings("Twilio.CURRENT")


    14

        .update({ status: "paused" });


    15




    16

      console.log(recording.accountSid);


    17

    }


    18




    19

    updateCallRecording();

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

      "call_sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "conference_sid": null,


    6

      "channels": 2,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:36 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": null,


    11

      "price_unit": null,


    12

      "duration": null,


    13

      "sid": "Twilio.CURRENT",


    14

      "source": "StartCallRecordingAPI",


    15

      "status": "paused",


    16

      "error_code": null,


    17

      "encryption_details": null,


    18

      "track": "both",


    19

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    20

    }

Update a Recording: Pause a Conference Recording with Twilio.CURRENTLink to code sample: Update a Recording: Pause a Conference Recording with Twilio.CURRENT

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

    async function updateConferenceRecording() {


    11

      const recording = await client


    12

        .conferences("CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .recordings("Twilio.CURRENT")


    14

        .update({ status: "paused" });


    15




    16

      console.log(recording.accountSid);


    17

    }


    18




    19

    updateConferenceRecording();

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

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "conference_sid": "CFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    6

      "channels": 1,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:39 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": null,


    11

      "price_unit": null,


    12

      "duration": null,


    13

      "sid": "Twilio.CURRENT",


    14

      "source": "StartConferenceRecordingAPI",


    15

      "status": "paused",


    16

      "error_code": null,


    17

      "encryption_details": null,


    18

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    19

    }

Update a Recording:Resume a Call RecordingLink to code sample: Update a Recording:Resume a Call Recording

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

    async function updateCallRecording() {


    11

      const recording = await client


    12

        .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .update({ status: "in-progress" });


    15




    16

      console.log(recording.accountSid);


    17

    }


    18




    19

    updateCallRecording();

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

      "call_sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "conference_sid": null,


    6

      "channels": 2,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:36 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": null,


    11

      "price_unit": null,


    12

      "duration": null,


    13

      "sid": "REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

      "source": "StartCallRecordingAPI",


    15

      "status": "in-progress",


    16

      "error_code": null,


    17

      "encryption_details": null,


    18

      "track": "both",


    19

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    20

    }

Update a Recording:Stop a Call RecordingLink to code sample: Update a Recording:Stop a Call Recording

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

    async function updateCallRecording() {


    11

      const recording = await client


    12

        .calls("CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .update({ status: "stopped" });


    15




    16

      console.log(recording.accountSid);


    17

    }


    18




    19

    updateCallRecording();

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

      "call_sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "conference_sid": null,


    6

      "channels": 2,


    7

      "date_created": "Fri, 14 Oct 2016 21:56:34 +0000",


    8

      "date_updated": "Fri, 14 Oct 2016 21:56:36 +0000",


    9

      "start_time": "Fri, 14 Oct 2016 21:56:34 +0000",


    10

      "price": null,


    11

      "price_unit": null,


    12

      "duration": null,


    13

      "sid": "REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

      "source": "StartCallRecordingAPI",


    15

      "status": "stopped",


    16

      "error_code": null,


    17

      "encryption_details": null,


    18

      "track": "both",


    19

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    20

    }

* * *

## Delete a Recording

delete-a-recording page anchor

Positive FeedbackNegative Feedback

Copy code block


    DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json

Deletes a recording from your account. Once the recording is deleted:

  * You will no longer be billed for storage of those minutes
  * The recording is set to a status of `deleted`
  * The metadata is _preserved for a period of 40 days_ , during which time the metadata is still visible in the Console and API.
  * The recording media cannot be recovered.


If successful, `DELETE` returns HTTP 204 (No Content) with no body.

Only `completed` recordings can be deleted. Recordings with any other status are not available for deletion.

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Recording resources to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<RE>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Recording resource to delete.

Pattern: `^RE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

(information)

## Info

To delete a large set of Voice Recordings, you can use the bulk deletion capabilities available in the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console/voice/recordings/recording-logs "Twilio Console").

Example:

Delete a RecordingLink to code sample: Delete a Recording

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

    async function deleteRecording() {


    11

      await client.recordings("REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").remove();


    12

    }


    13




    14

    deleteRecording();