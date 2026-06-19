# CRM search

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/search-the-crm*

---

CRM

# CRM search

The CRM search endpoints make getting data more efficient by allowing developers to filter, sort, and search across any CRM object type.

Use the CRM search endpoints to filter, sort, and search objects, records, and engagements across your CRM. For example, use the endpoints to get a list of contacts in your account, or a list of all open deals. To use these endpoints from an app, a CRM scope is required. Refer to this [list of available scopes](/docs/apps/developer-platform/build-apps/authentication/scopes) to learn which granular CRM scopes can be used to accomplish your goal.

##

​

Make a search request

To search your CRM, make a `POST` request to the object’s search endpoint. CRM search endpoints are constructed using the following format: `/crm/v3/objects/{object}/search`. In the request body, you’ll include filters to narrow your search by CRM property values. For example, the code snippet below would retrieve a list of all contacts that have a specific company email address.


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "email",
              "operator": "CONTAINS_TOKEN",
              "value": "*@hubspot.com"
            }
          ]
        }
      ]
    }


Each object that you search will include a set of default properties that gets returned. For contacts, a search will return `createdate`, `email`, `firstname`, `hs_object_id`, `lastmodifieddate`, and `lastname`. For example, the above request would return the following response:


    {
      "total": 2,
      "results": [
        {
          "id": "100451",
          "properties": {
            "createdate": "2024-01-17T19:55:04.281Z",
            "email": "testperson@hubspot.com",
            "firstname": "Test",
            "hs_object_id": "100451",
            "lastmodifieddate": "2024-09-11T13:27:39.356Z",
            "lastname": "Person"
          },
          "createdAt": "2024-01-17T19:55:04.281Z",
          "updatedAt": "2024-09-11T13:27:39.356Z",
          "archived": false
        },
        {
          "id": "57156923994",
          "properties": {
            "createdate": "2024-09-11T18:21:50.012Z",
            "email": "emailmaria@hubspot.com",
            "firstname": "Maria",
            "hs_object_id": "57156923994",
            "lastmodifieddate": "2024-10-21T21:36:02.961Z",
            "lastname": "Johnson (Sample Contact)"
          },
          "createdAt": "2024-09-11T18:21:50.012Z",
          "updatedAt": "2024-10-21T21:36:02.961Z",
          "archived": false
        }
      ]
    }


To return a specific set of properties, include a `properties` array in the request body. For example:


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "annualrevenue",
              "operator": "GT",
              "value": "10000000"
            }
          ]
        }
      ],
      "properties": ["annualrevenue", "name"]
    }


The response for the above request would look like:


    {
      "total": 38,
      "results": [
        {
          "id": "2810868468",
          "properties": {
            "annualrevenue": "1000000000",
            "createdate": "2020-01-09T20:11:27.309Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.333Z",
            "hs_object_id": "2810868468",
            "name": "Google"
          },
          "createdAt": "2020-01-09T20:11:27.309Z",
          "updatedAt": "2024-09-13T20:23:03.333Z",
          "archived": false
        },
        {
          "id": "2823023532",
          "properties": {
            "annualrevenue": "10000000000",
            "createdate": "2020-01-13T16:21:08.270Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.064Z",
            "hs_object_id": "2823023532",
            "name": "Pepsi"
          },
          "createdAt": "2020-01-13T16:21:08.270Z",
          "updatedAt": "2024-09-13T20:23:03.064Z",
          "archived": false
        },
        {
          "id": "5281147580",
          "properties": {
            "annualrevenue": "50000000",
            "createdate": "2021-02-01T21:17:12.250Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.332Z",
            "hs_object_id": "5281147580",
            "name": "CORKCICLE"
          },
          "createdAt": "2021-02-01T21:17:12.250Z",
          "updatedAt": "2024-09-13T20:23:03.332Z",
          "archived": false
        },
        {
          "id": "5281147581",
          "properties": {
            "annualrevenue": "1000000000",
            "createdate": "2021-02-01T21:17:12.250Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.064Z",
            "hs_object_id": "5281147581",
            "name": "Ulta Beauty"
          },
          "createdAt": "2021-02-01T21:17:12.250Z",
          "updatedAt": "2024-09-13T20:23:03.064Z",
          "archived": false
        },
        {
          "id": "5281147583",
          "properties": {
            "annualrevenue": "50000000",
            "createdate": "2021-02-01T21:17:12.251Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.332Z",
            "hs_object_id": "5281147583",
            "name": "Narvar"
          },
          "createdAt": "2021-02-01T21:17:12.251Z",
          "updatedAt": "2024-09-13T20:23:03.332Z",
          "archived": false
        },
        {
          "id": "5281496154",
          "properties": {
            "annualrevenue": "1000000000",
            "createdate": "2021-02-01T21:17:12.267Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.332Z",
            "hs_object_id": "5281496154",
            "name": "Etsy Inc"
          },
          "createdAt": "2021-02-01T21:17:12.267Z",
          "updatedAt": "2024-09-13T20:23:03.332Z",
          "archived": false
        },
        {
          "id": "5281496155",
          "properties": {
            "annualrevenue": "1000000000",
            "createdate": "2021-02-01T21:17:12.267Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.069Z",
            "hs_object_id": "5281496155",
            "name": "grubhub"
          },
          "createdAt": "2021-02-01T21:17:12.267Z",
          "updatedAt": "2024-09-13T20:23:03.069Z",
          "archived": false
        },
        {
          "id": "5281496157",
          "properties": {
            "annualrevenue": "1000000000",
            "createdate": "2021-02-01T21:17:12.267Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.332Z",
            "hs_object_id": "5281496157",
            "name": "discover"
          },
          "createdAt": "2021-02-01T21:17:12.267Z",
          "updatedAt": "2024-09-13T20:23:03.332Z",
          "archived": false
        },
        {
          "id": "5281496158",
          "properties": {
            "annualrevenue": "50000000",
            "createdate": "2021-02-01T21:17:12.268Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.064Z",
            "hs_object_id": "5281496158",
            "name": "Soludos"
          },
          "createdAt": "2021-02-01T21:17:12.268Z",
          "updatedAt": "2024-09-13T20:23:03.064Z",
          "archived": false
        },
        {
          "id": "5281499282",
          "properties": {
            "annualrevenue": "1000000000",
            "createdate": "2021-02-01T21:17:12.285Z",
            "hs_lastmodifieddate": "2024-09-13T20:23:03.066Z",
            "hs_object_id": "5281499282",
            "name": "AEO Management Co."
          },
          "createdAt": "2021-02-01T21:17:12.285Z",
          "updatedAt": "2024-09-13T20:23:03.066Z",
          "archived": false
        }
      ],
      "paging": {
        "next": {
          "after": "10"
        }
      }
    }


##

​

Searchable CRM objects and engagements

###

​

Objects

The tables below contain the object search endpoints, the objects they refer to, and the properties that are returned by default.

Search endpoint| Object| Default returned properties
---|---|---
`/crm/v3/objects/carts/search`| Carts| `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/companies/search`| Companies| `name`, `domain`, `createdate`,`hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/contacts/search`| Contacts| `firstname`,`lastname`,`email`,`lastmodifieddate`,`hs_object_id`, `createdate`
`/crm/v3/objects/deals/search`| Deals| `dealname`, `amount`, `closedate`, `pipeline`, `dealstage`, `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/deal_split/search`| Deal splits| `hs_createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/discounts/search`| Discounts| `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/feedback_submissions/search`| Feedback submissions| `hs_createdate`,`hs_lastmodifieddate`,`hs_object_id`
`/crm/v3/objects/fees/search`| Fees| `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/invoices/search`| Invoices| `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/leads/search`| Leads| `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/line_items/search`| Line items| `quantity`, `amount`, `price`, `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/orders/search`| Orders| `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/commerce_payments/search`| Payments| `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/products/search`| Products| `name`, `description` ,`price`, `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/quotes/search`| Quotes| `hs_expiration_date`, `hs_public_url_key`, `hs_status`,`hs_title`, `hs_createdate`, `hs_lastmodifieddate`,`hs_object_id`
`/crm/v3/objects/subscriptions/search`| Subscriptions (Commerce)| `hs_createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/taxes/search`| Taxes| `createdate`, `hs_lastmodifieddate`, `hs_object_id`
`/crm/v3/objects/tickets/search`| Tickets| `content`, `hs_pipeline`, `hs_pipeline_stage`,`hs_ticket_category`, `hs_ticket_priority`, `subject`,`createdate`, `hs_lastmodifieddate`, `hs_object_id`

###

​

Engagements

The table below contains the engagement search endpoints, the engagements they refer to, and the properties that are returned by default.

Search endpoint| Engagement| Default returned properties
---|---|---
`/crm/v3/objects/calls/search`| Calls| `hs_createdate`,`hs_lastmodifieddate`,`hs_object_id`
`/crm/v3/objects/emails/search`| Emails| `hs_createdate`,`hs_lastmodifieddate`,`hs_object_id`
`/crm/v3/objects/meetings/search`| Meetings| `hs_createdate`,`hs_lastmodifieddate`,`hs_object_id`
`/crm/v3/objects/notes/search`| Notes| `hs_createdate`,`hs_lastmodifieddate`,`hs_object_id`
`/crm/v3/objects/tasks/search`| Tasks| `hs_createdate`,`hs_lastmodifieddate`,`hs_object_id`

##

​

Search default searchable properties

Search all default text properties in records of the specified object to find all records that have a value containing the specified string. By default, the results will be returned in order of object creation (oldest first), but you can override this with sorting. For example, the request below searches for all contacts with a default text property value containing the letter `X`.


    curl https://api.hubapi.com/crm/v3/objects/contacts/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \
      --data '{
        "query": "x"
      }'


Below are the properties that are searched by default through the above method:

Search endpoint| Object| Default searchable properties
---|---|---
`/crm/v3/objects/calls/search`| Calls| `hs_call_title`, `hs_body_preview`
`/crm/v3/objects/companies/search`| Companies| `website`, `phone`, `name`, `domain`
`/crm/v3/objects/contacts/search`| Contacts| `firstname`,`lastname`,`email`,`phone`,`hs_additional_emails`, `fax`, `mobilephone`, `company`, `hs_marketable_until_renewal`
`/crm/v3/objects/{objectType}/search`| Custom objects| Up to 20 selected properties.
`/crm/v3/objects/deals/search`| Deals| `dealname`,`pipeline`,`dealstage`, `description`, `dealtype`
`/crm/v3/objects/emails/search`| Emails| `hs_email_subject`
`/crm/v3/objects/feedback_submissions/search`| Feedback submissions| `hs_submission_name`, `hs_content`
`/crm/v3/objects/meetings/search`| Meetings| `hs_meeting_title`, `hs_meeting_body`
`/crm/v3/objects/notes/search`| Notes| `hs_note_body`
`/crm/v3/objects/products/search`| Products| `name`, `description` ,`price`, `hs_sku`
`/crm/v3/objects/quotes/search`| Quotes| `hs_sender_firstname`, `hs_sender_lastname`, `hs_proposal_slug`, `hs_title`, `hs_sender_company_name`, `hs_sender_email`, `hs_quote_number`, `hs_public_url_key`
`/crm/v3/objects/tasks/search`| Tasks| `hs_task_body`, `hs_task_subject`
`/crm/v3/objects/tickets/search`| Tickets| `subject`, `content`, `hs_pipeline_stage`, `hs_ticket_category`, `hs_ticket_id`

##

​

Filter search results

Use filters in the request body to limit the results to only records with matching property values. For example, the request below searches for all contacts with a first name of _Alice._

**Please note:** when filtering search results for calls, conversations, emails, meetings, notes, or tasks, the property `hs_body_preview_html` is not supported. For emails, the properties `hs_email_html` and `hs_body_preview` are also not supported.


    curl https://api.hubapi.com/crm/v3/objects/contacts/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \

      --data '{
        "filterGroups":[
          {
            "filters":[
              {
                "propertyName": "firstname",
                "operator": "EQ",
                "value": "Alice"
              }
            ]
          }
        ]
      }'


To include multiple filter criteria, you can group `filters` within **`filterGroups`** :

  * To apply _AND_ logic, include a comma-separated list of conditions within one set of `filters`.
  * To apply _OR_ logic, include multiple `filters` within a `filterGroup`.You can include a maximum of five `filterGroups` with up to 6 `filters` in each group, with a maximum of 18 filters in total. If you’ve included too many groups or filters, you’ll receive a `VALIDATION_ERROR` error response. For example, the request below searches for contacts with the first name `Alice` AND a last name other than `Smith` _,_ OR contacts that don’t have a value for the property `email`.


    curl https://api.hubapi.com/crm/v3/objects/contacts/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \
      --data '{
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "firstname",
              "operator": "EQ",
              "value": "Alice"
            },
            {
              "propertyName": "lastname",
              "operator": "NEQ",
              "value": "Smith"
            }
          ]
        },
        {
          "filters": [
            {
              "propertyName": "email",
              "operator": "NOT_HAS_PROPERTY"
            }
          ]
        }
      ]
    }'


You can use operators in filters to specify which records should be returned. Values in filters are case-insensitive, with the following two exceptions:

  * When filtering for an enumeration property, search is case-sensitive for all filter operators.
  * When filtering for a string property using `IN` and `NOT_IN` operators, the searched values must be lowercase.Below are the available filter operators:


Operator| Description
---|---
`LT`| Less than the specified value.
`LTE`| Less than or equal to the specified value.
`GT`| Greater than the specified value.
`GTE`| Greater than or equal to the specified value.
`EQ`| Equal to the specified value.
`NEQ`| Not equal to the specified value.
`BETWEEN`| Within the specified range. In your request, use key-value pairs to set `highValue` and `value`. Refer to the example below the table.
`IN`| Included within the specified list. Searches by exact match. In your request, include the list values in a `values` array. When searching a string property with this operator, values must be lowercase. Refer to the example below the table.
`NOT_IN`| Not included within the specified list. In your request, include the list values in a `values` array. When searching a string property with this operator, values must be lowercase.
`HAS_PROPERTY`| Has a value for the specified property.
`NOT_HAS_PROPERTY`| Doesn’t have a value for the specified property.
`CONTAINS_TOKEN`| Contains a token. In your request, you can use wildcards (*) to complete a partial search. For example, use the value `*@hubspot.com` to retrieve contacts with a HubSpot email address.
`NOT_CONTAINS_TOKEN`| Doesn’t contain a token.

For example, you can use the `BETWEEN` operator to search for all tasks that were last modified within a specific time range:


    curl https://api.hubapi.com/crm/v3/objects/tasks/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \
      --data '{
       "filterGroups":[{
          "filters":[
            {
              "propertyName":"hs_lastmodifieddate",
              "operator":"BETWEEN",
              "highValue": "1642672800000",
              "value":"1579514400000"
            }
          ]
        }]
    }'


For another example, you can use the `IN` operator to search for companies that have specified values selected in a dropdown property.


    curl https://api.hubapi.com/crm/v3/objects/companies/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \
      --data '{
        "filterGroups":[
          {
            "filters":[
              {
               "propertyName":"enumeration_property",
               "operator":"IN",
              "values": ["value_1", "value_2"]
            }
            ]
          }
        ],
       "properties": ["annualrevenue", "enumeration_property", "name"]
      }'


##

​

Search through associations

Search for records that are associated with other specific records by using the pseudo-property `associations.{objectType}`. For example, the request below searches for all tickets associated with a contact that has the contact ID of `123`:


    curl https://api.hubapi.com/crm/v3/objects/tickets/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \
      --data '{
        "filters": [
          {
            "propertyName": "associations.contact",
            "operator": "EQ",
            "value": "123"
          }
        ]
      }'


**Please note:** the option to search through custom object associations is not currently supported via search endpoints. To find custom object associations, you can use the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide).

##

​

Sort search results

Use a sorting rule in the request body to list results in ascending or descending order. Only one sorting rule can be applied to any search. For example, the request below sorts returned contacts with most recently created first:


    curl https://api.hubapi.com/crm/v3/objects/contacts/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \
      --data '{
        "sorts": [
          {
            "propertyName": "createdate",
            "direction": "DESCENDING"
          }
        ]
      }'


##

​

Paging through results

By default, the search endpoints will return pages of 10 records at a time. This can be changed by setting the `limit` parameter in the request body. The maximum number of supported objects per page is 200. For example, the request below would return pages containing 20 results each.


    curl https://api.hubapi.com/crm/v3/objects/contacts/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \
      --data '{
        "limit": 20
      }'


To access the next page of results, you must pass an **`after`** parameter provided in the **`paging.next.after`** property of the previous response. If the **`paging.next.after`** property isn’t provided, there are no additional results to display. You must format the value in the `after` parameter as an integer. For example, the request below would return the next page of results:


    curl https://api.hubapi.com/crm/v3/objects/contacts/search \
      --request POST \
      --header "Content-Type: application/json" \
      --header "authorization: Bearer YOUR_ACCESS_TOKEN" \
      --data '{
        "after": "20"
      }'


##

​

Limits

  * It may take a few moments for newly created or updated CRM objects to appear in search results.
  * Archived CRM objects won’t appear in any search results.
  * The search endpoints are [rate limited](/docs/developer-tooling/platform/usage-guidelines) to _five_ requests per second per account.
  * The maximum number of supported objects per page is 200.
  * A query can contain a maximum of 3,000 characters. If the body of your request exceeds 3,000 characters, a 400 error will be returned.
  * The search endpoints are limited to 10,000 total results for any given query. Attempting to page beyond 10,000 will result in a 400 error.
  * When filtering, you can include a maximum of five `filterGroups` with up to six `filters` in each group, with a maximum of 18 filters in total.
  * When searching for phone numbers, HubSpot uses special calculated properties to standardize the format. These properties all start with `hs_searchable_calculated_*`. As a part of this standardization, HubSpot only uses the area code and local number. You should refrain from including the country code in your search or filter criteria.


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)