# A2P 10DLC - BrandRegistrations resource

*Source: https://www.twilio.com/docs/messaging/api/brand-registration-resource*

---

# A2P 10DLC - BrandRegistrations resource

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

This API reference page supplements the [ISV API onboarding guides](/docs/messaging/compliance/a2p-10dlc/onboarding-isv "ISV API onboarding guides"). Don't use this API resource without following the appropriate guide, or you might experience **delays in registration and unintended fees**.

A BrandRegistration resource represents an A2P 10DLC Brand. It is a "container" that holds all of the business details required by The Campaign Registry (TCR) to create an A2P 10DLC Brand.

* * *

## BrandRegistration Properties

brandregistration-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<BN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string to identify Brand Registration.

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Brand Registration resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

customerProfileBundleSidSID<BU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A2P Messaging Profile Bundle BundleSid.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

a2pProfileBundleSidSID<BU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A2P Messaging Profile Bundle BundleSid.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

brandTypestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Type of brand. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for the low volume, SOLE_PROPRIETOR campaign use case. There can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR brand. STANDARD is for all other campaign use cases. Multiple campaign use cases can be created per STANDARD brand.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Brand Registration status. One of "PENDING", "APPROVED", "FAILED", "IN_REVIEW", "DELETION_PENDING", "DELETION_FAILED", "SUSPENDED".

Possible values:

`PENDING``APPROVED``FAILED``IN_REVIEW``DELETION_PENDING``DELETION_FAILED``SUSPENDED`

* * *

tcrIdstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Campaign Registry (TCR) Brand ID. Assigned only after successful brand registration.

* * *

failureReasonstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

DEPRECATED. A reason why brand registration has failed. Only applicable when status is FAILED.

* * *

errorsarray

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of errors that occurred during the brand registration process.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the Brand Registration resource.

* * *

brandScoreinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The secondary vetting score if it was done. Otherwise, it will be the brand score if it's returned from TCR. It may be null if no score is available.

* * *

brandFeedbackarray[enum<string>]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

DEPRECATED. Feedback on how to improve brand score

Possible values:

`TAX_ID``STOCK_SYMBOL``NONPROFIT``GOVERNMENT_ENTITY``OTHERS`

* * *

identityStatusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

When a brand is registered, TCR will attempt to verify the identity of the brand based on the supplied information.

Possible values:

`SELF_DECLARED``UNVERIFIED``VERIFIED``VETTED_VERIFIED`

* * *

russell3000boolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Publicly traded company identified in the Russell 3000 Index

* * *

governmentEntityboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Identified as a government entity

* * *

taxExemptStatusstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Nonprofit organization tax-exempt status per section 501 of the U.S. tax code.

* * *

skipAutomaticSecVetboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A flag to disable automatic secondary vetting for brands which it would otherwise be done.

* * *

mockboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

## Create a BrandRegistration

create-a-brandregistration page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/a2p/BrandRegistrations`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

customerProfileBundleSidSID<BU>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Customer Profile Bundle Sid.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

a2PProfileBundleSidSID<BU>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A2P Messaging Profile Bundle Sid.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

brandTypestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Type of brand being created. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.

* * *

mockboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.

* * *

skipAutomaticSecVetboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A flag to disable automatic secondary vetting for brands which it would otherwise be done.

Select from available examples

Copy code block


    {


      "CustomerProfileBundleSid": "BU0000009f7e067e279523808d267e2d90",


      "A2PProfileBundleSid": "BU1111109f7e067e279523808d267e2d85",


      "BrandType": "STANDARD",


      "SkipAutomaticSecVet": false,


      "Mock": false


    }

The sample below shows how to create a BrandRegistration.

The `customer_profile_bundle_sid` is the SID associated with the Secondary Customer Profile. It starts with `BU`. You can see Secondary Customer Profile SIDs in [the Console(link takes you to an external page)](https://console.twilio.com/us1/account/trust-hub/overview "the Console"), or you can [list CustomerProfiles via the TrustHub API](/docs/trust-hub/trusthub-rest-api/customer-profiles#read-multiple-customerprofile-resources "list CustomerProfiles via the TrustHub API"). Be sure to use the correct Account SID and Auth Token for the request.

The `a2p_profile_bundle_sid` is the SID of the TrustProduct resource associated with the business. It also starts with `BU`. You can find the appropriate SID by using the TrustHub API to list all of an Account's [TrustProducts](/docs/trust-hub/trusthub-rest-api/trust-products#read-multiple-trustproduct-resources "TrustProducts"). Be sure to use the correct Account SID and Auth Token for the request.

Create a BrandRegistrationLink to code sample: Create a BrandRegistration

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

    async function createBrandRegistrations() {


    11

      const brandRegistration = await client.messaging.v1.brandRegistrations.create(


    12

        {


    13

          a2PProfileBundleSid: "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

          customerProfileBundleSid: "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    15

        }


    16

      );


    17




    18

      console.log(brandRegistration.sid);


    19

    }


    20




    21

    createBrandRegistrations();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "BN0044409f7e067e279523808d267e2d85",


    3

      "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",


    4

      "customer_profile_bundle_sid": "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "a2p_profile_bundle_sid": "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    6

      "date_created": "2021-01-28T10:45:51Z",


    7

      "date_updated": "2021-01-28T10:45:51Z",


    8

      "brand_type": "STANDARD",


    9

      "status": "PENDING",


    10

      "tcr_id": "BXXXXXX",


    11

      "failure_reason": "Registration error",


    12

      "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85",


    13

      "brand_score": 42,


    14

      "brand_feedback": [


    15

        "TAX_ID",


    16

        "NONPROFIT"


    17

      ],


    18

      "identity_status": "VERIFIED",


    19

      "russell_3000": true,


    20

      "government_entity": false,


    21

      "tax_exempt_status": "501c3",


    22

      "skip_automatic_sec_vet": false,


    23

      "errors": [],


    24

      "mock": false,


    25

      "links": {


    26

        "brand_vettings": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings",


    27

        "brand_registration_otps": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/SmsOtp"


    28

      }


    29

    }

The sample below shows an example of how to use the [skip_automatic_sec_vet parameter](/docs/messaging/compliance/a2p-10dlc/collect-business-info#skip_automatic_sec_vet "skip_automatic_sec_vet parameter") when creating a new BrandRegistration. This is **only** for registering a Low Volume Standard Brand, 527 political organization, or political organization with a Campaign Verify token.

Create a BrandRegistration and skip secondary vettingLink to code sample: Create a BrandRegistration and skip secondary vetting

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

    async function createBrandRegistrations() {


    11

      const brandRegistration = await client.messaging.v1.brandRegistrations.create(


    12

        {


    13

          a2PProfileBundleSid: "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

          customerProfileBundleSid: "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    15

          skipAutomaticSecVet: true,


    16

        }


    17

      );


    18




    19

      console.log(brandRegistration.sid);


    20

    }


    21




    22

    createBrandRegistrations();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "BN0044409f7e067e279523808d267e2d85",


    3

      "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",


    4

      "customer_profile_bundle_sid": "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "a2p_profile_bundle_sid": "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    6

      "date_created": "2021-01-28T10:45:51Z",


    7

      "date_updated": "2021-01-28T10:45:51Z",


    8

      "brand_type": "STANDARD",


    9

      "status": "PENDING",


    10

      "tcr_id": "BXXXXXX",


    11

      "failure_reason": "Registration error",


    12

      "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85",


    13

      "brand_score": 42,


    14

      "brand_feedback": [


    15

        "TAX_ID",


    16

        "NONPROFIT"


    17

      ],


    18

      "identity_status": "VERIFIED",


    19

      "russell_3000": true,


    20

      "government_entity": false,


    21

      "tax_exempt_status": "501c3",


    22

      "skip_automatic_sec_vet": true,


    23

      "errors": [],


    24

      "mock": false,


    25

      "links": {


    26

        "brand_vettings": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings",


    27

        "brand_registration_otps": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/SmsOtp"


    28

      }


    29

    }

* * *

## Retrieve a specific BrandRegistration

retrieve-a-specific-brandregistration page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/a2p/BrandRegistrations/{Sid}`

This request returns a specific BrandRegistration. You can use this request to check the `status` of the BrandRegistration.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<BN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Brand Registration resource to fetch.

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve a BrandRegistrationLink to code sample: Retrieve a BrandRegistration

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

    async function fetchBrandRegistrations() {


    11

      const brandRegistration = await client.messaging.v1


    12

        .brandRegistrations("BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .fetch();


    14




    15

      console.log(brandRegistration.sid);


    16

    }


    17




    18

    fetchBrandRegistrations();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",


    4

      "customer_profile_bundle_sid": "BU3344409f7e067e279523808d267e2d85",


    5

      "a2p_profile_bundle_sid": "BU3344409f7e067e279523808d267e2d85",


    6

      "date_created": "2021-01-27T14:18:35Z",


    7

      "date_updated": "2021-01-27T14:18:36Z",


    8

      "brand_type": "STANDARD",


    9

      "status": "PENDING",


    10

      "tcr_id": "BXXXXXX",


    11

      "failure_reason": "Registration error",


    12

      "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85",


    13

      "brand_score": 42,


    14

      "brand_feedback": [


    15

        "TAX_ID",


    16

        "NONPROFIT"


    17

      ],


    18

      "identity_status": "VERIFIED",


    19

      "russell_3000": true,


    20

      "government_entity": false,


    21

      "tax_exempt_status": "501c3",


    22

      "skip_automatic_sec_vet": false,


    23

      "mock": false,


    24

      "errors": [],


    25

      "links": {


    26

        "brand_vettings": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings",


    27

        "brand_registration_otps": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/SmsOtp"


    28

      }


    29

    }

* * *

## Retrieve a list of BrandRegistrations

retrieve-a-list-of-brandregistrations page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/a2p/BrandRegistrations`

This request returns a list of an Account's BrandRegistrations. If working with subaccounts, be sure to use the appropriate Account SID and Auth Token when sending this request.

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

Retrieve a list of BrandRegistrations for an AccountLink to code sample: Retrieve a list of BrandRegistrations for an Account

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

    async function listBrandRegistrations() {


    11

      const brandRegistrations = await client.messaging.v1.brandRegistrations.list({


    12

        limit: 20,


    13

      });


    14




    15

      brandRegistrations.forEach((b) => console.log(b.sid));


    16

    }


    17




    18

    listBrandRegistrations();

### Response

Note about this response

Copy response


    1

    {


    2

      "meta": {


    3

        "page": 0,


    4

        "page_size": 50,


    5

        "first_page_url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "next_page_url": null,


    8

        "key": "data",


    9

        "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations?PageSize=50&Page=0"


    10

      },


    11

      "data": [


    12

        {


    13

          "sid": "BN0044409f7e067e279523808d267e2d85",


    14

          "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",


    15

          "customer_profile_bundle_sid": "BU3344409f7e067e279523808d267e2d85",


    16

          "a2p_profile_bundle_sid": "BU3344409f7e067e279523808d267e2d85",


    17

          "date_created": "2021-01-27T14:18:35Z",


    18

          "date_updated": "2021-01-27T14:18:36Z",


    19

          "brand_type": "STANDARD",


    20

          "status": "APPROVED",


    21

          "tcr_id": "BXXXXXX",


    22

          "failure_reason": "Registration error",


    23

          "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85",


    24

          "brand_score": 42,


    25

          "brand_feedback": [


    26

            "TAX_ID",


    27

            "NONPROFIT"


    28

          ],


    29

          "identity_status": "VERIFIED",


    30

          "russell_3000": true,


    31

          "tax_exempt_status": "501c3",


    32

          "government_entity": false,


    33

          "skip_automatic_sec_vet": false,


    34

          "errors": [],


    35

          "mock": false,


    36

          "links": {


    37

            "brand_vettings": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings",


    38

            "brand_registration_otps": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/SmsOtp"


    39

          }


    40

        }


    41

      ]


    42

    }

* * *

## Update a BrandRegistration

update-a-brandregistration page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/a2p/BrandRegistrations/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<BN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Brand Registration resource to update.

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Update a BrandRegistrationLink to code sample: Update a BrandRegistration

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

    async function updateBrandRegistrations() {


    11

      const brandRegistration = await client.messaging.v1


    12

        .brandRegistrations("BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update();


    14




    15

      console.log(brandRegistration.sid);


    16

    }


    17




    18

    updateBrandRegistrations();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "customer_profile_bundle_sid": "BU3344409f7e067e279523808d267e2d85",


    5

      "a2p_profile_bundle_sid": "BU3344409f7e067e279523808d267e2d85",


    6

      "date_created": "2021-01-27T14:18:35Z",


    7

      "date_updated": "2021-01-27T14:18:36Z",


    8

      "brand_type": "STANDARD",


    9

      "status": "PENDING",


    10

      "tcr_id": "BXXXXXX",


    11

      "failure_reason": "Registration error",


    12

      "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "brand_score": 42,


    14

      "brand_feedback": [


    15

        "TAX_ID",


    16

        "NONPROFIT"


    17

      ],


    18

      "identity_status": "VERIFIED",


    19

      "russell_3000": false,


    20

      "government_entity": false,


    21

      "tax_exempt_status": "501c3",


    22

      "skip_automatic_sec_vet": false,


    23

      "errors": [],


    24

      "mock": false,


    25

      "links": {


    26

        "brand_vettings": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Vettings",


    27

        "brand_registration_otps": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SmsOtp"


    28

      }


    29

    }