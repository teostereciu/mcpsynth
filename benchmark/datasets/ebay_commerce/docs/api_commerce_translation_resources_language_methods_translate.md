# commerce/translation/resources/language/methods/translate

*Source: https://developer.ebay.com/api-docs/commerce/translation/resources/language/methods/translate*

---

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

### Sample 1: Translate an Item's Title

### Sample 2: Translate an Item's Description

#### Thank you for helping us to improve the eBay developer program.
POST/translate
This method translates listing title and listing description text from one language into another. For a full list of supported language translations, see thetable.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
The language of the input text to be translated. Not allLanguageEnumvalues are supported in this field. For a full list of supported language pairings, see the Supported languagestable.Occurrence:Required
The input text to translate. The maximum number of characters permitted is determined by thetranslationContextvalue:ITEM_TITLE: 1000 characters maximumITEM_DESCRIPTION: 20,000 characters maximum.Note:When translatingITEM_DESCRIPTIONtext, HTML/CSS markup and links can be included and will not count toward this 20,000 character limit.Note:Currently, only one input string can be translated per API call. Support for multiple continuous text strings is expected in the future.Occurrence:Required
The target language for the translation of the input text. Not allLanguageEnumvalues are supported in this field. For a full list of supported language pairings, see the Supported languagestable.Occurrence:Required
Input the listing entity to be translated.Valid Values:ITEM_TITLEandITEM_DESCRIPTION
This call has no response headers.
The enumeration value indicates the language of the input text.Occurrence:Always
Occurrence:Always
An array showing the input and translated text. Only one input string can be translated at this time. Support for multiple continuous text strings is expected in the future.Occurrence:Always
The original text, in the language specified in thefromfield, that was input into thetextfield in the request.Occurrence:Always
The translation of the original text into the language specified in thetofield.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
Translate the title of an item's listing from English to German.
This sample translates an item's title from English to German.
POSThttps://api.ebay.com/commerce/translation/v1_beta/translate
Upon success, the response includes the translated title, the original title, as well as the source and target languages.
Translate the description of an item from English to Chinese (Mandarin).
This sample translates an item's description from English to Chinese (Mandarin).
POSThttps://apid.ebay.com/commerce/translation/v1/translate
Related topics
If you need help, contactDeveloper Technical Support.
- ITEM_TITLE: 1000 characters maximum
- ITEM_DESCRIPTION: 20,000 characters maximum.Note:When translatingITEM_DESCRIPTIONtext, HTML/CSS markup and links can be included and will not count toward this 20,000 character limit.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
[/TABLE]

[TABLE]
Input container/field | Type | Description
from | LanguageEnum | The language of the input text to be translated. Not allLanguageEnumvalues are supported in this field. For a full list of supported language pairings, see the Supported languagestable.Occurrence:Required
text | array ofstring | The input text to translate. The maximum number of characters permitted is determined by thetranslationContextvalue:ITEM_TITLE: 1000 characters maximumITEM_DESCRIPTION: 20,000 characters maximum.Note:When translatingITEM_DESCRIPTIONtext, HTML/CSS markup and links can be included and will not count toward this 20,000 character limit.Note:Currently, only one input string can be translated per API call. Support for multiple continuous text strings is expected in the future.Occurrence:Required
to | LanguageEnum | The target language for the translation of the input text. Not allLanguageEnumvalues are supported in this field. For a full list of supported language pairings, see the Supported languagestable.Occurrence:Required
translationContext | TranslationContextEnum | Input the listing entity to be translated.Valid Values:ITEM_TITLEandITEM_DESCRIPTIONOccurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
from | LanguageEnum | The enumeration value indicates the language of the input text.Occurrence:Always
to | LanguageEnum | The enumeration value indicates the language of the translated text.Occurrence:Always
translations | array ofTranslation | An array showing the input and translated text. Only one input string can be translated at this time. Support for multiple continuous text strings is expected in the future.Occurrence:Always
translations.originalText | string | The original text, in the language specified in thefromfield, that was input into thetextfield in the request.Occurrence:Always
translations.translatedText | string | The translation of the original text into the language specified in thetofield.Occurrence:Always
[/TABLE]

[TABLE]
200 | OK
400 | Bad Request
500 | Internal Server Error
[/TABLE]

[TABLE]
110000 | API_TRANSLATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
110001 | API_TRANSLATION | REQUEST | From language is invalid, missing or not supported. For more information, see the API call reference documentation.
110002 | API_TRANSLATION | REQUEST | To language is invalid, missing or not supported. For more information, see the API call reference documentation.
110003 | API_TRANSLATION | REQUEST | Context is not supported. For more information, see the API call reference documentation.
110004 | API_TRANSLATION | REQUEST | Maximum number of input text reached. For more information, see the API call reference documentation.
110005 | API_TRANSLATION | REQUEST | Maximum length of input text reached. For more information, see the API call reference documentation.
110006 | API_TRANSLATION | REQUEST | Unsupported from and to combination.
110007 | API_TRANSLATION | REQUEST | Markups are not supported in input texts for title translation context.
110008 | API_TRANSLATION | REQUEST | Input text missing.
[/TABLE]