# New Community Post page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/new_community_post_page/*

---

## On this page

  * [New Community Post page](/api-reference/help_center/help-center-templates/new_community_post_page/#new-community-post-page)
  * [Available properties](/api-reference/help_center/help-center-templates/new_community_post_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/new_community_post_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/new_community_post_page/#available-forms)
  * [Example](/api-reference/help_center/help-center-templates/new_community_post_page/#example)


# New Community Post page

## On this page

  * [New Community Post page](/api-reference/help_center/help-center-templates/new_community_post_page/#new-community-post-page)
  * [Available properties](/api-reference/help_center/help-center-templates/new_community_post_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/new_community_post_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/new_community_post_page/#available-forms)
  * [Example](/api-reference/help_center/help-center-templates/new_community_post_page/#example)


## New Community Post page

The New Community Post page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/community/posts/new`.

### Available properties

You can use the following properties in the Article page template.

Name| Type| Description
---|---|---
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user
path_steps| array| An array of [path_step](/api-reference/help_center/help-center-templates/objects#path_step-object) objects

### Available helpers

You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
breadcrumbs| Breadcrumbs for the New Community Post page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)

### Available forms

You can add the following form to the New Community Post page template:

Name| Description
---|---
post| A form to send a new post comment

Use the `form` helper to insert it. See [Form Helper](/api-reference/help_center/help-center-templates/helpers#form-helper).

#### Available identifiers

The following [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers) are available in this page:

Identifier| Form| Field(s)| Description
---|---|---|---
title| post| label, input| Identifies a text field for the post title
details| post| label, wysiwyg| Identifies a text field for the post body (use [wysiwyg](/api-reference/help_center/help-center-templates/advanced_helpers#wysiwyg-helper) for rich content)
topic| post| label, select| Identifies a drop-down to select a topic

### Example


    <nav class="sub-nav">  {{breadcrumbs}}  {{search}}</nav>
    <h1 class="page-header">  {{t 'what_is_your_post_about'}}</h1>
    <div class="form">  {{#form 'post' class='new_community_post'}}    <div class="form-field {{#required 'title'}} required {{/required}}">      {{label 'title'}}      {{input 'title'}}      {{#validate 'title'}}        <div class="notification notification-error notification-inline">          {{error 'title'}}        </div>      {{/validate}}    </div>
        {{suggestion_list class='searchbox'}}
        <div class="form-field {{#required 'details'}} required {{/required}}">      {{label 'details'}}      {{wysiwyg 'details'}}      {{#validate 'details'}}        <div class="notification notification-error notification-inline">          {{error 'details'}}        </div>      {{/validate}}    </div>
        <div class="form-field {{#required 'topic'}} required {{/required}}">      {{label 'topic'}}      {{select 'topic'}}      {{#validate 'topic'}}        <div class="notification notification-error notification-inline">          {{error 'topic'}}        </div>      {{/validate}}    </div>
        <footer>{{input type='submit'}}</footer>  {{/form}}</div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)