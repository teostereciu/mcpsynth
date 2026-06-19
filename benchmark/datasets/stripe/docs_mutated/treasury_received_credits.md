# treasury/received_credits

*Source: https://docs.stripe.com/api/treasury/received_credits*

---

# Received Credits
ReceivedCredits represent funds sent to aFinancialAccount(for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

# The ReceivedCredit object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerAmount (in cents) transferred.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- failure_codenullableenumReason for the failure. A ReceivedCredit might fail because the receiving FinancialAccount is closed or frozen.Possible enum valuesaccount_closedFunds can’t be sent to a closed FinancialAccount.account_frozenFunds can’t be sent to a frozen FinancialAccount.international_transactionInternational transactions can’t be sent to FinancialAccount.otherFunds can’t be sent to FinancialAccount for other reasons.
- financial_accountnullablestringThe FinancialAccount that received the funds.
- hosted_regulatory_receipt_urlnullablestringAhosted transaction receiptURL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.
- initiating_payment_method_detailsobjectDetails about the PaymentMethod used to send a ReceivedCredit.Show child attributes
- linked_flowsobjectOther flows linked to a ReceivedCredit.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- networkenumThe rails used to send the funds.Possible enum valuesachcardstripeus_domestic_wire
- reversal_detailsnullableobjectDetails describing when a ReceivedCredit may be reversed.Show child attributes
- statusenumStatus of the ReceivedCredit. ReceivedCredits are created eithersucceeded(approved) orfailed(declined). If a ReceivedCredit is declined, the failure reason can be found in thefailure_codefield.Possible enum valuesfailedThe ReceivedCredit was declined, and no Transaction was created.succeededThe ReceivedCredit was approved.
- transactionnullablestringExpandableThe Transaction associated with this object.

#### idstring

#### objectstring

#### amountinteger

#### createdtimestamp

#### currencyenum

#### descriptionstring

#### failure_codenullableenum

[TABLE]
account_closedFunds can’t be sent to a closed FinancialAccount.
account_frozenFunds can’t be sent to a frozen FinancialAccount.
international_transactionInternational transactions can’t be sent to FinancialAccount.
otherFunds can’t be sent to FinancialAccount for other reasons.
[/TABLE]

```
account_closed
```

```
account_frozen
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

[TABLE]
ach
card
stripe
us_domestic_wire
[/TABLE]

```
us_domestic_wire
```

#### reversal_detailsnullableobject

#### statusenum

[TABLE]
failedThe ReceivedCredit was declined, and no Transaction was created.
succeededThe ReceivedCredit was approved.
[/TABLE]

#### transactionnullablestringExpandable

```
{"id":"rc_1MtkSr2eZvKYlo2CcysvUbEw","object":"treasury.received_credit","amount":1000,"created":1680755425,"currency_code":"usd","notes":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkSr2eZvKYlo2CsJozwFWD","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"credit_reversal":null,"issuing_authorization":null,"issuing_transaction":null,"source_flow":null,"source_flow_type":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}
```

```
{"id":"rc_1MtkSr2eZvKYlo2CcysvUbEw","object":"treasury.received_credit","amount":1000,"created":1680755425,"currency_code":"usd","notes":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkSr2eZvKYlo2CsJozwFWD","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"credit_reversal":null,"issuing_authorization":null,"issuing_transaction":null,"source_flow":null,"source_flow_type":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}
```

# Retrieve a ReceivedCredit
Retrieves the details of an existing ReceivedCredit by passing the unique ReceivedCredit ID from the ReceivedCredit list.

### Parameters
Noparameters.

### Returns
Returns a ReceivedCredit object.

```
curlhttps://api.stripe.com/v1/treasury/received_credits/rc_1MtkSr2eZvKYlo2CcysvUbEw \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/received_credits/rc_1MtkSr2eZvKYlo2CcysvUbEw \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"rc_1MtkSr2eZvKYlo2CcysvUbEw","object":"treasury.received_credit","amount":1000,"created":1680755425,"currency_code":"usd","notes":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkSr2eZvKYlo2CsJozwFWD","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"credit_reversal":null,"issuing_authorization":null,"issuing_transaction":null,"source_flow":null,"source_flow_type":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}
```

```
{"id":"rc_1MtkSr2eZvKYlo2CcysvUbEw","object":"treasury.received_credit","amount":1000,"created":1680755425,"currency_code":"usd","notes":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkSr2eZvKYlo2CsJozwFWD","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"credit_reversal":null,"issuing_authorization":null,"issuing_transaction":null,"source_flow":null,"source_flow_type":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}
```

# List all ReceivedCredits
Returns a list of ReceivedCredits.

### Parameters
- financial_accountstringThe FinancialAccount that received the funds.
- linked_flowsobjectOnly return ReceivedCredits described by the flow.Show child parameters
- statusenumOnly return ReceivedCredits that have the given status:succeededorfailed.Possible enum valuesfailedThe ReceivedCredit was declined, and no Transaction was created.succeededThe ReceivedCredit was approved.

#### financial_accountstring

#### linked_flowsobject

#### statusenum

[TABLE]
failedThe ReceivedCredit was declined, and no Transaction was created.
succeededThe ReceivedCredit was approved.
[/TABLE]

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitReceivedCredits, starting after ReceivedCreditstarting_after. Each entry in the array is a separate ReceivedCredit object. If no more ReceivedCredits are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/treasury/received_credits \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \-d limit=3
```

```
curl-G https://api.stripe.com/v1/treasury/received_credits \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \-d limit=3
```

```
{"object":"list","url":"/v1/treasury/received_credits","has_more":false,"data":[{"id":"rc_1MtkSr2eZvKYlo2CcysvUbEw","object":"treasury.received_credit","amount":1000,"created":1680755425,"currency_code":"usd","notes":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkSr2eZvKYlo2CsJozwFWD","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"credit_reversal":null,"issuing_authorization":null,"issuing_transaction":null,"source_flow":null,"source_flow_type":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}]}
```

```
{"object":"list","url":"/v1/treasury/received_credits","has_more":false,"data":[{"id":"rc_1MtkSr2eZvKYlo2CcysvUbEw","object":"treasury.received_credit","amount":1000,"created":1680755425,"currency_code":"usd","notes":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkSr2eZvKYlo2CsJozwFWD","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"credit_reversal":null,"issuing_authorization":null,"issuing_transaction":null,"source_flow":null,"source_flow_type":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}]}
```

# Test mode: Create a ReceivedCreditTest helper
Use this endpoint to simulate a test mode ReceivedCredit initiated by a third party. In live mode, you can’t directly create ReceivedCredits initiated by third parties.

### Parameters
- amountintegerRequiredAmount (in cents) to be transferred.
- currencyenumRequiredThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- financial_accountstringRequiredThe FinancialAccount to send funds to.
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
A test mode ReceivedCredit object.

```
curlhttps://api.stripe.com/v1/test_helpers/treasury/received_credits \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1000 \-d currency_code=usd \-d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \-d network=ach
```

```
curlhttps://api.stripe.com/v1/test_helpers/treasury/received_credits \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1000 \-d currency_code=usd \-d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \-d network=ach
```

```
{"id":"rc_1MtkSr2eZvKYlo2CcysvUbEw","object":"treasury.received_credit","amount":1000,"created":1680755425,"currency_code":"usd","notes":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkSr2eZvKYlo2CsJozwFWD","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"credit_reversal":null,"issuing_authorization":null,"issuing_transaction":null,"source_flow":null,"source_flow_type":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}
```

```
{"id":"rc_1MtkSr2eZvKYlo2CcysvUbEw","object":"treasury.received_credit","amount":1000,"created":1680755425,"currency_code":"usd","notes":"Stripe Test","failure_code":null,"financial_account":"fa_1MtkSr2eZvKYlo2CsJozwFWD","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw","initiating_payment_method_details":{"billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"bank_name":"STRIPE TEST BANK","last4":"6789","routing_number":"110000000"}},"linked_flows":{"credit_reversal":null,"issuing_authorization":null,"issuing_transaction":null,"source_flow":null,"source_flow_type":null},"livemode":false,"network":"ach","reversal_details":{"deadline":1681084800,"restricted_reason":null},"status":"succeeded","transaction":"trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}
```