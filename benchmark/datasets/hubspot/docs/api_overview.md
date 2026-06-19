# 2026-03 API reference

*Source: https://developers.hubspot.com/docs/api/overview*

---

# 2026-03 API reference

Reference documentation for HubSpot’s date-versioned APIs, introduced with the 2026-03 release.

The 2026-03 APIs use a date-based versioning scheme that replaces the previous numeric version paths (e.g., `/crm/v3/`). All endpoints in this section follow the pattern:


    /api-name/2026-03/resource


For example, to retrieve all contacts:


    GET /crm/objects/2026-03/contacts


All APIs, whether legacy, new, or beta, use the same root path as before: `https://api.hubapi.com/`. This versioning model gives HubSpot the ability to ship updates on a predictable schedule. When a new date version is released, the previous version continues to work until its end-of-life date, giving you time to migrate. For new integrations, always use the latest date version. Learn more about this change on [HubSpot’s Developer Changelog](https://developers.hubspot.com/changelog/introducing-date-based-api-versioning). Across the API reference section, use the versioning dropdown menu in the top bar to switch versions. If there’s an equivalent endpoint to the one you’re currently viewing, you’ll automatically be sent there. Otherwise, you’ll land on that version’s home page.

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)