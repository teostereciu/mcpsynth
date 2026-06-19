from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import *
from generated_tools.blogposts import *
from generated_tools.comments import *
from generated_tools.content import *
from generated_tools.content_labels import *
from generated_tools.labels import *
from generated_tools.pages import *
from generated_tools.properties import *
from generated_tools.search import *
from generated_tools.spaces import *
from generated_tools.users import *
from generated_tools.versions import *


mcp = FastMCP("confluence-cloud")


def _safe(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            return {"error": str(e)}
    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper


for fn in [
    get_pages, create_page, get_page, update_page, delete_page, update_page_title, get_pages_for_label, get_pages_in_space,
    get_spaces, create_space, get_space,
    get_blog_posts, create_blog_post, get_blog_post, update_blog_post, delete_blog_post, get_blog_posts_for_label, get_blog_posts_in_space,
    search_content, search_users,
    get_attachments, get_attachment, delete_attachment, get_attachments_for_blog_post, get_attachments_for_custom_content, get_attachments_for_label, get_attachments_for_page, get_attachment_thumbnail_download,
    get_attachment_comments, get_custom_content_comments, get_page_footer_comments, get_page_inline_comments, get_blog_post_footer_comments, get_blog_post_inline_comments, get_footer_comments, create_footer_comment, get_footer_comment, update_footer_comment, delete_footer_comment, get_footer_comment_children, get_inline_comments, create_inline_comment, get_inline_comment, update_inline_comment, delete_inline_comment, get_inline_comment_children,
    get_labels, get_labels_for_attachment, get_labels_for_blog_post, get_labels_for_custom_content, get_labels_for_page, get_labels_for_space, get_labels_for_space_content,
    get_attachment_versions, get_attachment_version_details, get_blog_post_versions, get_blog_post_version_details, get_page_versions, get_page_version_details, get_custom_content_versions, get_custom_content_version_details, get_footer_comment_versions, get_footer_comment_version_details, get_inline_comment_versions, get_inline_comment_version_details,
    get_page_properties, create_page_property, get_page_property, update_page_property, delete_page_property, get_blog_post_properties, create_blog_post_property, get_blog_post_property, update_blog_post_property, delete_blog_post_property, get_attachment_properties, create_attachment_property, get_attachment_property, update_attachment_property, delete_attachment_property, get_comment_properties, create_comment_property, get_comment_property, update_comment_property, delete_comment_property,
    get_user, get_anonymous_user, get_current_user, get_group_memberships_for_user, get_multiple_users, get_user_email, get_user_emails_in_batch,
    archive_pages, publish_shared_draft, publish_legacy_draft, search_content_by_cql,
    add_labels_to_content, remove_label_from_content_by_query, remove_label_from_content,
]:
    mcp.tool()(_safe(fn))


if __name__ == "__main__":
    mcp.run()
