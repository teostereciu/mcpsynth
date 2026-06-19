# Tokenization-webhooks/1/post/recurring.token.alreadyExisting

*Source: https://docs.adyen.com/api-explorer/Tokenization-webhooks/1/post/recurring.token.alreadyExisting*

---

# Token already exists
Adyen sends this webhook when you attempt to create or update a token with details that match an already existing token.
The date and time when the event happened, in ISO 8601 extended format.
Contains event details.
The identifier of the merchant account related to the event that triggered the webhook.
A text description that provides details about the operation, intended for audit purposes.
Your unique shopper reference that is associated with thestoredPaymentMethodId.
The ID of the token.
The type of the payment method.
The environment from which the webhook originated.
Possible values:test,live.
The PSP reference of the event that triggered the webhook.
The type of webhook.
The version of this entity.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK