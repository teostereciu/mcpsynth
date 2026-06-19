# Rate limits

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/usage_limits/*

---

## On this page

  * [Monitoring your request activity](/api-reference/introduction/rate-limits/#monitoring-your-request-activity)
  * [Zendesk Suite plan limits](/api-reference/introduction/rate-limits/#zendesk-suite-plan-limits)
  * [Zendesk Support plan limits](/api-reference/introduction/rate-limits/#zendesk-support-plan-limits)
  * [Endpoint rate limits](/api-reference/introduction/rate-limits/#endpoint-rate-limits)
  * [External Content API limits](/api-reference/introduction/rate-limits/#external-content-api-limits)
  * [Offset pagination limits](/api-reference/introduction/rate-limits/#offset-pagination-limits)
  * [Job limit](/api-reference/introduction/rate-limits/#job-limit)
  * [Apps rate limit](/api-reference/introduction/rate-limits/#apps-rate-limit)
  * [Account limit](/api-reference/introduction/rate-limits/#account-limit)


# Rate limits

## On this page

  * [Monitoring your request activity](/api-reference/introduction/rate-limits/#monitoring-your-request-activity)
  * [Zendesk Suite plan limits](/api-reference/introduction/rate-limits/#zendesk-suite-plan-limits)
  * [Zendesk Support plan limits](/api-reference/introduction/rate-limits/#zendesk-support-plan-limits)
  * [Endpoint rate limits](/api-reference/introduction/rate-limits/#endpoint-rate-limits)
  * [External Content API limits](/api-reference/introduction/rate-limits/#external-content-api-limits)
  * [Offset pagination limits](/api-reference/introduction/rate-limits/#offset-pagination-limits)
  * [Job limit](/api-reference/introduction/rate-limits/#job-limit)
  * [Apps rate limit](/api-reference/introduction/rate-limits/#apps-rate-limit)
  * [Account limit](/api-reference/introduction/rate-limits/#account-limit)


Requests to the Zendesk Support API may be subject to the following limits:

  * Monitoring your request activity
  * Zendesk Suite plan limits
  * Zendesk Support plan limits
  * Endpoint rate limits
  * External Content API limits
  * Offset pagination limits
  * Job limit
  * Apps rate limit
  * Account limit


Notwithstanding the limits specified in this document, the system might still limit requests if it detects an unusual spike in requests from all sources for the account, including internal product requests. For example, this can happen in a denial-of-service attack. See Account limit.

### Monitoring your request activity

You can compare your request activity in the last 24 hours against your rate limit. See [Monitoring API usage against your rate limit](https://support.zendesk.com/hc/en-us/articles/4408836402074-Managing-API-usage-in-your-Zendesk-account#topic_gfl_mz4_jyb).

You can use the following response headers to confirm the account's current rate limit and monitor the number of requests remaining in the current minute:


    X-Rate-Limit: 700X-Rate-Limit-Remaining: 699

If the rate limit is exceeded, the API responds with a [429 Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) status code. The response also has a `Retry-After` header that tells you how many seconds to wait before retrying API requests. Ensure your code handles 429 errors and waits the `Retry-After` interval before retrying requests.

For tips on avoiding and handling 429 errors, see [Best practices for avoiding rate limiting](/documentation/api-basics/best-practices/best-practices-for-avoiding-rate-limiting/).

#### Monitoring the request activity of Ticketing APIs

Ticketing APIs such as the Tickets API and the Users API have additional rate limit headers in their responses. The headers provide more information about the account's current rate limit and the number of requests remaining in the current minute. The 429 errors described above also apply to these responses.


    x-rate-limit: 700ratelimit-limit: 700x-rate-limit-remaining: 699ratelimit-remaining: 699ratelimit-reset: 41zendesk-ratelimit-tickets-index: total=100; remaining=99; resets=41

For examples of how you can use the rate limit information, see [Using rate limit headers in your application](/documentation/ticketing/using-the-zendesk-api/best-practices-for-avoiding-rate-limiting/#using-rate-limit-headers-in-your-application).

### Zendesk Suite plan limits

The following limits apply depending on your Zendesk Suite plan type. Not all rate limits are covered in this table. Make sure to also check the documentation for the specific endpoint for complete details.

Limit| Team| Growth| Professional| Enterprise| Enterprise Plus
---|---|---|---|---|---
Support and Help Center API requests per minute| 200| 400| 400| 700| 2500
Chat API requests per minute| 200| 200| 200| 200| 200
[Custom objects](/api-reference/custom-data/custom-objects/custom_objects/) (soft limit)| 3| 5| 30| 50| 50
Custom object size| 32 KB| 32 KB| 32 KB| 32 KB| 32 KB
[Legacy Custom Objects](/api-reference/custom-data/custom-objects-api/custom-objects-api/), [Profiles](/api-reference/ticketing/users/profiles_api/profiles_api/), and [Events](/api-reference/ticketing/users/events-api/events-api/) API requests per minute| 250| 250| 500| 700| 1000
[Legacy Custom objects](/api-reference/custom-data/custom-objects-api/custom-objects-api/) total| 100,000| 100,000| 250,000| 1,000,000| 25,000,000
[Legacy Relationships](/api-reference/custom-data/custom-objects-api/relationships/) total| 100,000| 100,000| 250,000| 1,000,000| 25,000,000
Legacy Relationship types (soft limit)| 50| 50| 50| 50| 50
[Events](/api-reference/ticketing/users/events-api/events-api/) per month| 150,000| 150,000| 350,000| 750,000| 3,000,000
[Events](/api-reference/ticketing/users/events-api/events-api/) retention period| 90 days| 90 days| 1 year| 1 year| 3 years
[Profiles](/api-reference/ticketing/users/profiles_api/profiles_api/) per person| 20| 20| 20| 20| 20
[Events](/api-reference/ticketing/users/events-api/events-api/) and [Profiles](/api-reference/ticketing/users/profiles_api/profiles_api/) source values| 50| 50| 50| 50| 50
[Events](/api-reference/ticketing/users/events-api/events-api/) and [Profiles](/api-reference/ticketing/users/profiles_api/profiles_api/) type values| 2500| 2500| 2500| 2500| 2500
Zendesk Events Connector - Zendesk events sent per minute| n/a| 5000*| 5000| 5000| 5000

*Only available with the High Volume API add-on.

You can increase the Support and Help Center API rate limits with the High Volume API add-on.

For additional information about limits, see:

  * [Chat API rate limiting](/api-reference/live-chat/introduction/#rate-limiting)
  * [Sunshine limits](/api-reference/custom-data/introduction/#limits)


### Zendesk Support plan limits

The following Support, Help Center, and Custom Objects API rate limits apply on your Zendesk Support plan type.

Plan| Requests per minute
---|---
Essential (legacy)| 10
Team| 200
Professional| 400
Enterprise| 700
High Volume API add-on| 2500

The rate limits for the Help Center API are the same as for the Support API. However, requests to the Help Center API don't count against the rate limit of the Support API, and conversely.

#### High Volume API add-on

The High Volume add-an increases a qualifying plan's limit to 2500 requests per minute to the Support and Help Center APIs. It doesn't add an additional 2500 requests to the plan's limit.

The add-on is available on the Zendesk Suite Growth plan and above, and the Zendesk Support Professional plan and above. You must have a minimum of 10 [agent seats](https://support.zendesk.com/hc/en-us/articles/4408834934554) to purchase this add-on. The add-on is not required on the Zendesk Suite Enterprise Plus plan because the plan has a built-in rate limit of 2500.

Subject to Zendeskâs prior written consent, Zendesk may allow you to increase API usage limits beyond 2500 requests per minute for an additional fee.

### Endpoint rate limits

Some endpoints have their own rate limit. For example, the Update Ticket endpoint has a rate limit of 30 updates to the same ticket by the same agent within a 10-minute period. Zendesk reserves the right to adjust the rate limit for given endpoints to provide a high quality of service for all clients.

Name| Path| Rate limit
---|---|---
List Tickets| GET /api/v2/tickets.json?page={num}| 50 requests per minute where num is over 500
Update Ticket| PUT /api/v2/tickets/{id}.json| 30 updates per 10 minutes per user per ticket. **Note** : This limit applies to any PUT request that updates tickets. For example, a user can have 20 updates on ticket A, 25 updates on ticket B, and 23 updates on ticket C, all within 10 minutes without any issues

100 requests per min per account

300 requests per min per account with the High Volume add-on
Incremental Exports global limit| GET /api/v2/incremental/*| 10 requests per minute
Incremental Exports with High Volume add-on| GET /api/v2/incremental/*| 30 requests per minute
Exporting Views| GET /api/v2/views/{id}/export.json| 100000 requests per hour
Executing Views| GET /api/v2/views/{view_id}/execute.json| 5 requests per minute, per view, per agent
Update User| PUT /api/v2/users/{user_id}| 5 requests per minute per user

1 request per second per account
Create or Update User| POST /api/v2/users/create_or_update| 5 requests per minute per user

1 request per second per account
Export Search Results| GET /api/v2/search/export?query={query}| 100 requests per minute per account
Update Organization| PUT /api/v2/organization/{organization_id}| 5 requests per minute per organization
Create or Reply to Side Conversation| POST /api/v2/tickets/{ticket_id}/side_conversations[/{id}/reply]| 300 requests per 10 minutes
Incremental Side Conversation Events| GET /api/v2/tickets/side_conversations/events| 600 requests per 10 minutes
Get Ticket Attachment Content| GET /attachments/token/{token}/?name={file}| 2500 requests per minute

10 requests per minute per upload for uploads not associated with a ticket or comment.

For information on associating attachments and ticket, see [Upload Files API](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/#upload-files)

### External Content API limits

The Help Center API rate limits apply to the External Content API if no stricter rate limit is documented in the following table.

Help Center API rate limits apply to searches performed through the Help Center API, but they do not apply to searches performed through the UI.

Description| Limit
---|---
External record creation| 770 records per minute
External record size| 10000 bytes per record
External sources| 20
External types| 20
External records| 50000

### Offset pagination limits

API requests that use offset pagination are subject to limits as described in [Pagination](/api-reference/introduction/pagination/#offset-pagination-limit).

### Job limit

Some endpoints such as the [Update Many Tickets](/api-reference/ticketing/tickets/tickets/#update-many-tickets) endpoint queue background jobs to do the work. You can have up to 30 queued or running jobs at once. If you exceed the limit, you will receive a "TooManyJobs" error. Example:


    {  "error":"TooManyJobs",  "description":"Too many UserBulkUpdateJobV2 jobs are currently queued or running. Try again later.",  "current_job_ids":["14b1939441cb2e96d0c0835ede22ce03", ...]}

Zendesk includes a response header you can use to see the current jobs limit and how many additional jobs you can queue before reaching the limit:


    zendesk-ratelimit-inflight-jobs: total=30; remaining=29; resets=60

  * **total** is the maximum number of queued or running jobs allowed concurrently
  * **remaining** is the number of additional jobs you can queue before youâll receive a "TooManyJobs" error
  * **resets** is the number of seconds until the limit resets


### Apps rate limit

API requests made by [Zendesk apps](/documentation/apps/) are subject to an additional rate limit of 100 requests per minute per user per app at the client level, and 700 calls per 5 minutes per user per app at the API level.

### Account limit

Zendesk might limit requests if it detects an unusual spike in requests from all sources for the account, including internal product requests. For example, this can happen in a denial-of-service attack. The account-wide limit is 100,000 requests per minute.

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)