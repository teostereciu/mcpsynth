# climate/order

*Source: https://docs.stripe.com/api/climate/order*

---

# Climate Order
Orders represent your intent to purchase a particular Climate product. When you create an order, thepayment is deducted from your merchant balance.

# The Climate order object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- amount_feesintegerTotal amount ofFrontier’s service fees in the currency’s smallest unit.
- amount_subtotalintegerTotal amount of the carbon removal in the currency’s smallest unit.
- amount_totalintegerTotal amount of the order including fees in the currency’s smallest unit.
- beneficiarynullableobjectPublicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.Show child attributes
- canceled_atnullabletimestampTime at which the order was canceled. Measured in seconds since the Unix epoch.
- cancellation_reasonnullableenumReason for the cancellation of this order.Possible enum valuesexpiredOrder was not confirmed and expired automaticallyproduct_unavailableOrder could not be fulfilled because the product is no longer availablerequestedOrder was canceled by a cancellation request
- certificatenullablestringFor delivered orders, a URL to a delivery certificate for the order.
- confirmed_atnullabletimestampTime at which the order was confirmed. Measured in seconds since the Unix epoch.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencystringThree-letterISO currency code, in lowercase, representing the currency for this order.
- delayed_atnullabletimestampTime at which the order’s expected_delivery_year was delayed. Measured in seconds since the Unix epoch.
- delivered_atnullabletimestampTime at which the order was delivered. Measured in seconds since the Unix epoch.
- delivery_detailsarray of objectsDetails about the delivery of carbon removal for this order.Show child attributes
- expected_delivery_yearintegerThe year this order is expected to be delivered.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- metric_tonsdecimal stringQuantity of carbon removal that is included in this order.
- productstringExpandableUnique ID for the ClimateProductthis order is purchasing.
- product_substituted_atnullabletimestampTime at which the order’s product was substituted for a different product. Measured in seconds since the Unix epoch.
- statusenumThe current status of this order.Possible enum valuesawaiting_fundsStatus when an order has been attached to a funding_source and is awaiting it’s settlementcanceledStatus when an order has been canceledconfirmedStatus when an order has been successfully confirmed and payment has been madedeliveredStatus when an order has been delivered

#### idstring

#### objectstring

#### amount_feesinteger

#### amount_subtotalinteger

#### amount_totalinteger

#### beneficiarynullableobject

#### canceled_atnullabletimestamp

#### cancellation_reasonnullableenum

[TABLE]
expiredOrder was not confirmed and expired automatically
product_unavailableOrder could not be fulfilled because the product is no longer available
requestedOrder was canceled by a cancellation request
[/TABLE]

```
product_unavailable
```

#### certificatenullablestring

#### confirmed_atnullabletimestamp

#### createdtimestamp

#### currencystring

#### delayed_atnullabletimestamp

#### delivered_atnullabletimestamp

#### delivery_detailsarray of objects

#### expected_delivery_yearinteger

#### livemodeboolean

#### metadataobject

#### metric_tonsdecimal string

#### productstringExpandable

#### product_substituted_atnullabletimestamp

#### statusenum

[TABLE]
awaiting_fundsStatus when an order has been attached to a funding_source and is awaiting it’s settlement
canceledStatus when an order has been canceled
confirmedStatus when an order has been successfully confirmed and payment has been made
deliveredStatus when an order has been delivered
[/TABLE]

```
awaiting_funds
```

```
{"id":"climorder_1aTnU0B63jkB3XAQKUbA5yyl","object":"climate.order","amount_fees":17,"amount_subtotal":550,"amount_total":567,"beneficiary":{"public_name":"{{YOUR_BUSINESS_NAME}}"},"canceled_at":null,"cancellation_reason":null,"certificate":null,"confirmed_at":1881439205,"created":1881439205,"currency":"usd","delayed_at":null,"delivered_at":null,"delivery_details":[],"expected_delivery_year":2027,"livemode":false,"metadata":{},"metric_tons":"0.01","product":"climsku_frontier_offtake_portfolio_2027","product_substituted_at":null,"status":"confirmed"}
```

```
{"id":"climorder_1aTnU0B63jkB3XAQKUbA5yyl","object":"climate.order","amount_fees":17,"amount_subtotal":550,"amount_total":567,"beneficiary":{"public_name":"{{YOUR_BUSINESS_NAME}}"},"canceled_at":null,"cancellation_reason":null,"certificate":null,"confirmed_at":1881439205,"created":1881439205,"currency":"usd","delayed_at":null,"delivered_at":null,"delivery_details":[],"expected_delivery_year":2027,"livemode":false,"metadata":{},"metric_tons":"0.01","product":"climsku_frontier_offtake_portfolio_2027","product_substituted_at":null,"status":"confirmed"}
```

# Create an order
Creates a Climate order object for a given Climate product. The order will be processed immediatelyafter creation and payment will be deducted your Stripe balance.

### Parameters
- productstringRequiredUnique identifier of the Climate product.
- amountintegerRequested amount of carbon removal units. Either this ormetric_tonsmust be specified.
- beneficiaryobjectPublicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.Show child parameters
- currencystringRequest currency for the order as a three-letterISO currency code, in lowercase. Must be a supportedsettlement currency for your account. If omitted, the account’s default currency will be used.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- metric_tonsstringRequested number of tons for the order. Either this oramountmust be specified.

#### productstringRequired

#### amountinteger

#### beneficiaryobject

#### currencystring

#### metadataobject

#### metric_tonsstring

### Returns
The new Climate order object.

```
curlhttps://api.stripe.com/v1/climate/orders \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d metric_tons="0.01"\-d product=climsku_frontier_offtake_portfolio_2027
```

```
curlhttps://api.stripe.com/v1/climate/orders \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d metric_tons="0.01"\-d product=climsku_frontier_offtake_portfolio_2027
```

```
{"id":"climorder_1aTnU0B63jkB3XAQKUbA5yyl","object":"climate.order","amount_fees":17,"amount_subtotal":550,"amount_total":567,"beneficiary":{"public_name":"{{YOUR_BUSINESS_NAME}}"},"canceled_at":null,"cancellation_reason":null,"certificate":null,"confirmed_at":1881439205,"created":1881439205,"currency":"usd","delayed_at":null,"delivered_at":null,"delivery_details":[],"expected_delivery_year":2027,"livemode":false,"metadata":{},"metric_tons":"0.01","product":"climsku_frontier_offtake_portfolio_2027","product_substituted_at":null,"status":"confirmed"}
```

```
{"id":"climorder_1aTnU0B63jkB3XAQKUbA5yyl","object":"climate.order","amount_fees":17,"amount_subtotal":550,"amount_total":567,"beneficiary":{"public_name":"{{YOUR_BUSINESS_NAME}}"},"canceled_at":null,"cancellation_reason":null,"certificate":null,"confirmed_at":1881439205,"created":1881439205,"currency":"usd","delayed_at":null,"delivered_at":null,"delivery_details":[],"expected_delivery_year":2027,"livemode":false,"metadata":{},"metric_tons":"0.01","product":"climsku_frontier_offtake_portfolio_2027","product_substituted_at":null,"status":"confirmed"}
```

# Update an order
Updates the specified order by setting the values of the parameters passed.

### Parameters
- orderstringRequiredUnique identifier of the order.
- beneficiaryobjectPublicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### orderstringRequired

#### beneficiaryobject

#### metadataobject

### Returns
The updated Climate order object.

```
curlhttps://api.stripe.com/v1/climate/orders/climorder_1aTnU0B63jkB3XAQKUbA5yyl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/climate/orders/climorder_1aTnU0B63jkB3XAQKUbA5yyl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"climorder_1aTnU0B63jkB3XAQKUbA5yyl","object":"climate.order","amount_fees":17,"amount_subtotal":550,"amount_total":567,"beneficiary":{"public_name":"{{YOUR_BUSINESS_NAME}}"},"canceled_at":null,"cancellation_reason":null,"certificate":null,"confirmed_at":1881439205,"created":1881439205,"currency":"usd","delayed_at":null,"delivered_at":null,"delivery_details":[],"expected_delivery_year":2027,"livemode":false,"metadata":{"order_id":"6735"},"metric_tons":"0.01","product":"climsku_frontier_offtake_portfolio_2027","product_substituted_at":null,"status":"confirmed"}
```

```
{"id":"climorder_1aTnU0B63jkB3XAQKUbA5yyl","object":"climate.order","amount_fees":17,"amount_subtotal":550,"amount_total":567,"beneficiary":{"public_name":"{{YOUR_BUSINESS_NAME}}"},"canceled_at":null,"cancellation_reason":null,"certificate":null,"confirmed_at":1881439205,"created":1881439205,"currency":"usd","delayed_at":null,"delivered_at":null,"delivery_details":[],"expected_delivery_year":2027,"livemode":false,"metadata":{"order_id":"6735"},"metric_tons":"0.01","product":"climsku_frontier_offtake_portfolio_2027","product_substituted_at":null,"status":"confirmed"}
```

# Retrieve an order
Retrieves the details of a Climate order object with the given ID.

### Parameters
- orderstringRequiredUnique identifier of the order.

#### orderstringRequired

### Returns
Returns a Climate order object if a valid identifier was provided. Throws an error otherwise.

```
curlhttps://api.stripe.com/v1/climate/orders/climorder_1aTnU0B63jkB3XAQKUbA5yyl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/climate/orders/climorder_1aTnU0B63jkB3XAQKUbA5yyl \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"climorder_1aTnU0B63jkB3XAQKUbA5yyl","object":"climate.order","amount_fees":17,"amount_subtotal":550,"amount_total":567,"beneficiary":{"public_name":"{{YOUR_BUSINESS_NAME}}"},"canceled_at":null,"cancellation_reason":null,"certificate":null,"confirmed_at":1881439205,"created":1881439205,"currency":"usd","delayed_at":null,"delivered_at":null,"delivery_details":[],"expected_delivery_year":2027,"livemode":false,"metadata":{},"metric_tons":"0.01","product":"climsku_frontier_offtake_portfolio_2027","product_substituted_at":null,"status":"confirmed"}
```

```
{"id":"climorder_1aTnU0B63jkB3XAQKUbA5yyl","object":"climate.order","amount_fees":17,"amount_subtotal":550,"amount_total":567,"beneficiary":{"public_name":"{{YOUR_BUSINESS_NAME}}"},"canceled_at":null,"cancellation_reason":null,"certificate":null,"confirmed_at":1881439205,"created":1881439205,"currency":"usd","delayed_at":null,"delivered_at":null,"delivery_details":[],"expected_delivery_year":2027,"livemode":false,"metadata":{},"metric_tons":"0.01","product":"climsku_frontier_offtake_portfolio_2027","product_substituted_at":null,"status":"confirmed"}
```