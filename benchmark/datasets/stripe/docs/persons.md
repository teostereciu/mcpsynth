# persons

*Source: https://docs.stripe.com/api/persons*

---

# Person
This is an object representing a person associated with a Stripe account.
A platform can only access a subset of data in a person for an account whereaccount.controller.requirement_collectionisstripe, which includes Standard and Express accounts, after creating an Account Link or Account Session to start Connect onboarding.
See theStandard onboardingorExpress onboardingdocumentation for information about prefilling information and account onboarding steps. Learn more abouthandling identity verification with the API.

# The Person object

### Attributes
- idstringUnique identifier for the object.
- accountstringThe account the person is associated with.
- addressnullableobjectThe person’s address.Show child attributes
- dobnullableobjectThe person’s date of birth.Show child attributes
- emailnullablestringThe person’s email address. Also available for accounts wherecontroller.requirement_collectionisstripe.
- first_namenullablestringThe person’s first name. Also available for accounts wherecontroller.requirement_collectionisstripe.
- last_namenullablestringThe person’s last name. Also available for accounts wherecontroller.requirement_collectionisstripe.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- phonenullablestringThe person’s phone number.
- relationshipobjectDescribes the person’s relationship to the account. Also available for accounts wherecontroller.requirement_collectionisstripe.Show child attributes
- requirementsnullableobjectInformation about the requirements for this person, including what information needs to be collected, and by when.Show child attributes

#### idstring

#### accountstring

#### addressnullableobject

#### dobnullableobject

#### emailnullablestring

#### first_namenullablestring

#### last_namenullablestring

#### metadataobject

#### phonenullablestring

#### relationshipobject

#### requirementsnullableobject

### More attributesExpand all
- objectstring
- additional_tos_acceptancesobject
- address_kananullableobject
- address_kanjinullableobject
- createdtimestamp
- first_name_kananullablestring
- first_name_kanjinullablestring
- full_name_aliasesnullablearray of strings
- future_requirementsnullableobject
- gendernullableenum
- id_number_providedboolean
- id_number_secondary_providednullableboolean
- last_name_kananullablestring
- last_name_kanjinullablestring
- maiden_namenullablestring
- nationalitynullablestring
- political_exposurenullableenum
- registered_addressnullableobject
- ssn_last_4_providedboolean
- us_cfpb_datanullableobject
- verificationobject

#### objectstring

#### additional_tos_acceptancesobject

#### address_kananullableobject

#### address_kanjinullableobject

#### createdtimestamp

#### first_name_kananullablestring

#### first_name_kanjinullablestring

#### full_name_aliasesnullablearray of strings

#### future_requirementsnullableobject

#### gendernullableenum

#### id_number_providedboolean

#### id_number_secondary_providednullableboolean

#### last_name_kananullablestring

#### last_name_kanjinullablestring

#### maiden_namenullablestring

#### nationalitynullablestring

#### political_exposurenullableenum

#### registered_addressnullableobject

#### ssn_last_4_providedboolean

#### us_cfpb_datanullableobject

#### verificationobject

# Create a person
Creates a new person.

### Parameters
- addressobjectThe person’s address.Show child parameters
- dobobjectThe person’s date of birth.Show child parameters
- emailstringThe person’s email address.The maximum length is 800 characters.
- first_namestringThe person’s first name.
- id_numberstringThe person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide aPII token provided by Stripe.js.
- last_namestringThe person’s last name.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- phonestringThe person’s phone number.
- relationshipobjectThe relationship that this person has with the account’s legal entity.Show child parameters
- ssn_last_4stringThe last four digits of the person’s Social Security number (U.S. only).

#### addressobject

#### dobobject

#### emailstring

#### first_namestring

#### id_numberstring

#### last_namestring

#### metadataobject

#### phonestring

#### relationshipobject

#### ssn_last_4string

### More parametersExpand all
- additional_tos_acceptancesobject
- address_kanaobject
- address_kanjiobject
- documentsobject
- first_name_kanastring
- first_name_kanjistring
- full_name_aliasesarray of strings
- genderenum
- id_number_secondarystring
- last_name_kanastring
- last_name_kanjistring
- maiden_namestring
- nationalitystring
- person_tokenstring
- political_exposureenum
- registered_addressobject
- us_cfpb_dataobject
- verificationobject

#### additional_tos_acceptancesobject

#### address_kanaobject

#### address_kanjiobject

#### documentsobject

#### first_name_kanastring

#### first_name_kanjistring

#### full_name_aliasesarray of strings

#### genderenum

#### id_number_secondarystring

#### last_name_kanastring

#### last_name_kanjistring

#### maiden_namestring

#### nationalitystring

#### person_tokenstring

#### political_exposureenum

#### registered_addressobject

#### us_cfpb_dataobject

#### verificationobject

### Returns
Returns apersonobject.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d first_name=John \-d last_name=Doe
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d first_name=John \-d last_name=Doe
```

```
{"id":"person_1N9XNb2eZvKYlo2CjPX7xF6F","object":"person","account":"acct_1032D82eZvKYlo2C","created":1684518375,"dob":{"day":null,"month":null,"year":null},"first_name":"John","future_requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"id_number_provided":false,"last_name":"Doe","metadata":{},"relationship":{"director":false,"executive":false,"owner":false,"percent_ownership":null,"representative":false,"title":null},"requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"ssn_last_4_provided":false,"verification":{"additional_document":{"back":null,"details":null,"details_code":null,"front":null},"details":null,"details_code":null,"document":{"back":null,"details":null,"details_code":null,"front":null},"status":"unverified"}}
```

```
{"id":"person_1N9XNb2eZvKYlo2CjPX7xF6F","object":"person","account":"acct_1032D82eZvKYlo2C","created":1684518375,"dob":{"day":null,"month":null,"year":null},"first_name":"John","future_requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"id_number_provided":false,"last_name":"Doe","metadata":{},"relationship":{"director":false,"executive":false,"owner":false,"percent_ownership":null,"representative":false,"title":null},"requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"ssn_last_4_provided":false,"verification":{"additional_document":{"back":null,"details":null,"details_code":null,"front":null},"details":null,"details_code":null,"document":{"back":null,"details":null,"details_code":null,"front":null},"status":"unverified"}}
```

# Update a person
Updates an existing person.

### Parameters
- addressobjectThe person’s address.Show child parameters
- dobobjectThe person’s date of birth.Show child parameters
- emailstringThe person’s email address.The maximum length is 800 characters.
- first_namestringThe person’s first name.
- id_numberstringThe person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide aPII token provided by Stripe.js.
- last_namestringThe person’s last name.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- phonestringThe person’s phone number.
- relationshipobjectThe relationship that this person has with the account’s legal entity.Show child parameters
- ssn_last_4stringThe last four digits of the person’s Social Security number (U.S. only).

#### addressobject

#### dobobject

#### emailstring

#### first_namestring

#### id_numberstring

#### last_namestring

#### metadataobject

#### phonestring

#### relationshipobject

#### ssn_last_4string

### More parametersExpand all
- additional_tos_acceptancesobject
- address_kanaobject
- address_kanjiobject
- documentsobject
- first_name_kanastring
- first_name_kanjistring
- full_name_aliasesarray of strings
- genderenum
- id_number_secondarystring
- last_name_kanastring
- last_name_kanjistring
- maiden_namestring
- nationalitystring
- person_tokenstring
- political_exposureenum
- registered_addressobject
- us_cfpb_dataobject
- verificationobject

#### additional_tos_acceptancesobject

#### address_kanaobject

#### address_kanjiobject

#### documentsobject

#### first_name_kanastring

#### first_name_kanjistring

#### full_name_aliasesarray of strings

#### genderenum

#### id_number_secondarystring

#### last_name_kanastring

#### last_name_kanjistring

#### maiden_namestring

#### nationalitystring

#### person_tokenstring

#### political_exposureenum

#### registered_addressobject

#### us_cfpb_dataobject

#### verificationobject

### Returns
Returns apersonobject.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"person_1MqjB62eZvKYlo2CaeEJzKVR","person":"person_1MqjB62eZvKYlo2CaeEJzKVR","object":"person","account":"acct_1032D82eZvKYlo2C","created":1680035496,"dob":{"day":null,"month":null,"year":null},"first_name":"Jane","future_requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"id_number_provided":false,"last_name":"Diaz","metadata":{"order_id":"6735"},"relationship":{"director":false,"executive":false,"owner":false,"percent_ownership":null,"representative":false,"title":null},"requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"ssn_last_4_provided":false,"verification":{"additional_document":{"back":null,"details":null,"details_code":null,"front":null},"details":null,"details_code":null,"document":{"back":null,"details":null,"details_code":null,"front":null},"status":"unverified"}}
```

```
{"id":"person_1MqjB62eZvKYlo2CaeEJzKVR","person":"person_1MqjB62eZvKYlo2CaeEJzKVR","object":"person","account":"acct_1032D82eZvKYlo2C","created":1680035496,"dob":{"day":null,"month":null,"year":null},"first_name":"Jane","future_requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"id_number_provided":false,"last_name":"Diaz","metadata":{"order_id":"6735"},"relationship":{"director":false,"executive":false,"owner":false,"percent_ownership":null,"representative":false,"title":null},"requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"ssn_last_4_provided":false,"verification":{"additional_document":{"back":null,"details":null,"details_code":null,"front":null},"details":null,"details_code":null,"document":{"back":null,"details":null,"details_code":null,"front":null},"status":"unverified"}}
```

# Retrieve a person
Retrieves an existing person.

### Parameters
Noparameters.

### Returns
Returns apersonobject.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"person_1N9XNb2eZvKYlo2CjPX7xF6F","object":"person","account":"acct_1032D82eZvKYlo2C","created":1684518375,"dob":{"day":null,"month":null,"year":null},"first_name":null,"future_requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"id_number_provided":false,"last_name":null,"metadata":{},"relationship":{"director":false,"executive":false,"owner":false,"percent_ownership":null,"representative":false,"title":null},"requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"ssn_last_4_provided":false,"verification":{"additional_document":{"back":null,"details":null,"details_code":null,"front":null},"details":null,"details_code":null,"document":{"back":null,"details":null,"details_code":null,"front":null},"status":"unverified"}}
```

```
{"id":"person_1N9XNb2eZvKYlo2CjPX7xF6F","object":"person","account":"acct_1032D82eZvKYlo2C","created":1684518375,"dob":{"day":null,"month":null,"year":null},"first_name":null,"future_requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"id_number_provided":false,"last_name":null,"metadata":{},"relationship":{"director":false,"executive":false,"owner":false,"percent_ownership":null,"representative":false,"title":null},"requirements":{"alternatives":[],"currently_due":[],"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"ssn_last_4_provided":false,"verification":{"additional_document":{"back":null,"details":null,"details_code":null,"front":null},"details":null,"details_code":null,"document":{"back":null,"details":null,"details_code":null,"front":null},"status":"unverified"}}
```