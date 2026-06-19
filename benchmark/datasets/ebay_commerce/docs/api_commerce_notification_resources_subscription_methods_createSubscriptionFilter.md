# commerce/notification/resources/subscription/methods/createSubscriptionFilter

*Source: https://developer.ebay.com/api-docs/commerce/notification/resources/subscription/methods/createSubscriptionFilter*

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

### Sample 1: Receive Notifications from a Specific Marketplace

### Sample 2: Receive Notifications from a Specific Marketplace and Exclude Specific Meta Categories

### Sample 3: Receive Notifications from Multiple Marketplaces and Exclude Specific Meta Categories

#### Thank you for helping us to improve the eBay developer program.
POST/subscription/{subscription_id}/filter
This method allows applications to create a filter for a subscription. Filters allow applications to only be sent notifications that match a provided criteria. Notifications that do not match this criteria will not be sent to the destination.ThefilterSchemavalue must be a validJSON Schema Core document(version 2020-12 or later). ThefilterSchemaprovided must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications. The user does not need to provide$schemaand$iddefinitions.When a filter is first created, it is not immediately active on the subscription. If the request has a valid JSON body, the successful call returns the HTTP status code201 Created. Newly created filters are inPENDINGstatus until they are reviewed. If a filter is valid, it will move fromPENDINGstatus toENABLEDstatus. You can find the status of a filter using thegetSubscriptionFiltermethod. SeeCreating a subscription filter for a topicfor additional information.Note:Only one filter can be inENABLED(which means active) status on a subscription at a time. If anENABLEDfilter is overwritten by a new call toCREATEa filter for the subscription, it stays inENABLEDstatus until the newPENDINGfilter becomes theENABLEDfilter, and the existing filter then becomesDISABLED.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
https://api.ebay.com/oauth/api_scope/commerce.notification.subscription
SeeOAuth access tokensfor more information.
Note:An OAuth token created with theclient credentials grant flowand thehttps://api.ebay.com/oauth/api_scopescope is required in order to create, update, or retrieveapplication-basedsubscriptions to notification topics. An OAuth token created with theauthorization code grant flowand thehttps://api.ebay.com/oauth/api_scope/commerce.notification.subscriptionscope is required in order to create, update, or retrieveuser-basedsubscriptions to notification topics.
The content of a subscription filter as a validJSON Schema Core document(version 2020-12 or later). ThefilterSchemaprovided must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications.Note:Not all topics can have filters applied to them. UsegetTopicandgetTopicsrequests to determine if a specific topic is filterable. Filterable topics have the booleanfilterablereturned astruein the response.Note:If the JSON supplied as a subscription filter specifies a field that does not exist in the notifications for a topic, or if the topic is not filterable, the filter will be rejected and becomeDISABLED. If it is valid, however, the filter will move fromPENDINGstatus toENABLEDstatus.Initially, when thecreateSubscriptionFilterrequest has been made, if the request has a valid JSON body a201 Createdis returned. After that, the validation of thefilterSchemahappens. SeeCreating a subscription filter for a topicfor additional information.Occurrence:Required
SeeHTTP response headersfor details.
This call has no payload.
This call has no field definitions.
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This call creates a filter for a specified subscription that only sends notifications from a specific marketplace.
The input specifies thesubscriptionIdas a path parameter. It also requires thefilterSchemain the request payload. In this example, the request is to only receive notifications from the eBay France marketplace.
POSThttps://api.ebay.com/commerce/notification/v1/subscription/{subscription_id}/filter
A successful call returns the HTTP status code201 Created. This method has no response payload.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
subscription_id | string | The unique identifier of the subscription for which a filter will be created.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
[/TABLE]

[TABLE]
Input container/field | Type | Description
filterSchema | object | The content of a subscription filter as a validJSON Schema Core document(version 2020-12 or later). ThefilterSchemaprovided must describe the subscription's notification payload such that it supplies valid criteria to filter the subscription's notifications.Note:Not all topics can have filters applied to them. UsegetTopicandgetTopicsrequests to determine if a specific topic is filterable. Filterable topics have the booleanfilterablereturned astruein the response.Note:If the JSON supplied as a subscription filter specifies a field that does not exist in the notifications for a topic, or if the topic is not filterable, the filter will be rejected and becomeDISABLED. If it is valid, however, the filter will move fromPENDINGstatus toENABLEDstatus.Initially, when thecreateSubscriptionFilterrequest has been made, if the request has a valid JSON body a201 Createdis returned. After that, the validation of thefilterSchemahappens. SeeCreating a subscription filter for a topicfor additional information.Occurrence:Required
[/TABLE]

[TABLE]
Location | The location where the subscription filter resource was created.
[/TABLE]

[TABLE]
201 | Created
400 | Bad Request
403 | Forbidden
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
195000 | API_NOTIFICATION | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
195013 | API_NOTIFICATION | REQUEST | The subscription id does not exist.
195028 | API_NOTIFICATION | REQUEST | The application is not authorized to access the specified subscription.
195032 | API_NOTIFICATION | REQUEST | The specified subscription topic is not filterable.
195033 | API_NOTIFICATION | REQUEST | The specified 'filterSchema' value is invalid.
[/TABLE]