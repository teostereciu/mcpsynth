# CRM API | Pipelines

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/pipelines/guide*

---

Pipelines

# CRM API | Pipelines

The Pipelines endpoints are used to view, create, and manage pipelines in the HubSpot CRM and service tools.

Scope requirements

In HubSpot, a pipeline is where records are tracked through stages. For example, sales pipelines can be used to predict revenue and identify roadblocks or service pipelines can be used to manage ticket statuses and analyze blockers. Depending on your [subscription](https://legal.hubspot.com/hubspot-product-and-services-catalog), you can create multiple pipelines for an object. For example, when working with deals, an account might have one pipeline for _New Sales_ and another for _Contract Renewals_. Pipelines are available for the following [objects](/docs/guides/crm/understanding-the-crm):

  * Deals
  * Tickets
  * Appointments
  * Courses
  * Listings
  * Orders
  * Services
  * Leads (_**Sales Hub**_ _Professional_ and _Enterprise_ only)
  * Custom objects (_Enterprise_ only)


##

​

Manage pipelines

###

​

Create a pipeline

Accounts with a _Starter_ , _Professional_ , or _Enterprise_ subscription can create additional pipelines. If your account has a _**Sales Hub**_ subscription, you can create [multiple deal pipelines.](https://knowledge.hubspot.com/object-settings/set-up-and-customize-pipelines) If your account has a _**Service Hub**_ subscription, you can create multiple [ticket pipelines](https://knowledge.hubspot.com/object-settings/set-up-and-customize-pipelines). To create a new pipeline, make a `POST` request to `/crm/v3/pipelines/{objectType}`. In the request body, include the following:

  * `displayOrder`: a number that decides the order the pipeline is displayed within all pipelines of the object. If multiple pipelines are the same number in the order, they’ll be listed alphabetically by label.
  * `label`: the name of the pipeline as it is displayed in HubSpot.
  * `stages`: inputs to set the stages in the pipeline. For each stage, include the following:
    * `metadata`: properties related to the stage, optional for all objects except deals. For deals, `probability` is required with a value between `0.0` and `1.0`, `0.0` being _Closed Lost_ and `1.0` being _Closed Won_. For tickets, you can include `ticketState`with a value of either `OPEN` or `CLOSED`.
    * `displayOrder`: a number that decides the order in which the stage will be displayed.
    * `label`: the stage name. This must be unique for each stage.


**Please note:** Appointment, course, listing, lead, order, and service pipelines can have up to 30 stages. Deal, ticket, and custom object pipelines can have up to 100 stages.

For example, to create a new deal pipeline, your request may look like the following:


    {
      "displayOrder": 3,
      "label": "New deal pipeline",
      "stages": [
        {
          "label": "In Progress",
          "metadata": {
            "probability": "0.2"
          },
          "displayOrder": 0
        },
        {
          "label": "Contract signed",
          "metadata": {
            "probability": "0.8"
          },
          "displayOrder": 1
        },
        {
          "label": "Closed Won",
          "metadata": {
            "probability": "1.0"
          },
          "displayOrder": 2
        },
        {
          "label": "Closed Lost",
          "metadata": {
            "probability": "0.0"
          },
          "displayOrder": 3
        }
      ]
    }


###

​

Replace a pipeline

If there’s an existing pipeline you want to replace instead of creating a new pipeline, make a `PUT` request to `/crm/v3/pipelines/{objectType}/{pipelineId}` with the `id` of the pipeline to replace. In the request body, include the fields required when creating a new pipeline. The information you add in the request body will overwrite the existing pipeline’s details.

###

​

Retrieve pipelines

  * To retrieve all pipelines for an object, make a `GET` request to `/crm/v3/pipelines/{objectType}`. Each pipeline’s `id`, `label`, and `displayOrder` values will be returned, along with information about when it was created or updated. You can use the `id` values to retrieve and update individual pipelines.
  * To retrieve an individual pipeline, make a `GET` request to `/crm/v3/pipelines/{objectType}/{pipelineId}`.


###

​

Update a pipeline

To edit a pipeline’s details, such as label or display order, make a `PATCH` request to `/crm/v3/pipelines/{objectType}/{pipelineId}`. In the request body, include the properties to update. If you want to edit a pipeline’s stages, use the stage endpoints.

###

​

Delete a pipeline

To delete a pipeline, make a `DELETE` request to `/crm/v3/pipelines/{objectType}/{pipelineId}`. To check if there are records in the pipeline, include the `validateReferencesBeforeDelete` parameter with a value of `true`. When the parameter is included, you’ll be notified of existing records and cannot delete the pipeline until the records have been deleted or moved to a different pipeline. If there are existing records, your response will look similar to the following:


    {
      "status": "error",
      "message": "Stage IDs: [renter_viewing, renter_security_deposit_paid, renter_new_lead, renter_closed_won, renter_closed_lost] are being referenced by object IDs: [22901690010]",
      "correlationId": "1fb9ac01-f574-4919-bf55-2c8c25ac1507",
      "context": {
        "stageIds": [
          "[renter_viewing, renter_security_deposit_paid, renter_new_lead, renter_closed_won, renter_closed_lost]"
        ],
        "objectIds": ["[22901690010]"]
      },
      "category": "VALIDATION_ERROR",
      "subCategory": "PipelineError.STAGE_ID_IN_USE"
    }


##

​

Manage pipeline stages

###

​

Create a stage

To add a new stage to a pipeline, make a `POST` request to `/crm/v3/pipelines/{objectType}/{pipelineId}/stages`. In the request body, include the following:

  * `displayOrder`: a number that decides the order of the stage in the pipeline. If multiple stages are the same number in the order, they’ll be listed alphabetically by label.
  * `label`: the name of the stage as it is displayed in HubSpot.
  * `metadata`: an object that includes properties for the stage, optional for all objects except deals. For deals, `probability` is required with a value between `0.0` and `1.0`, `0.0` being _Closed Lost_ and `1.0` being _Closed Won_. For tickets, you can include `ticketState` with a value of `OPEN` or `CLOSED`.


**Please note:** Appointment, course, listing, lead, order, and service pipelines can have up to 30 stages. Deal, ticket, and custom object pipelines can have up to 100 stages.

For example, to add a stage called _Contract signed_ as the fifth stage in a pipeline, your request would look like:


    {
      "metadata": {
        "probability": "0.8"
      },
      "displayOrder": 4,
      "label": "Contract signed"
    }


###

​

Replace a stage

If there’s an existing pipeline stage you want to replace instead of creating a new stage, make a `PUT` request to `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}` with the `id` of the stage to replace. In the request body, include the fields required when creating a new stage. The information you add in the request body will overwrite the existing stage’s details.

###

​

Retrieve stages

  * To retrieve all stages in a pipeline, make a `GET` request to `/crm/v3/pipelines/{objectType}/{pipelineId}/stages`. Each stage’s `id`, `label`, and `displayOrder` values will be returned, along with information about when it was created or updated. You can use the `id` values to retrieve and update individual stages.
  * To retrieve an individual stage, make a `GET` request to `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}`.


###

​

Update a stage

To edit a stage’s details, such as label or display order, make a `PATCH` request to `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}`. In the request body, include the properties to update.

###

​

Delete a stage

To delete a pipeline stage, make a `DELETE` request to `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}`.

##

​

Track changes to pipelines and stages

You can use the audit endpoints to track changes made to your pipelines and pipeline stages.

  * To view changes made to a pipeline, make a `GET` request to `/crm/v3/pipelines/{objectType}/{pipelineId}/audit`.
  * To view changes made to a stage, make a `GET` request to `/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}/audit`.

In the response, updates are listed in reverse chronological order with details about the type of action, when it occurred, and who made the change. For example, when auditing changes to a pipeline, your response would look like the following:


    {
      "results": [
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2024-10-07T20:58:57.414Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"objectType\":\"DEAL\",\"objectTypeId\":\"0-3\",\"version\":11,\"label\":\"Partner pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334737395,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":1,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334737395,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":2,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334737395,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":3,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334737395,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":4,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334737395,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":5,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"259717454\",\"label\":\"Contract signed\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1728334734115,\"updatedAt\":1728334737395,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":6,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"true\",\"probability\":\"1.0\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334737395,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":7,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334737395,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null}],\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334737395,\"limitExempt\":false,\"autoCloseDateEnabled\":true,\"clearCloseDateWhenMovingClosedToOpen\":false,\"permission\":null,\"createStageId\":null,\"inactiveDefaultPipeline\":false,\"default\":false}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2024-10-07T20:58:54.143Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"objectType\":\"DEAL\",\"objectTypeId\":\"0-3\",\"version\":10,\"label\":\"Partner pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334734115,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":1,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334734115,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":2,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334734115,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":3,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334734115,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":4,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334734115,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":5,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"true\",\"probability\":\"1.0\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334734115,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":6,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334734115,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null},{\"displayOrder\":7,\"portalId\":123456,\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"stageId\":\"259717454\",\"label\":\"Contract signed\",\"metadata\":{\"probability\":\"0.2\",\"isClosed\":\"false\"},\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1728334734115,\"updatedAt\":1728334734115,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"internalWriteOnly\":false,\"active\":true,\"isApprovalStage\":null}],\"createdBy\":9586504,\"updatedBy\":9586504,\"createdAt\":1614359253457,\"updatedAt\":1728334734115,\"limitExempt\":false,\"autoCloseDateEnabled\":true,\"clearCloseDateWhenMovingClosedToOpen\":false,\"permission\":null,\"createStageId\":null,\"inactiveDefaultPipeline\":false,\"default\":false}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2023-07-27T15:30:01.098Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Partner pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"true\",\"probability\":\"1.0\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null}],\"version\":8,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2023-03-17T17:37:42.613Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Partner pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null}],\"version\":7,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2023-03-17T17:31:59.276Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Partner pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null}],\"version\":6,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2023-03-17T17:29:18.824Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Partner pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null}],\"version\":5,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2022-12-09T20:29:21.004Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Partner pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null}],\"version\":null,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2022-11-08T14:32:11.024Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Additional pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null}],\"version\":null,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2022-11-08T14:31:58.571Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Additional pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"writePermissions\":\"CRM_PERMISSIONS_ENFORCEMENT\",\"isInternalWriteOnly\":null}],\"version\":null,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2022-05-11T17:49:38.304Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Additional pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":9586504,\"updatedAt\":1652291367982,\"internalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":9586504,\"updatedAt\":1652291367982,\"internalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":9586504,\"updatedAt\":1652291367982,\"internalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":9586504,\"updatedAt\":1652291367982,\"internalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":9586504,\"updatedAt\":1652291367982,\"internalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"true\",\"probability\":\"0.8\"},\"updatedBy\":9586504,\"updatedAt\":1652291367982,\"internalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"true\",\"probability\":\"0.8\"},\"updatedBy\":9586504,\"updatedAt\":1652291367982,\"internalWriteOnly\":null}],\"version\":1,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "UPDATE",
          "timestamp": "2022-05-11T17:49:28.001Z",
          "message": "Pipeline update",
          "rawObject": "{\"displayOrder\":1,\"pipelineId\":\"11348541\",\"portalId\":123456,\"label\":\"Additional pipeline\",\"active\":true,\"stages\":[{\"displayOrder\":0,\"stageId\":\"11348542\",\"label\":\"Appointment scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"updatedBy\":null,\"updatedAt\":null,\"internalWriteOnly\":null},{\"displayOrder\":1,\"stageId\":\"11348543\",\"label\":\"Qualified to buy\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"updatedBy\":null,\"updatedAt\":null,\"internalWriteOnly\":null},{\"displayOrder\":2,\"stageId\":\"11348544\",\"label\":\"Presentation scheduled\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"updatedBy\":null,\"updatedAt\":null,\"internalWriteOnly\":null},{\"displayOrder\":3,\"stageId\":\"11348545\",\"label\":\"Decision Maker Bought-In\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"internalWriteOnly\":null},{\"displayOrder\":4,\"stageId\":\"11348546\",\"label\":\"Contract sent\",\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"updatedBy\":null,\"updatedAt\":null,\"internalWriteOnly\":null},{\"displayOrder\":5,\"stageId\":\"11348547\",\"label\":\"Closed won\",\"metadata\":{\"isClosed\":\"true\",\"probability\":\"0.8\"},\"updatedBy\":null,\"updatedAt\":null,\"internalWriteOnly\":null},{\"displayOrder\":6,\"stageId\":\"11348548\",\"label\":\"Closed lost\",\"metadata\":{\"isClosed\":\"true\",\"probability\":\"0.0\"},\"updatedBy\":null,\"updatedAt\":null,\"internalWriteOnly\":null}],\"version\":0,\"updatedBy\":null}",
          "fromUserId": 9586504
        },
        {
          "portalId": 123456,
          "identifier": "123456:11348541",
          "action": "CREATE",
          "timestamp": "2021-02-26T17:07:35.013Z",
          "message": "User defined. pipeline created",
          "rawObject": "{\"label\":\"Additional pipeline\",\"displayOrder\":1,\"active\":true,\"stages\":[{\"label\":\"Appointment scheduled\",\"displayOrder\":0,\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.2\"},\"portalId\":123456,\"pipelineId\":\"11348541\",\"stageId\":\"11348542\",\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":null,\"createdAt\":1614359253457,\"updatedAt\":null,\"active\":true},{\"label\":\"Qualified to buy\",\"displayOrder\":1,\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.4\"},\"portalId\":123456,\"pipelineId\":\"11348541\",\"stageId\":\"11348543\",\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":null,\"createdAt\":1614359253457,\"updatedAt\":null,\"active\":true},{\"label\":\"Presentation scheduled\",\"displayOrder\":2,\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.6\"},\"portalId\":123456,\"pipelineId\":\"11348541\",\"stageId\":\"11348544\",\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":null,\"createdAt\":1614359253457,\"updatedAt\":null,\"active\":true},{\"label\":\"Decision Maker Bought-In\",\"displayOrder\":3,\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.8\"},\"portalId\":123456,\"pipelineId\":\"11348541\",\"stageId\":\"11348545\",\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":null,\"createdAt\":1614359253457,\"updatedAt\":null,\"active\":true},{\"label\":\"Contract sent\",\"displayOrder\":4,\"metadata\":{\"isClosed\":\"false\",\"probability\":\"0.9\"},\"portalId\":123456,\"pipelineId\":\"11348541\",\"stageId\":\"11348546\",\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":null,\"createdAt\":1614359253457,\"updatedAt\":null,\"active\":true},{\"label\":\"Closed won\",\"displayOrder\":5,\"metadata\":{\"isClosed\":\"true\",\"probability\":\"1.0\"},\"portalId\":123456,\"pipelineId\":\"11348541\",\"stageId\":\"11348547\",\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":null,\"createdAt\":1614359253457,\"updatedAt\":null,\"active\":true},{\"label\":\"Closed lost\",\"displayOrder\":6,\"metadata\":{\"isClosed\":\"true\",\"probability\":\"0.0\"},\"portalId\":123456,\"pipelineId\":\"11348541\",\"stageId\":\"11348548\",\"maxVisibleVersion\":null,\"createdBy\":9586504,\"updatedBy\":null,\"createdAt\":1614359253457,\"updatedAt\":null,\"active\":true}],\"objectType\":\"DEAL\",\"objectTypeId\":\"0-3\",\"pipelineId\":\"11348541\",\"portalId\":123456,\"version\":0,\"createdBy\":9586504,\"updatedBy\":null,\"createdAt\":1614359253457,\"updatedAt\":null,\"limitExempt\":false,\"permission\":null,\"default\":false}",
          "fromUserId": 9586504
        }
      ]
    }


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)