# payouts

*Source: https://docs.stripe.com/api/payouts*

---

# Payouts
APayoutobject is created when you receive funds from Stripe, or when youinitiate a payout to either a bank account or debit card of aconnectedStripe account. You can retrieve individual payouts,and list all payouts. Payouts are made onvaryingschedules, depending on your country andindustry.
Related guide:Receiving payouts

# The Payout object

### Attributes
- idstringUnique identifier for the object.
- amountintegerThe amount (incents) that transfers to your bank account or debit card.
- arrival_datetimestampDate that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- statement_descriptornullablestringExtra information about a payout that displays on the user’s bank statement.
- statusstringCurrent status of the payout:paid,pending,in_transit,canceledorfailed. A payout ispendinguntil it’s submitted to the bank, when it becomesin_transit. The status changes topaidif the transaction succeeds, or tofailedorcanceled(within 5 business days). Some payouts that fail might initially show aspaid, then change tofailed.

#### idstring

#### amountinteger

#### arrival_datetimestamp

#### currencyenum

#### descriptionnullablestring

#### metadatanullableobject

#### statement_descriptornullablestring

#### statusstring

### More attributesExpand all
- objectstring
- application_feenullablestringExpandableConnect only
- application_fee_amountnullableintegerConnect only
- automaticboolean
- balance_transactionnullablestringExpandable
- createdtimestamp
- destinationnullablestringExpandable
- failure_balance_transactionnullablestringExpandable
- failure_codenullableenum
- failure_messagenullablestring
- livemodeboolean
- methodstring
- original_payoutnullablestringExpandable
- payout_methodnullablestring
- reconciliation_statusenum
- reversed_bynullablestringExpandable
- source_typestring
- trace_idnullableobject
- typeenum

#### objectstring

#### application_feenullablestringExpandableConnect only

#### application_fee_amountnullableintegerConnect only

#### automaticboolean

#### balance_transactionnullablestringExpandable

#### createdtimestamp

#### destinationnullablestringExpandable

#### failure_balance_transactionnullablestringExpandable

#### failure_codenullableenum

#### failure_messagenullablestring

#### livemodeboolean

#### methodstring

#### original_payoutnullablestringExpandable

#### payout_methodnullablestring

#### reconciliation_statusenum

#### reversed_bynullablestringExpandable

#### source_typestring

#### trace_idnullableobject

#### typeenum

```
{"id":"po_1OaFDbEcg9tTZuTgNYmX0PKB","object":"payout","amount":1100,"arrival_date":1680652800,"automatic":false,"balance_transaction":"txn_1OaFDcEcg9tTZuTgYMR25tSe","created":1680648691,"currency":"usd","description":null,"destination":"ba_1MtIhL2eZvKYlo2CAElKwKu2","failure_balance_transaction":null,"failure_code":null,"failure_message":null,"livemode":false,"metadata":{},"method":"standard","original_payout":null,"reconciliation_status":"not_applicable","reversed_by":null,"source_type":"card","statement_descriptor":null,"status":"pending","type":"bank_account"}
```

```
{"id":"po_1OaFDbEcg9tTZuTgNYmX0PKB","object":"payout","amount":1100,"arrival_date":1680652800,"automatic":false,"balance_transaction":"txn_1OaFDcEcg9tTZuTgYMR25tSe","created":1680648691,"currency":"usd","description":null,"destination":"ba_1MtIhL2eZvKYlo2CAElKwKu2","failure_balance_transaction":null,"failure_code":null,"failure_message":null,"livemode":false,"metadata":{},"method":"standard","original_payout":null,"reconciliation_status":"not_applicable","reversed_by":null,"source_type":"card","statement_descriptor":null,"status":"pending","type":"bank_account"}
```

# Create a payout
To send funds to your own bank account, create a new payout object. YourStripe balancemust cover the payout amount. If it doesn’t, you receive an “Insufficient Funds” error.
If your API key is in test mode, money won’t actually be sent, though every other action occurs as if you’re in live mode.
If you create a manual payout on a Stripe account that uses multiple payment source types, you need to specify the source type balance that the payout draws from. Thebalance objectdetails available and pending amounts by source type.

### Parameters
- amountintegerRequiredA positive integer in cents representing how much to payout.
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- statement_descriptorstringA string that displays on the recipient’s bank or card statement (up to 22 characters). Astatement_descriptorthat’s longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all.

#### amountintegerRequired

#### currencyenumRequired

#### descriptionstring

#### metadataobject

#### statement_descriptorstring

### More parametersExpand all
- destinationstring
- methodstring
- payout_methodstringPreview feature
- source_typestring

#### destinationstring

#### methodstring

#### payout_methodstringPreview feature

#### source_typestring

### Returns
Returns a payout object if no initial errors are present during the payout creation (invalid routing number, insufficient funds, and so on). We initially mark the status of the payout object aspending.

```
curlhttps://api.stripe.com/v1/payouts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1100 \-d currency=usd
```

```
curlhttps://api.stripe.com/v1/payouts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=1100 \-d currency=usd
```

```
{"id":"po_1OaFDbEcg9tTZuTgNYmX0PKB","object":"payout","amount":1100,"arrival_date":1680652800,"automatic":false,"balance_transaction":"txn_1OaFDcEcg9tTZuTgYMR25tSe","created":1680648691,"currency":"usd","description":null,"destination":"ba_1MtIhL2eZvKYlo2CAElKwKu2","failure_balance_transaction":null,"failure_code":null,"failure_message":null,"livemode":false,"metadata":{},"method":"standard","original_payout":null,"reconciliation_status":"not_applicable","reversed_by":null,"source_type":"card","statement_descriptor":null,"status":"pending","type":"bank_account"}
```

```
{"id":"po_1OaFDbEcg9tTZuTgNYmX0PKB","object":"payout","amount":1100,"arrival_date":1680652800,"automatic":false,"balance_transaction":"txn_1OaFDcEcg9tTZuTgYMR25tSe","created":1680648691,"currency":"usd","description":null,"destination":"ba_1MtIhL2eZvKYlo2CAElKwKu2","failure_balance_transaction":null,"failure_code":null,"failure_message":null,"livemode":false,"metadata":{},"method":"standard","original_payout":null,"reconciliation_status":"not_applicable","reversed_by":null,"source_type":"card","statement_descriptor":null,"status":"pending","type":"bank_account"}
```

# Update a payout
Updates the specified payout by setting the values of the parameters you pass. We don’t change parameters that you don’t provide. This request only accepts the metadata as arguments.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### metadataobject

### Returns
Returns the payout object if the update succeeds. This callraisesan errorif update parameters are invalid.

```
curlhttps://api.stripe.com/v1/payouts/po_1OaFDbEcg9tTZuTgNYmX0PKB \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/payouts/po_1OaFDbEcg9tTZuTgNYmX0PKB \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"po_1OaFDbEcg9tTZuTgNYmX0PKB","object":"payout","amount":1100,"arrival_date":1680652800,"automatic":false,"balance_transaction":"txn_1OaFDcEcg9tTZuTgYMR25tSe","created":1680648691,"currency":"usd","description":null,"destination":"ba_1MtIhL2eZvKYlo2CAElKwKu2","failure_balance_transaction":null,"failure_code":null,"failure_message":null,"livemode":false,"metadata":{"order_id":"6735"},"method":"standard","original_payout":null,"reconciliation_status":"not_applicable","reversed_by":null,"source_type":"card","statement_descriptor":null,"status":"pending","type":"bank_account"}
```

```
{"id":"po_1OaFDbEcg9tTZuTgNYmX0PKB","object":"payout","amount":1100,"arrival_date":1680652800,"automatic":false,"balance_transaction":"txn_1OaFDcEcg9tTZuTgYMR25tSe","created":1680648691,"currency":"usd","description":null,"destination":"ba_1MtIhL2eZvKYlo2CAElKwKu2","failure_balance_transaction":null,"failure_code":null,"failure_message":null,"livemode":false,"metadata":{"order_id":"6735"},"method":"standard","original_payout":null,"reconciliation_status":"not_applicable","reversed_by":null,"source_type":"card","statement_descriptor":null,"status":"pending","type":"bank_account"}
```

# Retrieve a payout
Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list. Stripe returns the corresponding payout information.

### Parameters
Noparameters.

### Returns
Returns a payout object if a you provide a valid identifier.raisesAn erroroccurs otherwise.

```
curlhttps://api.stripe.com/v1/payouts/po_1OaFDbEcg9tTZuTgNYmX0PKB \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/payouts/po_1OaFDbEcg9tTZuTgNYmX0PKB \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"po_1OaFDbEcg9tTZuTgNYmX0PKB","object":"payout","amount":1100,"arrival_date":1680652800,"automatic":false,"balance_transaction":"txn_1OaFDcEcg9tTZuTgYMR25tSe","created":1680648691,"currency":"usd","description":null,"destination":"ba_1MtIhL2eZvKYlo2CAElKwKu2","failure_balance_transaction":null,"failure_code":null,"failure_message":null,"livemode":false,"metadata":{},"method":"standard","original_payout":null,"reconciliation_status":"not_applicable","reversed_by":null,"source_type":"card","statement_descriptor":null,"status":"pending","type":"bank_account"}
```

```
{"id":"po_1OaFDbEcg9tTZuTgNYmX0PKB","object":"payout","amount":1100,"arrival_date":1680652800,"automatic":false,"balance_transaction":"txn_1OaFDcEcg9tTZuTgYMR25tSe","created":1680648691,"currency":"usd","description":null,"destination":"ba_1MtIhL2eZvKYlo2CAElKwKu2","failure_balance_transaction":null,"failure_code":null,"failure_message":null,"livemode":false,"metadata":{},"method":"standard","original_payout":null,"reconciliation_status":"not_applicable","reversed_by":null,"source_type":"card","statement_descriptor":null,"status":"pending","type":"bank_account"}
```