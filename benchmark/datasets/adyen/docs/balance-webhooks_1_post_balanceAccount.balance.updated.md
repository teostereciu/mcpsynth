# balance-webhooks/1/post/balanceAccount.balance.updated

*Source: https://docs.adyen.com/api-explorer/balance-webhooks/1/post/balanceAccount.balance.updated*

---

# Balance updated
Adyen sends this webhook when the specified balance type reaches or drops below the threshold you configured.
Contains event details.
The unique identifier of the balance account.
The unique identifier of the balance platform.
The list balance types.
The balance that is available for use.
The sum of transactions that have already been settled.
The sum of transactions that will be settled in the future.
The balance currently held in reserve.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
The three-characterISO currency code.
The unique identifier of the balance webhook setting.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK