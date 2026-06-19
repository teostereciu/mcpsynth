# Webhooks/1/post/DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION

*Source: https://docs.adyen.com/api-explorer/Webhooks/1/post/DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION*

---

# Direct Debit Notice of Change Notification
A Notice of Change (NOC) was processed for an update to bank account details. This applies to both ACH Direct Debit and EFT PAD transactions.
The timestamp indicating when the webhook was created.
Contains the details of the bank account update.
The Notification of Change information.
The corrected bank account number provided by the receiving bank.
The corrected bank account type provided by the receiving bank. This field is specific to ACH Direct Debit transactions.
Possible values:
- Savings
- Checking
The corrected bank location ID provided by the receiving bank. This field is specific to EFT PAD transactions.
The corrected bank routing number provided by the receiving bank. This field is specific to ACH Direct Debit transactions.
A standard code from the ACH network that specifies the reason for a Notice of Change (e.g., an incorrect account number). This field is specific to ACH Direct Debit transactions.
Possible values:
- C01: Incorrect bank account number.
- C02: Incorrect transit/routing number.
- C03: Incorrect transit/routing number and bank account number.
- C04: Bank account name change.
- C05: Incorrect payment code.
- C06: Incorrect bank account number and transit code.
- C07: Incorrect transit/routing number, bank account number and payment code.
- C09: Incorrect individual ID number.
- C10: Incorrect company name.
- C11: Incorrect company identification.
- C12: Incorrect company name and company ID.
PSP Reference.
Shopper reference.
The environment from which the webhook originated.
The type of notification.
The version of this webhook type.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - No ContentWebhook events are accepted on the basis of the HTTP status code.

#### 200 - No Content