# Checkout/71/post/cardDetails

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/cardDetails*

---

# Get the brands and other details of a card
Use this endpoint to get information about the card or network token that enables you to decide on the routing of the transaction and the eligibility of the card for the type of transaction.
If you includeyour supported brandsin the request, the response also tells you if you support eachbrand that was identified on the card.
If you have an API-only integration and collect card data, use this endpoint to find out if the shopper's card is co-bad. For co-badged cards, you must let the shopper choose the brand to pay with  if you support both brands.

## Server-side API libraries
We provide open-sourceserver-side API librariesin several languages:
- PHP
- Java
- Node.js
- .NET
- Go
- Python
- Ruby
- Apex (beta)
See ourintegration examplesfor example uses of the libraries.

## Developer resources
BIN Lookup API is available through a Postman collection. Click the button below to create a fork, then set the environment variables atEnvironments>Adyen APIs.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
A minimum of the first six digits of the card number. The full card number gives the best result.
You must befully PCI compliantto collect raw card data. Alternatively, you can use theencryptedCardNumberfield.
The shopper country code.
Format:ISO 3166-1 alpha-2Example: NL or DE
The encrypted card number.
The merchant account identifier, with which you want to process the transaction.
The card brands you support. This is thebrandsarray from your/paymentMethodsresponse.

```
/paymentMethods
```
If not included, our API uses the ones configured for your merchant account and, if provided, the country code.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessbrandsarray[object]The list of brands identified for the card.Show childrenHide childrensupportedbooleanIndicates if you support the card brand.typestringThe name of the card brand.fundingSourcestringThe funding source of the card, for exampleDEBIT,CREDIT, orPREPAID.isCardCommercialbooleanIndicates if this is a commercial card or a consumer card. Iftrue, it is a commercial card. Iffalse, it is a consumer card.issuingCountryCodestringThe two-letter country code  of the country where the card was issued.

#### 200 - OK