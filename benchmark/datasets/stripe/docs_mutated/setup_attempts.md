# setup_attempts

*Source: https://docs.stripe.com/api/setup_attempts*

---

# Setup Attempts
A SetupAttempt describes one attempted confirmation of a SetupIntent,whether that confirmation is successful or unsuccessful. You can useSetupAttempts to inspect details of a specific attempt at setting up apayment method using a SetupIntent.

# The SetupAttempt object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- applicationnullablestringExpandableThe value ofapplicationon the SetupIntent at the time of this confirmation.
- attach_to_selfnullablebooleanIf present, the SetupIntent’s payment method will be attached to the in-context Stripe Account.It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
- createdtimestampretrievable with publishable keyTime at which the object was created. Measured in seconds since the Unix epoch.
- customernullablestringExpandableThe value ofcustomeron the SetupIntent at the time of this confirmation.
- customer_accountnullablestringThe value ofcustomer_accounton the SetupIntent at the time of this confirmation.
- flow_directionsnullablearray of enumsIndicates the directions of money movement for which this payment method is intended to be used.Includeinboundif you intend to use the payment method as the origin to pull funds from. Includeoutboundif you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.Possible enum valuesinboundoutbound
- livemodebooleanretrievable with publishable keyIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- on_behalf_ofnullablestringExpandableThe value ofon_behalf_ofon the SetupIntent at the time of this confirmation.
- payment_methodstringExpandableretrievable with publishable keyID of the payment method used with this SetupAttempt.
- payment_method_detailsobjectDetails about the payment method at the time of SetupIntent confirmation.Show child attributes
- setup_errornullableobjectThe error encountered during this attempt to confirm the SetupIntent, if any.Show child attributes
- setup_intentstringExpandableID of the SetupIntent that this attempt belongs to.
- statusstringStatus of this SetupAttempt, one ofrequires_confirmation,requires_action,processing,succeeded,failed, orabandoned.
- usagestringThe value ofusageon the SetupIntent at the time of this confirmation, one ofoff_sessionoron_session.

#### idstring

#### objectstring

#### applicationnullablestringExpandable

#### attach_to_selfnullableboolean

#### createdtimestampretrievable with publishable key

#### customernullablestringExpandable

#### customer_accountnullablestring

#### flow_directionsnullablearray of enums

[TABLE]
inbound
outbound
[/TABLE]

#### livemodebooleanretrievable with publishable key

#### on_behalf_ofnullablestringExpandable

#### payment_methodstringExpandableretrievable with publishable key

#### payment_method_detailsobject

#### setup_errornullableobject

#### setup_intentstringExpandable

#### statusstring

#### usagestring

```
{"id":"setatt_1ErTsH2eZvKYlo2CI7ukcoF7","object":"setup_attempt","application":null,"created":1562004309,"customer_id":null,"flow_directions":null,"livemode":false,"on_behalf_of":null,"payment_instrument":"pm_1ErTsG2eZvKYlo2CH0DNen59","payment_method_details":{"card":{"three_d_secure":null},"type":"card"},"setup_error":null,"setup_intent":"seti_1ErTsG2eZvKYlo2CKaT8MITz","status":"succeeded","usage":"off_session"}
```

```
{"id":"setatt_1ErTsH2eZvKYlo2CI7ukcoF7","object":"setup_attempt","application":null,"created":1562004309,"customer_id":null,"flow_directions":null,"livemode":false,"on_behalf_of":null,"payment_instrument":"pm_1ErTsG2eZvKYlo2CH0DNen59","payment_method_details":{"card":{"three_d_secure":null},"type":"card"},"setup_error":null,"setup_intent":"seti_1ErTsG2eZvKYlo2CKaT8MITz","status":"succeeded","usage":"off_session"}
```

# List all SetupAttempts
Returns a list of SetupAttempts that associate with a provided SetupIntent.

### Parameters
- setup_intentstringRequiredOnly return SetupAttempts created by the SetupIntent specified bythis ID.

#### setup_intentstringRequired

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
Adictionarywith adataproperty that containsan array of up tolimitSetupAttempts that are created by thespecified SetupIntent, which start after SetupAttemptsstarting_after. Eachentry in the array is a separate SetupAttempts object. If no otherSetupAttempts are available, the resulting array is be empty. Thisrequest should neverraisean error.

```
curl-G https://api.stripe.com/v1/setup_attempts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3 \-d setup_intent=seti_1ErTsG2eZvKYlo2CKaT8MITz
```

```
curl-G https://api.stripe.com/v1/setup_attempts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3 \-d setup_intent=seti_1ErTsG2eZvKYlo2CKaT8MITz
```

```
{"object":"list","url":"/v1/setup_attempts","has_more":false,"data":[{"id":"setatt_1ErTsH2eZvKYlo2CI7ukcoF7","object":"setup_attempt","application":null,"created":1562004309,"customer_id":null,"flow_directions":null,"livemode":false,"on_behalf_of":null,"payment_instrument":"pm_1ErTsG2eZvKYlo2CH0DNen59","payment_method_details":{"card":{"three_d_secure":null},"type":"card"},"setup_error":null,"setup_intent":"seti_1ErTsG2eZvKYlo2CKaT8MITz","status":"succeeded","usage":"off_session"}]}
```

```
{"object":"list","url":"/v1/setup_attempts","has_more":false,"data":[{"id":"setatt_1ErTsH2eZvKYlo2CI7ukcoF7","object":"setup_attempt","application":null,"created":1562004309,"customer_id":null,"flow_directions":null,"livemode":false,"on_behalf_of":null,"payment_instrument":"pm_1ErTsG2eZvKYlo2CH0DNen59","payment_method_details":{"card":{"three_d_secure":null},"type":"card"},"setup_error":null,"setup_intent":"seti_1ErTsG2eZvKYlo2CKaT8MITz","status":"succeeded","usage":"off_session"}]}
```