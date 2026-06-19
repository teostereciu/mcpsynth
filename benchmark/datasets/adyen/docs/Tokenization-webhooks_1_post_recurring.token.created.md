# Tokenization-webhooks/1/post/recurring.token.created

*Source: https://docs.adyen.com/api-explorer/Tokenization-webhooks/1/post/recurring.token.created*

---

# Token created
Adyen sends this webhook when a token is created.
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