# Factor Resource

*Source: https://www.twilio.com/docs/verify/api/passkeys-factor*

---

# Factor Resource

Positive FeedbackNegative Feedback

* * *

The Passkey Factor resource is currently used by Passkeys. This factor is different than the Factor resource used for Push and TOTP verification and its properties apply to Passkeys only. A single `Entity` links to multiple `Passkey Factors` and `TOTP/Push Factors`.

* * *

## Passkey Factor properties

passkey-factor-properties page anchor

Positive FeedbackNegative Feedback

(information)

## Info

For security reasons the `options` property is ONLY returned when the resource is created and is never returned in later requests.

(information)

## Info

In the request, if the specified `Entity` with the `{identity}` path parameter doesn't exist, it will be created automatically. You don't need to create a new Entity separately before making this request.

* * *

## Factor Properties

factor-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<YF>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this Factor.

Pattern: `^YF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

Customer unique identity for the Entity owner of the Factor.

* * *

binding

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains the `factor_type` specific secret and metadata. The Binding property is ONLY returned upon Factor creation.

* * *

optionsnull

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this Factor was created, given in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this Factor was updated, given in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The friendly name of this Factor. This can be any string up to 64 characters, meant for humans to distinguish between Factors.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Status of this Factor. One of `unverified` or `verified`.

Possible values:

`unverified``verified`

* * *

factorTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Type of this Factor. Currently `push` and `totp` are supported.

Possible values:

`push``totp``passkeys`

* * *

config

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An object that contains configurations specific to a `factor_type`.

* * *

metadata

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Custom metadata associated with the factor.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of this resource.

* * *

## Create a Passkeys Factor resource

create-a-passkeys-factor-resource page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/Passkeys/Factors`

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

friendlyNamestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

identitystring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

configobject

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Show config properties

Property nameTypeRequiredPIIDescriptionChild properties

relyingPartyobject

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains the information of the party requesting the user for authentication

Show relyingParty properties

Property nameTypeRequiredPIIDescriptionChild properties

idstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

originsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

authenticatorAttachmentenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`platform``cross-platform``any`

* * *

discoverableCredentialsenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`required``preferred``discouraged`

* * *

userVerificationenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`required``preferred``discouraged`

Copy code block


    {


      "friendly_name": "FriendlyName",


      "identity": "ff483d1ff591898a9942916050d2ca3f",


      "config": {


        "relying_party": {


          "id": "example.com",


          "name": "Example",


          "origins": [


            "https://example.com"


          ]


        },


        "authenticator_attachment": "platform",


        "discoverable_credentials": "preferred",


        "user_verification": "preferred"


      }


    }

Create a FactorLink to code sample: Create a Factor

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

    async function createNewFactorPasskey() {


    11

      const newFactor = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .newFactors.create({


    14

          friendly_name: "friendly_name",


    15

          identity: "identity",


    16

        });


    17




    18

      console.log(newFactor.sid);


    19

    }


    20




    21

    createNewFactorPasskey();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "identity": "identity",


    7

      "binding": null,


    8

      "date_created": "2015-07-30T20:00:00Z",


    9

      "date_updated": "2015-07-30T20:00:00Z",


    10

      "friendly_name": "friendly_name",


    11

      "status": "unverified",


    12

      "factor_type": "passkeys",


    13

      "config": {


    14

        "relying_party": {


    15

          "id": "example.com",


    16

          "name": "Example",


    17

          "origins": [


    18

            "https://example.com"


    19

          ]


    20

        },


    21

        "authenticator_attachment": "platform",


    22

        "discoverable_credentials": "preferred",


    23

        "user_verification": "preferred"


    24

      },


    25

      "options": {


    26

        "publicKey": {


    27

          "rp": {


    28

            "id": "example.com",


    29

            "name": "Example"


    30

          },


    31

          "user": {


    32

            "id": "WUU0ZmQzYWFmNGU0NTMyNGQwZjNlMTM0NjA3YjIxOTEyYg",


    33

            "name": "friendly_name",


    34

            "displayName": "friendly_name"


    35

          },


    36

          "challenge": "WUYwNDhkMWE3ZWMzYTJhNjk3MDA1OWMyNzY2YmJjN2UwZg",


    37

          "pubKeyCredParams": {


    38

            "type": "public-key",


    39

            "alg": -7


    40

          },


    41

          "timeout": 600000,


    42

          "excludeCredentials": [],


    43

          "authenticatorSelection": {


    44

            "authenticatorAttachment": "platform",


    45

            "requireResidentKey": false,


    46

            "residentKey": "preferred",


    47

            "userVerification": "preferred"


    48

          },


    49

          "attestation": "none"


    50

        }


    51

      },


    52

      "metadata": null,


    53

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors/YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    54

    }

* * *

## Verify a Passkeys Factor resource

verify-a-passkeys-factor-resource page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/Passkeys/Factors`

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

friendlyNamestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

identitystring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

configobject

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Show config properties

Property nameTypeRequiredPIIDescriptionChild properties

relyingPartyobject

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains the information of the party requesting the user for authentication

Show relyingParty properties

Property nameTypeRequiredPIIDescriptionChild properties

idstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

originsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

authenticatorAttachmentenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`platform``cross-platform``any`

* * *

discoverableCredentialsenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`required``preferred``discouraged`

* * *

userVerificationenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`required``preferred``discouraged`

Copy code block


    {


      "friendly_name": "FriendlyName",


      "identity": "ff483d1ff591898a9942916050d2ca3f",


      "config": {


        "relying_party": {


          "id": "example.com",


          "name": "Example",


          "origins": [


            "https://example.com"


          ]


        },


        "authenticator_attachment": "platform",


        "discoverable_credentials": "preferred",


        "user_verification": "preferred"


      }


    }

Update a FactorLink to code sample: Update a Factor

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

    async function createNewFactorPasskey() {


    11

      const newFactor = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .newFactors.create({


    14

          friendly_name: "friendly_name",


    15

          identity: "identity",


    16

        });


    17




    18

      console.log(newFactor.sid);


    19

    }


    20




    21

    createNewFactorPasskey();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "identity": "identity",


    7

      "binding": null,


    8

      "date_created": "2015-07-30T20:00:00Z",


    9

      "date_updated": "2015-07-30T20:00:00Z",


    10

      "friendly_name": "friendly_name",


    11

      "status": "unverified",


    12

      "factor_type": "passkeys",


    13

      "config": {


    14

        "relying_party": {


    15

          "id": "example.com",


    16

          "name": "Example",


    17

          "origins": [


    18

            "https://example.com"


    19

          ]


    20

        },


    21

        "authenticator_attachment": "platform",


    22

        "discoverable_credentials": "preferred",


    23

        "user_verification": "preferred"


    24

      },


    25

      "options": {


    26

        "publicKey": {


    27

          "rp": {


    28

            "id": "example.com",


    29

            "name": "Example"


    30

          },


    31

          "user": {


    32

            "id": "WUU0ZmQzYWFmNGU0NTMyNGQwZjNlMTM0NjA3YjIxOTEyYg",


    33

            "name": "friendly_name",


    34

            "displayName": "friendly_name"


    35

          },


    36

          "challenge": "WUYwNDhkMWE3ZWMzYTJhNjk3MDA1OWMyNzY2YmJjN2UwZg",


    37

          "pubKeyCredParams": {


    38

            "type": "public-key",


    39

            "alg": -7


    40

          },


    41

          "timeout": 600000,


    42

          "excludeCredentials": [],


    43

          "authenticatorSelection": {


    44

            "authenticatorAttachment": "platform",


    45

            "requireResidentKey": false,


    46

            "residentKey": "preferred",


    47

            "userVerification": "preferred"


    48

          },


    49

          "attestation": "none"


    50

        }


    51

      },


    52

      "metadata": null,


    53

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors/YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    54

    }