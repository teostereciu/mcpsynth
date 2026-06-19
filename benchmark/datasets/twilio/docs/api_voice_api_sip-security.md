# SIP Security Best Practices

*Source: https://www.twilio.com/docs/voice/api/sip-security*

---

# SIP Security Best Practices

Positive FeedbackNegative Feedback

* * *

## Overview

overview page anchor

Positive FeedbackNegative Feedback

When exposing a SIP application to the public internet, you should take special care to secure your applications against unauthorized access. Malicious third parties often look for poorly secured VoIP systems to exploit.

Twilio offers the following mechanisms to secure your application to avoid such situations:

  * [IP Authentication](/docs/voice/api/sip-security#ipauth "IP Authentication")
  * [Digest Authentication](/docs/voice/api/sip-security#digest "Digest Authentication")
  * [TLS](/docs/voice/api/sip-security#tls "TLS")


* * *

## IP Authentication

ipauth page anchor

Positive FeedbackNegative Feedback

One of the easiest and effective ways of securing your SIP application is to only accept SIP traffic from IP endpoints you trust.

To enable this on Twilio, create an IP Access Control List (IP ACL) with the IPs of your endpoints and map it to your SIP Domain. By adding these IPs to your IP ACL, you ensure that only those IPs can connect to your SIP domain. All other traffic is blocked.

IP Access Control Lists can be created with the [SIP tools on Twilio.com](/user/account/sip/ip-acls "SIP tools on Twilio.com") or via the REST API.

(warning)

## Warning

IP Authentication does not protect you when communicating with multi-tenant 3rd party services, such as an IP trunking carrier or a hosted PBX service. Any user with an account on the 3rd party system would be able to send traffic to your application from the same allowed IP. IP authentication alone does not protect against certain other types of attacks. It is highly recommended that you also configure User Credentials.

* * *

## Digest Authentication

digest page anchor

Positive FeedbackNegative Feedback

An additional mechanism to secure your SIP application is to use [digest authentication(link takes you to an external page)](https://en.wikipedia.org/wiki/Digest_access_authentication "digest authentication"). Once enabled, incoming SIP requests will be challenged and you will need to authenticate with a username and password.

To enable this on Twilio, create a Credential List with the set of usernames and passwords that you want to have access to your SIP application and map it to your SIP Domain. Twilio requires that your password meet the following minimum requirements:

  * Minimum number of 12 characters
  * At least one mixed case
  * At least one digit


Credential Lists can be created with the [SIP tools on Twilio.com](/user/account/sip/cls "SIP tools on Twilio.com") or via the [REST API](/docs/api/rest "REST API").

* * *

## TLS

tls page anchor

Positive FeedbackNegative Feedback

Transport Layer Security (TLS) is a mechanism for securing your SIP connections. It is recommended you use TLS as your SIP transport to prevent data being passed between your endpoints and Twilio in cleartext.

Twilio does not currently validate the certificates of the remote clients. This means that you may use self-signed certs on your clients, but this also means that TLS alone is not suitable as an authentication mechanism. At this time, it is only meant to be used to encrypt the SIP communication and does not protect against man-in-the-middle attacks.

* * *

## Application Design

application-design page anchor

Positive FeedbackNegative Feedback

In addition to the above, there are things you can do when you build your application to ensure secure access. First, always use HTTPS and `POST` methods for your URLs. Connecting over HTTPS will prevent your data being passed in cleartext between your app and Twilio.

Second, always [validate the X-Twilio-Signature](/docs/security#validating-requests "validate the X-Twilio-Signature") header passed back in the TwiML requests. This will prevent 3rd parties from interfering with your application's operation data. Twilio SDKs contain a Utilities class that [help you perform request validation](/docs/security#validation-with-libraries "help you perform request validation").

Third, Twilio passes information in the TwiML callbacks that can be used to check that your application is being accessed by the appropriate endpoints. This information is:

  1. The source IP address of the SIP request in the TwiML request.
  2. If using digest authentication, Twilio will pass the username that authenticated.
  3. The "From" header and Request URI of the SIP request.


You can use this information to verify a request or check for anomalous traffic patterns. For example, you can check:

  1. Is the source IP address one of your IP addresses?
  2. Is the user accessing a URI that they shouldn't have access to?
  3. Are you receiving too many requests from a specific From address?