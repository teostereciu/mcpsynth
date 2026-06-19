# Notification/6/post/ACCOUNT_HOLDER_CREATED

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/ACCOUNT_HOLDER_CREATED*

---

# Account holder created
Adyen sends this webhook whenan account holder is created.
The details of the account holder creation.
The code of a new account created for the account holder.
The code of the new account holder.
Details of the new account holder.
The address of the account holder.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
Array of bank accounts associated with the account holder. For details about the requiredbankAccountDetailfields, seeRequired information.
The bank account number (without separators).
Refer toRequired informationfor details on field requirements.
The type of bank account.
Only applicable to bank accounts held in the USA.
The permitted values are:checking,savings.
Refer toRequired informationfor details on field requirements.
The name of the bank account.
Merchant reference to the bank account.
The unique identifier (UUID) of the Bank Account.
If, during an account holder create or update request, this field is left blank (but other fields provided), a new Bank Account will be created with a procedurally-generated UUID.
If, during an account holder create request, a UUID is provided, the creation of the Bank Account will fail while the creation of the account holder will continue.
If, during an account holder update request, a UUID that is not correlated with an existing Bank Account is provided, the update of the account holder will fail.
If, during an account holder update request, a UUID that is correlated with an existing Bank Account is provided, the existing Bank Account will be updated.
The bank identifier code.
Refer toRequired informationfor details on field requirements.
The city in which the bank branch is located.
Refer toRequired informationfor details on field requirements.
The bank code of the banking institution with which the bank account is registered.
Refer toRequired informationfor details on field requirements.
The name of the banking institution with which the bank account is held.
Refer toRequired informationfor details on field requirements.
The branch code of the branch under which the bank account is registered. The value to be specified in this parameter depends on the country of the bank account:
- United States - Routing number
- United Kingdom - Sort code
- Germany - Bankleitzahl
Refer toRequired informationfor details on field requirements.
The check code of the bank account.
Refer toRequired informationfor details on field requirements.
The two-letter country code in which the bank account is registered.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
Refer toRequired informationfor details on field requirements.
The currency in which the bank account deals.
The permitted currency codes are defined in ISO-4217 (e.g. 'EUR').
The international bank account number.
The IBAN standard is defined in ISO-13616.
Refer toRequired informationfor details on field requirements.
The city of residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
The country code of the country of residence of the bank account owner.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
Refer toRequired informationfor details on field requirements.
The date of birth of the bank account owner.
The date should be in ISO-8601 format yyyy-mm-dd (e.g. 2000-01-31).
The house name or number of the residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
The name of the bank account owner.
Refer toRequired informationfor details on field requirements.
The country code of the country of nationality of the bank account owner.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
Refer toRequired informationfor details on field requirements.
The postal code of the residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
The state of residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
The street name of the residence of the bank account owner.
Refer toRequired informationfor details on field requirements.
If set to true, the bank account is a primary account.
The tax ID number.
Refer toRequired informationfor details on field requirements.
The URL to be used for bank account verification.
This may be generated on bank account creation.
Refer toRequired informationfor details on field requirements.
The opaque reference value returned by the Adyen API during bank account login.
Details about the business or nonprofit account holder.
Required when creating an account holder withlegalEntityBusinessorNonProfit.
The registered name of the company (if it differs from the legal name of the company).
The legal name of the company.
Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company.
Address of the ultimate parent company.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
Details about the ultimate parent company's business.
The legal name of the company.
The registration number of the company.
Market Identifier Code (MIC).
International Securities Identification Number (ISIN).
Stock Ticker symbol.
Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create an ultimate parent company. Required when updating an existing entry in an/updateAccountHolderrequest.
The registration number of the company.
Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer toour verification guide.
The address of the person.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
The e-mail address of the person.
The phone number of the person provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
Job title of the person. Required when theshareholderTypeisController.
Example values:Chief Executive Officer,Chief Financial Officer,Chief Operating Officer,President,Vice President,Executive President,Managing Member,Partner,Treasurer,Director, orOther.
The name of the person.
The first name.
The gender.
The following values are permitted:MALE,FEMALE,UNKNOWN.
The name's infix, if applicable.
A maximum length of twenty (20) characters is imposed.
The last name.
Contains information about the person.
The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
Array that contains information about the person's identification document. You can submit only one entry per document type.
The expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.
The state where the document was issued (if applicable).
The number in the document.
The type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.
To delete an existing entry for a documenttype, send only thetypefield in your request.
The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.
The phone number of the person.
The two-character country code of the phone number.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
The phone number.
The inclusion of the phone number country code is not necessary.
The type of the phone number.
The following values are permitted:Landline,Mobile,SIP,Fax.
The unique identifier (UUID) of the shareholder entry.
If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Shareholder will be created with a procedurally-generated UUID.
If, during an Account Holder create request, a UUID is provided, the creation of Account Holder will fail with a validation Error..
If, during an Account Holder update request, a UUID that is not correlated with an existing Shareholder is provided, the update of the Shareholder will fail.
If, during an Account Holder update request, a UUID that is correlated with an existing Shareholder is provided, the existing Shareholder will be updated.
Your reference for the shareholder entry.
Specifies how the person is associated with the account holder.
Possible values:
- Owner: Individuals who directly or indirectly own 25% or more of a company.
- Controller: Individuals who are members of senior management staff responsible for managing a company or organization.
The URL of the person's website.
Signatories associated with the company.
Each array entry should represent one signatory.
The address of the person.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
The e-mail address of the person.
The phone number of the person provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
Job title of the signatory.
Example values:Chief Executive Officer,Chief Financial Officer,Chief Operating Officer,President,Vice President,Executive President,Managing Member,Partner,Treasurer,Director, orOther.
The name of the person.
The first name.
The gender.
The following values are permitted:MALE,FEMALE,UNKNOWN.
The name's infix, if applicable.
A maximum length of twenty (20) characters is imposed.
The last name.
Contains information about the person.
The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
Array that contains information about the person's identification document. You can submit only one entry per document type.
The expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.
The state where the document was issued (if applicable).
The number in the document.
The type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.
To delete an existing entry for a documenttype, send only thetypefield in your request.
The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.
The phone number of the person.
The two-character country code of the phone number.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
The phone number.
The inclusion of the phone number country code is not necessary.
The type of the phone number.
The following values are permitted:Landline,Mobile,SIP,Fax.
The unique identifier (UUID) of the signatory.
If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Signatory will be created with a procedurally-generated UUID.
If, during an Account Holder create request, a UUID is provided, the creation of the Signatory will fail while the creation of the Account Holder will continue.
If, during an Account Holder update request, a UUID that is not correlated with an existing Signatory is provided, the update of the Signatory will fail.
If, during an Account Holder update request, a UUID that is correlated with an existing Signatory is provided, the existing Signatory will be updated.
Your reference for the signatory.
The URL of the person's website.
Market Identifier Code (MIC).
International Securities Identification Number (ISIN).
Stock Ticker symbol.
The tax ID of the company.
The email address of the account holder.
The phone number of the account holder provided as a single string. It will be handled as a landline phone.Examples:"0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
Details about the individual account holder.
Required when creating an account holder withlegalEntityIndividual.
The name of the individual.
Make sure your account holder registers using the name shown on their Photo ID.
Maximum length: 80 characters
Cannot contain numbers. /n Cannot be empty.
The first name.
The gender.
The following values are permitted:MALE,FEMALE,UNKNOWN.
The name's infix, if applicable.
A maximum length of twenty (20) characters is imposed.
The last name.
Personal information of the individual.
The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
Array that contains information about the person's identification document. You can submit only one entry per document type.
The expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.
The state where the document was issued (if applicable).
The number in the document.
The type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.
To delete an existing entry for a documenttype, send only thetypefield in your request.
The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.
Date when you last reviewed the account holder's information, in ISO-8601 YYYY-MM-DD format. For example,2020-01-31.
An array containing information about the account holder'slegal arrangements.
The address of the legal arrangement.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement.
Use only when updating an account holder. If you include this field when creating an account holder, the request will fail.
An array containing information about other entities that are part of the legal arrangement.
The address of the entity.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
Required when creating an entity withlegalEntityTypeBusiness,NonProfit,PublicCompany, orPartnership.
The registered name of the company (if it differs from the legal name of the company).
The legal name of the company.
Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company.
Address of the ultimate parent company.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
Details about the ultimate parent company's business.
The legal name of the company.
The registration number of the company.
Market Identifier Code (MIC).
International Securities Identification Number (ISIN).
Stock Ticker symbol.
Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create an ultimate parent company. Required when updating an existing entry in an/updateAccountHolderrequest.
The registration number of the company.
Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer toour verification guide.
The address of the person.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
The e-mail address of the person.
The phone number of the person provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
Job title of the person. Required when theshareholderTypeisController.
Example values:Chief Executive Officer,Chief Financial Officer,Chief Operating Officer,President,Vice President,Executive President,Managing Member,Partner,Treasurer,Director, orOther.
The name of the person.
The first name.
The gender.
The following values are permitted:MALE,FEMALE,UNKNOWN.
The name's infix, if applicable.
A maximum length of twenty (20) characters is imposed.
The last name.
Contains information about the person.
The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
Array that contains information about the person's identification document. You can submit only one entry per document type.
The expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.
The state where the document was issued (if applicable).
The number in the document.
The type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.
To delete an existing entry for a documenttype, send only thetypefield in your request.
The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.
The phone number of the person.
The two-character country code of the phone number.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
The phone number.
The inclusion of the phone number country code is not necessary.
The type of the phone number.
The following values are permitted:Landline,Mobile,SIP,Fax.
The unique identifier (UUID) of the shareholder entry.
If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Shareholder will be created with a procedurally-generated UUID.
If, during an Account Holder create request, a UUID is provided, the creation of Account Holder will fail with a validation Error..
If, during an Account Holder update request, a UUID that is not correlated with an existing Shareholder is provided, the update of the Shareholder will fail.
If, during an Account Holder update request, a UUID that is correlated with an existing Shareholder is provided, the existing Shareholder will be updated.
Your reference for the shareholder entry.
Specifies how the person is associated with the account holder.
Possible values:
- Owner: Individuals who directly or indirectly own 25% or more of a company.
- Controller: Individuals who are members of senior management staff responsible for managing a company or organization.
The URL of the person's website.
Signatories associated with the company.
Each array entry should represent one signatory.
The address of the person.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
The e-mail address of the person.
The phone number of the person provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
Job title of the signatory.
Example values:Chief Executive Officer,Chief Financial Officer,Chief Operating Officer,President,Vice President,Executive President,Managing Member,Partner,Treasurer,Director, orOther.
The name of the person.
The first name.
The gender.
The following values are permitted:MALE,FEMALE,UNKNOWN.
The name's infix, if applicable.
A maximum length of twenty (20) characters is imposed.
The last name.
Contains information about the person.
The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
Array that contains information about the person's identification document. You can submit only one entry per document type.
The expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.
The state where the document was issued (if applicable).
The number in the document.
The type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.
To delete an existing entry for a documenttype, send only thetypefield in your request.
The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.
The phone number of the person.
The two-character country code of the phone number.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
The phone number.
The inclusion of the phone number country code is not necessary.
The type of the phone number.
The following values are permitted:Landline,Mobile,SIP,Fax.
The unique identifier (UUID) of the signatory.
If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Signatory will be created with a procedurally-generated UUID.
If, during an Account Holder create request, a UUID is provided, the creation of the Signatory will fail while the creation of the Account Holder will continue.
If, during an Account Holder update request, a UUID that is not correlated with an existing Signatory is provided, the update of the Signatory will fail.
If, during an Account Holder update request, a UUID that is correlated with an existing Signatory is provided, the existing Signatory will be updated.
Your reference for the signatory.
The URL of the person's website.
Market Identifier Code (MIC).
International Securities Identification Number (ISIN).
Stock Ticker symbol.
The tax ID of the company.
The e-mail address of the entity.
The phone number of the contact provided as a single string.  It will be handled as a landline phone.Examples:"0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
Required when creating an entity withlegalEntityTypeIndividual.
The name of the individual.
Make sure your account holder registers using the name shown on their Photo ID.
Maximum length: 80 characters
Cannot contain numbers. /n Cannot be empty.
The first name.
The gender.
The following values are permitted:MALE,FEMALE,UNKNOWN.
The name's infix, if applicable.
A maximum length of twenty (20) characters is imposed.
The last name.
Personal information of the individual.
The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
Array that contains information about the person's identification document. You can submit only one entry per document type.
The expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.
The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.
The state where the document was issued (if applicable).
The number in the document.
The type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.
To delete an existing entry for a documenttype, send only thetypefield in your request.
The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.
Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement entity.
Use only when updating an account holder. If you include this field when creating an account holder, the request will fail.
Your reference for the legal arrangement entity.
An array containing the roles of the entity in the legal arrangement.
The possible values depend on the legal arrangementtype.
- FortypeAssociation:ControllingPersonandShareholder.
- FortypePartnership:PartnerandShareholder.
- FortypeTrust:Trustee,Settlor,Protector,Beneficiary,  andShareholder.
The legal entity type.
Possible values:Business,Individual,NonProfit,PublicCompany, orPartnership.
The phone number of the entity.
The two-character country code of the phone number.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
The phone number.
The inclusion of the phone number country code is not necessary.
The type of the phone number.
The following values are permitted:Landline,Mobile,SIP,Fax.
The URL of the website of the contact.
Your reference for the legal arrangement. Must be between 3 to 128 characters.
The form of legal arrangement. Required iftypeisTrustorPartnership.
The possible values depend on thetype.
- FortypeTrust:CashManagementTrust,CorporateUnitTrust,DeceasedEstate,DiscretionaryInvestmentTrust,DiscretionaryServicesManagementTrust,DiscretionaryTradingTrust,FirstHomeSaverAccountsTrust,FixedTrust,FixedUnitTrust,HybridTrust,ListedPublicUnitTrust,OtherTrust,PooledSuperannuationTrust,PublicTradingTrust, orUnlistedPublicUnitTrust.
- FortypePartnership:LimitedPartnership,FamilyPartnership, orOtherPartnership
The legal name of the legal arrangement. Minimum length: 3 characters.
The registration number of the legal arrangement.
The tax identification number of the legal arrangement.
Thetype of legal arrangement.
Possible values:
- Association
- Partnership
- SoleProprietorship
- Trust
The Merchant Category Code of the account holder.
If not specified in the request, this will be derived from the platform account (which is configured by Adyen).
A set of key and value pairs for general use by the account holder or merchant.
The keys do not have specific names and may be used for storing miscellaneous data as desired.
The values being stored have a maximum length of eighty (80) characters and will be truncated if necessary.
Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs.
Array of tokenized card details associated with the account holder. For details about how you can use the tokens to pay out, refer toPay out to cards.
ThemerchantAccountyou used in the/paymentsrequest when yousaved the account holder's card details.

```
merchantAccount
```
Adyen-generated unique alphanumeric identifier (UUID) for the payout method, returned in the response when you create a payout method. Required when updating an existing payout method in an/updateAccountHolderrequest.
Your reference for the payout method.
TherecurringDetailReferencereturned in the/paymentsresponse when yousaved the account holder's card details.

```
recurringDetailReference
```
TheshopperReferenceyou sent in the/paymentsrequest when yousaved the account holder's card details.

```
shopperReference
```
The phone number of the account holder.
Required if afullPhoneNumberis not provided.
The two-character country code of the phone number.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
The phone number.
The inclusion of the phone number country code is not necessary.
The type of the phone number.
The following values are permitted:Landline,Mobile,SIP,Fax.
The principal business address of the account holder.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
Array of stores associated with the account holder. Required when onboarding account holders that have an Adyenpoint of sale.
The address of the physical store where the account holder will process payments from.
The name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.
The two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.
The number or name of the house.
The postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.
Maximum length:
- 5 digits for addresses in the US.
- 10 characters for all other countries.
The abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.
Maximum length:
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
The name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.
The phone number of the store provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
Store logo for payment method setup.
The merchant account to which the store belongs.
The merchant category code (MCC) that classifies the business of the account holder.
Merchant house number for payment method setup.
The phone number of the store.
The two-character country code of the phone number.
The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').
The phone number.
The inclusion of the phone number country code is not necessary.
The type of the phone number.
The following values are permitted:Landline,Mobile,SIP,Fax.
The sales channel. Possible values:Ecommerce,POS.
The unique reference for the split configuration, returned when you configure splits in your Customer Area. When this is provided, thevirtualAccountis also required. Adyen uses the configuration and thevirtualAccountto split funds between accounts in your platform.
The status of the store. Possible values:Pending,Active,Inactive,InactiveWithModifications,Closed.
Adyen-generated unique alphanumeric identifier (UUID) for the store, returned in the response when you create a store. Required when updating an existing store in an/updateAccountHolderrequest.
The name of the account holder's store. This value is shown in shopper statements.
- Length: Between 3 to 22 characters
- The following characters arenotsupported::;}{$#@!|<>%^*+=\
Note:storeName does not appear in American Express shopper statements by default. Contact Adyen Support to enable this for American Express.
Your unique identifier for the store. The Customer Area also uses this value for the store description.
- Length: Between 3 to 128 characters
- The following characters arenotsupported::;}{$#@!|<>%^*+=\
The account holder'saccountCodewhere the split amount will be sent. Required when you provide thesplitConfigurationUUID.
URL of the ecommerce store.
The URL of the website of the account holder.
The status of the new account holder.
A list of events scheduled for the account holder.
The event.
Permitted values:InactivateAccount,RefundNotPaidOutTransfers.
For more information, refer toVerification checks.
The date on which the event will take place.
The reason why this event has been created.
The payout state of the account holder.
Indicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payouts will be permitted for any of the account holder's accounts. If this field is true, payouts will be permitted for any of the account holder's accounts.
The reason why payouts (to all of the account holder's accounts) have been disabled (by the platform). If thedisabledfield is true, this field can be used to explain why.
Indicates whether payouts have been disabled (by the platform) for all of the account holder's accounts. A platform may enable and disable this field at their discretion. If this field is true,allowPayoutwill be false and no payouts will be permitted for any of the account holder's accounts. If this field is false,allowPayoutmay or may not be enabled, depending on other factors.
The reason why payouts (to all of the account holder's accounts) have been disabled (by Adyen). If payouts have been disabled by Adyen, this field will explain why. If this field is blank, payouts have not been disabled by Adyen.
The maximum amount that payouts are limited to. Only applies if payouts are allowed but limited.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The payout tier that the account holder occupies.
The processing state of the account holder.
The reason why processing has been disabled.
Indicates whether the processing of payments is allowed.
The lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money in order to be placed into this tier).
The three-characterISO currency code.
The amount of the transaction, inminor units.
The upper bound of the processing tier (i.e., an account holder must have processed less than this amount of money in order to be placed into this tier).
The three-characterISO currency code.
The amount of the transaction, inminor units.
The processing tier that the account holder occupies.
The status of the account holder.
Permitted values:Active,Inactive,Suspended,Closed.
The reason why the status was assigned to the account holder.
The description of the new account holder.
A list of fields that caused the/createAccountHolderrequest to fail.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
The type of legal entity of the new account holder.
The three-characterISO currency code, with which the prospective account holder primarily deals.
The reference of a request. Can be used to uniquely identify the request.
The result code.
The details of KYC Verification of the account holder.
The results of the checks on the account holder.
A list of the checks and their statuses.
A list of the fields required for execution of the check.
The status of the check.
Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.
A summary of the execution of the check.
The code of the check. For possible values, refer toVerification codes.
A description of the check.
The type of check.
Possible values:
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
The results of the checks on the legal arrangements.
A list of the checks and their statuses.
A list of the fields required for execution of the check.
The status of the check.
Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.
A summary of the execution of the check.
The code of the check. For possible values, refer toVerification codes.
A description of the check.
The type of check.
Possible values:
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
The unique ID of the legal arrangement to which the check applies.
The results of the checks on the legal arrangement entities.
A list of the checks and their statuses.
A list of the fields required for execution of the check.
The status of the check.
Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.
A summary of the execution of the check.
The code of the check. For possible values, refer toVerification codes.
A description of the check.
The type of check.
Possible values:
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
The unique ID of the legal arrangement to which the entity belongs.
The unique ID of the legal arrangement entity to which the check applies.
The results of the checks on the payout methods.
A list of the checks and their statuses.
A list of the fields required for execution of the check.
The status of the check.
Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.
A summary of the execution of the check.
The code of the check. For possible values, refer toVerification codes.
A description of the check.
The type of check.
Possible values:
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
The unique ID of the payoput method to which the check applies.
The results of the checks on the shareholders.
A list of the checks and their statuses.
A list of the fields required for execution of the check.
The status of the check.
Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.
A summary of the execution of the check.
The code of the check. For possible values, refer toVerification codes.
A description of the check.
The type of check.
Possible values:
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
The unique ID of the legal arrangement to which the shareholder belongs, if applicable.
The unique ID of the legal arrangement entity to which the shareholder belongs, if applicable.
The code of the shareholder to which the check applies.
The results of the checks on the signatories.
A list of the checks and their statuses.
A list of the fields required for execution of the check.
The status of the check.
Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.
A summary of the execution of the check.
The code of the check. For possible values, refer toVerification codes.
A description of the check.
The type of check.
Possible values:
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
The code of the signatory to which the check applies.
The result of the check on the Ultimate Parent Company.
A list of the checks and their statuses.
A list of the fields required for execution of the check.
The status of the check.
Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.
A summary of the execution of the check.
The code of the check. For possible values, refer toVerification codes.
A description of the check.
The type of check.
Possible values:
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
The code of the Ultimate Parent Company to which the check applies.
The identifier of the profile that applies to this entity.
Error information of failed request. No value provided here if no error occurred on processing.
The Adyen code that is mapped to the error message.
A short explanation of the issue.
The date and time when an event has been completed.
The event type of the notification.
The user or process that has triggered the notification.
Indicates whether the notification originated from the live environment or the test environment. If true, the notification originated from the live environment. If false, the notification originated from the test environment.
The PSP reference of the request from which the notification originates.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringSet this parameter to[accepted]to acknowledge that you received a notification from Adyen.

#### 200 - OK