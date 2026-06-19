# onboarding-on-invite-webhooks/1/post/balancePlatform.accountHolder.onboarded

*Source: https://docs.adyen.com/api-explorer/onboarding-on-invite-webhooks/1/post/balancePlatform.accountHolder.onboarded*

---

# Account holder onboarded
Adyen sends this webhook when a new account holder has been onboarded to your balance platform.
The webhook payload contains information about resources created by Adyen for the specified account holder. You can use these resource references and IDs when processing payments or making payouts to your users.
Contains event details.
The unique identifier of the account holder that has been onboarded.
Your description of the account holder.
The unique identifier of the account holder.
Your reference for the account holder.
The time zone of the account holder. For example,Europe/Amsterdam.
Defaults to the time zone of the balance platform if no time zone is set. For possible values, see thelist of time zone codes.
The primary balance account of the account holder.
The default three-characterISO currency codeof the balance account. For example,EUR.
Your description of the balance account.
The unique identifier of the balance account.
Your reference for the balance account.
The unique identifier of the balance platform.
Contains key-value pairs that specify the actions that the account holder can do in your platform. The key is acapabilityrequired for your integration. For example,receivePayments. The value is an object containing the settings for the capability.
Indicates whether the account holder is permitted to use the capability.
Indicates whether the capability is enabled.
Indicates whether the capability is requested.
The status of the verification process for the capability.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
The unique identifier of the legal entity associated with the account holder.
The unique identifier of the merchant account.
The list of stores for the account holder.
The unique identifier of the balance account that the store is associated with.
The unique identifier of the business line that the store is associated with.
Your description of the store.
The unique identifier of the store.
The list of payment methods associated with the store.
Indicates whether the payment method is allowed.
The unique identifier of the payment method.
Your reference for the payment method.
Thepayment method variant.
Verification status of the payment method.
Your reference to recognize the store by.
The unique identifier of thesplit configuration profile.
The list of transfer instruments that the legal entity owns.
The unique identifier of the balance account this transfer instrument is associated with.
The unique identifier of the transfer instrument.
The type of transfer instrument.
Possible value:bankAccount.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK