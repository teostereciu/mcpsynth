# Section page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/section_page/*

---

## On this page

  * [Section page](/api-reference/help_center/help-center-templates/section_page/#section-page)
  * [Available properties](/api-reference/help_center/help-center-templates/section_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/section_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/section_page/#example)


# Section page

## On this page

  * [Section page](/api-reference/help_center/help-center-templates/section_page/#section-page)
  * [Available properties](/api-reference/help_center/help-center-templates/section_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/section_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/section_page/#example)


## Section page

The Section page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/sections/{section_id}`.

### Available properties

You can use the following property in the Section page template.

Name| Type| Description
---|---|---
section| object| A [section](/api-reference/help_center/help-center-templates/objects#section-object) object
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
breadcrumbs| Breadcrumbs for the current page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)
subscribe| A link to follow or unfollow new articles or comments in the section

### Example


    <nav class="sub-nav">  {{breadcrumbs}}  {{subscribe}}</nav>
    <h1>{{section.name}}</h1><p class="section-description">{{section.description}}</p>
    {{#if section.articles}}  <ul class="article-list">    {{#each section.articles}}      <li class="article">        <a href="{{url}}">{{title}}</a>      </li>    {{/each}}  </ul>{{else}}  <i class="section-empty">    <a href="{{section.url}}">{{t 'empty'}}</a>  </i>{{/if}}
    {{pagination}}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)