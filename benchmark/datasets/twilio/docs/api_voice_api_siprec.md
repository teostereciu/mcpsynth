# Siprec subresource

*Source: https://www.twilio.com/docs/voice/api/siprec*

---

# Siprec subresource

Positive FeedbackNegative Feedback

* * *

## Siprec Properties

siprec-properties page anchor

Positive FeedbackNegative Feedback

Siprec is a subresource of [Calls](/docs/voice/api/call-resource "Calls") and allows you to start a stream on a phone call and send that stream to one of the available partners via a configured [SIPREC Connector(link takes you to an external page)](https://console.twilio.com/us1/develop/add-ons/catalog?tags=stream_connectors "SIPREC Connector"). You can also stop streams started via the [<Siprec> TwiML](/docs/voice/twiml/siprec "<Siprec> TwiML") instruction.

Twilio operates as a Session Recording Client (SRC) for SIPREC, while Twilio's partners, such as Gridspace, operate as Session Recording Servers (SRS). Alternatively, you can provision your own SRS using the [Twilio SIPREC Connector(link takes you to an external page)](https://console.twilio.com/us1/develop/add-ons/catalog?tags=stream_connectors "Twilio SIPREC Connector").

The SRC sends the SIPREC media to be recorded to the SRS. The SRS is responsible for storing/processing the media.

Twilio forks the audio stream of the current call and sends it in real-time to the configured connector.

There are a maximum of **four** forked streams allowed per call. By default, `<Siprec>` uses two forked streams: one for the inbound track and one for the outbound track.

Dual-Tone Multi-Frequency (DTMF) tones aren't sent to the connector.

Any communication issues encountered while streaming media to the partner will be reported in the Twilio Debugger with additional information about the failure.

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<SR>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Siprec resource.

Pattern: `^SR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this Siprec resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Siprec resource is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used to stop the Siprec.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status - one of `stopped`, `in-progress`

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

The URI of the resource, relative to `https://api.twilio.com`.

* * *

## Configuring a SIPREC Connector

configure-siprec-connector page anchor

Positive FeedbackNegative Feedback

Connectors are configured in Marketplace to ensure that the credentials needed to send the stream to a partner are stored securely. You can install and manage connectors in the [Stream Connectors Console page in Marketplace(link takes you to an external page)](https://console.twilio.com/us1/develop/add-ons/catalog?tags=stream_connectors "Stream Connectors Console page in Marketplace") or via the [Marketplace API](/docs/marketplace/listings/api-overview-users "Marketplace API") using the [InstalledAddOns Resource](/docs/marketplace/api/installed-add-ons "InstalledAddOns Resource").

(information)

## Info

If you'd like to use a specific partner and don't find them in the available [Stream Connectors(link takes you to an external page)](https://console.twilio.com/us1/develop/add-ons/catalog?tags=stream_connectors "Stream Connectors") list, contact Twilio Support directly with details about your desired partner through the [Console(link takes you to an external page)](https://console.twilio.com/ "Console") or [Help Center(link takes you to an external page)](https://help.twilio.com "Help Center") to submit a ticket.

### Twilio's SIPREC Connector

twilios-siprec-connector page anchor

Positive FeedbackNegative Feedback

Configure your SIPREC Connector using the parameters below.

Parameter Name| Description
---|---
Installed Add-On SID| The unique identifier for your connector. It's automatically configured when you install a connector.
Unique Name| The unique name to use for your SIPREC Connector. This is the name you will use when initiating the [<Siprec> TwiML](/docs/voice/twiml/siprec "<Siprec> TwiML") instruction or using the API.
Use In| Specifies that the connector is available to your Voice Applications.
Session Recording Server| The SIP URI of the server you want to stream the media to. This should be a standard SIP URI. For example, sip:name@example.com:5060.
Credentials Header Name| The SIP header name that your recording service uses to pass the Authorization credentials. For example, `X-Auth-Token`.
Credentials| The credential token or value for Authorization to be sent to your recording service. This value will be hidden when entered in the text box.

Using Twilio's SIPREC Connector provides some additional SIP features. The **SIP URI** within the `Session Recording Server` parameter supports additional parameters: `secure` which enables Secure Real-time Transport Protocol (SRTP), as well as, `edge` which allows you to control which [Twilio edge](/docs/global-infrastructure/edge-locations "Twilio edge") your SIPREC connections egress by.

For example, to enable SRTP and set the [edge location](/docs/global-infrastructure/edge-locations "edge location") to the ashburn edge, you would provide populate **SIP URI** below as the `Session Recording Server` address:

`sip:your-domain.com;secure=true&edge=ashburn`

* * *

## Create a Siprec

create-a-siprec page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec.json`

Parameter| Type| Description
---|---|---
`AccountSid` Path| SID<AC>| The SID of the [Account](/docs/iam/api/account "Account") that created this Siprec subresource. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`CallSid` Path| SID<CA>| The SID of the [Call](/docs/voice/api/call-resource "Call") the Siprec subresource is associated with. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`Name` Optional| string| The user-specified name of this Siprec subresource, if one was given when the Siprec was created. This may be used to stop the Siprec. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`ConnectorName` Optional| string| Unique name used when configuring the connector via Marketplace Add-on. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`Track` Optional| string| One of `inbound_track`, `outbound_track`, `both_tracks`. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`StatusCallback` Optional| uri| Absolute URL of the status callback. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`StatusCallbackMethod` Optional| http_method| The http method for the `StatusCallback` (one of `GET`, `POST`). [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`Parameter1.Name` Optional| string| Parameter name [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`Parameter1.Value` Optional| string| Parameter value [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")

### Using the SIPREC status callback

using-the-siprec-status-callback page anchor

Positive FeedbackNegative Feedback

SIPREC is a protocol that enables recording and sending streams to one of the available partners via the SIPREC connector configuration. With the addition of a status callback, you can now get detailed information about the status of a SIPREC session. This feature can be used to quickly detect and troubleshoot any unexpected issues with a SIPREC session, such as an unexpected failure or interruption.

**There are two ways to use SIPREC status callback:**

From [<Siprec>](/docs/voice/twiml/siprec#code-start-a-new-siprec-stream "<Siprec>") TwiML, for example:

Copy code block


    1

    <Start>


    2

    <Siprec name="my-first-siprec" connectorName="Gridspace1" statusCallback="https://87b252436d40.ngrok.app" statusCallbackMethod="GET"/>


    3

    </Start>

From Start/Stop SIPREC API, for example:

Copy code block


    1

    curl -u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN -XPOST https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Siprec.json --data-urlencode \


    2

    "Name=my-first-siprec" --data-urlencode "ConnectorName=Gridspace1" --data-urlencode "StatusCallback=https://XXXXXXXX.ngrok.app" --data-urlencode "StatusCallbackMethod=GET"

The request to the status callback contains the standard [TwiML request parameters](/docs/voice/twiml#request-parameters "TwiML request parameters") and the following parameters:

Parameter| Description
---|---
`AccountSid`| The SID of the [Account](/docs/iam/api/account "Account") that created this Siprec subresource. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`CallSid`| The SID of the [Call](/docs/voice/api/call-resource "Call") the Siprec subresource is associated with. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`SiprecSid`| The SID of the Siprec subresource is associated with. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`SiprecName`| The Name of the Siprec subresource is associated with. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`SiprecEvent`| The Event of the Siprec callback. Values can be: `siprec-started`, `siprec-stopped`, `siprec-error` [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")
`Timestamp`| The timestamp of when the Siprec callback was made. [Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "Not PII")

If an error has occurred, additional parameters `SiprecError`, `SiprecErrorCode` will be set as well. These params will provide context on the error that has occurred with the Siprec subresource.

* * *

## Update a Siprec

update-a-siprec page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec/{Sid}.json`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this Siprec resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Siprec resource is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Siprec resource, or the `name` used when creating the resource

### Request body parameters

request-body-parameters page anchor

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

Update a SiprecLink to code sample: Update a Siprec

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

    async function updateSiprec() {


    11

      const siprec = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .siprec("Sid")


    14

        .update({ status: "stopped" });


    15




    16

      console.log(siprec.sid);


    17

    }


    18




    19

    updateSiprec();

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

      "sid": "Sid",


    5

      "name": null,


    6

      "status": "stopped",


    7

      "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000",


    8

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec/SRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    9

    }