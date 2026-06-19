# Notification/6/post/ACCOUNT_HOLDER_PAYOUT

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/ACCOUNT_HOLDER_PAYOUT*

---

# Paid out to account holder
Adyen sends this notification when apayout requestto an account holder is processed and the payout is scheduled.
Details of the payout to the Account Holder.
The code of the account from which the payout was made.
The code of the Account Holder to which the payout was made.
The payout amounts (per currency).
The three-characterISO currency code.
The amount of the transaction, inminor units.
Details of the Bank Account to which the payout was made.
The bank account number (without separators).
Refer toRequired informationfor details on field requirements.
The type of bank account.
Only applicable to bank accounts held in the USA.
The permitted values are:checking,savings.
Refer toRequired informationfor details on field requirements.
The name of the bank account.
Merchant reference to the bank account.
The unique identifier (UUID) of the Bank Account.
If, during an account holder create or update request, this field is left blank (but other fields provided), a new Bank Account will be created with a procedurally-generated UUID.
If, during an account holder create request, a UUID is provided, the creation of the Bank Account will fail while the creation of the account holder will continue.
If, during an account holder update request, a UUID that is not correlated with an existing Bank Account is provided, the update of the account holder will fail.
If, during an account holder update request, a UUID that is correlated with an existing Bank Account is provided, the existing Bank Account will be updated.
The bank identifier code.
Refer toRequired informationfor details on field requirements.
The city in which the bank branch is located.
Refer toRequired informationfor details on field requirements.
The bank code of the banking institution with which the bank account is registered.
Refer toRequired informationfor details on field requirements.
The name of the banking institution with which the bank account is held.
Refer toRequired informationfor details on field requirements.
The branch code of the branch under which the bank account is registered. The value to be specified in this parameter depends on the country of the bank account:
- United States - Routing number
- United Kingdom - Sort code
- Germany - Bankleitzahl
Refer toRequired informationfor details on field requirements.
The check code of the bank account.
Refer toRequired informationfor details on field requirements.
The two-letter country code in which the bank account is registered.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
Refer toRequired informationfor details on field requirements.
The currency in which the bank account deals.
The permitted currency codes are defined in ISO-4217 (e.g. 'EUR').
The international bank account number.
The IBAN standard is defined in ISO-13616.
Refer toRequired informationfor details on field requirements.
The city of residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
The country code of the country of residence of the bank account owner.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
Refer toRequired informationfor details on field requirements.
The date of birth of the bank account owner.
The date should be in ISO-8601 format yyyy-mm-dd (e.g. 2000-01-31).
The house name or number of the residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
The name of the bank account owner.
Refer toRequired informationfor details on field requirements.
The country code of the country of nationality of the bank account owner.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
Refer toRequired informationfor details on field requirements.
The postal code of the residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
The state of residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
The street name of the residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
If set to true, the bank account is a primary account.
The tax ID number.
Refer toRequired informationfor details on field requirements.
The URL to be used for bank account verification.
This may be generated on bank account creation.
Refer toRequired informationfor details on field requirements.
A description of the payout.
The estimated date of arrival.
Invalid fields list.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
The merchant reference.
The PSP reference of the original payout.
The country code of the bank from which the payout was initiated.
The account number of the bank from which the payout was initiated.
The balance account id to which payment was made
The name of the bank the payout from which the payout was initiated.
The branch code of the bank from which the payout was initiated.
The unique payout identifier.
Speed with which payouts for this account are processed. Permitted values:STANDARD,SAME_DAY.
The payout status.
The message regarding the operation status.
The message code.
The message text.
The status code.
Error information of failed request. No value provided here if no error occurred on processing.
The Adyen code that is mapped to the error message.
A short explanation of the issue.
The date and time when an event has been completed.
The event type of the notification.
The user or process that has triggered the notification.
Indicates whether the notification originated from the live environment or the test environment. If true, the notification originated from the live environment. If false, the notification originated from the test environment.
The PSP reference of the request from which the notification originates.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringSet this parameter to[accepted]to acknowledge that you received a notification from Adyen.

#### 200 - OK