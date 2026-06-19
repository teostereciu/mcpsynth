# Error Codes

*Source: https://www.twilio.com/docs/verify/api/v1/error-codes*

---

# Error Codes

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

* * *

## HTTP Status Codes

http-status-codes page anchor

Positive FeedbackNegative Feedback

Status| Reason
---|---
`200 OK`| Response is correct. The body of the response will include the data requested.
`400 Bad Request`| There was an error with the request. The body of the response will have more info.
`429 Too Many Requests`| API usage limit. If you reach API usage limits, a 429 will be returned. Please wait until you pass the limit and attempt the call again.
`503 Service Unavailable`| There are multiple possible reasons for a `HTTP 503` error.

* * *

## Error Codes

error-codes page anchor

Positive FeedbackNegative Feedback

Status| Error Message
---|---
[60200](/docs/api/errors/60200 "60200")| Invalid parameter
[60201](/docs/api/errors/60201 "60201")| Invalid verification code
[60202](/docs/api/errors/60202 "60202")| Max check attempts reached
[60203](/docs/api/errors/60203 "60203")| Max send attempts reached
[60204](/docs/api/errors/60204 "60204")| Service does not support this feature
[60205](/docs/api/errors/60205 "60205")| SMS is not supported by landline phone number
[60206](/docs/api/errors/60206 "60206")| 'Amount' & 'Payee' params are required
[60207](/docs/api/errors/60207 "60207")| Max rate limits per service reached
[60208](/docs/api/errors/60208 "60208")| Rate limit with that UniqueName already exists
[60209](/docs/api/errors/60209 "60209")| UniqueName format is invalid
[60210](/docs/api/errors/60210 "60210")| Max Buckets per Rate limit reached
[60211](/docs/api/errors/60211 "60211")| Bucket with the given Interval already exists
[60212](/docs/api/errors/60212 "60212")| Too many concurrent requests for phone number
[60213](/docs/api/errors/60213 "60213")| A Messaging Configuration already exists for the given country