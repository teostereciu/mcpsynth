# balanceplatform-webhooks/2/post/balancePlatform.cardorder.updated

*Source: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/2/post/balancePlatform.cardorder.updated*

---

# Card order updated
Adyen sends this webhook when there is an update in card order status.
Contains event details.
The unique identifier of the balance platform.
The status of the card delivery.
Possible values:created,rejected,processing,produced,shipped,delivered,notApplicable,unknown.
An error message.
The status of the PIN delivery.
The tracking number of the PIN delivery.
The unique identifier of the card order item.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
The ID of the resource.
The unique identifier of the payment instrument related to the card order item.
Contains information about the status of the PIN delivery.
An error message.
The status of the PIN delivery.
The tracking number of the PIN delivery.
The shipping method used to deliver the card or the PIN.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK