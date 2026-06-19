# Notification/6/post/ACCOUNT_HOLDER_VERIFICATION

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/ACCOUNT_HOLDER_VERIFICATION*

---

# Verification results received
Adyen sends this webhook when verification results are available.
The details of the Account Holder verification.
The code of the account holder.
Information on the verification status
A list of the fields required for execution of the check.
The status of the check.
Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.
A summary of the execution of the check.
The code of the check. For possible values, refer toVerification codes.
A description of the check.
The type of check.
Possible values:
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
The unique ID of the legal arrangement that has been verified.
The unique ID of the legal arrangement entity that has been verified.
The unique code of the payout method that has been verified.
The code of the shareholder that has been verified.
The code of the signatory that has been verified.
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