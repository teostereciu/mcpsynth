# Challenge Resource

*Source: https://www.twilio.com/docs/verify/api/passkeys-challenge*

---

# Challenge Resource

Positive FeedbackNegative Feedback

* * *

The Passkeys Challenge resource represents a single verification attempt of a [Service](/docs/verify/api/service "Service"), an [Entity](/docs/verify/api/entity "Entity") or a [Factor](/docs/verify/api/passkeys-factor "Factor").

* * *

## Challenge Properties

challenge-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

optionsobject

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An object that contains challenge options. Currently only used for `passkeys`.

* * *

sidSID<YC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this Challenge.

Pattern: `^YC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Account.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

serviceSidSID<VA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Service.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

entitySidSID<YE>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Entity.

Pattern: `^YE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

identitystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Customer unique identity for the Entity owner of the Challenge.

* * *

factorSidSID<YF>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Factor.

Pattern: `^YF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this Challenge was created, given in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this Challenge was updated, given in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateRespondedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this Challenge was responded, given in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

expirationDatestring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date-time when this Challenge expires, given in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Status of this Challenge. One of `pending`, `expired`, `approved` or `denied`.

Possible values:

`pending``expired``approved``denied`

* * *

respondedReasonenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reason for the Challenge to be in certain `status`. One of `none`, `not_needed` or `not_requested`.

Possible values:

`none``not_needed``not_requested`

* * *

details

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Details provided to give context about the Challenge.

* * *

hiddenDetails

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Details provided to give context about the Challenge.

* * *

metadata

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Custom metadata associated with the challenge.

* * *

factorTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Factor Type of this Challenge. Currently `push` and `totp` are supported.

Possible values:

`push``totp``passkeys`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of this resource.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains a dictionary of URL links to nested resources of this Challenge.

* * *

## Create a Passkeys Challenge resource

create-a-passkeys-challenge-resource page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/Passkeys/Challenges`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Service.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/json`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

identitystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

factorSidstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Select from available examples

Copy code block


    {}

Create a ChallengeLink to code sample: Create a Challenge

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

    async function createChallengePasskeys() {


    11

      const newChallenge = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .newChallenge()


    14

        .create({


    15

          identity: "identity",


    16

        });


    17




    18

      console.log(newChallenge.options);


    19

    }


    20




    21

    createChallengePasskeys();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "entity_sid": "",


    6

      "identity": "identity",


    7

      "factor_sid": "",


    8

      "factor_type": "passkeys",


    9

      "status": "pending",


    10

      "date_created": "2025-07-30T20:00:00Z",


    11

      "date_updated": "2025-07-30T20:00:00Z",


    12

      "date_responded": null,


    13

      "details": null,


    14

      "expiration_date": null,


    15

      "hidden_details": null,


    16

      "links": null,


    17

      "metadata": null,


    18

      "responded_reason": "none",


    19

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Passkeys/Challenges",


    20

      "options": {


    21

        "publicKey": {


    22

          "rp": {


    23

            "id": "example.com",


    24

            "name": "Example"


    25

          },


    26

          "user": {


    27

            "id": "WUU0ZmQzYWFmNGU0NTMyNGQwZjNlMTM0NjA3YjIxOTEyYg",


    28

            "name": "friendly_name",


    29

            "displayName": "friendly_name"


    30

          },


    31

          "challenge": "WUYwNDhkMWE3ZWMzYTJhNjk3MDA1OWMyNzY2YmJjN2UwZg",


    32

          "pubKeyCredParams": {


    33

            "type": "public-key",


    34

            "alg": -7


    35

          },


    36

          "timeout": 600000,


    37

          "excludeCredentials": [],


    38

          "authenticatorSelection": {


    39

            "authenticatorAttachment": "platform",


    40

            "requireResidentKey": false,


    41

            "residentKey": "preferred",


    42

            "userVerification": "preferred"


    43

          },


    44

          "attestation": "none"


    45

        }


    46

      }


    47

    }

* * *

## Approve a Passkeys Challenge resource

approve-a-passkeys-challenge-resource page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/Passkeys/ApproveChallenge`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Service.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/json`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

idstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A [base64url(link takes you to an external page)](https://base64.guru/standards/base64url "base64url") encoded representation of `rawId`.

* * *

rawIdstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The globally unique identifier for this `PublicKeyCredential`.

* * *

authenticatorAttachmentenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string that indicates the mechanism by which the WebAuthn implementation is attached to the authenticator at the time the associated `navigator.credentials.create()` or `navigator.credentials.get()` call completes.

Possible values:

`platform``cross-platform`

* * *

typeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The valid credential types supported by the API. The values of this enumeration are used for versioning the `AuthenticatorAssertion` and `AuthenticatorAttestation` structures according to the type of the authenticator.

Default: `public-key`Possible values:

`public-key`

* * *

responseobject

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The result of a WebAuthn authentication via a `navigator.credentials.get()` request, as specified in [AuthenticatorAttestationResponse(link takes you to an external page)](https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAttestationResponse "AuthenticatorAttestationResponse").

Show response properties

Property nameTypeRequiredPIIDescriptionChild properties

authenticatorDatastring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [authenticator data(link takes you to an external page)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API/Authenticator_data "authenticator data") structure contains information from the authenticator about the processing of a credential creation or authentication request.

* * *

clientDataJSONstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

This property contains the JSON-compatible serialization of the data passed from the browser to the authenticator in order to generate this credential.

* * *

signaturestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An assertion signature over `authenticatorData` and `clientDataJSON`. The assertion signature is created with the private key of the key pair that was created during the originating `navigator.credentials.create()` call and verified using the public key of that same key pair.

* * *

userHandlestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The user handle stored in the authenticator, specified as `user.id` in the options passed to the originating `navigator.credentials.create()` call. This property should contain a base64url-encoded entity SID.

Copy code block


    {


      "id": "6ySmhJd6qGUMCthiqszyb4Od4U6TFn0v3DLz-1EZrNQ",


      "rawId": "eb24a684977aa8650c0ad862aaccf26f839de14e93167d2fdc32f3fb5119acd4",


      "authenticatorAttachment": "platform",


      "type": "public-key",


      "response": {


        "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRlIiwiY2hhbGxlbmdlIjoiV1VZd05EaGtNV0UzWldNellUSmhOamszTURBMU9XTXlOelkyWW1Kak4yVXdaZyIsIm9yaWdpbiI6Imh0dHBzOi8vZXhhbXBsZS5jb20iLCJjcm9zc09yaWdpbiI6ZmFsc2V9",


        "signature": "MEYCIQDDs662ykELzpmxkQaOR6HY5GwO7n",


        "userHandle": "WUU0ZmQzYWFmNGU0NT",


        "authenticatorData": "o3mm9u6vuaVeN4wRgDTid"


      }


    }

Approve a Passkeys Challenge resourceLink to code sample: Approve a Passkeys Challenge resource

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

    async function updateChallengePasskeys() {


    11

      const approveChallenge = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .approveChallenge.update({


    14

          id: "id",


    15

          rawId: "rawId",


    16

          authenticatorAttachment: "platform",


    17

          response: {


    18

            authenticatorData: "authenticatorData",


    19

            clientDataJSON: "clientDataJSON",


    20

            signature: "signature",


    21

            userHandle: "userHandle",


    22

          },


    23

        });


    24




    25

      console.log(approveChallenge.options);


    26

    }


    27




    28

    updateChallengePasskeys();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "entity_sid": "",


    6

      "identity": "",


    7

      "factor_sid": "",


    8

      "factor_type": "passkeys",


    9

      "status": "approved",


    10

      "date_created": "2025-07-30T20:00:00Z",


    11

      "date_updated": "2025-07-30T20:00:00Z",


    12

      "date_responded": null,


    13

      "details": null,


    14

      "expiration_date": null,


    15

      "hidden_details": null,


    16

      "links": null,


    17

      "metadata": null,


    18

      "responded_reason": "none",


    19

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Passkeys/ApproveChallenge",


    20

      "options": {


    21

        "publicKey": {


    22

          "rp": {


    23

            "id": "example.com",


    24

            "name": "Example"


    25

          },


    26

          "user": {


    27

            "id": "WUU0ZmQzYWFmNGU0NTMyNGQwZjNlMTM0NjA3YjIxOTEyYg",


    28

            "name": "friendly_name",


    29

            "displayName": "friendly_name"


    30

          },


    31

          "challenge": "WUYwNDhkMWE3ZWMzYTJhNjk3MDA1OWMyNzY2YmJjN2UwZg",


    32

          "pubKeyCredParams": {


    33

            "type": "public-key",


    34

            "alg": -7


    35

          },


    36

          "timeout": 600000,


    37

          "excludeCredentials": [],


    38

          "authenticatorSelection": {


    39

            "authenticatorAttachment": "platform",


    40

            "requireResidentKey": false,


    41

            "residentKey": "preferred",


    42

            "userVerification": "preferred"


    43

          },


    44

          "attestation": "none"


    45

        }


    46

      }


    47

    }