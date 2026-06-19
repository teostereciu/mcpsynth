# Credential Resource

*Source: https://www.twilio.com/docs/conversations/api/credential-resource*

---

# Credential Resource

Positive FeedbackNegative Feedback

* * *

The Credential resource represents one credential record for a specific push notifications channel. Twilio Conversations supports the APNS, FCM, and GCM push notification channels. Each push notification channel vendor issues its own Credentials, and they can vary between vendors. The Credential resource allows you to save the Credentials that should be used for push notifications to a specific channel.

* * *

## Credential Properties

credential-properties page anchor

Positive FeedbackNegative Feedback

The Credential resource contains these properties:

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<CR>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this credential.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The human-readable name of this credential, limited to 64 characters. Optional.

* * *

typeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of push-notification service the credential is for. Can be: `fcm`, `gcm`, or `apn`.

Possible values:

`apn``gcm``fcm`

* * *

sandboxstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was last updated.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this credential.

* * *

## Create a Credential resource

create-a-credential-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Credentials`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

typeenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of push-notification service the credential is for. Can be: `fcm`, `gcm`, or `apn`.

Possible values:

`apn``gcm``fcm`

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A descriptive string that you create to describe the new resource. It can be up to 64 characters long.

* * *

certificatestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[APN only] The URL encoded representation of the certificate. For example, `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.

* * *

privateKeystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.

* * *

sandboxboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.

* * *

apiKeystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.

* * *

secretstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.

Select from available examples

Copy code block


    {


      "Type": "apn"


    }

Create a CredentialLink to code sample: Create a Credential

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

    async function createCredential() {


    11

      const credential = await client.conversations.v1.credentials.create({


    12

        type: "apn",


    13

      });


    14




    15

      console.log(credential.sid);


    16

    }


    17




    18

    createCredential();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "Test slow create",


    5

      "type": "apn",


    6

      "sandbox": "False",


    7

      "date_created": "2015-10-07T17:50:01Z",


    8

      "date_updated": "2015-10-07T17:50:01Z",


    9

      "url": "https://conversations.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    10

    }

* * *

## Fetch a Credential resource

fetch-a-credential-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Credentials/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<CR>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a CredentialLink to code sample: Fetch a Credential

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

    async function fetchCredential() {


    11

      const credential = await client.conversations.v1


    12

        .credentials("CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(credential.sid);


    16

    }


    17




    18

    fetchCredential();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "Test slow create",


    5

      "type": "apn",


    6

      "sandbox": "False",


    7

      "date_created": "2015-10-07T17:50:01Z",


    8

      "date_updated": "2015-10-07T17:50:01Z",


    9

      "url": "https://conversations.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    10

    }

* * *

## Read multiple Credential resources

read-multiple-credential-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Credentials`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 50, and the maximum is 100.

Minimum: `1`Maximum: `100`

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

List multiple CredentialsLink to code sample: List multiple Credentials

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

    async function listCredential() {


    11

      const credentials = await client.conversations.v1.credentials.list({


    12

        limit: 20,


    13

      });


    14




    15

      credentials.forEach((c) => console.log(c.sid));


    16

    }


    17




    18

    listCredential();

### Response

Note about this response

Copy response


    1

    {


    2

      "credentials": [


    3

        {


    4

          "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

          "friendly_name": "Test slow create",


    7

          "type": "apn",


    8

          "sandbox": "False",


    9

          "date_created": "2015-10-07T17:50:01Z",


    10

          "date_updated": "2015-10-07T17:50:01Z",


    11

          "url": "https://conversations.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    12

        }


    13

      ],


    14

      "meta": {


    15

        "page": 0,


    16

        "page_size": 50,


    17

        "first_page_url": "https://conversations.twilio.com/v1/Credentials?PageSize=50&Page=0",


    18

        "previous_page_url": null,


    19

        "url": "https://conversations.twilio.com/v1/Credentials?PageSize=50&Page=0",


    20

        "next_page_url": null,


    21

        "key": "credentials"


    22

      }


    23

    }

* * *

## Update a Credential resource

update-a-credential-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Credentials/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<CR>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

typeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of push-notification service the credential is for. Can be: `fcm`, `gcm`, or `apn`.

Possible values:

`apn``gcm``fcm`

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A descriptive string that you create to describe the new resource. It can be up to 64 characters long.

* * *

certificatestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[APN only] The URL encoded representation of the certificate. For example, `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.

* * *

privateKeystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.

* * *

sandboxboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.

* * *

apiKeystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.

* * *

secretstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.

Copy code block


    {


      "FriendlyName": "Test slow create"


    }

Update a CredentialLink to code sample: Update a Credential

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

    async function updateCredential() {


    11

      const credential = await client.conversations.v1


    12

        .credentials("CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ type: "apn" });


    14




    15

      console.log(credential.sid);


    16

    }


    17




    18

    updateCredential();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "Test slow create",


    5

      "type": "apn",


    6

      "sandbox": "False",


    7

      "date_created": "2015-10-07T17:50:01Z",


    8

      "date_updated": "2015-10-07T17:50:01Z",


    9

      "url": "https://conversations.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    10

    }

* * *

## Delete a Credential resource

delete-a-credential-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Credentials/{Sid}`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<CR>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a CredentialLink to code sample: Delete a Credential

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

    async function deleteCredential() {


    11

      await client.conversations.v1


    12

        .credentials("CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .remove();


    14

    }


    15




    16

    deleteCredential();