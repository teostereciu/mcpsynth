# balanceplatform-webhooks/2/post/balancePlatform.balanceAccount.created

*Source: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/2/post/balancePlatform.balanceAccount.created*

---

# Balance account created
Adyen sends this webhook when you successfullycreate a balance account.
Contains event details.
The unique identifier of theaccount holderassociated with the balance account.
List of balances with the amount and currency.
The balance available for use.
The sum of the transactions that have already been settled.
The three-characterISO currency codeof the balance.
The sum of the transactions that will be settled in the future.
The balance currently held in reserve.
The default three-characterISO currency codeof the balance account. This is the currency displayed on the Balance Account overview page in your Customer Area.
The default value isEUR.
After a balance account is created, you cannot change its default currency.
A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder.
The unique identifier of the balance account.
A set of key and value pairs for general use.
The keys do not have specific names and may be used for storing miscellaneous data as desired.
Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs.
The unique identifier of the account of the migrated account holder in the classic integration.
Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account.
Specifies at what time a sales day ends for this account.
Possible values: Time in"HH:MM"format.HHranges from00to07.MMmust be00.
Default value:"00:00".
Specifies after how many business days the funds in a settlement batch are made available in this balance account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or implementation manager to enable this.
Possible values:1to20, ornull.
Default value:null.
Your reference for the balance account, maximum 150 characters.
The status of the balance account, set toactiveby default.
The time zone of the balance account. For example,Europe/Amsterdam.
Defaults to the time zone of the account holder if no time zone is set. For possible values, see thelist of time zone codes.
The unique identifier of the balance platform.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK