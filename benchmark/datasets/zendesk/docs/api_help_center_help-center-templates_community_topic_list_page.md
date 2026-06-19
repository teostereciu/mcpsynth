# Community Topic List page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_topic_list_page/*

---

## On this page

  * [Community Topic List page](/api-reference/help_center/help-center-templates/community_topic_list_page/#community-topic-list-page)
  * [Available properties](/api-reference/help_center/help-center-templates/community_topic_list_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/community_topic_list_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/community_topic_list_page/#example)


# Community Topic List page

## On this page

  * [Community Topic List page](/api-reference/help_center/help-center-templates/community_topic_list_page/#community-topic-list-page)
  * [Available properties](/api-reference/help_center/help-center-templates/community_topic_list_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/community_topic_list_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/community_topic_list_page/#example)


## Community Topic List page

The Community Topic List page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/community/topics`.

### Available properties

Name| Type| Description
---|---|---
topics| array| An array of [topic](/api-reference/help_center/help-center-templates/objects#topic-object) objects
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
breadcrumbs| Breadcrumbs for the Topic list page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)

### Example


    <nav class="sub-nav">  {{breadcrumbs}}  {{search}}</nav>
    <header class="page-header">  <span class="dropdown">    <span class="dropdown-toggle">      <h1>{{t 'community'}}</h1>    </span>    <span class="dropdown-menu" role="menu">      {{link 'topics' role='menuitem' selected='true'}}      {{link 'posts' role='menuitem'}}    </span>  </span>  <span class="post-to-community">    {{link 'new_post' role='button'}}  </span></header>
    {{#unless topics}}  <p>{{t 'no_content'}}</p>{{/unless}}
    <ul class="topic-list">  {{#each topics}}    <li>      <h3>        {{#if internal}}          <span class="visibility-internal" data-title="{{t 'internal'}}">            <span class="visibility-internal-icon"></span>          </span>        {{/if}}        <a href="{{url}}">{{name}}</a>      </h3>      <p>{{excerpt description}}</p>      <span class="meta-group">        <span>{{t 'post_count' count=post_count}}</span>        <span>{{t 'follower_count' count=follower_count}}</span>      </span>    </li>  {{/each}}</ul>
    {{pagination}}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)