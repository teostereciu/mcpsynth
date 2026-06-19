# Property validations API

*Source: https://developers.hubspot.com/docs/api-reference/crm-property-validations-v3/guide*

---

Property Validations

# Property validations API

The property validations endpoints allow you to view, create, and update validation rules for your properties.

[Property validation rules](https://knowledge.hubspot.com/properties/set-validation-rules-for-properties) determine formatting requirements for text, date picker, date and time picker, and number properties. For example, an _Account ID_ property that can only include numbers. You can use the property validations API to set up validation rules, edit existing validation rules, or retrieve validation rules so you’re aware of formatting requirements when setting or updating property values.

Scope requirements

To complete more actions with properties, refer to the [Properties API](/docs/api-reference/crm-properties-v3/guide).

##

​

Add or update validation rules for a property

To add or update validation rules, make a `PUT` request to `/crm/v3/property-validations/{objectTypeId}/{propertyName}/rule-type/{ruleType}`. The `ruleType` is a category for the rule, for which options depend on the [property `type` and `fieldType`](/docs/api-reference/crm-properties-v3/guide#property-type-and-fieldtype-values). When you make the request, if there’s an existing validation rule with that `ruleType`, the rule you’ve created will overwrite the existing rule. The rule will not overwrite rules of other types. In your request body, include the following:

  * `ruleArguments`: an array containing the arguments that define the specific conditions or parameters for the validation rule. Arguments depend on the `ruleType`.
  * `shouldApplyNormalization` (optional): a boolean that indicates whether to normalize input before validation.

The available `ruleType` values and their arguments are:

`ruleType` values| Supported `type` (and `fieldType`)| Rule description| Arguments| Examples
---|---|---|---|---
`AFTER_DATETIME_DURATION`| `datetime`| Require a duration after the current date and time.| ISO-8601 period| `["P1Y"]` (1 year)
`AFTER_DURATION`| `date`| Require a duration after the current date.| ISO-8601 period| `["P7D"]` (7 days)
`ALPHANUMERIC`| `string` (`text` and `textarea`)| Restrict values to certain alphanumeric characters.| One of `ALPHANUMERIC`, `ALPHA_ONLY`, or `NUMERIC_ONLY`.| `["ALPHA_ONLY"]`
`BEFORE_DATETIME_DURATION`| `datetime`| Require a duration before the current date and time.| ISO-8601 period| `["P1M"]` (1 month)
`BEFORE_DURATION`| `date`| Require a duration before the current date.| ISO-8601 period| `["P30D"]` (30 days)
`DAYS_OF_WEEK`| `date`, `datetime`| Restrict values to specific days.| One to seven days by name (e.g, `MONDAY`, `TUESDAY`).| `["MONDAY", "WEDNESDAY", "FRIDAY"]`
`DECIMAL`| `number`| Restrict the number of decimal places in values.| Integer (0-20)| `["2"]`
`DOMAIN`| `string` (`text`)| Validate domain formatting.| None| `[]`
`EMAIL`| `string` (`text`)| Validate email address formatting.| None| `[]`
`EMAIL_ALLOWED_DOMAINS`| `string` (`text`)| Restrict to specific email domains.| One to 20 domain strings.| `["company.com", "partner.com"]`.
`EMAIL_BLOCKED_DOMAINS`| `string` (`text`)| Block specific email domains.| One to 20 domain strings.| `["competitor.com"]`
`END_DATE`| `date`| Set a maximum date.| Unix timestamp (ms)| `["1640995200000"]`
`END_DATETIME`| `datetime`| Set a maximum date and time.| Unix timestamp (ms)| `["1640995200000"]`
`FORMAT`| `string` (`text` and `textarea`)| Require specific text case formatting.| One of `CAPITALIZATION`, `UPPER`, or `LOWER`.| `["UPPER"]`
`MAX_LENGTH`| `string` (`text`, `textarea`, and `phonenumber`)| Set a maximum character length.| Integer (1-10000)| `["100"]`
`MAX_NUMBER`| `number`| Set a maximum numeric value.| Numeric value| `["1000"]` or `["99.99"]`
`MIN_LENGTH`| `string` (`text`, `textarea`, and `phonenumber`)| Set a minimum character length.| Integer (greater than 1)| `["5"]`
`MIN_NUMBER`| `number`| Set a minimum numeric value.| Numeric value| `["0"]` or `["-10.5"]`
`PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE`| `string` (`phonenumber`)| Validate phone number formatting, with option to validate by country code.| None, or optional 2-letter country code (lowercase).| `[]` or `["us"]`
`REGEX`| `string` (`text` and `textarea`)| Validate values with custom regular expressions.| Regex pattern (RE2 syntax), error message.| `["^[A-Z]+$", "Must be uppercase"]`
`SPECIAL_CHARACTERS`| `string` (`text` and `textarea`)| Restrict special characters.| `NOT_ALLOWED`| `["NOT_ALLOWED"]`
`START_DATE`| `date`| Set a minimum date.| Unix timestamp (ms)| `["1640995200000"]`
`START_DATETIME`| `datetime`| Set a minimum date and time.| Unix timestamp (ms)| `["1640995200000"]`
`URL`| `string` (`text`)| Validate URL formatting.| None| `[]`
`URL_ALLOWED_DOMAINS`| `string` (`text`)| Restrict to certain domains.| One to 20 domain strings.| `["hubspot.com", "example.com"]`
`URL_BLOCKED_DOMAINS`| `string` (`text`)| Block specific domains.| One to 20 domain strings.| `["spam.com", "bad-site.net"]`
`WHITESPACE`| `string` (`text`)| Set rules for handling whitespace.| None, or optional `ALL` (default) or `TRIM`.| `[]` or `["TRIM"]`

For example:

  * To set an `ALPHANUMERIC` rule that allows only numeric characters for the _Order ID_ deal property, make a `PUT` request to `/crm/v3/property-validations/0-3/order_id/rule-type/ALPHANUMERIC` with the following request body:


    {
      "ruleArguments": [
        "NUMERIC_ONLY"
      ],
      "shouldApplyNormalization": false
    }


  * To set a `MIN_LENGTH` rule that requires at least one character for the _Pet name_ property, make a `PUT` request to `/crm/v3/property-validations/{custom object type ID}/pet_name/rule-type/MIN_LENGTH` with the following request body:


    {
      "ruleArguments": [
        "1"
      ]
    }


##

​

Retrieve all properties with validation rules for an object

To view all properties of an object that have validation rules, make a `GET` request to `/crm/v3/property-validations/{objectTypeId}`. Refer to [this guide](/docs/guides/crm/understanding-the-crm#object-type-ids) for a full list of `objectTypeId` values. Properties with validation rules are returned with the following fields:

  * `propertyName`: the name of the property with validation rules.
  * `propertyValidationRules`: an array with the rules set for the property. Includes each rule’s `ruleType` (the category for the rule) and `ruleArguments` (specific requirements of the rule).

For example, to request contact properties with validation rules, make a `GET` request to `/crm/v3/property-validations/0-1`. In the following response, there are two properties with rules, the `zip` (Postal Code) property which only allows numeric characters and the `age` property which requires a minimum value of 1.


    {
      "results": [
        {
          "propertyName": "zip",
          "propertyValidationRules": [
            {
              "ruleType": "ALPHANUMERIC",
              "ruleArguments": ["NUMERIC_ONLY"]
            }
          ]
        },
        {
          "propertyName": "age",
          "propertyValidationRules": [
            {
              "ruleType": "MIN_NUMBER",
              "ruleArguments": ["1"]
            }
          ]
        }
      ]
    }


##

​

Retrieve all validation rules for a property

To view the validation rules set for a specific property, make a `GET` request to `/crm/v3/property-validations/{objectTypeId}/{propertyName}`. You can refer to [this guide](/docs/api-reference/crm-property-validations-v3/guide#object-type-ids) for a full list of `objectTypeId` values and use the [Properties API](/docs/api-reference/crm-properties-v3/guide) to retrieve `propertyName` values. The property’s rules are returned with the `ruleType` and `ruleArguments` for each. For example, to view validation rules for an Order ID deal property, make a `GET` request to `/crm/v3/property-validations/0-3/order_id`. In the following response, the property has three rules that require the value to contain between one and eight numeric characters.


    {
      "results": [
        {
          "ruleType": "ALPHANUMERIC",
          "ruleArguments": ["NUMERIC_ONLY"]
        },
        {
          "ruleType": "MAX_LENGTH",
          "ruleArguments": ["10"]
        },
        {
          "ruleType": "MIN_LENGTH",
          "ruleArguments": ["1"]
        }
      ]
    }


##

​

Retrieve a specific type of validation rule for a property

To view more information about a specific validation rule for a property, make a `GET` request to `/crm/v3/property-validations/{objectTypeId}/{propertyName}/rule-type/{ruleType}`. The response includes the `ruleType`, `ruleArguments`, and the optional `shouldApplyNormalization` field. For example, to view more details about the alphanumeric character rule for the _Order ID_ property, make a `GET` request to `/crm/v3/property-validations/0-3/order_id/rule-type/ALPHANUMERIC`.

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)