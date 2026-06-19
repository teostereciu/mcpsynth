# Verify Return and Error Codes

*Source: https://www.twilio.com/docs/verify/api/v1/return-and-error-codes*

---

# Verify Return and Error Codes

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

Verify v1 API has reached End of Sale. It is now closed to new customers and will be fully deprecated in the future.

For new development, we encourage you to use the [Verify v2 API](/docs/verify/api "Verify v2 API"). v2 has an improved developer experience and new features, including:

  * Twilio server-side SDKs in multiple languages
  * [PSD2](/docs/verify/verifying-transactions-psd2 "PSD2") Secure Customer Authentication Support
  * [Improved Visibility and Insights](/docs/verify/migrating-1x-2x#improved-visibility-and-insights "Improved Visibility and Insights")


Existing customers will not be impacted at this time until Verify v1 API has reached End of Life. For more information about migration, see [Migrating from 1.x to 2.x](/docs/verify/migrating-1x-2x "Migrating from 1.x to 2.x").

As a RESTful API, Twilio's Verify API will return HTTP responses and error codes which will help verify normal behavior as well as contextualize exceptions.

* * *

## Return Codes

return-codes page anchor

Positive FeedbackNegative Feedback

The following status codes are used:

`200`: OK Response is correct. The body of the response will include the data requested.

`400`: Bad Request There was an error with the request. The body of the response will have more info.

`401`: Unauthorized Token is invalid. If your API key is wrong a 401 will be generated. Please check the API key.

`429`: Too Many Requests API usage limit. If you reach API usage limits, a 429 will be returned. Please wait until you pass the limit and attempt the call again.

`503`: Service Unavailable There are multiple possible reasons for a `HTTP 503` error.

  * Internal Twilio error.
  * Your application is accessing an API call you don't have access to.


* * *

## Error Codes

error-codes page anchor

Positive FeedbackNegative Feedback

When the API returns a status other than `200`, we add an error code in the message body. This table enumerates and describes all of the possible error codes.

Error Code| HTTP Status| Error Message| Description| Category
---|---|---|---|---
60000| 400| An error occurred| Default error message when an error is not configured correctly.| ALL
60001| 401| Invalid API key| When the given API key does not correspond to any Authy app| ALL
60002| 400| Invalid request| A request containing invalid parameters or invalid data| ALL
60003| 429| DoS protection| Client has reached the maximum number of requests per time unit on the given endpoint| ALL
60004| 400| Invalid parameter| The given parameter is not valid| ALL
60005| 400| UTF-8 invalid| Client sending request with UTF-8 invalid characters| ALL
60021| 403| Phone verification couldn't be created| An error occurring creating phone verification| Phone Verification
60022| 401| Verification code is incorrect| The phone verification code was incorrect| Phone Verification
60023| 404| Phone verification not found| The phone verification was not found with the parameters given| Phone Verification
60032| 400| SMS was not found| Used by the Feedback API, when a record cannot be found with the given SMS id| Feedback
60033| 400| Phone number is invalid| The phone number or country code is invalid| ALL
60042| 400| Either uuid or country_code and phone number are required| Invalid parameters in phone verification| Phone Verification
60046| 400| Missing dashboard account ids to process| Accounts ids required to be processed| Dashboard
60060| 503| Your account is suspended| Twilio account is suspended| Phone Verification
60064| 403| Failed to enable OneTouch| Can't update application settings on enabling OneTouch| Dashboard
60065| 403| Needs to enable OneTouch first| Application does not have onetouch enabled and is trying to do a OneTouch request| Dashboard
60066| 403| Error saving the callback information| When application settings can't be updated with callback information| Dashboard
60069| 400| Access key can not be saved| Access key invalid on creation| Dashboard
60070| 400| Application was not valid| Application was not valid on create or update| Dashboard
60071| 404| Access key not found| Access key not found| Dashboard
60072| 404| Invalid access key| The access key is wrong| Dashboard
60073| 400| Invalid application API key| Application API Key is wrong| Dashboard
60074| 400| Access key doesn't have enough permissions| The given access key doesn't have enough permissions to access the URL| Dashboard
60075| 400| Delete application failed| Can not delete application due some special condition. i.e. still has users when tried to delete the app or has pending invoices| Dashboard
60078| 403| Invalid country code| The given country code is not valid| ALL
60082| 403| Can not send SMS to landline phone numbers| When trying to send an SMS to a landline phone number| Phone Verification
60083| 403| Phone number not provisioned with any carrier| When trying to send a phone verification to a not provisioned phone number| Phone Verification