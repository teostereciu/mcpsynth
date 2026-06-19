# treasury/received_debits

*Source: https://docs.stripe.com/api/treasury/received_debits*

---

# Received Debits
ReceivedDebits represent funds pulled from aFinancialAccount. These are not initiated from the FinancialAccount.

# The ReceivedDebit object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerAmount (in cents) transferred.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- failure_codenullableenumReason for the failure. A ReceivedDebit might fail because the FinancialAccount doesn’t have sufficient funds, is closed, or is frozen.Possible enum valuesaccount_closedFunds can’t be pulled from a closed FinancialAccount.account_frozenFunds can’t be pulled from a frozen FinancialAccount.insufficient_fundsThe FinancialAccount doesn’t have a sufficient balance.international_transactionInternational transactions can’t pull funds from the FinancialAccount.otherFunds can’t be pulled from the FinancialAccount for other reasons.
- financial_accountnullablestringThe FinancialAccount that funds were pulled from.
- hosted_regulatory_receipt_urlnullablestringAhosted transaction receiptURL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.
- initiating_payment_method_detailsobjectDetails about how a ReceivedDebit was created.Show child attributes
- linked_flowsobjectOther flows linked to a ReceivedDebit.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- networkenumThe network used for the ReceivedDebit.
- reversal_detailsnullableobjectDetails describing when a ReceivedDebit might be reversed.Show child attributes
- statusenumStatus of the ReceivedDebit. ReceivedDebits are created with a status of eithersucceeded(approved) orfailed(declined). The failure reason can be found under thefailure_code.Possible enum valuesfailedThe ReceivedDebit was declined, and no Transaction was created.succeededThe ReceivedDebit was approved.
- transactionnullablestringExpandableThe Transaction associated with this object.

#### idstring

#### objectstring

#### amountinteger

#### createdtimestamp

#### currencyenum

#### descriptionstring

#### failure_codenullableenum

[TABLE]
account_closedFunds can’t be pulled from a closed FinancialAccount.
account_frozenFunds can’t be pulled from a frozen FinancialAccount.
insufficient_fundsThe FinancialAccount doesn’t have a sufficient balance.
international_transactionInternational transactions can’t pull funds from the FinancialAccount.
otherFunds can’t be pulled from the FinancialAccount for other reasons.
[/TABLE]

```
account_closed
```

```
account_frozen
```

```
insufficient_funds
```

```
international_transaction
```

#### financial_accountnullablestring

#### hosted_regulatory_receipt_urlnullablestring

#### initiating_payment_method_detailsobject

#### linked_flowsobject

#### livemodeboolean

#### networkenum

#### reversal_detailsnullableobject

#### statusenum

[TABLE]
failedThe ReceivedDebit was declined, and no Transaction was created.
succeededThe ReceivedDebit was approved.
[/TABLE]

#### transactionnullablestringExpandable

```
{"id":"rd_1MtkUY2eZvKYlo2CT9SYD1AF","object":"treasury.received_debit","amount":1000,"created":1680755530,"currency":"usd","description":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkUY2eZvKYlo2CY3s6OQyK","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"debit_reversal":null,"inbound_transfer":null,"issuing_authorization":null,"issuing_transaction":null,"payout":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkUY2eZvKYlo2ChymLKPp5"}
```

```
{"id":"rd_1MtkUY2eZvKYlo2CT9SYD1AF","object":"treasury.received_debit","amount":1000,"created":1680755530,"currency":"usd","description":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkUY2eZvKYlo2CY3s6OQyK","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"debit_reversal":null,"inbound_transfer":null,"issuing_authorization":null,"issuing_transaction":null,"payout":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkUY2eZvKYlo2ChymLKPp5"}
```

# Retrieve a ReceivedDebit
Retrieves the details of an existing ReceivedDebit by passing the unique ReceivedDebit ID from the ReceivedDebit list

### Parameters
Noparameters.

### Returns
Returns a ReceivedDebit object.

```
curlhttps://api.stripe.com/v1/treasury/received_debits/rd_1MtkUY2eZvKYlo2CT9SYD1AF \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/received_debits/rd_1MtkUY2eZvKYlo2CT9SYD1AF \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"rd_1MtkUY2eZvKYlo2CT9SYD1AF","object":"treasury.received_debit","amount":1000,"created":1680755530,"currency":"usd","description":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkUY2eZvKYlo2CY3s6OQyK","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"debit_reversal":null,"inbound_transfer":null,"issuing_authorization":null,"issuing_transaction":null,"payout":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkUY2eZvKYlo2ChymLKPp5"}
```

```
{"id":"rd_1MtkUY2eZvKYlo2CT9SYD1AF","object":"treasury.received_debit","amount":1000,"created":1680755530,"currency":"usd","description":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkUY2eZvKYlo2CY3s6OQyK","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"debit_reversal":null,"inbound_transfer":null,"issuing_authorization":null,"issuing_transaction":null,"payout":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkUY2eZvKYlo2ChymLKPp5"}
```

# List all ReceivedDebits
Returns a list of ReceivedDebits.

### Parameters
- financial_accountstringThe FinancialAccount that funds were pulled from.
- statusenumOnly return ReceivedDebits that have the given status:succeededorfailed.Possible enum valuesfailedThe ReceivedDebit was declined, and no Transaction was created.succeededThe ReceivedDebit was approved.

#### financial_accountstring

#### statusenum

[TABLE]
failedThe ReceivedDebit was declined, and no Transaction was created.
succeededThe ReceivedDebit was approved.
[/TABLE]

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitReceivedDebits, starting after ReceivedDebitstarting_after. Each entry in the array is a separate ReceivedDebit object. If no more ReceivedDebits are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/treasury/received_debits \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkUY2eZvKYlo2CY3s6OQyK \-d limit=3
```

```
curl-G https://api.stripe.com/v1/treasury/received_debits \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkUY2eZvKYlo2CY3s6OQyK \-d limit=3
```

```
{"object":"list","url":"/v1/treasury/received_debits","has_more":false,"data":[{"id":"rd_1MtkUY2eZvKYlo2CT9SYD1AF","object":"treasury.received_debit","amount":1000,"created":1680755530,"currency":"usd","description":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkUY2eZvKYlo2CY3s6OQyK","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"debit_reversal":null,"inbound_transfer":null,"issuing_authorization":null,"issuing_transaction":null,"payout":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkUY2eZvKYlo2ChymLKPp5"}]}
```

```
{"object":"list","url":"/v1/treasury/received_debits","has_more":false,"data":[{"id":"rd_1MtkUY2eZvKYlo2CT9SYD1AF","object":"treasury.received_debit","amount":1000,"created":1680755530,"currency":"usd","description":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkUY2eZvKYlo2CY3s6OQyK","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"debit_reversal":null,"inbound_transfer":null,"issuing_authorization":null,"issuing_transaction":null,"payout":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkUY2eZvKYlo2ChymLKPp5"}]}
```

# Test mode: Create a ReceivedDebitTest helper
Use this endpoint to simulate a test mode ReceivedDebit initiated by a third party. In live mode, you can’t directly create ReceivedDebits initiated by third parties.

### Parameters
- amountintegerRequiredAmount (in cents) to be transferred.
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- financial_accountstringRequiredThe FinancialAccount to pull funds from.
- networkenumRequiredSpecifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See thedocsto learn more about money movement timelines for each network type.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- initiating_payment_method_detailsobjectInitiating payment method details for the object.Show child parameters

#### amountintegerRequired

#### currencyenumRequired

#### financial_accountstringRequired

#### networkenumRequired

#### descriptionstring

#### initiating_payment_method_detailsobject

### Returns
A test mode ReceivedDebit object.

```
curlhttps://api.stripe.com/v1/test_helpers/treasury/received_debits \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1000 \-d currency=usd \-d financial_account=fa_1MtkUY2eZvKYlo2CY3s6OQyK \-d network=ach
```

```
curlhttps://api.stripe.com/v1/test_helpers/treasury/received_debits \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1000 \-d currency=usd \-d financial_account=fa_1MtkUY2eZvKYlo2CY3s6OQyK \-d network=ach
```

```
{"id":"rd_1MtkUY2eZvKYlo2CT9SYD1AF","object":"treasury.received_debit","amount":1000,"created":1680755530,"currency":"usd","description":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkUY2eZvKYlo2CY3s6OQyK","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"debit_reversal":null,"inbound_transfer":null,"issuing_authorization":null,"issuing_transaction":null,"payout":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkUY2eZvKYlo2ChymLKPp5"}
```

```
{"id":"rd_1MtkUY2eZvKYlo2CT9SYD1AF","object":"treasury.received_debit","amount":1000,"created":1680755530,"currency":"usd","description":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkUY2eZvKYlo2CY3s6OQyK","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"debit_reversal":null,"inbound_transfer":null,"issuing_authorization":null,"issuing_transaction":null,"payout":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkUY2eZvKYlo2ChymLKPp5"}
```