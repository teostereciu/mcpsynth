# invoice-payment

*Source: https://docs.stripe.com/api/invoice-payment*

---

# Invoice Payment
Invoice Payments represent payments made against invoices. Invoice Payments canbe accessed in two ways:
- By expanding thepaymentsfield on theInvoiceresource.
- By using the Invoice Payment retrieve and list endpoints.
Invoice Payments include the mapping between payment objects, such as Payment Intent, and Invoices.This resource and its endpoints allows you to easily track if a payment is associated with a specific invoice andmonitor the allocation details of the payments.

# The Invoice Payment object

### Attributes
- idstringUnique identifier for the object.
- amount_paidnullableintegerAmount that was actually paid for this invoice, incents. This field is null until the payment ispaid. This amount can be less than theamount_requestedif the PaymentIntent’samount_receivedis not sufficient to pay all of the invoices that it is attached to.
- amount_requestedintegerAmount intended to be paid toward this invoice, incents
- invoicestringExpandableThe invoice that was paid.
- is_defaultbooleanStripe automatically creates a default InvoicePayment when the invoice is finalized, and keeps it synchronized with the invoice’samount_remaining. The PaymentIntent associated with the default payment can’t be edited or canceled directly.
- paymentobjectThe details on the payment.Show child attributes
- statusstringThe status of the payment, one ofopen,paid, orcanceled.

#### idstring

#### amount_paidnullableinteger

#### amount_requestedinteger

#### invoicestringExpandable

#### is_defaultboolean

#### paymentobject

#### statusstring

### More attributesExpand all
- objectstring
- createdtimestamp
- currencystring
- livemodeboolean
- status_transitionsobject

#### objectstring

#### createdtimestamp

#### currencystring

#### livemodeboolean

#### status_transitionsobject

```
{"id":"inpay_1M3USa2eZvKYlo2CBjuwbq0N","object":"invoice_payment","amount_paid":2000,"amount_requested":2000,"created":1391288554,"currency_code":"usd","invoice":"in_103Q0w2eZvKYlo2C5PYwf6Wf","is_default":true,"livemode":false,"payment":{"type":"payment_intent","payment_intent":"pi_103Q0w2eZvKYlo2C364X582Z"},"status":"paid","status_transitions":{"canceled_at":null,"paid_at":1391288554}}
```

```
{"id":"inpay_1M3USa2eZvKYlo2CBjuwbq0N","object":"invoice_payment","amount_paid":2000,"amount_requested":2000,"created":1391288554,"currency_code":"usd","invoice":"in_103Q0w2eZvKYlo2C5PYwf6Wf","is_default":true,"livemode":false,"payment":{"type":"payment_intent","payment_intent":"pi_103Q0w2eZvKYlo2C364X582Z"},"status":"paid","status_transitions":{"canceled_at":null,"paid_at":1391288554}}
```

# Retrieve an InvoicePayment
Retrieves the invoice payment with the given ID.

### Parameters
Noparameters.

### Returns
Returns aninvoice_paymentobject if a valid invoice payment ID was provided. Otherwise, this callraisesan error.

```
curlhttps://api.stripe.com/v1/invoice_payments/inpay_1M3USa2eZvKYlo2CBjuwbq0N \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/invoice_payments/inpay_1M3USa2eZvKYlo2CBjuwbq0N \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"inpay_1M3USa2eZvKYlo2CBjuwbq0N","object":"invoice_payment","amount_paid":2000,"amount_requested":2000,"created":1391288554,"currency_code":"usd","invoice":"in_103Q0w2eZvKYlo2C5PYwf6Wf","is_default":true,"livemode":false,"payment":{"type":"payment_intent","payment_intent":"pi_103Q0w2eZvKYlo2C364X582Z"},"status":"paid","status_transitions":{"canceled_at":null,"paid_at":1391288554}}
```

```
{"id":"inpay_1M3USa2eZvKYlo2CBjuwbq0N","object":"invoice_payment","amount_paid":2000,"amount_requested":2000,"created":1391288554,"currency_code":"usd","invoice":"in_103Q0w2eZvKYlo2C5PYwf6Wf","is_default":true,"livemode":false,"payment":{"type":"payment_intent","payment_intent":"pi_103Q0w2eZvKYlo2C364X582Z"},"status":"paid","status_transitions":{"canceled_at":null,"paid_at":1391288554}}
```

# List all payments for an invoice
When retrieving an invoice, there is an includable payments property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of payments.

### Parameters
- invoicestringThe identifier of the invoice whose payments to return.
- paymentobjectThe payment details of the invoice payments to return.Show child parameters
- statusenumThe status of the invoice payments to return.Possible enum valuescanceledThe payment has been canceled; it will not be credited to the invoice.openThe payment is incomplete and isn’t credited to the invoice. More fine-grained information available on the payment intentpaidThe payment is complete and has been credited to the invoice.

#### invoicestring

#### paymentobject

#### statusenum

[TABLE]
canceledThe payment has been canceled; it will not be credited to the invoice.
openThe payment is incomplete and isn’t credited to the invoice. More fine-grained information available on the payment intent
paidThe payment is complete and has been credited to the invoice.
[/TABLE]

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
Adictionarywith adataproperty that contains an array of up tolimitinvoice payments, starting after invoice paymentstarting_after. Each entry in the array is a separateinvoice_payment object. If no more invoice payments are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/invoice_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d invoice=in_103Q0w2eZvKYlo2C5PYwf6Wf
```

```
curl-G https://api.stripe.com/v1/invoice_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d invoice=in_103Q0w2eZvKYlo2C5PYwf6Wf
```

```
{"object":"list","url":"/v1/invoice_payments","has_more":false,"data":[{"id":"inpay_1M3USa2eZvKYlo2CBjuwbq0N","object":"invoice_payment","amount_paid":2000,"amount_requested":2000,"created":1391288554,"currency_code":"usd","invoice":"in_103Q0w2eZvKYlo2C5PYwf6Wf","is_default":true,"livemode":false,"payment":{"type":"payment_intent","payment_intent":"pi_103Q0w2eZvKYlo2C364X582Z"},"status":"paid","status_transitions":{"canceled_at":null,"paid_at":1391288554}}]}
```

```
{"object":"list","url":"/v1/invoice_payments","has_more":false,"data":[{"id":"inpay_1M3USa2eZvKYlo2CBjuwbq0N","object":"invoice_payment","amount_paid":2000,"amount_requested":2000,"created":1391288554,"currency_code":"usd","invoice":"in_103Q0w2eZvKYlo2C5PYwf6Wf","is_default":true,"livemode":false,"payment":{"type":"payment_intent","payment_intent":"pi_103Q0w2eZvKYlo2C364X582Z"},"status":"paid","status_transitions":{"canceled_at":null,"paid_at":1391288554}}]}
```