# API guide

*Source: https://developers.hubspot.com/docs/api-reference/legacy/communication-preferences/guide*

---

Communication preferences

# API guide

The v4 subscription preferences endpoints allow you to manage email subscriptions details for contacts in your account.

Scope requirements

Subscription types represent the lawful basis to communicate with your contacts through email. Contacts can [manage their email preferences](https://knowledge.hubspot.com/marketing-email/insert-subscription-links-into-marketing-emails) so they’re only opted in to emails they want to receive. The v4 subscriptions APIs allow you to programmatically subscribe or unsubscribe contacts from your email subscription types, or unsubscribe a contact from all email communication. These APIs also provide support for the [Brands add-on](https://knowledge.hubspot.com/branding/associate-your-assets-with-brands).

**Please note:** Some of the endpoints below provide support for a `businessUnitId` field or query parameter, which you can use if you purchased the [Brands add-on](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands). Be aware that business units is the former name for [brands](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands), but this change does _not_ impact the API. You should continue using any previous reference to `businessUnitId`. You can get a list of brands in your account using the [brands API](/docs/api-reference/legacy/account/brands/guide).

##

​

Scope requirements

The following scopes are required to use the v4 subscription API endpoints, based on the endpoint you’re using:

  * `communication_preferences.read`: provides access to fetch subscription type definitions and subscription preferences for a contact.
  * `communication_preferences.write`: provides access to update subscription preferences for a contact.
  * `communication_preferences.read_write`: provides access to both fetch and update subscription preferences for a contact and fetch all subscription definitions in your account.

The scopes below are required to use the batch subscription endpoints. You must have an _**Marketing Hub** Enterprise_ subscription to authorize these scopes for your app.

  * `communication_preferences.statuses.batch.read`: provides access to fetch subscription statuses in bulk.
  * `communication_preferences.statuses.batch.write`: provides access to manage and update subscription statuses in bulk.


##

​

Get all subscription types

To get a list of all email subscription types in your account, make a `GET` request to `/communication-preferences/v4/definitions`. If you have the [Brands add-on](/docs/api-reference/legacy/account/brands/guide), you can filter subscription types by brand by including the `businessUnitId` as a query parameter in your request. The default _Account_ brand will always use `"businessUnitId": 0`. The subscription types will be returned within the `results` field of the response.


    // Example response for GET request to /communication-preferences/v4/definitions
    {
      "status": "COMPLETE",
      "results": [
        {
          "businessUnitId": 41857,
          "id": "33583163",
          "name": "Marketing Information",
          "description": "Marketing offers and updates.",
          "purpose": "Marketing",
          "communicationMethod": "Email",
          "isActive": true,
          "isDefault": true,
          "isInternal": false,
          "createdAt": "2022-02-09T21:06:59.247Z",
          "updatedAt": "2022-02-09T21:06:59.247Z"
        },
        {
          "businessUnitId": 0,
          "id": "39644612",
          "name": "New recipe newsletter",
          "description": "Subscription for new recipes and kitchen updates",
          "purpose": "Marketing",
          "communicationMethod": "Email",
          "isActive": true,
          "isDefault": false,
          "isInternal": false,
          "createdAt": "2022-04-14T20:37:03.073Z",
          "updatedAt": "2022-04-14T20:37:03.073Z"
        }
      ]
    }


You can optionally include the `includeTranslations=true` query parameter in your request to retrieve any subscription translations associated with each definition. For example, if you made a `GET` request to `/communication-preferences/v4/definitions?includeTranslations=true`, the response would resemble the following:


    // Example response for GET request to /communication-preferences/v4/definitions with subscription translations included
    {
      "status": "COMPLETE",
      "results": [
        {
          "subscriptionTranslations": [
            {
              "subscriptionId": 88249125,
              "languageCode": "ar",
              "name": "test",
              "description": "test",
              "updatedAt": 1724702359758,
              "createdAt": 0
            }
          ],
          "businessUnitId": 0,
          "id": "88249125",
          "name": "test",
          "description": "test",
          "purpose": "",
          "communicationMethod": "",
          "isActive": false,
          "isDefault": false,
          "isInternal": false,
          "createdAt": "2022-12-22T21:06:03.522Z",
          "updatedAt": "2024-08-26T19:59:39.926Z"
        }
      ],
      "startedAt": "2024-08-30T20:17:36.744Z",
      "completedAt": "2024-08-30T20:17:36.753Z"
    }


##

​

Get subscription preferences for a specific contact

To get the current subscription preferences for a specific contact, make a `GET` request to `/communication-preferences/v4/statuses/{subscriberIdString}?channel=EMAIL` where the `subscriberIdString` is the email address of the contact. For example, to get the subscription preferences for a contact with an email address of `jdoe@example.com`, you’d make a `GET` request to `/preferences/v4/statuses/jdoe@example.com?channel=EMAIL`. The response will include a full list of the current subscription preferences for the contact in the `results` field. An example response is included below:


    // Example response for GET request to /communication-preferences/v4/statuses/jdoe@example.com?channel=EMAIL
    {
      "status": "SUCCESS",
      "results": [
        {
          "businessUnitId": 41857,
          "channel": "EMAIL",
          "subscriberIdString": "jdoe@example.com",
          "subscriptionId": 33583163,
          "status": "NOT_SPECIFIED",
          "source": "Not specified",
          "legalBasis": null,
          "legalBasisExplanation": null,
          "setStatusSuccessReason": null,
          "timestamp": "2024-06-05T13:39:29.495Z"
        },
        {
          "businessUnitId": 0,
          "channel": "EMAIL",
          "subscriberIdString": "jdoe@example.com",
          "subscriptionId": 39644612,
          "status": "SUBSCRIBED",
          "source": "Self Service Resubscription",
          "legalBasis": "CONSENT_WITH_NOTICE",
          "legalBasisExplanation": "Contact provided explicit consent via form.",
          "setStatusSuccessReason": null,
          "timestamp": "2023-02-09T20:13:19.046Z"
        }
      ]
    }


Based on whether the contact explicitly opted in or opted out to a given a subscription, they can have the following `status` for a subscription type:

  * `SUBSCRIBED`: contact opted into the subscription type.
  * `UNSUBSCRIBED`: contact opted out of the subscription type.
  * `NOT_SPECIFIED`: contact hasn’t provided opt-in preference for the subscription type.

Learn more about [opt-in consent for email](https://knowledge.hubspot.com/marketing-email/understand-opt-in-consent-for-email).

##

​

Get contacts who unsubscribed from all email communications

Contacts can also opt out of all email communications from your business. To get a list of all contacts who are currently opted out of all email subscription types, make a `POST` request to `/communication-preferences/v4/statuses/batch/unsubscribe-all/read`. If you have the [Brands add-on](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands), you’ll see the `wideStatusType: "BUSINESS_UNIT_WIDE"` field in the response. Note that the default _Account_ brand will always use `"businessUnitId": 0`.

##

​

Get a specific contact who unsubscribed from all email communications

To check whether a specific contact is unsubscribed from all email subscription types, make a `GET` request to `/communication-preferences/v4/statuses/{subscriberIdString}/unsubscribe-all`, where the subscriberIdString is the email address of the contact. If you have the [Brands add-on](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands), you’ll see the `wideStatusType: "BUSINESS_UNIT_WIDE"` field in the response. Note that the default _Account_ brand will always use `"businessUnitId": 0`. For example, to check whether a contact with an email address of `jdoe@example.com` has opted out of all email communications, you’d make a `GET` request to `/communication-preferences/v4/statuses/jdoe@example.com/unsubscribe-all`.

##

​

Update subscription preferences for a specific contact

To update the subscription preferences for a contact, make a `POST` request to `/communication-preferences/v4/statuses/{subscriberIdString}`, where the `subscriberIdString` is the email address of the contact. In the request body, you’ll need to include the fields listed the table below:

Parameter| Type| Description
---|---|---
`subscriptionId`| Number| The internal ID of the subscription type. You can get a full list of subscription IDs by making a `GET` request to `/communication-preferences/v4/statuses/&#123;subscriberIdString&#125;`.
`statusState`| string| The opt-in or opt-out state that you want to update the contact’s subscription to. The possible values are `SUBSCRIBED`, `UNSUBSCRIBED`, or `NOT_SPECIFIED`.
`legalBasis`| string| The legal reason for changing the subscriber’s status. If you data privacy settings turned on, this field is required, along with the `legalBasisExplanation` field.
`legalBasisExplanation`| string| An explanation for the legal basis you provided for updating the subscriber status.
`channel`| string| The channel type for the subscription type. Currently, the only supported channel type is `EMAIL`.

For example, the request body below would subscribe a contact into the subscription associated with the internal ID of `39644612`. You can fetch a list of all subscription types available to get their IDs by making a `GET` request to `/communication-preferences/v4/definitions`.


    // Example request body for POST request to /communication-preferences/v4/statuses/jdoe@exampl.ecom
    {
      "subscriptionId": 39644612,
      "statusState": "SUBSCRIBED",
      "legalBasis": "LEGITIMATE_INTEREST_OTHER",
      "legalBasisExplanation": "Contact mentioned that they mistakenly unsubscribed and they'd like to opt back into our newsletter.",
      "channel": "EMAIL"
    }


##

​

Update a contact’s “Opted out of all email” status

To unsubscribe a contact from all email communication in an account or specific business unit (i.e., “Opted out of all”), make a `POST` request to `/communications-preferences/v4/statuses/{subscriberIdString}/unsubscribe-all`, where the `subscriberIdString` is the email address of the contact.

  * If you have the [Brands add-on](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands), you’ll also need to include the `businessUnitId` query parameter in your request. Note that the _Account_ brand will always use `"businessUnitId": 0`.
  * You can optionally include the `verbose` query parameter to include the details of the updated subscription statuses the contact has unsubscribed from in the response. If you don’t use the `verbose` query parameter, the resulting response will be empty.

Following a successful `POST` request, the contact will be unsubscribed from all email communication from your account. If you have the Brands add-on, the contact will be unsubscribed from all email from the brand specified in your request, but will still be eligible to receive email from other brands in your account.

##

​

Using batch subscription endpoints

If you have an _**Marketing Hub**_ _Enterprise_ account, you can use the bulk subscription endpoints detailed below to fetch and manage subscription statuses for multiple contacts in a single API request.

###

​

Get “Opted out of all communication” subscription status for a list of contacts

To get a list of the _Opted out of all communication_ statuses for multiple contacts across an account or for a specific business unit, you can make a `POST` request to `/communication-preferences/v4/statuses/batch/unsubscribe-all/read`, and provide the following query parameters:

  * `businessUnitId`: if you have the [Brands add-on](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands), you can include this parameter to specify which business unit your contacts will be opted out of all subscription types from. If you don’t provide this query parameter in the URL of your request, then all statuses for the account will be returned across all brands.
  * `channel`: the communication type to unsubscribe all contacts out of. Currently, the only the supported channel is `EMAIL`.

In the body of your request, provide a list of the email addresses for the associated contacts you want to retrieve using the `inputs` field:


    // Example request body for unsubscribing multiple contacts from all subscriptions in an account or business unit
    {
      "inputs": ["test1@hubspot.com"]
    }


For example, if you made a `POST` request to `/communication-preferences/v4/statuses/batch/unsubscribe-all/read?channel=EMAIL`, the resulting response would resemble the following:


    // Example response body for POST request to /communication-preferences/v4/statuses/batch/unsubscribe-all/read
    {
      "status": "COMPLETE",
      "results": [
        {
          "subscriberIdString": "test1@husbpot.com",
          "wideStatuses": [
            {
              "businessUnitId": 0,
              "wideStatusType": "PORTAL_WIDE",
              "subscriberIdString": "string",
              "status": "SUBSCRIBED",
              "channel": "EMAIL",
              "timestamp": "2024-08-02T21:37:58.597Z"
            }
          ]
        },
        {
          "subscriberIdString": "test2@hubspot.com",
          "wideStatuses": [
            {
              "businessUnitId": 0,
              "wideStatusType": "PORTAL_WIDE",
              "subscriberIdString": "string",
              "status": "SUBSCRIBED",
              "channel": "EMAIL",
              "timestamp": "2024-05-22T12:151:01.145Z"
            }
          ]
        }
      ],
      "startedAt": "2024-08-02T19:25:35.063Z",
      "completedAt": "2024-08-02T19:25:35.114Z"
    }


###

​

Get specific subscription statuses for multiple contacts

To get the subscription statuses of multiple contacts in an account or for a specific business unit, make a `POST` request to `/communication-preferences/v4/statuses/batch/read`. If you have the Brands add-on, you can include the `businessUnitId` query parameter to specify which brand your contacts will be opted out of all subscription types from. In the body of your request, provide a list of the email addresses for the associated contacts you want to opted out of all email communications using the `inputs` field:


    // Example request body for unsubscribing multiple contacts from all subscriptions in an account or business unit
    {
      "inputs": ["test1@hubspot.com"]
    }


For example, if you made a `POST` request to `/communication-preferences/v4/statuses/batch/read?channel=EMAIL`, the resulting response would resemble the following:


    // Example response body for POST request to /communication-preferences/v4/statuses/batch/read
    {
      "status": "COMPLETE",
      "results": [
        {
          "subscriberIdString": "test@husbpot.com",
          "statuses": [
            {
              "businessUnitId": 0,
              "channel": "EMAIL",
              "subscriberIdString": "test@husbpot.com",
              "subscriptionId": 88221657,
              "status": "UNSUBSCRIBED",
              "source": "Public status API",
              "legalBasis": null,
              "legalBasisExplanation": null,
              "setStatusSuccessReason": null,
              "timestamp": "2024-08-02T19:28:39.390Z"
            }
          ]
        }
      ],
      "startedAt": "2024-08-02T21:50:28.203Z",
      "completedAt": "2024-08-02T21:50:28.245Z"
    }


###

​

Update the “Opted out of all email” status for multiple contacts

To unsubscribe multiple contacts from all subscription types in an account or for a specific business unit, make a `POST` request to `/communication-preferences/v4/statuses/batch/unsubscribe-all`, and provide the following query parameters in your request:

  * `businessUnitId`: if you have the [Brands add-on](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands), you can include this parameter to specify which brand your contacts will be opted out of all subscription types from.
  * `channel`: the communication type to unsubscribe all contacts out of. Currently, the only the supported channel is `EMAIL`.
  * `verbose`: an optional boolean value that controls if the endpoint returns all the subscriptions that were impacted for all contacts.

In the body of your request, provide a list of the email addresses for the associated contacts you want to opted out of all email communications using the `inputs` field:


    // Example request body for unsubscribing multiple contacts from all subscriptions in an account or business unit
    {
      "inputs": ["test1@hubspot.com", "test2@hubspot.com"]
    }


For example, if you made a `POST` request to `/communication-preferences/v4/statuses/batch/unsubscribe-all?channel=EMAIL&verbose=true`, the resulting response would resemble the following:


    // Example response for POST request to /communication-preferences/v4/statuses/batch/unsubscribe-all?channel=EMAIL&verbose=true
    {
      "status": "COMPLETE",
      "results": [
        {
          "subscriberIdString": "test1@husbpot.com",
          "statuses": [
            {
              "businessUnitId": 0,
              "channel": "EMAIL",
              "subscriberIdString": "test@husbpot.com",
              "subscriptionId": 87914424,
              "status": "UNSUBSCRIBED",
              "source": "Public status API",
              "legalBasis": null,
              "legalBasisExplanation": null,
              "setStatusSuccessReason": "UNSUBSCRIBE_FROM_ALL_OCCURRED",
              "timestamp": "2024-08-02T19:28:39.390Z"
            }
          ]
        },
        {
          "subscriberIdString": "test2@husbpot.com",
          "statuses": [
            {
              "businessUnitId": 0,
              "channel": "EMAIL",
              "subscriberIdString": "test2@husbpot.com",
              "subscriptionId": 87914424,
              "status": "UNSUBSCRIBED",
              "source": "Public status API",
              "legalBasis": null,
              "legalBasisExplanation": null,
              "setStatusSuccessReason": "UNSUBSCRIBE_FROM_ALL_OCCURRED",
              "timestamp": "2024-08-02T19:28:39.390Z"
            }
          ]
        }
      ],
      "startedAt": "2024-08-02T19:25:35.063Z",
      "completedAt": "2024-08-02T19:25:35.114Z"
    }


###

​

Unsubscribe multiple contacts from specific subscription types

To update the specific subscription types of multiple contacts in an account or for a specific business unit, make a `POST` request to `/communication-preferences/v4/statuses/batch/write`, and provide the details of the subscription updates in the inputs field in the body of your request. For example, the following request body would subscribe the contact with an email address of `test@hubspot.com`[](mailto:test@hubspot.com) to the subscription with an ID of 123:


    // Example request body for POST request to /communication-preferences/v4/statuses/batch/write
    {
      "inputs": [
        {
          "subscriptionId": 123,
          "statusState": "SUBSCRIBED",
          "legalBasis": "LEGITIMATE_INTEREST_PQL",
          "legalBasisExplanation": "string",
          "channel": "EMAIL",
          "subscriberIdString": "test@hubspot.com"
        }
      ]
    }


For the example request body above, the resulting response would resemble the following:


    // Example response for POST request to /communication-preferences/v4/statuses/batch/write
    {
      "status": "COMPLETE",
      "results": [
        {
          "businessUnitId": 0,
          "channel": "EMAIL",
          "subscriberIdString": "test@husbpot.com",
          "subscriptionId": 63722844,
          "status": "UNSUBSCRIBED",
          "source": "Public status API",
          "legalBasis": null,
          "legalBasisExplanation": null,
          "setStatusSuccessReason": "RESUBSCRIBE_OCCURRED",
          "timestamp": "2024-08-02T21:46:29.110Z"
        }
      ],
      "startedAt": "2024-08-02T21:46:29.088Z",
      "completedAt": "2024-08-02T21:46:29.228Z"
    }


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)