# Account | Users API

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/users/guide*

---

Users

# Account | Users API

A user object stores information such as a user’s working hours, timezone, additional phone number, and job title. The user endpoints allow you to manage this data and sync it between HubSpot and other systems.

Scope requirements

Use this API to fetch information about users in the account, along with updating their working hours, timezone, additional phone number, and job title properties. This API can be especially useful for syncing HubSpot user data with external workforce management tools. For example, use these endpoints keep a user’s working hours in sync with an external scheduling system. Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs/guides/crm/understanding-the-crm) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](https://knowledge.hubspot.com/get-started/manage-your-crm-database).

##

​

Retrieve users

Depending on the information you need, there are a few ways to retrieve HubSpot users:

  * To retrieve all users, make a `GET` request to `/crm/objects/2026-03/users/`.
  * To retrieve a specific user, make a `GET` request to the above URL and specify a user ID. For example: `crm/objects/2026-03/users/207838823235`.
  * To retrieve a batch of users by ID, make a `POST` request to `/crm/objects/2026-03/users/batch/read`.
  * To retrieve users that meet a specific set of criteria, you can make a `POST` request to `/crm/objects/2026-03/users/search` and include search filters in the request body. Learn more about [searching the CRM](/docs/api-reference/latest/crm/search-the-crm).


**Please note:** In a response for the users API, `id` and `hs_object_id` are the same and represent a user _only_ in the HubSpot account from which the data was requested. This is different than the `id` values in the [user provisioning API](/docs/api-reference/latest/account/settings/user-provisioning/guide) (`hs_internal_user_id`) which refers to a user across all accounts, and in the [owners API](/docs/api-reference/latest/crm/owners/guide) (`hubspot_owner_id`) which refers to a user as an owner of records.

For example, the following response returns users, their unique identifiers within the selected HubSpot account, and information about when they were created or modified:


    {
      "results": [
        {
          "id": "207838823235",
          "properties": {
            "hs_createdate": "2021-01-10T20:36:06.761Z",
            "hs_lastmodifieddate": "2023-08-29T18:17:55.697Z",
            "hs_object_id": "207838823235"
          },
          "createdAt": "2021-01-10T20:36:06.761Z",
          "updatedAt": "2023-08-29T18:17:55.697Z",
          "archived": false
        },
        {
          "id": "207840253600",
          "properties": {
            "hs_createdate": "2017-12-22T12:22:12.212Z",
            "hs_lastmodifieddate": "2023-08-29T18:17:55.697Z",
            "hs_object_id": "207840253600"
          },
          "createdAt": "2017-12-22T12:22:12.212Z",
          "updatedAt": "2023-08-29T18:17:55.697Z",
          "archived": false
        }
      ]
    }


To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. Learn more about user properties below. For example, making a `GET` request to the following URL would result in the response below: `crm/objects/2026-03/users?properties=hs_job_title,hs_additional_phone`


    {
      "results": [
        {
          "id": "207838823235",
          "properties": {
            "hs_additional_phone": "+1123456780",
            "hs_createdate": "2021-01-10T20:36:06.761Z",
            "hs_job_title": "CEO",
            "hs_lastmodifieddate": "2023-08-29T18:17:55.697Z",
            "hs_object_id": "207838823235"
          },
          "createdAt": "2021-01-10T20:36:06.761Z",
          "updatedAt": "2023-08-29T18:17:55.697Z",
          "archived": false
        },
        {
          "id": "207840253600",
          "properties": {
            "hs_additional_phone": "+1238675309",
            "hs_createdate": "2021-01-10T20:36:06.761Z",
            "hs_job_title": "Vice President",
            "hs_lastmodifieddate": "2023-08-29T18:17:55.697Z",
            "hs_object_id": "207838823235"
          },
          "createdAt": "2017-12-22T12:22:12.212Z",
          "updatedAt": "2023-08-29T18:17:55.697Z",
          "archived": false
        }
      ]
    }


For the batch read endpoint, you can either retrieve users by their ID or by another [unique identifier property](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties) by including an `idProperty` field. For example, to read a batch of users, your request could look like either of the following:


    {
      "properties": ["hs_job_title", "hs_additional_phone"],
      "inputs": [
        {
          "id": "207838823235"
        },
        {
          "id": "207840253600"
        }
      ]
    }


    {
      "properties": ["hs_job_title", "hs_additional_phone"],
      "idProperty": "externalIdProperty",
      "inputs": [
        {
          "id": "0001111"
        },
        {
          "id": "0001112"
        }
      ]
    }


##

​

Update users

You can update users by ID individually or in batches.

  * To update an individual user, make a `PATCH` request to `/crm/objects/2026-03/users/{userId}`.
  * To update a batch of users, make a `POST` request to `/crm/objects/2026-03/users/batch/update`, including the user IDs or unique `idProperty` in the request body as shown in the section above.

For each endpoint, you’ll need to include a request body that contains the properties you want to update. For example, the request body below would update a user’s timezone and working hours:


    {
      "properties": {
        "hs_standard_time_zone": "America/Detroit",
        "hs_working_hours": "[{\"days\":\"SATURDAY\",\"startMinute\":540,\"endMinute\":1020},{\"days\":\"WEDNESDAY\",\"startMinute\":540,\"endMinute\":1020}]"
      }
    }


Only some properties can be set through this API. See the properties section below for a list of the available propeties.

##

​

User properties

To retrieve a list of all available user properties, you can use the properties API by making a `GET` request to `crm/properties/2026-03/user`. Learn more about using the [properties API](/docs/api-reference/latest/crm/properties/guide). Below are the user properties that can be set through this API.

Parameter| Type| Description
---|---|---
`hs_additional_phone`| String| The user’s additional phone number. Users can set this in their [user preferences](https://knowledge.hubspot.com/user-management/manage-user-properties-and-preferences#set-user-preferences).
`hs_availability_status`| String| The user’s availability status. The value must be either `"available"` or `"away"`.
`hs_job_title`| String| The user’s job title. Users can set this in their [user preferences](https://knowledge.hubspot.com/user-management/manage-user-properties-and-preferences#set-user-preferences).
`hs_main_user_language_skill`| String| The user’s main language skill. The value must match an existing language skill. Learn more about formatting language skills below.
`hs_out_of_office_hours`| String| The user’s out of office hours. Out of office hours must not overlap. Each out of office hours’ start time must be later than the previous start time.
`hs_secondary_user_language_skill`| String| The user’s secondary language skill. The value must match an existing language skill. Learn more about formatting language skills below.
`hs_standard_time_zone`| String| The user’s timezone. Timezone values must use standard [TZ identifiers](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), such as `"America/New_York"` or `"Europe/Dublin"`. This property must be set before you can set the user’s working hours.
`hs_uncategorized_skills`| String| The user’s custom uncategorized skill. This property value must match an existing custom uncatgorized skill in the portal.
`hs_working_hours`| String| The user’s working hours. This property value is formatted as stringified JSON. Learn more about formatting for working hours below.

###

​

Working hours

`hs_working_hours` accepts a stringified JSON value. It consists of an array with an object for each set of working hours.


    "[{\"days\":\"VALUE\",\"startMinute\":number,\"endMinute\":number}]"


Parameter| Type| Description
---|---|---
`days`| Stringified JSON| The days included in a set of working hours. Values include:

  * `MONDAY_TO_FRIDAY`
  * `SATURDAY_SUNDAY`
  * `EVERY_DAY`
  * `MONDAY`
  * `TUESDAY`
  * `WEDNESDAY`
  * `THURSDAY`
  * `FRIDAY`
  * `SATURDAY`
  * `SUNDAY`


`startMinute`| Number| Working hours start time in minutes. Must be within the range of `0` \- `1440`, where `0` represents 12:00AM midnight. For example, a 9:00AM start time would be represented as `540`.
`endMinute`| Number| Working hours end time in minutes. Follows the same rules as `startMinute`.For example, 5:00PM is represented as `1020`.

**Please note:**

  * The `hs_standard_time_zone` property must be set before you can set working hours.
  * Working hours cannot overlap.


For example, if a user works Monday through Friday, 9:00AM to 5:00PM, you would format that as follows:


    "[{\"days\":\"MONDAY_TO_FRIDAY\",\"startMinute\":540,\"endMinute\":1020}]"


If a user works Monday 9:00AM to 5:00PM and Saturday 11:00AM to 2:00PM, the array would contain an object to represent each set of working hours:


    "[{\"days\":\"MONDAY\",\"startMinute\":540,\"endMinute\":1020},{\"days\":\"SATURDAY\",\"startMinute\":660,\"endMinute\":840}]"


###

​

Out of office hours

If a user will be unavailable due to scheduled time off, you can set any periods during which they’ll be out of office using the `hs_out_of_office_hours` property:

  * The property accepts an array of date ranges, each specified by a `startTimestamp` and `endTimestamp`.
  * The date ranges cannot overlap with one another, and the `startTimestamp` of each date range must be later than the previous `startTimestamp`.

For example, if you wanted to specify out-of-office hours during October 31st 2024 9:00 AM to 5:00 PM and November 28 2024 9:00 AM to 5:00 PM, you’d specify the following value for the `hs_out_of_office_hours` property for a user:


    "[{\"startTimestamp\": 17303796000,\"endTimestamp\": 17304084000},{\"startTimestamp\": 17328024000,\"endTimestamp\": 17328312000}]"


###

​

Language skills

`hs_main_user_language_skill` or `hs_secondary_user_language_skill` must match an existing language skill. The following JSON array lists all valid options for language skill categories:


    [
      {
        "label": "Dansk",
        "value": "da"
      },
      {
        "label": "Deutsch",
        "value": "de"
      },
      {
        "label": "English",
        "value": "en"
      },
      {
        "label": "Español",
        "value": "es"
      },
      {
        "label": "Français",
        "value": "fr"
      },
      {
        "label": "Italiano",
        "value": "it"
      },
      {
        "label": "Nederlands",
        "value": "nl"
      },
      {
        "label": "Norsk",
        "value": "no"
      },
      {
        "label": "Polski",
        "value": "pl"
      },
      {
        "label": "Português",
        "value": "ptbr"
      },
      {
        "label": "Suomi",
        "value": "fi"
      },
      {
        "label": "Svenska",
        "value": "sv"
      },
      {
        "label": "中文 - 繁體",
        "value": "zhtw"
      },
      {
        "label": "日本語",
        "value": "ja"
      }
    ]


Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)