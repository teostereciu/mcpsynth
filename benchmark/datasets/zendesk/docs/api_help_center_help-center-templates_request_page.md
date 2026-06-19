# Request page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/request_page/*

---

## On this page

  * [Request page](/api-reference/help_center/help-center-templates/request_page/#request-page)
  * [Available properties](/api-reference/help_center/help-center-templates/request_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/request_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/request_page/#available-forms)
  * [Example](/api-reference/help_center/help-center-templates/request_page/#example)


# Request page

## On this page

  * [Request page](/api-reference/help_center/help-center-templates/request_page/#request-page)
  * [Available properties](/api-reference/help_center/help-center-templates/request_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/request_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/request_page/#available-forms)
  * [Example](/api-reference/help_center/help-center-templates/request_page/#example)


## Request page

The Request page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/requests/{request_id}`.

### Available properties

You can use the following properties in the Request page template.

Name| Type| Description
---|---|---
request| object| A [request](/api-reference/help_center/help-center-templates/objects#request-object) object
group| object| A [group](/api-reference/help_center/help-center-templates/objects#group) object
assignee| object| The agent assigned to the request [user](/api-reference/help_center/help-center-templates/objects#user-object)
custom_fields| array| An array of request custom [field](/api-reference/help_center/help-center-templates/objects#request-field-object) objects
comments| array| An array of request [comment](/api-reference/help_center/help-center-templates/objects#request-comment-object) objects
attachments| array| An array of [attachment](/api-reference/help_center/help-center-templates/objects#attachment-object) objects
collaborators| array| An array of [user](/api-reference/help_center/help-center-templates/objects#user-object) objects describing the request's collaborators (cc's), if any
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
satisfaction_response| object| A [satisfaction_response](/api-reference/help_center/help-center-templates/objects#satisfaction-response-object) object (available in Templating API v3 and above)
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user
path_steps| array| An array of [path_step](/api-reference/help_center/help-center-templates/objects#path_step-object) objects

### Available helpers

You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
breadcrumbs| Breadcrumbs for the current page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
satisfaction| A link that lets the user rate his or her satisfaction with how the request was handled. See [satisfaction helper](/api-reference/help_center/help-center-templates/advanced_helpers#satisfaction-helper)
comment_callout| A link for creating a follow-up ticket, if the current one has been closed. See [comment_callout helper](/api-reference/help_center/help-center-templates/advanced_helpers#comment_callout-helper)
form| A form for data input. See bellow the available forms for this page

Note that you can also use the [upload helper](/api-reference/help_center/help-center-templates/advanced_helpers#upload-helper) inside the comment form.

### Available forms

You can add the following forms to the Request page template:

Name| Description
---|---
[comment](/api-reference/help_center/help-center-templates/helpers#form-helper)| A form to send new request comment
[organization](/api-reference/help_center/help-center-templates/helpers#form-helper)| A form to change the request organization

Use the `form` helper to insert them. See [Form Helper](/api-reference/help_center/help-center-templates/helpers#form-helper).

#### Available identifiers

The following [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers) are available in this page:

Identifier| Form| Field(s)| Description
---|---|---|---
organization| organization| select| Identifies a drop-down to select an organization
body| comment| textarea, wysiwyg| Identifies a text field for a request comment (use [wysiwyg](/api-reference/help_center/help-center-templates/advanced_helpers#wysiwyg-helper) for rich content)
mark_as_solved| comment| label, checkbox| Identifies a checkbox to mark a request as solved
ccs| comment| token_field| Identifies an email (CC) field

### Example


    <nav class="sub-nav clearfix">  {{breadcrumbs}}  {{search}}</nav><section class="request-details">  <strong>{{request.subject}}</strong> (request #{{request.id}})  {{request.description}}  {{comment_callout}}</section>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)