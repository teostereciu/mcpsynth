# SIP Interface over Twilio Interconnect

*Source: https://www.twilio.com/docs/voice/api/sip-interconnect*

---

# SIP Interface over Twilio Interconnect

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

**On 21 February 2024 Twilio will be updating the media IPs and port ranges for calls in all regions to 168.86.128.0/18 and expanding the UDP port range to 10000-60000.** Old IP and port ranges will no longer accept or send traffic after this date.

[Twilio Interconnect](/docs/interconnect "Twilio Interconnect") allows you to connect your SIP infrastructure using a private connection (e.g. VPN, cross-connect) to a Twilio SIP Interface.

* * *

## Configure your SIP Interface over Twilio Interconnect

configure-your-sip-interface-over-twilio-interconnect page anchor

Positive FeedbackNegative Feedback

### Sending SIP to Twilio

sip-out page anchor

Positive FeedbackNegative Feedback

To connect over Twilio Interconnect, point your communications infrastructure to the following localized SIP Domain URIs:

SIP Domain URI| Interconnect Exchange
---|---
`{example}.sip.ashburn-ix.twilio.com`| Ashburn, Virginia, United States
`{example}.sip.san-jose-ix.twilio.com`| San Jose, California, United States
`{example}.sip.london-ix.twilio.com`| London, United Kingdom
`{example}.sip.frankfurt-ix.twilio.com`| Frankfurt, Germany
`{example}.sip.singapore-ix.twilio.com`| Singapore
`{example}.sip.tokyo-ix.twilio.com`| Tokyo, Japan
`{example}.sip.sydney-ix.twilio.com`| Sydney, Australia
`{example}.sip.sao-paulo-ix.twilio.com`| São Paulo, Brazil

(information)

## Info

`{example}` will be replaced by the unique part of the SIP Domain that you previously configured. Refer to [Programmable SIP Domains(link takes you to an external page)](https://www.twilio.com/console/voice/sip/endpoints "Programmable SIP Domains") for SIP Domain setup. For example, if your SIP Domain was `example.sip.twilio.com` , then it would be `example.sip.london-ix.twilio.com` (for the London IX).

(information)

## Info

If you are looking for the [legacy Interconnect SIP Domain URI list, visit here](/docs/global-infrastructure/localized-uris/interconnect-sip-uris#legacy-interconnect-sip-uris "legacy Interconnect SIP Domain URI list, visit here"). eg: `{example}.sip.de1.twilio.com`

### Receiving SIP from Twilio over Twilio Interconnect

sip-in page anchor

Positive FeedbackNegative Feedback

In order for your SIP Endpoint to receive calls from Twilio, you will use the same TwiML or REST API calls you use today. The only difference is that you will now be specifying your Twilio Interconnect Connection, by including the `edge` parameter in the URI with the value of the Twilio [Interconnect Edge Location](/docs/global-infrastructure/edge-locations#private-interconnect "Interconnect Edge Location") where your private connection is configured, for example:

Copy code block


    1

        <Response>


    2

            <Dial>


    3

                <Sip>


    4

                    sip:yourusername@example.com;edge={EDGE_LOCATION}


    5

                </Sip>


    6

            </Dial>


    7

        </Response>


    8

You may also use the deprecated `tnx` parameter in the URI with the SID value of the desired Twilio Interconnect connection, however, it is preferred that you use the `edge` parameter as documented above. An example of using the `tnx` parameter:

Copy code block


    1

        <Response>


    2

            <Dial>


    3

                <Sip>


    4

                    sip:yourusername@example.com;tnx={TNX_SID}


    5

                </Sip>


    6

            </Dial>


    7

        </Response>


    8

### Media IP addresses using Twilio Interconnect

ipwhitelist-tnx page anchor

Positive FeedbackNegative Feedback

**Interconnect Connections - Global Media IP Range**

The Interconnect Connections Destination IP Ranges and Port Ranges are now identical across all locations:

**Secure Media (ICE/STUN/SRTP) Edge Locations**| **Protocol**| **Source IP**| **Source Port †**| **Destination IP Ranges**| **Destination Port Range**
---|---|---|---|---|---
sydney-ix (**au1-ix**)
sao-paulo-ix (**br1-ix**)
london-ix (**ie1-ix**)
frankfurt-ix (**de1-ix**)
tokyo-ix (**jp1-ix**)
singapore-ix (**sg1-ix**)
ashburn-ix (**us1-ix**)
san-jose-ix (**us2-ix**)
roaming (**gll-ix**)| UDP| ANY| ANY| 168.86.128.0/18| 10,000 - 60,000

† The SDK will select any available port from the ephemeral range. On most machines, this means the port range 1,024 to 65,535.

### SIGNALLING IP addresses using Twilio Interconnect

ipwhitelist-tnx-1 page anchor

Positive FeedbackNegative Feedback

We strongly encourage you to allow all of Twilio's following IP address ranges and ports on your firewall for SIP signalling traffic. This is important if you have Numbers in different regions and for resilience purposes (e.g. if North America Virginia gateways are down, then North America Oregon gateways will be used).

#### North America Virginia Interconnect Gateways

north-america-virginia-interconnect-gateways page anchor

Copy code block


    1

        208.78.112.64


    2

        208.78.112.65


    3

        208.78.112.66


    4

        Ports: 5060 (UDP/TCP), 5061 (TLS)


    5

#### North America Oregon Interconnect Gateways

north-america-oregon-interconnect-gateways page anchor

Copy code block


    1

        67.213.136.64


    2

        67.213.136.65


    3

        67.213.136.66


    4

        Ports: 5060 (UDP/TCP), 5061 (TLS)


    5

#### Europe London Interconnect Gateways

europe-london-interconnect-gateways page anchor

Copy code block


    1

        185.187.132.68


    2

        185.187.132.69


    3

        185.187.132.70


    4

        Ports: 5060 (UDP/TCP), 5061 (TLS)


    5

#### Europe Frankfurt Interconnect Gateways

europe-frankfurt-interconnect-gateways page anchor

Copy code block


    1

        185.194.136.64


    2

        185.194.136.65


    3

        185.194.136.66


    4

        Ports: 5060 (UDP/TCP), 5061 (TLS)


    5

#### Asia Pacific Singapore Interconnect Gateways

asia-pacific-singapore-interconnect-gateways page anchor

Copy code block


    1

        103.75.151.68


    2

        103.75.151.69


    3

        103.75.151.70


    4

       Ports: 5060 (UDP/TCP), 5061 (TLS)


    5

#### Asia Pacific Tokyo Interconnect Gateways

asia-pacific-tokyo-interconnect-gateways page anchor

Copy code block


    1

     103.144.142.68


    2

     103.144.142.69


    3

     103.144.142.70


    4

        Ports: 5060 (UDP/TCP), 5061 (TLS)


    5

#### Asia Pacific Sydney Interconnect Gateways

asia-pacific-sydney-interconnect-gateways page anchor

Copy code block


    1

     103.146.214.68


    2

     103.146.214.69


    3

     103.146.214.70


    4

        Ports: 5060 (UDP/TCP), 5061 (TLS)

#### South America São Paulo Interconnect Gateways

south-america-são-paulo-interconnect-gateways page anchor

Copy code block


    1

     159.183.255.68


    2

     159.183.255.69


    3

     159.183.255.70


    4

        Ports: 5060 (UDP/TCP), 5061 (TLS)


    5