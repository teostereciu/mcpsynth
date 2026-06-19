# Community Post page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_post_page/*

---

## On this page

  * [Community Post page](/api-reference/help_center/help-center-templates/community_post_page/#community-post-page)
  * [Available properties](/api-reference/help_center/help-center-templates/community_post_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/community_post_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/community_post_page/#available-forms)
  * [Sorters](/api-reference/help_center/help-center-templates/community_post_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/community_post_page/#example)


# Community Post page

## On this page

  * [Community Post page](/api-reference/help_center/help-center-templates/community_post_page/#community-post-page)
  * [Available properties](/api-reference/help_center/help-center-templates/community_post_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/community_post_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/community_post_page/#available-forms)
  * [Sorters](/api-reference/help_center/help-center-templates/community_post_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/community_post_page/#example)


## Community Post page

The Community Post page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/community/posts/{post_id}`.

### Available properties

Name| Type| Description
---|---|---
post| object| A [post](/api-reference/help_center/help-center-templates/objects#post-object) object
topic| object| A [topic](/api-reference/help_center/help-center-templates/objects#topic-object) object
comment_sorters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects. Useful for sorting the comments. See Sorters below
current_comment_sorter| object| The [filter](/api-reference/help_center/help-center-templates/objects#filter-object) object of the current comment sorter
comments| array| An array of [comment](/api-reference/help_center/help-center-templates/objects#post-comment-object) objects
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
breadcrumbs| Breadcrumbs for the Community Post page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)
share| Sharing elements. See [share helper](/api-reference/help_center/help-center-templates/helpers#share-helper)
subscribe| A link to follow or unfollow new comments in the post. See [subscribe](/api-reference/help_center/help-center-templates/helpers#subscribe-helper)
comment_callout| Partial rendering of the actions necessary to comment

### Available forms

You can add the following form to the Community Post page template:

Name| Description
---|---
comment| A form to send a new post comment

Use the `form` helper to insert it. See [Form Helper](/api-reference/help_center/help-center-templates/helpers#form-helper).

#### Available identifiers

The following [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers) are available in this page:

Identifier| Form| Field(s)| Description
---|---|---|---
body| comment| textarea, wysiwyg| Identifies a text field for post comments (use [wysiwyg](/api-reference/help_center/help-center-templates/advanced_helpers#wysiwyg-helper) for rich content)
official| comment| label, checkbox| Identifies a checkbox field to mark a comment as official

### Sorters

Iterating through the `comment_sorters` array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects adds the following links to the page:

Link text| Action
---|---
Date| Sorts by most recent comment creation time in descending order
Votes| Sorts by highest vote sum in descending order

Official comments are always given the highest priority and shown at the top.

### Example


    <nav class="sub-nav">  {{breadcrumbs}}  {{search scoped=true}}</nav>
    <header class="page-header">  <span class="post-actions">    {{post.actions}}    {{#with post.ticket}}      <a href="{{url}}" target="_zendesk_lotus" class="escalation-badge">        #{{id}}      </a>    {{/with}}  </span>  <span class="post-to-community">    {{link 'new_post' role='button'}}  </span></header>
    <div class="main-column">
      <article class="post {{#if post.featured}} post-featured {{/if}} {{#if post.pinned}} post-pinned {{/if}}">
        <div class="post-vote vote">      {{vote 'up' class='vote-up' selected_class='vote-voted'}}      <span class="vote-sum">{{post.vote_sum}}</span>      {{vote 'down' class='vote-down' selected_class='vote-voted'}}    </div>
        <div class="post-container">
          <div class="post-header">        <h1 title="{{post.title}}">{{post.title}}</h1>        <div class="post-info">          <div class="post-avatar {{#if post.author.agent}} post-avatar-agent {{/if}}">            <img src="{{post.author.avatar_url}}" alt="Avatar" />          </div>          <div class="post-meta">            <strong class="post-author" title="{{post.author.name}}">              {{#link 'user_profile' id=post.author.id}}                {{post.author.name}}              {{/link}}            </strong>            <div class="post-published meta">              {{date post.created_at}}            </div>          </div>          <div class="post-status">            {{#if post.status}}              <span class="post-{{post.status_dasherized}}">{{post.status_name}}</span>            {{/if}}          </div>          <div class="post-follow">{{subscribe}}</div>        </div>      </div>
          <div class="post-body markdown">{{post.details}}</div>
          <div class="post-share">{{share}}</div>
        </div>
      </article>
      <div class="comment-sorter">    {{#each comment_sorters}}      <a aria-selected="{{selected}}" href="{{url}}">{{name}}</a>    {{/each}}  </div>
      <h4 class="comment-heading">    {{t 'comments_count' count=post.comment_count}}  </h4>
      <ul id="comments" class="comment-list">    {{#each comments}}      <li id="{{anchor}}" class="comment">
            {{#if official}}          <div class="comment-bookmark"></div>        {{else}}          <div class="comment-vote vote">            {{vote 'up' class='vote-up' selected_class='vote-voted'}}            <span class="vote-sum">{{vote_sum}}</span>            {{vote 'down' class='vote-down' selected_class='vote-voted'}}          </div>        {{/if}}
            <div class="comment-avatar {{#if author.agent}} comment-avatar-agent {{/if}}">          <img src="{{author.avatar_url}}" alt="Avatar" />        </div>
            <div class="comment-container">
              <header class="comment-header">            <strong class="comment-author" title="{{author.name}}">              {{#link "user_profile" id=author.id}}                {{author.name}}              {{/link}}            </strong>            {{date created_at class='comment-published'}}            {{#if official}}              <span class="comment-official">{{t 'official_comment'}}</span>            {{/if}}            {{#if pending}}              <span class="comment-pending">{{t 'pending_approval'}}</span>            {{/if}}          </header>
              <div class="comment-body markdown">{{body}}</div>
              <footer class="comment-footer">            <span class="comment-actions">              {{#with ticket}}                <a href="{{url}}" target="_zendesk_lotus" class="escalation-badge">                  #{{id}}                </a>              {{/with}}              {{actions}}            </span>          </footer>
            </div>
          </li>    {{/each}}  </ul>
      {{pagination}}
      <div>{{comment_callout}}</div>
      {{#form 'comment' class='comment-form'}}    <div class="comment-vote"></div>    <div class="comment-avatar">      {{user_avatar class='user-avatar'}}    </div>    <div class="comment-container">      {{wysiwyg 'body'}}      <div class="comment-form-controls">        {{checkbox 'official'}}        {{label 'official'}}        {{input type='submit'}}      </div>    </div>  {{/form}}
    </div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)