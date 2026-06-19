# ManagementNotification/3/post/terminalBoarding.triggered

*Source: https://docs.adyen.com/api-explorer/ManagementNotification/3/post/terminalBoarding.triggered*

---

# Result of terminal boarding
The boarding of a payment terminal succeeded.
Timestamp for when the webhook was created.
Contains event details.
The unique identifier of the company account.
The unique identifier of the merchant account.
The unique identifier of the store.
The unique identifier of the terminal.
The environment from which the webhook originated.
Possible values:test,live.
Type of notification.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK