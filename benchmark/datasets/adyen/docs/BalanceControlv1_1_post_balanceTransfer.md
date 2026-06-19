# BalanceControlv1/1/post/balanceTransfer

*Source: https://docs.adyen.com/api-explorer/BalanceControlv1/1/post/balanceTransfer*

---

# Start a balance transfer
Starts a balance transfer request between merchant accounts. The following conditions must be met before you can successfully transfer balances:
- The source and destination merchant accounts must be under the same company account and legal entity.
- The source merchant account must have sufficient funds.
- The source and destination merchant accounts must have at least one common processing currency.
When sending multiple API requests with the same source and destination merchant accounts, send the requests sequentially andnotin parallel. Some requests may not be processed if the requests are sent in parallel.
The amount of the transfer inminor units.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
A human-readable description for the transfer. You can use alphanumeric characters and hyphens. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.
The unique identifier of the source merchant account from which funds are deducted.
A reference for the balance transfer. If you don't provide this in the request, Adyen generates a unique reference.
Maximum length: 80 characters.
The unique identifier of the destination merchant account from which funds are transferred.
The type of balance transfer. Possible values:tax,fee,terminalSale,credit,debit, andadjustment.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessamountobjectThe amount of the transfer inminor units.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.createdAtstringThe date when the balance transfer was requested.descriptionstringMax length:140A human-readable description for the transfer. You can use alphanumeric characters and hyphens. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.fromMerchantstringThe unique identifier of the source merchant account from which funds are deducted.pspReferencestringAdyen's 16-character string reference associated with the balance transfer.referencestringMax length:80A reference for the balance transfer. If you don't provide this in the request, Adyen generates a unique reference.
Maximum length: 80 characters.statusstringThe status of the balance transfer. Possible values:transferred,failed,error, andnotEnoughBalance.toMerchantstringThe unique identifier of the destination merchant account from which funds are transferred.typestringThe type of balance transfer. Possible values:tax,fee,terminalSale,credit,debit, andadjustment.

#### 200 - OK