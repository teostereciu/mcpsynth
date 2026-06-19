# legalentity/4/patch/legalEntities/(id)

*Source: https://docs.adyen.com/api-explorer/legalentity/4/patch/legalEntities/(id)*

---

# Update a legal entity
Updates a legal entity.
To change the legal entity type, include only the newtypein your request.
If you need to update information for the legal entity, make a separate request. To update theentityAssociationsarray, you need to replace the entire array.For example, if the array has 3 entries and you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.
Requests to this endpoint are subject to rate limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.
Use the requested verification code 0_0001 to resolve any suberrors associated with the legal entity. Requested verification codes can only be used in your test environment.
The unique identifier of the legal entity.
Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example,issueCardfor Issuing. The value is an object containing the settings for the capability.
List of legal entities associated with the current legal entity.
For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories.
The individual's job title if thetypeisuboThroughControlorsignatory.
The unique identifier of the associatedlegal entity.
Default value:falseSet totrueif the entity associationtypedirector,secondaryPartnerorshareholderis also a nominee. Only applicable to New Zealand.
The individual's relationship to a legal representative if thetypeislegalRepresentative. Possible values:parent,guardian.
Defines the KYC exemption reason for a settlor associated with a trust. Only applicable to trusts in Australia.
For example,professionalServiceProvider,deceased, orcontributionBelowThreshold.
Defines the relationship of the legal entity to the current legal entity.
Possible value for individuals:legalRepresentative.
Possible values for organizations:director,signatory,trustOwnership,uboThroughOwnership,uboThroughControl, orultimateParentCompany.
Possible values for sole proprietorships:soleProprietorship.
Possible value for trusts:trust.
Possible values for trust members:definedBeneficiary,protector,secondaryTrustee,settlor,uboThroughControl, oruboThroughOwnership.
Possible value for unincorporated partnership:unincorporatedPartnership.
Possible values for unincorporated partnership members:secondaryPartner,uboThroughControl,uboThroughOwnership
Information about the individual. Required iftypeisindividual.
The individual's birth information.
The individual's date of birth, in YYYY-MM-DD format.
The email address of the legal entity.
Information about the individual's identification document.
The card number of the document that was issued (AU only).
The expiry date of the document, in YYYY-MM-DD format.
The two-characterISO 3166-1 alpha-2country code where the document was issued. For example,US.
The state or province where the document was issued (AU only).
Applies only to individuals in the US. Set totrueif the individual does not have an SSN. To verify their identity, Adyen will require them to upload an ID document.
The number in the document.
Type of identity data. For individuals, the following types are supported. See ouronboarding guidefor other supported countries.
- Australia:driversLicense,passport
- Hong Kong:driversLicense,nationalIdNumber,passport
- New Zealand:driversLicense,passport
- Singapore:driversLicense,nationalIdNumber,passport
- All other supported countries:nationalIdNumber
The individual's name.
The individual's first name. Must not be blank.
The infix in the individual's name, if any.
The individual's last name. Must not be blank.
The individual's nationality.
The phone number of the legal entity.
The full phone number, including the country code. For example,+3112345678.
The type of phone number.
Possible values:mobile,landline,sip,fax.
The residential address of the individual.
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
Support information for the legal entity. Required if you have a platform setup.
The support email address of the legal entity. Required if you have a platform setup.
The support phone number of the legal entity. Required if you have a platform setup.
The full phone number, including the country code. For example,+3112345678.
The type of phone number.
Possible values:mobile,landline,sip,fax.
The tax information of the individual.
The two-letterISO 3166-1 alpha-2country code.
The tax ID number (TIN) of the organization or individual.
Set this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.
The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.
The website and app URL of the legal entity.
The URL of the website or the app store URL.
Information about the organization. Required iftypeisorganization.
The two-characterISO 3166-1 alpha-2country code of the governing country.
The date when the organization was incorporated in YYYY-MM-DD format.
Required if the value ofstatusOfLegalProceedingis one of the following:
underJudicialAdministration,bankruptcyInsolvency,otherLegalMeasures
The date at which a legal proceeding was initiated, inYYYY-MM-DDformat. Example:2000-02-12
Your description for the organization.
The organization's trading name, if different from the registered legal name.
Set this totrueif the organization or legal arrangement does not have aDoing business asname.
The sector of the economy the legal entity operates within, represented by a 2-4 digit code that may include a ".". Example: 45.11
You can locate economic sector codes for your area by referencing codes defined by the NACE (Nomenclature of Economic Activities) used in the European Union.
The email address of the legal entity.
The financial report information of the organization.
The annual turnover of the business.
The balance sheet total of the business.
The currency used for the annual turnover, balance sheet total, and net assets.
The date the financial data were provided, in YYYY-MM-DD format.
The number of employees of the business.
The net assets of the business.
The global legal entity identifier for the organization.
Indicates that the registered business address is also the company's headquarters.
The institutional sector the organization operates within.
The type of business entity as defined in the national legal system. Use a legal form listed within the accepted legal forms compiled by the Central Bank of Europe.
The organization's legal name.
The phone number of the legal entity.
The full phone number, including the country code. For example,+3112345678.
The type of phone number.
Possible values:mobile,landline,sip,fax.
The address where the organization operates from. Provide this if the principal place of business is different from theregisteredAddress.
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
The address of the organization registered at their registrar (such as the Chamber of Commerce).
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
The organization's registration number.
Set this totrueif the organization does not have a registration number available. Only applicable for organizations in New Zealand, and incorporated partnerships and government organizations in Australia.
The status of any current or past legal action taken against the legal entity.
Possible values:noLegalActionsTaken,underJudicialAdministration,bankruptcyInsolvency,otherLegalMeasures
If the value of this field isnoLegalActionsTaken, thendateOfInitiationOfLegalProceedingis not required. Otherwise, it is required.
Information about the organization's publicly traded stock. Provide this object only iftypeislistedPublicCompany.
The four-digitMarket Identifier Codeof the stock market where the organization's stocks are traded.
The 12-digit International Securities Identification Number (ISIN) of the company, without dashes (-).
The stock ticker symbol.
Support information for the legal entity. Required if you have a platform setup.
The support email address of the legal entity. Required if you have a platform setup.
The support phone number of the legal entity. Required if you have a platform setup.
The full phone number, including the country code. For example,+3112345678.
The type of phone number.
Possible values:mobile,landline,sip,fax.
The tax information of the organization.
The two-letterISO 3166-1 alpha-2country code.
The tax ID number (TIN) of the organization or individual.
Set this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.
The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.
The tax reporting classification (FATCA/CRS self-certification) of the organization.
The organization's business type.
Possible values:other,listedPublicCompany,subsidiaryOfListedPublicCompany,governmentalOrganization,internationalOrganization,financialInstitution.
The Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a US financial institution and thebusinessTypeisfinancialInstitution.
The organization's main source of income. Only required ifbusinessTypeisother.
Possible values:businessOperation,realEstateSales,investmentInterestOrRoyalty,propertyRental,other.
The tax reporting classification type.
Possible values:nonFinancialNonReportable,financialNonReportable,nonFinancialActive,nonFinancialPassive.
Type of organization.
Possible values:associationIncorporated,governmentalOrganization,listedPublicCompany,nonProfit,partnershipIncorporated,privateCompany.
The reason the organization has not provided a VAT number.
Possible values:industryExemption,belowTaxThreshold.
The organization's VAT number.
The website and app URL of the legal entity.
The URL of the website or the app store URL.
Your reference for the legal entity, maximum 150 characters.
Information about the sole proprietorship. Required iftypeissoleProprietorship.
The two-characterISO 3166-1 alpha-2country code of the governing country.
The date when the legal arrangement was incorporated in YYYY-MM-DD format.
The registered name, if different from thename.
Set this totrueif the legal arrangement does not have aDoing business asname.
The information from the financial report of the sole proprietorship.
The annual turnover of the business.
The balance sheet total of the business.
The currency used for the annual turnover, balance sheet total, and net assets.
The date the financial data were provided, in YYYY-MM-DD format.
The number of employees of the business.
The net assets of the business.
The legal name.
The business address. Required if the principal place of business is different from theregisteredAddress.
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
The address registered at the registrar, such as the Chamber of Commerce.
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
The registration number.
The tax information is absent.
The tax information of the entity.
The two-letterISO 3166-1 alpha-2country code.
The tax ID number (TIN) of the organization or individual.
Set this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.
The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.
The reason for not providing a VAT number.
Possible values:industryExemption,belowTaxThreshold.
The VAT number.
Information about the trust. Required iftypeistrust.
The two-characterISO 3166-1 alpha-2country code of the governing country.
The date when the legal arrangement was incorporated in YYYY-MM-DD format.
A short description about the trust. Only applicable for charitable trusts in New Zealand.
The registered name, if different from thename.
Set this totrueif the legal arrangement does not have aDoing business asname.
The legal name.
The business address. Required if the principal place of business is different from theregisteredAddress.
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
The address registered at the registrar, such as the Chamber of Commerce.
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
The registration number.
The tax information of the entity.
The two-letterISO 3166-1 alpha-2country code.
The tax ID number (TIN) of the organization or individual.
Set this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.
The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.
Type of trust.
See possible values for trusts inAustraliaandNew Zealand.
The undefined beneficiary information of the entity.
The details of the undefined beneficiary.
The reason for not providing a VAT number.
Possible values:industryExemption,belowTaxThreshold.
The VAT number.
The type of legal entity.
Possible values:individual,organization,soleProprietorship, ortrust.
Information about the unincorporated partnership. Required iftypeisunincorporatedPartnership.
The two-characterISO 3166-1 alpha-2country code of the governing country.
The date when the legal arrangement was incorporated in YYYY-MM-DD format.
Short description about the Legal Arrangement.
The registered name, if different from thename.
Set this totrueif the legal arrangement does not have aDoing business asname.
The legal name.
The business address. Required if the principal place of business is different from theregisteredAddress.
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
The address registered at the registrar, such as the Chamber of Commerce.
The name of the city. Required ifstateOrProvinceis provided.
If you specify the city, you must also sendpostalCodeandstreet.
The two-letterISO 3166-1 alpha-2country code.
The postal code. Required ifstateOrProvinceand/orcityis provided.
When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.
The two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.
If you specify the state or province, you must also sendcity,postalCode, andstreet.
The name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.
The apartment, unit, or suite number.
The registration number.
The tax information of the entity.
The two-letterISO 3166-1 alpha-2country code.
The tax ID number (TIN) of the organization or individual.
Set this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.
The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.
The reason for not providing a VAT number.
Possible values:industryExemption,belowTaxThreshold.
The VAT number.
A key-value pair that specifies the verification process for a legal entity. Set toupfrontfor upfront verification formarketplaces.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesscapabilitiesobjectContains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example,issueCardfor Issuing. The value is an object containing the settings for the capability.Show childrenHide childrenallowedbooleanIndicates whether the capability is allowed. Adyen sets this totrueif the verification is successful.allowedLevelstringThe capability level that is allowed for the legal entity.Possible values:notApplicable,low,medium,high.allowedSettingsobjectThe settings that are allowed for the legal entity.Show childrenHide childrenamountPerIndustryobjectThe maximum amount a card holder can spend per industry.Show childrenHide childrencurrencystringThe type of currency. Must be EUR (or EUR equivalent)valueintegerTotal value of amount. Must be >= 0authorizedCardUsersbooleanThe number of card holders who can use the card.fundingSourcearray[string]The funding source of the card, for exampledebit.intervalstringThe period when the rule conditions apply.maxAmountobjectThe maximum amount a card holder can withdraw per day.Show childrenHide childrencurrencystringThe type of currency. Must be EUR (or EUR equivalent)valueintegerTotal value of amount. Must be >= 0requestedbooleanIndicates whether the capability is requested. To check whether the legal entity is permitted to use the capability, refer to theallowedfield.requestedLevelstringThe requested level of the capability. Some capabilities, such as those used incard issuing, have different levels. Levels increase the capability, but also require additional checks and increased monitoring.Possible values:notApplicable,low,medium,high.requestedSettingsobjectThe settings that are requested for the legal entity.Show childrenHide childrenamountPerIndustryobjectThe maximum amount a card holder can spend per industry.Show childrenHide childrencurrencystringThe type of currency. Must be EUR (or EUR equivalent)valueintegerTotal value of amount. Must be >= 0authorizedCardUsersbooleanThe number of card holders who can use the card.fundingSourcearray[string]The funding source of the card, for exampledebit.intervalstringThe period when the rule conditions apply.maxAmountobjectThe maximum amount a card holder can withdraw per day.Show childrenHide childrencurrencystringThe type of currency. Must be EUR (or EUR equivalent)valueintegerTotal value of amount. Must be >= 0transferInstrumentsarray[object]The capability status of transfer instruments associated with the legal entity.Show childrenHide childrenallowedbooleanIndicates whether the capability is allowed for the supporting entity.If a capability is allowed for a supporting entity but not for the parent legal entity, this means the legal entity has other supporting entities that failed verification.You can use the allowed supporting entityregardless of the verification status of other supporting entities.idstringSupporting entity referencerequestedbooleanIndicates whether the supporting entity capability is requested.verificationStatusstringThe status of the verification checks for the capability of the supporting entity.Possible values:pending: Adyen is running the verification.invalid: The verification failed. Check if theerrorsarray contains more information.valid: The verification has been successfully completed.rejected: Adyen has verified the information, but found reasons to not allow the capability.verificationStatusstringThe status of the verification checks for the capability.Possible values:pending: Adyen is running the verification.invalid: The verification failed. Check if theerrorsarray contains more information.valid: The verification has been successfully completed.rejected: Adyen has verified the information, but found reasons to not allow the capability.documentDetailsarray[object]List of documents uploaded for the legal entity.Show childrenHide childrenactivebooleanIdentifies whether the document is active and used for checks.descriptionstringYour description for the document.fileNamestringDocument name.idstringThe unique identifier of the resource.modificationDatestringThe modification date of the document.pagesarray[object]List of document pagesShow childrenHide childrenpageNamestringpageNumberintegertypestringtypestringType of document, used when providing an ID number or uploading a document.documentsarray[object]Deprecated in version 1Use thedocumentDetailsarray instead.List of documents uploaded for the legal entity.Show childrenHide childrenidstringThe unique identifier of the resource.entityAssociationsarray[object]List of legal entities associated with the current legal entity.
For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories.Show childrenHide childrenassociatorIdstringThe unique identifier of another legal entity with which thelegalEntityIdis associated. When thelegalEntityIdis associated to legal entities other than the current one, the response returns all the associations.entityTypestringThe legal entity type of associated legal entity.For example,organization,soleProprietorshiporindividual.jobTitlestringThe individual's job title if thetypeisuboThroughControlorsignatory.legalEntityIdstringThe unique identifier of the associatedlegal entity.namestringThe name of the associatedlegal entity.Forindividual,name.firstNameandname.lastName.Fororganization,legalName.ForsoleProprietorship,name.nomineebooleanDefault value:falseSet totrueif the entity associationtypedirector,secondaryPartnerorshareholderis also a nominee. Only applicable to New Zealand.relationshipstringThe individual's relationship to a legal representative if thetypeislegalRepresentative. Possible values:parent,guardian.settlorExemptionReasonarray[string]Defines the KYC exemption reason for a settlor associated with a trust. Only applicable to trusts in Australia.For example,professionalServiceProvider,deceased, orcontributionBelowThreshold.typestringDefines the relationship of the legal entity to the current legal entity.Possible value for individuals:legalRepresentative.Possible values for organizations:director,signatory,trustOwnership,uboThroughOwnership,uboThroughControl, orultimateParentCompany.Possible values for sole proprietorships:soleProprietorship.Possible value for trusts:trust.Possible values for trust members:definedBeneficiary,protector,secondaryTrustee,settlor,uboThroughControl, oruboThroughOwnership.Possible value for unincorporated partnership:unincorporatedPartnership.Possible values for unincorporated partnership members:secondaryPartner,uboThroughControl,uboThroughOwnershipidstringThe unique identifier of the legal entity.individualobjectInformation about the individual. Required iftypeisindividual.Show childrenHide childrenbirthDataobjectThe individual's birth information.Show childrenHide childrendateOfBirthstringThe individual's date of birth, in YYYY-MM-DD format.emailstringThe email address of the legal entity.identificationDataobjectInformation about the individual's identification document.Show childrenHide childrencardNumberstringThe card number of the document that was issued (AU only).expiryDatestringThe expiry date of the document, in YYYY-MM-DD format.issuerCountrystringDeprecated in version 1The two-characterISO 3166-1 alpha-2country code where the document was issued. For example,US.issuerStatestringThe state or province where the document was issued (AU only).nationalIdExemptbooleanApplies only to individuals in the US. Set totrueif the individual does not have an SSN. To verify their identity, Adyen will require them to upload an ID document.numberstringThe number in the document.typestringType of identity data. For individuals, the following types are supported. See ouronboarding guidefor other supported countries.Australia:driversLicense,passportHong Kong:driversLicense,nationalIdNumber,passportNew Zealand:driversLicense,passportSingapore:driversLicense,nationalIdNumber,passportAll other supported countries:nationalIdNumbernameobjectThe individual's name.Show childrenHide childrenfirstNamestringThe individual's first name. Must not be blank.infixstringThe infix in the individual's name, if any.lastNamestringThe individual's last name. Must not be blank.nationalitystringThe individual's nationality.phoneobjectThe phone number of the legal entity.Show childrenHide childrennumberstringThe full phone number, including the country code. For example,+3112345678.phoneCountryCodestringThe two-letterISO 3166-1 alpha-2country code prefix of the phone number. For example,USorNL.The value of thephoneCountryCodeis determined by the country code digit(s) ofphone.numbertypestringThe type of phone number.
Possible values:mobile,landline,sip,fax.residentialAddressobjectThe residential address of the individual.Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.supportobjectSupport information for the legal entity. Required if you have a platform setup.Show childrenHide childrenemailstringThe support email address of the legal entity. Required if you have a platform setup.phoneobjectThe support phone number of the legal entity. Required if you have a platform setup.Show childrenHide childrennumberstringThe full phone number, including the country code. For example,+3112345678.phoneCountryCodestringThe two-letterISO 3166-1 alpha-2country code prefix of the phone number. For example,USorNL.The value of thephoneCountryCodeis determined by the country code digit(s) ofphone.numbertypestringThe type of phone number.
Possible values:mobile,landline,sip,fax.taxInformationarray[object]The tax information of the individual.Show childrenHide childrencountrystringMin length:2Max length:2The two-letterISO 3166-1 alpha-2country code.numberstringThe tax ID number (TIN) of the organization or individual.numberAbsentbooleanSet this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.typestringThe TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.webDataobjectDeprecated in version 1The website and app URL of the legal entity.Show childrenHide childrenwebAddressstringThe URL of the website or the app store URL.webAddressIdstringThe unique identifier of the web address.organizationobjectInformation about the organization. Required iftypeisorganization.Show childrenHide childrencountryOfGoverningLawstringThe two-characterISO 3166-1 alpha-2country code of the governing country.dateOfIncorporationstringThe date when the organization was incorporated in YYYY-MM-DD format.dateOfInitiationOfLegalProceedingstringRequired if the value ofstatusOfLegalProceedingis one of the following:underJudicialAdministration,bankruptcyInsolvency,otherLegalMeasuresThe date at which a legal proceeding was initiated, inYYYY-MM-DDformat. Example:2000-02-12descriptionstringYour description for the organization.doingBusinessAsstringThe organization's trading name, if different from the registered legal name.doingBusinessAsAbsentbooleanSet this totrueif the organization or legal arrangement does not have aDoing business asname.economicSectorstringThe sector of the economy the legal entity operates within, represented by a 2-4 digit code that may include a ".". Example: 45.11You can locate economic sector codes for your area by referencing codes defined by the NACE (Nomenclature of Economic Activities) used in the European Union.emailstringThe email address of the legal entity.financialReportsarray[object]The financial report information of the organization.Show childrenHide childrenannualTurnoverstringThe annual turnover of the business.balanceSheetTotalstringThe balance sheet total of the business.currencyOfFinancialDatastringThe currency used for the annual turnover, balance sheet total, and net assets.dateOfFinancialDatastringThe date the financial data were provided, in YYYY-MM-DD format.employeeCountstringThe number of employees of the business.netAssetsstringThe net assets of the business.globalLegalEntityIdentifierstringThe global legal entity identifier for the organization.headOfficeIndicatorbooleanIndicates that the registered business address is also the company's headquarters.institutionalSectorstringThe institutional sector the organization operates within.legalFormstringThe type of business entity as defined in the national legal system. Use a legal form listed within the accepted legal forms compiled by the Central Bank of Europe.legalNamestringThe organization's legal name.phoneobjectThe phone number of the legal entity.Show childrenHide childrennumberstringThe full phone number, including the country code. For example,+3112345678.phoneCountryCodestringThe two-letterISO 3166-1 alpha-2country code prefix of the phone number. For example,USorNL.The value of thephoneCountryCodeis determined by the country code digit(s) ofphone.numbertypestringThe type of phone number.
Possible values:mobile,landline,sip,fax.principalPlaceOfBusinessobjectThe address where the organization operates from. Provide this if the principal place of business is different from theregisteredAddress.Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.registeredAddressobjectThe address of the organization registered at their registrar (such as the Chamber of Commerce).Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.registrationNumberstringThe organization's registration number.registrationNumberAbsentbooleanSet this totrueif the organization does not have a registration number available. Only applicable for organizations in New Zealand, and incorporated partnerships and government organizations in Australia.statusOfLegalProceedingstringThe status of any current or past legal action taken against the legal entity.Possible values:noLegalActionsTaken,underJudicialAdministration,bankruptcyInsolvency,otherLegalMeasuresIf the value of this field isnoLegalActionsTaken, thendateOfInitiationOfLegalProceedingis not required. Otherwise, it is required.stockDataobjectInformation about the organization's publicly traded stock. Provide this object only iftypeislistedPublicCompany.Show childrenHide childrenmarketIdentifierstringThe four-digitMarket Identifier Codeof the stock market where the organization's stocks are traded.stockNumberstringThe 12-digit International Securities Identification Number (ISIN) of the company, without dashes (-).tickerSymbolstringThe stock ticker symbol.supportobjectSupport information for the legal entity. Required if you have a platform setup.Show childrenHide childrenemailstringThe support email address of the legal entity. Required if you have a platform setup.phoneobjectThe support phone number of the legal entity. Required if you have a platform setup.Show childrenHide childrennumberstringThe full phone number, including the country code. For example,+3112345678.phoneCountryCodestringThe two-letterISO 3166-1 alpha-2country code prefix of the phone number. For example,USorNL.The value of thephoneCountryCodeis determined by the country code digit(s) ofphone.numbertypestringThe type of phone number.
Possible values:mobile,landline,sip,fax.taxInformationarray[object]The tax information of the organization.Show childrenHide childrencountrystringMin length:2Max length:2The two-letterISO 3166-1 alpha-2country code.numberstringThe tax ID number (TIN) of the organization or individual.numberAbsentbooleanSet this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.typestringThe TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.taxReportingClassificationobjectThe tax reporting classification (FATCA/CRS self-certification) of the organization.Show childrenHide childrenbusinessTypestringThe organization's business type.Possible values:other,listedPublicCompany,subsidiaryOfListedPublicCompany,governmentalOrganization,internationalOrganization,financialInstitution.financialInstitutionNumberstringThe Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a US financial institution and thebusinessTypeisfinancialInstitution.mainSourceOfIncomestringThe organization's main source of income. Only required ifbusinessTypeisother.Possible values:businessOperation,realEstateSales,investmentInterestOrRoyalty,propertyRental,other.typestringThe tax reporting classification type.Possible values:nonFinancialNonReportable,financialNonReportable,nonFinancialActive,nonFinancialPassive.typestringType of organization.Possible values:associationIncorporated,governmentalOrganization,listedPublicCompany,nonProfit,partnershipIncorporated,privateCompany.vatAbsenceReasonstringThe reason the organization has not provided a VAT number.Possible values:industryExemption,belowTaxThreshold.vatNumberstringThe organization's VAT number.webDataobjectDeprecated in version 1The website and app URL of the legal entity.Show childrenHide childrenwebAddressstringThe URL of the website or the app store URL.webAddressIdstringThe unique identifier of the web address.problemsarray[object]List of verification errors related to capabilities for the legal entity.Show childrenHide childrenentityobjectShow childrenHide childrendocumentsarray[string]List of document IDs corresponding to the verification errors from capabilities.idstringownerobjectShow childrenHide childrendocumentsarray[string]List of document IDs corresponding to the verification errors from capabilities.idstringtypestringtypestringverificationErrorsarray[object]Show childrenHide childrencapabilitiesarray[string]Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing.The value is an object containing the settings for the capability.codestringThe general error code.messagestringThe general error message.remediatingActionsarray[object]An object containing possible solutions to fix a verification error.Show childrenHide childrencodestringmessagestringsubErrorsarray[object]An array containing more granular information about the cause of the verification error.Show childrenHide childrencapabilitiesarray[string]Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing.The value is an object containing the settings for the capability.codestringThe general error code.messagestringThe general error message.typestringThe type of error.Possible values:invalidInputdataMissingpendingStatusrejecteddataReviewremediatingActionsarray[object]An object containing possible solutions to fix a verification error.Show childrenHide childrencodestringmessagestringtypestringThe type of error.Possible values:invalidInputdataMissingpendingStatusrejecteddataReviewreferencestringMax length:150Your reference for the legal entity, maximum 150 characters.soleProprietorshipobjectInformation about the sole proprietorship. Required iftypeissoleProprietorship.Show childrenHide childrencountryOfGoverningLawstringThe two-characterISO 3166-1 alpha-2country code of the governing country.dateOfIncorporationstringThe date when the legal arrangement was incorporated in YYYY-MM-DD format.doingBusinessAsstringThe registered name, if different from thename.doingBusinessAsAbsentbooleanSet this totrueif the legal arrangement does not have aDoing business asname.financialReportsarray[object]The information from the financial report of the sole proprietorship.Show childrenHide childrenannualTurnoverstringThe annual turnover of the business.balanceSheetTotalstringThe balance sheet total of the business.currencyOfFinancialDatastringThe currency used for the annual turnover, balance sheet total, and net assets.dateOfFinancialDatastringThe date the financial data were provided, in YYYY-MM-DD format.employeeCountstringThe number of employees of the business.netAssetsstringThe net assets of the business.namestringThe legal name.principalPlaceOfBusinessobjectThe business address. Required if the principal place of business is different from theregisteredAddress.Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.registeredAddressobjectThe address registered at the registrar, such as the Chamber of Commerce.Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.registrationNumberstringThe registration number.taxAbsentbooleanThe tax information is absent.taxInformationarray[object]The tax information of the entity.Show childrenHide childrencountrystringMin length:2Max length:2The two-letterISO 3166-1 alpha-2country code.numberstringThe tax ID number (TIN) of the organization or individual.numberAbsentbooleanSet this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.typestringThe TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.vatAbsenceReasonstringThe reason for not providing a VAT number.Possible values:industryExemption,belowTaxThreshold.vatNumberstringThe VAT number.transferInstrumentsarray[object]List of transfer instruments that the legal entity owns.Show childrenHide childrenaccountIdentifierstringThe masked IBAN or bank account number.idstringThe unique identifier of the resource.realLastFourstringFour last digits of the bank account number. If the transfer instrument is created usinginstant bank account verification, and it is a virtual bank account, these digits may be different from the last four digits of the masked account number.trustedSourcebooleanIdentifies if the bank account was created throughinstant bank verification.trustobjectInformation about the trust. Required iftypeistrust.Show childrenHide childrencountryOfGoverningLawstringThe two-characterISO 3166-1 alpha-2country code of the governing country.dateOfIncorporationstringThe date when the legal arrangement was incorporated in YYYY-MM-DD format.descriptionstringA short description about the trust. Only applicable for charitable trusts in New Zealand.doingBusinessAsstringThe registered name, if different from thename.doingBusinessAsAbsentbooleanSet this totrueif the legal arrangement does not have aDoing business asname.namestringThe legal name.principalPlaceOfBusinessobjectThe business address. Required if the principal place of business is different from theregisteredAddress.Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.registeredAddressobjectThe address registered at the registrar, such as the Chamber of Commerce.Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.registrationNumberstringThe registration number.taxInformationarray[object]The tax information of the entity.Show childrenHide childrencountrystringMin length:2Max length:2The two-letterISO 3166-1 alpha-2country code.numberstringThe tax ID number (TIN) of the organization or individual.numberAbsentbooleanSet this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.typestringThe TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.typestringType of trust.See possible values for trusts inAustraliaandNew Zealand.undefinedBeneficiaryInfoarray[object]The undefined beneficiary information of the entity.Show childrenHide childrendescriptionstringThe details of the undefined beneficiary.referencestringThe reference of the undefined beneficiary.vatAbsenceReasonstringThe reason for not providing a VAT number.Possible values:industryExemption,belowTaxThreshold.vatNumberstringThe VAT number.typestringThe type of legal entity.Possible values:individual,organization,soleProprietorship, ortrust.unincorporatedPartnershipobjectInformation about the unincorporated partnership. Required iftypeisunincorporatedPartnership.Show childrenHide childrencountryOfGoverningLawstringThe two-characterISO 3166-1 alpha-2country code of the governing country.dateOfIncorporationstringThe date when the legal arrangement was incorporated in YYYY-MM-DD format.descriptionstringShort description about the Legal Arrangement.doingBusinessAsstringThe registered name, if different from thename.doingBusinessAsAbsentbooleanSet this totrueif the legal arrangement does not have aDoing business asname.namestringThe legal name.principalPlaceOfBusinessobjectThe business address. Required if the principal place of business is different from theregisteredAddress.Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.registeredAddressobjectThe address registered at the registrar, such as the Chamber of Commerce.Show childrenHide childrencitystringThe name of the city. Required ifstateOrProvinceis provided.If you specify the city, you must also sendpostalCodeandstreet.countrystringThe two-letterISO 3166-1 alpha-2country code.postalCodestringThe postal code. Required ifstateOrProvinceand/orcityis provided.When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA.stateOrProvincestringThe two-letter ISO 3166-2 state or province code. For example,CAin the US. Required for Australia and New Zealand.If you specify the state or province, you must also sendcity,postalCode, andstreet.streetstringThe name of the street, and the house or building number. Required ifstateOrProvinceand/orcityis provided.street2stringThe apartment, unit, or suite number.registrationNumberstringThe registration number.taxInformationarray[object]The tax information of the entity.Show childrenHide childrencountrystringMin length:2Max length:2The two-letterISO 3166-1 alpha-2country code.numberstringThe tax ID number (TIN) of the organization or individual.numberAbsentbooleanSet this totrueif the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia.typestringThe TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provideSSN,EIN, orITINfor the US.typestringType of Partnership.Possible values:limitedPartnershipgeneralPartnershipfamilyPartnershipcommercialPartnershippublicPartnershipotherPartnershipgbrgmbhkgaacvvofmaatschapprivateFundLimitedPartnershipbusinessTrustEntitybusinessPartnershiplimitedLiabilityPartnershipegcooperativevoscomunidadDeBienesherenciaYacentecomunidadDePropietariossepscabtkktscssncvatAbsenceReasonstringThe reason for not providing a VAT number.Possible values:industryExemption,belowTaxThreshold.vatNumberstringThe VAT number.verificationDeadlinesarray[object]List of verification deadlines and the capabilities that will be disallowed if verification errors are not resolved.Show childrenHide childrencapabilitiesarray[string]The list of capabilities that will be disallowed if information is not reviewed by the time of the deadlineentityIdsarray[string]The unique identifiers of the legal entity or supporting entities that the deadline applies toexpiresAtstringThe date that verification is due by before capabilities are disallowed.verificationPlanstringA key-value pair that specifies the verification process for a legal entity. Set toupfrontfor upfront verification formarketplaces.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- pending: Adyen is running the verification.
- invalid: The verification failed. Check if theerrorsarray contains more information.
- valid: The verification has been successfully completed.
- rejected: Adyen has verified the information, but found reasons to not allow the capability.
- pending: Adyen is running the verification.
- invalid: The verification failed. Check if theerrorsarray contains more information.
- valid: The verification has been successfully completed.
- rejected: Adyen has verified the information, but found reasons to not allow the capability.
- Forindividual,name.firstNameandname.lastName.
- Fororganization,legalName.
- ForsoleProprietorship,name.
- Australia:driversLicense,passport
- Hong Kong:driversLicense,nationalIdNumber,passport
- New Zealand:driversLicense,passport
- Singapore:driversLicense,nationalIdNumber,passport
- All other supported countries:nationalIdNumber
- invalidInput
- dataMissing
- pendingStatus
- rejected
- dataReview
- invalidInput
- dataMissing
- pendingStatus
- rejected
- dataReview
- limitedPartnership
- generalPartnership
- familyPartnership
- commercialPartnership
- publicPartnership
- otherPartnership
- gbr
- gmbh
- kgaa
- cv
- vof
- maatschap
- privateFundLimitedPartnership
- businessTrustEntity
- businessPartnership
- limitedLiabilityPartnership
- eg
- cooperative
- vos
- comunidadDeBienes
- herenciaYacente
- comunidadDePropietarios
- sep
- sca
- bt
- kkt
- scs
- snc

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error