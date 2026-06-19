# CRM API | Owners

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/owners/guide*

---

Owners

# CRM API | Owners

HubSpot uses owners to assign CRM objects to specific people. These endpoints are used to get a list of available owners for an account.

Scope requirements

HubSpot owners [assign](https://knowledge.hubspot.com/records/how-to-set-a-record-owner) specific users to records, activities, or marketing tasks, and can be used in personalization tokens for your content. Owners are automatically created and updated in HubSpot when new users are added or existing owners are synced from [Salesforce](https://knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration). The owners API endpoints are read-only, so you can use them to retrieve an owner’s identifying details, including the owner ID. This identifier can then be used to assign ownership to CRM records in HubSpot, via an integration, or via property change API calls.

##

​

Retrieve a list of owners

To retrieve the current owners in your account, make a `GET` request to `/crm/v3/owners`. The response will return each user’s name, email, ID values, create/update dates, and if applicable, team information. Two ID values are returned, which are used for different purposes:

  * `id`: the ID of the owner. This value should be used when retrieving information about a specific owner, and when assigning an owner to a record or activity.
  * `userId`: the ID of the user. This value can be used to specify users in the [settings API](/docs/api-reference/legacy/account/settings/user-provisioning/guide), but will result in an error if it is used to assign ownership.

Your response will look similar to the following:


    {
      "results": [
        {
          "id": "41629779",
          "email": "email@hubspot.com",
          "type": "PERSON",
          "firstName": "HubSpot",
          "lastName": "Test Owner",
          "userId": 9586504,
          "userIdIncludingInactive": 9586504,
          "createdAt": "2019-12-25T13:01:35.228Z",
          "updatedAt": "2023-08-22T13:40:26.790Z",
          "archived": false,
          "teams": [
            {
              "id": "368389",
              "name": "Sales Team",
              "primary": true
            }
          ]
        },
        {
          "id": "60158084",
          "email": "email@gmail.com",
          "type": "PERSON",
          "firstName": "Test",
          "lastName": "Email",
          "userId": 9274996,
          "userIdIncludingInactive": 9274996,
          "createdAt": "2021-02-10T17:59:04.891Z",
          "updatedAt": "2023-02-09T17:41:52.767Z",
          "archived": false,
          "teams": [
            {
              "id": "368389",
              "name": "Sales Team",
              "primary": true
            }
          ]
        },
        {
          "id": "81538190",
          "email": "salesmanager@hubspot.com",
          "type": "PERSON",
          "firstName": "Sales",
          "lastName": "Manager Example",
          "userId": 3892666,
          "userIdIncludingInactive": 3892666,
          "createdAt": "2021-05-27T16:55:57.242Z",
          "updatedAt": "2022-08-02T18:34:35.039Z",
          "archived": false
        }
      ]
    }


You can also retrieve archived owners to view users that were deactivated. To do so, add the `archived` parameter with the value `true`. For archived users, there is still an `id` value, but the `userId` value will be `null`. The user ID is instead stored in the `userIdIncludingInactive` field. For example:


    {
      "results": [
        {
          "id": "42103462",
          "email": "useremail@hubspot.com",
          "type": "PERSON",
          "firstName": "",
          "lastName": "",
          "userId": null,
          "userIdIncludingInactive": 9685555,
          "createdAt": "2020-01-09T20:28:50.080Z",
          "updatedAt": "2020-01-09T20:28:50.080Z",
          "archived": true
        }
      ]
    }


##

​

Retrieve information about an individual owner

To retrieve a specific owner, make a `GET` request to `/crm/v3/owners/{ownerId}`. You should use the `id` value to specify the owner for which you want more details.

**Please note:** The `updatedAt` value in the response changes based on updates to the Owner object itself. It will not be updated for changes to the User object. For example, changing a user’s permissions will _not_ update the `updatedAt` value.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)