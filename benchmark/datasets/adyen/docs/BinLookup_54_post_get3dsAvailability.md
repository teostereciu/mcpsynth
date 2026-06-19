# BinLookup/54/post/get3dsAvailability

*Source: https://docs.adyen.com/api-explorer/BinLookup/54/post/get3dsAvailability*

---

# Check if 3D Secure is available
Verifies whether 3D Secure is available for the specified BIN or card brand. For 3D Secure 2, this endpoint also returns device fingerprinting keys.
For more information, refer to3D Secure 2.
This field contains additional data, which may be required for a particular request.
TheadditionalDataobject consists of entries, each of which includes the key and value.
List of brands.
Card number or BIN.
The merchant account identifier.
A recurring detail reference corresponding to a card.
The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID).
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessbinDetailsobjectBin Group DetailsShow childrenHide childrenissuerCountrystringThe country where the card was issued.dsPublicKeysarray[object]List of Directory Server (DS) public keys.Show childrenHide childrenbrandstringCard brand.directoryServerIdstringDirectory Server (DS) identifier.fromSDKVersionstringThe version of the mobile 3D Secure 2 SDK. For the possible values, refer to the versions inAdyen 3DS2 AndroidandAdyen 3DS2 iOS.publicKeystringPublic key. The 3D Secure 2 SDK encrypts the device information by using the DS public key.rootCertificatesstringDirectory Server root certificates. The 3D Secure 2 SDK verifies the ACS signed content using the rootCertificates.threeDS1SupportedbooleanIndicator if 3D Secure 1 is supported.threeDS2CardRangeDetailsarray[object]List of brand and card range pairs.Show childrenHide childrenacsInfoIndarray[string]Provides additional information to the 3DS Server.
Possible values:01 (Authentication is available at ACS)02 (Attempts supported by ACS or DS)03 (Decoupled authentication supported)04 (Whitelisting supported)brandCodestringCard brand.endRangestringBIN end range.startRangestringBIN start range.threeDS2Versionsarray[string]Supported 3D Secure protocol versionsthreeDSMethodURLstringIn a 3D Secure 2 browser-based flow, this is the URL where you should send the device fingerprint to.threeDS2supportedbooleanIndicator if 3D Secure 2 is supported.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- 01 (Authentication is available at ACS)
- 02 (Attempts supported by ACS or DS)
- 03 (Decoupled authentication supported)
- 04 (Whitelisting supported)

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error