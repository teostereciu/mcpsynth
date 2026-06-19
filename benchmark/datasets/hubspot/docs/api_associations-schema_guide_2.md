# Configure associations

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/associations/associations-schema/guide*

---

Associations schema

# Configure associations

The Associations Schema endpoints are used to manage association types across objects.

Scope requirements

Associations represent the relationships between objects and activities in the HubSpot CRM. Record associations can exist between records of different objects (e.g., Contact to Company), as well as within the same object (e.g., Company to Company). The Associations API includes two sets of endpoints:

  * **Association schema endpoints** : view your account’s association definitions (also known as types), create and manage custom association labels, and set limits for associations. In this article, you’ll learn more about using the associations schema endpoints.
  * **[Association details endpoints](/docs/api-reference/latest/crm/associations/associate-records)** : once association types are defined, create, edit, and remove associations between records. Learn more about using the [associations details endpoints](api-reference/latest/crm/associations/associate-records/guide#associate-records-with-a-label).

Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs/guides/crm/understanding-the-crm) guide.

##

​

Understand association definitions, configurations, and labels

To manage association definition (a.k.a association type) configurations and labels, use the _Association schema_ endpoints. These endpoints include configuration endpoints and label endpoints. You should use the endpoints for the following goals:

  * **Association definitions (labels)** : create and manage association types, including creating, editing, and deleting custom association labels. For example, create a _Billing contact_ label between contacts and deals or a _Manager_ and _Employee_ paired label between contacts.
  * **Association definition configurations** : set and manage limits for how many associations can exist per association type. For example, allow up to five associated deals per company or only one associated contact with the _Decision maker_ label per company.


###

​

HubSpot-defined associations

HubSpot provides a set of predefined association types (e.g., unlabeled contact to company), but account admins can [define their own association labels](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels) to provide additional context for record relationships (e.g., manager and employee). There are two HubSpot-defined association types:

  * **Primary:** the main company that the other record is associated with. Primary associations can be used in HubSpot tools such as [lists and workflows](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels#use-associations-in-hubspot-tools). For records with multiple associated companies, the [association details API](/docs/api-reference/latest/crm/associations/associate-records/guide#associate-records-with-a-label) supports changing which company is considered the primary.
  * **Unlabeled:** a default association added when any records are associated. This type denotes that an association exists, and will always be [returned](/docs/api-reference/latest/crm/associations/associate-records#retrieve-associated-records) in responses with a `label` value of `null`. When a record has a primary association or a custom association label, those types will be [listed alongside the unlabeled association type](/docs/api-reference/latest/crm/associations/associate-records#retrieve-associated-records).

You can view all of the HubSpot-defined association types in the [association details guide](/docs/api-reference/latest/crm/associations/associate-records#association-type-id-values).

###

​

Custom association labels

You can create association labels to further define record associations. For example, you could create a _Decision maker_ label to indicate which contacts at a company are responsible for making purchasing decisions. Learn more about creating association labels below.

##

​

Create and manage association types

Use the definitions endpoints to create custom labeled association types and review or manage existing types.

###

​

Create association labels

You can create custom labeled association types [in HubSpot](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels) or through the association schema API endpoint. You can create up to 10 association labels between each object pairing (e.g. contacts and companies, contacts and contacts). There are two types of [association labels](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels) you can use to describe the relationships between records:

  * **Single:** one label that applies to both records in the relationship. For example, _Friend_ or _Colleague_.
  * **Paired** : a pair of labels for when different words are used to describe each side of the associated records’ relationship. For example, _Parent_ and _Child_ or _Employer_ and _Employee_. To create paired labels, you must include the `inverseLabel` field in your request to name the second label in the pair.

To create a labeled association type, make a `POST` request to `/crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels` and include the following in your request:

Parameter| Description
---|---
`name`| The internal name of the association type. This value _cannot_ include hyphens or begin with a numerical character.
`label`| The alphanumeric name of the [association label as shown in HubSpot](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels).
`inverseLabel` (paired labels only)| The name of the second label in the pair of labels.

Your request body could look similar to the following examples:

Single label


    {
      "label": "Partner",
      "name": "partner"
    }


Paired label


    {
      "label": "Manager",
      "inverseLabel": "Employee",
      "name": "manager_employee"
    }


In the response, the new association label’s `category` and unique `typeId` will be returned, which you can use to retrieve, update, or delete the label moving forward. For paired labels, there’ll be a value for each direction of the association (e.g., `550` for contact to company and `551` for company to contact). For example, for the paired label request above, the response would look like:


    {
      "results": [
        {
          "category": "USER_DEFINED",
          "typeId": 145,
          "label": "Employee"
        },
        {
          "category": "USER_DEFINED",
          "typeId": 144,
          "label": "Manager"
        }
      ]
    }


Once created, you can now add the label when [associating records](/docs/api-reference/latest/crm/associations/associate-records#associate-records-with-a-label).

###

​

Retrieve association labels

To view the association types between specific objects, make a `GET` request to `/crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels`. You’ll receive an array, each item containing:

Parameter| Description
---|---
`category`| Whether the association type was created by HubSpot (`HUBSPOT_DEFINED`) or by a user (`USER_DEFINED`).
`typeId`| The numeric ID for that association type. This is used to [set a label when associating records](/docs/api-reference/latest/crm/associations/associate-records#associate-records-with-a-label). Refer to [this list](/docs/api-reference/latest/crm/associations/associate-records#association-type-id-values) for all the HubSpot defined `typeId` values.
`label`| The alphanumeric label. This will be `null` for the unlabeled association type.

You can also find these values in HubSpot [in your association settings](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels#association-label-api-details). For example, to view all association types from contacts to companies, make a `GET` request to `/crm/associations/2026-03/contacts/companies/labels`. Your response would look similar to the following:


    {
      "results": [
        {
          "category": "HUBSPOT_DEFINED",
          "typeId": 1,
          "label": "Primary"
        },
        {
          "category": "USER_DEFINED",
          "typeId": 28,
          "label": "Billing contact"
        },
        {
          "category": "USER_DEFINED",
          "typeId": 142,
          "label": "Toy Tester"
        },
        {
          "category": "USER_DEFINED",
          "typeId": 26,
          "label": "Manager"
        },
        {
          "category": "USER_DEFINED",
          "typeId": 30,
          "label": "Decision maker"
        },
        {
          "category": "USER_DEFINED",
          "typeId": 37,
          "label": "Chef"
        },
        {
          "category": "USER_DEFINED",
          "typeId": 32,
          "label": "Contractor"
        },
        {
          "category": "HUBSPOT_DEFINED",
          "typeId": 279,
          "label": null
        }
      ]
    }


###

​

Update association labels

You can edit the `label` field for association types, which updates the name as it appears in HubSpot in your settings and on records. You _cannot_ change the internal `name` or `typeId`. To update a label, make a `PUT` request to `/crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels`. In the request body, including the `associationTypeId` and a new value for `label`. If editing a paired label, you can also include a new value for `inverseLabel`. Using the example in the section above, to update the label _Contractor_ to _Contract worker_ , your request body would look like:


    {
      "associationTypeId": 32,
      "label": "Contract worker"
    }


###

​

Delete association labels

You can delete custom association labels if they’re no longer in use. If a label is used to describe associated records, you’ll need to [remove the label](/docs/api-reference/latest/crm/associations/associate-records#remove-record-associations) from associations before deleting. Default association types, including the _Primary company_ label, _cannot_ be deleted. To delete an association label, make a `DELETE` request to `/crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels/{associationTypeId}`. You’ll no longer be able to use this label when associating records.

##

​

Set and manage association limits

Use the definition configuration endpoints to set up [limits](https://knowledge.hubspot.com/object-settings/set-limits-for-record-associations) for the number of associated records between objects, or how often a label can be used to describe associations. There are also [technical limits and limits based on your HubSpot subscription](https://legal.hubspot.com/hubspot-product-and-services-catalog).

###

​

Create or update association limits

You can create new or update existing association limits between objects.

  * To create limits, make a `POST` request to `/crm/associations/2026-03/definitions/configurations/{fromObjectType}/{toObjectType}/batch/create`.
  * To update existing limits, make a `POST` request to `/crm/associations/2026-03/definitions/configurations/{fromObjectType}/{toObjectType}/batch/update`.

In the request body, include `inputs` with the following:

Parameter| Description
---|---
`category`| The category of the association you’re setting a limit for, either `HUBSPOT_DEFINED` or `USER_DEFINED`.
`typeId`| The numeric ID for the association type you want to set a limit for. Refer to [this list](/docs/api-reference/latest/crm/associations/associate-records#association-type-id-values) of default `typeId` values or [retrieve the value](/docs/api-reference/latest/crm/associations/associate-records#retrieve-association-labels) for custom labels.
`maxToObjectIds`| The maximum number of associations allowed for the association type.

For example, to set limits that a deal can be associated with a maximum of five contacts with only one contact labeled _Point of contact_ , your request body would look like the following:


    {
      "inputs": [
        {
          "category": "HUBSPOT_DEFINED",
          "typeId": 3,
          "maxToObjectIds": 5
        },
        {
          "category": "USER_DEFINED",
          "typeId": 35,
          "maxToObjectIds": 1
        }
      ]
    }


###

​

Retrieve association limits

  * To read all defined association limits, make a `GET` request to `/crm/associations/2026-03/definitions/configurations/all`. This will return custom association limits defined across all objects.
  * To read association limits between two specific objects, make a `GET` request to `/crm/associations/2026-03/definitions/configurations/{fromObjectType}/{toObjectType}`.

For both requests, the response will return the associations’ values for `category`, `typeId`, `maxToObjectIds`, and `label`. For example, if retrieving limits between deals and contacts, the response would look similar to:


    {
      "results": [
        {
          "category": "HUBSPOT_DEFINED",
          "typeId": 3,
          "userEnforcedMaxToObjectIds": 5,
          "label": null
        }
      ]
    }


###

​

Delete association limits

To delete specific association limits, make a `POST` request to `/crm/associations/2026-03/definitions/configurations/{fromObjectType}/{toObjectType}/batch/purge`. In the request body, include the `category` and `typeId` values of the association types for which you want to remove limits. For example, to remove the _Point of contact_ limit between deals and contacts, the request would look like:


    {
      "inputs": [
        {
          "category": "USER_DEFINED",
          "typeId": 35
        }
      ]
    }


If successful, you’ll receive a 204 response and the included limit will return to the system default (i.e. Many contacts can have the label _Point of contact_).

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)