# customer_balance_transactions

*Source: https://docs.stripe.com/api/customer_balance_transactions*

---

# Customer Balance Transaction
Each customer has aBalancevalue,which denotes a debit or credit that’s automatically applied to their next invoice upon finalization.You may modify the value directly by using theupdate customer API,or by creating a Customer Balance Transaction, which increments or decrements the customer’sbalanceby the specifiedamount.
Related guide:Customer balance

# The Customer Balance Transaction object

### Attributes
- idstringUnique identifier for the object.
- amountintegerThe amount of the transaction. A negative value is a credit for the customer’s balance, and a positive value is a debit to the customer’sbalance.
- currencyenumThree-letterISO currency code, in lowercase. Must be asupported currency.
- customerstringExpandableThe ID of the customer the transaction belongs to.
- customer_accountnullablestringThe ID of an Account representing a customer that the transaction belongs to.
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.
- ending_balanceintegerThe customer’sbalanceafter the transaction was applied. A negative value decreases the amount due on the customer’s next invoice. A positive value increases the amount due on the customer’s next invoice.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- typeenumTransaction type:adjustment,applied_to_invoice,credit_note,initial,invoice_overpaid,invoice_too_large,invoice_too_small,unspent_receiver_credit,unapplied_from_invoice,checkout_session_subscription_payment, orcheckout_session_subscription_payment_canceled. See theCustomer Balance pageto learn more about transaction types.Possible enum valuesadjustmentAn explicitly created adjustment transaction to debit or credit the credit balance.applied_to_invoiceTraces the application of credit against a linked Invoice.checkout_session_subscription_paymentTraces the customer balance applied to an Invoice to be created for the linked Checkout Session.checkout_session_subscription_payment_canceledTraces the reversal of an applied balance by the linked Checkout Session. Paired with an earlier ‘checkout_session_subscription_payment‘ transaction.credit_noteTraces the creation of credit to a Credit Note and its associated Invoice.initialThe starting value of the customer’s credit balance.invoice_overpaidCredits to the credit balance when an invoice receives payments exceeding the amount due.invoice_too_largeDebits to the credit balance when the amount due on an invoice is greater than Stripe’s maximum chargeable amount and the customer does not have a cash balance.invoice_too_smallDebits to the credit balance when the amount due on an invoice is less than Stripe’s minimum chargeable amount and the customer does not have a cash balance.migrationFunds migrated from the legacy customer credit balance.Show 2 more

#### idstring

#### amountinteger

#### currencyenum

#### customerstringExpandable

#### customer_accountnullablestring

#### descriptionnullablestring

#### ending_balanceinteger

#### metadatanullableobject

#### typeenum

[TABLE]
adjustmentAn explicitly created adjustment transaction to debit or credit the credit balance.
applied_to_invoiceTraces the application of credit against a linked Invoice.
checkout_session_subscription_paymentTraces the customer balance applied to an Invoice to be created for the linked Checkout Session.
checkout_session_subscription_payment_canceledTraces the reversal of an applied balance by the linked Checkout Session. Paired with an earlier ‘checkout_session_subscription_payment‘ transaction.
credit_noteTraces the creation of credit to a Credit Note and its associated Invoice.
initialThe starting value of the customer’s credit balance.
invoice_overpaidCredits to the credit balance when an invoice receives payments exceeding the amount due.
invoice_too_largeDebits to the credit balance when the amount due on an invoice is greater than Stripe’s maximum chargeable amount and the customer does not have a cash balance.
invoice_too_smallDebits to the credit balance when the amount due on an invoice is less than Stripe’s minimum chargeable amount and the customer does not have a cash balance.
migrationFunds migrated from the legacy customer credit balance.
Show 2 more
[/TABLE]

```
applied_to_invoice
```

```
checkout_session_subscription_payment
```

```
checkout_session_subscription_payment_canceled
```

```
credit_note
```

```
invoice_overpaid
```

```
invoice_too_large
```

```
invoice_too_small
```

### More attributesExpand all
- objectstring
- checkout_sessionnullablestringExpandable
- createdtimestamp
- credit_notenullablestringExpandable
- invoicenullablestringExpandable
- livemodeboolean

#### objectstring

#### checkout_sessionnullablestringExpandable

#### createdtimestamp

#### credit_notenullablestringExpandable

#### invoicenullablestringExpandable

#### livemodeboolean

```
{"id":"cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI","object":"customer_balance_transaction","amount":-500,"created":1680216086,"credit_note":null,"currency":"usd","customer":"cus_NcjdgdwZyI9Rj7","description":null,"ending_balance":-500,"invoice":null,"livemode":false,"metadata":{},"type":"adjustment"}
```

```
{"id":"cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI","object":"customer_balance_transaction","amount":-500,"created":1680216086,"credit_note":null,"currency":"usd","customer":"cus_NcjdgdwZyI9Rj7","description":null,"ending_balance":-500,"invoice":null,"livemode":false,"metadata":{},"type":"adjustment"}
```

# Create a customer balance transaction
Creates an immutable transaction that updates the customer’s creditbalance.

### Parameters
- amountintegerRequiredThe integer amount incentsto apply to the customer’s credit balance.
- currencyenumRequiredThree-letterISO currency code, in lowercase. Must be asupported currency. Specifies theinvoice_credit_balancethat this transaction will apply to. If the customer’scurrencyis not set, it will be updated to this value.
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.The maximum length is 350 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### amountintegerRequired

#### currencyenumRequired

```
invoice_credit_balance
```

#### descriptionstring

#### metadataobject

### Returns
Returns a customer balance transaction object if the call succeeded.

```
curlhttps://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=-500 \-d currency=usd
```

```
curlhttps://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d amount=-500 \-d currency=usd
```

```
{"id":"cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI","object":"customer_balance_transaction","amount":-500,"created":1680216086,"credit_note":null,"currency":"usd","customer":"cus_NcjdgdwZyI9Rj7","description":null,"ending_balance":-500,"invoice":null,"livemode":false,"metadata":{},"type":"adjustment"}
```

```
{"id":"cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI","object":"customer_balance_transaction","amount":-500,"created":1680216086,"credit_note":null,"currency":"usd","customer":"cus_NcjdgdwZyI9Rj7","description":null,"ending_balance":-500,"invoice":null,"livemode":false,"metadata":{},"type":"adjustment"}
```

# Update a customer credit balance transaction
Most credit balance transaction fields are immutable, but you may update itsdescriptionandmetadata.

### Parameters
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.The maximum length is 350 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### descriptionstring

#### metadataobject

### Returns
Returns a customer balance transaction object if the call succeeded.

```
curlhttps://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI","object":"customer_balance_transaction","amount":-500,"created":1680216086,"credit_note":null,"currency":"usd","customer":"cus_NcjdgdwZyI9Rj7","description":null,"ending_balance":-500,"invoice":null,"livemode":false,"metadata":{"order_id":"6735"},"type":"adjustment"}
```

```
{"id":"cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI","object":"customer_balance_transaction","amount":-500,"created":1680216086,"credit_note":null,"currency":"usd","customer":"cus_NcjdgdwZyI9Rj7","description":null,"ending_balance":-500,"invoice":null,"livemode":false,"metadata":{"order_id":"6735"},"type":"adjustment"}
```

# Retrieve a customer balance transaction
Retrieves a specific customer balance transaction that updated the customer’sbalances.

### Parameters
Noparameters.

### Returns
Returns a customer balance transaction object if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI","object":"customer_balance_transaction","amount":-500,"created":1680216086,"credit_note":null,"currency":"usd","customer":"cus_NcjdgdwZyI9Rj7","description":null,"ending_balance":-500,"invoice":null,"livemode":false,"metadata":{},"type":"adjustment"}
```

```
{"id":"cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI","object":"customer_balance_transaction","amount":-500,"created":1680216086,"credit_note":null,"currency":"usd","customer":"cus_NcjdgdwZyI9Rj7","description":null,"ending_balance":-500,"invoice":null,"livemode":false,"metadata":{},"type":"adjustment"}
```