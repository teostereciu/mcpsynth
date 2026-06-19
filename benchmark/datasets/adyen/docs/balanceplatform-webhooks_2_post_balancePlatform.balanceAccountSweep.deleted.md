# balanceplatform-webhooks/2/post/balancePlatform.balanceAccountSweep.deleted

*Source: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/2/post/balancePlatform.balanceAccountSweep.deleted*

---

# Sweep deleted
Adyen sends this webhook when you successfullydelete a sweep.
Contains event details.
The unique identifier of the balance account for which the sweep was configured.
The unique identifier of the balance platform.
Contains information about the sweep resource that triggered the event.
The type of transfer that results from the sweep.
Possible values:
- bank: Sweep to atransfer instrument.
- internal: Transfer to anotherbalance accountwithin your platform.
Required when settingpriorities.
The destination or the source of the funds, depending on the sweeptype.
Either abalanceAccountId,transferInstrumentId, ormerchantAccountis required.
The unique identifier of the destination or sourcebalance account.
If you are updating the counterparty from a transfer instrument to a balance account, settransferInstrumentIdtonull.
The merchant account that will be the source of funds.
You can only use this parameter with sweeps oftypepulland if you are processing payments with Adyen.
The unique identifier of the destination or sourcetransfer instrumentdepending on the sweeptype
. To set up automated top-up sweeps to balance accounts in yourmarketplaceorplatform, use this parameter in combination with amerchantAccountand a sweeptypeofpull.
Top-up sweeps start a direct debit request from the source transfer instrument. Contact Adyen Support to enable this feature.> If you are updating the counterparty from a balance account to a transfer instrument, setbalanceAccountIdtonull.
The three-characterISO currency codein uppercase. For example,EUR.
The sweep currency must match any of thebalances currencies.
The message that will be used in the sweep transfer's description body with a maximum length of 140 characters.
If the message is longer after replacing placeholders, the message will be cut off at 140 characters.
The unique identifier of the sweep.
The list of priorities for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. You can provide multiple priorities, ordered by your preference. Adyen will try to pay out using the priorities in the given order. If the first priority is not currently supported or enabled for your platform, the system will try the next one, and so on.
The request will be accepted as long asat least oneof the provided priorities is valid (i.e., supported by Adyen and activated for your platform). For example, if you provide["wire","regular"], andwireis not supported butregularis, the request will still be accepted and processed.
Possible values:
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).
Setcategorytobank. For more details, see optional priorities setup formarketplacesorplatforms.
The reason for disabling the sweep.
The human readable reason for disabling the sweep.
Your reference for the sweep configuration.
The reference sent to or received from the counterparty. Only alphanumeric characters are allowed.
The schedule when thetriggerAmountis evaluated. If the balance meets the threshold, funds are pushed out of or pulled in to the balance account.
Acron expressionthat is used to set the sweep schedule. The schedule uses the time zone of the balance account.
For example,30 17 * * MONschedules a sweep every Monday at 17:30.
The expression must have five values separated by a single space in the following order:
- Minute:0-59
- Hour:0-23
- Day of the month:1-31
- Month:1-12orJAN-DEC
- Day of the week:0-7(0 and 7 are Sunday) orMON-SUN.
The following non-standard characters are supported:*,L,#,Wand/. Seecrontab gurufor more examples.
Required whentypeiscron.
The schedule type.
Possible values:
- cron: push out funds based on acronExpression.
- daily: push out funds daily at 07:00 AM CET.
- weekly: push out funds every Monday at 07:00 AM CET.
- monthly: push out funds every first of the month at 07:00 AM CET.
- balance: execute the sweep instantly if thetriggerAmountis reached.
The status of the sweep. If not provided, by default, this is set toactive.
Possible values:
- active:  the sweep is enabled and funds will be pulled in or pushed out based on the defined configuration.
- inactive: the sweep is disabled and cannot be triggered.
The amount that must be pushed out or pulled in. You can configure eithersweepAmountortargetAmount, not both.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The amount that must be available in the balance account after the sweep. You can configure eithersweepAmountortargetAmount, not both.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The threshold amount that triggers the sweep. If not provided, by default, the amount is set to zero. ThetriggerAmountis evaluated according to the specifiedschedule.type.
- Fortypepull, if the balance is less than or equal to thetriggerAmount, funds are pulled in to the balance account.
- Fortypepush, if the balance is more than or equal to thetriggerAmount, funds are pushed out of the balance account.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The direction of sweep, whether pushing out or pulling in funds to the balance account. If not provided, by default, this is set topush.
Possible values:
- push:push out fundsto a destination balance account or transfer instrument.
- pull:pull in fundsfrom a source merchant account, transfer instrument, or balance account.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK