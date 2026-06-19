# A2P 10DLC - Usecases subresource

*Source: https://www.twilio.com/docs/messaging/api/usapptopersonusecase-resource*

---

# A2P 10DLC - Usecases subresource

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

This API reference supplements the [ISV API onboarding guides](/docs/messaging/compliance/a2p-10dlc/onboarding-isv "ISV API onboarding guides"). Don't use this API resource without following the appropriate guide, or you might experience **delays in registration and unintended fees**.

Usecases is a subresource of [UsAppToPerson (Usa2p)](/docs/messaging/api/usapptoperson-resource "UsAppToPerson \(Usa2p\)") and provides a list of possible A2P 10DLC use cases that a specific brand can use when creating an A2P 10DLC Campaign.

* * *

## Usecase Properties

usecase-properties page anchor

Positive FeedbackNegative Feedback

* * *

## Retrieve a list of A2P 10DLC use cases

retrieve-a-list-of-a2p-10dlc-use-cases page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/Compliance/Usa2p/Usecases`

This request returns a list of possible A2P 10DLC use cases for a given Messaging Service and A2P 10DLC brand.

You need to provide one of the `code` values when creating a [Usa2p resource](/docs/messaging/api/usapptoperson-resource "Usa2p resource").

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") to fetch the resource from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

brandRegistrationSidSID<BN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string to identify the A2P brand.

Pattern: `^BN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve A2P 10DLC use cases for a brandLink to code sample: Retrieve A2P 10DLC use cases for a brand

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

    async function fetchUsAppToPersonUsecase() {


    11

      const usAppToPersonUsecase = await client.messaging.v1


    12

        .services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .usAppToPersonUsecases.fetch({


    14

          brandRegistrationSid: "BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    15

        });


    16




    17

      console.log(usAppToPersonUsecase.usAppToPersonUsecases);


    18

    }


    19




    20

    fetchUsAppToPersonUsecase();

### Response

Note about this response

Copy response


    1

    {


    2

      "us_app_to_person_usecases": [


    3

        {


    4

          "code": "2FA",


    5

          "name": "Two-Factor authentication (2FA)",


    6

          "description": "Two-Factor authentication, one-time use password, password reset",


    7

          "post_approval_required": false


    8

        },


    9

        {


    10

          "code": "ACCOUNT_NOTIFICATION",


    11

          "name": "Account Notification",


    12

          "description": "All reminders, alerts, and notifications. (Examples include: flight delayed, hotel booked, appointment reminders.)",


    13

          "post_approval_required": false


    14

        },


    15

        {


    16

          "code": "AGENTS_FRANCHISES",


    17

          "name": "Agents and Franchises",


    18

          "description": "For brands that have multiple agents, franchises or offices in the same brand vertical, but require individual localised numbers per agent/location/office.",


    19

          "post_approval_required": true


    20

        },


    21

        {


    22

          "code": "CHARITY",


    23

          "name": "Charity",


    24

          "description": "Includes:  5013C Charity\nDoes not include: Religious organizations",


    25

          "post_approval_required": false


    26

        },


    27

        {


    28

          "code": "PROXY",


    29

          "name": "Proxy",


    30

          "description": "Peer-to-peer app-based group messaging with proxy/pooled numbers (For example: GroupMe)\nSupporting personalized services and non-exposure of personal numbers for enterprise or A2P communications. (Examples include: Uber and AirBnb.)",


    31

          "post_approval_required": true


    32

        },


    33

        {


    34

          "code": "CUSTOMER_CARE",


    35

          "name": "Customer Care",


    36

          "description": "All customer care messaging, including account management and support",


    37

          "post_approval_required": false


    38

        },


    39

        {


    40

          "code": "DELIVERY_NOTIFICATION",


    41

          "name": "Delivery Notification",


    42

          "description": "Information about the status of the delivery of a product or service",


    43

          "post_approval_required": false


    44

        },


    45

        {


    46

          "code": "EMERGENCY",


    47

          "name": "Emergency",


    48

          "description": "Notification services designed to support public safety / health during natural disasters, armed conflicts, pandemics and other national or regional emergencies",


    49

          "post_approval_required": true


    50

        },


    51

        {


    52

          "code": "FRAUD_ALERT",


    53

          "name": "Fraud Alert Messaging",


    54

          "description": "Fraud alert notification",


    55

          "post_approval_required": false


    56

        },


    57

        {


    58

          "code": "HIGHER_EDUCATION",


    59

          "name": "Higher Education",


    60

          "description": "For campaigns created on behalf of Colleges or Universities and will also include School Districts etc that fall outside of any \"free to the consumer\" messaging model",


    61

          "post_approval_required": false


    62

        },


    63

        {


    64

          "code": "K12_EDUCATION",


    65

          "name": "K-12 Education",


    66

          "description": "Campaigns created for messaging platforms that support schools from grades K-12 and distance learning centers. This is not for Post-Secondary schools.",


    67

          "post_approval_required": true


    68

        },


    69

        {


    70

          "code": "LOW_VOLUME",


    71

          "name": "Low Volume Mixed",


    72

          "description": "Low throughput, any combination of use-cases. Examples include:  test, demo accounts",


    73

          "post_approval_required": false


    74

        },


    75

        {


    76

          "code": "MARKETING",


    77

          "name": "Marketing",


    78

          "description": "Any communication with marketing and/or promotional content",


    79

          "post_approval_required": false


    80

        },


    81

        {


    82

          "code": "MIXED",


    83

          "name": "Mixed",


    84

          "description": "Mixed messaging reserved for specific consumer service industry",


    85

          "post_approval_required": false


    86

        },


    87

        {


    88

          "code": "POLITICAL",


    89

          "name": "Political",


    90

          "description": "Part of organized effort to influence decision making of specific group. All campaigns to be verified",


    91

          "post_approval_required": false


    92

        },


    93

        {


    94

          "code": "POLLING_VOTING",


    95

          "name": "Polling and voting",


    96

          "description": "Polling and voting",


    97

          "post_approval_required": false


    98

        },


    99

        {


    100

          "code": "PUBLIC_SERVICE_ANNOUNCEMENT",


    101

          "name": "Public Service Announcement",


    102

          "description": "An informational message that is meant to raise the audience awareness about an important issue",


    103

          "post_approval_required": false


    104

        },


    105

        {


    106

          "code": "SECURITY_ALERT",


    107

          "name": "Security Alert",


    108

          "description": "A notification that the security of a system, either software or hardware, has been compromised in some way and there is an action you need to take",


    109

          "post_approval_required": false


    110

        },


    111

        {


    112

          "code": "SOCIAL",


    113

          "name": "Social",


    114

          "description": "Communication within or between closed communities (For example: influencers alerts)",


    115

          "post_approval_required": true


    116

        },


    117

        {


    118

          "code": "SWEEPSTAKE",


    119

          "name": "Sweepstake",


    120

          "description": "Sweepstake",


    121

          "post_approval_required": true


    122

        }


    123

      ]


    124

    }