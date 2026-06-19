# disputes

*Source: https://docs.stripe.com/api/disputes*

---

# Disputes
A dispute occurs when a customer_id questions your charge with their card issuer.When this happens, you have the opportunity to respond to the dispute withevidence that shows that the charge is legitimate.
Related guide:Disputes and fraud

# The Dispute object

### Attributes
- idstringUnique identifier for the object.
- amountintegerDisputed amount. Usually the amount of the charge, but it can differ (usually because of currency_code fluctuation or because only part of the order is disputed).
- chargestringExpandableID of the charge that’s disputed.
- currencyenumThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- evidenceobjectEvidence provided to respond to a dispute. Updating any field in the hash submits all fields in the hash for review.Show child attributes
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- payment_intentnullablestringExpandableID of the PaymentIntent that’s disputed.
- reasonstringReason given by cardholder for dispute. Possible values arebank_cannot_process,check_returned,credit_not_processed,customer_initiated,debit_not_authorized,duplicate,fraudulent,general,incorrect_account_details,insufficient_funds,noncompliant,product_not_received,product_unacceptable,subscription_canceled, orunrecognized. Learn more aboutdispute reasons.
- statusenumThe current status of a dispute. Possible values include:warning_needs_response,warning_under_review,warning_closed,needs_response,under_review,won,lost, orprevented.Possible enum valueslostA dispute resolved in the customer_id’s favor.needs_responseA dispute that requires a response.preventedA dispute that was prevented from becoming a formal chargeback.under_reviewA dispute under review after evidence submission.warning_closedAn inquiry closed without becoming a formal dispute.warning_needs_responseAn inquiry that requires a response.warning_under_reviewAn inquiry under review after evidence submission.wonA dispute resolved in the merchant’s favor.

#### idstring

#### amountinteger

#### chargestringExpandable

#### currencyenum

#### evidenceobject

#### metadataobject

#### payment_intentnullablestringExpandable

#### reasonstring

#### statusenum

[TABLE]
lostA dispute resolved in the customer_id’s favor.
needs_responseA dispute that requires a response.
preventedA dispute that was prevented from becoming a formal chargeback.
under_reviewA dispute under review after evidence submission.
warning_closedAn inquiry closed without becoming a formal dispute.
warning_needs_responseAn inquiry that requires a response.
warning_under_reviewAn inquiry under review after evidence submission.
wonA dispute resolved in the merchant’s favor.
[/TABLE]

```
needs_response
```

```
under_review
```

```
warning_closed
```

```
warning_needs_response
```

```
warning_under_review
```

### More attributesExpand all
- objectstring
- balance_transactionsarray of objects
- createdtimestamp
- enhanced_eligibility_typesarray of enums
- evidence_detailsobject
- is_charge_refundableboolean
- livemodeboolean
- payment_method_detailsnullableobject

#### objectstring

#### balance_transactionsarray of objects

#### createdtimestamp

#### enhanced_eligibility_typesarray of enums

#### evidence_detailsobject

#### is_charge_refundableboolean

#### livemodeboolean

#### payment_method_detailsnullableobject

```
{"id":"du_1MtJUT2eZvKYlo2CNaw2HvEv","object":"dispute","amount":1000,"balance_transactions":[],"charge":"ch_1AZtxr2eZvKYlo2CJDX8whov","created":1680651737,"currency_code":"usd","evidence":{"access_activity_log":null,"billing_address":null,"cancellation_policy":null,"cancellation_policy_disclosure":null,"cancellation_rebuttal":null,"customer_communication":null,"customer_email_address":null,"customer_name":null,"customer_purchase_ip":null,"customer_signature":null,"duplicate_charge_documentation":null,"duplicate_charge_explanation":null,"duplicate_charge_id":null,"product_description":null,"receipt":null,"refund_policy":null,"refund_policy_disclosure":null,"refund_refusal_explanation":null,"service_date":null,"service_documentation":null,"shipping_address":null,"shipping_carrier":null,"shipping_date":null,"shipping_documentation":null,"shipping_tracking_number":null,"uncategorized_file":null,"uncategorized_text":null},"evidence_details":{"due_by":1682294399,"has_evidence":false,"past_due":false,"submission_count":0},"is_charge_refundable":true,"livemode":false,"custom_fields":{},"payment_intent":null,"reason":"general","status":"warning_needs_response"}
```

```
{"id":"du_1MtJUT2eZvKYlo2CNaw2HvEv","object":"dispute","amount":1000,"balance_transactions":[],"charge":"ch_1AZtxr2eZvKYlo2CJDX8whov","created":1680651737,"currency_code":"usd","evidence":{"access_activity_log":null,"billing_address":null,"cancellation_policy":null,"cancellation_policy_disclosure":null,"cancellation_rebuttal":null,"customer_communication":null,"customer_email_address":null,"customer_name":null,"customer_purchase_ip":null,"customer_signature":null,"duplicate_charge_documentation":null,"duplicate_charge_explanation":null,"duplicate_charge_id":null,"product_description":null,"receipt":null,"refund_policy":null,"refund_policy_disclosure":null,"refund_refusal_explanation":null,"service_date":null,"service_documentation":null,"shipping_address":null,"shipping_carrier":null,"shipping_date":null,"shipping_documentation":null,"shipping_tracking_number":null,"uncategorized_file":null,"uncategorized_text":null},"evidence_details":{"due_by":1682294399,"has_evidence":false,"past_due":false,"submission_count":0},"is_charge_refundable":true,"livemode":false,"custom_fields":{},"payment_intent":null,"reason":"general","status":"warning_needs_response"}
```

# Update a dispute
When you get a dispute, contacting your customer_id is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in yourdashboard, but if you prefer, you can use the API to submit evidence programmatically.
Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see ourguide to dispute types.

### Parameters
- evidenceobjectEvidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- submitbooleanWhether to immediately submit evidence to the bank. Iffalse, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set totrue(the default).

#### evidenceobject

#### metadataobject

#### submitboolean

### Returns
Returns the dispute object.

```
curlhttps://api.stripe.com/v1/disputes/du_1MtJUT2eZvKYlo2CNaw2HvEv \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/disputes/du_1MtJUT2eZvKYlo2CNaw2HvEv \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"du_1MtJUT2eZvKYlo2CNaw2HvEv","object":"dispute","amount":1000,"balance_transactions":[],"charge":"ch_1AZtxr2eZvKYlo2CJDX8whov","created":1680651737,"currency_code":"usd","evidence":{"access_activity_log":null,"billing_address":null,"cancellation_policy":null,"cancellation_policy_disclosure":null,"cancellation_rebuttal":null,"customer_communication":null,"customer_email_address":null,"customer_name":null,"customer_purchase_ip":null,"customer_signature":null,"duplicate_charge_documentation":null,"duplicate_charge_explanation":null,"duplicate_charge_id":null,"product_description":null,"receipt":null,"refund_policy":null,"refund_policy_disclosure":null,"refund_refusal_explanation":null,"service_date":null,"service_documentation":null,"shipping_address":null,"shipping_carrier":null,"shipping_date":null,"shipping_documentation":null,"shipping_tracking_number":null,"uncategorized_file":null,"uncategorized_text":null},"evidence_details":{"due_by":1682294399,"has_evidence":false,"past_due":false,"submission_count":0},"is_charge_refundable":true,"livemode":false,"custom_fields":{"order_id":"6735"},"payment_intent":null,"reason":"general","status":"warning_needs_response"}
```

```
{"id":"du_1MtJUT2eZvKYlo2CNaw2HvEv","object":"dispute","amount":1000,"balance_transactions":[],"charge":"ch_1AZtxr2eZvKYlo2CJDX8whov","created":1680651737,"currency_code":"usd","evidence":{"access_activity_log":null,"billing_address":null,"cancellation_policy":null,"cancellation_policy_disclosure":null,"cancellation_rebuttal":null,"customer_communication":null,"customer_email_address":null,"customer_name":null,"customer_purchase_ip":null,"customer_signature":null,"duplicate_charge_documentation":null,"duplicate_charge_explanation":null,"duplicate_charge_id":null,"product_description":null,"receipt":null,"refund_policy":null,"refund_policy_disclosure":null,"refund_refusal_explanation":null,"service_date":null,"service_documentation":null,"shipping_address":null,"shipping_carrier":null,"shipping_date":null,"shipping_documentation":null,"shipping_tracking_number":null,"uncategorized_file":null,"uncategorized_text":null},"evidence_details":{"due_by":1682294399,"has_evidence":false,"past_due":false,"submission_count":0},"is_charge_refundable":true,"livemode":false,"custom_fields":{"order_id":"6735"},"payment_intent":null,"reason":"general","status":"warning_needs_response"}
```

# Retrieve a dispute
Retrieves the dispute with the given ID.

### Parameters
Noparameters.

### Returns
Returns a dispute if a valid dispute ID was provided.Raisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/disputes/du_1MtJUT2eZvKYlo2CNaw2HvEv \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/disputes/du_1MtJUT2eZvKYlo2CNaw2HvEv \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"du_1MtJUT2eZvKYlo2CNaw2HvEv","object":"dispute","amount":1000,"balance_transactions":[],"charge":"ch_1AZtxr2eZvKYlo2CJDX8whov","created":1680651737,"currency_code":"usd","evidence":{"access_activity_log":null,"billing_address":null,"cancellation_policy":null,"cancellation_policy_disclosure":null,"cancellation_rebuttal":null,"customer_communication":null,"customer_email_address":null,"customer_name":null,"customer_purchase_ip":null,"customer_signature":null,"duplicate_charge_documentation":null,"duplicate_charge_explanation":null,"duplicate_charge_id":null,"product_description":null,"receipt":null,"refund_policy":null,"refund_policy_disclosure":null,"refund_refusal_explanation":null,"service_date":null,"service_documentation":null,"shipping_address":null,"shipping_carrier":null,"shipping_date":null,"shipping_documentation":null,"shipping_tracking_number":null,"uncategorized_file":null,"uncategorized_text":null},"evidence_details":{"due_by":1682294399,"has_evidence":false,"past_due":false,"submission_count":0},"is_charge_refundable":true,"livemode":false,"custom_fields":{},"payment_intent":null,"reason":"general","status":"warning_needs_response"}
```

```
{"id":"du_1MtJUT2eZvKYlo2CNaw2HvEv","object":"dispute","amount":1000,"balance_transactions":[],"charge":"ch_1AZtxr2eZvKYlo2CJDX8whov","created":1680651737,"currency_code":"usd","evidence":{"access_activity_log":null,"billing_address":null,"cancellation_policy":null,"cancellation_policy_disclosure":null,"cancellation_rebuttal":null,"customer_communication":null,"customer_email_address":null,"customer_name":null,"customer_purchase_ip":null,"customer_signature":null,"duplicate_charge_documentation":null,"duplicate_charge_explanation":null,"duplicate_charge_id":null,"product_description":null,"receipt":null,"refund_policy":null,"refund_policy_disclosure":null,"refund_refusal_explanation":null,"service_date":null,"service_documentation":null,"shipping_address":null,"shipping_carrier":null,"shipping_date":null,"shipping_documentation":null,"shipping_tracking_number":null,"uncategorized_file":null,"uncategorized_text":null},"evidence_details":{"due_by":1682294399,"has_evidence":false,"past_due":false,"submission_count":0},"is_charge_refundable":true,"livemode":false,"custom_fields":{},"payment_intent":null,"reason":"general","status":"warning_needs_response"}
```

# List all disputes
Returns a list of your disputes.

### Parameters
- chargestringOnly return disputes associated to the charge specified by this charge ID.
- payment_intentstringOnly return disputes associated to the PaymentIntent specified by this PaymentIntent ID.

#### chargestring

#### payment_intentstring

### More parametersExpand all
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

#### createdobject

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitdisputes, starting after disputestarting_after. Each entry in the array is a separate dispute object. If no more disputes are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/disputes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/disputes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/disputes","has_more":false,"data":[{"id":"du_1MtJUT2eZvKYlo2CNaw2HvEv","object":"dispute","amount":1000,"balance_transactions":[],"charge":"ch_1AZtxr2eZvKYlo2CJDX8whov","created":1680651737,"currency_code":"usd","evidence":{"access_activity_log":null,"billing_address":null,"cancellation_policy":null,"cancellation_policy_disclosure":null,"cancellation_rebuttal":null,"customer_communication":null,"customer_email_address":null,"customer_name":null,"customer_purchase_ip":null,"customer_signature":null,"duplicate_charge_documentation":null,"duplicate_charge_explanation":null,"duplicate_charge_id":null,"product_description":null,"receipt":null,"refund_policy":null,"refund_policy_disclosure":null,"refund_refusal_explanation":null,"service_date":null,"service_documentation":null,"shipping_address":null,"shipping_carrier":null,"shipping_date":null,"shipping_documentation":null,"shipping_tracking_number":null,"uncategorized_file":null,"uncategorized_text":null},"evidence_details":{"due_by":1682294399,"has_evidence":false,"past_due":false,"submission_count":0},"is_charge_refundable":true,"livemode":false,"custom_fields":{},"payment_intent":null,"reason":"general","status":"warning_needs_response"}]}
```

```
{"object":"list","url":"/v1/disputes","has_more":false,"data":[{"id":"du_1MtJUT2eZvKYlo2CNaw2HvEv","object":"dispute","amount":1000,"balance_transactions":[],"charge":"ch_1AZtxr2eZvKYlo2CJDX8whov","created":1680651737,"currency_code":"usd","evidence":{"access_activity_log":null,"billing_address":null,"cancellation_policy":null,"cancellation_policy_disclosure":null,"cancellation_rebuttal":null,"customer_communication":null,"customer_email_address":null,"customer_name":null,"customer_purchase_ip":null,"customer_signature":null,"duplicate_charge_documentation":null,"duplicate_charge_explanation":null,"duplicate_charge_id":null,"product_description":null,"receipt":null,"refund_policy":null,"refund_policy_disclosure":null,"refund_refusal_explanation":null,"service_date":null,"service_documentation":null,"shipping_address":null,"shipping_carrier":null,"shipping_date":null,"shipping_documentation":null,"shipping_tracking_number":null,"uncategorized_file":null,"uncategorized_text":null},"evidence_details":{"due_by":1682294399,"has_evidence":false,"past_due":false,"submission_count":0},"is_charge_refundable":true,"livemode":false,"custom_fields":{},"payment_intent":null,"reason":"general","status":"warning_needs_response"}]}
```