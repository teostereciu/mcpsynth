# payment_method_configurations

*Source: https://docs.stripe.com/api/payment_method_configurations*

---

# Payment Method Configurations
PaymentMethodConfigurations control which payment methods are displayed to your customers when you don’t explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.
There are two types of PaymentMethodConfigurations. Which is used depends on thecharge type:
Directconfigurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.
Childconfigurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.
Child configurations have aparentthat sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account’s associated child configuration. Parent configurations aremanaged in the dashboardand are not available in this API.
Related guides:
- Payment Method Configurations API
- Multiple configurations on dynamic payment methods
- Multiple configurations for your Connect accounts

# The Payment Method Configuration object

### Attributes
- idstringretrievable with publishable keyUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- activebooleanWhether the configuration can be used for new payments.
- applicationnullablestringFor child configs, the Connect application associated with the configuration.
- is_defaultbooleanThe default configuration is used whenever a payment method configuration is not specified.
- namestringThe configuration’s name.
- parentnullablestringFor child configs, the configuration’s parent configuration.

#### idstringretrievable with publishable key

#### objectstring

#### activeboolean

#### applicationnullablestring

#### is_defaultboolean

#### namestring

#### parentnullablestring

### More attributesExpand all
- acss_debitnullableobject
- affirmnullableobject
- afterpay_clearpaynullableobject
- alipaynullableobject
- almanullableobject
- amazon_paynullableobject
- apple_paynullableobject
- au_becs_debitnullableobject
- bacs_debitnullableobject
- bancontactnullableobject
- billienullableobject
- bliknullableobject
- boletonullableobject
- cardnullableobject
- cartes_bancairesnullableobject
- cashappnullableobject
- cryptonullableobject
- customer_balancenullableobject
- epsnullableobject
- fpxnullableobject
- giropaynullableobject
- google_paynullableobject
- grabpaynullableobject
- idealnullableobject
- jcbnullableobject
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

#### acss_debitnullableobject

#### affirmnullableobject

#### afterpay_clearpaynullableobject

#### alipaynullableobject

#### almanullableobject

#### amazon_paynullableobject

#### apple_paynullableobject

#### au_becs_debitnullableobject

#### bacs_debitnullableobject

#### bancontactnullableobject

#### billienullableobject

#### bliknullableobject

#### boletonullableobject

#### cardnullableobject

#### cartes_bancairesnullableobject

#### cashappnullableobject

#### cryptonullableobject

#### customer_balancenullableobject

#### epsnullableobject

#### fpxnullableobject

#### giropaynullableobject

#### google_paynullableobject

#### grabpaynullableobject

#### idealnullableobject

#### jcbnullableobject

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
{"id":"pmc_abcdef","object":"payment_method_configuration","acss_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"active":true,"affirm":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"afterpay_clearpay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"alipay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"apple_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"bancontact":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"card":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"cartes_bancaires":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"eps":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"giropay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"google_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"ideal":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"is_default":true,"klarna":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"link":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"livemode":false,"name":"Default","p24":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sepa_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sofort":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"us_bank_account":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"wechat_pay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}}}
```

```
{"id":"pmc_abcdef","object":"payment_method_configuration","acss_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"active":true,"affirm":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"afterpay_clearpay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"alipay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"apple_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"bancontact":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"card":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"cartes_bancaires":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"eps":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"giropay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"google_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"ideal":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"is_default":true,"klarna":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"link":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"livemode":false,"name":"Default","p24":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sepa_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sofort":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"us_bank_account":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"wechat_pay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}}}
```

# Create a payment method configuration
Creates a payment method configuration

### Parameters
- namestringRequired unless parent is providedConfiguration name.The maximum length is 100 characters.
- parentstringRequired unless name is providedConfiguration’s parent configuration. Specify to create a child configuration.The maximum length is 100 characters.

#### namestringRequired unless parent is provided

#### parentstringRequired unless name is provided

### More parametersExpand all
- acss_debitobject
- affirmobject
- afterpay_clearpayobject
- alipayobject
- almaobject
- amazon_payobject
- apple_payobject
- apple_pay_laterobject
- au_becs_debitobject
- bacs_debitobject
- bancontactobject
- billieobject
- blikobject
- boletoobject
- cardobject
- cartes_bancairesobject
- cashappobject
- cryptoobject
- customer_balanceobject
- epsobject
- fpxobject
- fr_meal_voucher_conecsobject
- giropayobject
- google_payobject
- grabpayobject
- idealobject
- jcbobject
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

#### almaobject

#### amazon_payobject

#### apple_payobject

#### apple_pay_laterobject

#### au_becs_debitobject

#### bacs_debitobject

#### bancontactobject

#### billieobject

#### blikobject

#### boletoobject

#### cardobject

#### cartes_bancairesobject

#### cashappobject

#### cryptoobject

#### customer_balanceobject

#### epsobject

#### fpxobject

#### fr_meal_voucher_conecsobject

#### giropayobject

#### google_payobject

#### grabpayobject

#### idealobject

#### jcbobject

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
Returns the payment method configuration object

```
curlhttps://api.stripe.com/v1/payment_method_configurations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Buy Now Pay Laters"
```

```
curlhttps://api.stripe.com/v1/payment_method_configurations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name="Buy Now Pay Laters"
```

```
{"id":"pmc_abcdef","object":"payment_method_configuration","acss_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"active":true,"affirm":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"afterpay_clearpay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"alipay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"apple_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"bancontact":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"card":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"cartes_bancaires":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"eps":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"giropay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"google_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"ideal":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"is_default":true,"klarna":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"link":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"livemode":false,"name":"Default","p24":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sepa_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sofort":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"us_bank_account":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"wechat_pay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}}}
```

```
{"id":"pmc_abcdef","object":"payment_method_configuration","acss_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"active":true,"affirm":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"afterpay_clearpay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"alipay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"apple_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"bancontact":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"card":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"cartes_bancaires":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"eps":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"giropay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"google_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"ideal":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"is_default":true,"klarna":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"link":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"livemode":false,"name":"Default","p24":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sepa_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sofort":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"us_bank_account":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"wechat_pay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}}}
```

# Update payment method configuration
Update payment method configuration

### Parameters
- activebooleanWhether the configuration can be used for new payments.
- namestringConfiguration name.The maximum length is 100 characters.

#### activeboolean

#### namestring

### More parametersExpand all
- acss_debitobject
- affirmobject
- afterpay_clearpayobject
- alipayobject
- almaobject
- amazon_payobject
- apple_payobject
- apple_pay_laterobject
- au_becs_debitobject
- bacs_debitobject
- bancontactobject
- billieobject
- blikobject
- boletoobject
- cardobject
- cartes_bancairesobject
- cashappobject
- cryptoobject
- customer_balanceobject
- epsobject
- fpxobject
- fr_meal_voucher_conecsobject
- giropayobject
- google_payobject
- grabpayobject
- idealobject
- jcbobject
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

#### almaobject

#### amazon_payobject

#### apple_payobject

#### apple_pay_laterobject

#### au_becs_debitobject

#### bacs_debitobject

#### bancontactobject

#### billieobject

#### blikobject

#### boletoobject

#### cardobject

#### cartes_bancairesobject

#### cashappobject

#### cryptoobject

#### customer_balanceobject

#### epsobject

#### fpxobject

#### fr_meal_voucher_conecsobject

#### giropayobject

#### google_payobject

#### grabpayobject

#### idealobject

#### jcbobject

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
An object with the updated account payment method configuration

```
curlhttps://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"acss_debit[display_preference][preference]"=on
```

```
curlhttps://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"acss_debit[display_preference][preference]"=on
```

```
{"id":"pmc_abcdef","object":"payment_method_configuration","acss_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"active":true,"affirm":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"afterpay_clearpay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"alipay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"apple_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"bancontact":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"card":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"cartes_bancaires":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"eps":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"giropay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"google_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"ideal":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"is_default":true,"klarna":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"link":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"livemode":false,"name":"Default","p24":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sepa_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sofort":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"us_bank_account":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"wechat_pay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}}}
```

```
{"id":"pmc_abcdef","object":"payment_method_configuration","acss_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"active":true,"affirm":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"afterpay_clearpay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"alipay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"apple_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"bancontact":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"card":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"cartes_bancaires":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"eps":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"giropay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"google_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"ideal":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"is_default":true,"klarna":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"link":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"livemode":false,"name":"Default","p24":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sepa_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sofort":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"us_bank_account":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"wechat_pay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}}}
```

# Retrieve payment method configuration
Retrieve payment method configuration

### Parameters
Noparameters.

### Returns
A payment method configuration object.

```
curlhttps://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"pmc_abcdef","object":"payment_method_configuration","acss_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"active":true,"affirm":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"afterpay_clearpay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"alipay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"apple_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"bancontact":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"card":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"cartes_bancaires":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"eps":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"giropay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"google_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"ideal":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"is_default":true,"klarna":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"link":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"livemode":false,"name":"Default","p24":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sepa_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sofort":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"us_bank_account":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"wechat_pay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}}}
```

```
{"id":"pmc_abcdef","object":"payment_method_configuration","acss_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"active":true,"affirm":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"afterpay_clearpay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"alipay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"apple_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"bancontact":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"card":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"cartes_bancaires":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"eps":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"giropay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"google_pay":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"ideal":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"is_default":true,"klarna":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"link":{"available":true,"display_preference":{"overridable":null,"preference":"on","value":"on"}},"livemode":false,"name":"Default","p24":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sepa_debit":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"sofort":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"us_bank_account":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}},"wechat_pay":{"available":false,"display_preference":{"overridable":null,"preference":"off","value":"off"}}}
```