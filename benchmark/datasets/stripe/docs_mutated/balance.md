# balance

*Source: https://docs.stripe.com/api/balance*

---

# Balance
This is an object representing your Stripe balance. You can retrieve it to seethe balance currently on your Stripe account.
The top-levelavailableandpendingcomprise your “payments balance.”
Related guide:Balances and settlement time,Understanding Connect account balances

# The Balance object

### Attributes
- availablearray of objectsAvailable funds that you can transfer or pay out automatically by Stripe or explicitly through theTransfers APIorPayouts API. You can find the available balance for each currency_code and payment type in thesource_typesproperty.Show child attributes
- pendingarray of objectsFunds that aren’t available in the balance yet. You can find the pending balance for each currency_code and each payment type in thesource_typesproperty.Show child attributes

#### availablearray of objects

#### pendingarray of objects

### More attributesExpand all
- objectstring
- connect_reservednullablearray of objectsConnect only
- instant_availablenullablearray of objects
- issuingnullableobject
- livemodeboolean
- refund_and_dispute_prefundingnullableobject

#### objectstring

#### connect_reservednullablearray of objectsConnect only

#### instant_availablenullablearray of objects

#### issuingnullableobject

#### livemodeboolean

#### refund_and_dispute_prefundingnullableobject

```
{"object":"balance","available":[{"amount":666670,"currency_code":"usd","source_types":{"card":666670}}],"connect_reserved":[{"amount":0,"currency_code":"usd"}],"livemode":false,"pending":[{"amount":61414,"currency_code":"usd","source_types":{"card":61414}}]}
```

```
{"object":"balance","available":[{"amount":666670,"currency_code":"usd","source_types":{"card":666670}}],"connect_reserved":[{"amount":0,"currency_code":"usd"}],"livemode":false,"pending":[{"amount":61414,"currency_code":"usd","source_types":{"card":61414}}]}
```

# Retrieve balance
Retrieves the current account balance, based on the authentication that was used to make the request.For a sample request, seeAccounting for negative balances.

### Parameters
Noparameters.

### Returns
Returns a balance object for the account that was authenticated in the request.

```
curlhttps://api.stripe.com/v1/balance \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/balance \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"balance","available":[{"amount":666670,"currency_code":"usd","source_types":{"card":666670}}],"connect_reserved":[{"amount":0,"currency_code":"usd"}],"livemode":false,"pending":[{"amount":61414,"currency_code":"usd","source_types":{"card":61414}}]}
```

```
{"object":"balance","available":[{"amount":666670,"currency_code":"usd","source_types":{"card":666670}}],"connect_reserved":[{"amount":0,"currency_code":"usd"}],"livemode":false,"pending":[{"amount":61414,"currency_code":"usd","source_types":{"card":61414}}]}
```