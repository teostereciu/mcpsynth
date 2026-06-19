# Transcriptions resource

*Source: https://www.twilio.com/docs/voice/api/recording-transcription*

---

# Transcriptions resource

Positive FeedbackNegative Feedback

* * *

A Transcription resource represents the transcribed text and metadata from a transcribed recording of a voice call.

The transcription text comes from converting an audio recording to readable text. To generate transcriptions from call recordings, use the [TwiML `<Record>` verb](/docs/voice/twiml/record) and set `transcribe="true"`.

(information)

## PCI compliance

Call recordings aren't Payment Card Industry (PCI) compliant by default. To use Voice Recordings in a [PCI workflow](/docs/voice/pci-workflows "PCI workflow"), [enable PCI Mode in the Twilio Console(link takes you to an external page)](https://www.twilio.com/console/voice/settings "enable PCI Mode in the Twilio Console").

To transcribe voice recordings, use the <Transcription> TwiML noun. Native and Marketplace transcriptions aren't available when PCI Mode is enabled.

(warning)

## Warning

If you request recording transcription, your account incurs additional charges. Transcription is a paid feature. Twilio only transcribes recordings initiated with the TwiML `<Record>` verb and that have a duration no longer than two minutes in length.
To learn about pricing, see the [transcriptions pricing page(link takes you to an external page)](https://www.twilio.com/en-us/voice/pricing/us#extras "transcriptions pricing page").

* * *

## Transcriptions properties

transcriptions-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Transcription resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to create the transcription.

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

durationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The duration of the transcribed audio in seconds.

* * *

pricenumber

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The charge for the transcript in the currency associated with the account. This value is populated after the transcript is complete so it may not be available immediately.

* * *

priceUnitstring<currency>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The currency in which `price` is measured, in [ISO 4127(link takes you to an external page)](https://www.iso.org/iso/home/standards/currency_codes.htm "ISO 4127") format (e.g. `usd`, `eur`, `jpy`).

* * *

recordingSidSID<RE>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Recording](/docs/voice/api/recording "Recording") from which the transcription was created.

Pattern: `^RE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<TR>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that that we created to identify the Transcription resource.

Pattern: `^TR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the transcription. Can be: `in-progress`, `completed`, `failed`.

Possible values:

`in-progress``completed``failed`

* * *

transcriptionTextstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The text content of the transcription.

* * *

typestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The transcription type. Can only be: `fast`.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

## Retrieve a Transcription

retrieve-a-transcription page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Transcriptions/{Sid}.json`

Returns the JSON metadata for the Transcription.

  * The Transcriptions resource doesn't support CSV and HTML formatted responses.
Requests made for CSV and HTML files return an HTTP `404` status code.

  * To retrieve only the transcription text, append "`.txt`" to the Transcriptions resource's URI:

Copy code block

        /2010-04-01/Accounts/{AccountSid}/Transcriptions/{TranscriptionSid}.txt


### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Transcription resource to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<TR>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Transcription resource to fetch.

Pattern: `^TR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve a TranscriptionLink to code sample: Retrieve a Transcription

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

    async function fetchTranscription() {


    11

      const transcription = await client


    12

        .transcriptions("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .fetch();


    14




    15

      console.log(transcription.accountSid);


    16

    }


    17




    18

    fetchTranscription();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "api_version": "2008-08-01",


    4

      "date_created": "Sun, 13 Feb 2011 02:12:08 +0000",


    5

      "date_updated": "Sun, 13 Feb 2011 02:30:01 +0000",


    6

      "duration": "1",


    7

      "price": "-0.05000",


    8

      "price_unit": "USD",


    9

      "recording_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "sid": "TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    11

      "status": "failed",


    12

      "transcription_text": "(blank)",


    13

      "type": "fast",


    14

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    15

    }

* * *

## Retrieve a list of Transcriptions

retrieve-a-list-of-transcriptions page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Transcriptions.json`

Returns a list of Transcriptions generated from all recordings in an account.

The response contains a [paginated list](/docs/usage/twilios-response#pagination "paginated list").

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Transcription resources to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

Retrieve a list of TranscriptionsLink to code sample: Retrieve a list of Transcriptions

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

    async function listTranscription() {


    11

      const transcriptions = await client.transcriptions.list({ limit: 20 });


    12




    13

      transcriptions.forEach((t) => console.log(t.accountSid));


    14

    }


    15




    16

    listTranscription();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "start": 0,


    9

      "transcriptions": [


    10

        {


    11

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    12

          "api_version": "2008-08-01",


    13

          "date_created": "Thu, 25 Aug 2011 20:59:45 +0000",


    14

          "date_updated": "Thu, 25 Aug 2011 20:59:45 +0000",


    15

          "duration": "10",


    16

          "price": "0.00000",


    17

          "price_unit": "USD",


    18

          "recording_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    19

          "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

          "status": "completed",


    21

          "transcription_text": null,


    22

          "type": "fast",


    23

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    24

        }


    25

      ],


    26

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json?PageSize=1&Page=0"


    27

    }

To access a full list of transcriptions from a given Recording, pass the `RecordingSid` to the [Recording resource](/docs/voice/api/recording "Recording resource"):

Copy code block


    /2010-04-01/Accounts/{YourAccountSid}/Recordings/{RecordingSid}/Transcriptions.json

To fetch Transcriptions from a Recording, write a cURL command that resembles the following:

Copy code block


    1

    curl -G https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings/REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Transcriptions.json \


    2

         -u 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:your_auth_token'

  * To return an XML-formatted response, change the end of this URI from `.json` to `.xml`.

  * The Recording Transcription resource doesn't support CSV and HTML formatted responses.
Requests made for CSV and HTML files return an HTTP `404` status code.

  * To return only the transcription text, append "`.txt`" to the Transcription resource's URI:

Copy code block

        1

        curl -G https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings/REXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Transcriptions.txt \


        2

          -u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN


* * *

## Delete a Transcription

delete-a-transcription page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Transcriptions/{Sid}.json`

Delete a transcription from your account.

If the request succeeds, Twilio returns HTTP `204 (No Content)` with no body.

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Transcription resources to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<TR>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Transcription resource to delete.

Pattern: `^TR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a TranscriptionLink to code sample: Delete a Transcription

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

    async function deleteTranscription() {


    11

      await client.transcriptions("TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").remove();


    12

    }


    13




    14

    deleteTranscription();