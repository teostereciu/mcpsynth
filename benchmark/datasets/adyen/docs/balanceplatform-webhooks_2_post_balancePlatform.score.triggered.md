# balanceplatform-webhooks/2/post/balancePlatform.score.triggered

*Source: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/2/post/balancePlatform.score.triggered*

---

# Score signal triggered
For merchants who opt in to the Score product, Adyen sends this webhook when a score signal is triggered against an account holder.
Contains event details.
Contains information about the account holder.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The status of the account holder.
The automated action(s) taken as a result of the score signals that were triggered.
The unique identifier of the balance platform.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
The ID of the resource.
The score of the identity resulting from the signal(s) that were triggered.
The name(s) of the score signals that were triggered.
The type(s) of the score signals that were triggered.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK