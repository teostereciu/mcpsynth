# Account information API

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/account-information/guide*

---

Account information

# Account information API

HubSpot’s account information API endpoints provide account configuration and usage data.

Scope requirements

The following endpoints provide information about a given HubSpot account, including the account settings, and the daily API usage and limits for [legacy private apps](/docs/apps/legacy-apps/private-apps/overview).

##

​

Get account details for a HubSpot account

To retrieve details for a standard HubSpot account, make a `GET` request to `/account-info/2026-03/details`. The response will resemble the following:


    {
      "portalId": 123456,
      "accountType": "STANDARD",
      "timeZone": "US/Eastern",
      "companyCurrency": "USD",
      "additionalCurrencies": [
        "EUR"
      ],
      "utcOffset": "-05:00",
      "utcOffsetMilliseconds": -18000000,
      "uiDomain": "app.hubspot.com",
      "dataHostingLocation": "na1"
    }


A full list of properties is provided in the table below:

Property| Type| Description
---|---|---
`portalId`| Number| The ID of the HubSpot account, sometimes referred to as the account’s [Hub ID](https://knowledge.hubspot.com/account-management/manage-multiple-hubspot-accounts#check-your-current-account).
`accountType`| String| An enumeration corresponding to the [account type](/docs/getting-started/account-types):

  * `STANDARD`: a [standard HubSpot account](/docs/getting-started/account-types#standard-hubspot-accounts).
  * `DEVELOPER_TEST`: a [developer test account](/docs/getting-started/account-types#developer-test-accounts).
  * `SANDBOX`: a [sandbox](/docs/getting-started/account-types#sandbox-accounts) account.
  * `APP_DEVELOPER`: a [legacy developer account](/docs/getting-started/account-types#developer-accounts).


`timeZone`| String| The name of the account’s [configured timezone](https://knowledge.hubspot.com/account-management/change-your-language-and-region-settings#customize-your-account-time-zone) (e.g., `"US/Eastern"`).
`companyCurrency`| String| The currency code of the account’s [configured currency](https://knowledge.hubspot.com/account-management/add-and-edit-your-account-currencies).
`additionalCurrencies`| Array| An array of [additional](https://knowledge.hubspot.com/account-management/add-and-edit-your-account-currencies#configure-new-currencies) configured currencies. Note that a _Starter_ account or higher is required to add more than one account currency.
`utcOffset`| String| The difference in hours between the account’s timezone and Coordinated Universal Time (UTC).
`utcOffsetMilliseconds| Number| The difference in milliseconds between the account’s timezone and Coordinated Universal Time (UTC).
`uiDomain`| String| The domain used to log in to the main HubSpot user interface.
`dataHostingLocation`| String| The location of the data center where your account is hosted (e.g., `"eu1"` or `"na1"`).

##

​

Check daily API usage and limits for a legacy private app

The daily API usage endpoint can be used to check the aggregate API calls that all legacy private apps have made for the current day, and the API usage limits for that account. The current day is measured from midnight to midnight based on the connected account’s time zone settings. Read more about HubSpot’s [API usage guidelines](/docs/developer-tooling/platform/usage-guidelines). To retrieve usage and limit data for your [legacy private apps](/docs/apps/legacy-apps/private-apps/overview), make a `GET` request to `/account-info/2026-03/api-usage/daily/private-apps`. The response will resemble the following:


    {
      "results": [
        {
          "name": "private-apps-api-calls-daily",
          "usageLimit": 1000000,
          "currentUsage": 2,
          "collectedAt": "2025-12-12T22:25:10.655Z",
          "fetchStatus": "SUCCESS",
          "resetsAt": "2025-12-13T05:00:00Z"
        }
      ]
    }


The table below provides details on the properties returned in the `results` array of the response:

Property| Type| Description
---|---|---
`name`| String| An identifier used by HubSpot for the API call.
`usageLimit`| Number| The [daily limit](/docs/developer-tooling/platform/usage-guidelines#privately-distributed-app-limits) for your legacy private apps.
`currentUsage`| Number| The total number of calls your legacy private apps have made during the current period (starting from midnight of the current day).
`collectedAt`| String| An ISO 8601 timestamp denoting when usage was measured.
`fetchStatus`| String| An enumeration denoting the status of the usage request.
`resetsAt`| String| An ISO 8601 timestamp denoting when the current period of usage will reset.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)