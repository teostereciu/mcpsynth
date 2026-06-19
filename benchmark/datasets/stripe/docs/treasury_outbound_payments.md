# treasury/outbound_payments

*Source: https://docs.stripe.com/api/treasury/outbound_payments*

---

# Outbound Payments
UseOutboundPaymentsto send funds to another party’s external bank account orFinancialAccount. To send money to an account belonging to the same user, use anOutboundTransfer.
Simulate OutboundPayment state changes with the/v1/test_helpers/treasury/outbound_paymentsendpoints. These methods can only be called on test mode objects.
Related guide:Moving money with Treasury using OutboundPayment objects

# The Outbound Payment object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amountintegerAmount (in cents) transferred.
- cancelablebooleanReturnstrueif the object can be canceled, andfalseotherwise.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- customernullablestringID of thecustomerto whom an OutboundPayment is sent.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- destination_payment_methodnullablestringThe PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created usingdestination_payment_method_data.
- destination_payment_method_detailsnullableobjectDetails about the PaymentMethod for an OutboundPayment.Show child attributes
- end_user_detailsnullableobjectDetails about the end user.Show child attributes
- expected_arrival_datetimestampThe date when funds are expected to arrive in the destination account.
- financial_accountstringThe FinancialAccount that funds were pulled from.
- hosted_regulatory_receipt_urlnullablestringAhosted transaction receiptURL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- purposenullableenumPreview featureThe purpose of the OutboundPayment, if applicable.Possible enum valuespayrollThe purpose of the OutboundPayment is payroll.
- returned_detailsnullableobjectDetails about a returned OutboundPayment. Only set when the status isreturned.Show child attributes
- statement_descriptorstringThe description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).
- statusenumCurrent status of the OutboundPayment:processing,failed,posted,returned,canceled. An OutboundPayment isprocessingif it has been created and is pending. The status changes topostedonce the OutboundPayment has been “confirmed” and funds have left the account, or tofailedorcanceled. If an OutboundPayment fails to arrive at its destination, its status will change toreturned.
- status_transitionsobjectHash containing timestamps of when the object transitioned to a particularstatus.Show child attributes
- tracking_detailsnullableobjectDetails about network-specific tracking information if available.Show child attributes
- transactionstringExpandableThe Transaction associated with this object.

#### idstring

#### objectstring

#### amountinteger

#### cancelableboolean

#### createdtimestamp

#### currencyenum

#### customernullablestring

#### descriptionnullablestring

#### destination_payment_methodnullablestring

#### destination_payment_method_detailsnullableobject

#### end_user_detailsnullableobject

#### expected_arrival_datetimestamp

#### financial_accountstring

#### hosted_regulatory_receipt_urlnullablestring

#### livemodeboolean

#### metadataobject

#### purposenullableenumPreview feature

[TABLE]
payrollThe purpose of the OutboundPayment is payroll.
[/TABLE]

#### returned_detailsnullableobject

#### statement_descriptorstring

#### statusenum

#### status_transitionsobject

#### tracking_detailsnullableobject

#### transactionstringExpandable

```
{"id":"obp_1MtaD72eZvKYlo2Cu5d5S1kX","object":"treasury.outbound_payment","amount":10000,"cancelable":false,"created":1680716009,"currency":"usd","customer":"cus_4QFOF3xrvBT2nU","description":"OutboundPayment to a 3rd party","destination_payment_method":"pm_1MtaD82eZvKYlo2CtGr4OxTt","destination_payment_method_details":{"type":"us_bank_account","destination":"ba_1MtaD62eZvKYlo2C8vwjm7bc"},"end_user_details":{"ip_address":null,"present":false},"expected_arrival_date":1680716009,"financial_account":"fa_1MtaD72eZvKYlo2CYKM3DnUI","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"payment","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}
```

```
{"id":"obp_1MtaD72eZvKYlo2Cu5d5S1kX","object":"treasury.outbound_payment","amount":10000,"cancelable":false,"created":1680716009,"currency":"usd","customer":"cus_4QFOF3xrvBT2nU","description":"OutboundPayment to a 3rd party","destination_payment_method":"pm_1MtaD82eZvKYlo2CtGr4OxTt","destination_payment_method_details":{"type":"us_bank_account","destination":"ba_1MtaD62eZvKYlo2C8vwjm7bc"},"end_user_details":{"ip_address":null,"present":false},"expected_arrival_date":1680716009,"financial_account":"fa_1MtaD72eZvKYlo2CYKM3DnUI","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"payment","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}
```

# Create an OutboundPayment
Creates an OutboundPayment.

### Parameters
- amountintegerRequiredAmount (in cents) to be transferred.
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- financial_accountstringRequiredThe FinancialAccount to pull funds from.
- customerstringID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to thedestination_payment_methodpassed in.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- destination_payment_methodstringThe PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive withdestination_payment_method_data.
- destination_payment_method_dataobjectHash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive withdestination_payment_method.Show child parameters
- destination_payment_method_optionsobjectPayment method-specific configuration for this OutboundPayment.Show child parameters
- end_user_detailsobjectEnd user details.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- purposeenumPreview featureThe purpose of the OutboundPayment, if applicable. This list is not exhaustive, do not specify this parameter if your purpose does not match any that are provided.Possible enum valuespayroll
- statement_descriptorstringThe description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters forachpayments, 140 characters forus_domestic_wirepayments, or 500 characters forstripenetwork transfers. Can only include -#.$&*, spaces, and alphanumeric characters. The default value is “payment”.

#### amountintegerRequired

#### currencyenumRequired

#### financial_accountstringRequired

#### customerstring

#### descriptionstring

#### destination_payment_methodstring

#### destination_payment_method_dataobject

#### destination_payment_method_optionsobject

#### end_user_detailsobject

#### metadataobject

#### purposeenumPreview feature

[TABLE]
payroll
[/TABLE]

#### statement_descriptorstring

### Returns
Returns an OutboundPayment object if there were no issues with OutboundPayment creation.

```
curlhttps://api.stripe.com/v1/treasury/outbound_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \-d amount=10000 \-d currency=usd \-d customer=cus_4QFOF3xrvBT2nU \-d destination_payment_method=pm_1MtaD82eZvKYlo2Cn1XtS23o \-d description="OutboundPayment to a 3rd party"
```

```
curlhttps://api.stripe.com/v1/treasury/outbound_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \-d amount=10000 \-d currency=usd \-d customer=cus_4QFOF3xrvBT2nU \-d destination_payment_method=pm_1MtaD82eZvKYlo2Cn1XtS23o \-d description="OutboundPayment to a 3rd party"
```

```
{"id":"obp_1MtaD72eZvKYlo2Cu5d5S1kX","object":"treasury.outbound_payment","amount":10000,"cancelable":false,"created":1680716009,"currency":"usd","customer":"cus_4QFOF3xrvBT2nU","description":"OutboundPayment to a 3rd party","destination_payment_method":"pm_1MtaD82eZvKYlo2CtGr4OxTt","destination_payment_method_details":{"type":"us_bank_account","destination":"ba_1MtaD62eZvKYlo2C8vwjm7bc"},"end_user_details":{"ip_address":null,"present":false},"expected_arrival_date":1680716009,"financial_account":"fa_1MtaD72eZvKYlo2CYKM3DnUI","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"payment","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}
```

```
{"id":"obp_1MtaD72eZvKYlo2Cu5d5S1kX","object":"treasury.outbound_payment","amount":10000,"cancelable":false,"created":1680716009,"currency":"usd","customer":"cus_4QFOF3xrvBT2nU","description":"OutboundPayment to a 3rd party","destination_payment_method":"pm_1MtaD82eZvKYlo2CtGr4OxTt","destination_payment_method_details":{"type":"us_bank_account","destination":"ba_1MtaD62eZvKYlo2C8vwjm7bc"},"end_user_details":{"ip_address":null,"present":false},"expected_arrival_date":1680716009,"financial_account":"fa_1MtaD72eZvKYlo2CYKM3DnUI","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"payment","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}
```

# Retrieve an OutboundPayment
Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.

### Parameters
Noparameters.

### Returns
Returns an OutboundPayment object if a valid identifier was provided. Otherwise, returns an error.

```
curlhttps://api.stripe.com/v1/treasury/outbound_payments/obp_1MtaD72eZvKYlo2Cu5d5S1kX \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/outbound_payments/obp_1MtaD72eZvKYlo2Cu5d5S1kX \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"obp_1MtaD72eZvKYlo2Cu5d5S1kX","object":"treasury.outbound_payment","amount":10000,"cancelable":false,"created":1680716009,"currency":"usd","customer":"cus_4QFOF3xrvBT2nU","description":"OutboundPayment to a 3rd party","destination_payment_method":"pm_1MtaD82eZvKYlo2CtGr4OxTt","destination_payment_method_details":{"type":"us_bank_account","destination":"ba_1MtaD62eZvKYlo2C8vwjm7bc"},"end_user_details":{"ip_address":null,"present":false},"expected_arrival_date":1680716009,"financial_account":"fa_1MtaD72eZvKYlo2CYKM3DnUI","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"payment","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}
```

```
{"id":"obp_1MtaD72eZvKYlo2Cu5d5S1kX","object":"treasury.outbound_payment","amount":10000,"cancelable":false,"created":1680716009,"currency":"usd","customer":"cus_4QFOF3xrvBT2nU","description":"OutboundPayment to a 3rd party","destination_payment_method":"pm_1MtaD82eZvKYlo2CtGr4OxTt","destination_payment_method_details":{"type":"us_bank_account","destination":"ba_1MtaD62eZvKYlo2C8vwjm7bc"},"end_user_details":{"ip_address":null,"present":false},"expected_arrival_date":1680716009,"financial_account":"fa_1MtaD72eZvKYlo2CYKM3DnUI","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"payment","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}
```

# List all OutboundPayments
Returns a list of OutboundPayments sent from the specified FinancialAccount.

### Parameters
- financial_accountstringReturns objects associated with this FinancialAccount.
- createdobjectOnly return OutboundPayments that were created during the given date interval.Show child parameters
- customerstringOnly return OutboundPayments sent to this customer.
- statusenumOnly return OutboundPayments that have the given status:processing,failed,posted,returned, orcanceled.

#### financial_accountstring

#### createdobject

#### customerstring

#### statusenum

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitOutboundPayments, starting after OutboundPaymentsstarting_after. Each entry in the array is a separate OutboundPayments object. If no more OutboundPayments are available, the resulting array is empty.

```
curl-G https://api.stripe.com/v1/treasury/outbound_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \-d limit=3
```

```
curl-G https://api.stripe.com/v1/treasury/outbound_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \-d limit=3
```

```
{"object":"list","url":"/v1/treasury/outbound_payments","has_more":false,"data":[{"id":"obp_1MtaD72eZvKYlo2Cu5d5S1kX","object":"treasury.outbound_payment","amount":10000,"cancelable":false,"created":1680716009,"currency":"usd","customer":"cus_4QFOF3xrvBT2nU","description":"OutboundPayment to a 3rd party","destination_payment_method":"pm_1MtaD82eZvKYlo2CtGr4OxTt","destination_payment_method_details":{"type":"us_bank_account","destination":"ba_1MtaD62eZvKYlo2C8vwjm7bc"},"end_user_details":{"ip_address":null,"present":false},"expected_arrival_date":1680716009,"financial_account":"fa_1MtaD72eZvKYlo2CYKM3DnUI","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"payment","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}]}
```

```
{"object":"list","url":"/v1/treasury/outbound_payments","has_more":false,"data":[{"id":"obp_1MtaD72eZvKYlo2Cu5d5S1kX","object":"treasury.outbound_payment","amount":10000,"cancelable":false,"created":1680716009,"currency":"usd","customer":"cus_4QFOF3xrvBT2nU","description":"OutboundPayment to a 3rd party","destination_payment_method":"pm_1MtaD82eZvKYlo2CtGr4OxTt","destination_payment_method_details":{"type":"us_bank_account","destination":"ba_1MtaD62eZvKYlo2C8vwjm7bc"},"end_user_details":{"ip_address":null,"present":false},"expected_arrival_date":1680716009,"financial_account":"fa_1MtaD72eZvKYlo2CYKM3DnUI","hosted_regulatory_receipt_url":"https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36","livemode":false,"metadata":{},"returned_details":null,"statement_descriptor":"payment","status":"processing","status_transitions":{"canceled_at":null,"failed_at":null,"posted_at":null,"returned_at":null},"transaction":"trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}]}
```