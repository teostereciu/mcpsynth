# Secure Media

*Source: https://www.twilio.com/docs/voice/api/secure-media*

---

# Secure Media

Positive FeedbackNegative Feedback

* * *

Secure Media uses encryption to ensure that the call media and associated signaling remains private during transmission. Transport Layer Security (TLS) provides encryption for SIP signaling. Secure Real-time Transport Protocol (SRTP) provides encryption for call content/media packets.

SRTP provides a framework for the encryption of RTP & RTCP. [RFC 4568(link takes you to an external page)](https://tools.ietf.org/html/rfc4568 "RFC 4568"), Session Description Protocol (SDP) Security Description (SDES) for Media Streams, defines such a protocol specifically designed to exchange cryptographic material using a newly defined SDP crypto attribute.

* * *

## Inbound

inbound page anchor

Positive FeedbackNegative Feedback

You can enable or disable Secure Media in your SIP Domain. It is disabled by default.

You can expect the following:

  * **Enabled** : TLS must be used to encrypt SIP messages and SRTP must be used for the media packets. Any non-encrypted calls will be rejected.
  * **Disabled** : RTP must be used for media packets. SIP messages may be sent in the clear or using TLS. Any SRTP encrypted calls will be rejected.


(information)

## Info

  * SRTP supports the following crypto suites: `AES_CM_128_HMAC_SHA1_80` and `AES_CM_128_HMAC_SHA1_32`. Both may be included in an order of preference.
  * The optional master key identifier (MKI) parameter is not supported


* * *

## Outbound

outbound page anchor

Positive FeedbackNegative Feedback

Ensure you configure `secure=true` parameter as part of SIP URI to secure media in SIP outbound calls.

Copy code block


    1

    <?xml version="1.0" encoding="UTF-8"?>


    2

    <Response>


    3

      <Dial>


    4

        <Sip>sip:jack@example.com;secure=true</Sip>


    5

      </Dial>


    6

    </Response>

The default port **5061** will be used for TLS.

(information)

## Info

  * Only a single crypto suite for SRTP will be included: `AES_CM_128_HMAC_SHA1_80`
  * The optional master key identifier (MKI) parameter is not supported


* * *

## TLS/SRTP support with Asterisk

tlssrtp-support-with-asterisk page anchor

Positive FeedbackNegative Feedback

Asterisk ships by default with `chan_sip` driver and works well with Twilio. However, if you have some reason to run `PJSIP` driver with Asterisk, note the following:

Here is [a guide to installing a non-bundled version of PJSIP(link takes you to an external page)](https://asteriskpro.blogspot.com/2017/07/how-to-install-asterisk-13-and-pjsip-on.html "a guide to installing a non-bundled version of PJSIP"). Change the version to **2.5.5** in the steps.

(warning)

## Warning

Asterisk 13.8 cert2 defaults to `PJSIP 2.5` which will not work with Twilio for TLS/SRTP purposes. Non-encrypted calls will still work.

Make sure to use the latest `PJSIP` driver, which at this time is **`2.5.5`**.

You may see following message in your log:

`ERROR[10886]: pjproject:0 <?>: tlsc0x7f217c03 RFC 5922 (section 7.2) does not allow TLS wildcard certificates. Advise your SIP provider, please!`

This message can be ignored.