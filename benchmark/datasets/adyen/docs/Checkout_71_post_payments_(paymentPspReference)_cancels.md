# Checkout/71/post/payments/(paymentPspReference)/cancels

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/payments/(paymentPspReference)/cancels*

---

# Cancel an authorised payment
Cancels the authorisation on a payment that has not yet beencaptured, and returns a unique reference for this request. You get the outcome of the request asynchronously, in aCANCELLATIONwebhook.
If you want to cancel a payment but don't have thepspReference, use the/cancelsendpoint instead.

```
pspReference
```
If you want to cancel a payment but are not sure whether it has been captured, use the/payments/{paymentPspReference}/reversalsendpoint instead.

```
/payments/{paymentPspReference}/reversals
```
For more information, refer toCancel.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
ThepspReferenceof the payment that you want to cancel.

```
pspReference
```
Information about your application. For more details, seeBuilding Adyen solutions.
Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc.
Name of the field. For example, Name of External Platform.
Version of the field. For example, Version of External Platform.
Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc.
Name of the field. For example, Name of External Platform.
Version of the field. For example, Version of External Platform.
Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc.
External platform integrator.
Name of the field. For example, Name of External Platform.
Version of the field. For example, Version of External Platform.
Merchant developed software, such as cashier application, used to interact with the Adyen API.
Name of the field. For example, Name of External Platform.
Version of the field. For example, Version of External Platform.
Merchant device information.
Operating system running on the merchant device.
Version of the operating system on the merchant device.
Merchant device reference.
Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests.
Locale on the shopper interaction device.
Operating system running on the shopper interaction device.
Version of the operating system on the shopper interaction device.
Enhanced scheme data that may be required for processing the payment. For example, airline information.
Airline enhanced scheme datathat may be required for processing the transaction and/or for interchange savings.
The reference number for the invoice, issued by the agency.
- Encoding: ASCII
- minLength: 1 character
- maxLength: 6 characters
The two-letter agency plan identifier.
- Encoding: ASCII
- minLength: 2 characters
- maxLength: 2 characters
The amount charged for boarding the plane, inminor units.
- Encoding: Numeric
- minLength: 1 character
- maxLength: 11 characters
TheIATA3-digit accounting code (PAX) that identifies the carrier.
- Format: IATA 3-digit accounting code (PAX)
- Example: KLM = 074
- minLength: 3 characters
- maxLength: 3 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
TheCRSused to make the reservation and purchase the ticket.
- Encoding: ASCII
- minLength: 4 characters
- maxLength: 4 characters
The alphanumeric customer reference number.
- Encoding: ASCII
- maxLength: 20 characters
- If you send more than 20 characters, the customer reference number is truncated
- Must not start with a space or be all spaces.
TheIATA2-letter accounting code (PAX) that identifies the carrier.
- Encoding: ASCII
- Example: KLM = KL
- minLength: 2 characters
- maxLength: 2 characters
- Must not start with a space or be all spaces.
A code that identifies the type of item bought. The description of the code can appear on credit card statements.
- Encoding: ASCII
- Example: Passenger ticket = 01
- minLength: 2 characters
- maxLength: 2 characters
The flight departure date. Time is optional.
- Format for date only:yyyy-MM-dd
- Format for date and time:yyyy-MM-ddTHH:mm
- Use local time of departure airport.
- minLength: 10 characters
- maxLength: 16 characters
TheIATA2-letter accounting code (PAX) that identifies the carrier.
This field is required if the airline data includes leg details.
- Example: KLM = KL
- minLength: 2 characters
- maxLength: 2 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
A one-letter travel class identifier.
The following are common:
- F: first class
- J: business class
- Y: economy class
- W: premium economy
- Encoding: ASCII
- minLength: 1 character
- maxLength: 1 character
- Must not start with a space or be all spaces.
- Must not be all zeros.
Date and time of travel in formatyyyy-MM-ddTHH:mm.
- Use local time of departure airport.
- minLength: 16 characters
- maxLength: 16 characters
TheIATAthree-letter airport code of the departure airport.
This field is required if the airline data includes leg details.
- Encoding: ASCII
- Example: Amsterdam = AMS
- minLength: 3 characters
- maxLength: 3 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The amount ofdeparture taxcharged, inminor units.
- Encoding: Numeric
- minLength: 1
- maxLength: 11
- Must not be all zeros.
TheIATA3-letter airport code of the destination airport.
This field is required if the airline data includes leg details.
- Example: Amsterdam = AMS
- Encoding: ASCII
- minLength: 3 characters
- maxLength: 3 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
Thefare basis code, alphanumeric.
- minLength: 1 character
- maxLength: 15 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The flight identifier.
- minLength: 1 character
- maxLength: 5 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
A one-letter code that indicates whether the passenger is entitled to make a stopover. Can be a space, O if the passenger is entitled to make a stopover, or X if they are not.
- Encoding: ASCII
- minLength: 1 character
- maxLength: 1 character
The passenger's name, initials, and title.
- Format: last name + first name or initials + title
- Example:FLYER / MARY MS
- minLength: 1 character
- maxLength: 20 characters
- If you send more than 20 characters, the name is truncated
- Must not start with a space or be all spaces.
- Must not be all zeros.
The passenger's date of birth.
- Formatyyyy-MM-dd
- minLength: 10
- maxLength: 10
The passenger's first name.
This field is required if the airline data includes passenger details or leg details.
- Encoding: ASCII
The passenger's last name.
This field is required if the airline data includes passenger details or leg details.
- Encoding: ASCII
The passenger's phone number, including country code. This is an alphanumeric field that can include the '+' and '-' signs.
- Encoding: ASCII
- minLength: 3 characters
- maxLength: 30 characters
The IATA passenger type code (PTC).
- Encoding: ASCII
- minLength: 3 characters
- maxLength: 6 characters
The address of the organization that issued the ticket.
- minLength: 0 characters
- maxLength: 16 characters
The date that the ticket was issued to the passenger.
- minLength: 10 characters
- maxLength: 10 characters
- FormatISO 8601: yyyy-MM-dd
The ticket's unique identifier.
- minLength: 1 character
- maxLength: 15 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The unique identifier from IATA or ARC for the travel agency that issues the ticket.
- Encoding: ASCII
- minLength: 1 character
- maxLength: 8 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The name of the travel agency.
- Encoding: ASCII
- minLength: 1 character
- maxLength: 25 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
Level 2 and Level 3 enhanced scheme datathat may be required for processing the transaction and/or for interchange savings.
The reference number to identify the customer and their order.
- Format: ASCII
- Max length: 25 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
The destination address information.
The two-letterISO 3166-1 alpha-2or three-letterISO 3166-1 alpha-3 country codefor the destination address.
- Encoding: ASCII
- Min length: 2 characters
- Max length: 3 characters
The postal code of the destination address.
- Encoding: ASCII
- Max length: 10 characters
- Must not start with a space.
- For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.
- For Canada, it must be in 6 digits format. For example, M4B 1G5.
The state or province code of the destination address.
- Encoding: ASCII
- Max length: 3 characters
- Must not start with a space.
The duty tax amount, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
The shipping amount, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
The list of item detail lines.
The code that identifies the item in a standardized commodity coding scheme. There are different commodity coding schemes:
- UNSPSC commodity codes
- HS commodity codes
- NAICS commodity codes
- NAPCS commodity codes
- Encoding: ASCII
- Max length: 12 characters
- Must not start with a space or be all spaces.
- Must not be all zeros.
A description of the item, that provides details about the purchase.
For Visa transactions with level 3 ESD, the description must not be the same or very similar to your merchant name, or, consist only of common words like "product", or "service".
- Encoding: ASCII
- Max length: 26 characters
- Must not be a single character.
- Must not be blank.
- Must not be all special characters.
- Must not start with a space or be all spaces.
- Must not be all zeros.
The discount amount, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
The product code. Must be a unique product code associated with the item or service. This can be your unique code for the item, or the manufacturer's product code.
- Encoding: ASCII.
- Max length: 12 characters
The number of items. Must be an integer greater than zero.
- Encoding: Numeric
- Max value: 9999
The total amount for the line item, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
SeeAmount requirements for level 2/3 ESDto learn more about how to calculate the line item total.
The unit of measurement for an item.
- Encoding: ASCII
- Max length: 3 characters
The unit price, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
The date of the order.
- Min Length: 10 characters
- Max Length: 10 characters
- FormatISO 8601: yyyy-MM-dd
The postal code of the address where the item is shipped from.
- Encoding: ASCII
- Max length: 10 characters
- For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.
- For Canada, it must be in 6 digits format. For example, M4B 1G5.
The amount of state or provincialtax included in the total transaction amount, inminor units.
- For example, 2000 means USD 20.00.
- Encoding: Numeric
- Max value: 10000000000
- For L2 data: must not be all zeroes.
- For L3 data: can be zero.
The merchant account that is used to process the payment.
Your reference for the cancel request. Maximum length: 80 characters.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 201 - CreatedThe request has been fulfilled and has resulted in one or more new resources being created.Show moreShow lessmerchantAccountstringThe merchant account that is used to process the payment.paymentPspReferencestringThepspReferenceof the payment to cancel.pspReferencestringAdyen's 16-character reference associated with the cancel request.referencestringYour reference for the cancel request.statusstringThe status of your request. This will always have the valuereceived.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 201 - Created

```
pspReference
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error