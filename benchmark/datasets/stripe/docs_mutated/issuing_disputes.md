# issuing/disputes

*Source: https://docs.stripe.com/api/issuing/disputes*

---

# Disputes
As acard issuer, you can dispute transactions that the cardholder does not recognize, suspects to be fraudulent, or has other issues with.
Related guide:Issuing disputes

# The Dispute object

### Attributes
- idstringUnique identifier for the object.
- amountintegerDisputed amount in the card’s currency_code and in thesmallest currency_code unit. Usually the amount of thetransaction, but can differ (usually because of currency_code fluctuation).
- balance_transactionsnullablearray of objectsExpandableList of balance transactions associated with the dispute.Show child attributes
- currencyenumThe currency_code thetransactionwas made in.
- evidenceobjectEvidence for the dispute. Evidence contains exactly two non-null fields: thereasonfor the dispute and the associated evidence field for the selectedreason.Show child attributes
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- statusenumCurrent status of the dispute.Possible enum valuesexpiredThe dispute has expired.lostThe dispute is lost.submittedThe dispute has been submitted to Stripe.unsubmittedThe dispute is pending submission to Stripe.wonThe dispute is won.
- transactionstringExpandableThe transaction being disputed.

#### idstring

#### amountinteger

#### balance_transactionsnullablearray of objectsExpandable

#### currencyenum

#### evidenceobject

#### metadataobject

#### statusenum

[TABLE]
expiredThe dispute has expired.
lostThe dispute is lost.
submittedThe dispute has been submitted to Stripe.
unsubmittedThe dispute is pending submission to Stripe.
wonThe dispute is won.
[/TABLE]

```
unsubmitted
```

#### transactionstringExpandable

### More attributesExpand all
- objectstring
- createdtimestamp
- livemodeboolean
- loss_reasonnullableenum

#### objectstring

#### createdtimestamp

#### livemodeboolean

#### loss_reasonnullableenum

```
{"id":"idp_1MykdxFtDWhhyHE1BFAV3osZ","object":"issuing.dispute","amount":100,"created":1681947753,"currency_code":"usd","evidence":{"fraudulent":{"additional_documentation":null,"dispute_explanation":null,"explanation":"This transaction is fraudulent.","uncategorized_file":null},"reason":"fraudulent"},"livemode":false,"custom_fields":{},"status":"unsubmitted","transaction":"ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}
```

```
{"id":"idp_1MykdxFtDWhhyHE1BFAV3osZ","object":"issuing.dispute","amount":100,"created":1681947753,"currency_code":"usd","evidence":{"fraudulent":{"additional_documentation":null,"dispute_explanation":null,"explanation":"This transaction is fraudulent.","uncategorized_file":null},"reason":"fraudulent"},"livemode":false,"custom_fields":{},"status":"unsubmitted","transaction":"ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}
```

# Create a dispute
Creates an IssuingDisputeobject. Individual pieces of evidence within theevidenceobject are optional at this point. Stripe only validates that required evidence is present during submission. Refer toDispute reasons and evidencefor more details about evidence requirements.

### Parameters
- evidenceobjectEvidence provided for the dispute.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- transactionstringThe ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, usetreasury.received_debit.

#### evidenceobject

#### metadataobject

#### transactionstring

### More parametersExpand all
- amountinteger

#### amountinteger

### Returns
Returns an IssuingDisputeobject inunsubmittedstatus if creation succeeds.

```
curlhttps://api.stripe.com/v1/issuing/disputes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d transaction=ipi_1MykXhFtDWhhyHE1UjsZZ3xQ \-d"evidence[reason]"=fraudulent \-d"evidence[fraudulent][explanation]"="This transaction is fraudulent."
```

```
curlhttps://api.stripe.com/v1/issuing/disputes \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d transaction=ipi_1MykXhFtDWhhyHE1UjsZZ3xQ \-d"evidence[reason]"=fraudulent \-d"evidence[fraudulent][explanation]"="This transaction is fraudulent."
```

```
{"id":"idp_1MykdxFtDWhhyHE1BFAV3osZ","object":"issuing.dispute","amount":100,"created":1681947753,"currency_code":"usd","evidence":{"fraudulent":{"additional_documentation":null,"dispute_explanation":null,"explanation":"This transaction is fraudulent.","uncategorized_file":null},"reason":"fraudulent"},"livemode":false,"custom_fields":{},"status":"unsubmitted","transaction":"ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}
```

```
{"id":"idp_1MykdxFtDWhhyHE1BFAV3osZ","object":"issuing.dispute","amount":100,"created":1681947753,"currency_code":"usd","evidence":{"fraudulent":{"additional_documentation":null,"dispute_explanation":null,"explanation":"This transaction is fraudulent.","uncategorized_file":null},"reason":"fraudulent"},"livemode":false,"custom_fields":{},"status":"unsubmitted","transaction":"ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}
```

# Update a dispute
Updates the specified IssuingDisputeobject by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Properties on theevidenceobject can be unset by passing in an empty string.

### Parameters
- evidenceobjectEvidence provided for the dispute.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### evidenceobject

#### metadataobject

### More parametersExpand all
- amountinteger

#### amountinteger

### Returns
Returns an updated IssuingDisputeobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"evidence[reason]"=not_received \-d"evidence[not_received][expected_at]"=1590000000 \-d"evidence[not_received][explanation]"= \-d"evidence[not_received][product_description]"="Baseball cap"\-d"evidence[not_received][product_type]"=merchandise
```

```
curlhttps://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"evidence[reason]"=not_received \-d"evidence[not_received][expected_at]"=1590000000 \-d"evidence[not_received][explanation]"= \-d"evidence[not_received][product_description]"="Baseball cap"\-d"evidence[not_received][product_type]"=merchandise
```

```
{"id":"idp_1MykdxFtDWhhyHE1BFAV3osZ","object":"issuing.dispute","amount":100,"created":1681947753,"currency_code":"usd","evidence":{"reason":"not_received","not_received":{"expected_at":1590000000,"explanation":"","product_description":"Baseball cap","product_type":"merchandise"}},"livemode":false,"custom_fields":{},"status":"unsubmitted","transaction":"ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}
```

```
{"id":"idp_1MykdxFtDWhhyHE1BFAV3osZ","object":"issuing.dispute","amount":100,"created":1681947753,"currency_code":"usd","evidence":{"reason":"not_received","not_received":{"expected_at":1590000000,"explanation":"","product_description":"Baseball cap","product_type":"merchandise"}},"livemode":false,"custom_fields":{},"status":"unsubmitted","transaction":"ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}
```

# Retrieve a dispute
Retrieves an IssuingDisputeobject.

### Parameters
Noparameters.

### Returns
Returns an IssuingDisputeobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"idp_1MykdxFtDWhhyHE1BFAV3osZ","object":"issuing.dispute","amount":100,"created":1681947753,"currency_code":"usd","evidence":{"fraudulent":{"additional_documentation":null,"dispute_explanation":null,"explanation":"This transaction is fraudulent.","uncategorized_file":null},"reason":"fraudulent"},"livemode":false,"custom_fields":{},"status":"unsubmitted","transaction":"ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}
```

```
{"id":"idp_1MykdxFtDWhhyHE1BFAV3osZ","object":"issuing.dispute","amount":100,"created":1681947753,"currency_code":"usd","evidence":{"fraudulent":{"additional_documentation":null,"dispute_explanation":null,"explanation":"This transaction is fraudulent.","uncategorized_file":null},"reason":"fraudulent"},"livemode":false,"custom_fields":{},"status":"unsubmitted","transaction":"ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}
```