# Custom object records API guide

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/custom-objects/guide*

---

Custom Objects

# Custom object records API guide

HubSpot custom objects allow organizations to represent and organize data based on unique business requirements. Create and update custom object records with the custom objects API.

Supported products

Required Scopes

Once you’ve defined a custom object, use the objects API to create and manage the custom object’s records. Learn how to define custom objects with the [schemas API](/docs/api-reference/legacy/crm/objects/schemas/guide) or [within HubSpot](https://knowledge.hubspot.com/object-settings/create-custom-objects#create-a-custom-object).

##

​

Retrieve custom object records

You can retrieve custom object records individually or in batches. Use the objects API to retrieve all custom object records or retrieve specific custom object records by unique identifier values. To retrieve custom object records based on specific criteria, use the CRM search API.

###

​

Retrieve all custom object records or specific records by ID

  * To retrieve an individual custom object record, make a `GET` request to `/crm/v3/objects/{objectTypeId}/{recordId}`.
  * To request a list of all a custom object’s records, make a `GET` request to `/crm/v3/objects/{objectTypeId}`.
  * To retrieve a batch of specific custom object records by record ID or a [custom unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties), make a `POST` request to `/crm/v3/objects/{objectTypeId}/batch/read` and include the `id` values of records in the request body.

For these endpoints, you can include the following query parameters in the request URL:

Parameter| Description
---|---
`properties`| A comma-separated list of the properties to be returned in the response. If the requested record doesn’t have a value for a property, it will not appear in the response.
`propertiesWithHistory`| A comma separated list of the current and historical properties to be returned in the response. If the requested record doesn’t have a value for a property, it will not appear in the response.
`associations`| A comma-separated list of objects to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide) and [defining associations for custom objects with the schemas API.](/docs/api-reference/legacy/crm/objects/schemas/guide) **Note** : this parameter is _not_ supported in the batch read endpoint. Learn more about [batch reading associations with the associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide).
`idProperty`| Indicates the unique identifier property used to identify records. You only need to use this parameter if retrieving by a [custom unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties).

For example, for a custom object Cars (`objectTypeId`= `2-3465404`), to retrieve a car record with the owner’s name, make a `GET` request to `/crm/v3/objects/2-3465404/{carId}?properties=owner` and your response would look similar to the following:


    {
      "id": "65059681027",
      "properties": {
        "hs_createdate": "2024-11-20T20:12:09.236Z",
        "hs_lastmodifieddate": "2024-11-20T20:12:10.610Z",
        "owner": "John Smith",
        "hs_object_id": "65059681027"
      },
      "createdAt": "2024-11-20T20:12:09.236Z",
      "updatedAt": "2024-11-20T20:12:10.610Z",
      "archived": false
    }


To retrieve a batch of car records, your request could look like either of the following:


    {
      "properties": ["owner", "model"],
      "inputs": [
        {
          "id": "7891023"
        },
        {
          "id": "987654"
        }
      ]
    }


    {
      "properties": ["owner", "model"],
      "idProperty": "VIN",
      "inputs": [
        {
          "id": "3GTU2MEH7JG290400"
        },
        {
          "id": "1FDYF7TX8MD923255"
        }
      ]
    }


You can retrieve up to 100 custom object records in a batch request.

  * To retrieve a specific number of records under 100, add a value to the `limit` parameter. For example, you would use `?limit=50` to retrieve 50 records.
  * To retrieve additional records in subsequent requests (i.e., the records after the limit was reached in your request), include the `after` parameter with the `after` value returned from the previous request. This value is the Record ID of the next record. For example, `?after=123456`.

For example, to retrieve 50 car records, your request URL would be `GET` `/crm/v3/objects/2-3465404?limit=50`. In your response, under the `paging` object below the list of returned cars, the `after` value is the `id` of the next car that would’ve been returned. To request 50 more cars, starting with the next returned value, make a `GET` request to `/crm/v3/objects/2-3465404?limit=50&after={id}`. The `after` field is highlighted in the example response below:


    {
       "results":[
          {
             "id":"4388553737",
             "properties":{
                "hs_createdate":"2022-12-08T19:43:14.857Z",
                "hs_lastmodifieddate":"2024-08-06T14:50:43.773Z",
                "hs_object_id":"4388553737"
             },
             "createdAt":"2022-12-08T19:43:14.857Z",
             "updatedAt":"2024-08-06T14:50:43.773Z",
             "archived":false,
             "url":"https://app.hubspot.com/contacts/{HubID}/record/2-3465404/4388553737"
          },
          {
             "id":"5712789257",
             "properties":{
                "hs_createdate":"2023-03-27T18:47:16.490Z",
                "hs_lastmodifieddate":"2023-03-27T18:47:16.490Z",
                "hs_object_id":"5712789257"
             },
             "createdAt":"2023-03-27T18:47:16.490Z",
             "updatedAt":"2023-03-27T18:47:16.490Z",
             "archived":false,
             "url":"https://app.hubspot.com/contacts/{HubID}/record/2-3465404/5712789257"
          }
       ],
       "paging":{
          "next":{
             "after":"5712789258",
             "link":"https://api.hubapi.com/crm/v3/objects/2-3465404?limit=2&after=5712789258"
          }
       }
    }


###

​

Retrieve custom object records based on criteria

To include filters that retrieve custom object records based on specific criteria, use the [CRM search API](/docs/api-reference/legacy/crm/search-the-crm#filter-search-results). The `id` values of returned records can then be used to manage records via the objects API endpoints. For example, to retrieve all 2026 cars with a listing price over $50,000, you’d make a `POST` request to `/crm/v3/objects/2-3465404/search`, and your request would look like the following:


    {
        "filterGroups":[
          {
            "filters":[
              {
                "propertyName": "year",
                "operator": "EQ",
                "value": "2026"
              },
              {
                "propertyName": "price",
                "operator": "GT",
                "value": "50000"
              }
            ]
          }
        ]
      }


##

​

Create custom object records

  * To create a record for a custom object, make a `POST` request to `/crm/v3/objects/{objectTypeId}`.
  * To create multiple records, make a `POST` request to `/crm/v3/objects/{objectTypeId}/batch/create`.

In your request, include data for each record in a `properties` object. You can also add an `associations` object to associate your new record with existing records (e.g., companies, deals), or activities (e.g., meetings, notes).

If you want to create and update records at the same time, learn how to upsert records below.

###

​

Properties

Record details are stored in properties. To view all available properties for a custom object, you can retrieve a list of your account’s properties by making a `GET` request to `/crm/v3/properties/{objectTypeId}`. The [required properties](/docs/api-reference/legacy/crm/objects/custom-objects/guide#properties) for a custom object are specified in the object’s [schema](/docs/api-reference/legacy/crm/objects/schemas/guide). Learn more about the [properties API](/docs/api-reference/legacy/crm/properties/guide) and [how to format property values.](/docs/api-reference/legacy/crm/properties/guide#update-or-clear-a-property-s-values) For example, to create a new car record without associations, your request may look similar to the following:


    {
      "properties": {
        "VIN": "1FT8W3A68HEC69514",
        "year": "2026",
        "make": "BMW",
        "model": "X1",
        "price": "51000"
      }
    }


For example, to create multiple cars without associations, your request may look similar to the following:


    {
      "inputs": [
        {
          "properties": {
            "VIN": "1FT8W3A68HEC69514",
            "year": "2017",
            "make": "Ford",
            "model": "F-350 SD"
          }
        },
        {
          "properties": {
            "VIN": "19UNC1B07LY000049",
            "year": "2020",
            "make": "Acura",
            "model": "NSX"
          }
        }
      ]
    }


###

​

Associations

When creating a new custom object record, you can also associate it with [existing records](https://knowledge.hubspot.com/records/associate-records) or [activities](https://knowledge.hubspot.com/records/associate-activities-with-records) by including an `associations` object. For custom objects, you must [define the association type](/docs/api-reference/legacy/crm/objects/schemas/guide) with the desired object before associating their records. In the `associations` object, include the following:

Parameter| Description
---|---
`to`| The record or activity you want to associate with the custom object record, specified by its unique `id` value.
`types`| The type of the association between the custom object record and the record/activity. Include the `associationCategory` and `associationTypeId`. Retrieve the value for the custom object’s association types via the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide#retrieve-association-types).

For example, to create a new car and associate it with an existing contact and ticket, your request would look like the following:


    {
      "properties": {
        "VIN": "1FT8W3A68HEC69514",
        "year": "2017",
        "make": "Ford",
        "model": "F-350 SD"
      },
      "associations": [
        {
          "to": {
            "id": 123456
          },
          "types": [
            {
              "associationCategory": "USER_DEFINED",
              "associationTypeId": 1
            }
          ]
        },
        {
          "to": {
            "id": 556677
          },
          "types": [
            {
              "associationCategory": "USER_DEFINED",
              "associationTypeId": 13
            }
          ]
        }
      ]
    }


For example, to create multiple cars and associate them with existing deals and meetings, your request would look similar to the following:

For batch create actions, you can enable multi-status errors which tell you which records were successfully created and which were not. Learn more about [setting up multi-status error handling](/docs/api-reference/legacy/crm/using-object-apis#multi-status-errors-for-batch-create-requests).


    {
      "inputs": [
        {
          "associations": [
            {
              "types": [
                {
                  "associationCategory": "USER_DEFINED",
                  "associationTypeId": 6
                }
              ],
              "to": {
                "id": "23125848331"
              }
            },
            {
              "types": [
                {
                  "associationCategory": "HUBSPOT_DEFINED",
                  "associationTypeId": 21
                }
              ],
              "to": {
                "id": "65059681027"
              }
            }
          ],
          "properties": {
            "VIN": "1FT8W3A68HEC69514",
            "year": "2017",
            "make": "Ford",
            "model": "F-350 SD"
          }
        },
        {
          "associations": [
            {
              "types": [
                {
                  "associationCategory": "HUBSPOT_DEFINED",
                  "associationTypeId": 6
                }
              ],
              "to": {
                "id": "23125848331"
              }
            },
            {
              "types": [
                {
                  "associationCategory": "HUBSPOT_DEFINED",
                  "associationTypeId": 21
                }
              ],
              "to": {
                "id": "65059681027"
              }
            }
          ],
          "properties": {
            "VIN": "19UNC1B07LY000049",
            "year": "2020",
            "make": "Acura",
            "model": "NSX"
          }
        }
      ]
    }


##

​

Update custom object records

You can update custom object records individually or in batches. For existing records, the Record ID is a default [unique value](/docs/api-reference/legacy/crm/understanding-the-crm#unique-identifiers-and-record-ids) that you can use to update the record via API, but you can also identify records using the `idProperty` parameter with a [custom unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties). If you want to create and update records at the same time, learn how to upsert records.

  * To update an individual custom object record, make a `PATCH` request to `/crm/v3/objects/{objectTypeId}/{recordId}`, and include the data you want to update.
  * To update multiple custom object records, make a `POST` request to `/crm/v3/objects/{objectTypeId}/batch/update`. In the request body, include an array with the identifiers for the records and the properties you want to update.


If you’ve [merged records](https://knowledge.hubspot.com/records/merge-records), you can use the previous record ID values stored in the `hs_merged_object_ids` field to update a record using the basic update endpoint. However, these values are not supported when updating records using the batch update endpoint.

For example, to update a car, your request would look similar to the following:


    {
      "properties": {
        "price": "45000",
        "dealership": "Mountain Mazda"
      }
    }


##

​

Upsert records

You can also batch create and update custom object records at the same time using the upsert endpoint. For this endpoint, you can use a [custom unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties). Following the request, if the records already exist, they’ll be updated and if the records don’t exist, they’ll be created. To upsert records, make a `POST` request to `/crm/v3/objects/{objectTypeId}/batch/upsert`. In your request body, include the `idProperty` parameter to identify the unique identifier property you’re using. Include that property’s value as the `id` ​and add the other properties you want to set or update. For example, to upsert cars to set the `price` property using `VIN` as the identifier, your request would look similar to the following:


    {
      "inputs": [
        {
          "properties": {
            "price": "4000"
          },
          "id": "1D7HU18Z42S598204",
          "idProperty": "VIN"
        },
        {
          "properties": {
            "price": "50000"
          },
          "id": "1FDWF7DX3GDA03952",
          "idProperty": "VIN"
        },
        {
          "properties": {
            "price": "8000"
          },
          "id": "WA1JMDFE6AD006604",
          "idProperty": "VIN"
        }
      ]
    }


##

​

Update custom object record associations

Once custom object records are created, you can update their associations using the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide). For custom objects, you must [define the association type](/docs/api-reference/legacy/crm/objects/schemas/guide) with the desired object before you can associate their records.

  * To associate a custom object record with other records or an activity, make a `PUT` request to `/crm/v3/objects/{objectTypeId}/{fromRecordId}/associations/{toObjectTypeId}/{toRecordId}/{associationTypeId}`.
  * To remove an association between a custom object record and a record or activity, make a `DELETE` request to the following URL: `/crm/v3/objects/{objectTypeId}/{fromRecordId}/associations/{toObjectTypeId}/{toRecordId}/{associationTypeId}`.


To retrieve the `associationTypeId` values, make a `GET` request to `/crm/v4/associations/{fromObjectTypeId}/{toObjectTypeId}/labels`.

##

​

Pin an activity on a custom object record

You can [pin an activity](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a custom object record by including the `hs_pinned_engagement_id` field in your create, update, or upsert request. In the field, include the `id` of the activity to pin, which can be retrieved by making a `GET` request to `/crm/v3/objects/{objectTypeId}/{recordId}` for calls, communications, emails, meetings, notes, postal mail, or tasks. You can pin one activity per record, and the activity must already be associated with the record prior to pinning. For example, to set or update an existing car’s pinned activity, your request could look like:


    {
      "properties": {
        "hs_pinned_engagement_id": 123456789
      }
    }


To create a new car, associate it with an activity, and pin that activity, you request would look like:


    {
      "properties": {
        "VIN": "19UNC1B07LY000049",
        "year": "2020",
        "make": "Acura",
        "model": "NSX"
      },
      "associations": [
        {
          "to": {
            "id": 123456789
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 14
            }
          ]
        }
      ]
    }


##

​

Delete custom object records

You can delete custom object records individually or in batches, which will add the record to the recycling bin in HubSpot. You can [restore the record within HubSpot](https://knowledge.hubspot.com/records/restore-deleted-records) for up to 90 days after deletion.

  * To delete an individual custom object record by its record ID, make a `DELETE` request to `/crm/v3/objects/{objectTypeId}/{recordId}`.
  * To delete multiple custom object records, make a `POST` request to `/crm/v3/objects/{objectTypeId}/batch/archive` and include the record ID values as the `id` inputs in your request body.

For example, to delete multiple cars, your request would look like:


    {
      "inputs": [
        {
          "id": "123456"
        },
        {
          "id": "7891011"
        },
        {
          "id": "12123434"
        }
      ]
    }


##

​

Limits

Object API batch endpoints are limited to 100 inputs per request. For example, create or retrieve up to 100 cars per request.

Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)