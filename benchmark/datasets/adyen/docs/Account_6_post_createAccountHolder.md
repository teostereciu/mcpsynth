# Account/6/post/createAccountHolder

*Source: https://docs.adyen.com/api-explorer/Account/6/post/createAccountHolder*

---

# Create an account holder
Creates an account holder thatrepresents the sub-merchant's entityin your platform. The details that you need to provide in the request depend on the sub-merchant's legal entity type. For more information, refer toAccount holder and accounts.
Your unique identifier for the prospective account holder.
The length must be between three (3) and fifty (50) characters long. Only letters, digits, and hyphens (-) are allowed.
The details of the prospective account holder.
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
If set totrue, an account with the default options is automatically created for the account holder.
By default, this field is set totrue.
A description of the prospective account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores_.
The legal entity type of the account holder. This determines the information that should be provided in the request.
Possible values:Business,Individual, orNonProfit.
- If set toBusinessorNonProfit, thenaccountHolderDetails.businessDetailsmust be provided, with at least one entry in theaccountHolderDetails.businessDetails.shareholderslist.
- If set toIndividual, thenaccountHolderDetails.individualDetailsmust be provided.
The three-characterISO currency code, with which the prospective account holder primarily deals.
The startingprocessing tierfor the prospective account holder.
The identifier of the profile that applies to this entity.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessaccountCodestringThe code of a new account created for the account holder.accountHolderCodestringThe code of the new account holder.accountHolderDetailsobjectDetails of the new account holder.Show childrenHide childrenaddressobjectThe address of the account holder.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.bankAccountDetailsarray[object]Array of bank accounts associated with the account holder. For details about the requiredbankAccountDetailfields, seeRequired information.Show childrenHide childrenaccountNumberstringThe bank account number (without separators).Refer toRequired informationfor details on field requirements.accountTypestringThe type of bank account.
Only applicable to bank accounts held in the USA.
The permitted values are:checking,savings.Refer toRequired informationfor details on field requirements.bankAccountNamestringThe name of the bank account.bankAccountReferencestringMerchant reference to the bank account.bankAccountUUIDstringThe unique identifier (UUID) of the Bank Account.If, during an account holder create or update request, this field is left blank (but other fields provided), a new Bank Account will be created with a procedurally-generated UUID.If, during an account holder create request, a UUID is provided, the creation of the Bank Account will fail while the creation of the account holder will continue.If, during an account holder update request, a UUID that is not correlated with an existing Bank Account is provided, the update of the account holder will fail.If, during an account holder update request, a UUID that is correlated with an existing Bank Account is provided, the existing Bank Account will be updated.bankBicSwiftstringThe bank identifier code.Refer toRequired informationfor details on field requirements.bankCitystringThe city in which the bank branch is located.Refer toRequired informationfor details on field requirements.bankCodestringThe bank code of the banking institution with which the bank account is registered.Refer toRequired informationfor details on field requirements.bankNamestringThe name of the banking institution with which the bank account is held.Refer toRequired informationfor details on field requirements.branchCodestringThe branch code of the branch under which the bank account is registered. The value to be specified in this parameter depends on the country of the bank account:United States - Routing numberUnited Kingdom - Sort codeGermany - BankleitzahlRefer toRequired informationfor details on field requirements.checkCodestringThe check code of the bank account.Refer toRequired informationfor details on field requirements.countryCodestringThe two-letter country code in which the bank account is registered.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').Refer toRequired informationfor details on field requirements.currencyCodestringThe currency in which the bank account deals.The permitted currency codes are defined in ISO-4217 (e.g. 'EUR').ibanstringThe international bank account number.The IBAN standard is defined in ISO-13616.Refer toRequired informationfor details on field requirements.ownerCitystringThe city of residence of the bank account owner.Refer toRequired informationfor details on field requirements.ownerCountryCodestringThe country code of the country of residence of the bank account owner.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').Refer toRequired informationfor details on field requirements.ownerDateOfBirthstringDeprecatedThe date of birth of the bank account owner.
The date should be in ISO-8601 format yyyy-mm-dd (e.g. 2000-01-31).ownerHouseNumberOrNamestringThe house name or number of the residence of the bank account owner.Refer toRequired informationfor details on field requirements.ownerNamestringThe name of the bank account owner.Refer toRequired informationfor details on field requirements.ownerNationalitystringThe country code of the country of nationality of the bank account owner.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').Refer toRequired informationfor details on field requirements.ownerPostalCodestringThe postal code of the residence of the bank account owner.Refer toRequired informationfor details on field requirements.ownerStatestringThe state of residence of the bank account owner.Refer toRequired informationfor details on field requirements.ownerStreetstringThe street name of the residence of the bank account owner.Refer toRequired informationfor details on field requirements.primaryAccountbooleanIf set to true, the bank account is a primary account.taxIdstringThe tax ID number.Refer toRequired informationfor details on field requirements.urlForVerificationstringThe URL to be used for bank account verification.
This may be generated on bank account creation.Refer toRequired informationfor details on field requirements.bankAggregatorDataReferencestringThe opaque reference value returned by the Adyen API during bank account login.businessDetailsobjectDetails about the business or nonprofit account holder.
Required when creating an account holder withlegalEntityBusinessorNonProfit.Show childrenHide childrendoingBusinessAsstringThe registered name of the company (if it differs from the legal name of the company).legalBusinessNamestringThe legal name of the company.listedUltimateParentCompanyarray[object]Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company.Show childrenHide childrenaddressobjectAddress of the ultimate parent company.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.businessDetailsobjectDetails about the ultimate parent company's business.Show childrenHide childrenlegalBusinessNamestringThe legal name of the company.registrationNumberstringThe registration number of the company.stockExchangestringMarket Identifier Code (MIC).stockNumberstringInternational Securities Identification Number (ISIN).stockTickerstringStock Ticker symbol.ultimateParentCompanyCodestringAdyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create an ultimate parent company. Required when updating an existing entry in an/updateAccountHolderrequest.registrationNumberstringThe registration number of the company.shareholdersarray[object]Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer toour verification guide.Show childrenHide childrenaddressobjectThe address of the person.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.emailstringThe e-mail address of the person.fullPhoneNumberstringThe phone number of the person provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"jobTitlestringJob title of the person. Required when theshareholderTypeisController.Example values:Chief Executive Officer,Chief Financial Officer,Chief Operating Officer,President,Vice President,Executive President,Managing Member,Partner,Treasurer,Director, orOther.nameobjectThe name of the person.Show childrenHide childrenfirstNamestringMax length:80The first name.genderstringMax length:1The gender.The following values are permitted:MALE,FEMALE,UNKNOWN.infixstringMax length:20The name's infix, if applicable.A maximum length of twenty (20) characters is imposed.lastNamestringMax length:80The last name.personalDataobjectContains information about the person.Show childrenHide childrendateOfBirthstringThe person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.documentDataarray[object]Array that contains information about the person's identification document. You can submit only one entry per document type.Show childrenHide childrenexpirationDatestringThe expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.issuerCountrystringMin length:2Max length:2The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.issuerStatestringThe state where the document was issued (if applicable).numberstringThe number in the document.typestringThe type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.To delete an existing entry for a documenttype, send only thetypefield in your request.nationalitystringMin length:2Max length:2The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.phoneNumberobjectThe phone number of the person.Show childrenHide childrenphoneCountryCodestringThe two-character country code of the phone number.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').phoneNumberstringThe phone number.The inclusion of the phone number country code is not necessary.phoneTypestringThe type of the phone number.The following values are permitted:Landline,Mobile,SIP,Fax.shareholderCodestringThe unique identifier (UUID) of the shareholder entry.If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Shareholder will be created with a procedurally-generated UUID.If, during an Account Holder create request, a UUID is provided, the creation of Account Holder will fail with a validation Error..If, during an Account Holder update request, a UUID that is not correlated with an existing Shareholder is provided, the update of the Shareholder will fail.If, during an Account Holder update request, a UUID that is correlated with an existing Shareholder is provided, the existing Shareholder will be updated.shareholderReferencestringYour reference for the shareholder entry.shareholderTypestringSpecifies how the person is associated with the account holder.Possible values:Owner: Individuals who directly or indirectly own 25% or more of a company.Controller: Individuals who are members of senior management staff responsible for managing a company or organization.webAddressstringThe URL of the person's website.signatoriesarray[object]Signatories associated with the company.
Each array entry should represent one signatory.Show childrenHide childrenaddressobjectThe address of the person.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.emailstringThe e-mail address of the person.fullPhoneNumberstringThe phone number of the person provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"jobTitlestringJob title of the signatory.Example values:Chief Executive Officer,Chief Financial Officer,Chief Operating Officer,President,Vice President,Executive President,Managing Member,Partner,Treasurer,Director, orOther.nameobjectThe name of the person.Show childrenHide childrenfirstNamestringMax length:80The first name.genderstringMax length:1The gender.The following values are permitted:MALE,FEMALE,UNKNOWN.infixstringMax length:20The name's infix, if applicable.A maximum length of twenty (20) characters is imposed.lastNamestringMax length:80The last name.personalDataobjectContains information about the person.Show childrenHide childrendateOfBirthstringThe person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.documentDataarray[object]Array that contains information about the person's identification document. You can submit only one entry per document type.Show childrenHide childrenexpirationDatestringThe expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.issuerCountrystringMin length:2Max length:2The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.issuerStatestringThe state where the document was issued (if applicable).numberstringThe number in the document.typestringThe type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.To delete an existing entry for a documenttype, send only thetypefield in your request.nationalitystringMin length:2Max length:2The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.phoneNumberobjectThe phone number of the person.Show childrenHide childrenphoneCountryCodestringThe two-character country code of the phone number.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').phoneNumberstringThe phone number.The inclusion of the phone number country code is not necessary.phoneTypestringThe type of the phone number.The following values are permitted:Landline,Mobile,SIP,Fax.signatoryCodestringThe unique identifier (UUID) of the signatory.If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Signatory will be created with a procedurally-generated UUID.If, during an Account Holder create request, a UUID is provided, the creation of the Signatory will fail while the creation of the Account Holder will continue.If, during an Account Holder update request, a UUID that is not correlated with an existing Signatory is provided, the update of the Signatory will fail.If, during an Account Holder update request, a UUID that is correlated with an existing Signatory is provided, the existing Signatory will be updated.signatoryReferencestringYour reference for the signatory.webAddressstringThe URL of the person's website.stockExchangestringMarket Identifier Code (MIC).stockNumberstringInternational Securities Identification Number (ISIN).stockTickerstringStock Ticker symbol.taxIdstringThe tax ID of the company.emailstringThe email address of the account holder.fullPhoneNumberstringThe phone number of the account holder provided as a single string. It will be handled as a landline phone.Examples:"0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"individualDetailsobjectDetails about the individual account holder.
Required when creating an account holder withlegalEntityIndividual.Show childrenHide childrennameobjectThe name of the individual.Make sure your account holder registers using the name shown on their Photo ID.
Maximum length: 80 characters
Cannot contain numbers. /n Cannot be empty.Show childrenHide childrenfirstNamestringMax length:80The first name.genderstringMax length:1The gender.The following values are permitted:MALE,FEMALE,UNKNOWN.infixstringMax length:20The name's infix, if applicable.A maximum length of twenty (20) characters is imposed.lastNamestringMax length:80The last name.personalDataobjectPersonal information of the individual.Show childrenHide childrendateOfBirthstringThe person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.documentDataarray[object]Array that contains information about the person's identification document. You can submit only one entry per document type.Show childrenHide childrenexpirationDatestringThe expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.issuerCountrystringMin length:2Max length:2The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.issuerStatestringThe state where the document was issued (if applicable).numberstringThe number in the document.typestringThe type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.To delete an existing entry for a documenttype, send only thetypefield in your request.nationalitystringMin length:2Max length:2The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.lastReviewDatestringDate when you last reviewed the account holder's information, in ISO-8601 YYYY-MM-DD format. For example,2020-01-31.legalArrangementsarray[object]An array containing information about the account holder'slegal arrangements.Show childrenHide childrenaddressobjectThe address of the legal arrangement.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.legalArrangementCodestringAdyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement.
Use only when updating an account holder. If you include this field when creating an account holder, the request will fail.legalArrangementEntitiesarray[object]An array containing information about other entities that are part of the legal arrangement.Show childrenHide childrenaddressobjectThe address of the entity.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.businessDetailsobjectRequired when creating an entity withlegalEntityTypeBusiness,NonProfit,PublicCompany, orPartnership.Show childrenHide childrendoingBusinessAsstringThe registered name of the company (if it differs from the legal name of the company).legalBusinessNamestringThe legal name of the company.listedUltimateParentCompanyarray[object]Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company.Show childrenHide childrenaddressobjectAddress of the ultimate parent company.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.businessDetailsobjectDetails about the ultimate parent company's business.Show childrenHide childrenlegalBusinessNamestringThe legal name of the company.registrationNumberstringThe registration number of the company.stockExchangestringMarket Identifier Code (MIC).stockNumberstringInternational Securities Identification Number (ISIN).stockTickerstringStock Ticker symbol.ultimateParentCompanyCodestringAdyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create an ultimate parent company. Required when updating an existing entry in an/updateAccountHolderrequest.registrationNumberstringThe registration number of the company.shareholdersarray[object]Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer toour verification guide.Show childrenHide childrenaddressobjectThe address of the person.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.emailstringThe e-mail address of the person.fullPhoneNumberstringThe phone number of the person provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"jobTitlestringJob title of the person. Required when theshareholderTypeisController.Example values:Chief Executive Officer,Chief Financial Officer,Chief Operating Officer,President,Vice President,Executive President,Managing Member,Partner,Treasurer,Director, orOther.nameobjectThe name of the person.Show childrenHide childrenfirstNamestringMax length:80The first name.genderstringMax length:1The gender.The following values are permitted:MALE,FEMALE,UNKNOWN.infixstringMax length:20The name's infix, if applicable.A maximum length of twenty (20) characters is imposed.lastNamestringMax length:80The last name.personalDataobjectContains information about the person.Show childrenHide childrendateOfBirthstringThe person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.documentDataarray[object]Array that contains information about the person's identification document. You can submit only one entry per document type.Show childrenHide childrenexpirationDatestringThe expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.issuerCountrystringMin length:2Max length:2The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.issuerStatestringThe state where the document was issued (if applicable).numberstringThe number in the document.typestringThe type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.To delete an existing entry for a documenttype, send only thetypefield in your request.nationalitystringMin length:2Max length:2The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.phoneNumberobjectThe phone number of the person.Show childrenHide childrenphoneCountryCodestringThe two-character country code of the phone number.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').phoneNumberstringThe phone number.The inclusion of the phone number country code is not necessary.phoneTypestringThe type of the phone number.The following values are permitted:Landline,Mobile,SIP,Fax.shareholderCodestringThe unique identifier (UUID) of the shareholder entry.If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Shareholder will be created with a procedurally-generated UUID.If, during an Account Holder create request, a UUID is provided, the creation of Account Holder will fail with a validation Error..If, during an Account Holder update request, a UUID that is not correlated with an existing Shareholder is provided, the update of the Shareholder will fail.If, during an Account Holder update request, a UUID that is correlated with an existing Shareholder is provided, the existing Shareholder will be updated.shareholderReferencestringYour reference for the shareholder entry.shareholderTypestringSpecifies how the person is associated with the account holder.Possible values:Owner: Individuals who directly or indirectly own 25% or more of a company.Controller: Individuals who are members of senior management staff responsible for managing a company or organization.webAddressstringThe URL of the person's website.signatoriesarray[object]Signatories associated with the company.
Each array entry should represent one signatory.Show childrenHide childrenaddressobjectThe address of the person.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.emailstringThe e-mail address of the person.fullPhoneNumberstringThe phone number of the person provided as a single string.  It will be handled as a landline phone.
Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"jobTitlestringJob title of the signatory.Example values:Chief Executive Officer,Chief Financial Officer,Chief Operating Officer,President,Vice President,Executive President,Managing Member,Partner,Treasurer,Director, orOther.nameobjectThe name of the person.Show childrenHide childrenfirstNamestringMax length:80The first name.genderstringMax length:1The gender.The following values are permitted:MALE,FEMALE,UNKNOWN.infixstringMax length:20The name's infix, if applicable.A maximum length of twenty (20) characters is imposed.lastNamestringMax length:80The last name.personalDataobjectContains information about the person.Show childrenHide childrendateOfBirthstringThe person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.documentDataarray[object]Array that contains information about the person's identification document. You can submit only one entry per document type.Show childrenHide childrenexpirationDatestringThe expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.issuerCountrystringMin length:2Max length:2The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.issuerStatestringThe state where the document was issued (if applicable).numberstringThe number in the document.typestringThe type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.To delete an existing entry for a documenttype, send only thetypefield in your request.nationalitystringMin length:2Max length:2The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.phoneNumberobjectThe phone number of the person.Show childrenHide childrenphoneCountryCodestringThe two-character country code of the phone number.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').phoneNumberstringThe phone number.The inclusion of the phone number country code is not necessary.phoneTypestringThe type of the phone number.The following values are permitted:Landline,Mobile,SIP,Fax.signatoryCodestringThe unique identifier (UUID) of the signatory.If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Signatory will be created with a procedurally-generated UUID.If, during an Account Holder create request, a UUID is provided, the creation of the Signatory will fail while the creation of the Account Holder will continue.If, during an Account Holder update request, a UUID that is not correlated with an existing Signatory is provided, the update of the Signatory will fail.If, during an Account Holder update request, a UUID that is correlated with an existing Signatory is provided, the existing Signatory will be updated.signatoryReferencestringYour reference for the signatory.webAddressstringThe URL of the person's website.stockExchangestringMarket Identifier Code (MIC).stockNumberstringInternational Securities Identification Number (ISIN).stockTickerstringStock Ticker symbol.taxIdstringThe tax ID of the company.emailstringThe e-mail address of the entity.fullPhoneNumberstringThe phone number of the contact provided as a single string.  It will be handled as a landline phone.Examples:"0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"individualDetailsobjectRequired when creating an entity withlegalEntityTypeIndividual.Show childrenHide childrennameobjectThe name of the individual.Make sure your account holder registers using the name shown on their Photo ID.
Maximum length: 80 characters
Cannot contain numbers. /n Cannot be empty.Show childrenHide childrenfirstNamestringMax length:80The first name.genderstringMax length:1The gender.The following values are permitted:MALE,FEMALE,UNKNOWN.infixstringMax length:20The name's infix, if applicable.A maximum length of twenty (20) characters is imposed.lastNamestringMax length:80The last name.personalDataobjectPersonal information of the individual.Show childrenHide childrendateOfBirthstringThe person's date of birth, in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.documentDataarray[object]Array that contains information about the person's identification document. You can submit only one entry per document type.Show childrenHide childrenexpirationDatestringThe expiry date of the document,
in ISO-8601 YYYY-MM-DD format. For example,2000-01-31.issuerCountrystringMin length:2Max length:2The country where the document was issued, in the two-characterISO 3166-1 alpha-2format. For example,NL.issuerStatestringThe state where the document was issued (if applicable).numberstringThe number in the document.typestringThe type of the document. Possible values:ID,DRIVINGLICENSE,PASSPORT,SOCIALSECURITY,VISA.To delete an existing entry for a documenttype, send only thetypefield in your request.nationalitystringMin length:2Max length:2The nationality of the person represented by a two-character country code,  inISO 3166-1 alpha-2format. For example,NL.legalArrangementEntityCodestringAdyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement entity.
Use only when updating an account holder. If you include this field when creating an account holder, the request will fail.legalArrangementEntityReferencestringYour reference for the legal arrangement entity.legalArrangementMembersarray[string]An array containing the roles of the entity in the legal arrangement.The possible values depend on the legal arrangementtype.FortypeAssociation:ControllingPersonandShareholder.FortypePartnership:PartnerandShareholder.FortypeTrust:Trustee,Settlor,Protector,Beneficiary,  andShareholder.legalEntityTypestringThe legal entity type.Possible values:Business,Individual,NonProfit,PublicCompany, orPartnership.phoneNumberobjectThe phone number of the entity.Show childrenHide childrenphoneCountryCodestringThe two-character country code of the phone number.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').phoneNumberstringThe phone number.The inclusion of the phone number country code is not necessary.phoneTypestringThe type of the phone number.The following values are permitted:Landline,Mobile,SIP,Fax.webAddressstringThe URL of the website of the contact.legalArrangementReferencestringYour reference for the legal arrangement. Must be between 3 to 128 characters.legalFormstringThe form of legal arrangement. Required iftypeisTrustorPartnership.The possible values depend on thetype.FortypeTrust:CashManagementTrust,CorporateUnitTrust,DeceasedEstate,DiscretionaryInvestmentTrust,DiscretionaryServicesManagementTrust,DiscretionaryTradingTrust,FirstHomeSaverAccountsTrust,FixedTrust,FixedUnitTrust,HybridTrust,ListedPublicUnitTrust,OtherTrust,PooledSuperannuationTrust,PublicTradingTrust, orUnlistedPublicUnitTrust.FortypePartnership:LimitedPartnership,FamilyPartnership, orOtherPartnershipnamestringThe legal name of the legal arrangement. Minimum length: 3 characters.registrationNumberstringThe registration number of the legal arrangement.taxNumberstringThe tax identification number of the legal arrangement.typestringThetype of legal arrangement.Possible values:AssociationPartnershipSoleProprietorshipTrustmerchantCategoryCodestringThe Merchant Category Code of the account holder.If not specified in the request, this will be derived from the platform account (which is configured by Adyen).metadataobjectA set of key and value pairs for general use by the account holder or merchant.
The keys do not have specific names and may be used for storing miscellaneous data as desired.The values being stored have a maximum length of eighty (80) characters and will be truncated if necessary.
Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs.payoutMethodsarray[object]Array of tokenized card details associated with the account holder. For details about how you can use the tokens to pay out, refer toPay out to cards.Show childrenHide childrenmerchantAccountstringThemerchantAccountyou used in the/paymentsrequest when yousaved the account holder's card details.payoutMethodCodestringAdyen-generated unique alphanumeric identifier (UUID) for the payout method, returned in the response when you create a payout method. Required when updating an existing payout method in an/updateAccountHolderrequest.payoutMethodReferencestringYour reference for the payout method.recurringDetailReferencestringTherecurringDetailReferencereturned in the/paymentsresponse when yousaved the account holder's card details.shopperReferencestringTheshopperReferenceyou sent in the/paymentsrequest when yousaved the account holder's card details.phoneNumberobjectThe phone number of the account holder.Required if afullPhoneNumberis not provided.Show childrenHide childrenphoneCountryCodestringThe two-character country code of the phone number.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').phoneNumberstringThe phone number.The inclusion of the phone number country code is not necessary.phoneTypestringThe type of the phone number.The following values are permitted:Landline,Mobile,SIP,Fax.principalBusinessAddressobjectThe principal business address of the account holder.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.storeDetailsarray[object]Array of stores associated with the account holder. Required when onboarding account holders that have an Adyenpoint of sale.Show childrenHide childrenaddressobjectThe address of the physical store where the account holder will process payments from.Show childrenHide childrencitystringThe name of the city. Required if thehouseNumberOrName,street,postalCode, orstateOrProvinceare provided.countrystringThe two-character country code of the address in ISO-3166-1 alpha-2 format. For example,NL.houseNumberOrNamestringThe number or name of the house.postalCodestringThe postal code. Required if thehouseNumberOrName,street,city, orstateOrProvinceare provided.Maximum length:5 digits for addresses in the US.10 characters for all other countries.stateOrProvincestringThe abbreviation of the state or province. Required if thehouseNumberOrName,street,city, orpostalCodeare provided.Maximum length:2 characters for addresses in the US or Canada.3 characters for all other countries.streetstringThe name of the street. Required if thehouseNumberOrName,city,postalCode, orstateOrProvinceare provided.fullPhoneNumberstringThe phone number of the store provided as a single string.  It will be handled as a landline phone.Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"logostringStore logo for payment method setup.merchantAccountstringThe merchant account to which the store belongs.merchantCategoryCodestringThe merchant category code (MCC) that classifies the business of the account holder.merchantHouseNumberstringMerchant house number for payment method setup.phoneNumberobjectThe phone number of the store.Show childrenHide childrenphoneCountryCodestringThe two-character country code of the phone number.The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').phoneNumberstringThe phone number.The inclusion of the phone number country code is not necessary.phoneTypestringThe type of the phone number.The following values are permitted:Landline,Mobile,SIP,Fax.shopperInteractionstringThe sales channel. Possible values:Ecommerce,POS.splitConfigurationUUIDstringThe unique reference for the split configuration, returned when you configure splits in your Customer Area. When this is provided, thevirtualAccountis also required. Adyen uses the configuration and thevirtualAccountto split funds between accounts in your platform.statusstringThe status of the store. Possible values:Pending,Active,Inactive,InactiveWithModifications,Closed.storestringAdyen-generated unique alphanumeric identifier (UUID) for the store, returned in the response when you create a store. Required when updating an existing store in an/updateAccountHolderrequest.storeNamestringThe name of the account holder's store. This value is shown in shopper statements.Length: Between 3 to 22 charactersThe following characters arenotsupported::;}{$#@!|<>%^*+=\Note:storeName does not appear in American Express shopper statements by default. Contact Adyen Support to enable this for American Express.storeReferencestringYour unique identifier for the store. The Customer Area also uses this value for the store description.Length: Between 3 to 128 charactersThe following characters arenotsupported::;}{$#@!|<>%^*+=\virtualAccountstringThe account holder'saccountCodewhere the split amount will be sent. Required when you provide thesplitConfigurationUUID.webAddressstringURL of the ecommerce store.webAddressstringThe URL of the website of the account holder.accountHolderStatusobjectThe status of the new account holder.Show childrenHide childreneventsarray[object]A list of events scheduled for the account holder.Show childrenHide childreneventstringThe event.Permitted values:InactivateAccount,RefundNotPaidOutTransfers.
For more information, refer toVerification checks.executionDatestringThe date on which the event will take place.reasonstringThe reason why this event has been created.payoutStateobjectThe payout state of the account holder.Show childrenHide childrenallowPayoutbooleanIndicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payouts will be permitted for any of the account holder's accounts. If this field is true, payouts will be permitted for any of the account holder's accounts.disableReasonstringThe reason why payouts (to all of the account holder's accounts) have been disabled (by the platform). If thedisabledfield is true, this field can be used to explain why.disabledbooleanIndicates whether payouts have been disabled (by the platform) for all of the account holder's accounts. A platform may enable and disable this field at their discretion. If this field is true,allowPayoutwill be false and no payouts will be permitted for any of the account holder's accounts. If this field is false,allowPayoutmay or may not be enabled, depending on other factors.notAllowedReasonstringThe reason why payouts (to all of the account holder's accounts) have been disabled (by Adyen). If payouts have been disabled by Adyen, this field will explain why. If this field is blank, payouts have not been disabled by Adyen.payoutLimitobjectThe maximum amount that payouts are limited to. Only applies if payouts are allowed but limited.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency code.valueintegerThe amount of the transaction, inminor units.tierNumberintegerThe payout tier that the account holder occupies.processingStateobjectThe processing state of the account holder.Show childrenHide childrendisableReasonstringThe reason why processing has been disabled.disabledbooleanIndicates whether the processing of payments is allowed.processedFromobjectThe lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money in order to be placed into this tier).Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency code.valueintegerThe amount of the transaction, inminor units.processedToobjectThe upper bound of the processing tier (i.e., an account holder must have processed less than this amount of money in order to be placed into this tier).Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency code.valueintegerThe amount of the transaction, inminor units.tierNumberintegerThe processing tier that the account holder occupies.statusstringThe status of the account holder.Permitted values:Active,Inactive,Suspended,Closed.statusReasonstringThe reason why the status was assigned to the account holder.descriptionstringThe description of the new account holder.invalidFieldsarray[object]A list of fields that caused the/createAccountHolderrequest to fail.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.legalEntitystringThe type of legal entity of the new account holder.primaryCurrencystringDeprecatedThe three-characterISO currency code, with which the prospective account holder primarily deals.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.verificationobjectThe details of KYC Verification of the account holder.Show childrenHide childrenaccountHolderobjectThe results of the checks on the account holder.Show childrenHide childrenchecksarray[object]A list of the checks and their statuses.Show childrenHide childrenrequiredFieldsarray[string]A list of the fields required for execution of the check.statusstringThe status of the check.Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.summaryobjectA summary of the execution of the check.Show childrenHide childrenkycCheckCodeintegerThe code of the check. For possible values, refer toVerification codes.kycCheckDescriptionstringA description of the check.typestringThe type of check.Possible values:BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.COMPANY_VERIFICATIONCARD_VERIFICATIONIDENTITY_VERIFICATIONLEGAL_ARRANGEMENT_VERIFICATIONNONPROFIT_VERIFICATIONPASSPORT_VERIFICATIONPAYOUT_METHOD_VERIFICATION: Used in v6 and later.PCI_VERIFICATIONlegalArrangementsarray[object]The results of the checks on the legal arrangements.Show childrenHide childrenchecksarray[object]A list of the checks and their statuses.Show childrenHide childrenrequiredFieldsarray[string]A list of the fields required for execution of the check.statusstringThe status of the check.Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.summaryobjectA summary of the execution of the check.Show childrenHide childrenkycCheckCodeintegerThe code of the check. For possible values, refer toVerification codes.kycCheckDescriptionstringA description of the check.typestringThe type of check.Possible values:BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.COMPANY_VERIFICATIONCARD_VERIFICATIONIDENTITY_VERIFICATIONLEGAL_ARRANGEMENT_VERIFICATIONNONPROFIT_VERIFICATIONPASSPORT_VERIFICATIONPAYOUT_METHOD_VERIFICATION: Used in v6 and later.PCI_VERIFICATIONlegalArrangementCodestringThe unique ID of the legal arrangement to which the check applies.legalArrangementsEntitiesarray[object]The results of the checks on the legal arrangement entities.Show childrenHide childrenchecksarray[object]A list of the checks and their statuses.Show childrenHide childrenrequiredFieldsarray[string]A list of the fields required for execution of the check.statusstringThe status of the check.Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.summaryobjectA summary of the execution of the check.Show childrenHide childrenkycCheckCodeintegerThe code of the check. For possible values, refer toVerification codes.kycCheckDescriptionstringA description of the check.typestringThe type of check.Possible values:BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.COMPANY_VERIFICATIONCARD_VERIFICATIONIDENTITY_VERIFICATIONLEGAL_ARRANGEMENT_VERIFICATIONNONPROFIT_VERIFICATIONPASSPORT_VERIFICATIONPAYOUT_METHOD_VERIFICATION: Used in v6 and later.PCI_VERIFICATIONlegalArrangementCodestringThe unique ID of the legal arrangement to which the entity belongs.legalArrangementEntityCodestringThe unique ID of the legal arrangement entity to which the check applies.payoutMethodsarray[object]The results of the checks on the payout methods.Show childrenHide childrenchecksarray[object]A list of the checks and their statuses.Show childrenHide childrenrequiredFieldsarray[string]A list of the fields required for execution of the check.statusstringThe status of the check.Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.summaryobjectA summary of the execution of the check.Show childrenHide childrenkycCheckCodeintegerThe code of the check. For possible values, refer toVerification codes.kycCheckDescriptionstringA description of the check.typestringThe type of check.Possible values:BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.COMPANY_VERIFICATIONCARD_VERIFICATIONIDENTITY_VERIFICATIONLEGAL_ARRANGEMENT_VERIFICATIONNONPROFIT_VERIFICATIONPASSPORT_VERIFICATIONPAYOUT_METHOD_VERIFICATION: Used in v6 and later.PCI_VERIFICATIONpayoutMethodCodestringThe unique ID of the payoput method to which the check applies.shareholdersarray[object]The results of the checks on the shareholders.Show childrenHide childrenchecksarray[object]A list of the checks and their statuses.Show childrenHide childrenrequiredFieldsarray[string]A list of the fields required for execution of the check.statusstringThe status of the check.Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.summaryobjectA summary of the execution of the check.Show childrenHide childrenkycCheckCodeintegerThe code of the check. For possible values, refer toVerification codes.kycCheckDescriptionstringA description of the check.typestringThe type of check.Possible values:BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.COMPANY_VERIFICATIONCARD_VERIFICATIONIDENTITY_VERIFICATIONLEGAL_ARRANGEMENT_VERIFICATIONNONPROFIT_VERIFICATIONPASSPORT_VERIFICATIONPAYOUT_METHOD_VERIFICATION: Used in v6 and later.PCI_VERIFICATIONlegalArrangementCodestringThe unique ID of the legal arrangement to which the shareholder belongs, if applicable.legalArrangementEntityCodestringThe unique ID of the legal arrangement entity to which the shareholder belongs, if applicable.shareholderCodestringThe code of the shareholder to which the check applies.signatoriesarray[object]The results of the checks on the signatories.Show childrenHide childrenchecksarray[object]A list of the checks and their statuses.Show childrenHide childrenrequiredFieldsarray[string]A list of the fields required for execution of the check.statusstringThe status of the check.Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.summaryobjectA summary of the execution of the check.Show childrenHide childrenkycCheckCodeintegerThe code of the check. For possible values, refer toVerification codes.kycCheckDescriptionstringA description of the check.typestringThe type of check.Possible values:BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.COMPANY_VERIFICATIONCARD_VERIFICATIONIDENTITY_VERIFICATIONLEGAL_ARRANGEMENT_VERIFICATIONNONPROFIT_VERIFICATIONPASSPORT_VERIFICATIONPAYOUT_METHOD_VERIFICATION: Used in v6 and later.PCI_VERIFICATIONsignatoryCodestringThe code of the signatory to which the check applies.ultimateParentCompanyarray[object]The result of the check on the Ultimate Parent Company.Show childrenHide childrenchecksarray[object]A list of the checks and their statuses.Show childrenHide childrenrequiredFieldsarray[string]A list of the fields required for execution of the check.statusstringThe status of the check.Possible values:AWAITING_DATA,DATA_PROVIDED,FAILED,INVALID_DATA,PASSED,PENDING,RETRY_LIMIT_REACHED.summaryobjectA summary of the execution of the check.Show childrenHide childrenkycCheckCodeintegerThe code of the check. For possible values, refer toVerification codes.kycCheckDescriptionstringA description of the check.typestringThe type of check.Possible values:BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.COMPANY_VERIFICATIONCARD_VERIFICATIONIDENTITY_VERIFICATIONLEGAL_ARRANGEMENT_VERIFICATIONNONPROFIT_VERIFICATIONPASSPORT_VERIFICATIONPAYOUT_METHOD_VERIFICATION: Used in v6 and later.PCI_VERIFICATIONultimateParentCompanyCodestringThe code of the Ultimate Parent Company to which the check applies.verificationProfilestringThe identifier of the profile that applies to this entity.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- United States - Routing number
- United Kingdom - Sort code
- Germany - Bankleitzahl
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- Owner: Individuals who directly or indirectly own 25% or more of a company.
- Controller: Individuals who are members of senior management staff responsible for managing a company or organization.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- Owner: Individuals who directly or indirectly own 25% or more of a company.
- Controller: Individuals who are members of senior management staff responsible for managing a company or organization.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- FortypeAssociation:ControllingPersonandShareholder.
- FortypePartnership:PartnerandShareholder.
- FortypeTrust:Trustee,Settlor,Protector,Beneficiary,  andShareholder.
- FortypeTrust:CashManagementTrust,CorporateUnitTrust,DeceasedEstate,DiscretionaryInvestmentTrust,DiscretionaryServicesManagementTrust,DiscretionaryTradingTrust,FirstHomeSaverAccountsTrust,FixedTrust,FixedUnitTrust,HybridTrust,ListedPublicUnitTrust,OtherTrust,PooledSuperannuationTrust,PublicTradingTrust, orUnlistedPublicUnitTrust.
- FortypePartnership:LimitedPartnership,FamilyPartnership, orOtherPartnership
- Association
- Partnership
- SoleProprietorship
- Trust

```
merchantAccount
```

```
recurringDetailReference
```

```
shopperReference
```
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- 5 digits for addresses in the US.
- 10 characters for all other countries.
- 2 characters for addresses in the US or Canada.
- 3 characters for all other countries.
- Length: Between 3 to 22 characters
- The following characters arenotsupported::;}{$#@!|<>%^*+=\
- Length: Between 3 to 128 characters
- The following characters arenotsupported::;}{$#@!|<>%^*+=\
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION
- BANK_ACCOUNT_VERIFICATION: Used in v5 and earlier. Replaced byPAYOUT_METHOD_VERIFICATIONin v6 and later.
- COMPANY_VERIFICATION
- CARD_VERIFICATION
- IDENTITY_VERIFICATION
- LEGAL_ARRANGEMENT_VERIFICATION
- NONPROFIT_VERIFICATION
- PASSPORT_VERIFICATION
- PAYOUT_METHOD_VERIFICATION: Used in v6 and later.
- PCI_VERIFICATION

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error