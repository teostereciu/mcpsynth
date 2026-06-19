# transaction-webhooks/4/post/balancePlatform.transaction.created

*Source: https://docs.adyen.com/api-explorer/transaction-webhooks/4/post/balancePlatform.transaction.created*

---

# Transaction created
After a transfer is booked in a balance account, Adyen sends this webhook with information about the transaction.
Contains details about the event.
Contains information about the account holder associated with thebalanceAccount.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
Contains information about the amount of the transaction.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Contains information about the balance account involved in the transaction.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The unique identifier of the balance platform.
The date the transaction was booked into the balance account.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
Thedescriptionfrom the/transfersrequest.
The unique identifier of the transaction.
Contains information about the payment instrument that was used for the transaction.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The type of wallet that the network token is associated with.
The reference sent to or received from the counterparty.
- For outgoing funds, this is thereferenceForBeneficiaryfrom the/transfersrequest.
- For incoming funds, this is the reference from the sender.

```
referenceForBeneficiary
```
The status of the transaction.
Possible values:
- pending: The transaction is still pending.
- booked: The transaction has been booked to the balance account.
Contains information about the transfer related to the transaction.
The relevant data according to the transfer category.
The ID of the resource.
Thereferencefrom the/transfersrequest. If you haven't provided any, Adyen generates a unique reference.
The date the transfer amount becomes available in the balance account.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of the webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK