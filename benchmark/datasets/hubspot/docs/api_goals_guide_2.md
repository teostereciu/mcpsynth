# CRM API | Goals

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/goals/guide*

---

Goals

# CRM API | Goals

Goals are used to create user-specific quotas for their sales and services teams based on templates provided by HubSpot. The goals endpoints allow you to sync this data between HubSpot and other systems.

Scope requirements

In HubSpot, goals are used to create user-specific quotas for their sales and services teams based on templates provided by HubSpot. The goals API allow you to retrieve goals data in your HubSpot account. Learn more about [using goals in HubSpot](https://knowledge.hubspot.com/reports/create-sales-goals).

##

​

Understanding Goal Architecture

Unlike standard objects (like Deals or Contacts) which exist as single rows, a “Goal” in HubSpot is a container for multiple time-bound objects. To successfully create or manage goals, you must understand the hierarchy of the three key components: **Goal Family** , **Goal Target Group** , and **Goal Target**.

###

​

The Goal Hierarchy

The API defines a goal using a nesting structure linked by specific IDs.

####

​

Goal Family (The “Goal”)

This is what a user perceives as “One Goal” (e.g., “2025 Revenue Quota”). It is identified by the `hs_group_correlation_uuid`. This ID links every time-slice together into one cohesive unit.

In your account, all targets (whether weekly, monthly, quarterly, or yearly) appear under a single goal name (e.g., Calls made) because they share the same `hs_group_correlation_uuid`. If this ID differs across targets, they will appear as separate goals.

####

​

Goal Target Group (The Schedule)

This represents the schedule or assignment constraints (e.g., “Monthly targets for User A”). It is identified by the `hs_goal_target_group_id`. All time periods for that specific user’s schedule share this ID.

In your account, this determines which targets are grouped together for a specific assignment. For user goals, the `hubspot_owner_id` property determines who sees this goal in their dashboard. For team goals, the `hs_assignee_team_id` (or `hubspot_team_id`) property is used instead to assign the goal to the entire team.

####

​

Goal Target (The Time Slice)

These are the individual objects holding the data. For a monthly goal, there are 12 separate `goal_target` objects (Jan, Feb, Mar…). Each has its own `hs_start_datetime` and `hs_target_amount`.

In your account, each target appears as a distinct column in the goal timeline, showing the specific target for that period and tracking progress against that individual slice.

###

​

Example: Structure of a Monthly Goal

The JSON below illustrates two separate goal objects: one for January and one for February. While the target data (dates and amounts) changes for each month, they belong to the same **Goal Family** and **Goal Target Group**. As shown in the highlighted lines, the `hs_goal_name`, `hs_group_correlation_uuid`, and `hs_goal_target_group_id` remain constant to link these objects into a single cohesive goal schedule.


    [
      {
        "properties": {
          "hs_goal_name": "2025 Revenue Quota",
          "hs_group_correlation_uuid": "40499cb1-d8e7-495d-a1c7-07e3ed4b5468",
          "hs_goal_target_group_id": "1234567",
          "hubspot_owner_id": "901831746",
          "hs_start_datetime": "2025-01-01T00:00:00Z",
          "hs_end_datetime": "2025-01-31T23:59:59.999Z",
          "hs_target_amount": "5000.00"
        }
      },
      {
        "properties": {
          "hs_goal_name": "2025 Revenue Quota",
          "hs_group_correlation_uuid": "40499cb1-d8e7-495d-a1c7-07e3ed4b5468",
          "hs_goal_target_group_id": "1234567",
          "hubspot_owner_id": "901831746",
          "hs_start_datetime": "2025-02-01T00:00:00Z",
          "hs_end_datetime": "2025-02-28T23:59:59.999Z",
          "hs_target_amount": "6000.00"
        }
      }
    ]


##

​

Retrieve goals

To retrieve goals, make a request in one of the following ways:

  * **Retrieve a single target:** `GET /crm/objects/2026-03/goal_targets/{goalTargetId}/`
  * **Retrieve all targets:** `GET /crm/objects/2026-03/goal_targets`
  * **Search for targets:** `POST /crm/objects/2026-03/goal_targets/search`

To retrieve goals that meet a specific set of criteria (filtering), you can make a `POST` request to the search endpoint and include filters in the request body. Learn more about [searching the CRM](/docs/api-reference/latest/crm/search-the-crm). For example, to retrieve a goal with an ID of `44027423340`, the request URL would be the following: `https://api.hubapi.com/crm/objects/2026-03/goal_targets/44027423340/` The response will include a few default properties, including the create date, last modified date.


    {
      "id": "87504620389",
      "properties": {
        "hs_createdate": "2021-11-30T22:18:49.923Z",
        "hs_lastmodifieddate": "2023-12-11T19:21:32.851Z",
        "hs_object_id": "87504620389"
      },
      "createdAt": "2021-11-30T22:18:49.923Z",
      "updatedAt": "2023-12-11T19:21:32.851Z",
      "archived": false
    }


To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. Learn more about goal properties below. For example, making a `GET` request to the following URL would result in the response below: `crm/objects/2026-03/goal_targets/{goalTargetId}?properties=hs_goal_name,hs_target_amount`


    {
      "id": "87504620389",
      "properties": {
        "hs_createdate": "2021-11-30T22:18:49.923Z",
        "hs_lastmodifieddate": "2023-12-11T19:21:32.851Z",
        "hs_object_id": "87504620389"
      },
      "createdAt": "2021-11-30T22:18:49.923Z",
      "updatedAt": "2023-12-11T19:21:32.851Z",
      "archived": false
    }


##

​

Create goals

To create goals, make a `POST` request to `/crm/objects/2026-03/goal_targets/batch/create`. To ensure these objects appear as a single goal in the UI, your batch request must adhere to specific architectural constraints:

  * **Shared Identifiers:** Every target object in the batch must share the same `hs_group_correlation_uuid` and `hs_goal_target_group_id`. This links them into a “Goal Family”.
  * **Sequential Dates:** You must increment the `hs_start_datetime` and `hs_end_datetime` for each object. For monthly goals, start dates must be the first millisecond of the month, and end dates must be the last millisecond of the month.
  * **Milestone Accuracy:** The number of objects must match the `hs_milestone` frequency (e.g., creating 12 objects for a “monthly” milestone).

This example shows the creation of the first two months of an annual sales quota goal. Note that the UUIDs remain constant while the dates increment. `/crm/objects/2026-03/goal_targets/batch/create`


    {
      "inputs": [
        {
          "properties": {
            "hs_goal_name": "Sales Quota 2027",
            "hs_milestone": "monthly",
            "hs_goal_type": "sales_quota",
            "hs_target_amount": "1200.00",
            "hs_start_datetime": "2027-01-01T00:00:00Z",
            "hs_end_datetime": "2027-01-31T23:59:59.999Z",
            "hs_group_correlation_uuid": "40499cb1-d8e7-495d-a1c7-07e3ed4b5468",
            "hs_goal_target_group_id": "1234567"
          }
        },
        {
          "properties": {
            "hs_goal_name": "Sales Quota 2027",
            "hs_milestone": "monthly",
            "hs_goal_type": "sales_quota",
            "hs_target_amount": "1200.00",
            "hs_start_datetime": "2027-02-01T00:00:00Z",
            "hs_end_datetime": "2027-02-28T23:59:59.999Z",
            "hs_group_correlation_uuid": "40499cb1-d8e7-495d-a1c7-07e3ed4b5468",
            "hs_goal_target_group_id": "1234567"
          }
        }
      ]
    }


##

​

Update Goals

To update goals, make a request in one of the following ways:

  * **Update a single target:** `PATCH /crm/objects/2026-03/goal_targets/{goalTargetId}`
  * **Batch update multiple targets:** `POST /crm/objects/2026-03/goal_targets/batch/update`

Because a “Goal” consists of multiple independent objects (e.g., 12 monthly targets), you must choose the correct update method to avoid breaking the goal structure in the UI.

  * **When to use Single Update (`PATCH`):** Use this when changing data specific to one time slice.
    * **Example:** Changing the `hs_target_amount` for just the month of October.
    * **Example:** Manually overriding the `hs_kpi_value` for a specific month.
  * **When to use Batch Update (`POST`):** Use this when changing properties that define the **Goal Family**. If you change these on one object but not the others, the goal may disappear from the UI or appear as duplicates.
    * **Example:** Renaming the goal (`hs_goal_name`). You must update all 12 targets.
    * **Example:** Changing the pipeline (`hs_pipeline_ids`). You must update all 12 targets.

This example shows updates to the target amount for a specific month and triggers a notification to the user. `PATCH /crm/objects/2026-03/goal_targets/{goalTargetId}`


    {
      "properties": {
        "hs_target_amount": "5500.00",
        "hs_should_notify_on_edit_updates": "true"
      }
    }


##

​

Delete Goals

To delete goals, make a request in one of the following ways:

  * **Delete a single target:** `DELETE /crm/objects/2026-03/goal_targets/{goalTargetId}`
  * **Batch delete multiple targets:** `POST /crm/objects/2026-03/goal_targets/batch/archive`

Because a standard goal consists of multiple distinct objects (e.g., 12 monthly targets), you must understand the scope of your deletion request.

  * **Deleting a Single Target (`DELETE`):** If you use the `DELETE` endpoint on a single ID, you are removing only that specific slice of time.
    * **Example:** If you delete the target for “January,” the goal will still exist in the UI for February through December. The goal family remains active, but the start date or total target amount may calculate incorrectly in reports.
  * **Deleting a Goal Family (`POST`):** To completely remove a goal (e.g., “2025 Revenue Quota”) from the system, you must delete every target object associated with that goal’s `hs_group_correlation_uuid`.
    * **Example:** You must first query the goal targets to retrieve all IDs associated with the Goal Family, and then use the batch archive endpoint to delete them all simultaneously.

This example shows the deletion of an entire quarterly goal. You must include the IDs for all four quarters in the batch archive request. `POST /crm/objects/2026-03/goal_targets/batch/archive`


    {
      "inputs": [
        {"id": "11111"},
        {"id": "22222"},
        {"id": "33333"},
        {"id": "44444"}
      ]
    }


##

​

Goals properties

When making a `GET` request to the Goals API, you can also request specific goal properties. For example, if you wanted to include properties such as `hs_goal_name`, `hs_target_amount`, `hs_start_datetime`, `hs_end_datetime`, and `hs_created_by_user_id`, the request URL may resemble the following: `https://api.hubapi.com/crm/objects/2026-03/goal_targets/44027423340?properties=hs_goal_name,hs_target_amount,hs_start_datetime,hs_end_datetime,hs_created_by_user_id` The response may look similar to the JSON excerpt below:


    {
      "id": "44027423340",
      "properties": {
        "hs_created_by_user_id": "885536",
        "hs_createdate": "2023-02-15T15:53:07.080Z",
        "hs_end_datetime": "2024-01-01T00:00:00Z",
        "hs_goal_name": "Revenue Goal 2023",
        "hs_lastmodifieddate": "2023-02-16T10:02:21.131Z",
        "hs_object_id": "44027423340",
        "hs_start_datetime": "2023-12-01T00:00:00Z",
        "hs_target_amount": "2000.00"
      },
      "createdAt": "2023-02-15T15:53:07.080Z",
      "updatedAt": "2023-02-16T10:02:21.131Z",
      "archived": false
    }


The available properties and their descriptions can be found in the Goal Property Glossary below.

##

​

Goal Property Glossary

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)