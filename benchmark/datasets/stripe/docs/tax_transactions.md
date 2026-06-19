# tax/transactions

*Source: https://docs.stripe.com/api/tax/transactions*

---

# Tax Transactions
A Tax Transaction records the tax collected from or refunded to your customer.
Related guide:Calculate tax in your custom payment flow

# The Tax Transaction object

### Attributes
- idstringUnique identifier for the transaction.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- currencystringThree-letterISO currency code, in lowercase. Must be asupported currency.
- customer_detailsobjectThe customer’s details, such as address and tax IDs.Show child attributes
- line_itemsnullableobjectExpandableThe tax collected or refunded, by line item.Show child attributes
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- referencestringA custom unique identifier, such as ‘myOrder_123’.
- typeenumIfreversal, this transaction reverses an earlier transaction.Possible enum valuesreversalRepresents a partial or full reversal of an earlier transaction.transactionRepresents a customer sale or order.

#### idstring

#### objectstring

#### currencystring

#### customer_detailsobject

#### line_itemsnullableobjectExpandable

#### metadatanullableobject

#### referencestring

#### typeenum

[TABLE]
reversalRepresents a partial or full reversal of an earlier transaction.
transactionRepresents a customer sale or order.
[/TABLE]

```
transaction
```

### More attributesExpand all
- createdtimestamp
- customernullablestring
- livemodeboolean
- posted_attimestamp
- reversalnullableobject
- ship_from_detailsnullableobject
- shipping_costnullableobject
- tax_datetimestamp

#### createdtimestamp

#### customernullablestring

#### livemodeboolean

#### posted_attimestamp

#### reversalnullableobject

#### ship_from_detailsnullableobject

#### shipping_costnullableobject

#### tax_datetimestamp

```
{"id":"tax_1NaS0I2eZvKYlo2CRuMhUcmz","object":"tax.transaction","created":1690932566,"currency":"usd","customer":null,"customer_details":{"address":{"city":"South San Francisco","country":"US","line1":"354 Oyster Point Blvd","line2":"","postal_code":"94080","state":"CA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"line_items":{"object":"list","data":[{"id":"tax_li_ONCP443tgfS8I1","object":"tax.transaction_line_item","amount":1499,"amount_tax":148,"livemode":false,"metadata":null,"product":null,"quantity":1,"reference":"Pepperoni Pizza","reversal":null,"tax_behavior":"exclusive","tax_code":"txcd_40060003","type":"transaction"}],"has_more":false,"url":"/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz/line_items"},"livemode":false,"metadata":null,"posted_at":1690932566,"reference":"myOrder_123","reversal":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"ship_from_details":{"address":{"postal_code":"75001","state":"TX","country":"US"}},"tax_date":1690932566,"type":"transaction"}
```

```
{"id":"tax_1NaS0I2eZvKYlo2CRuMhUcmz","object":"tax.transaction","created":1690932566,"currency":"usd","customer":null,"customer_details":{"address":{"city":"South San Francisco","country":"US","line1":"354 Oyster Point Blvd","line2":"","postal_code":"94080","state":"CA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"line_items":{"object":"list","data":[{"id":"tax_li_ONCP443tgfS8I1","object":"tax.transaction_line_item","amount":1499,"amount_tax":148,"livemode":false,"metadata":null,"product":null,"quantity":1,"reference":"Pepperoni Pizza","reversal":null,"tax_behavior":"exclusive","tax_code":"txcd_40060003","type":"transaction"}],"has_more":false,"url":"/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz/line_items"},"livemode":false,"metadata":null,"posted_at":1690932566,"reference":"myOrder_123","reversal":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"ship_from_details":{"address":{"postal_code":"75001","state":"TX","country":"US"}},"tax_date":1690932566,"type":"transaction"}
```

# Create a reversal transaction
Partially or fully reverses a previously createdTransaction.

### Parameters
- modeenumRequiredIfpartial, the provided line item or shipping cost amounts are reversed. Iffull, the original transaction is fully reversed.Possible enum valuesfullThe original transaction is fully reversed.partialThe provided line item amounts are reversed.
- original_transactionstringRequiredThe ID of the Transaction to partially or fully reverse.
- referencestringRequiredA custom identifier for this reversal, such asmyOrder_123-refund_1, which must be unique across all transactions. The reference helps identify this reversal transaction in exportedtax reports.The maximum length is 500 characters.
- flat_amountintegerRequired if mode=partial and line_items nor shipping_cost providedA flat amount to reverse across the entire transaction, in thesmallest currency unitin negative. This value represents the total amount to refund from the transaction, including taxes.
- line_itemsarray of objectsRequired if mode=partial and neither shipping_cost nor flat_amount is providedThe line item amounts to reverse.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### modeenumRequired

[TABLE]
fullThe original transaction is fully reversed.
partialThe provided line item amounts are reversed.
[/TABLE]

#### original_transactionstringRequired

#### referencestringRequired

#### flat_amountintegerRequired if mode=partial and line_items nor shipping_cost provided

#### line_itemsarray of objectsRequired if mode=partial and neither shipping_cost nor flat_amount is provided

#### metadataobject

### More parametersExpand all
- shipping_costobjectRequired if mode=partial and neither line_items nor flat_amount is provided

#### shipping_costobjectRequired if mode=partial and neither line_items nor flat_amount is provided

### Returns
A new TaxTransactionobject representing the reversal.

```
curlhttps://api.stripe.com/v1/tax/transactions/create_reversal \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d mode=partial \-d original_transaction=tax_1NaTVd2eZvKYlo2CoOX2Nf7P \-d reference=myOrder_123-refund_1 \-d"line_items[0][amount]"=-1499 \-d"line_items[0][amount_tax]"=-148 \-d"line_items[0][original_line_item]"=tax_li_ONDxh8JZw14sP8 \-d"line_items[0][reference]"="refund of Pepperoni Pizza"\-d"expand[0]"=line_items
```

```
curlhttps://api.stripe.com/v1/tax/transactions/create_reversal \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d mode=partial \-d original_transaction=tax_1NaTVd2eZvKYlo2CoOX2Nf7P \-d reference=myOrder_123-refund_1 \-d"line_items[0][amount]"=-1499 \-d"line_items[0][amount_tax]"=-148 \-d"line_items[0][original_line_item]"=tax_li_ONDxh8JZw14sP8 \-d"line_items[0][reference]"="refund of Pepperoni Pizza"\-d"expand[0]"=line_items
```

```
{"id":"tax_1NaTVd2eZvKYlo2CoOX2Nf7P","object":"tax.transaction","created":1690938353,"currency":"usd","customer":null,"customer_details":{"address":{"city":null,"country":"US","line1":"354 Oyster Point Blvd","line2":"","postal_code":"94080","state":"CA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"line_items":{"object":"list","data":[{"id":"tax_li_ONDxh8JZw14sP8","object":"tax.transaction_line_item","amount":1499,"amount_tax":148,"livemode":false,"metadata":null,"product":null,"quantity":1,"reference":"Pepperoni Pizza","reversal":null,"tax_behavior":"exclusive","tax_code":"txcd_40060003","type":"transaction"}],"has_more":false,"url":"/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items"},"livemode":false,"metadata":null,"posted_at":1690932566,"reference":"myOrder_123","reversal":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_date":1690938353,"type":"transaction"}
```

```
{"id":"tax_1NaTVd2eZvKYlo2CoOX2Nf7P","object":"tax.transaction","created":1690938353,"currency":"usd","customer":null,"customer_details":{"address":{"city":null,"country":"US","line1":"354 Oyster Point Blvd","line2":"","postal_code":"94080","state":"CA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"line_items":{"object":"list","data":[{"id":"tax_li_ONDxh8JZw14sP8","object":"tax.transaction_line_item","amount":1499,"amount_tax":148,"livemode":false,"metadata":null,"product":null,"quantity":1,"reference":"Pepperoni Pizza","reversal":null,"tax_behavior":"exclusive","tax_code":"txcd_40060003","type":"transaction"}],"has_more":false,"url":"/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items"},"livemode":false,"metadata":null,"posted_at":1690932566,"reference":"myOrder_123","reversal":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_date":1690938353,"type":"transaction"}
```

# Create a transaction from a calculation
Creates a Tax Transaction from a calculation, if that calculation hasn’t expired. Calculations expire after 90 days.

### Parameters
- calculationstringRequiredTax Calculation ID to be used as input when creating the transaction.
- referencestringRequiredA custom order or sale identifier, such as ‘myOrder_123’. Must be unique across all transactions, including reversals.The maximum length is 500 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### calculationstringRequired

#### referencestringRequired

#### metadataobject

### More parametersExpand all
- posted_attimestamp

#### posted_attimestamp

### Returns
A TaxTransactionobject.

```
curlhttps://api.stripe.com/v1/tax/transactions/create_from_calculation \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d calculation=taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2 \-d reference=myOrder_123 \-d"expand[]"=line_items
```

```
curlhttps://api.stripe.com/v1/tax/transactions/create_from_calculation \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d calculation=taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2 \-d reference=myOrder_123 \-d"expand[]"=line_items
```

```
{"id":"tax_1NaTVd2eZvKYlo2CoOX2Nf7P","object":"tax.transaction","created":1690938353,"currency":"usd","customer":null,"customer_details":{"address":{"city":null,"country":"US","line1":"354 Oyster Point Blvd","line2":"","postal_code":"94080","state":"CA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"line_items":{"object":"list","data":[{"id":"tax_li_ONDxh8JZw14sP8","object":"tax.transaction_line_item","amount":1499,"amount_tax":148,"livemode":false,"metadata":null,"product":null,"quantity":1,"reference":"Pepperoni Pizza","reversal":null,"tax_behavior":"exclusive","tax_code":"txcd_40060003","type":"transaction"}],"has_more":false,"url":"/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items"},"livemode":false,"metadata":null,"posted_at":1690932566,"reference":"myOrder_123","reversal":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_date":1690938353,"type":"transaction"}
```

```
{"id":"tax_1NaTVd2eZvKYlo2CoOX2Nf7P","object":"tax.transaction","created":1690938353,"currency":"usd","customer":null,"customer_details":{"address":{"city":null,"country":"US","line1":"354 Oyster Point Blvd","line2":"","postal_code":"94080","state":"CA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"line_items":{"object":"list","data":[{"id":"tax_li_ONDxh8JZw14sP8","object":"tax.transaction_line_item","amount":1499,"amount_tax":148,"livemode":false,"metadata":null,"product":null,"quantity":1,"reference":"Pepperoni Pizza","reversal":null,"tax_behavior":"exclusive","tax_code":"txcd_40060003","type":"transaction"}],"has_more":false,"url":"/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items"},"livemode":false,"metadata":null,"posted_at":1690932566,"reference":"myOrder_123","reversal":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_date":1690938353,"type":"transaction"}
```

# Retrieve a transaction
Retrieves a TaxTransactionobject.

### Parameters
Noparameters.

### Returns
A TaxTransactionobject.

```
curlhttps://api.stripe.com/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"tax_1NaS0I2eZvKYlo2CRuMhUcmz","object":"tax.transaction","created":1690932566,"currency":"usd","customer":null,"customer_details":{"address":{"city":"South San Francisco","country":"US","line1":"354 Oyster Point Blvd","line2":"","postal_code":"94080","state":"CA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"line_items":{"object":"list","data":[{"id":"tax_li_ONCP443tgfS8I1","object":"tax.transaction_line_item","amount":1499,"amount_tax":148,"livemode":false,"metadata":null,"product":null,"quantity":1,"reference":"Pepperoni Pizza","reversal":null,"tax_behavior":"exclusive","tax_code":"txcd_40060003","type":"transaction"}],"has_more":false,"url":"/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz/line_items"},"livemode":false,"metadata":null,"posted_at":1690932566,"reference":"myOrder_123","reversal":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"ship_from_details":{"address":{"postal_code":"75001","state":"TX","country":"US"}},"tax_date":1690932566,"type":"transaction"}
```

```
{"id":"tax_1NaS0I2eZvKYlo2CRuMhUcmz","object":"tax.transaction","created":1690932566,"currency":"usd","customer":null,"customer_details":{"address":{"city":"South San Francisco","country":"US","line1":"354 Oyster Point Blvd","line2":"","postal_code":"94080","state":"CA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"line_items":{"object":"list","data":[{"id":"tax_li_ONCP443tgfS8I1","object":"tax.transaction_line_item","amount":1499,"amount_tax":148,"livemode":false,"metadata":null,"product":null,"quantity":1,"reference":"Pepperoni Pizza","reversal":null,"tax_behavior":"exclusive","tax_code":"txcd_40060003","type":"transaction"}],"has_more":false,"url":"/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz/line_items"},"livemode":false,"metadata":null,"posted_at":1690932566,"reference":"myOrder_123","reversal":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"ship_from_details":{"address":{"postal_code":"75001","state":"TX","country":"US"}},"tax_date":1690932566,"type":"transaction"}
```