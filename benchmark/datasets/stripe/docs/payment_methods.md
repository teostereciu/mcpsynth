# payment_methods

*Source: https://docs.stripe.com/api/payment_methods*

---

# Payment Methods
PaymentMethod objects represent your customer’s payment instruments.You can use them withPaymentIntentsto collect payments or save them toCustomer objects to store instrument details for future payments.
Related guides:Payment MethodsandMore Payment Scenarios.

# The PaymentMethod object

### Attributes
- idstringUnique identifier for the object.
- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.Show child attributes
- customernullablestringExpandableThe ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- typeenumThe type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.Possible enum valuesacss_debitPre-authorized debit paymentsare used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).affirmAffirmis a buy now, pay later payment method in the US.afterpay_clearpayAfterpay / Clearpayis a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.alipayAlipayis a digital wallet payment method used in China.almaAlmais a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.amazon_payAmazon Payis a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.au_becs_debitBECS Direct Debitis used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).bacs_debitBacs Direct Debitis used to debit UK bank accounts.bancontactBancontactis a bank redirect payment method used in Belgium.billieBillieis a payment method.Show 44 more

#### idstring

#### billing_detailsobject

#### customernullablestringExpandable

#### metadatanullableobject

#### typeenum

[TABLE]
acss_debitPre-authorized debit paymentsare used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).
affirmAffirmis a buy now, pay later payment method in the US.
afterpay_clearpayAfterpay / Clearpayis a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.
alipayAlipayis a digital wallet payment method used in China.
almaAlmais a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.
amazon_payAmazon Payis a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.
au_becs_debitBECS Direct Debitis used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).
bacs_debitBacs Direct Debitis used to debit UK bank accounts.
bancontactBancontactis a bank redirect payment method used in Belgium.
billieBillieis a payment method.
Show 44 more
[/TABLE]

```
afterpay_clearpay
```

```
au_becs_debit
```

### More attributesExpand all
- objectstring
- acss_debitnullableobject
- affirmnullableobject
- afterpay_clearpaynullableobject
- alipaynullableobject
- allow_redisplaynullableenum
- almanullableobject
- amazon_paynullableobject
- au_becs_debitnullableobject
- bacs_debitnullableobject
- bancontactnullableobject
- billienullableobject
- bliknullableobject
- boletonullableobject
- cardnullableobject
- card_presentnullableobject
- cashappnullableobject
- createdtimestamp
- cryptonullableobject
- customnullableobject
- customer_balancenullableobject
- epsnullableobject
- fpxnullableobject
- giropaynullableobject
- grabpaynullableobject
- idealnullableobject
- interac_presentnullableobjectPreview feature
- kakao_paynullableobject
- klarnanullableobject
- konbininullableobject
- kr_cardnullableobject
- linknullableobject
- livemodeboolean
- mb_waynullableobject
- mobilepaynullableobject
- multibanconullableobject
- naver_paynullableobject
- nz_bank_accountnullableobject
- oxxonullableobject
- p24nullableobject
- pay_by_banknullableobject
- payconullableobject
- paynownullableobject
- paypalnullableobject
- paypaynullableobjectPreview feature
- paytonullableobject
- pixnullableobject
- promptpaynullableobject
- radar_optionsnullableobject
- revolut_paynullableobject
- samsung_paynullableobject
- satispaynullableobject
- sepa_debitnullableobject
- sofortnullableobject
- swishnullableobject
- twintnullableobject
- us_bank_accountnullableobject
- wechat_paynullableobject
- zipnullableobject

#### objectstring

#### acss_debitnullableobject

#### affirmnullableobject

#### afterpay_clearpaynullableobject

#### alipaynullableobject

#### allow_redisplaynullableenum

#### almanullableobject

#### amazon_paynullableobject

#### au_becs_debitnullableobject

#### bacs_debitnullableobject

#### bancontactnullableobject

#### billienullableobject

#### bliknullableobject

#### boletonullableobject

#### cardnullableobject

#### card_presentnullableobject

#### cashappnullableobject

#### createdtimestamp

#### cryptonullableobject

#### customnullableobject

#### customer_balancenullableobject

#### epsnullableobject

#### fpxnullableobject

#### giropaynullableobject

#### grabpaynullableobject

#### idealnullableobject

#### interac_presentnullableobjectPreview feature

#### kakao_paynullableobject

#### klarnanullableobject

#### konbininullableobject

#### kr_cardnullableobject

#### linknullableobject

#### livemodeboolean

#### mb_waynullableobject

#### mobilepaynullableobject

#### multibanconullableobject

#### naver_paynullableobject

#### nz_bank_accountnullableobject

#### oxxonullableobject

#### p24nullableobject

#### pay_by_banknullableobject

#### payconullableobject

#### paynownullableobject

#### paypalnullableobject

#### paypaynullableobjectPreview feature

#### paytonullableobject

#### pixnullableobject

#### promptpaynullableobject

#### radar_optionsnullableobject

#### revolut_paynullableobject

#### samsung_paynullableobject

#### satispaynullableobject

#### sepa_debitnullableobject

#### sofortnullableobject

#### swishnullableobject

#### twintnullableobject

#### us_bank_accountnullableobject

#### wechat_paynullableobject

#### zipnullableobject

```
{"id":"pm_1Q0PsIJvEtkwdCNYMSaVuRz6","object":"payment_method","allow_redisplay":"unspecified","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"John Doe","phone":null},"created":1726673582,"customer":null,"livemode":false,"metadata":{},"type":"us_bank_account","us_bank_account":{"account_holder_type":"individual","account_type":"checking","bank_name":"STRIPE TEST BANK","financial_connections_account":null,"fingerprint":"LstWJFsCK7P349Bg","last4":"6789","networks":{"preferred":"ach","supported":["ach"]},"routing_number":"110000000","status_details":{}}}
```

```
{"id":"pm_1Q0PsIJvEtkwdCNYMSaVuRz6","object":"payment_method","allow_redisplay":"unspecified","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"John Doe","phone":null},"created":1726673582,"customer":null,"livemode":false,"metadata":{},"type":"us_bank_account","us_bank_account":{"account_holder_type":"individual","account_type":"checking","bank_name":"STRIPE TEST BANK","financial_connections_account":null,"fingerprint":"LstWJFsCK7P349Bg","last4":"6789","networks":{"preferred":"ach","supported":["ach"]},"routing_number":"110000000","status_details":{}}}
```

# Create a PaymentMethod
Creates a PaymentMethod object. Read theStripe.js referenceto learn how to create PaymentMethods via Stripe.js.
Instead of creating a PaymentMethod directly, we recommend using thePaymentIntentsAPI to accept a payment immediately or theSetupIntentAPI to collect payment method details ahead of a future payment.

### Parameters
- typeenumRequiredThe type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.Possible enum valuesacss_debitPre-authorized debit paymentsare used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).affirmAffirmis a buy now, pay later payment method in the US.afterpay_clearpayAfterpay / Clearpayis a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.alipayAlipayis a digital wallet payment method used in China.almaAlmais a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.amazon_payAmazon Payis a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.au_becs_debitBECS Direct Debitis used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).bacs_debitBacs Direct Debitis used to debit UK bank accounts.bancontactBancontactis a bank redirect payment method used in Belgium.billieBillieis a payment method.Show 44 more
- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### typeenumRequired

[TABLE]
acss_debitPre-authorized debit paymentsare used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).
affirmAffirmis a buy now, pay later payment method in the US.
afterpay_clearpayAfterpay / Clearpayis a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.
alipayAlipayis a digital wallet payment method used in China.
almaAlmais a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.
amazon_payAmazon Payis a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.
au_becs_debitBECS Direct Debitis used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).
bacs_debitBacs Direct Debitis used to debit UK bank accounts.
bancontactBancontactis a bank redirect payment method used in Belgium.
billieBillieis a payment method.
Show 44 more
[/TABLE]

```
afterpay_clearpay
```

```
au_becs_debit
```

#### billing_detailsobject

#### metadataobject

### More parametersExpand all
- acss_debitobject
- affirmobject
- afterpay_clearpayobject
- alipayobject
- allow_redisplayenum
- almaobject
- amazon_payobject
- au_becs_debitobject
- bacs_debitobject
- bancontactobject
- billieobject
- blikobject
- boletoobject
- cardobject
- cashappobject
- cryptoobject
- customobject
- customer_balanceobject
- epsobject
- fpxobject
- giropayobject
- grabpayobject
- idealobject
- interac_presentobjectPreview feature
- kakao_payobject
- klarnaobject
- konbiniobject
- kr_cardobject
- linkobject
- mb_wayobject
- mobilepayobject
- multibancoobject
- naver_payobject
- nz_bank_accountobject
- oxxoobject
- p24object
- pay_by_bankobject
- paycoobject
- paynowobject
- paypalobject
- paypayobjectPreview feature
- paytoobject
- pixobject
- promptpayobject
- radar_optionsobject
- revolut_payobject
- samsung_payobject
- satispayobject
- sepa_debitobject
- sofortobject
- swishobject
- twintobject
- us_bank_accountobject
- wechat_payobject
- zipobject

#### acss_debitobject

#### affirmobject

#### afterpay_clearpayobject

#### alipayobject

#### allow_redisplayenum

#### almaobject

#### amazon_payobject

#### au_becs_debitobject

#### bacs_debitobject

#### bancontactobject

#### billieobject

#### blikobject

#### boletoobject

#### cardobject

#### cashappobject

#### cryptoobject

#### customobject

#### customer_balanceobject

#### epsobject

#### fpxobject

#### giropayobject

#### grabpayobject

#### idealobject

#### interac_presentobjectPreview feature

#### kakao_payobject

#### klarnaobject

#### konbiniobject

#### kr_cardobject

#### linkobject

#### mb_wayobject

#### mobilepayobject

#### multibancoobject

#### naver_payobject

#### nz_bank_accountobject

#### oxxoobject

#### p24object

#### pay_by_bankobject

#### paycoobject

#### paynowobject

#### paypalobject

#### paypayobjectPreview feature

#### paytoobject

#### pixobject

#### promptpayobject

#### radar_optionsobject

#### revolut_payobject

#### samsung_payobject

#### satispayobject

#### sepa_debitobject

#### sofortobject

#### swishobject

#### twintobject

#### us_bank_accountobject

#### wechat_payobject

#### zipobject

### Returns
Returns a PaymentMethod object.

```
curlhttps://api.stripe.com/v1/payment_methods \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=us_bank_account \-d"us_bank_account[account_holder_type]"=individual \-d"us_bank_account[account_number]"=000123456789 \-d"us_bank_account[routing_number]"=110000000 \-d"billing_details[name]"="John Doe"
```

```
curlhttps://api.stripe.com/v1/payment_methods \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=us_bank_account \-d"us_bank_account[account_holder_type]"=individual \-d"us_bank_account[account_number]"=000123456789 \-d"us_bank_account[routing_number]"=110000000 \-d"billing_details[name]"="John Doe"
```

```
{"id":"pm_1Q0PsIJvEtkwdCNYMSaVuRz6","object":"payment_method","allow_redisplay":"unspecified","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"John Doe","phone":null},"created":1726673582,"customer":null,"livemode":false,"metadata":{},"type":"us_bank_account","us_bank_account":{"account_holder_type":"individual","account_type":"checking","bank_name":"STRIPE TEST BANK","financial_connections_account":null,"fingerprint":"LstWJFsCK7P349Bg","last4":"6789","networks":{"preferred":"ach","supported":["ach"]},"routing_number":"110000000","status_details":{}}}
```

```
{"id":"pm_1Q0PsIJvEtkwdCNYMSaVuRz6","object":"payment_method","allow_redisplay":"unspecified","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"John Doe","phone":null},"created":1726673582,"customer":null,"livemode":false,"metadata":{},"type":"us_bank_account","us_bank_account":{"account_holder_type":"individual","account_type":"checking","bank_name":"STRIPE TEST BANK","financial_connections_account":null,"fingerprint":"LstWJFsCK7P349Bg","last4":"6789","networks":{"preferred":"ach","supported":["ach"]},"routing_number":"110000000","status_details":{}}}
```

# Update a PaymentMethod
Updates a PaymentMethod object. A PaymentMethod must be attached to a customer to be updated.

### Parameters
- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### billing_detailsobject

#### metadataobject

### More parametersExpand all
- allow_redisplayenum
- cardobject
- paytoobject
- us_bank_accountobject

#### allow_redisplayenum

#### cardobject

#### paytoobject

#### us_bank_accountobject

### Returns
Returns a PaymentMethod object.

```
curlhttps://api.stripe.com/v1/payment_methods/pm_1Q0PsIJvEtkwdCNYMSaVuRz6 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/payment_methods/pm_1Q0PsIJvEtkwdCNYMSaVuRz6 \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"pm_1Q0PsIJvEtkwdCNYMSaVuRz6","object":"payment_method","allow_redisplay":"unspecified","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"John Doe","phone":null},"created":1726673582,"customer":null,"livemode":false,"metadata":{"order_id":"6735"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"individual","account_type":"checking","bank_name":"STRIPE TEST BANK","financial_connections_account":null,"fingerprint":"LstWJFsCK7P349Bg","last4":"6789","networks":{"preferred":"ach","supported":["ach"]},"routing_number":"110000000","status_details":{}}}
```

```
{"id":"pm_1Q0PsIJvEtkwdCNYMSaVuRz6","object":"payment_method","allow_redisplay":"unspecified","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":"John Doe","phone":null},"created":1726673582,"customer":null,"livemode":false,"metadata":{"order_id":"6735"},"type":"us_bank_account","us_bank_account":{"account_holder_type":"individual","account_type":"checking","bank_name":"STRIPE TEST BANK","financial_connections_account":null,"fingerprint":"LstWJFsCK7P349Bg","last4":"6789","networks":{"preferred":"ach","supported":["ach"]},"routing_number":"110000000","status_details":{}}}
```

# Retrieve a Customer's PaymentMethod
Retrieves a PaymentMethod object for a given Customer.

### Parameters
Noparameters.

### Returns
Returns a PaymentMethod object.

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods/pm_1NVChw2eZvKYlo2CHxiM5E2E \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods/pm_1NVChw2eZvKYlo2CHxiM5E2E \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"pm_1NVChw2eZvKYlo2CHxiM5E2E","object":"payment_method","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":"pass"},"country":"US","exp_month":12,"exp_year":2034,"fingerprint":"Xt5EWLLDS7FJjR1c","funding":"credit","generated_from":null,"last4":"4242","networks":{"available":["visa"],"preferred":null},"three_d_secure_usage":{"supported":true},"wallet":null},"created":1689682128,"customer":"cus_9s6XKzkNRiz8i3","livemode":false,"metadata":{},"redaction":null,"type":"card"}
```

```
{"id":"pm_1NVChw2eZvKYlo2CHxiM5E2E","object":"payment_method","billing_details":{"address":{"city":null,"country":null,"line1":null,"line2":null,"postal_code":null,"state":null},"email":null,"name":null,"phone":null},"card":{"brand":"visa","checks":{"address_line1_check":null,"address_postal_code_check":null,"cvc_check":"pass"},"country":"US","exp_month":12,"exp_year":2034,"fingerprint":"Xt5EWLLDS7FJjR1c","funding":"credit","generated_from":null,"last4":"4242","networks":{"available":["visa"],"preferred":null},"three_d_secure_usage":{"supported":true},"wallet":null},"created":1689682128,"customer":"cus_9s6XKzkNRiz8i3","livemode":false,"metadata":{},"redaction":null,"type":"card"}
```