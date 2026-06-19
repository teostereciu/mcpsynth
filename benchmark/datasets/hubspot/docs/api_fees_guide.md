# CRM API | Fees

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/fees/guide*

---

Fees

# CRM API | Fees

Learn how you can create and manage fees that can be included in invoices and legacy quotes.

Scope requirements

Use the fees API to create and manage fees that can be included in [invoices](/docs/api-reference/legacy/crm/objects/invoices/guide) and [legacy quotes](/docs/api-reference/legacy/crm/objects/quotes/guide). Fees are used in conjunction with [discounts](/docs/api-reference/legacy/crm/objects/discounts/guide) and [taxes](/docs/api-reference/legacy/crm/objects/taxes/guide) when determining the pricing totals. Any discounts you associate with your quote will be applied first, followed by associated fees, then any associated taxes.

Currently, fees cannot be associated with [CPQ quotes](/docs/guides/crm/create-cpq-quotes).

##

​

Create fees

Fees can be created individually or in batches:

  * To create one fee, make a `POST` request to `/crm/v3/objects/fees`.
  * To create multiple fees, make a `POST` request to `/crm/v3/objects/fees/batch/create`.

In the request body, include your fee data in a `properties` object. You can also add an `associations` object to associate the fee with existing objects (e.g., invoices, quotes).

For batch create actions, you can enable multi-status errors which tell you which records were successfully created and which were not. Learn more about [setting up multi-status error handling](/docs/api-reference/error-handling#multi-status-errors).

###

​

Create fees with property values

When creating a fee, you must include a set of fee properties to store the fee’s details. For example, to create a new fee, your request may look similar to the following:


    {
      "properties": {
        "hs_label": "Processing fee",
        "hs_type": "FIXED",
        "hs_value": "25"
      }
    }


The following properties are required when creating a fee:

Parameter| Type| Description
---|---|---
`hs_label` | String| The label of the fee, displayed in HubSpot.
`hs_type` | String| The type of the fee (either `PERCENT` or `FIXED`).
`hs_value` | Number| The value of the fee. For a percentage-based fee, the value should be a number between `0` and `100`. For a fixed fee, the value should be a number.

For example, the following request body would create a 10% fee:


    {
      "properties": {
        "hs_label": "A percentage-based fee of 10%",
        "hs_type": "PERCENT",
        "hs_value": "10"
      }
    }


The response will include the created fee with its ID and properties.


    {
      "id": "512",
      "properties": {
        "hs_label": "A percentage-based fee of 10%",
        "hs_type": "PERCENT",
        "hs_value": "10",
        "hs_createdate": "2024-04-11T20:42:01.734Z",
        "hs_lastmodifieddate": "2024-04-11T20:42:01.734Z",
        "hs_object_id": "512"
      },
      "createdAt": "2024-04-11T20:42:01.734Z",
      "updatedAt": "2024-04-11T20:42:01.734Z",
      "archived": false
    }


###

​

Create fees with associations

To associate a fee with another object at the time of creation, you can include an `associations` array in the request body. In the `associations` array, include an object for each association you want to create, which will specify the type of object you want to associate the fee with and the type of association. You can also associate fees with other objects at a later time by updating the fee’s associations. The following request body would create a fee and associate it with a quote (ID of `123456`):


    {
      "properties": {
        "hs_label": "Flat processing fee",
        "hs_type": "FIXED",
        "hs_value": "25"
      },
      "associations": [
        {
          "to": {
            "id": "123456"
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 363
            }
          ]
        }
      ]
    }


Parameter| Type| Description
---|---|---
`to` | Object| The object you want to associate the fee with, specified by its ID.
`types` | Array| The type of association between the fee and the object. This array contains the following fields: `associationCategory` (the [type of association](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values), either `HUBSPOT_DEFINED` or `USER_DEFINED`) and `associationTypeId` (a unique identifier to indicate the association type between the fee and the other object).

###

​

Create a batch of fees

To create multiple fees with one request, make a `POST` request to `/crm/v3/objects/fees/batch/create`. In the request body, include an `inputs` array with each fee’s properties and associations. For example, the following request body would batch create two fees, one fixed fee of $25 and one percentage-based fee of 5%:


    {
      "inputs": [
        {
          "properties": {
            "hs_label": "Processing fee",
            "hs_type": "FIXED",
            "hs_value": "25"
          },
          "associations": []
        },
        {
          "properties": {
            "hs_label": "Service fee",
            "hs_type": "PERCENT",
            "hs_value": "5"
          },
          "associations": []
        }
      ]
    }


The response will include all created fees:


    {
      "status": "COMPLETE",
      "results": [
        {
          "id": "513",
          "properties": {
            "hs_label": "Processing fee",
            "hs_type": "FIXED",
            "hs_value": "25",
            "hs_createdate": "2024-04-11T20:42:01.734Z",
            "hs_lastmodifieddate": "2024-04-11T20:42:01.734Z",
            "hs_object_id": "513"
          },
          "createdAt": "2024-04-11T20:42:01.734Z",
          "updatedAt": "2024-04-11T20:42:01.734Z",
          "archived": false
        },
        {
          "id": "514",
          "properties": {
            "hs_label": "Service fee",
            "hs_type": "PERCENT",
            "hs_value": "5",
            "hs_createdate": "2024-04-11T20:42:01.734Z",
            "hs_lastmodifieddate": "2024-04-11T20:42:01.734Z",
            "hs_object_id": "514"
          },
          "createdAt": "2024-04-11T20:42:01.734Z",
          "updatedAt": "2024-04-11T20:42:01.734Z",
          "archived": false
        }
      ],
      "startedAt": "2024-04-11T20:42:01.500Z",
      "completedAt": "2024-04-11T20:42:01.900Z"
    }


##

​

Retrieve fees

The fees API provides endpoints for retrieving individual fees, all fees, and batches of fees. You can also search for fees that meet a specific set of criteria. When retrieving fees, you can include the parameters below in the request. When retrieving all fees or individual fees, include them as query parameters in the request URL. When retrieving batches of fees, include them in the request body.

Parameter| Description
---|---
`properties`| A comma separated list of the properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a fee doesn’t have a value, it will be returned as `null`.
`propertiesWithHistory`| A comma separated list of the current and historical properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a fee doesn’t have a value, it will be returned as `null`.
`associations`| A comma separated list of objects to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API.](/docs/api-reference/legacy/crm/associations/associate-records/guide)

###

​

Retrieve a single fee

To retrieve an individual fee, make a `GET` request to `/crm/v3/objects/fees/{feeId}`, where `{feeId}` is the ID of the fee you want to retrieve. The response will include a set of default properties, including the create date and last modified date.


    {
      "id": "512",
      "properties": {
        "hs_createdate": "2024-04-10T18:59:32.441Z",
        "hs_lastmodifieddate": "2024-04-10T18:59:32.441Z",
        "hs_object_id": "512"
      },
      "createdAt": "2024-04-10T18:59:32.441Z",
      "updatedAt": "2024-04-10T18:59:32.441Z",
      "archived": false
    }


To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example: `/crm/v3/objects/fees/512?properties=hs_label,hs_type,hs_value`


    {
      "id": "512",
      "properties": {
        "hs_createdate": "2024-04-10T18:59:32.441Z",
        "hs_label": "Processing fee",
        "hs_lastmodifieddate": "2024-04-10T18:59:32.441Z",
        "hs_object_id": "512",
        "hs_type": "FIXED",
        "hs_value": "25"
      },
      "createdAt": "2024-04-10T18:59:32.441Z",
      "updatedAt": "2024-04-10T18:59:32.441Z",
      "archived": false
    }


###

​

Retrieve all fees

To retrieve all fees, make a `GET` request to `/crm/v3/objects/fees`. You can retrieve up to 100 fees in one request.

  * To retrieve a specific amount under 100, add a value to the `limit` parameter (e.g., `?limit=50`).
  * To retrieve additional fees in subsequent requests (i.e. the fees after the limit was reached in your request), include the `after` parameter with the `after` value returned from the previous request (e.g., `?after=123456`).

For example, to retrieve 50 fees, your request URL would be `GET` `/crm/v3/objects/fees?limit=50`. In your response, under the `paging` object below the list of returned fees, the `after` value is the `id` of the next fee that would’ve been returned. To request 50 more fees, starting with the next returned value, make a `GET` request to `/crm/v3/objects/fees?limit=50&after={id}`.


    {
      "results": [
        {
          "id": "42037508740",
          "properties": {
            "hs_createdate": "2022-11-03T14:24:02.602Z",
            "hs_lastmodifieddate": "2022-11-03T14:24:02.602Z",
            "hs_object_id": "42037508740"
          },
          "createdAt": "2022-11-03T14:24:02.602Z",
          "updatedAt": "2022-11-03T14:24:02.602Z",
          "archived": false
        }
      ],
      "paging": {
        "next": {
          "after": "33452",
          "link": "https://api.hubspot.com/crm/v3/objects/fees/?limit=1&after=33452"
        }
      }
    }


###

​

Retrieve a batch of fees

To retrieve multiple fees by their IDs, make a `POST` request to `/crm/v3/objects/fees/batch/read`. In the request body, include the IDs of the fees you want to retrieve along with the properties you want returned:


    {
      "inputs": [
        { "id": "512" },
        { "id": "513" }
      ],
      "properties": ["hs_label", "hs_type", "hs_value"],
      "propertiesWithHistory": []
    }


###

​

Search for fees

You can use the search endpoint to retrieve fees that meet a specific set of [filter criteria](/docs/api-reference/legacy/crm/search-the-crm#filter-search-results). Make a `POST` request to `/crm/v3/objects/fees/search` and include your filter criteria in the request body. For example, to search for all percentage-based fees:


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "hs_type",
              "value": "PERCENT",
              "operator": "EQ"
            }
          ]
        }
      ],
      "properties": ["hs_label", "hs_type", "hs_value"]
    }


The response will include matching fees and the total count:


    {
      "total": 2,
      "results": [
        {
          "id": "512",
          "properties": {
            "hs_createdate": "2024-04-10T18:59:32.441Z",
            "hs_label": "Service fee",
            "hs_lastmodifieddate": "2024-04-10T18:59:32.441Z",
            "hs_object_id": "512",
            "hs_type": "PERCENT",
            "hs_value": "5"
          },
          "createdAt": "2024-04-10T18:59:32.441Z",
          "updatedAt": "2024-04-10T18:59:32.441Z",
          "archived": false
        }
      ]
    }


##

​

Update fees

You can update fees individually or in batches.

###

​

Update a single fee

To update an individual fee, make a `PATCH` request to `/crm/v3/objects/fees/{feeId}`. In the request body, include a `properties` object containing the properties that you want to update. Note that you cannot update the fee’s associations using this endpoint. Instead, you’ll need to use the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide#associate-records) to update the fee’s associations. For example, to update a fee’s value:


    {
      "properties": {
        "hs_value": "15"
      }
    }


The response will include a set of default properties along with the property that you updated:


    {
      "id": "512",
      "properties": {
        "hs_createdate": "2024-04-11T20:42:01.734Z",
        "hs_label": "A percentage-based fee of 10%",
        "hs_lastmodifieddate": "2024-04-11T21:00:00.234Z",
        "hs_object_id": "512",
        "hs_type": "PERCENT",
        "hs_value": "15"
      },
      "createdAt": "2024-04-11T20:42:01.734Z",
      "updatedAt": "2024-04-11T21:00:00.234Z",
      "archived": false
    }


###

​

Update a batch of fees

To update multiple fees at once, make a `POST` request to `/crm/v3/objects/fees/batch/update`. In the request body, include an `inputs` array with the ID and updated properties for each fee:


    {
      "inputs": [
        {
          "id": "512",
          "properties": {
            "hs_value": "12"
          }
        },
        {
          "id": "513",
          "properties": {
            "hs_label": "Updated processing fee",
            "hs_value": "30"
          }
        }
      ]
    }


The response will include all updated fees:


    {
      "status": "COMPLETE",
      "results": [
        {
          "id": "512",
          "properties": {
            "hs_label": "A percentage-based fee of 10%",
            "hs_type": "PERCENT",
            "hs_value": "12",
            "hs_createdate": "2024-04-11T20:42:01.734Z",
            "hs_lastmodifieddate": "2024-04-11T21:05:00.234Z",
            "hs_object_id": "512"
          },
          "createdAt": "2024-04-11T20:42:01.734Z",
          "updatedAt": "2024-04-11T21:05:00.234Z",
          "archived": false
        },
        {
          "id": "513",
          "properties": {
            "hs_label": "Updated processing fee",
            "hs_type": "FIXED",
            "hs_value": "30",
            "hs_createdate": "2024-04-11T20:42:01.734Z",
            "hs_lastmodifieddate": "2024-04-11T21:05:00.234Z",
            "hs_object_id": "513"
          },
          "createdAt": "2024-04-11T20:42:01.734Z",
          "updatedAt": "2024-04-11T21:05:00.234Z",
          "archived": false
        }
      ],
      "startedAt": "2024-04-11T21:05:00.000Z",
      "completedAt": "2024-04-11T21:05:00.500Z"
    }


##

​

Associate existing fees

To associate an existing fee with other objects, you can set the association via the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide#associate-records) by making a `PUT` request to: `/crm/v4/objects/fees/{feeId}/associations/default/{toObjectType}/{toObjectId}/`

Parameter| Description
---|---
`feeId`| The ID of the fee you want to associate.
`toObjectType`| The type of object that you want to associate the fee with (e.g., quote).
`toObjectId`| The ID of the individual object that you want to associate the fee with.

For example, if you wanted to associate a fee with a specific quote, your request URL would look like the following: `/crm/v4/objects/fees/8675309/associations/default/quote/123456` The response will return the details of the association, including the association details of each direction (quote-to-fee and fee-to-quote).


    {
      "completedAt": "2026-01-07T19:12:31.789Z",
      "status": "COMPLETE",
      "startedAt": "2026-01-07T19:12:31.695Z",
      "results": [
        {
          "from": {
            "id": "8675309"
          },
          "to": {
            "id": "123456"
          },
          "associationSpec": {
            "associationCategory": "HUBSPOT_DEFINED",
            "associationTypeId": 363
          }
        },
        {
          "from": {
            "id": "123456"
          },
          "to": {
            "id": "8675309"
          },
          "associationSpec": {
            "associationCategory": "HUBSPOT_DEFINED",
            "associationTypeId": 364
          }
        }
      ]
    }


###

​

Remove an association

To remove an association between a fee and another object, make a `DELETE` request to `/crm/v3/objects/fees/{feeId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. To retrieve the `associationTypeId` value, refer to [this list](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values) of default values, or make a `GET` request to /crm/v4/associations///labels.

Parameter| Description
---|---
`feeId`| The ID of the fee you want to remove the association from.
`toObjectType`| The type of object that you want to remove the association from (e.g., quote).
`toObjectId`| The ID of the individual object that you want to remove the association from.
`associationTypeId`| The ID of the association type you want to remove.

##

​

Delete fees

To delete a fee, make a `DELETE` request to `/crm/v3/objects/fees/{feeId}`. A successful request returns a `204` response with no body.

###

​

Delete a batch of fees

To delete multiple fees with one request, make a `POST` request to `/crm/v3/objects/fees/batch/archive`. In the request body, include an `inputs` array with the IDs of the fees you want to delete:


    {
      "inputs": [
        { "id": "512" },
        { "id": "513" }
      ]
    }


A successful request returns a `204` response with no body.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)