# Using Object APIs

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/using-object-apis*

---

CRM

# Using Object APIs

Learn how to use the object API endpoints to create and manage records or activities.

Using the object APIs, you can create and manage records and activities within HubSpot. The object APIs have the same basic functionality for all supported objects, so you can substitute the `objectTypeId` in the endpoints to work with different objects. For example, to create contacts, you’d make a `POST` request to `crm/objects/2026-03/0-1` and to create courses, the request would be to `crm/objects/2026-03/0-410`.

Some objects have limited API functionality. For more details, click the link to an object’s endpoints reference documentation in the table below. If an object listed doesn’t have its own guide, you can refer to the [objects API](/docs/apps/developer-platform/add-features/app-objects/overview#overview-of-app-objects) guide and substitute the `{objectTypeId}` in each endpoint to your desired object.

Expand the section below to view objects and their [object type ID](/docs/guides/crm/understanding-the-crm#object-type-ids) values.

Object type ID values

Object| Type ID
---|---
Appointments| `0-421`
[Calls](/docs/api-reference/latest/crm/activities/calls/guide)| `0-48`
[Carts](/docs/api-reference/latest/crm/objects/carts/guide)| `0-142`
[Communications](/docs/api-reference/latest/crm/objects/communications/guide)| `0-18`
[Companies](/docs/api-reference/latest/crm/objects/companies/guide)| `0-2`
[Contacts](/docs/api-reference/latest/crm/objects/contacts/guide)| `0-1`
Courses| `0-410`
[Custom objects](/docs/api-reference/latest/crm/objects/custom-objects/guide)| `2-XXX`
[Deals](/docs/api-reference/latest/crm/objects/deals/guide)| `0-3`
[Discounts](/docs/api-reference/latest/crm/objects/discounts/guide)| `0-84`
[Emails](/docs/api-reference/latest/crm/activities/emails/guide)| `0-49`
[Feedback submissions](/docs/api-reference/latest/crm/objects/feedback-submissions/guide)| `0-19`
[Fees](/docs/api-reference/latest/crm/objects/fees/guide)| `0-85`
[Goals](/docs/api-reference/latest/crm/objects/goals/guide)| `0-74`
[Invoices](/docs/api-reference/latest/crm/objects/invoices/guide)| `0-53`
[Leads](/docs/api-reference/latest/crm/objects/leads/guide)| `0-136`
[Line items](/docs/api-reference/latest/crm/objects/line-items/guide)| `0-8`
Listings| `0-420`
[Marketing events](/docs/api-reference/latest/marketing/marketing-events/guide)| `0-54`
[Meetings](/docs/api-reference/latest/crm/activities/meetings/guide)| `0-47`
[Notes](/docs/api-reference/latest/crm/activities/notes/guide)| `0-46`
[Orders](/docs/api-reference/latest/crm/objects/orders/guide)| `0-123`
[Payments](/docs/api-reference/latest/crm/objects/commerce-payments/guide)| `0-101`
[Postal mail](/docs/api-reference/latest/crm/activities/postal-mail/guide)| `0-116`
[Products](/docs/api-reference/latest/crm/objects/products/guide)| `0-7`
[Projects](/docs/guides/account/projects/guide)| `0-970`
[Quotes](/docs/api-reference/latest/crm/objects/quotes/guide)| `0-14`
Services| `0-162`
[Subscriptions](/docs/api-reference/latest/crm/objects/commerce-subscriptions/guide)| `0-69`
[Tasks](/docs/api-reference/latest/crm/activities/tasks/guide)| `0-27`
[Taxes](/docs/api-reference/latest/crm/objects/taxes/guide)| `0-86`
[Tickets](/docs/api-reference/latest/crm/objects/tickets/guide)| `0-5`
[Users](/docs/api-reference/latest/crm/objects/users/guide)| `0-115`

In this article, learn the basics of how to use the object APIs.

New objects (e.g., appointments, courses, listings, services) must be activated in the HubSpot account before you can manage their records via API. Learn how to check if they’re activated via the [object library API](/docs/api-reference/latest/crm/objects/object-library/guide) and [how to activate them in HubSpot](https://knowledge.hubspot.com/data-management/data-model-templates#view-the-object-library).

##

​

Retrieve records

You can retrieve records individually or in batches. You can use the objects API to retrieve all records of an object or retrieve specific records by unique identifier values. To retrieve records based on specific criteria, use the CRM search API.

###

​

Retrieve all records or specific records by ID

  * To retrieve an individual record, make a `GET` request to `/crm/objects/2026-03/{objectTypeId}/{recordId}`.
  * To request a list of all records for an object, make a `GET` request to `/crm/objects/2026-03/{objectTypeId}`.
  * To retrieve a batch of specific records by record ID or a [custom unique identifier property](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties), make a `POST` request to `crm/objects/2026-03/{objectTypeId}/batch/read` and include the `id` values of records in the request body.


Although the batch endpoint only retrieves records, it requires the `POST` method because batch requests send up to 100 record IDs in the request body. Using the `POST` method avoids the URL length limits that are applied to `GET` requests.

For these endpoints, you can include the following query parameters in the request URL:

Parameter| Description
---|---
`properties`| A comma separated list of the properties to be returned in the response. If the requested record doesn’t have a value for a property, it will not appear in the response.
`propertiesWithHistory`| A comma separated list of the current and historical properties to be returned in the response. If the requested record doesn’t have a value for a property, it will not appear in the response.
`associations`| A comma-separated list of objects to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API.](/docs/api-reference/latest/crm/associations/associate-records/guide) **Note** : this parameter is _not_ supported in the batch read endpoint. Learn more about [batch reading associations with the associations API](/docs/api-reference/latest/crm/associations/associate-records/guide).
`idProperty`| Indicates the unique identifier property used to identify records. You only need to use this parameter if retrieving by a [custom unique identifier property](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties).

For example, to retrieve a meeting with the meeting’s text body and starting time, you’d make a `GET` request to `/crm/objects/2026-03/0-47/{meetingId}?properties=hs_meeting_body,hs_timestamp` and your response would look similar to the following:


    {
      "id": "65059681027",
      "properties": {
        "hs_createdate": "2024-11-20T20:12:09.236Z",
        "hs_lastmodifieddate": "2024-11-20T20:12:10.610Z",
        "hs_meeting_body": "<div style=\"\" dir=\"auto\" data-top-level=\"true\"><p style=\"margin:0;\">New meeting</p></div>",
        "hs_object_id": "65059681027",
        "hs_timestamp": "2024-11-20T20:12:03.054Z"
      },
      "createdAt": "2024-11-20T20:12:09.236Z",
      "updatedAt": "2024-11-20T20:12:10.610Z",
      "archived": false
    }


To retrieve a batch of deals, your request could look like either of the following:


    {
      "properties": ["dealname", "dealstage", "pipeline"],
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
      "properties": ["dealname", "dealstage", "pipeline"],
      "idProperty": "uniqueordernumber",
      "inputs": [
        {
          "id": "0001111"
        },
        {
          "id": "0001112"
        }
      ]
    }


You can retrieve up to 100 records in a batch request.

  * To retrieve a specific number of records under 100, add a value to the `limit` parameter. For example, you would use `?limit=50` to retrieve 50 records.
  * To retrieve additional records in subsequent requests (i.e. the records after the limit was reached in your request), include the `after` parameter with the `after` value returned from the previous request. This value is the Record ID of the next record. For example, `?after=123456`.

For example, to retrieve 50 listings, your request URL would be `GET` `/crm/objects/2026-03/0-420?limit=50`. In your response, under the `paging` object below the list of returned listings, the `after` value is the `id` of the next listing that would’ve been returned. To request 50 more listings, starting with the next returned value, make a `GET` request to `/crm/objects/2026-03/0-420?limit=50&after={id}`. The `after` field is highlighted in the example response below:


    {
      "results": [
        {
          "id": "513881705057",
          "properties": {
            "hs_createdate": "2025-12-22T18:16:33.376Z",
            "hs_lastmodifieddate": "2025-12-22T18:16:33.376Z",
            "hs_object_id": "513881705057"
          },
          "createdAt": "2025-12-22T18:16:33.376Z",
          "updatedAt": "2025-12-22T18:16:33.376Z",
          "archived": false,
          "url": "https://app.hubspot.com/contacts/{HubId}/record/0-420/513881705057"
        }
      ],
      "paging": {
        "next": {
          "after": "513881705058",
          "link": "https://api.hubapi.com/crm/objects/v3/0-420?limit=1&after=513881705058"
        }
      }
    }


###

​

Retrieve records based on criteria

To include filters that retrieve records based on specific criteria, use the [CRM search API](/docs/api-reference/latest/crm/search-the-crm#filter-search-results). The `id` values of returned records can then be used to manage records via the objects API endpoints. For example, to retrieve all deals in the _Presentation scheduled_ stage with a value over $10,000, you’d make a `POST` request to `/crm/objects/2026-03/deals/search`, and your request would look like the following:


    {
        "filterGroups":[
          {
            "filters":[
              {
                "propertyName": "dealstage",
                "operator": "EQ",
                "value": "presentationscheduled"
              },
              {
                "propertyName": "amount",
                "operator": "GT",
                "value": "10000"
              }
            ]
          }
        ]
      }


##

​

Create records

  * To create a record for an object, make a `POST` request to `crm/objects/2026-03/{objectTypeId}`.
  * To create multiple records, make a `POST` request to `/crm/objects/2026-03/{objectTypeId}/batch/create`.

In your request, include data for each record in a `properties` object. You can also add an `associations` object to associate your new record with existing records (e.g., companies, deals), or activities (e.g., meetings, notes).

If you want to create and update records at the same time, learn how to upsert records below.

###

​

Properties

Record details are stored in properties. To view all available properties for an object, you can retrieve a list of your account’s properties by making a `GET` request to `/crm/properties/2026-03/{objectTypeId}`. Learn more about the [properties API](/docs/api-reference/latest/crm/properties/guide) and [how to format property values.](/docs/api-reference/latest/crm/properties/guide#update-or-clear-a-property-s-values) Expand the section below to view the objects for which records can be created via API, and the properties required for creation.

Required properties to create records

Object| Type ID| Required properties to create
---|---|---
Appointments| `0-421`| `hs_appointment_name`
Calls| `0-48`| `hs_timestamp`
Carts| `0-142`| None, but recommended `hs_cart_name`
Communications| `0-18`| `hs_timestamp` and `hs_communication_channel_type`
Companies| `0-2`| At least one of `domain` (recommended) or `name`
Contacts| `0-1`| None, but recommended at least one of `email`, `firstname`, or `lastname`
Courses| `0-410`| `hs_course_name`
Custom objects| `2-XXX`| The [required properties](/docs/api-reference/latest/crm/objects/custom-objects/guide#properties) specified in your object’s [schema](/docs/api-reference/latest/crm/objects/object-library/guide).
Deals| `0-3`| `dealname`, `dealstage` and `pipeline`
Emails| `0-49`| `hs_timestamp` and `hs_email_direction`
Invoices| `0-53`| `hs_currency`
Leads| `0-136`| `hs_associated_contact_email`, `hs_associated_contact_lastname`, `hs_lead_name`, `hs_associated_company_domain`, `hs_associated_contact_firstname`, and `hs_associated_company_name`
Line items| `0-8`| None, but review [recommended properties](/docs/api-reference/latest/crm/objects/line-items/guide).
Listings| `0-420`| `hs_name`
Marketing events| `0-54`| `hs_event_description` and `hs_event_name`
Meetings| `0-47`| `hs_timestamp`
Notes| `0-46`| `hs_timestamp`
Orders| `0-123`| `hs_order_name`
Payments| `0-101`| `hs_initial_amount` and `hs_initiated_date`
Postal mail| `0-116`| `hs_timestamp`
Products| `0-7`| `hs_sku`, `hs_folder`, `price`, `name`, and `description`
Projects| `0-970`| `hs_name`, `hs_pipeline`, and `hs_pipeline_stage`
Quotes| `0-14`| `hs_title` and `hs_expiration_date`
Services| `0-162`| `hs_name`, `hs_pipeline`, and `hs_pipeline_stage`
Subscriptions| `0-69`| `hs_name`
Tasks| `0-27`| `hs_timestamp`
Tickets| `0-5`| `subject` (the ticket’s name), `hs_pipeline_stage` (the ticket’s status), and `hs_pipeline`
Users| `0-115`| `hs_internal_user_id` and `hs_email`

For example, to create a new ticket without associations, your request may look similar to the following:


    {
      "properties": {
        "hs_pipeline": "0",
        "hs_pipeline_stage": "1",
        "hs_ticket_priority": "HIGH",
        "subject": "troubleshoot report"
      }
    }


For example, to create multiple contacts without associations, your request may look similar to the following:


    {
      "inputs": [
        {
          "properties": {
            "email": "testone@test.com",
            "firstname": "Test",
            "lastname": "PersonOne",
            "favorite_food": "Pizza"
          }
        },
        {
          "properties": {
            "email": "testtwo@test.com",
            "firstname": "Test",
            "lastname": "PersonTwo",
            "favorite_food": "Ice cream"
          }
        }
      ]
    }


###

​

Associations

When creating a new record, you can also associate it with [existing records](https://knowledge.hubspot.com/records/associate-records) or [activities](https://knowledge.hubspot.com/records/associate-activities-with-records) by including an `associations` object. In the `associations` object, you should include the following:

Parameter| Description
---|---
`to`| The record or activity you want to associate with the record, specified by its unique `id` value.
`types`| The type of the association between the record and the record/activity. Include the `associationCategory` and `associationTypeId`. Default association type IDs are listed [here](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values), or you can retrieve the value for custom association types (i.e. labels) via the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide#retrieve-association-types).

For example, to create a new contact and associate with an existing company and email, your request would look like the following:


    {
      "properties": {
        "email": "example@hubspot.com",
        "firstname": "Jane",
        "lastname": "Doe",
        "phone": "(555) 555-5555",
        "company": "HubSpot",
        "website": "hubspot.com",
        "lifecyclestage": "marketingqualifiedlead"
      },
      "associations": [
        {
          "to": {
            "id": 123456
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 279
            }
          ]
        },
        {
          "to": {
            "id": 556677
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 197
            }
          ]
        }
      ]
    }


For example, to create multiple deals and associate them with existing companies and meetings, your request would look similar to the following:

For batch create actions, you can enable multi-status errors which tell you which records were successfully created and which were not. Learn more about setting up multi-status error handling.


    {
      "inputs": [
        {
          "associations": [
            {
              "types": [
                {
                  "associationCategory": "HUBSPOT_DEFINED",
                  "associationTypeId": 5
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
                  "associationTypeId": 211
                }
              ],
              "to": {
                "id": "65059681027"
              }
            }
          ],
          "properties": {
            "dealname": "New deal 1",
            "dealstage": "qualifiedtobuy",
            "pipeline": "default"
          }
        },
        {
          "associations": [
            {
              "types": [
                {
                  "associationCategory": "HUBSPOT_DEFINED",
                  "associationTypeId": 5
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
                  "associationTypeId": 211
                }
              ],
              "to": {
                "id": "65059681027"
              }
            }
          ],
          "properties": {
            "dealname": "New deal 2",
            "dealstage": "qualifiedtobuy",
            "pipeline": "default"
          }
        }
      ]
    }


##

​

Update records

You can update records individually or in batches. For existing records, the Record ID is a default [unique value](/docs/guides/crm/understanding-the-crm#unique-identifiers-and-record-ids) that you can use to update the record via API, but you can also identify records using the `idProperty` parameter with a [custom unique identifier property](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties). If you want to create and update records at the same time, learn how to upsert records.

  * To update an individual record, make a `PATCH` request to `/crm/objects/2026-03/{objectTypeId}/{recordId}`, and include the data you want to update.
  * To update multiple records, make a `POST` request to `/crm/objects/2026-03/{objectTypeId}/batch/update`. In the request body, include an array with the identifiers for the records and the properties you want to update.


If you’ve [merged records](https://knowledge.hubspot.com/records/merge-records), you can use the previous record ID values stored in the `hs_merged_object_ids` field to update a record using the basic update endpoint. However, these values are not supported when updating records using the batch update endpoint.

For example, to update a contact, your request would look similar to the following:


    {
      "properties": {
        "favorite_food": "burger",
        "jobtitle": "Manager",
        "lifecyclestage": "Customer"
      }
    }


##

​

Upsert records

You can also batch create and update records at the same time using the upsert endpoint. For this endpoint, you can use a [custom unique identifier property](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties) or `email` for contacts. Following the request, if the records already exist, they’ll be updated and if the records don’t exist, they’ll be created. To upsert records, make a `POST` request to `/crm/objects/2026-03/{objectTypeId}/batch/upsert`. In your request body, include the `idProperty` parameter to identify the unique identifier property you’re using. Include that property’s value as the `id` ​and add the other properties you want to set or update.

Partial upserts are not supported when using `email` as the `idProperty` for contacts. To complete a partial upsert, use a custom unique identifier property as the `idProperty` instead.

For example, to upsert contacts to set the phone number property using `email` as the identifier, your request would look similar to the following:


    {
      "inputs": [
        {
          "properties": {
            "phone": "5555555555"
          },
          "id": "luke@lukesdiner.com",
          "idProperty": "email"
        },
        {
          "properties": {
            "phone": "7777777777"
          },
          "id": "lorelai@thedragonfly.com",
          "idProperty": "email"
        },
        {
          "properties": {
            "phone": "1111111111"
          },
          "id": "michel@thedragonfly.com",
          "idProperty": "email"
        }
      ]
    }


##

​

Update associations

Once records are created, you can update their associations using the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide).

  * To associate a record with other records or an activity, make a `PUT` request to `/crm/objects/2026-03/{objectTypeId}/{fromRecordId}/associations/{toObjectTypeId}/{toRecordId}`.
  * To remove an association between a record and a record or activity, make a `DELETE` request to the following URL: `/crm/objects/2026-03/{objectTypeId}/{fromRecordId}/associations/{toObjectTypeId}/{toRecordId}`.


To retrieve the `associationTypeId` value, refer to [this list](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values) of default values, or make a `GET` request to `/crm/associations/2026-03/{fromObjectTypeId}/{toObjectTypeId}/labels`.

##

​

Pin an activity on a record

You can [pin an activity](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record by including the `hs_pinned_engagement_id` field in your create, update, or upsert request. In the field, include the `id` of the activity to pin, which can be retrieved by making a `GET` request to `/crm/objects/2026-03/{objectTypeId}/{recordId}` for calls, communications, emails, meetings, notes, postal mail, or tasks. You can pin one activity per record, and the activity must already be associated with the record prior to pinning. For example, to set or update an existing deal’s pinned activity, your request could look like:


    {
      "properties": {
        "hs_pinned_engagement_id": 123456789
      }
    }


To create a new deal, associate it with an activity, and pin that activity, you request would look like:


    {
      "properties": {
        "dealname": "New Deal",
        "pipeline": "default",
        "dealstage": "appointmentscheduled",
        "hs_pinned_engagement_id": 123456789
      },
      "associations": [
        {
          "to": {
            "id": 123456789
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 205
            }
          ]
        }
      ]
    }


##

​

Delete records

You can delete records individually or in batches, which will add the record to the recycling bin in HubSpot. You can [restore the record within HubSpot](https://knowledge.hubspot.com/records/restore-deleted-records) for up to 90 days after deletion.

  * To delete an individual record by its record ID, make a `DELETE` request to `/crm/objects/2026-03/{objectTypeId}/{recordId}`.
  * To delete multiple records, make a `POST` request to `/crm/objects/2026-03/{objectTypeId}/batch/archive` and include the record ID values as the `id` inputs in your request body.

For example, to delete multiple appointments, your request would look like:


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

Object API batch endpoints are limited to 100 inputs per request. For example, create or retrieve up to 100 contacts per request.

##

​

Error handling

The following are common errors you may encounter when using the object APIs. Refer to the [error handling guide](/docs/api-reference/error-handling#common-error-responses) for details about more error responses and how to resolve them.

Error| Details
---|---
`207 Multi-Status`| Returned when there are different statuses (e.g., errors and successes), which occurs when you’ve enabled multi-status error handling for the object API batch create endpoints.
`400 Bad Request`| Returned when your request includes invalid formatting or values. The error response will include details about why the error occurred.
`401 Unauthorized`| Returned when the authentication provided is invalid. See the [authentication overview](/docs/apps/developer-platform/build-apps/authentication/overview) for details on authenticating API requests.
`403 Forbidden`| Returned when the authentication provided does not have the proper permissions to access the specific URL. See the [list of scopes](/docs/apps/developer-platform/build-apps/authentication/scopes) to understand which scopes are required for your request.
`423 Locked`| Returned when attempting to sync a large volume of data (e.g., upserting thousands of company records in a very short period of time). Include a delay of at least 2 seconds between your API requests.
`429 Too many requests`| Returned when your account or app is over its API [rate limits](/docs/developer-tooling/platform/usage-guidelines).

For example:

  * If you attempt to create a company with an invalid property name, your error response would look like:


400 Bad Request


    {
      "status": "error",
      "message": "Property values were not valid: [{\"isValid\":false,\"message\":\"Property \\\"testproperty\\\" does not exist\",\"error\":\"PROPERTY_DOESNT_EXIST\",\"name\":\"testproperty\",\"localizedErrorMessage\":\"Property \\\"testproperty\\\" does not exist\",\"portalId\":{HubId}}]",
      "correlationId": "8a3f6c3a-8296-4002-b0a6-2a06fecf7c0c",
      "errors": [
        {
          "message": "Property \"testproperty\" does not exist",
          "code": "PROPERTY_DOESNT_EXIST",
          "context": {
            "propertyName": [
              "testproperty"
            ]
          }
        }
      ],
      "category": "VALIDATION_ERROR"
    }


  * If you attempt to retrieve deals without the `crm.objects.deals.read` scope, your response would look like:


403 Forbidden


    {
      "status": "error",
      "message": "This app hasn't been granted all required scopes to make this call. Read more about required scopes here: https://developers.hubspot.com/scopes.",
      "correlationId": "dc49c0a8-9952-4937-aad4-e322b1e5cee0",
      "errors": [
        {
          "message": "One or more of the following scopes are required.",
          "context": {
            "requiredGranularScopes": [
              "crm.schemas.deals.read",
              "crm.objects.deals.sensitive.read.v2",
              "crm.objects.deals.read",
              "crm.objects.deals.highly_sensitive.read.v2"
            ]
          }
        }
      ],
      "links": {
        "scopes": "https://developers.hubspot.com/scopes"
      },
      "category": "MISSING_SCOPES"
    }


###

​

Multi-status errors for batch create requests

For the object APIs’ batch create endpoints, you can enable multi-status responses that include partial failures by including a unique `objectWriteTraceId` value for each input in your request. The `objectWriteTraceId` can be any unique string that helps you identify which records succeeded or failed. For example, a request to create tickets could look like:


    {
        "inputs": [
            {
                "objectWriteTraceId": "549b1c2a9350",
                "properties": {
                    "hs_pipeline_stage": "1"
                }
            },
            {
                "objectWriteTraceId": "549b1c2a9351",
                "properties": {
                    "missing": "1"
                }
            }
        ]
    }


In the response, statuses are grouped so you can see which creates were successful and which failed. For the above request, your response would look like:


    {
      "status": "COMPLETE",
      "results": [
        {
          "id": "1145814089",
          "properties": {
            "createdate": "2024-08-15T17:09:13.648Z",
            "hs_helpdesk_sort_timestamp": "2024-08-15T17:09:13.648Z",
            "hs_last_message_from_visitor": "false",
            "hs_lastmodifieddate": "2024-08-15T17:09:13.648Z",
            "hs_object_id": "1145814089",
            "hs_object_source": "API",
            "hs_object_source_label": "INTERNAL_PROCESSING",
            "hs_pipeline": "0",
            "hs_pipeline_stage": "1",
            "hs_ticket_id": "1145814089"
          },
          "createdAt": "2024-08-15T17:09:13.648Z",
          "updatedAt": "2024-08-15T17:09:13.648Z",
          "archived": false
        }
      ],
      "numErrors": 1,
      "errors": [
        {
          "status": "error",
          "category": "VALIDATION_ERROR",
          "message": "Property values were not valid: [{\"isValid\":false,\"message\":\"Property \\\"missing\\\" does not exist\",\"error\":\"PROPERTY_DOESNT_EXIST\",\"name\":\"missing\",\"localizedErrorMessage\":\"Property \\\"missing\\\" does not exist\",\"portalId\":891936587}]",
          "context": {
            "objectWriteTraceId": ["549b1c2a9351"]
          }
        }
      ],
      "startedAt": "2024-08-15T17:09:13.610Z",
      "completedAt": "2024-08-15T17:09:13.910Z"
    }


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)