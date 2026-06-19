# tax/calculations

*Source: https://docs.stripe.com/api/tax/calculations*

---

# Tax Calculations
A Tax Calculation allows you to calculate the tax to collect from your customer.
Related guide:Calculate tax in your custom payment flow

# The Tax Calculation object

### Attributes
- idnullablestringUnique identifier for the calculation.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amount_totalintegerTotal amount after taxes in thesmallest currency unit.
- currencystringThree-letterISO currency code, in lowercase. Must be asupported currency.
- customer_detailsobjectThe customer’s details, such as address and tax IDs.Show child attributes
- expires_atnullabletimestampTimestamp of date at which the tax calculation will expire.
- line_itemsnullableobjectExpandableThe list of items the customer is purchasing.Show child attributes
- shipping_costnullableobjectThe shipping cost details for the calculation.Show child attributes
- tax_amount_exclusiveintegerThe amount of tax to be collected on top of the line item prices.
- tax_amount_inclusiveintegerThe amount of tax already included in the line item prices.
- tax_breakdownarray of objectsBreakdown of individual tax amounts that add up to the total.Show child attributes

#### idnullablestring

#### objectstring

#### amount_totalinteger

#### currencystring

#### customer_detailsobject

#### expires_atnullabletimestamp

#### line_itemsnullableobjectExpandable

#### shipping_costnullableobject

#### tax_amount_exclusiveinteger

#### tax_amount_inclusiveinteger

#### tax_breakdownarray of objects

### More attributesExpand all
- customernullablestring
- livemodeboolean
- ship_from_detailsnullableobject
- tax_datetimestamp

#### customernullablestring

#### livemodeboolean

#### ship_from_detailsnullableobject

#### tax_datetimestamp

```
{"id":"taxcalc_1OduxkBUZ691iUZ4iWvpMApI","object":"tax.calculation","amount_total":1953,"currency":"usd","customer":null,"customer_details":{"address":{"city":"Seattle","country":"US","line1":"920 5th Ave","line2":null,"postal_code":"98104","state":"WA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"expires_at":1706708005,"line_items":{"object":"list","data":[{"id":"tax_li_PSqf3RMNZa23H4","object":"tax.calculation_line_item","amount":1499,"amount_tax":154,"livemode":false,"product":null,"quantity":1,"reference":"Music Streaming Coupon","tax_behavior":"exclusive","tax_code":"txcd_10000000"}],"has_more":false,"total_count":1,"url":"/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"},"livemode":false,"ship_from_details":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_amount_exclusive":154,"tax_amount_inclusive":0,"tax_breakdown":[{"amount":154,"inclusive":false,"tax_rate_details":{"country":"US","percentage_decimal":"10.25","state":"WA","tax_type":"sales_tax"},"taxability_reason":"standard_rated","taxable_amount":1499},{"amount":0,"inclusive":false,"tax_rate_details":{"country":"DE","percentage_decimal":"0.0","state":null,"tax_type":"vat"},"taxability_reason":"zero_rated","taxable_amount":300}],"tax_date":1706535204}
```

```
{"id":"taxcalc_1OduxkBUZ691iUZ4iWvpMApI","object":"tax.calculation","amount_total":1953,"currency":"usd","customer":null,"customer_details":{"address":{"city":"Seattle","country":"US","line1":"920 5th Ave","line2":null,"postal_code":"98104","state":"WA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"expires_at":1706708005,"line_items":{"object":"list","data":[{"id":"tax_li_PSqf3RMNZa23H4","object":"tax.calculation_line_item","amount":1499,"amount_tax":154,"livemode":false,"product":null,"quantity":1,"reference":"Music Streaming Coupon","tax_behavior":"exclusive","tax_code":"txcd_10000000"}],"has_more":false,"total_count":1,"url":"/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"},"livemode":false,"ship_from_details":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_amount_exclusive":154,"tax_amount_inclusive":0,"tax_breakdown":[{"amount":154,"inclusive":false,"tax_rate_details":{"country":"US","percentage_decimal":"10.25","state":"WA","tax_type":"sales_tax"},"taxability_reason":"standard_rated","taxable_amount":1499},{"amount":0,"inclusive":false,"tax_rate_details":{"country":"DE","percentage_decimal":"0.0","state":null,"tax_type":"vat"},"taxability_reason":"zero_rated","taxable_amount":300}],"tax_date":1706535204}
```

# Create a Tax Calculation
Calculates tax based on the input and returns a TaxCalculationobject.

### Parameters
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency.
- line_itemsarray of objectsRequiredA list of items the customer is purchasing.Show child parameters
- customer_detailsobjectRequired unless customer providedDetails about the customer, including address and tax IDs.Show child parameters
- shipping_costobjectShipping cost details to be used for the calculation.Show child parameters

#### currencyenumRequired

#### line_itemsarray of objectsRequired

#### customer_detailsobjectRequired unless customer provided

#### shipping_costobject

### More parametersExpand all
- customerstringRequired unless customer_details provided
- ship_from_detailsobject
- tax_dateinteger

#### customerstringRequired unless customer_details provided

#### ship_from_detailsobject

#### tax_dateinteger

### Returns
A TaxCalculationobject containing the first 100 inputline_itemsif the calculation succeeds. Otherwise, an error (for example, indicating that the customer address was invalid).

```
curlhttps://api.stripe.com/v1/tax/calculations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d currency=usd \-d"customer_details[address][line1]"="920 5th Ave"\-d"customer_details[address][city]"=Seattle \-d"customer_details[address][state]"=WA \-d"customer_details[address][postal_code]"=98104 \-d"customer_details[address][country]"=US \-d"customer_details[address_source]"=shipping \-d"line_items[0][amount]"=1499 \-d"line_items[0][tax_code]"=txcd_10000000 \-d"line_items[0][reference]"="Music Streaming Coupon"\-d"shipping_cost[amount]"=300 \-d"expand[0]"=line_items
```

```
curlhttps://api.stripe.com/v1/tax/calculations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d currency=usd \-d"customer_details[address][line1]"="920 5th Ave"\-d"customer_details[address][city]"=Seattle \-d"customer_details[address][state]"=WA \-d"customer_details[address][postal_code]"=98104 \-d"customer_details[address][country]"=US \-d"customer_details[address_source]"=shipping \-d"line_items[0][amount]"=1499 \-d"line_items[0][tax_code]"=txcd_10000000 \-d"line_items[0][reference]"="Music Streaming Coupon"\-d"shipping_cost[amount]"=300 \-d"expand[0]"=line_items
```

```
{"id":"taxcalc_1OduxkBUZ691iUZ4iWvpMApI","object":"tax.calculation","amount_total":1953,"currency":"usd","customer":null,"customer_details":{"address":{"city":"Seattle","country":"US","line1":"920 5th Ave","line2":null,"postal_code":"98104","state":"WA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"expires_at":1706708005,"line_items":{"object":"list","data":[{"id":"tax_li_PSqf3RMNZa23H4","object":"tax.calculation_line_item","amount":1499,"amount_tax":154,"livemode":false,"product":null,"quantity":1,"reference":"Music Streaming Coupon","tax_behavior":"exclusive","tax_code":"txcd_10000000"}],"has_more":false,"total_count":1,"url":"/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"},"livemode":false,"ship_from_details":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_amount_exclusive":154,"tax_amount_inclusive":0,"tax_breakdown":[{"amount":154,"inclusive":false,"tax_rate_details":{"country":"US","percentage_decimal":"10.25","state":"WA","tax_type":"sales_tax"},"taxability_reason":"standard_rated","taxable_amount":1499},{"amount":0,"inclusive":false,"tax_rate_details":{"country":"DE","percentage_decimal":"0.0","state":null,"tax_type":"vat"},"taxability_reason":"zero_rated","taxable_amount":300}],"tax_date":1706535204}
```

```
{"id":"taxcalc_1OduxkBUZ691iUZ4iWvpMApI","object":"tax.calculation","amount_total":1953,"currency":"usd","customer":null,"customer_details":{"address":{"city":"Seattle","country":"US","line1":"920 5th Ave","line2":null,"postal_code":"98104","state":"WA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"expires_at":1706708005,"line_items":{"object":"list","data":[{"id":"tax_li_PSqf3RMNZa23H4","object":"tax.calculation_line_item","amount":1499,"amount_tax":154,"livemode":false,"product":null,"quantity":1,"reference":"Music Streaming Coupon","tax_behavior":"exclusive","tax_code":"txcd_10000000"}],"has_more":false,"total_count":1,"url":"/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"},"livemode":false,"ship_from_details":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_amount_exclusive":154,"tax_amount_inclusive":0,"tax_breakdown":[{"amount":154,"inclusive":false,"tax_rate_details":{"country":"US","percentage_decimal":"10.25","state":"WA","tax_type":"sales_tax"},"taxability_reason":"standard_rated","taxable_amount":1499},{"amount":0,"inclusive":false,"tax_rate_details":{"country":"DE","percentage_decimal":"0.0","state":null,"tax_type":"vat"},"taxability_reason":"zero_rated","taxable_amount":300}],"tax_date":1706535204}
```

# Retrieve a calculation's line items
Retrieves the line items of a tax calculation as a collection, if the calculation hasn’t expired.

### Parameters
- ending_beforestringA cursor for use in pagination.ending_beforeis an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting withobj_bar, your subsequent call can includeending_before=obj_barin order to fetch the previous page of the list.The maximum length is 500 characters.
- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
- starting_afterstringA cursor for use in pagination.starting_afteris an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending withobj_foo, your subsequent call can includestarting_after=obj_fooin order to fetch the next page of the list.The maximum length is 500 characters.

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
A list of Line Item objects if the Tax calculation is found. Otherwise returns a ‘not found’ error.

```
curl-G https://api.stripe.com/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items","has_more":false,"data":[{"id":"tax_li_OcYJb5mQOSSSWD","object":"tax.calculation_line_item","amount":1499,"amount_tax":148,"livemode":false,"product":null,"quantity":1,"reference":"Pepperoni Pizza","tax_behavior":"exclusive","tax_code":"txcd_40060003"}]}
```

```
{"object":"list","url":"/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items","has_more":false,"data":[{"id":"tax_li_OcYJb5mQOSSSWD","object":"tax.calculation_line_item","amount":1499,"amount_tax":148,"livemode":false,"product":null,"quantity":1,"reference":"Pepperoni Pizza","tax_behavior":"exclusive","tax_code":"txcd_40060003"}]}
```

# Retrieve a Tax Calculation
Retrieves a TaxCalculationobject, if the calculation hasn’t expired.

### Parameters
Noparameters.

### Returns
A TaxCalculationobject if the Tax calculation is found. Otherwise returns a ‘not found’ error.

```
curlhttps://api.stripe.com/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"taxcalc_1OduxkBUZ691iUZ4iWvpMApI","object":"tax.calculation","amount_total":1953,"currency":"usd","customer":null,"customer_details":{"address":{"city":"Seattle","country":"US","line1":"920 5th Ave","line2":null,"postal_code":"98104","state":"WA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"expires_at":1706708005,"line_items":{"object":"list","data":[{"id":"tax_li_PSqf3RMNZa23H4","object":"tax.calculation_line_item","amount":1499,"amount_tax":154,"livemode":false,"product":null,"quantity":1,"reference":"Music Streaming Coupon","tax_behavior":"exclusive","tax_code":"txcd_10000000"}],"has_more":false,"total_count":1,"url":"/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"},"livemode":false,"ship_from_details":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_amount_exclusive":154,"tax_amount_inclusive":0,"tax_breakdown":[{"amount":154,"inclusive":false,"tax_rate_details":{"country":"US","percentage_decimal":"10.25","state":"WA","tax_type":"sales_tax"},"taxability_reason":"standard_rated","taxable_amount":1499},{"amount":0,"inclusive":false,"tax_rate_details":{"country":"DE","percentage_decimal":"0.0","state":null,"tax_type":"vat"},"taxability_reason":"zero_rated","taxable_amount":300}],"tax_date":1706535204}
```

```
{"id":"taxcalc_1OduxkBUZ691iUZ4iWvpMApI","object":"tax.calculation","amount_total":1953,"currency":"usd","customer":null,"customer_details":{"address":{"city":"Seattle","country":"US","line1":"920 5th Ave","line2":null,"postal_code":"98104","state":"WA"},"address_source":"shipping","ip_address":null,"tax_ids":[],"taxability_override":"none"},"expires_at":1706708005,"line_items":{"object":"list","data":[{"id":"tax_li_PSqf3RMNZa23H4","object":"tax.calculation_line_item","amount":1499,"amount_tax":154,"livemode":false,"product":null,"quantity":1,"reference":"Music Streaming Coupon","tax_behavior":"exclusive","tax_code":"txcd_10000000"}],"has_more":false,"total_count":1,"url":"/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"},"livemode":false,"ship_from_details":null,"shipping_cost":{"amount":300,"amount_tax":0,"tax_behavior":"exclusive","tax_code":"txcd_92010001"},"tax_amount_exclusive":154,"tax_amount_inclusive":0,"tax_breakdown":[{"amount":154,"inclusive":false,"tax_rate_details":{"country":"US","percentage_decimal":"10.25","state":"WA","tax_type":"sales_tax"},"taxability_reason":"standard_rated","taxable_amount":1499},{"amount":0,"inclusive":false,"tax_rate_details":{"country":"DE","percentage_decimal":"0.0","state":null,"tax_type":"vat"},"taxability_reason":"zero_rated","taxable_amount":300}],"tax_date":1706535204}
```