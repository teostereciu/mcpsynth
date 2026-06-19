# treasury/outbound_transfers

*Source: https://docs.stripe.com/api/treasury/outbound_transfers*

---

# Outbound Transfers
UseOutboundTransfersto transfer funds from aFinancialAccountto a PaymentMethod belonging to the same entity. To send funds to a different party, useOutboundPaymentsinstead. You can send funds over ACH rails or through a domestic wire transfer to a user’s own external bank account.
Simulate OutboundTransfer state changes with the/v1/test_helpers/treasury/outbound_transfersendpoints. These methods can only be called on test mode objects.
Related guide:Moving money with Treasury using OutboundTransfer objects

# The OutboundTransfer object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerAmount (in cents) transferred.
- cancelablebooleanReturnstrueif the object can be canceled, andfalseotherwise.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- destination_payment_methodnullablestringThe PaymentMethod used as the payment instrument for an OutboundTransfer.
- destination_payment_method_detailsobjectDetails about the PaymentMethod for an OutboundTransferShow child attributes
- expected_arrival_datetimestampThe date when funds are expected to arrive in the destination account.
- financial_accountstringThe FinancialAccount that funds were pulled from.
- hosted_regulatory_receipt_urlnullablestringAhosted transaction receiptURL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- returned_detailsnullableobjectDetails about a returned OutboundTransfer. Only set when the status isreturned.Show child attributes
- statement_descriptorstringInformation about the OutboundTransfer to be sent to the recipient account.
- statusenumCurrent status of the OutboundTransfer:processing,failed,canceled,posted,returned. An OutboundTransfer isprocessingif it has been created and is pending. The status changes topostedonce the OutboundTransfer has been “confirmed” and funds have left the account, or tofailedorcanceled. If an OutboundTransfer fails to arrive at its destination, its status will change toreturned.
- status_transitionsobjectHash containing timestamps of when the object transitioned to a particularstatus.Show child attributes
- tracking_detailsnullableobjectDetails about network-specific tracking information if available.Show child attributes
- transactionstringExpandableThe Transaction associated with this object.

#### idstring

#### objectstring

#### amountinteger

#### cancelableboolean

#### createdtimestamp

#### currencyenum

#### descriptionnullablestring

#### destination_payment_methodnullablestring

#### destination_payment_method_detailsobject

#### expected_arrival_datetimestamp

#### financial_accountstring

#### hosted_regulatory_receipt_urlnullablestring

#### livemodeboolean

#### metadataobject

#### returned_detailsnullableobject

#### statement_descriptorstring

#### statusenum

#### status_transitionsobject

#### tracking_detailsnullableobject

#### transactionstringExpandable

```
{"id":"obt_1Mtaaz2eZvKYlo2CUu1tWGAl","object":"treasury.outbound_transfer","amount":500,"cancelable":true,"created":1680717489,"currency":"usd","description":"OutboundTransfer to my external bank account","destination_payment_method":"pm_1234567890","destination_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"expected_arrival_date":1680825600,"financial_account":"fa_1Mtaaz2eZvKYlo2CUf56sIA1","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"transfer","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}
```

```
{"id":"obt_1Mtaaz2eZvKYlo2CUu1tWGAl","object":"treasury.outbound_transfer","amount":500,"cancelable":true,"created":1680717489,"currency":"usd","description":"OutboundTransfer to my external bank account","destination_payment_method":"pm_1234567890","destination_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"expected_arrival_date":1680825600,"financial_account":"fa_1Mtaaz2eZvKYlo2CUf56sIA1","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"transfer","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}
```

# Create an OutboundTransfer
Creates an OutboundTransfer.

### Parameters
- amountintegerRequiredAmount (in cents) to be transferred.
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- financial_accountstringRequiredThe FinancialAccount to pull funds from.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- destination_payment_methodstringThe PaymentMethod to use as the payment instrument for the OutboundTransfer.
- destination_payment_method_dataobjectPreview featureHash used to generate the PaymentMethod to be used for this OutboundTransfer. Exclusive withdestination_payment_method.Show child parameters
- destination_payment_method_optionsobjectHash describing payment method configuration details.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- statement_descriptorstringStatement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters forachtransfers or 140 characters forus_domestic_wiretransfers. The default value is “transfer”. Can only include -#.$&*, spaces, and alphanumeric characters.

#### amountintegerRequired

#### currencyenumRequired

#### financial_accountstringRequired

#### descriptionstring

#### destination_payment_methodstring

#### destination_payment_method_dataobjectPreview feature

#### destination_payment_method_optionsobject

#### metadataobject

#### statement_descriptorstring

### Returns
Returns an OutboundTransfer object if there were no issues with OutboundTransfer creation. The status of the created OutboundTransfer object is initially marked asprocessing.

```
curlhttps://api.stripe.com/v1/treasury/outbound_transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1Mtaaz2eZvKYlo2CUf56sIA1 \-d destination_payment_method=pm_1234567890 \-d amount=500 \-d currency=usd \-d description="OutboundTransfer to my external bank account"
```

```
curlhttps://api.stripe.com/v1/treasury/outbound_transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1Mtaaz2eZvKYlo2CUf56sIA1 \-d destination_payment_method=pm_1234567890 \-d amount=500 \-d currency=usd \-d description="OutboundTransfer to my external bank account"
```

```
{"id":"obt_1Mtaaz2eZvKYlo2CUu1tWGAl","object":"treasury.outbound_transfer","amount":500,"cancelable":true,"created":1680717489,"currency":"usd","description":"OutboundTransfer to my external bank account","destination_payment_method":"pm_1234567890","destination_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"expected_arrival_date":1680825600,"financial_account":"fa_1Mtaaz2eZvKYlo2CUf56sIA1","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"transfer","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}
```

```
{"id":"obt_1Mtaaz2eZvKYlo2CUu1tWGAl","object":"treasury.outbound_transfer","amount":500,"cancelable":true,"created":1680717489,"currency":"usd","description":"OutboundTransfer to my external bank account","destination_payment_method":"pm_1234567890","destination_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"expected_arrival_date":1680825600,"financial_account":"fa_1Mtaaz2eZvKYlo2CUf56sIA1","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"transfer","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}
```

# Retrieve an OutboundTransfer
Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundTransfer creation request or OutboundTransfer list.

### Parameters
Noparameters.

### Returns
Returns an OutboundTransfer object if a valid identifier was provided. Otherwise, returns an error.

```
curlhttps://api.stripe.com/v1/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"obt_1Mtaaz2eZvKYlo2CUu1tWGAl","object":"treasury.outbound_transfer","amount":500,"cancelable":true,"created":1680717489,"currency":"usd","description":"OutboundTransfer to my external bank account","destination_payment_method":"pm_1234567890","destination_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"expected_arrival_date":1680825600,"financial_account":"fa_1Mtaaz2eZvKYlo2CUf56sIA1","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"transfer","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}
```

```
{"id":"obt_1Mtaaz2eZvKYlo2CUu1tWGAl","object":"treasury.outbound_transfer","amount":500,"cancelable":true,"created":1680717489,"currency":"usd","description":"OutboundTransfer to my external bank account","destination_payment_method":"pm_1234567890","destination_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"expected_arrival_date":1680825600,"financial_account":"fa_1Mtaaz2eZvKYlo2CUf56sIA1","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"transfer","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}
```

# List all OutboundTransfers
Returns a list of OutboundTransfers sent from the specified FinancialAccount.

### Parameters
- financial_accountstringReturns objects associated with this FinancialAccount.
- statusenumOnly return OutboundTransfers that have the given status:processing,canceled,failed,posted, orreturned.

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
Adictionarywith adataproperty that contains an array of up tolimitOutboundTransfers, starting after OutboundTransferstarting_after. Each entry in the array is a separate OutboundTransfer object. If no more OutboundTransfers are available, the resulting array is empty.

```
curl-G https://api.stripe.com/v1/treasury/outbound_transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3 \-d financial_account=fa_1Mtaaz2eZvKYlo2CUf56sIA1
```

```
curl-G https://api.stripe.com/v1/treasury/outbound_transfers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3 \-d financial_account=fa_1Mtaaz2eZvKYlo2CUf56sIA1
```

```
{"object":"list","url":"/v1/treasury/outbound_transfers","has_more":false,"data":[{"id":"obt_1Mtaaz2eZvKYlo2CUu1tWGAl","object":"treasury.outbound_transfer","amount":500,"cancelable":true,"created":1680717489,"currency":"usd","description":"OutboundTransfer to my external bank account","destination_payment_method":"pm_1234567890","destination_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"expected_arrival_date":1680825600,"financial_account":"fa_1Mtaaz2eZvKYlo2CUf56sIA1","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"transfer","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}]}
```

```
{"object":"list","url":"/v1/treasury/outbound_transfers","has_more":false,"data":[{"id":"obt_1Mtaaz2eZvKYlo2CUu1tWGAl","object":"treasury.outbound_transfer","amount":500,"cancelable":true,"created":1680717489,"currency":"usd","description":"OutboundTransfer to my external bank account","destination_payment_method":"pm_1234567890","destination_payment_method_details":{"billing_details":{"address":{"city":"San Francisco","country":"US","line1":"1234 Fake Street","line2":null,"postal_code":"94102","state":"CA"},"email":null,"name":"Jane Austen"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"company","account_type":"checking","bank_name":"STRIPE TEST BANK","fingerprint":"AP24Iso0btGp4N10","last4":"6789","network":"ach","routing_number":"110000000"}},"expected_arrival_date":1680825600,"financial_account":"fa_1Mtaaz2eZvKYlo2CUf56sIA1","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"transfer","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}]}
```