# negative-balance-compensation-warning-webhooks/1/post/balancePlatform.negativeBalanceCompensationWarning.scheduled

*Source: https://docs.adyen.com/api-explorer/negative-balance-compensation-warning-webhooks/1/post/balancePlatform.negativeBalanceCompensationWarning.scheduled*

---

# Negative balance compensation scheduled
Adyen sends this webhook to inform you about a balance account whose balance has been negative for 20 or more days. If you do not transfer funds to that balance account to cover the negative balance before the scheduled compensation date, a transfer is made from your liable balance account on that date.
Contains event details.
The details of the account holder who owns the balance account with a negative balance.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The negative balance amount of the balance account.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The unique identifier of the balance platform.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
The ID of the resource.
The balance account ID of the account that will be used to compensate the balance account whose balance is negative.
The date the balance for the account became negative.
The date when a compensation transfer to the account is scheduled to happen.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - No ContentWebhook events are accepted on the basis of the HTTP status code.

#### 200 - No Content