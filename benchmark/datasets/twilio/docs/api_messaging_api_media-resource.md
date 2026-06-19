# Media subresource

*Source: https://www.twilio.com/docs/messaging/api/media-resource*

---

# Media subresource

Positive FeedbackNegative Feedback

* * *

Media is a subresource of [Messages](/docs/messaging/api/message-resource "Messages") and represents a piece of media, such as an image, that is associated with a Message.

Twilio creates a Media subresource and stores the contents of the media when the following events occur:

  1. You [send an MMS](/docs/messaging/tutorials/how-to-send-sms-messages "send an MMS") with an image via Twilio.
  2. You [send a WhatsApp message with an image](/docs/whatsapp/tutorial/send-and-receive-media-messages-twilio-api-whatsapp "send a WhatsApp message with an image") via Twilio.
  3. You receive media in a message sent to one of your Twilio numbers or messaging channel addresses.


Twilio retains the stored media until you [delete the related Media subresource instance.](/docs/messaging/api/media-resource#delete-media "delete the related Media subresource instance.")

(information)

## Info

**Authentication required** : Twilio enforces [HTTP Basic Authentication](/docs/glossary/what-is-basic-authentication "HTTP Basic Authentication") for all media URLs. Authenticate using an [API key](/docs/iam/api-keys "API key") as the username and an API key secret as the password. You can also use your Account SID and Auth Token when testing locally.

(warning)

## Warning

You can send messages using Twilio with up to 10 media files that have a total size of up to 5MB. Twilio resizes images as necessary for successful delivery based on carrier specifications. Twilio rejects messages with over 5MB of media.

* * *

## Medium Properties

medium-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") associated with this Media resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

contentTypestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The default [MIME type(link takes you to an external page)](https://en.wikipedia.org/wiki/Internet_media_type "MIME type") of the media, for example `image/jpeg`, `image/png`, or `image/gif`.

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when this Media resource was created, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when this Media resource was last updated, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

parentSidSID<SM|MM>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource that is associated with this Media resource.

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<ME>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that identifies this Media resource.

Pattern: `^ME[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of this Media resource, relative to `https://api.twilio.com`.

* * *

## Retrieve Media

retrieve-media page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json`

Returns a single Media subresource using one of several representations:

  * `content-type`
  * `XML`
  * `JSON`


* * *

## Default: content-type

default-content-type page anchor

Positive FeedbackNegative Feedback

Without an extension, Twilio returns the media using the mime-type it assigned when it generated the media.

Copy code block


    1

    GET /2010-04-01/Accounts/AC.../Message/MM.../Media/ME557ce644e5ab84fa21cc21112e22c485


    2

### Alternative: XML

alternative-xml page anchor

Positive FeedbackNegative Feedback

Appending ".xml" to the URI returns a familiar XML representation. For example:

Copy code block


    1

    GET /2010-04-01/Accounts/AC.../Message/MM.../Media/ME557ce644e5ab84fa21cc21112e22c485.xml


    2

Copy code block


    1

    <TwilioResponse>


    2

     <Media>


    3

       <Sid>ME557ce644e5ab84fa21cc21112e22c485</Sid>


    4

       <AccountSid>ACda6f1e11047ebd6fe7a55f120be3a900</AccountSid>


    5

       <ParentSid>MM8dfedb55c129dd4d6bd1f59af9d11080</ParentSid>


    6

       <ContentType>image/jpeg</ContentType>


    7

       <DateCreated>Fri, 17 Jul 2009 01:52:49 +0000</DateCreated>


    8

       <DateUpdated>Fri, 17 Jul 2009 01:52:49 +0000</DateUpdated>


    9

       <Uri>/2010-04-01/Accounts/ACda6f1e11047ebd6fe7a55f120be3a900/Message/MM8dfedb55c129dd4d6bd1f59af9d11080/Media/ME557ce644e5ab84fa21cc21112e22c485.xml</Uri>


    10

     </Media>


    11

    </TwilioResponse>

### Alternative: JSON

alternative-json page anchor

Positive FeedbackNegative Feedback

Appending ".json" to the URI returns a familiar JSON representation. For example:

Copy code block


    1

    GET /2010-04-01/Accounts/AC.../Message/MM.../Media/ME557ce644e5ab84fa21cc21112e22c485.json


    2

Copy code block


    1

    {


    2

        "sid": "ME557ce644e5ab84fa21cc21112e22c485",


    3

        "account_sid": "ACda6f1e11047ebd6fe7a55f120be3a900",


    4

        "parent_sid": "MM8ff928b2451c0db925bd2d581f0fba79",


    5

        "content_type": "image/jpeg",


    6

        "date_created": "Fri, 26 Apr 2013 05:41:35 +0000",


    7

        "date_updated": "Fri, 26 Apr 2013 05:41:35 +0000",


    8

        "uri": "/2010-04-01/Accounts/ACda6f1e11047ebd6fe7a55f120be3a900/Message/MM8dfedb55c129dd4d6bd1f59af9d11080/Media/ME557ce644e5ab84fa21cc21112e22c485.json"


    9

    }

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") associated with the Media resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messageSidSID<SM|MM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource that is associated with the Media resource.

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<ME>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Media resource to fetch.

Pattern: `^ME[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

(warning)

## Warning

**Authentication required** : Twilio enforces [HTTP Basic Authentication](/docs/glossary/what-is-basic-authentication "HTTP Basic Authentication") for all media URLs. Authenticate using an [API key](/docs/iam/api-keys "API key") as the username and an API key secret as the password. You can also use your Account SID and Auth Token when testing locally.

When you fetch your Message Media via the API, you will receive the media content directly. If you need to embed media in web applications without exposing your credentials, download the media files and serve them from your own server or cloud storage service.

For applications that need temporary access to media URLs, consider implementing a server-side proxy that handles authentication and serves media to your client applications.

Fetch a MediumLink to code sample: Fetch a Medium

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

    async function fetchMedia() {


    11

      const media = await client


    12

        .messages("SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .media("MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .fetch();


    15




    16

      console.log(media.accountSid);


    17

    }


    18




    19

    fetchMedia();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "content_type": "image/jpeg",


    4

      "date_created": "Sun, 16 Aug 2015 15:53:54 +0000",


    5

      "date_updated": "Sun, 16 Aug 2015 15:53:55 +0000",


    6

      "parent_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

      "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    9

    }

* * *

## Retrieve a list of Media

retrieve-a-list-of-media page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media.json`

Returns a list of Media associated with your Message. The list includes [paging information](/docs/usage/twilios-response#pagination "paging information").

Retrieve a list of Media associated with a MessageLink to code sample: Retrieve a list of Media associated with a Message

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

    async function listMedia() {


    11

      const media = await client


    12

        .messages("MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .media.list({ limit: 20 });


    14




    15

      media.forEach((m) => console.log(m.accountSid));


    16

    }


    17




    18

    listMedia();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?DateCreated%3E=2008-01-02&PageSize=50&Page=0",


    4

      "media_list": [


    5

        {


    6

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "content_type": "image/jpeg",


    8

          "date_created": "Sun, 16 Aug 2015 15:53:54 +0000",


    9

          "date_updated": "Sun, 16 Aug 2015 15:53:55 +0000",


    10

          "parent_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    12

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    13

        }


    14

      ],


    15

      "next_page_uri": null,


    16

      "page": 0,


    17

      "page_size": 50,


    18

      "previous_page_uri": null,


    19

      "start": 0,


    20

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json?DateCreated%3E=2008-01-02&PageSize=50&Page=0"


    21

    }

### Filter by date created

filter-by-date-created page anchor

Positive FeedbackNegative Feedback

You may limit the list of Message Media to media created on a given date. Provide the following query string parameter to your API call:

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that is associated with the Media resources.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messageSidSID<SM|MM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource that is associated with the Media resources.

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include Media resources that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read Media that were created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read Media that were created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read Media that were created on or after midnight of this date.

* * *

dateCreatedBeforestring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include Media resources that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read Media that were created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read Media that were created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read Media that were created on or after midnight of this date.

* * *

dateCreatedAfterstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include Media resources that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read Media that were created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read Media that were created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read Media that were created on or after midnight of this date.

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

* * *

## Delete Media

delete-media page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json`

Deletes Media from your account.

If successful, returns HTTP 204 (No Content) with no body.

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that is associated with the Media resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messageSidSID<SM|MM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Message resource that is associated with the Media resource.

Pattern: `^(SM|MM)[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<ME>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique identifier of the to-be-deleted Media resource.

Pattern: `^ME[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete Media from your accountLink to code sample: Delete Media from your account

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

    async function deleteMedia() {


    11

      await client


    12

        .messages("MM800f449d0399ed014aae2bcc0cc2f2ec")


    13

        .media("ME557ce644e5ab84fa21cc21112e22c485")


    14

        .remove();


    15

    }


    16




    17

    deleteMedia();

### Hints and Advanced Uses

hints page anchor

Positive FeedbackNegative Feedback

  * Twilio attempts to cache the media file the first time it is used. This may add a slight delay in sending the message.
  * Twilio caches files when HTTP headers allow it (via ETag and Last-Modified headers). Responding with `Cache-Control: no-cache` ensures Twilio always checks if the file has changed, allowing your web server to respond with a new version or with a 304 Not Modified to instruct Twilio to use its cached version.