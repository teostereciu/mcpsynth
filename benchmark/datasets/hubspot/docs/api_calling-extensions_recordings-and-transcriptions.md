# Call recordings and transcripts

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/extensions/calling-extensions/recordings-and-transcriptions*

---

Calling extensions

# Call recordings and transcripts

Learn how to log call recordings and their associated transcripts in HubSpot.

Below, learn how to build on top of HubSpot’s [Conversation Intelligence](https://knowledge.hubspot.com/calling/manage-phone-numbers-registered-for-calling#turn-on-conversation-intelligence-sales-hub-or-service-hub-enterprise-only) functionality by integrating external call recordings with logged call activities in HubSpot. This will allow users to play call recordings on CRM record timelines and review transcripts automatically provided by HubSpot.

##

​

Requirements

  * HubSpot will only transcribe calls associated with [users with a paid _Sales_ or _Services_ hub seat](https://knowledge.hubspot.com/account-management/manage-seats).
  * Only `.WAV`, `.FLAC`, and `.MP4` audio files will be transcribed.
  * The audio file must be downloadable as an octet-stream.
  * In the transcription system, HubSpot splits the audio file into its different channels and treats each channel as a separate speaker. If all of the speakers are on the same audio channel, or if the caller or recipient are on an unexpected channel, HubSpot will _not_ be able to transcribe the audio recording. Therefore, each speaker in an audio file should be on a separate channel. For calls with two channels, the caller should be on channel 1, and the call recipient should be on channel 2, regardless of whether the call is inbound or outbound.
  * If your users want to fast forward or rewind a call recording in the HubSpot app, the recording URL needs to respect the `range` header and return a `206 partial content`​ (not a `200` server code).


##

​

Create an endpoint to provide authenticated recording URLs

To list and transcribe calls on a [record’s timeline](https://knowledge.hubspot.com/records/view-the-history-of-an-activity-on-a-record) in HubSpot, create an endpoint that will be invoked to retrieve the authenticated call URLs associated with each engagement. Your endpoint should accept the following parameters:

  * `externalId`: the unique ID associated with a call URL, provided as a path parameter. This will correspond to the same parameter you include in the metadata of your `POST` request to the engagements API, which you can then use in your app’s backend to associate with the recording URL.
  * `externalAccountId`: a unique ID associated with the HubSpot account that made the call engagement, provided as a query parameter. You can use this parameter along with the externalId to identify the call recording.
  * `appId`: the [ID of your app](/docs/apps/legacy-apps/public-apps/overview#find-an-app-s-id), provided as a query parameter.

Your endpoint should return a JSON response with an `authenticatedUrl` field that provides the recording URL.


    {
      "authenticatedUrl": "https://app-test.com/retrieve/authenticated/recordings/test-call-01"
    }


##

​

Register your endpoint with HubSpot

Once your endpoint is ready, make a `POST` request using your app’s ID to `/crm/extensions/calling/2026-03/{appId}/settings/recording`. In the request body, provide the URL of your endpoint in the `urlToRetrieveAuthedRecording` field.

  * Your endpoint’s URL must contain the `%s` character sequence, which HubSpot will substitute with the `externalId` of the engagement when calling your endpoint. The `%s` character sequence can be located anywhere in your URL.
  * Provide the full path of your endpoint URL in your `POST` request, including the `https://` prefix.


    {
      "urlToRetrieveAuthedRecording": "https://app-test.com/retrieve/authenticated/recordings/%s"
    }


If you change the location of your endpoint, you can make a `PATCH` request to `/crm/extensions/calling/2026-03/{appId}/settings/recording` and provide an updated value for `urlToRetrieveAuthedRecording`.

##

​

Log a call using the engagements API

After you’ve registered your calling app’s endpoint with HubSpot, you can log a call by making a `POST` request to `/crm/objects/2026-03/calls`. In the request body, include the engagement data within the `properties` field. The `hs_call_external_id`, `hs_call_external_account_id`, `hs_call_app_id`, and `hs_call_source` properties are required to ensure that HubSpot can fetch the authenticated recording URL.


    {
      "properties": {
        "hs_timestamp": "2021-03-17T01:32:44.872Z",
        "hs_call_title": "Test v3 API",
        "hubspot_owner_id": "11526487",
        "hs_call_body": "Decision maker out, will call back tomorrow",
        "hs_call_duration": "3800",
        "hs_call_from_number": "(555) 555 5555",
        "hs_call_to_number": "(555) 555 5555",
        "hs_call_source": "INTEGRATIONS_PLATFORM", // this has to be INTEGRATIONS_PLATFORM
        "hs_call_status": "COMPLETED",
        "hs_call_app_id": "test-app-01",
        "hs_call_external_id": "test-call-01",
        "hs_call_external_account_id": "test-account-01"
      }
    }


Next, [associate the call with a CRM record](/docs/api-reference/latest/crm/activities/calls/guide#associations) to ensure the transcript appears on the record timeline. To associate the call, make a `PUT` request to `/crm/objects/2026-03/calls/{callId}/associations/{toObjectType}/{toObjectId}`. For example, if the ID of the logged call you created is `17591596434` and the ID of the contact you want to associate it with is `104901`, your request URL would be: `/crm/objects/2026-03/calls/17591596434/associations/contacts/104901` When one of your app’s users navigates to the associated record timeline to view the engagement, HubSpot will call the endpoint you configured to serve the authenticated recording URL. For example, to retrieve the recording URL associated with the example engagement above, HubSpot would make a `GET` request to: `https://app-test.com/retrieve/authenticated/recordings/test-call-01?appId=app-101&externalAccountId=test-account-01`

##

​

Mark a call recording as ready

After logging a call, notify HubSpot that the recording is ready for transcription by making a `POST` request to `/crm/extensions/calling/2026-03/recordings/ready`. In the request body, include the call ID in the `engagementId` field.


    {
      "engagementId": 17591596434
    }


##

​

Review call recordings and transcripts in HubSpot

When a recording is ready, you can review it and the associated transcript by navigating to the record from the [calls index page](https://knowledge.hubspot.com/calling/review-calls-in-the-call-index#review-call-records). Meeting transcripts can also be reviewed from the [sales workspace](https://knowledge.hubspot.com/prospecting/use-meeting-assistant-in-the-prospecting-workspace#follow-up-after-meetings).

Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)