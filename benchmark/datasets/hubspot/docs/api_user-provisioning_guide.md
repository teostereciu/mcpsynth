# Settings API | User provisioning

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/user-provisioning/guide*

---

User Provisioning

# Settings API | User provisioning

The user provisioning endpoints allow you to provision and deprovision HubSpot users programmatically.

Scope requirements

Use the user provisioning API to create and manage users in the account, along with their permissions. You can also set user `firstName` and `lastName` properties through this API. To retrieve and update other user information, such as their job title and working hours, use the [users API](/docs/api-reference/latest/crm/objects/users/guide) instead.

##

​

Specifying a user

When specifying a user with the `userId` path parameter, you can either use the user’s ID or the user’s email. Specifying based on the user’s ID is the default behavior but if you want to use the user’s email, you can use the query parameter `idProperty` to set that. The following `GET` request would fetch a user with the email `myUser@gmail.com`: `https://api.hubspot.com/settings/users/2026-03/myUser@gmail.com?idProperty=EMAIL` You can set the `idProperty` query parameter in any endpoint that takes in `userId` as a path parameter.

##

​

Permission sets

HubSpot accounts can define permission sets to easily manage multiple users’ permissions at once. Once you’ve created a role and specified certain permissions for it, you can then assign new and existing users the role to grant them the same permissions. Permission sets that have paid seats attached to them can only be modified by applications that have the `billing-write` scope. The following is an example of a role definition for a user:


    {
      "id": "1234",
      "name": "a new role",
      "requiresBillingWrite": false
    }


Note that permission sets must be [created in the app](https://knowledge.hubspot.com/user-management/create-permission-sets) before attempting to assign them to users.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)