# Dialing Permissions - BulkCountryUpdates resource

*Source: https://www.twilio.com/docs/voice/api/dialingpermissions-bulkcountryupdate-resource*

---

# Dialing Permissions - BulkCountryUpdates resource

Positive FeedbackNegative Feedback

* * *

Updates country dialing permissions in bulk.

* * *

## BulkCountryUpdates properties

bulkcountryupdates-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

updateCountinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of countries updated

Default: `0`

* * *

updateRequeststring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A bulk update request to change voice dialing country permissions stored as a URL-encoded, JSON array of update objects. For example : `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`

The **UpdateRequest** parameter is a URL-encoded JSON string that describes an array of objects, each object containing these properties.

  * `high_risk_special_numbers_enabled` ‐ (**Boolean**) Whether high-risk special numbers are enabled
  * `high_risk_tollfraud_numbers_enabled` ‐ (**Boolean**) Whether high-risk toll fraud numbers are enabled
  * `iso_code` ‐ (**string**) The [ISO country code(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO country code")
  * `low_risk_numbers_enabled` ‐ (**Boolean**) Whether low risk numbers are enabled


* * *

## Create a BulkCountryUpdate

create-a-bulkcountryupdate page anchor

Positive FeedbackNegative Feedback

`POST https://voice.twilio.com/v1/DialingPermissions/BulkCountryUpdates`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

updateRequeststring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

URL encoded JSON array of update objects. example : `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`

Copy code block


    {


      "UpdateRequest": "[ { \"iso_code\": \"GB\", \"low_risk_numbers\": \"Enabled\", \"high_risk_special_numbers\":\"Enabled\", \"high_risk_irsf_numbers\": \"Enabled\" } ]"


    }

Create a BulkCountryUpdate to update a single countryLink to code sample: Create a BulkCountryUpdate to update a single country

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

    async function createDialingPermissionsCountryBulkUpdate() {


    11

      const bulkCountryUpdate =


    12

        await client.voice.v1.dialingPermissions.bulkCountryUpdates.create({


    13

          updateRequest: JSON.stringify([


    14

            {


    15

              iso_code: "GB",


    16

              low_risk_numbers_enabled: true,


    17

              high_risk_special_numbers_enabled: true,


    18

              high_risk_tollfraud_numbers_enabled: false,


    19

            },


    20

          ]),


    21

        });


    22




    23

      console.log(bulkCountryUpdate.updateCount);


    24

    }


    25




    26

    createDialingPermissionsCountryBulkUpdate();

### Response

Note about this response

Copy response


    1

    {


    2

      "update_count": 1,


    3

      "update_request": "[{\"iso_code\":\"GB\",\"low_risk_numbers_enabled\":true,\"high_risk_special_numbers_enabled\":true,\"high_risk_tollfraud_numbers_enabled\":false}]"


    4

    }

Create a BulkCountryUpdate to enable low-risk numbers in several countriesLink to code sample: Create a BulkCountryUpdate to enable low-risk numbers in several countries

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

    async function createDialingPermissionsCountryBulkUpdate() {


    11

      const bulkCountryUpdate =


    12

        await client.voice.v1.dialingPermissions.bulkCountryUpdates.create({


    13

          updateRequest: JSON.stringify([


    14

            {


    15

              high_risk_special_numbers_enabled: false,


    16

              high_risk_tollfraud_numbers_enabled: false,


    17

              iso_code: "US",


    18

              low_risk_numbers_enabled: true,


    19

            },


    20

            {


    21

              high_risk_special_numbers_enabled: false,


    22

              high_risk_tollfraud_numbers_enabled: false,


    23

              iso_code: "DE",


    24

              low_risk_numbers_enabled: true,


    25

            },


    26

            {


    27

              high_risk_special_numbers_enabled: false,


    28

              high_risk_tollfraud_numbers_enabled: false,


    29

              iso_code: "FR",


    30

              low_risk_numbers_enabled: true,


    31

            },


    32

            {


    33

              high_risk_special_numbers_enabled: false,


    34

              high_risk_tollfraud_numbers_enabled: false,


    35

              iso_code: "GB",


    36

              low_risk_numbers_enabled: true,


    37

            },


    38

            {


    39

              high_risk_special_numbers_enabled: false,


    40

              high_risk_tollfraud_numbers_enabled: false,


    41

              iso_code: "IN",


    42

              low_risk_numbers_enabled: true,


    43

            },


    44

            {


    45

              high_risk_special_numbers_enabled: false,


    46

              high_risk_tollfraud_numbers_enabled: false,


    47

              iso_code: "IL",


    48

              low_risk_numbers_enabled: true,


    49

            },


    50

            {


    51

              high_risk_special_numbers_enabled: false,


    52

              high_risk_tollfraud_numbers_enabled: false,


    53

              iso_code: "JP",


    54

              low_risk_numbers_enabled: true,


    55

            },


    56

            {


    57

              high_risk_special_numbers_enabled: false,


    58

              high_risk_tollfraud_numbers_enabled: false,


    59

              iso_code: "BR",


    60

              low_risk_numbers_enabled: true,


    61

            },


    62

          ]),


    63

        });


    64




    65

      console.log(bulkCountryUpdate.updateCount);


    66

    }


    67




    68

    createDialingPermissionsCountryBulkUpdate();

### Response

Note about this response

Copy response


    1

    {


    2

      "update_count": 1,


    3

      "update_request": "[{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"US\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"DE\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"FR\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"GB\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"IN\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"IL\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"JP\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"BR\",\"low_risk_numbers_enabled\":true}]"


    4

    }

Create a BulkCountryUpdate to disable high-risk numbers in several countriesLink to code sample: Create a BulkCountryUpdate to disable high-risk numbers in several countries

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

    async function createDialingPermissionsCountryBulkUpdate() {


    11

      const bulkCountryUpdate =


    12

        await client.voice.v1.dialingPermissions.bulkCountryUpdates.create({


    13

          updateRequest: JSON.stringify([


    14

            {


    15

              high_risk_special_numbers_enabled: false,


    16

              high_risk_tollfraud_numbers_enabled: false,


    17

              iso_code: "CU",


    18

              low_risk_numbers_enabled: true,


    19

            },


    20

            {


    21

              high_risk_special_numbers_enabled: false,


    22

              high_risk_tollfraud_numbers_enabled: false,


    23

              iso_code: "LV",


    24

              low_risk_numbers_enabled: true,


    25

            },


    26

            {


    27

              high_risk_special_numbers_enabled: false,


    28

              high_risk_tollfraud_numbers_enabled: false,


    29

              iso_code: "SO",


    30

              low_risk_numbers_enabled: true,


    31

            },


    32

            {


    33

              high_risk_special_numbers_enabled: false,


    34

              high_risk_tollfraud_numbers_enabled: false,


    35

              iso_code: "LT",


    36

              low_risk_numbers_enabled: true,


    37

            },


    38

            {


    39

              high_risk_special_numbers_enabled: false,


    40

              high_risk_tollfraud_numbers_enabled: false,


    41

              iso_code: "GN",


    42

              low_risk_numbers_enabled: true,


    43

            },


    44

            {


    45

              high_risk_special_numbers_enabled: false,


    46

              high_risk_tollfraud_numbers_enabled: false,


    47

              iso_code: "GM",


    48

              low_risk_numbers_enabled: true,


    49

            },


    50

            {


    51

              high_risk_special_numbers_enabled: false,


    52

              high_risk_tollfraud_numbers_enabled: false,


    53

              iso_code: "MV",


    54

              low_risk_numbers_enabled: true,


    55

            },


    56

            {


    57

              high_risk_special_numbers_enabled: false,


    58

              high_risk_tollfraud_numbers_enabled: false,


    59

              iso_code: "EE",


    60

              low_risk_numbers_enabled: true,


    61

            },


    62

            {


    63

              high_risk_special_numbers_enabled: false,


    64

              high_risk_tollfraud_numbers_enabled: false,


    65

              iso_code: "ZW",


    66

              low_risk_numbers_enabled: true,


    67

            },


    68

            {


    69

              high_risk_special_numbers_enabled: false,


    70

              high_risk_tollfraud_numbers_enabled: false,


    71

              iso_code: "TN",


    72

              low_risk_numbers_enabled: true,


    73

            },


    74

          ]),


    75

        });


    76




    77

      console.log(bulkCountryUpdate.updateCount);


    78

    }


    79




    80

    createDialingPermissionsCountryBulkUpdate();

### Response

Note about this response

Copy response


    1

    {


    2

      "update_count": 1,


    3

      "update_request": "[{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"CU\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"LV\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"SO\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"LT\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"GN\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"GM\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"MV\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"EE\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"ZW\",\"low_risk_numbers_enabled\":true},{\"high_risk_special_numbers_enabled\":false,\"high_risk_tollfraud_numbers_enabled\":false,\"iso_code\":\"TN\",\"low_risk_numbers_enabled\":true}]"


    4

    }