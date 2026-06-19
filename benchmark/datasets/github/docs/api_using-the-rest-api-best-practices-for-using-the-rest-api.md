# Best practices for using the REST API

*Source: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api*

---

# Best practices for using the REST API
Follow these best practices when using GitHub's API.

## In this article

## Avoid polling
You should subscribe to webhook events instead of polling the API for data. This will help your integration stay within the API rate limit. For more information, seeWebhooks documentation.

## Make authenticated requests
Authenticated requests have a higher primary rate limit than unauthenticated requests. To avoid exceeding the rate limit, you should make authenticated requests. For more information, seeRate limits for the REST API.

## Avoid concurrent requests
To avoid exceeding secondary rate limits, you should make requests serially instead of concurrently. To achieve this, you can implement a queue system for requests.

## Pause between mutative requests
If you are making a large number ofPOST,PATCH,PUT, orDELETErequests, wait at least one second between each request. This will help you avoid secondary rate limits.

## Handle rate limit errors appropriately
If you receive a rate limit error, you should stop making requests temporarily according to these guidelines:
- If theretry-afterresponse header is present, you should not retry your request until after that many seconds has elapsed.
- If thex-ratelimit-remainingheader is0, you should not make another request until after the time specified by thex-ratelimit-resetheader. Thex-ratelimit-resetheader is in UTC epoch seconds.
- Otherwise, wait for at least one minute before retrying. If your request continues to fail due to a secondary rate limit, wait for an exponentially increasing amount of time between retries, and throw an error after a specific number of retries.
Continuing to make requests while you are rate limited may result in the banning of your integration.

## Follow redirects
The GitHub REST API uses HTTP redirection where appropriate. You should assume that any
request may result in a redirection. Receiving an HTTP redirection is not an error, and you should follow the redirect.
A301status code indicates permanent redirection. You should repeat your request to the URL specified by thelocationheader. Additionally, you should update your code to use this URL for future requests.
A302or307status code indicates temporary redirection. You should repeat your request to the URL specified by thelocationheader. However, you should not update your code to use this URL for future requests.
Other redirection status codes may be used in accordance with HTTP specifications.

## Do not manually parse URLs
Many API endpoints return URL values for fields in the response body. You should not try to parse these URLs or to predict the structure of future URLs. This can cause your integration to break if GitHub changes the structure of the URL in the future. Instead, you should look for a field that contains the information that you need. For example, the endpoint to create an issue returns anhtml_urlfield with a value likehttps://github.com/octocat/Hello-World/issues/1347and anumberfield with a value like1347. If you need to know the number of the issue, use thenumberfield instead of parsing thehtml_urlfield.
Similarly, you should not try to manually construct pagination queries. Instead, you should use the link headers to determine what pages of results you can request. For more information, seeUsing pagination in the REST API.

## Use conditional requests if appropriate
Most endpoints return anetagheader, and many endpoints return alast-modifiedheader. You can use the values of these headers to make conditionalGETrequests. If the response has not changed, you will receive a304 Not Modifiedresponse. Making a conditional request does not count against your primary rate limit if a304response is returned and the request was made while correctly authorized with anAuthorizationheader.
For example, if a previous request returned anetagheader value of644b5b0155e6404a9cc4bd9d8b1ae730, you can use theif-none-matchheader in a future request:

```
curl -H "Authorization: Bearer YOUR-TOKEN" https://api.github.com/meta --include --header 'if-none-match: "644b5b0155e6404a9cc4bd9d8b1ae730"'
```

```
curl -H "Authorization: Bearer YOUR-TOKEN" https://api.github.com/meta --include --header 'if-none-match: "644b5b0155e6404a9cc4bd9d8b1ae730"'
```
For example, if a previous request returned alast-modifiedheader value ofWed, 25 Oct 2023 19:17:59 GMT, you can use theif-modified-sinceheader in a future request:

```
curl -H "Authorization: Bearer YOUR-TOKEN" https://api.github.com/repos/github/docs --include --header 'if-modified-since: Wed, 25 Oct 2023 19:17:59 GMT'
```

```
curl -H "Authorization: Bearer YOUR-TOKEN" https://api.github.com/repos/github/docs --include --header 'if-modified-since: Wed, 25 Oct 2023 19:17:59 GMT'
```
Conditional requests for unsafe methods, such asPOST,PUT,PATCH, andDELETEare not supported unless otherwise noted in the documentation for a specific endpoint.

## Do not ignore errors
You should not ignore repeated4xxand5xxerror codes. Instead, you should ensure that you are correctly interacting with the API. For example, if an endpoint requests a string and you are passing it a numeric value, you will receive a validation error. Similarly, attempting to access an unauthorized or nonexistent endpoint will result in a4xxerror.
Intentionally ignoring repeated validation errors may result in the suspension of your app for abuse.

## Further reading
- Best practices for using webhooks
- Best practices for creating a GitHub App