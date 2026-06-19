# Associate records

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/associations/v3/associate-records*

---

v3

# Associate records

The CRM Associations endpoints are used to manage associations between tickets, products, line items, and their related contacts, companies, and deals.

The [new version of the Associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide) has additional functionality, including creating and managing association labels. Refer to the [v4 Associations API article](/docs/api-reference/legacy/crm/associations/associate-records/guide) for more information.

Scope requirements

Associations represent the relationships between objects and activities in the HubSpot CRM. You can use the v3 associations endpoints to create, retrieve, or remove associations in bulk. Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs/guides/crm/understanding-the-crm) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](https://knowledge.hubspot.com/get-started/manage-your-crm-database)[.](https://knowledge.hubspot.com/contacts-user-guide)

##

​

Association types

Associations are defined by object and direction. Association types are unidirectional, which means you’ll need to use a different definition depending on the starting object type. Each endpoint requires a `{fromObjectType}` and `{toObjectType}` that tell the direction of the association. For example:

  * To view all the defined association types from contacts to companies, you’d make a request to `/crm/v3/associations/contacts/companies/types`.
  * To see all tickets associated with a contact, you’d make a request to `/crm/v3/associations/Contacts/Tickets/batch/read` and identify the contact in the request body by its `objectId`. In this example, Contacts is the _fromObjectType_ , and Tickets is the _toObjectType_.

Association types can include unlabeled associations (e.g., contact-to-company), default labeled associations (e.g., contact-to-primary company), and custom labeled associations (e.g., _Decision maker_ contact-to-company).

##

​

Retrieve association types

To view all the defined association types between objects, including default associations and custom association labels, make a `GET` request to `/crm/v3/associations/{fromObjectType}/{toObjectType}/types`. Each type will have a returned numerical `id` value and `name` that can be used to reference the association type in other requests. For default associations, the numerical ID will be the same for all accounts, but for custom association labels, the ID will be unique to your account. For example, your response would look similar to the following:


    ///Example response GET /crm/v3/associations/contacts/companies/types
    {
      "results": [
        {
          "id": "136",
          "name": "franchise_owner_franchise_location"
        },
        {
          "id": "26",
          "name": "manager"
        },
        {
          "id": "1",
          "name": "contact_to_company"
        },
        {
          "id": "279",
          "name": "contact_to_company_unlabeled"
        },
        {
          "id": "32",
          "name": "contractor"
        },
        {
          "id": "37",
          "name": "chef"
        },
        {
          "id": "142",
          "name": "toy_tester"
        },
        {
          "id": "30",
          "name": "decision_maker"
        },
        {
          "id": "28",
          "name": "billing_contact"
        }
      ]
    }


While you can reference custom association types (i.e. labels) with the v3 Associations API, you cannot use the API to create or edit new labels. Learn how to create, update, and delete labels in the [v4 Associations API article](/docs/api-reference/legacy/crm/associations/associate-records/guide).

##

​

Create associations

To [associate records](https://knowledge.hubspot.com/records/associate-records), make a `POST` request to `/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/create`. In your request, include the `id` values for the records you want to associate, as well as the `type` of the association. For example, to associate contacts to companies, your request URL would be `/crm/v3/associations/Contacts/Companies/batch/create`, and your request would look similar to the following:


    ///Example request body
    {
      "inputs": [
        {
          "from": {
            "id": "53628"
          },
          "to": {
            "id": "12726"
          },
          "type": "contact_to_company"
        }
      ]
    }


##

​

Retrieve associations

To retrieve associated records, make a `POST` request to `/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/read`. In your request, include the `id` values of the records whose associations you want to view. This will be for the `{fromObjectType}`. For example, to retrieve deals associated with companies, your request URL would be `/crm/v3/associations/Companies/Deals/batch/read` and the request body would look like the following, with `id` values for the companies whose deal associations you want to view:


    {
      "inputs": [
        {
          "id": "5790939450"
        },
        {
          "id": "6108662573"
        }
      ]
    }


In your response, you’ll receive the `id` values of all associated records. For the above example, your response would include the `id` values for all associated deals and the association `type`. The response would look similar to the following:


    {
      "status": "COMPLETE",
      "results": [
        {
          "from": {
            "id": "5790939450"
          },
          "to": [
            {
              "id": "1467822235",
              "type": "company_to_deal"
            },
            {
              "id": "7213991219",
              "type": "company_to_deal"
            },
            {
              "id": "9993513636",
              "type": "company_to_deal"
            },
            {
              "id": "18731599139",
              "type": "company_to_deal"
            },
            {
              "id": "21678228008",
              "type": "company_to_deal"
            }
          ]
        },
        {
          "from": {
            "id": "6108662573"
          },
          "to": [
            {
              "id": "22901690010",
              "type": "company_to_deal"
            }
          ]
        }
      ],
      "startedAt": "2024-10-21T16:40:47.810Z",
      "completedAt": "2024-10-21T16:40:47.833Z"
    }


**Please note:** When retrieving records associated with companies (i.e. `crm/v3/associations/{fromObjectType}/companies/batch/read`), only the [primary associated company](https://knowledge.hubspot.com/records/associate-records#primary-company-association) will be returned. To view all associated companies, use the [V4 associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide).

##

​

Remove associations

To remove associations between records, make a `POST` request to `/crm/v3/associations/{fromObjectType}/{toObjectType}/batch/archive`. In the request body, include the `id` values for the from record and the to record, as well as their association type. For example, to remove the association between a company and a deal, your request would look like:


    {
      "inputs": [
        {
          "from": {
            "id": "5790939450"
          },
          "to": {
            "id": "21678228008"
          },
          "type": "company_to_deal"
        }
      ]
    }


##

​

Limits

The following limits apply for batch associations API endpoint requests:

  * **Batch read associations** : limited to 1,000 inputs per request body.
  * **Batch create associations** : limited to 2,000 inputs per request body.


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)