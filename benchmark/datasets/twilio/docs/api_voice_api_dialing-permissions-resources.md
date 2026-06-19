# Dialing Permissions overview

*Source: https://www.twilio.com/docs/voice/api/dialing-permissions-resources*

---

# Dialing Permissions overview

Positive FeedbackNegative Feedback

* * *

Twilio allows you to initiate outbound voice calls to the public telephone network in over 218 countries and territories around the world. Account level Voice Dialing Geographic Permissions allows you to control which of those countries can be called and also block destinations in countries with a high-risk of toll fraud.

For our partners that build and re-sell Twilio powered solutions using subaccounts, Twilio has provided the ability for a subaccount to inherit the dialing permissions of the Master Project. If the partner's customer (the tenant of the subaccount) requires a unique set of permissions, inheritance can be disabled and dialing permissions can be customized on that subaccount.

With this REST API for voice dialing permissions, you can create smart defaults for customers during signup. Smart defaults, aligned with customer needs, leads to more successful calls and more conversions.

* * *

## Countries permissions

countries-permissions page anchor

Positive FeedbackNegative Feedback

Voice dialing permissions are organized into country permissions identified by [ISO(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO") code of corresponding country.

Each [Country]](/docs/voice/api/dialingpermissions-country-resource) describes these three groups of phone number prefixes.

  * **High-risk special numbers** \- number types such as premium numbers, special services, shared cost, and others
  * **High-risk toll fraud numbers** \- narrow number ranges that have a high-risk of international revenue sharing fraud (IRSF) attacks, also known as [toll fraud(link takes you to an external page)](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html "toll fraud").
  * **Low-risk numbers** \- low risk phone numbers


Learn more about the [Countries resource](/docs/voice/api/dialingpermissions-country-resource "Countries resource").

* * *

## BulkCountryUpdates permissions

bulkcountryupdates-permissions page anchor

Positive FeedbackNegative Feedback

Voice dialing permissions for a country are updated by using the [BulkCountryUpdates resource](/docs/voice/api/dialingpermissions-bulkcountryupdate-resource "BulkCountryUpdates resource").

Voice dialing permissions for a country can be updated individually or in a group of countries. Learn more about the [BulkCountryUpdates resource](/docs/voice/api/dialingpermissions-bulkcountryupdate-resource "BulkCountryUpdates resource").

* * *

## HighRiskSpecialPrefixes

highriskspecialprefixes page anchor

Positive FeedbackNegative Feedback

The list of high-risk prefixes from a country is returned by the [HighRiskSpecialPrefixes subresource](/docs/voice/api/dialingpermissions-highriskspecialprefix-resource "HighRiskSpecialPrefixes subresource").

* * *

## Inheritance settings for voice dialing permissions

inheritance-settings-for-voice-dialing-permissions page anchor

Positive FeedbackNegative Feedback

The inheritance settings for voice dialing permissions are represented by the [Settings resource](/docs/voice/api/dialingpermissions-settings-resource "Settings resource").

You can list and update a subaccount's inheritance settings for voice dialing permissions by using the [Settings resource](/docs/voice/api/dialingpermissions-settings-resource "Settings resource").