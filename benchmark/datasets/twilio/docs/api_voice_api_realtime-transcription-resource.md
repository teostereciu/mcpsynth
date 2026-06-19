# Calls Transcriptions subresource

*Source: https://www.twilio.com/docs/voice/api/realtime-transcription-resource*

---

# Calls Transcriptions subresource

Positive FeedbackNegative Feedback

* * *

(new)

## Legal notice

Real-Time Transcriptions, including the `<Transcriptions>` TwiML noun and API, use artificial intelligence or machine learning technologies. By enabling or using any of the features or functionalities within Programmable Voice that are identified as using artificial intelligence or machine learning technology, you acknowledge and agree that your use of these features or functionalities is subject to the terms of the [Predictive and Generative AI/ML Features Addendum(link takes you to an external page)](https://www.twilio.com/en-us/legal/ai-terms/predictive-generative-ai-features "Predictive and Generative AI/ML Features Addendum").

Transcriptions is a subresource of [Calls](/docs/voice/api/call-resource "Calls") and represents a real-time audio transcription during a live call. You can start and stop a transcription on any in-progress call via API or via the [<Transcription> TwiML Noun](/docs/voice/twiml/transcription "<Transcription> TwiML Noun").

  * To start a real-time transcription on a live call, [create a Transcription](/docs/voice/api/realtime-transcription-resource#create-a-transcription "create a Transcription").
  * To stop a real-time transcription, [update a Transcription status](/docs/voice/api/realtime-transcription-resource#update-a-transcription "update a Transcription status").


* * *

## Calls Transcriptions properties

calls-transcriptions-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<GT>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Transcription resource.

Pattern: `^GT[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this Transcription resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Transcription resource is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The user-specified name of this Transcription, if one was given when the Transcription was created. This may be used to stop the Transcription.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status - one of `stopped`, `in-flight`

Possible values:

`in-progress``stopped`

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that this resource was last updated, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

## Create a Transcription

create-a-transcription page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions.json`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this Transcription resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Transcription resource is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The user-specified name of this Transcription, if one was given when the Transcription was created. This may be used to stop the Transcription.

* * *

trackenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

One of `inbound_track`, `outbound_track`, `both_tracks`.

Possible values:

`inbound_track``outbound_track``both_tracks`

* * *

statusCallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Absolute URL of the status callback.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The http method for the status_callback (one of GET, POST).

Possible values:

`GET``POST`

* * *

inboundTrackLabelstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Friendly name given to the Inbound Track

* * *

outboundTrackLabelstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Friendly name given to the Outbound Track

* * *

partialResultsboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates if partial results are going to be sent to the customer

* * *

languageCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Language code used by the transcription engine, specified in [BCP-47(link takes you to an external page)](https://www.rfc-editor.org/rfc/bcp/bcp47.txt "BCP-47") format

* * *

transcriptionEnginestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Definition of the transcription engine to be used, among those supported by Twilio

* * *

profanityFilterboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

indicates if the server will attempt to filter out profanities, replacing all but the initial character in each filtered word with asterisks

* * *

speechModelstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Recognition model used by the transcription engine, among those supported by the provider

* * *

hintsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A Phrase contains words and phrase "hints" so that the speech recognition engine is more likely to recognize them.

* * *

enableAutomaticPunctuationboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The provider will add punctuation to recognition result

* * *

intelligenceServicestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID or unique name of the [Intelligence Service](/docs/conversational-intelligence/api/service-resource "Intelligence Service") for persisting transcripts and running post-call Language Operators

* * *

conversationConfigurationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The ID of the Conversations Configuration for customizing conversation behavior in Intelligence Service

* * *

conversationIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The ID of the Conversation for associating this Transcription with an existing Conversation in Intelligence Service

* * *

enableProviderDataboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the callback includes raw provider data.

Select from available examples

Copy code block


    {}

Create a TranscriptionLink to code sample: Create a Transcription

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

    async function createRealtimeTranscription() {


    11

      const transcription = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .transcriptions.create();


    14




    15

      console.log(transcription.sid);


    16

    }


    17




    18

    createRealtimeTranscription();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "sid": "GTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "name": null,


    6

      "status": "in-progress",


    7

      "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000",


    8

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/GTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    9

    }

* * *

## Update a Transcription

update-a-transcription page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Transcriptions/{Sid}.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this Transcription resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Transcription resource is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Transcription resource, or the `name` used when creating the resource

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

statusenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`stopped`

Select from available examples

Copy code block


    {


      "Status": "stopped"


    }

You can stop an in-progress Transcription by updating the `status` to `stopped`. You can also [use TwiML to stop a Transcription](/docs/voice/twiml/transcription "use TwiML to stop a Transcription").

When making this request, you can use the Transcription subresource's SID or the `name` (if one was given when the Transcription was created).

Stop a real-time TranscriptionLink to code sample: Stop a real-time Transcription

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

    async function updateRealtimeTranscription() {


    11

      const transcription = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .transcriptions("GTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .update({ status: "stopped" });


    15




    16

      console.log(transcription.sid);


    17

    }


    18




    19

    updateRealtimeTranscription();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "sid": "GTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "name": null,


    6

      "status": "stopped",


    7

      "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000",


    8

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/GTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    9

    }

* * *

## HIPAA eligibility and PCI compliance

hipaa-eligibility-and-pci-compliance page anchor

Positive FeedbackNegative Feedback

HIPAA eligibility and PCI compliance varies depending on your selected speech model and whether you use webhooks or persisted transcripts. To determine whether your implementation may be HIPAA eligible or PCI compliant, see the following table.

Transcription engine| Speech model| Transcript destination| HIPAA eligibility| PCI-compliant
---|---|---|---|---
Google| Any supported model| Webhooks| Yes| Yes
Google| Any supported model| Persisted Transcript| Yes| No
Deepgram| `nova-2` or `nova-3` monolingual variants| Webhooks| Yes| Yes
Deepgram| `nova-2` or `nova-3` monolingual variants| Persisted Transcript| Yes| No
Deepgram| `nova-3` multilingual| Webhooks or Persisted Transcript| No| No

* * *

## AI nutrition facts

ai-nutrition-facts page anchor

Positive FeedbackNegative Feedback

(information)

## AI Nutrition Facts

The Calls Transcriptions subresource and `<Transcriptions>` TwiML noun use third-party artificial technology and machine learning technologies.

[Twilio's AI Nutrition Facts(link takes you to an external page)](https://nutrition-facts.ai/ "Twilio's AI Nutrition Facts") provide an overview of the AI feature you're using, so you can better understand how the AI is working with your data. Real-Time Transcriptions AI qualities are outlined in the following **Speech to Text Transcriptions - Programmable Voice Nutrition Facts** label. For more information and the glossary regarding the AI Nutrition Facts Label, see [Twilio's AI Nutrition Facts(link takes you to an external page)](https://nutrition-facts.ai/ "Twilio's AI Nutrition Facts").

## AI Nutrition Facts

### Speech to Text Transcriptions - Programmable Voice, Twilio Video, and Conversational Intelligence

Description
    Generate speech to text voice transcriptions (real-time and post-call) in Programmable Voice, Twilio Video, and Conversational Intelligence.

Privacy Ladder Level
    N/A

Feature is Optional
    Yes

Model Type
    Generative and Predictive - Automatic Speech Recognition

Base Model
    Deepgram Speech-to-Text, Google Speech-to-Text, Amazon Transcribe

#### Trust Ingredients

Base Model Trained with Customer Data
    No

Conversational Intelligence, Programmable Voice, and Twilio Video only use the default Base Model provided by the Model Vendor. The Base Model is not trained using customer data.

Customer Data is Shared with Model Vendor
    No

Conversational Intelligence, Programmable Voice, and Twilio Video only use the default Base Model provided by the Model Vendor. The Base Model is not trained using customer data.

Training Data Anonymized
    N/A

Base Model is not trained using any customer data.

Data Deletion
    Yes

Transcriptions are deleted by the customer using the Conversational Intelligence API or when a customer account is deprovisioned.

Human in the Loop
    Yes

The customer views output in the Conversational Intelligence API or Transcript Viewer.

Data Retention
    Until the customer deletes

Compliance

Logging & Auditing
    Yes

The customer can listen to the input (recording) and view the output (transcript).

Guardrails
    Yes

The customer can listen to the input (recording) and view the output (transcript).

Input/Output Consistency
    Yes

The customer is responsible for human review.

Other Resources
    https://www.twilio.com/docs/conversational-intelligence

Learn more about this label at [nutrition-facts.ai(link takes you to an external page)](https://www.nutrition-facts.ai)