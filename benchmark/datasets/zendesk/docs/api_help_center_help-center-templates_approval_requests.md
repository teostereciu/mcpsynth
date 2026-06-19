# Approval request page templates

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/approval_requests/*

---

## On this page

  * [Approval request page templates](/api-reference/help_center/help-center-templates/approval_requests/#approval-request-page-templates)
  * [Available properties](/api-reference/help_center/help-center-templates/approval_requests/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/approval_requests/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/approval_requests/#example)


# Approval request page templates

## On this page

  * [Approval request page templates](/api-reference/help_center/help-center-templates/approval_requests/#approval-request-page-templates)
  * [Available properties](/api-reference/help_center/help-center-templates/approval_requests/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/approval_requests/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/approval_requests/#example)


## Approval request page templates

Approval request page templates are accessible once approval requests are enabled in your account.

There are two approval requests page templates:

  * the approval request list page
  * the approval request page


Approval request pages are displayed only in help centers where approval requests are enabled.

The approval request list page appears when a user visits `https://{yoursubdomain}.zendesk.com/hc/{locale}/approval_requests/`.

The approval request page appears when a user visits `https://{yoursubdomain}.zendesk.com/hc/{locale}/approval_requests/{approval_request_id}`.

### Available properties

The following properties can be used in both the service list page template and the service page template.

Name| Type| Description
---|---|---
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user

### Available helpers

The following helpers are available for use in the approval request list and approval request page templates. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
breadcrumbs| Breadcrumbs for the current page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)

### Example


    <div class="container">  <div id="main-content">    <div id="approval-request-list"></div>  </div></div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)