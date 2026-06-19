# balanceplatform-webhooks/2/post/balancePlatform.mandate.created

*Source: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/2/post/balancePlatform.mandate.created*

---

# Mandate created
Adyen sends this webhook when adirect debit mandateis created.
Contains event details.
The unique identifier of the balance platform.
Contains information about the mandate that triggered the event.
The unique identifier of the balance account linked to the payment instrument.
Contains information to identify the counterparty.
Contains information about the owner of the counterparty bank account.
The full name of the entity that owns the bank account.
Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.
Contains the bank account details of the counterparty. The fields required in this object depend on the country of the bank account and the currency of the transfer.
The date when the mandate was created.
The unique identifier of the mandate.
The unique identifier of the payment instrument linked to the mandate.
The status of the mandate.
Possible values:pending,approved,cancelled.
The type of mandate. Possible value:bacs.
The date when the mandate was updated.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK