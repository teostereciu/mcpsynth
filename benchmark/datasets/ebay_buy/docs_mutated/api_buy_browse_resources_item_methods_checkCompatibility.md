# buy/browse/resources/item/methods/checkCompatibility

*Source: https://developer.ebay.com/api-docs/buy/browse/resources/item/methods/checkCompatibility*

---

### Restrictions

## Input

### Resource URI

### URI parameters

### HTTP request headers

### OAuth scope

### Request payload

### Request fields

## Output

### HTTP response headers

### Response payload

### Response fields

### HTTP status codes

## Error codes

## Warnings

## Samples

### Sample 1: Checks for Part Compatibility on US Marketplace

### Sample 2: Sandbox Sample

#### Thank you for helping us to improve the eBay developer program.
POST/item/{listing_id}/check_compatibility
This method checks if a product is compatible with the specified item. You can use this method to check the compatibility of cars, trucks, and motorcycles with a specific part listed on eBay.For example, to check the compatibility of a part, you pass in theitem_idof the part as a URI parameter and specify all the attributes used to define a specific car within thecompatibilityPropertiescontainer. If the call is successful, the response will beCOMPATIBLE,NOT_COMPATIBLE, orUNDETERMINED. Refer tocompatibilityStatusfor details.Note:The only products supported are cars, trucks, and motorcycles.To find the attributes and values for a specific marketplace, you can use the compatibility methods in theTaxonomy API. You can use this data to create menus to help buyers specify the product, such as their car.For more information and a list of required attributes for the US marketplace that describe motor vehicles, refer toCheck compatibilityin theBuying Integration Guide.For an example, refer to theSamplessection.Note:This method is supported in Sandbox butonlywhen passing in the specifieditem_idand compatibility name-value pairs listed inSample 2: Sandbox Sample.RestrictionsFor a list of supported sites and other restrictions, refer toAPI Restrictions.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Conditional
Occurrence:Strongly Recommended
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
An array of attribute name/value pairs used to define a specific product. For example: If you wanted to specify a specific car, one of the name/value pairs would be"name" : "Year","value" : "2019"For a list of the attributes required for cars and trucks and motorcycles seeCheck compatibilityin the Buy Integration Guide.Occurrence:Required
The name of the product attribute, such asMake,Model,Year, etc.Occurrence:Required
The value for thenameattribute, such asBMW,R1200GS,2011, etc.Occurrence:Required
This call has no response headers.
An enumeration value that tells you if the item is compatible with the product.The values are:COMPATIBLE- Indicates the item is compatible with the product specified in the request.NOT_COMPATIBLE- Indicates the item is not compatible with the product specified in the request. Be sure to check all thevaluefields to ensure they are correct as errors in the value can also cause this response.UNDETERMINED- Indicates one or more attributes for the specified product are missing so compatibility cannot be determined.  The response returns the attributes that are missing.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
An array of warning messages. These types of errors do not prevent the method from executing but should be checked.Occurrence:Conditional
This string value indicates the error category. There are three categories of errors:request errors,application errors, andsystem errors.Occurrence:Always
Occurrence:Always
The name of the primary system where the error occurred. This is relevant for application errors.Occurrence:Always
A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.Occurrence:Always
An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.Occurrence:Conditional
A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem.Occurrence:Conditional
A description of the condition that caused the error or warning.Occurrence:Always
An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.Occurrence:Conditional
This is the name of input field that caused an issue with the call request.Occurrence:Conditional
This is the actual value that was passed in for the element specified in thenamefield.Occurrence:Conditional
The name of the subdomain in which the error or warning occurred.Occurrence:NA
Occurrence:NA
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
For more on warnings, plus the codes of other common warnings, seeHandling errors.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample checks whether the part specified by the item ID is compatible with the specified vehicle.
The item ID of the motor vehicle is input as a path parameter in the URL, and the attributes (name/value pairs) that define a specific vehicle are included in the request payload. In this sample, the part is a headlight bulb and the request
       will check whether the bulb is compatible with a 2016 Honda EX-L Hatchback 4-Door.You also need to pass inEBAY_USin theX-EBAY-C-MARKETPLACE-IDrequest header.
POSThttps://api.ebay.com/buy/browse/v1/item/v1|1**********9|0/check_compatibility
The output is thecompatibilityStatusfield, which shows that the part is compatible with the vehicle.
This sample can be ran in the Sandbox enviroment to produce a result that indicates that a motor vehicle part is compatibile with the vehicle specified in the request payload.
POSThttps://api.sandbox.ebay.com/buy/browse/v1/item/v1%7C281726208046%7C0/check_compatibility
Related topics
If you need help, contactDeveloper Technical Support.

```
v1|2**********2|0
```

```
v1|1**********2|4**********2
```
- When targeting the French locale of the Belgium marketplace, it is required to pass infr-BEto specify this. If this locale is not specified, the language will default to Dutch.
- When targeting the French locale of the Canadian marketplace, it is required to pass infr-CAto specify this. If this locale is not specified, the language will default to English.
- COMPATIBLE- Indicates the item is compatible with the product specified in the request.
- NOT_COMPATIBLE- Indicates the item is not compatible with the product specified in the request. Be sure to check all thevaluefields to ensure they are correct as errors in the value can also cause this response.
- UNDETERMINED- Indicates one or more attributes for the specified product are missing so compatibility cannot be determined.  The response returns the attributes that are missing.
- Buying Apps
- API DocumentationBrowse APIDeal APIFeed Beta APIFeed APIMarketing APIOffer APIOrder API
- Guides
- Related DocsUsing eBay RESTful APIsCommerce APIsDeveloper APIsFinding APIShopping API

[TABLE]
Parameter | Type | Description
listing_id | string | This path parameter specifies the unique RESTful identifier of an item (such as the park you want to check).RESTful Item ID Format:v1|#|#For a single SKU listing, pass in the item ID:v1|2**********2|0For a multi-SKU listing, pass in the identifier of the variation:v1|1**********2|4**********2For more information about item IDs for RESTful APIs, refer toItem ID legacy API compatibility overviewin theBuying Integration Guide.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client.Its value should be set toapplication/json.For more information, refer toHTTP request headersin theUsing eBay RESTful APIsguide.Occurrence:Required
Accept-Language | string | This header is used to indicate the natural language and locale preferred by the user for the response.This header is required when targeting a specific locale of a marketplace that supports multiple locales. For example:When targeting the French locale of the Belgium marketplace, it is required to pass infr-BEto specify this. If this locale is not specified, the language will default to Dutch.When targeting the French locale of the Canadian marketplace, it is required to pass infr-CAto specify this. If this locale is not specified, the language will default to English.Occurrence:Conditional
X-EBAY-C-MARKETPLACE-ID | string | This header identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US.Note:If the marketplace ID value is invalid or missing, the default value ofEBAY_USis used.SeeMarketplaceIdEnumfor a list of supported marketplaces.Default:EBAY_USOccurrence:Strongly Recommended
[/TABLE]

[TABLE]
Input container/field | Type | Description
compatibilityProperties | array ofAttributeNameValue | An array of attribute name/value pairs used to define a specific product. For example: If you wanted to specify a specific car, one of the name/value pairs would be"name" : "Year","value" : "2019"For a list of the attributes required for cars and trucks and motorcycles seeCheck compatibilityin the Buy Integration Guide.Occurrence:Required
compatibilityProperties.name | string | The name of the product attribute, such asMake,Model,Year, etc.Occurrence:Required
compatibilityProperties.value | string | The value for thenameattribute, such asBMW,R1200GS,2011, etc.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
compatibilityStatus | CompatibilityStatus | An enumeration value that tells you if the item is compatible with the product.The values are:COMPATIBLE- Indicates the item is compatible with the product specified in the request.NOT_COMPATIBLE- Indicates the item is not compatible with the product specified in the request. Be sure to check all thevaluefields to ensure they are correct as errors in the value can also cause this response.UNDETERMINED- Indicates one or more attributes for the specified product are missing so compatibility cannot be determined.  The response returns the attributes that are missing.Code so that your app gracefully handles any future changes to this list.Occurrence:Conditional
warnings | array ofErrorDetailV3 | An array of warning messages. These types of errors do not prevent the method from executing but should be checked.Occurrence:Conditional
warnings.category | string | This string value indicates the error category. There are three categories of errors:request errors,application errors, andsystem errors.Occurrence:Always
warnings.domain | string | The name of the primary system where the error occurred. This is relevant for application errors.Occurrence:Always
warnings.errorId | integer | A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.Occurrence:Always
warnings.inputRefIds | array ofstring | An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.Occurrence:Conditional
warnings.longMessage | string | A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem.Occurrence:Conditional
warnings.message | string | A description of the condition that caused the error or warning.Occurrence:Always
warnings.outputRefIds | array ofstring | An array of reference IDs that identify the specific response elements most closely associated to the error or warning, if any.Occurrence:Conditional
warnings.parameters | array ofErrorParameterV3 | An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.Occurrence:Conditional
warnings.parameters.name | string | This is the name of input field that caused an issue with the call request.Occurrence:Conditional
warnings.parameters.value | string | This is the actual value that was passed in for the element specified in thenamefield.Occurrence:Conditional
warnings.subdomain | string | The name of the subdomain in which the error or warning occurred.Occurrence:NA
[/TABLE]

[TABLE]
200 | OK
404 | Not Found
409 | Conflict
500 | Internal Server Error
[/TABLE]

[TABLE]
11000 | API_BROWSE | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
11001 | API_BROWSE | REQUEST | The specified item ID was not found.
11011 | API_BROWSE | REQUEST | The marketplace value {marketplaceId} is not supported. The supported values are: {allowedMarketplaces}
11503 | API_BROWSE | REQUEST | The request is either empty or incomplete. For help, see the documentation for this call.
11505 | API_BROWSE | REQUEST | The item is not valid for compatibility validation.
11506 | API_BROWSE | REQUEST | The 'name' {compatibilityNames} appears more than once in the request.
11507 | API_BROWSE | REQUEST | The following name(s) in the request are not supported {attributes}.
[/TABLE]

[TABLE]
11504 | API_BROWSE | REQUEST | The following compatibilityProperties (attributes name/value pairs) are missing: {attributes}
[/TABLE]