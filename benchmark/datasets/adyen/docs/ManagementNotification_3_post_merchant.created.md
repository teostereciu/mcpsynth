# ManagementNotification/3/post/merchant.created

*Source: https://docs.adyen.com/api-explorer/ManagementNotification/3/post/merchant.created*

---

# Merchant account created
A merchant accountwas created.
Timestamp for when the webhook was created.
Contains event details.
Key-value pairs that specify the actions that the merchant account can do and its settings. The key is a capability. For example, thesendToTransferInstrumentis the capability required before you can pay out funds to the bank account. The value is an object containing the settings for the capability.
Indicates whether the capability is allowed. Adyen sets this totrueif the verification is successful.
The allowed level of the capability. Some capabilities have different levels which correspond to thresholds. Higher levels may require additional checks and increased monitoring.Possible values:notApplicable,low,medium,high.
The name of the capability. For example,sendToTransferInstrument.
List of entities that have problems with verification. The information includes the details of the errors and the actions that you can take to resolve them.
The ID and the type of entity that has verification errors.
List of document IDs to which the verification errors related to the capabilities correspond to.
The ID of the entity.
The owner of the entity that has an error. For example, if theentity.typeisBankAccount, then theownercontains the details of the legal entity that owns the bank account.
List of document IDs to which the verification errors related to the capabilities correspond to.
The ID of the entity.
The type of entity.
Possible values:LegalEntity,BankAccount, orDocument.
The type of entity.
Possible values:LegalEntity,BankAccount, orDocument.
List of verification errors.
The verification error code.
The verification error message.
The actions that you can take to resolve the verification error.
The remediating action code.
A description of how you can resolve the verification error.
More granular information about the verification error.
The verification error code.
The verification error message.
The type of verification error.
Possible values:invalidInput,dataMissing, andpendingStatus.
The actions that you can take to resolve the verification error.
The remediating action code.
A description of how you can resolve the verification error.
The type of verification error.
Possible values:invalidInput,dataMissing, andpendingStatus.
Indicates whether you requested the capability.
The level that you requested for the capability. Some capabilities have different levels which correspond to thresholds. Higher levels may require additional checks and increased monitoring.Possible values:notApplicable,low,medium,high.
The verification deadline for the capability that will be disallowed if verification errors are not resolved.
The status of the verification checks for the capability.
Possible values:
- pending: Adyen is running the verification.
- invalid: The verification failed. Check if theerrorsarray contains more information.
- valid: The verification was successful.
- rejected: Adyen checked the information and found reasons to not allow the capability.
The unique identifier of the company account.
The unique identifier of thelegal entity.
The unique identifier of the merchant account.
The status of the merchant account.
Possible values:
- PreActive: The merchant account has been created. Users cannot access the merchant account in the Customer Area. The account cannot process payments.
- Active: Users can access the merchant account in the Customer Area. If the company account is alsoActive, then payment processing and payouts are enabled.
- InactiveWithModifications: Users can access the merchant account in the Customer Area. The account cannot process new payments but can still modify payments, for example issue refunds. The account can still receive payouts.
- Inactive: Users can access the merchant account in the Customer Area. Payment processing and payouts are disabled.
- Closed: The account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled.
The environment from which the webhook originated.
Possible values:test,live.
Type of notification.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK