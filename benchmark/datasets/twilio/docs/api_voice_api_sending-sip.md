# Inbound - Sending SIP to Twilio

*Source: https://www.twilio.com/docs/voice/api/sending-sip*

---

# Inbound - Sending SIP to Twilio

Positive FeedbackNegative Feedback

* * *

## Overview

overview page anchor

Positive FeedbackNegative Feedback

Twilio's Programmable Voice SIP product enables you to use your existing SIP communications infrastructure (e.g. IP-PBX, SBC, etc) to initiate SIP sessions with Twilio and use [TwiML](/docs/voice/twiml "TwiML") and/or the [REST](/docs/usage/api "REST") APIs to create advanced voice applications. Twilio sits in the middle, enabling calls to be routed to your SIP communications infrastructure, PSTN, or to browsers and mobile apps. There are a few short steps to configure Twilio to interoperate with your infrastructure so you can start building and testing your voice app.

Expand image

* * *

## How it works

how-it-works page anchor

Positive FeedbackNegative Feedback

To send SIP to Twilio's cloud you need to create a Twilio SIP Domain. A SIP domain is a custom DNS hostname associated with your Twilio account that can accept SIP traffic. If anyone makes a SIP request using that domain, (e.g. `sip:alice@example.sip.us1.twilio.com`), it will be routed over the internet to Twilio. When a SIP request is received by Twilio, the SIP domain is used to determine the authentication criteria and subsequently used to look up the configured URL to webhook to your application that will provide instructions on how to handle the incoming SIP call. See [how Twilio passes data to your application](/docs/voice/twiml "how Twilio passes data to your application").

* * *

## Getting Started

getting-started page anchor

Positive FeedbackNegative Feedback

Log in to the Console and select Programmable Voice from the vertical menu on the left side of the view which will bring you to the Dashboard. Now navigate to [SIP Domains/Endpoints(link takes you to an external page)](https://www.twilio.com/console/voice/sip/endpoints "SIP Domains/Endpoints").

### Step 1: Create a Twilio Voice SIP Domain/Endpoint

step-1-create-a-twilio-voice-sip-domainendpoint page anchor

Positive FeedbackNegative Feedback

Click on the blue plus symbol on the Voice SIP Endpoints view

#### Friendly Name

friendly-name page anchor

Provide a friendly name for your SIP Domain such as _MyCompanySF_.

#### SIP URI / Domain name

sip-uri--domain-name page anchor

This property allows you to specify a global unique SIP Domain that is used to route the SIP traffic from your infrastructure over the public internet to the correct server hosted by Twilio in the cloud.

A SIP request uses a SIP URI such as the following: `sip:alice@example.sip.twilio.com`)

Twilio processes the incoming request and authenticates it using your chosen authentication method. If the request is authenticated, it webhooks to your requested URL discussed next. All users in the same SIP domain webhook to the same application URL.

Domain names can contain letters, numbers, and "-". By default, every account has its own Twilio Account SID reserved as a domain.

If you try to create a domain that already exists, you will receive an error. Creating subdomains of existing domains is permitted as long as you have already created the original domain. For example: foo.example.sip.twilio.com can only be created if you have already reserved example.sip.twilio.com.

Sub-accounts can create subdomains of any SIP domain in the master account. There exists a [REST API for creating Domains](/docs/voice/sip/api/sip-domain-resource#create-a-sipdomain-resource "REST API for creating Domains").

##### Localized SIP URIs

localized-sip-uris page anchor

If you wish to manually connect to a specific geographic [Edge Location](/docs/global-infrastructure/edge-locations "Edge Location") that is closest to the location of your communications infrastructure, you may do so by pointing your communications infrastructure to any of the following localized SIP URIs:

  * `{example}.sip.ashburn.twilio.com` (North America Virginia)
  * `{example}.sip.umatilla.twilio.com` (North America Oregon)
  * `{example}.sip.dublin.twilio.com` (Europe Ireland)
  * `{example}.sip.frankfurt.twilio.com` (Europe Frankfurt)
  * `{example}.sip.singapore.twilio.com` (Asia Pacific Singapore)
  * `{example}.sip.tokyo.twilio.com` (Asia Pacific Tokyo)
  * `{example}.sip.sao-paulo.twilio.com` (South America São Paulo)
  * `{example}.sip.sydney.twilio.com` (Asia Pacific Sydney)


(information)

## Info

If you are looking for a [list of legacy SIP localized URIs](/docs/global-infrastructure/localized-uris/sip-uris#legacy-sip-uris "list of legacy SIP localized URIs"), visit here.

#### Call Control Configuration

call-control-configuration page anchor

When configuring your SIP Domain in the Console, there is a **CONFIGURE WITH** dropdown that offers multiple options for handling incoming SIP calls. In the **A CALL COMES IN** section, you can select how Twilio should process SIP INVITE.

The following configuration options are available:

##### Webhooks

webhooks page anchor

Specify a URL that points to your web application that Twilio will invoke upon receipt of a SIP INVITE. The URL must [respond with TwiML](/docs/api/twiml/your_response "respond with TwiML") that specifies how to handle the incoming call.

##### Functions

functions page anchor

Use Twilio's Serverless Functions to handle SIP calls without managing infrastructure. Functions provide automatic scaling and regional deployment options.

**Console Configuration:**

When you select "Function" from the "A CALL COMES IN" dropdown, you'll see cascading selections:

  1. **Service** : Choose your Functions Service (or select "Default" for Classic Functions)
  2. **Environment** : Select the deployment environment (e.g., "production", "dev", "staging")
  3. **Function Path** : Select the specific Function to invoke (only public Functions appear here)


**Example Function for SIP:**

Copy code block


    1

    exports.handler = function(context, event, callback) {


    2

      const twiml = new Twilio.twiml.VoiceResponse();


    3




    4

      // Access SIP-specific parameters


    5

      const from = event.From; // SIP URI of caller


    6

      const to = event.To;     // SIP URI called


    7




    8

      // Log the call details


    9

      console.log(`SIP call from ${from} to ${to}`);


    10




    11

      // Handle the call


    12

      twiml.say('Welcome to your SIP-enabled application.');


    13

      twiml.dial('+14155551234');


    14




    15

      return callback(null, twiml);


    16

    };

Learn more: [Twilio Functions documentation](/docs/serverless/functions-assets/functions "Twilio Functions documentation")

(information)

## Info

**Classic vs Modern Functions** : When you see "Default" in the Service dropdown, this refers to Classic Functions (V1). For new implementations, we recommend using Modern Serverless Functions (V2) organized in Services with Environments for better development workflows and version control.

##### TwiML Bins

twiml-bins page anchor

Use TwiML Bins to host static or lightly-templated TwiML on Twilio. This is ideal for prototyping or simple call flows.

**Example TwiML Bin URL:**

Copy code block


    https://twimlets.com/message?Message%5B0%5D=Congratulations!%20You%20just%20made%20your%20first%20call%20with%20Twilio%20SIP.

Learn more: [TwiML Bins documentation](/docs/serverless/twiml-bins "TwiML Bins documentation")

##### Studio Flows

studio-flows page anchor

Point your SIP Domain to a Studio Flow for visual, drag-and-drop call handling. Studio provides a no-code interface for building IVRs, call routing, and more.

**Console Configuration:**

From the **A CALL COMES IN** dropdown, select **Studio** and choose your Flow from the list.

Learn more: [Studio documentation](/docs/studio "Studio documentation")

* * *

**Choosing the Right Option:**

Option| Best For| Complexity| Hosting Required
---|---|---|---
Functions| Most use cases, serverless apps| Low-Medium| No (Twilio-hosted)
Webhooks| Existing web apps, complex logic| Medium-High| Yes (self-hosted)
TwiML Bins| Prototypes, simple static flows| Very Low| No (Twilio-hosted)
Studio| Visual design, no-code solutions| Low| No (Twilio-hosted)

#### Fallback URL

fallback-url page anchor

If the primary call control configuration fails (for instance, due to an invalid TwiML response or timeout), you can optionally specify a Fallback URL to be invoked. This applies to all configuration types above.

#### Status Callback URL

status-callback-url page anchor

Optionally, you can specify a URL for Twilio to send webhook requests to as a call progresses. With inbound SIP calls, you receive only _completed_ status. For details on available callback events, see the [Status Callback documentation](/docs/api/twiml/sip#attributes-status-callback-event "Status Callback documentation").

**Authentication**

Authentication limits access to your SIP Domain from only approved devices and users. You must configure a minimum of either an Access Control List or a credential list. If you configure both, then both ACLs and credential lists are enforced.

#### IP Access Control Lists (ACL)

ip-access-control-lists-acl page anchor

If configured, then Twilio will only accept SIP traffic originating from the IPs in this list - all other packets will be dropped. You must specify a full IP address; no IP wildcarding is supported. IP Access Control Lists can be applied to one or more SIP Domains. There exists a REST API for [creating IP ACLs](/docs/api/voice/ip-access-control-list "creating IP ACLs").

#### Credential Lists

credential-lists page anchor

Credential Lists are sets of usernames and passwords that will be accepted by your SIP Domain.

If a Credential List is configured, your SIP INVITE will be challenged with a 407 Proxy Authentication Required requesting the appropriate user name and password.

For each username, you must set a password that meets the following minimum requirements:

  * Minimum of 12 characters
  * At least one mixed case
  * At least one digit


Twilio does not store the passwords you provide for usernames in cleartext; instead, the passwords are MD5 hashed in accordance with the digest authentication specification. Once a password is set, Twilio does not provide a way to retrieve the stored password. Credential Lists can be applied to one or more SIP Domains.

A REST API exists for [creating Credential Lists](/docs/api/voice/sip-credential-list "creating Credential Lists").

### Step 2: Allow Twilio's IP addresses and ports

step-2-allow-twilios-ip-addresses-and-ports page anchor

Positive FeedbackNegative Feedback

To ensure that your communications infrastructure doesn't block communication, you must update your allow list. See [the SIP documentation](/docs/api/voice/sip-interface#ip-addresses "the SIP documentation") for details.

### Step 3: Start sending SIP to your Twilio SIP Domain

step-3-start-sending-sip-to-your-twilio-sip-domain page anchor

Positive FeedbackNegative Feedback

Now that Twilio's IPs and ports are allowed in your system and your SIP Domain is created, you can send SIP requests to Twilio. If you used the example URL from Step 1, you will hear:

_"Congratulations! You just made your first call with Twilio SIP."_

* * *

## Advanced Features

advanced-features page anchor

Positive FeedbackNegative Feedback

(information)

## Info

SIP custom headers and UUI headers described in this section **only apply to Programmable Voice SIP calls**. If you include custom headers in SIP INVITEs that originate from Bring Your Own Carrier (BYOC) trunks, Twilio doesn't pass those headers to your webhook; they're discarded.

### SIP Custom Headers

sip-custom-headers page anchor

Positive FeedbackNegative Feedback

In order to better integrate with remote SIP applications, Twilio reads the headers that are sent in the SIP request and response messages. Twilio will read any headers beginning with the **X-** and prepended with SipHeader_ prefix in request parameters.

You can send multiple param & value pairs as part of the same header. For example, X-TestHeader: param1=value1;param2=value2;param3=value3

If you send headers **without X-** prefix, Twilio will not read the header. As a result, the header will not be passed in the output.

### UUI (User-to-User Information) Header

uui-user-to-user-information-header page anchor

Positive FeedbackNegative Feedback

In order to pass the contextual information of the caller, customers use UUI (User-to-User Information) header in SIP request messages. You can pass a **UUI (User-to-User) header** through a webhook as a parameter for incoming calls to Twilio.

Simply add UUI SIP header as part of the SIP message before sending it to Twilio. The headers will be sent as request parameters in the webhook requested from your server. For example, if you send the following SIP headers in your SIP message:

_User-to-User: 123456789;encoding=hex_

Twilio will prepend the UUI header with SipHeader_ prefix in webhook request to your server. For example,

_SipHeader_User-to-User "123456789;encoding=hex"_.