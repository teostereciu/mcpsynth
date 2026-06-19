# capital/financing_offers

*Source: https://docs.stripe.com/api/capital/financing_offers*

---

# Financing OfferPreview
This is an object representing an offer of financing fromStripe Capital to a Connect subaccount.

# The Financing offer objectPreview

### Attributes
- idstringA unique identifier for the financing object.
- objectstringThe object type: financing_offer.
- accepted_termsnullableobjectInformation about the current financing object. Describes currency_code, advance amount,fee amount, withhold rate, and fee discount of previous financing.Show child attributes
- accountstringThe ID of the merchant associated with this financing object.
- charged_off_atnullabletimestampThe time at which this financing offer was charged off, if applicable. Given in seconds since unix epoch.
- createdintegerTime at which the offer was created. Given in seconds since unix epoch.
- expires_afterfloatTime at which the offer expires. Given in seconds since unix epoch.
- financing_typenullableenumThe type of financing being offered.Possible enum valuescash_advanceCapital’s Merchant Cash Advance program.fixed_term_loanCapital’s fixed-term loan offering. See theintegration guidefor more information.flex_loanCapital’s flex loan offering. See theintegration guidefor more information.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- offered_termsnullableobjectInformation about the financing offer. Describes currency_code, offered advance amount,offered fee amount, campaign type, withhold rate, and fee discount rate of previousfinancing.Show child attributes
- product_typenullableenumFinancing product identifier.Possible enum valuesrefillA “refill” financing offer extended through Stripe Capital. Refills are a form of discounted refinancing. Seetheintegration guidefor more information.standardA standard financing offer extended through Stripe Capital.
- replacementnullablestringThe ID of the financing offer that replaced this offer.
- replacement_fornullablestringThe ID of the financing offer that this offer is a replacement for.
- statusenumThe current status of the offer.Possible enum valuesacceptedSet once an offer has been accepted by the Connected account.canceledSet when the Connected account has reached out to Capital’s servicing team within 48 hours of acceptance and requested cancellation of their offer.completedSet when the financing offer has fully repaid. This status is no longer in use. Seefully_repaidinstead.deliveredOnce an offer has been delivered, mark it so using themark_deliveredendpoint.expiredSet when the financing offer has expired, usually 30 days after creation.fully_repaidSet when the financing offer has been fully repaid.paid_outSet once an offer has been paid out to the Connected account.rejectedSet when Capital’s servicing team has rejected the application for financing. The Connected account receives anemail with the reason for rejection.replacedSet when the financing offer has been replaced.undeliveredAll offers begin in this state. A financing offer must be delivered to its Connected account using approvedmarketing materials.
- status_transitionsobjectPreview featureHash containing timestamps of when the offer transitioned to a particular status.Show child attributes
- typenullableenumDeprecatedSeefinancing_type.Possible enum valuescash_advancefixed_term_loanflex_loan

#### idstring

#### objectstring

#### accepted_termsnullableobject

#### accountstring

#### charged_off_atnullabletimestamp

#### createdinteger

#### expires_afterfloat

#### financing_typenullableenum

[TABLE]
cash_advanceCapital’s Merchant Cash Advance program.
fixed_term_loanCapital’s fixed-term loan offering. See theintegration guidefor more information.
flex_loanCapital’s flex loan offering. See theintegration guidefor more information.
[/TABLE]

```
cash_advance
```

```
fixed_term_loan
```

#### livemodeboolean

#### metadatanullableobject

#### offered_termsnullableobject

#### product_typenullableenum

[TABLE]
refillA “refill” financing offer extended through Stripe Capital. Refills are a form of discounted refinancing. Seetheintegration guidefor more information.
standardA standard financing offer extended through Stripe Capital.
[/TABLE]

#### replacementnullablestring

#### replacement_fornullablestring

#### statusenum

[TABLE]
acceptedSet once an offer has been accepted by the Connected account.
canceledSet when the Connected account has reached out to Capital’s servicing team within 48 hours of acceptance and requested cancellation of their offer.
completedSet when the financing offer has fully repaid. This status is no longer in use. Seefully_repaidinstead.
deliveredOnce an offer has been delivered, mark it so using themark_deliveredendpoint.
expiredSet when the financing offer has expired, usually 30 days after creation.
fully_repaidSet when the financing offer has been fully repaid.
paid_outSet once an offer has been paid out to the Connected account.
rejectedSet when Capital’s servicing team has rejected the application for financing. The Connected account receives anemail with the reason for rejection.
replacedSet when the financing offer has been replaced.
undeliveredAll offers begin in this state. A financing offer must be delivered to its Connected account using approvedmarketing materials.
[/TABLE]

```
fully_repaid
```

```
undelivered
```

#### status_transitionsobjectPreview feature

#### typenullableenumDeprecated

[TABLE]
cash_advance
fixed_term_loan
flex_loan
[/TABLE]

```
cash_advance
```

```
fixed_term_loan
```

```
{"id":"financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh","object":"capital.financing_offer","account":"acct_1NPvKgBY65lDjjDk","created":1688423699,"expires_after":1690934400,"financing_type":"flex_loan","livemode":true,"offered_terms":{"advance_amount":10000,"campaign_type":"newly_eligible_user","currency_code":"usd","fee_amount":1000,"previous_financing_fee_discount_rate":null,"withhold_rate":0.05},"product_type":"standard","status":"undelivered"}
```

```
{"id":"financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh","object":"capital.financing_offer","account":"acct_1NPvKgBY65lDjjDk","created":1688423699,"expires_after":1690934400,"financing_type":"flex_loan","livemode":true,"offered_terms":{"advance_amount":10000,"campaign_type":"newly_eligible_user","currency_code":"usd","fee_amount":1000,"previous_financing_fee_discount_rate":null,"withhold_rate":0.05},"product_type":"standard","status":"undelivered"}
```

# Retrieve a given financing offer
Get the details of the financing offer

### Parameters
Noparameters.

### Returns
Returns the financing offer object

```
curlhttps://api.stripe.com/v1/capital/financing_offers/financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/capital/financing_offers/financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh","object":"capital.financing_offer","account":"acct_1NPvKgBY65lDjjDk","created":1688423699,"expires_after":1690934400,"financing_type":"flex_loan","livemode":true,"offered_terms":{"advance_amount":10000,"campaign_type":"newly_eligible_user","currency_code":"usd","fee_amount":1000,"previous_financing_fee_discount_rate":null,"withhold_rate":0.05},"product_type":"standard","status":"undelivered"}
```

```
{"id":"financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh","object":"capital.financing_offer","account":"acct_1NPvKgBY65lDjjDk","created":1688423699,"expires_after":1690934400,"financing_type":"flex_loan","livemode":true,"offered_terms":{"advance_amount":10000,"campaign_type":"newly_eligible_user","currency_code":"usd","fee_amount":1000,"previous_financing_fee_discount_rate":null,"withhold_rate":0.05},"product_type":"standard","status":"undelivered"}
```

# List financing offers
Retrieves the financing offers available for Connected accounts that belong to your platform.

### Parameters
- connected_accountstringlimit list to offers belonging to given connected account
- createdobjectOnly return offers that were created during the given date interval.Show child parameters
- statusstringlimit list to offers with given status

#### connected_accountstring

#### createdobject

#### statusstring

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Returns a list of financing offers for Connected accounts on your platform.

```
curl-G https://api.stripe.com/v1/capital/financing_offers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/capital/financing_offers \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/capital/financing_offers","has_more":false,"data":[{"id":"financingoffer_1Nn7FV2eZvKYlo2CcGGcdZ6L","object":"capital.financing_offer","account":"acct_1Nn7FVGy17qyuPVN","created":1693951049,"expires_after":1696464000,"financing_type":"flex_loan","livemode":true,"offered_terms":{"advance_amount":10000,"campaign_type":"newly_eligible_user","currency_code":"usd","fee_amount":1000,"previous_financing_fee_discount_rate":null,"withhold_rate":0.05},"product_type":"standard","status":"undelivered"}]}
```

```
{"object":"list","url":"/v1/capital/financing_offers","has_more":false,"data":[{"id":"financingoffer_1Nn7FV2eZvKYlo2CcGGcdZ6L","object":"capital.financing_offer","account":"acct_1Nn7FVGy17qyuPVN","created":1693951049,"expires_after":1696464000,"financing_type":"flex_loan","livemode":true,"offered_terms":{"advance_amount":10000,"campaign_type":"newly_eligible_user","currency_code":"usd","fee_amount":1000,"previous_financing_fee_discount_rate":null,"withhold_rate":0.05},"product_type":"standard","status":"undelivered"}]}
```

# Mark that a financing offer has been delivered
Acknowledges that platform has received and delivered the financing_offer tothe intended merchant recipient.

### Parameters
Noparameters.

### Returns
Returns the financing offer object

```
curl-X POST https://api.stripe.com/v1/capital/financing_offers/financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh/mark_delivered \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curl-X POST https://api.stripe.com/v1/capital/financing_offers/financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh/mark_delivered \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh","object":"capital.financing_offer","account":"acct_1NPvKgBY65lDjjDk","created":1688423699,"expires_after":1690934400,"financing_type":"flex_loan","livemode":true,"offered_terms":{"advance_amount":10000,"campaign_type":"newly_eligible_user","currency_code":"usd","fee_amount":1000,"previous_financing_fee_discount_rate":null,"withhold_rate":0.05},"product_type":"standard","status":"delivered"}
```

```
{"id":"financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh","object":"capital.financing_offer","account":"acct_1NPvKgBY65lDjjDk","created":1688423699,"expires_after":1690934400,"financing_type":"flex_loan","livemode":true,"offered_terms":{"advance_amount":10000,"campaign_type":"newly_eligible_user","currency_code":"usd","fee_amount":1000,"previous_financing_fee_discount_rate":null,"withhold_rate":0.05},"product_type":"standard","status":"delivered"}
```