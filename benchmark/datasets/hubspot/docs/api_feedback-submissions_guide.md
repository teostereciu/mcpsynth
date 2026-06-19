# Survey responses

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/feedback-submissions/guide*

---

Feedback Submissions

# Survey responses

Survey response records store information about individual survey responses. The API endpoints allow you to manage this data and sync it between HubSpot and other systems.

Scope requirements

In HubSpot, survey responses store information submitted to one of your surveys. Surveys in HubSpot include [Net Promoter Score (NPS)](https://knowledge.hubspot.com/customer-feedback/how-do-i-send-a-customer-loyalty-survey), [Customer Satisfaction (CSAT)](https://knowledge.hubspot.com/customer-feedback/create-and-send-customer-satisfaction-surveys), [Customer Effort Score (CES)](https://knowledge.hubspot.com/customer-feedback/how-do-i-send-a-customer-support-survey), and [custom surveys](https://knowledge.hubspot.com/customer-feedback/create-a-custom-survey). You can use these endpoints to retrieve response data from your surveys. This API is read-only, so you cannot use it to create, update, or delete survey response data in HubSpot. Learn more about objects, properties, and associations APIs in the [Understanding the CRM](/docs/guides/crm/understanding-the-crm) guide.

##

​

Retrieve survey responses

To view details about your survey responses, you can retrieve data in bulk for multiple surveys, or for an individual survey. For example, you can use the API to see all survey responses for a specific NPS survey. To retrieve submissions, make a `GET` request to `/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}`. By default, the following properties are returned for each submission: `hs_createdate`, `hs_lastmodifieddate`, and `hs_object_id`, but you also can retrieve additional [properties](https://knowledge.hubspot.com/customer-feedback/survey-response-properties). For example, to retrieve survey submissions with the source and sentiment of the submissions, your request URL would look like: `https://api.hubspot.com/crm/v3/objects/feedback_submissions?properties=hs_sentiment,hs_survey_channel`.

##

​

Survey response properties

Survey responses have [default properties](https://knowledge.hubspot.com/customer-feedback/survey-response-properties#default-feedback-submission-properties) that contain information about the survey, submission answers, and the date the survey was submitted. You can also [create custom submissions properties](https://knowledge.hubspot.com/customer-feedback/survey-response-properties#custom-feedback-submission-properties). Survey response properties _cannot_ be created or edited via API. You can only create properties in the [survey response tool within HubSpot](https://knowledge.hubspot.com/customer-feedback/create-a-custom-survey#survey), and the properties cannot be edited after creation.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)