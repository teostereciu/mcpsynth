# legalentity/4/patch/businessLines/(id)

*Source: https://docs.adyen.com/api-explorer/legalentity/4/patch/businessLines/(id)*

---

# Update a business line
Updates a business line.
Requests to this endpoint are subject to rate limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.
The unique identifier of the business line.
A code that represents the industry of your legal entity. For example,4431Afor computer software stores.
A list of channels where goods or services are sold.
Possible values:pos,posMoto,eCommerce,ecomMoto,payByLink.
Required only in combination with theservicepaymentProcessing.
Contains information about the source of your user's funds. Required only if theserviceisbankingorissuing.
Indicates whether the funds are coming from transactions processed by Adyen. Iffalse, thetypeis required.
Required iftypeisbusiness,assetSale,gamblingWinningsorinheritance.
Fortypebusiness, provide the annual turn over of the business. FortypeassetSale,gamblingWinningsorinheritance, provide the amount of the funds.
The type of currency. Must be EUR (or EUR equivalent)
Total value of amount. Must be >= 0
The number of months that the asset has been in possession of the user.
For example, if the source of funds is of typecryptocurrencyIncomethenassetMonthsHeldis the number of months the user has owned the cryptocurrency.
Required iftypeiscryptocurrencyIncome. The cryptocurrency exchange where the funds were acquired.
Required iftypeisdonationsorinheritance. The date the funds were received, in YYYY-MM-DD format.
Required iftypeisassetSaleorgamblingWinnings. The date the funds were received, in YYYY-MM-DD format.
For example, if the source of funds is of typeassetSale, the dateOfSourceEvent is the date of the sale. If the source of funds is of typegamblingWinnings, the dateOfSourceEvent is the date of winnings.
Required iftypeisbusinessorassetSale. A description for the source of funds.
For example, fortypebusiness, provide a description of where the business transactions come from, such as payments through bank transfer. FortypeassetSale, provide a description of the asset. For example, the address of a residential property if it is a property sale.
Required iftypeisthirdPartyFunding. Information about the financiers.
The amount of the funds the financier provided.
The type of currency. Must be EUR (or EUR equivalent)
Total value of amount. Must be >= 0
The financier's first name.
The financier's last name.
The city and country/region where the financier is currently located. For example: Chicago, USA
Required iftypeisdonationsorinheritance. The legal entity ID representing the originator of the source of funds.
For example, if the source of funds isinheritance, thenoriginatorOfFundsReferenceshould be the legal entity reference of the benefactor.
Required iftypeisdonations. The reason for receiving the funds.
Required iftypeisdonationsorinheritance. The relationship of the originator of the funds to the recipient.
The type of the source of funds.
Possible values:
- business
- employment
- donations
- inheritance
- financialAid
- rentalIncome
- dividendIncome
- royaltyIncome
- thirdPartyFunding
- pensionIncome
- insuranceSettlement
- cryptocurrencyIncome
- assetSale
- loans
- gamblingWinnings
Required iftypeisgamblingWinnings. The location of the gambling site for the winnings.
For example, if the source of funds is online gambling, provide the website of the gambling company.
List of website URLs where your user's goods or services are sold. When this is required for a service but your user does not have an online presence, provide the reason in thewebDataExemptionobject.
The URL of the website or the app store URL.
The reason why the web data is not provided.
The reason why the web data was not provided. Possible value:noOnlinePresence.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessidstringThe unique identifier of the business line.industryCodestringA code that represents the industry of the legal entity formarketplacesorplatforms. For example,4431Afor computer software stores.legalEntityIdstringUnique identifier of thelegal entitythat owns the business line.problemsarray[object]The verification errors related to capabilities for this supporting entity.Show childrenHide childrenentityobjectShow childrenHide childrendocumentsarray[string]List of document IDs corresponding to the verification errors from capabilities.idstringownerobjectShow childrenHide childrendocumentsarray[string]List of document IDs corresponding to the verification errors from capabilities.idstringtypestringtypestringverificationErrorsarray[object]Show childrenHide childrencapabilitiesarray[string]Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing.The value is an object containing the settings for the capability.codestringThe general error code.messagestringThe general error message.remediatingActionsarray[object]An object containing possible solutions to fix a verification error.Show childrenHide childrencodestringmessagestringsubErrorsarray[object]An array containing more granular information about the cause of the verification error.Show childrenHide childrencapabilitiesarray[string]Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing.The value is an object containing the settings for the capability.codestringThe general error code.messagestringThe general error message.typestringThe type of error.Possible values:invalidInputdataMissingpendingStatusrejecteddataReviewremediatingActionsarray[object]An object containing possible solutions to fix a verification error.Show childrenHide childrencodestringmessagestringtypestringThe type of error.Possible values:invalidInputdataMissingpendingStatusrejecteddataReviewsalesChannelsarray[string]A list of channels where goods or services are sold.Possible values:pos,posMoto,eCommerce,ecomMoto,payByLink.Required only in combination with theservicepaymentProcessing.servicestringThe service for which you are creating the business line.Possible values:paymentProcessingissuingbankingsourceOfFundsobjectContains information about the source of your user's funds. Required only if theserviceisbankingorissuing.Show childrenHide childrenadyenProcessedFundsbooleanIndicates whether the funds are coming from transactions processed by Adyen. Iffalse, thetypeis required.amountobjectRequired iftypeisbusiness,assetSale,gamblingWinningsorinheritance.Fortypebusiness, provide the annual turn over of the business. FortypeassetSale,gamblingWinningsorinheritance, provide the amount of the funds.Show childrenHide childrencurrencystringThe type of currency. Must be EUR (or EUR equivalent)valueintegerTotal value of amount. Must be >= 0assetMonthsHeldintegerThe number of months that the asset has been in possession of the user.For example, if the source of funds is of typecryptocurrencyIncomethenassetMonthsHeldis the number of months the user has owned the cryptocurrency.cryptocurrencyExchangestringRequired iftypeiscryptocurrencyIncome. The cryptocurrency exchange where the funds were acquired.dateOfFundsReceivedstringRequired iftypeisdonationsorinheritance. The date the funds were received, in YYYY-MM-DD format.dateOfSourceEventstringRequired iftypeisassetSaleorgamblingWinnings. The date the funds were received, in YYYY-MM-DD format.For example, if the source of funds is of typeassetSale, the dateOfSourceEvent is the date of the sale. If the source of funds is of typegamblingWinnings, the dateOfSourceEvent is the date of winnings.descriptionstringRequired iftypeisbusinessorassetSale. A description for the source of funds.For example, fortypebusiness, provide a description of where the business transactions come from, such as payments through bank transfer. FortypeassetSale, provide a description of the asset. For example, the address of a residential property if it is a property sale.financiersarray[object]Required iftypeisthirdPartyFunding. Information about the financiers.Show childrenHide childrenamountobjectThe amount of the funds the financier provided.Show childrenHide childrencurrencystringThe type of currency. Must be EUR (or EUR equivalent)valueintegerTotal value of amount. Must be >= 0firstNamestringThe financier's first name.lastNamestringThe financier's last name.locationstringThe city and country/region where the financier is currently located. For example: Chicago, USAoriginatorLegalEntityIdstringRequired iftypeisdonationsorinheritance. The legal entity ID representing the originator of the source of funds.For example, if the source of funds isinheritance, thenoriginatorOfFundsReferenceshould be the legal entity reference of the benefactor.purposestringRequired iftypeisdonations. The reason for receiving the funds.relationshipstringRequired iftypeisdonationsorinheritance. The relationship of the originator of the funds to the recipient.typestringThe type of the source of funds.Possible values:businessemploymentdonationsinheritancefinancialAidrentalIncomedividendIncomeroyaltyIncomethirdPartyFundingpensionIncomeinsuranceSettlementcryptocurrencyIncomeassetSaleloansgamblingWinningswebsitestringRequired iftypeisgamblingWinnings. The location of the gambling site for the winnings.For example, if the source of funds is online gambling, provide the website of the gambling company.webDataarray[object]List of website URLs where your user's goods or services are sold. When this is required for a service but your user does not have an online presence, provide the reason in thewebDataExemptionobject.Show childrenHide childrenwebAddressstringThe URL of the website or the app store URL.webAddressIdstringThe unique identifier of the web address.webDataExemptionobjectThe reason why the web data is not provided.Show childrenHide childrenreasonstringThe reason why the web data was not provided. Possible value:noOnlinePresence.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
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
- paymentProcessing
- issuing
- banking
- business
- employment
- donations
- inheritance
- financialAid
- rentalIncome
- dividendIncome
- royaltyIncome
- thirdPartyFunding
- pensionIncome
- insuranceSettlement
- cryptocurrencyIncome
- assetSale
- loans
- gamblingWinnings

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error