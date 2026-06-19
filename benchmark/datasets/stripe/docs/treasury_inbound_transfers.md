# treasury/inbound_transfers

*Source: https://docs.stripe.com/api/treasury/inbound_transfers*

---

# Inbound Transfers
UseInboundTransfersto add funds to yourFinancialAccountvia a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.
Related guide:Moving money with Treasury using InboundTransfer objects

# The InboundTransfer object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerAmount (in cents) transferred.
- cancelablebooleanReturnstrueif the InboundTransfer is able to be canceled.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- failure_detailsnullableobjectDetails about this InboundTransfer’s failure. Only set when status isfailed.Show child attributes
- financial_accountstringThe FinancialAccount that received the funds.
- hosted_regulatory_receipt_urlnullablestringAhosted transaction receiptURL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.
- linked_flowsobjectOther flows linked to a InboundTransfer.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- origin_payment_methodnullablestringThe origin payment method to be debited for an InboundTransfer.
- origin_payment_method_detailsnullableobjectDetails about the PaymentMethod for an InboundTransfer.Show child attributes
- returnednullablebooleanReturnstrueif the funds for an InboundTransfer were returned after the InboundTransfer went to thesucceededstate.
- statement_descriptorstringStatement descriptor shown when funds are debited from the source. Not all payment networks supportstatement_descriptor.
- statusenumStatus of the InboundTransfer:processing,succeeded,failed, andcanceled. An InboundTransfer isprocessingif it is created and pending. The status changes tosucceededonce the funds have been “confirmed” and atransactionis created and posted. The status changes tofailedif the transfer fails.
- status_transitionsobjectHash containing timestamps of when the object transitioned to a particularstatus.Show child attributes
- transactionnullablestringExpandableThe Transaction associated with this object.

#### idstring

#### objectstring

#### amountinteger

#### cancelableboolean

#### createdtimestamp

#### currencyenum

#### descriptionnullablestring

#### failure_detailsnullableobject

#### financial_accountstring

#### hosted_regulatory_receipt_urlnullablestring

#### linked_flowsobject

#### livemodeboolean

#### metadataobject

#### origin_payment_methodnullablestring

#### origin_payment_method_detailsnullableobject

#### returnednullableboolean

#### statement_descriptorstring

#### statusenum

#### status_transitionsobject

#### transactionnullablestringExpandable

# Create an InboundTransfer
Creates an InboundTransfer.

### Parameters
- amountintegerRequiredAmount (in cents) to be transferred.
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- financial_accountstringRequiredThe FinancialAccount to send funds to.
- origin_payment_methodstringRequiredThe origin payment method to be debited for the InboundTransfer.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- statement_descriptorstringThe complete description that appears on your customers’ statements. Maximum 10 characters. Can only include -#.$&*, spaces, and alphanumeric characters.

#### amountintegerRequired

#### currencyenumRequired

#### financial_accountstringRequired

#### origin_payment_methodstringRequired

#### descriptionstring

#### metadataobject

#### statement_descriptorstring

### Returns
Returns an InboundTransfer object if there were no issues with InboundTransfer creation. The status of the created InboundTransfer object is initially marked asprocessing.

```
curlhttps://api.stripe.com/v1/treasury/inbound_transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \-d amount=10000 \-d currency=usd \-d origin_payment_method=pm_1KMDdkGPnV27VyGeAgGz8bsi \-d description="InboundTransfer from my bank account"
```

```
curlhttps://api.stripe.com/v1/treasury/inbound_transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \-d amount=10000 \-d currency=usd \-d origin_payment_method=pm_1KMDdkGPnV27VyGeAgGz8bsi \-d description="InboundTransfer from my bank account"
```

```
{"id":"ibt_1MtaDN2eZvKYlo2CxcxF1Qwi","object":"treasury.inbound_transfer","amount":10000,"cancelable":true,"created":1680716025,"currency":"usd","description":"InboundTransfer from my bank account","failure_details":null,"financial_account":"fa_1MtaDM2eZvKYlo2CvXrQknN4","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww","linked_flows":{"received_debit":null},"livemode":false,"metadata":{},"origin_payment_method":"pm_1KMDdkGPnV27VyGeAgGz8bsi","origin_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"returned":false,"statement_descriptor":"transfer","status":"processing","status_transitions":{"failed_at":null,"succeeded_at":null},"transaction":"trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}
```

```
{"id":"ibt_1MtaDN2eZvKYlo2CxcxF1Qwi","object":"treasury.inbound_transfer","amount":10000,"cancelable":true,"created":1680716025,"currency":"usd","description":"InboundTransfer from my bank account","failure_details":null,"financial_account":"fa_1MtaDM2eZvKYlo2CvXrQknN4","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww","linked_flows":{"received_debit":null},"livemode":false,"metadata":{},"origin_payment_method":"pm_1KMDdkGPnV27VyGeAgGz8bsi","origin_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"returned":false,"statement_descriptor":"transfer","status":"processing","status_transitions":{"failed_at":null,"succeeded_at":null},"transaction":"trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}
```

# Retrieve an InboundTransfer
Retrieves the details of an existing InboundTransfer.

### Parameters
Noparameters.

### Returns
Returns an InboundTransfer object if a valid identifier was provided. Otherwise, returns an error.

```
curlhttps://api.stripe.com/v1/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ibt_1MtaDN2eZvKYlo2CxcxF1Qwi","object":"treasury.inbound_transfer","amount":10000,"cancelable":true,"created":1680716025,"currency":"usd","description":"InboundTransfer from my bank account","failure_details":null,"financial_account":"fa_1MtaDM2eZvKYlo2CvXrQknN4","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww","linked_flows":{"received_debit":null},"livemode":false,"metadata":{},"origin_payment_method":"pm_1KMDdkGPnV27VyGeAgGz8bsi","origin_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"returned":false,"statement_descriptor":"transfer","status":"processing","status_transitions":{"failed_at":null,"succeeded_at":null},"transaction":"trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}
```

```
{"id":"ibt_1MtaDN2eZvKYlo2CxcxF1Qwi","object":"treasury.inbound_transfer","amount":10000,"cancelable":true,"created":1680716025,"currency":"usd","description":"InboundTransfer from my bank account","failure_details":null,"financial_account":"fa_1MtaDM2eZvKYlo2CvXrQknN4","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww","linked_flows":{"received_debit":null},"livemode":false,"metadata":{},"origin_payment_method":"pm_1KMDdkGPnV27VyGeAgGz8bsi","origin_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"returned":false,"statement_descriptor":"transfer","status":"processing","status_transitions":{"failed_at":null,"succeeded_at":null},"transaction":"trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}
```

# List all InboundTransfers
Returns a list of InboundTransfers sent from the specified FinancialAccount.

### Parameters
- financial_accountstringReturns objects associated with this FinancialAccount.
- statusenumOnly return InboundTransfers that have the given status:processing,succeeded,failedorcanceled.

#### financial_accountstring

#### statusenum

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitInboundTransfers, starting after InboundTransferstarting_after. Each entry in the array is a separate InboundTransfer object. If no more InboundTransfers are available, the resulting array is empty.

```
curl-G https://api.stripe.com/v1/treasury/inbound_transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtaDM2eZvKYlo2CvXrQknN4 \-d limit=3
```

```
curl-G https://api.stripe.com/v1/treasury/inbound_transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtaDM2eZvKYlo2CvXrQknN4 \-d limit=3
```

```
{"object":"list","url":"/v1/treasury/inbound_transfers","has_more":false,"data":[{"id":"ibt_1MtaDN2eZvKYlo2CxcxF1Qwi","object":"treasury.inbound_transfer","amount":10000,"cancelable":true,"created":1680716025,"currency":"usd","description":"InboundTransfer from my bank account","failure_details":null,"financial_account":"fa_1MtaDM2eZvKYlo2CvXrQknN4","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww","linked_flows":{"received_debit":null},"livemode":false,"metadata":{},"origin_payment_method":"pm_1KMDdkGPnV27VyGeAgGz8bsi","origin_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"returned":false,"statement_descriptor":"transfer","status":"processing","status_transitions":{"failed_at":null,"succeeded_at":null},"transaction":"trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}]}
```

```
{"object":"list","url":"/v1/treasury/inbound_transfers","has_more":false,"data":[{"id":"ibt_1MtaDN2eZvKYlo2CxcxF1Qwi","object":"treasury.inbound_transfer","amount":10000,"cancelable":true,"created":1680716025,"currency":"usd","description":"InboundTransfer from my bank account","failure_details":null,"financial_account":"fa_1MtaDM2eZvKYlo2CvXrQknN4","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww","linked_flows":{"received_debit":null},"livemode":false,"metadata":{},"origin_payment_method":"pm_1KMDdkGPnV27VyGeAgGz8bsi","origin_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"returned":false,"statement_descriptor":"transfer","status":"processing","status_transitions":{"failed_at":null,"succeeded_at":null},"transaction":"trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}]}
```