# Define custom events

*Source: https://developers.hubspot.com/docs/api-reference/legacy/events/define-events/guide*

---

Define events

# Define custom events

Learn more about creating custom events using HubSpot’s API.

Supported products

Scope requirements

Use custom events to define and track events that are unique to your business. Custom events capture what occurred at a specific moment in time, so are often used to track user activity and behavior. For example, create custom events that track when users add an item to a cart, view a page on your website, or log in to your app. By tracking user activity, events can give you a better understanding of behavioral patterns and changes over time. Before you can send event data into HubSpot, you need to define your custom event. Custom event definitions include details such as the event’s name, display label, target object, and event properties. Once defined, each instance of a custom event sent to HubSpot is called a [custom event occurrence](/docs/api-reference/legacy/events/send-event-data/guide). Below, learn more about creating and managing event definitions using the API. If you have an _Enterprise_ subscription, learn how to [define events in your HubSpot account](https://knowledge.hubspot.com/reports/create-custom-events).

If you’re a [technology partner](https://www.hubspot.com/partners/technology/join) looking to define events for your app in the HubSpot Marketplace, refer to [this guide about defining app events](/docs/apps/developer-platform/add-features/app-events/create-and-manage-event-types).

##

​

Define a custom event

To create a custom event schema (i.e. define a new custom event), make a `POST` request to `events/v3/event-definitions`. In the request body, include definitions for your event schema, including its label, name, CRM object associations, and custom properties. You can include the following fields in your request body:

Parameter| Type| Description
---|---|---
`label` | String| The event’s human readable label, which will display in HubSpot. The label can be up to 100 characters, but long labels may be cut off in certain parts of HubSpot’s UI.
`name`| String| The unique, internal name of the event, which you’ll use to reference the event through the API. The name can be up to 50 characters, must start with a letter, and can only contain lowercase letters, numbers, and underscores. If no value is provided, HubSpot will automatically generate one based on the label. Once defined, the `name` cannot be changed.
`description`| String| Text to describe the event, displayed in the HubSpot UI.
`propertyDefinitions`| Array| Include this array to define up to 50 custom event properties. For each property, include the required fields to create an event property.
`primaryObject`| String| The object with which to associate event data. Event occurrences will appear on records of that object. Can be one of: `"CONTACT"` (default), `"COMPANY"`, `"DEAL"`, `"TICKET"`, or `"<CUSTOM_OBJECT_NAME>"`. This cannot be changed after the event definition is created.
`customMatchingId`| Object| Sets a rule that automatically associates event occurrences with records of the specified object by matching the value of a property in the event data with the value of a _unique_ property on the target object. Includes a nested `primaryObjectRule` object with the following required fields:

  * `targetObjectPropertyName`: a string that specifies the name of the unique property on the target object to use for matching.
  * `eventPropertyName`: a string that specifies the name of the property in the custom event data to use for matching.

Learn more about setting up a custom matching ID.
`includeDefaultProperties`| Boolean| Specifies whether the event should include the default event properties. The default value is `true`, so only include this field to set the value as `false`. When `false`, the default event properties are not added to the event schema, which means you can only use your defined custom properties for event occurrences.

The request body below provides a basic example of an event definition, for which two custom properties are created and the default event properties are not included.


    {
      "label": "My event label",
      "name": "unique_event_name",
      "description": "An event description that helps users understand what the event tracks.",
      "primaryObject": "COMPANY",
      "propertyDefinitions": [
        {
          "name": "choice_property",
          "label": "Choice property",
          "type": "enumeration",
          "options": [
            {
              "label": "Option 1",
              "value": "1"
            },
            {
              "label": "Option 2",
              "value": "2"
            }
          ]
        },
        {
          "name": "string_property",
          "label": "String property",
          "type": "string"
        }
      ],
      "includeDefaultProperties": false
    }


###

​

Set up a custom matching ID

To automatically [link event occurrences to records](/docs/api-reference/legacy/events/send-event-data/guide#link-event-occurrences-to-records) of a specified object (e.g., automatically link event occurrences with companies), include the `customMatchingId` object in your definition request. In this object, define a `primaryObjectRule` object with the following fields: the unique object property that you’ve set up beforehand as the `targetObjectPropertyName`, and one of the properties from your event definition as the `eventPropertyName`. For example, the following request body specifies a `customMatchingId` that matches a company property `"unique_object_property"` and the event property `"string_property"`.


    {
      "label": "My event label",
      "name": "unique_event_name",
      "description": "An event description that helps users understand what the event tracks.",
      "primaryObject": "COMPANY",
      "propertyDefinitions": [
        {
          "name": "string_property",
          "label": "String property",
          "type": "string"
        }
      ],
      "customMatchingId": {
        "primaryObjectRule": {
          "targetObjectPropertyName": "unique_object_property",
          "eventPropertyName": "string_property"
        }
      }
    }


Including this rule means that you won’t need to specify the target `objectId` each time you send an event occurrence, instead using the `customMatchingId` event property as the matching ID to identify the record. Learn more about [sending custom event occurrences linked to records](/docs/api-reference/legacy/events/send-event-data/guide#link-event-occurrences-to-records).

##

​

Manage properties in event definitions

Event properties are used to store information on individual custom event occurrences. These properties should be used when appropriate for sending event occurrences, but they are not required for an event occurrence to be valid. For each event definition, HubSpot provides a default set of properties, but you can also create custom properties for an event. Below, learn about HubSpot’s default event properties, how to define new properties for existing events, and how to update existing custom event properties.

###

​

HubSpot’s default event properties

Expand the section below to view the default event properties. These properties are included for each event, unless you’ve set the `includeDefaultProperties` field as `false` when defining your custom event.

Show Default event properties list

Property name| Property label| Type| Field Type
---|---|---|---
`hs_browser`| Browser| String| Single-line text (`text`)
`hs_city`| City| String| Single-line text (`text`)
`hs_country`| Country| String| Single-line text (`text`)
`hs_device_type`| Device type| Enumeration| Dropdown select (`select`)
`hs_element_class`| Element class| String| Single-line text (`text`)
`hs_element_id`| Element ID| String| Single-line text (`text`)
`hs_element_text`| Element text| String| Single-line text (`text`)
`hs_language`| Language| Enumeration| Dropdown select (`select`)
`hs_link_href `| Link href| String| Single-line text (`text`)
`hs_page_content_type`| Page content type| Enumeration| Dropdown select (`select`)
`hs_page_id`| Page ID| String| Single-line text (`text`)
`hs_page_title`| Page title| String| Single-line text (`text`)
`hs_page_url`| Page URL| String| Single-line text (`text`)
`hs_region`| Region| String| Single-line text (`text`)
`hs_referrer`| Referrer| String| Single-line text (`text`)
`hs_user_agent`| User agent| String| Single-line text (`text`)
`hs_utm_campaign`| UTM Campaign| String| Single-line text (`text`)
`hs_utm_medium`| UTM Medium| String| Single-line text (`text`)
`hs_utm_source`| UTM Source| String| Single-line text (`text`)
`hs_utm_content`| UTM Content| String| Single-line text (`text`)
`hs_utm_term`| UTM Term| String| Single-line text (`text`)
`hs_operating_system`| Operating system| String| Single-line text (`text`)
`hs_operating_version`| Operating version| String| Single-line text (`text`)
`hs_screen_height`| Screen height| Number| Number (`number`)
`hs_screen_width`| Screen width| Number| Number (`number`)
`hs_asset_description`| Asset description| String| Single-line text (`text`)
`hs_asset_type`| Asset type| String| Single-line text (`text`)
`hs_campaign_id`| Campaign ID| String| Single-line text (`text`)
`hs_device_name`| Device name| String| Single-line text (`text`)
`hs_touchpoint_source`| Touchpoint source| String| Single-line text (`text`)
`hs_tracking_name`| Tracking name| String| Single-line text (`text`)
`hs_parent_module_id`| Parent Module ID| String| Single-line text (`text`)

The following tables show the valid option values for enumeration event properties. Use the option’s internal name when [setting a value for the property via API](/docs/api-reference/legacy/events/send-event-data/guide#send-event-occurrence-data).

Show `hs_device_type` options

Option internal names| Option labels
---|---
`Game Console`| Game Console
`PDA`| PDA
`Personal Computer`| Personal Computer
`Desktop`| Desktop
`Smartphone`| Smartphone
`Smart TV`| Smart TV
`Tablet`| Tablet
`Wearable Computer`| Wearable Computer
`Unknown`| Unknown

Show `hs_page_content_type` options

Option internal names| Option labels
---|---
`BLOG_POST`| Blog Post
`KNOWLEDGE_ARTICLE`| Knowledge Article
`LANDING_PAGE`| Landing Page
`LISTING_PAGE`| Listing Page
`STANDARD_PAGE`| Standard Page
`WEB_INTERACTIVE`| Web Interactive

###

​

Define new properties

You can create up to 50 custom properties per custom event.

  * To create custom properties when defining a new custom event, include the `propertyDefinitions` array in your definition request body.
  * To create a new property for an existing custom event, make a `POST` request to `events/v3/event-definitions/{eventName}/property`.

Include the following fields to define each property.

Field| Description
---|---
`label` | The property’s human-readable name. The label can be up to 50 characters, but long labels may be cut off in certain parts of the HubSpot UI.
`name`| The property’s unique internal name, which you’ll use when sending event data through the API. The name can be up to 50 characters, must start with a letter, and can only contain lowercase letters, numbers, and underscores. If no value is provided, HubSpot will automatically generate one based on the label. Once defined, the `name` cannot be changed.
`type` | The type of property. Learn more about supported property types and formatting requirements for each.
`description`| Text to describe the property, displayed in the HubSpot UI.

The supported properties types are listed in the table below, with the formatting requirements for defining each type. Learn more about [property types and field types](/docs/api-reference/legacy/crm/properties/guide#property-type-and-fieldtype-values).

Type| Description| Stored field type
---|---|---
`bool`| Receives a boolean value. Values must be represented as `true` or `false`.| Radio select (`radio`)
`date`| Receives a date representing a specific day, month, and year. Values must be represented in UTC time and can be formatted as [ISO 8601 strings or UNIX-formatted timestamps at midnight in milliseconds](/docs/api-reference/legacy/crm/properties/guide#add-values-to-date-and-datetime-properties).| Date picker (`date`)
`datetime`| Receives a [UNIX timestamp in milliseconds or ISO8601 strings representing a timestamp](/docs/api-reference/legacy/crm/properties/guide#add-values-to-date-and-datetime-properties).| Date picker (`date`)
`enumeration`| Receives values from predefined options. When creating this property type, include an `options` array to set the available values. You must provide at least one option.| Dropdown select (`select`)
`number`| Receives numeric values with up to one decimal.| Number (`number`)
`string`| Receives plain text strings. If the property name contains the words `url`, `referrer`, or `link`, the property value can be up to 1,024 characters. Otherwise, property values can be up to 256 characters.| Single-line text (`text`)

For example, to define a new enumeration property for an existing custom event, your request body would look like:


    {
      "name": "property_name",
      "label": "Property name",
      "type": "enumeration",
      "options": [
        {
          "label": "label",
          "value": "value"
        }
      ]
    }


###

​

Update existing custom properties

To update an existing property on a custom event, make a `PATCH` request to `events/v3/event-definitions/{eventName}/property`. The only fields that can be updated on a property are the `label`, `description`, and `options` for enumeration properties.

To change the type of property, use the `DELETE` endpoint to delete the property and recreate it with the correct type.

###

​

Delete a property

To delete an existing property on a custom event, make a `DELETE` request to `events/v3/event-definitions/{eventName}/property/{propertyName}`. When a property is deleted, it will no longer be available for use in future event occurrences, but past occurrences will still have the property values.

##

​

Update an event’s label or description

To update an existing custom event schema, make a `PATCH` request to `events/v3/event-definitions/{eventName}`. You can only update the custom event’s values for `label` and `description`.


    {
      "label": "Event label",
      "description": "A description of the event"
    }


##

​

Delete an event definition

To delete a custom event schema, make a `DELETE` request to `events/v3/event-definitions/{eventName}`. Deleting a custom event will remove it from any other HubSpot tools that are referencing it, such as workflows and reports.

When deleting an event, note the following:

  1. All of the events for that event definition will be deleted and cannot be restored.
  2. Previously deleted `eventName`’s _cannot_ be used again.


##

​

Get existing event definitions

To fetch a single event definition, make a `GET` request to `events/v3/event-definitions/{eventName}`. To search event definitions by specific criteria, make a `GET` request to `events/v3/event-definitions`. You can use the following query parameters to refine your search.

Parameter| Description
---|---
`searchString`| Searches for events that contain the specified characters in the `name` field.
`after`| A hashed string provided in paged responses for viewing the next page of search results.
`limit`| The maximum number of results to return.
`includeProperties`| A boolean value that specifies whether to include event properties in the returned results.

##

​

Next steps

After you’ve defined a custom event, learn how to [send event occurrence data via the API](/docs/api-reference/legacy/events/send-event-data/guide).

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)