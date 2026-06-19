# Address Configuration Resource

*Source: https://www.twilio.com/docs/conversations/api/address-configuration-resource*

---

# Address Configuration Resource

Positive FeedbackNegative Feedback

* * *

The Address Configuration resource manages the configurations related to a unique address within the Conversations product, allowing you to specify which addresses should auto-create a [Conversation](/docs/conversations/api/conversation-resource "Conversation") upon receiving an inbound message.
The unique address must be a single address (i.e. a WhatsApp or SMS phone number) that belongs to your Twilio Account.

The configuration can optionally include automatically attaching a [Conversation-scoped Webhook](/docs/conversations/api/conversation-scoped-webhook-resource "Conversation-scoped Webhook") to the auto-created conversations.

* * *

## AddressConfiguration properties

addressconfiguration-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<IG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^IG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") the address belongs to

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

typestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Type of Address, value can be `whatsapp` or `sms`.

* * *

addressstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The unique address to be configured. The address can be a whatsapp address or phone number

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The human-readable name of this configuration, limited to 256 characters. Optional.

* * *

autoCreation

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Auto Creation configuration for the address.

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

An absolute API resource URL for this address configuration.

* * *

addressCountrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code addresses.

* * *

## Create an AddressConfiguration resource

create-an-addressconfiguration-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Configuration/Addresses`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

typeenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Type of Address, value can be `whatsapp` or `sms`.

Possible values:

`sms``whatsapp``messenger``gbm``email``rcs``apple``chat`

* * *

addressstring

required

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The unique address to be configured. The address can be a whatsapp address or phone number

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The human-readable name of this configuration, limited to 256 characters. Optional.

* * *

autoCreation.enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Enable/Disable auto-creating conversations for messages to this address

* * *

autoCreation.typeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`webhook``studio``default`

* * *

autoCreation.conversationServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

autoCreation.webhookUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For type `webhook`, the url for the webhook request.

* * *

autoCreation.webhookMethodenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`get``post`

* * *

autoCreation.webhookFiltersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`

* * *

autoCreation.studioFlowSidSID<FW>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For type `studio`, the studio flow SID where the webhook should be sent to.

Pattern: `^FW[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

autoCreation.studioRetryCountinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For type `studio`, number of times to retry the webhook request

* * *

addressCountrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code addresses.

Select from available examples

Copy code block


    {


      "Address": "+37256123457",


      "Type": "sms",


      "FriendlyName": "My Test Configuration",


      "AutoCreation.Enabled": true,


      "AutoCreation.Type": "webhook",


      "AutoCreation.ConversationServiceSid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "AutoCreation.WebhookUrl": "https://example.com",


      "AutoCreation.WebhookMethod": "post",


      "AutoCreation.WebhookFilters": [


        "onParticipantAdded",


        "onMessageAdded"


      ],


      "AddressCountry": "CA"


    }

Create Address ConfigurationLink to code sample: Create Address Configuration

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

    async function createConfigurationAddress() {


    11

      const addressConfiguration =


    12

        await client.conversations.v1.addressConfigurations.create({


    13

          address: "+37256123457",


    14

          "autoCreation.conversationServiceSid": "ISXXXXXXXXXXXXXXXXXXXXXX",


    15

          "autoCreation.enabled": true,


    16

          "autoCreation.type": "webhook",


    17

          "autoCreation.webhookFilters": ["onParticipantAdded", "onMessageAdded"],


    18

          "autoCreation.webhookMethod": "get",


    19

          "autoCreation.webhookUrl": "https://example.com",


    20

          friendlyName: "My Test Configuration",


    21

          type: "sms",


    22

        });


    23




    24

      console.log(addressConfiguration.sid);


    25

    }


    26




    27

    createConfigurationAddress();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "sid": "IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "address": "+37256123457",


    5

      "type": "sms",


    6

      "friendly_name": "My Test Configuration",


    7

      "address_country": "CA",


    8

      "auto_creation": {


    9

        "enabled": true,


    10

        "type": "webhook",


    11

        "conversation_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    12

        "webhook_url": "https://example.com",


    13

        "webhook_method": "POST",


    14

        "webhook_filters": [


    15

          "onParticipantAdded",


    16

          "onMessageAdded"


    17

        ]


    18

      },


    19

      "date_created": "2016-03-24T21:05:50Z",


    20

      "date_updated": "2016-03-24T21:05:50Z",


    21

      "url": "https://conversations.twilio.com/v1/Configuration/Addresses/IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    22

    }

* * *

## Fetch an AddressConfiguration resource

fetch-an-addressconfiguration-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Configuration/Addresses/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration

Fetch Address ConfigurationLink to code sample: Fetch Address Configuration

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

    async function fetchConfigurationAddress() {


    11

      const addressConfiguration = await client.conversations.v1


    12

        .addressConfigurations("IGXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .fetch();


    14




    15

      console.log(addressConfiguration.sid);


    16

    }


    17




    18

    fetchConfigurationAddress();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "sid": "IGXXXXXXXXXXXXXXXXXXXXXXXX",


    4

      "address": "+37256123457",


    5

      "type": "sms",


    6

      "friendly_name": "My Test Configuration",


    7

      "address_country": "CA",


    8

      "auto_creation": {


    9

        "enabled": true,


    10

        "type": "webhook",


    11

        "conversation_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    12

        "webhook_url": "https://example.com",


    13

        "webhook_method": "POST",


    14

        "webhook_filters": [


    15

          "onParticipantAdded",


    16

          "onMessageAdded"


    17

        ]


    18

      },


    19

      "date_created": "2016-03-24T21:05:50Z",


    20

      "date_updated": "2016-03-24T21:05:50Z",


    21

      "url": "https://conversations.twilio.com/v1/Configuration/Addresses/IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    22

    }

* * *

## Read multiple AddressConfiguration resources

read-multiple-addressconfiguration-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Configuration/Addresses`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

typestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.

* * *

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 50, and the maximum is 50.

Minimum: `1`Maximum: `50`

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

List Address ConfigurationsLink to code sample: List Address Configurations

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

    async function listConfigurationAddress() {


    11

      const addressConfigurations =


    12

        await client.conversations.v1.addressConfigurations.list({ limit: 20 });


    13




    14

      addressConfigurations.forEach((a) => console.log(a.sid));


    15

    }


    16




    17

    listConfigurationAddress();

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

        "first_page_url": "https://conversations.twilio.com/v1/Configuration/Addresses?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Configuration/Addresses?PageSize=50&Page=0",


    8

        "next_page_url": null,


    9

        "key": "address_configurations"


    10

      },


    11

      "address_configurations": [


    12

        {


    13

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "sid": "IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "address": "+37256123457",


    16

          "type": "sms",


    17

          "friendly_name": "My Test Configuration",


    18

          "address_country": "CA",


    19

          "auto_creation": {


    20

            "enabled": true,


    21

            "type": "webhook",


    22

            "conversation_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

            "webhook_url": "https://example.com",


    24

            "webhook_method": "POST",


    25

            "webhook_filters": [


    26

              "onParticipantAdded",


    27

              "onMessageAdded"


    28

            ]


    29

          },


    30

          "date_created": "2016-03-24T21:05:50Z",


    31

          "date_updated": "2016-03-24T21:05:50Z",


    32

          "url": "https://conversations.twilio.com/v1/Configuration/Addresses/IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    33

        },


    34

        {


    35

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

          "sid": "IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",


    37

          "address": "+37256123458",


    38

          "type": "sms",


    39

          "friendly_name": "Studio Test Configuration",


    40

          "address_country": "US",


    41

          "auto_creation": {


    42

            "enabled": false,


    43

            "type": "studio",


    44

            "conversation_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    45

            "studio_flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    46

            "studio_retry_count": 3


    47

          },


    48

          "date_created": "2016-03-24T21:05:50Z",


    49

          "date_updated": "2016-03-24T21:05:50Z",


    50

          "url": "https://conversations.twilio.com/v1/Configuration/Addresses/IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"


    51

        },


    52

        {


    53

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    54

          "sid": "IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",


    55

          "address": "+37256123459",


    56

          "type": "sms",


    57

          "friendly_name": "Default Test Configuration",


    58

          "address_country": "NG",


    59

          "auto_creation": {


    60

            "enabled": true,


    61

            "type": "default"


    62

          },


    63

          "date_created": "2016-03-24T21:05:50Z",


    64

          "date_updated": "2016-03-24T21:05:50Z",


    65

          "url": "https://conversations.twilio.com/v1/Configuration/Addresses/IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac"


    66

        }


    67

      ]


    68

    }

* * *

## Update an AddressConfiguration resource

update-an-addressconfiguration-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Configuration/Addresses/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The human-readable name of this configuration, limited to 256 characters. Optional.

* * *

autoCreation.enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Enable/Disable auto-creating conversations for messages to this address

* * *

autoCreation.typeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`webhook``studio``default`

* * *

autoCreation.conversationServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

autoCreation.webhookUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For type `webhook`, the url for the webhook request.

* * *

autoCreation.webhookMethodenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`get``post`

* * *

autoCreation.webhookFiltersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`

* * *

autoCreation.studioFlowSidSID<FW>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For type `studio`, the studio flow SID where the webhook should be sent to.

Pattern: `^FW[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

autoCreation.studioRetryCountinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

For type `studio`, number of times to retry the webhook request

Copy code block


    {


      "FriendlyName": "My Test Configuration Updated",


      "AutoCreation.Enabled": false,


      "AutoCreation.Type": "studio",


      "AutoCreation.StudioFlowSid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "AutoCreation.StudioRetryCount": 3


    }

Update Address ConfigurationLink to code sample: Update Address Configuration

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

    async function updateConfigurationAddress() {


    11

      const addressConfiguration = await client.conversations.v1


    12

        .addressConfigurations("IGXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .update({


    14

          "autoCreation.enabled": false,


    15

          "autoCreation.studioFlowSid": "FWXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    16

          "autoCreation.studioRetryCount": 3,


    17

          "autoCreation.type": "studio",


    18

          friendlyName: "My Test Configuration Updated",


    19

        });


    20




    21

      console.log(addressConfiguration.sid);


    22

    }


    23




    24

    updateConfigurationAddress();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "sid": "IGXXXXXXXXXXXXXXXXXXXXXXX",


    4

      "address": "+37256123457",


    5

      "type": "sms",


    6

      "friendly_name": "My Test Configuration Updated",


    7

      "address_country": "CA",


    8

      "auto_creation": {


    9

        "enabled": false,


    10

        "type": "studio",


    11

        "conversation_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    12

        "studio_flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

        "studio_retry_count": 3


    14

      },


    15

      "date_created": "2016-03-24T21:05:50Z",


    16

      "date_updated": "2016-03-24T21:05:51Z",


    17

      "url": "https://conversations.twilio.com/v1/Configuration/Addresses/IGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    18

    }

* * *

## Delete an AddressConfiguration resource

delete-an-addressconfiguration-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Configuration/Addresses/{Sid}`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration

Delete Address ConfigurationLink to code sample: Delete Address Configuration

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

    async function deleteConfigurationAddress() {


    11

      await client.conversations.v1


    12

        .addressConfigurations("IGXXXXXXXXXXXXXXXXXXX")


    13

        .remove();


    14

    }


    15




    16

    deleteConfigurationAddress();