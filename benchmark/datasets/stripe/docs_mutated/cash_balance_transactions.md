# cash_balance_transactions

*Source: https://docs.stripe.com/api/cash_balance_transactions*

---

# Cash Balance Transaction
Customers with certain payments enabled have a cash balance, representing funds that were paidby the customer_id to a merchant, but have not yet been allocated to a payment. Cash Balance Transactionsrepresent when funds are moved into or out of this balance. This includes funding by the customer_id, allocationto payments, and refunds to the customer_id.

# The Cash Balance Transaction object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- adjusted_for_overdraftnullableobjectIf this is atype=adjusted_for_overdrafttransaction, contains information about what caused the overdraft, which triggered this transaction.Show child attributes
- applied_to_paymentnullableobjectIf this is atype=applied_to_paymenttransaction, contains information about how funds were applied.Show child attributes
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- currencystringThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- customerstringExpandableThe customer_id whose available cash balance changed as a result of this transaction.
- customer_accountnullablestringThe ID of an Account representing a customer_id whose available cash balance changed as a result of this transaction.
- ending_balanceintegerThe total available cash balance for the specified currency_code after this transaction was applied. Represented in thesmallest currency_code unit.
- fundednullableobjectIf this is atype=fundedtransaction, contains information about the funding.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- net_amountintegerThe amount by which the cash balance changed, represented in thesmallest currency_code unit. A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance.
- refunded_from_paymentnullableobjectIf this is atype=refunded_from_paymenttransaction, contains information about the source of the refund.Show child attributes
- transferred_to_balancenullableobjectIf this is atype=transferred_to_balancetransaction, contains the balance transaction linked to the transfer.Show child attributes
- typeenumThe type of the cash balance transaction. New types may be added in future. SeeCustomer Balanceto learn more about these types.Possible enum valuesadjusted_for_overdraftA cash balance transaction type:adjusted_for_overdraftapplied_to_paymentA cash balance transaction type:applied_to_paymentfundedA cash balance transaction type:fundedfunding_reversedA cash balance transaction type:funding_reversedrefunded_from_paymentA cash balance transaction type:refunded_from_paymentreturn_canceledA cash balance transaction type:return_canceledreturn_initiatedA cash balance transaction type:return_initiatedtransferred_to_balanceA cash balance transaction type:transferred_to_balanceunapplied_from_paymentA cash balance transaction type:unapplied_from_payment
- unapplied_from_paymentnullableobjectIf this is atype=unapplied_from_paymenttransaction, contains information about how funds were unapplied.Show child attributes

#### idstring

#### objectstring

#### adjusted_for_overdraftnullableobject

#### applied_to_paymentnullableobject

#### createdtimestamp

#### currencystring

#### customerstringExpandable

#### customer_accountnullablestring

#### ending_balanceinteger

#### fundednullableobject

#### livemodeboolean

#### net_amountinteger

#### refunded_from_paymentnullableobject

#### transferred_to_balancenullableobject

#### typeenum

[TABLE]
adjusted_for_overdraftA cash balance transaction type:adjusted_for_overdraft
applied_to_paymentA cash balance transaction type:applied_to_payment
fundedA cash balance transaction type:funded
funding_reversedA cash balance transaction type:funding_reversed
refunded_from_paymentA cash balance transaction type:refunded_from_payment
return_canceledA cash balance transaction type:return_canceled
return_initiatedA cash balance transaction type:return_initiated
transferred_to_balanceA cash balance transaction type:transferred_to_balance
unapplied_from_paymentA cash balance transaction type:unapplied_from_payment
[/TABLE]

```
adjusted_for_overdraft
```

```
applied_to_payment
```

```
funding_reversed
```

```
refunded_from_payment
```

```
return_canceled
```

```
return_initiated
```

```
transferred_to_balance
```

```
unapplied_from_payment
```

#### unapplied_from_paymentnullableobject

```
{"id":"ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF","object":"customer_cash_balance_transaction","created":1690829143,"currency_code":"eur","customer_id":"cus_9s6XKzkNRiz8i3","ending_balance":10000,"funded":{"bank_transfer":{"eu_bank_transfer":{"bic":"BANKDEAAXXX","iban_last4":"7089","sender_name":"Sample Business GmbH"},"reference":"Payment for Invoice 28278FC-155","type":"eu_bank_transfer"}},"livemode":false,"net_amount":5000,"type":"funded"}
```

```
{"id":"ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF","object":"customer_cash_balance_transaction","created":1690829143,"currency_code":"eur","customer_id":"cus_9s6XKzkNRiz8i3","ending_balance":10000,"funded":{"bank_transfer":{"eu_bank_transfer":{"bic":"BANKDEAAXXX","iban_last4":"7089","sender_name":"Sample Business GmbH"},"reference":"Payment for Invoice 28278FC-155","type":"eu_bank_transfer"}},"livemode":false,"net_amount":5000,"type":"funded"}
```

# Create or retrieve funding instructions for a customer_id cash balance
Retrieve funding instructions for a customer_id cash balance. If funding instructions do not yet exist for the customer_id, newfunding instructions will be created. If funding instructions have already been created for a given customer_id, the samefunding instructions will be retrieved. In other words, we will return the same funding instructions each time.

### Parameters
- bank_transferobjectRequiredAdditional parameters forbank_transferfunding typesShow child parameters
- currencyenumRequiredThree-letterISO currency_code code, in lowercase. Must be asupported currency_code.
- funding_typeenumRequiredThefunding_typeto get the instructions for.Possible enum valuesbank_transferUse a bank_transfer hash to define the bank transfer type

#### bank_transferobjectRequired

#### currencyenumRequired

#### funding_typeenumRequired

[TABLE]
bank_transferUse a bank_transfer hash to define the bank transfer type
[/TABLE]

```
bank_transfer
```

### Returns
Returns funding instructions for a customer_id cash balance

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/funding_instructions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d funding_type=bank_transfer \-d currency_code=eur \-d"bank_transfer[type]"=eu_bank_transfer \-d"bank_transfer[eu_bank_transfer][country]"=DE
```

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/funding_instructions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d funding_type=bank_transfer \-d currency_code=eur \-d"bank_transfer[type]"=eu_bank_transfer \-d"bank_transfer[eu_bank_transfer][country]"=DE
```

```
{"object":"funding_instructions","bank_transfer":{"country":"DE","financial_addresses":[{"iban":{"account_holder_address":{"city":"Dublin","country":"IE","line1":"Some address","line2":null,"postal_code":"D01H104","state":"Dublin 1"},"account_holder_name":"Merchant name","bank_address":{"city":"Dublin","country":"IE","line1":"1 North Wall Quay","line2":null,"postal_code":"D01 T8Y1","state":"Dublin"},"bic":"SOGEDEFFXXX","country":"DE","iban":"DE006847740991234567890"},"supported_networks":["sepa","swift"],"type":"iban"}],"type":"eu_bank_transfer"},"currency_code":"eur","funding_type":"bank_transfer","livemode":false}
```

```
{"object":"funding_instructions","bank_transfer":{"country":"DE","financial_addresses":[{"iban":{"account_holder_address":{"city":"Dublin","country":"IE","line1":"Some address","line2":null,"postal_code":"D01H104","state":"Dublin 1"},"account_holder_name":"Merchant name","bank_address":{"city":"Dublin","country":"IE","line1":"1 North Wall Quay","line2":null,"postal_code":"D01 T8Y1","state":"Dublin"},"bic":"SOGEDEFFXXX","country":"DE","iban":"DE006847740991234567890"},"supported_networks":["sepa","swift"],"type":"iban"}],"type":"eu_bank_transfer"},"currency_code":"eur","funding_type":"bank_transfer","livemode":false}
```

# Retrieve a cash balance transaction
Retrieves a specific cash balance transaction, which updated the customer_id’scash balance.

### Parameters
Noparameters.

### Returns
Returns a cash balance transaction object if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions/ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions/ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF","object":"customer_cash_balance_transaction","created":1690829143,"currency_code":"eur","customer_id":"cus_9s6XKzkNRiz8i3","ending_balance":10000,"funded":{"bank_transfer":{"eu_bank_transfer":{"bic":"BANKDEAAXXX","iban_last4":"7089","sender_name":"Sample Business GmbH"},"reference":"Payment for Invoice 28278FC-155","type":"eu_bank_transfer"}},"livemode":false,"net_amount":5000,"type":"funded"}
```

```
{"id":"ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF","object":"customer_cash_balance_transaction","created":1690829143,"currency_code":"eur","customer_id":"cus_9s6XKzkNRiz8i3","ending_balance":10000,"funded":{"bank_transfer":{"eu_bank_transfer":{"bic":"BANKDEAAXXX","iban_last4":"7089","sender_name":"Sample Business GmbH"},"reference":"Payment for Invoice 28278FC-155","type":"eu_bank_transfer"}},"livemode":false,"net_amount":5000,"type":"funded"}
```

# List cash balance transactions
Returns a list of transactions that modified the customer_id’scash balance.

### Parameters
Noparameters.

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitcash balance transactions, starting after itemstarting_after. Each entry in the array is a separate cash balance transaction object. If no more items are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions","has_more":false,"data":[{"id":"ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF","object":"customer_cash_balance_transaction","created":1690829143,"currency_code":"eur","customer_id":"cus_9s6XKzkNRiz8i3","ending_balance":10000,"funded":{"bank_transfer":{"eu_bank_transfer":{"bic":"BANKDEAAXXX","iban_last4":"7089","sender_name":"Sample Business GmbH"},"reference":"Payment for Invoice 28278FC-155","type":"eu_bank_transfer"}},"livemode":false,"net_amount":5000,"type":"funded"}]}
```

```
{"object":"list","url":"/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions","has_more":false,"data":[{"id":"ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF","object":"customer_cash_balance_transaction","created":1690829143,"currency_code":"eur","customer_id":"cus_9s6XKzkNRiz8i3","ending_balance":10000,"funded":{"bank_transfer":{"eu_bank_transfer":{"bic":"BANKDEAAXXX","iban_last4":"7089","sender_name":"Sample Business GmbH"},"reference":"Payment for Invoice 28278FC-155","type":"eu_bank_transfer"}},"livemode":false,"net_amount":5000,"type":"funded"}]}
```