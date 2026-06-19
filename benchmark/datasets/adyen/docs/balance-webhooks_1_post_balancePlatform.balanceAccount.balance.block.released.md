# balance-webhooks/1/post/balancePlatform.balanceAccount.balance.block.released

*Source: https://docs.adyen.com/api-explorer/balance-webhooks/1/post/balancePlatform.balanceAccount.balance.block.released*

---

# Blocked funds released
Adyen sends this webhook when funds that were previously blocked are released, making them available. Funds may be blocked for reasons such as:
Collateral for payments: Funds are held to secure loans or payments, and are released upon repayment.
Risk mitigation: Funds are held to cover potential risks like chargebacks, and are released after a set period, such as a return window.
Contains event details.
Contains information about the account holder associated with thebalanceAccount.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The amount released.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Contains information about the associated balance account.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The unique identifier of the balance platform.
The reference of the batch that was released.
The new blocked balance after the funds were released.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The blocked balance before the funds were released.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
The date and time when the amount was released, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK