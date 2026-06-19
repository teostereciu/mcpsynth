#!/usr/bin/env python3
"""
Generate grounding.json from documentation files
"""
import os
import re
import json
import glob

def parse_doc_file(filepath):
    """Parse a documentation file to extract endpoints"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract the endpoint lines
    endpoints = []
    
    # Match patterns like [GET/wiki/rest/api/xxx](...)
    pattern = r'\[(GET|POST|PUT|DEL|PATCH)/wiki(/[^\]]+)\]'
    matches = re.findall(pattern, content)
    
    for method, path in matches:
        # Normalize method
        method_normalized = method
        if method_normalized == 'DEL':
            method_normalized = 'DELETE'
        
        # Clean up path
        path_clean = path
        
        endpoints.append({
            'method': method_normalized,
            'path': path_clean
        })
    
    return endpoints

def main():
    grounding = {}
    
    # Map of tool names to doc files
    # This will be populated manually based on the server.py implementation
    
    # First pass: collect all available endpoints from docs
    all_endpoints = {}
    doc_files = glob.glob('docs/*.md')
    
    for doc_file in doc_files:
        doc_name = os.path.basename(doc_file)
        endpoints = parse_doc_file(doc_file)
        for endpoint in endpoints:
            key = f"{endpoint['method']} {endpoint['path']}"
            if key not in all_endpoints:
                all_endpoints[key] = {
                    'doc': doc_file,
                    'endpoints': []
                }
            all_endpoints[key]['endpoints'].append(doc_file)
    
    # Build grounding for implemented tools
    # Pages (v2)
    grounding['list_pages'] = {
        'doc': 'docs/api_v2_page.md',
        'endpoint': 'GET /wiki/api/v2/pages'
    }
    grounding['get_page'] = {
        'doc': 'docs/api_v2_page.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}'
    }
    grounding['create_page'] = {
        'doc': 'docs/api_v2_page.md',
        'endpoint': 'POST /wiki/api/v2/pages'
    }
    grounding['update_page'] = {
        'doc': 'docs/api_v2_page.md',
        'endpoint': 'PUT /wiki/api/v2/pages/{id}'
    }
    grounding['delete_page'] = {
        'doc': 'docs/api_v2_page.md',
        'endpoint': 'DELETE /wiki/api/v2/pages/{id}'
    }
    grounding['update_page_title'] = {
        'doc': 'docs/api_v2_page.md',
        'endpoint': 'PUT /wiki/api/v2/pages/{id}/title'
    }
    
    # Spaces (v2)
    grounding['list_spaces'] = {
        'doc': 'docs/api_v2_space.md',
        'endpoint': 'GET /wiki/api/v2/spaces'
    }
    grounding['get_space'] = {
        'doc': 'docs/api_v2_space.md',
        'endpoint': 'GET /wiki/api/v2/spaces/{id}'
    }
    grounding['create_space'] = {
        'doc': 'docs/api_v2_space.md',
        'endpoint': 'POST /wiki/api/v2/spaces'
    }
    
    # Search (v1)
    grounding['search_confluence'] = {
        'doc': 'docs/api_v1_search.md',
        'endpoint': 'GET /wiki/rest/api/search'
    }
    
    # Labels (v2)
    grounding['list_labels_for_page'] = {
        'doc': 'docs/api_v2_label.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}/labels'
    }
    grounding['add_labels_to_page'] = {
        'doc': 'docs/api_v2_label.md',
        'endpoint': 'POST /wiki/api/v2/pages/{id}/labels'
    }
    grounding['remove_label_from_page'] = {
        'doc': 'docs/api_v2_label.md',
        'endpoint': 'DELETE /wiki/api/v2/pages/{id}/labels/{label}'
    }
    
    # Attachments (v2)
    grounding['list_attachments_for_page'] = {
        'doc': 'docs/api_v2_attachment.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}/attachments'
    }
    grounding['get_attachment'] = {
        'doc': 'docs/api_v2_attachment.md',
        'endpoint': 'GET /wiki/api/v2/attachments/{id}'
    }
    grounding['delete_attachment'] = {
        'doc': 'docs/api_v2_attachment.md',
        'endpoint': 'DELETE /wiki/api/v2/attachments/{id}'
    }
    
    # Comments (v2)
    grounding['list_footer_comments_for_page'] = {
        'doc': 'docs/api_v2_comment.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}/footer-comments'
    }
    grounding['create_footer_comment'] = {
        'doc': 'docs/api_v2_comment.md',
        'endpoint': 'POST /wiki/api/v2/footer-comments'
    }
    grounding['list_inline_comments_for_page'] = {
        'doc': 'docs/api_v2_inline-comment.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}/inline-comments'
    }
    
    # Versions (v2)
    grounding['list_page_versions'] = {
        'doc': 'docs/api_v2_version.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}/versions'
    }
    grounding['get_page_version'] = {
        'doc': 'docs/api_v2_version.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}/versions/{version-number}'
    }
    
    # Blog Posts (v2)
    grounding['list_blog_posts'] = {
        'doc': 'docs/api_v2_blog-post.md',
        'endpoint': 'GET /wiki/api/v2/blogposts'
    }
    grounding['get_blog_post'] = {
        'doc': 'docs/api_v2_blog-post.md',
        'endpoint': 'GET /wiki/api/v2/blogposts/{id}'
    }
    grounding['create_blog_post'] = {
        'doc': 'docs/api_v2_blog-post.md',
        'endpoint': 'POST /wiki/api/v2/blogposts'
    }
    grounding['update_blog_post'] = {
        'doc': 'docs/api_v2_blog-post.md',
        'endpoint': 'PUT /wiki/api/v2/blogposts/{id}'
    }
    grounding['delete_blog_post'] = {
        'doc': 'docs/api_v2_blog-post.md',
        'endpoint': 'DELETE /wiki/api/v2/blogposts/{id}'
    }
    
    # Users (v2)
    grounding['get_user_by_account_id'] = {
        'doc': 'docs/api_v2_user.md',
        'endpoint': 'GET /wiki/api/v2/users'
    }
    grounding['get_current_user'] = {
        'doc': 'docs/api_v2_user.md',
        'endpoint': 'GET /wiki/api/v2/users/current'
    }
    
    # Content Properties (v2)
    grounding['get_content_properties'] = {
        'doc': 'docs/api_v2_content-properties.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}/properties'
    }
    grounding['set_content_property'] = {
        'doc': 'docs/api_v2_content-properties.md',
        'endpoint': 'POST /wiki/api/v2/pages/{id}/properties'
    }
    
    # Ancestors (v2)
    grounding['get_page_ancestors'] = {
        'doc': 'docs/api_v2_ancestor.md',
        'endpoint': 'GET /wiki/api/v2/pages/{id}/ancestors'
    }
    
    # Space Operations (v1)
    grounding['list_all_spaces_v1'] = {
        'doc': 'docs/api_v1_space.md',
        'endpoint': 'GET /wiki/rest/api/space'
    }
    grounding['get_space_by_key_v1'] = {
        'doc': 'docs/api_v1_space.md',
        'endpoint': 'GET /wiki/rest/api/space/{spaceKey}'
    }
    
    # Content Operations (v1)
    grounding['get_content_by_id_v1'] = {
        'doc': 'docs/api_v1_content.md',
        'endpoint': 'GET /wiki/rest/api/content/{id}'
    }
    grounding['create_content_v1'] = {
        'doc': 'docs/api_v1_content.md',
        'endpoint': 'POST /wiki/rest/api/content'
    }
    grounding['update_content_v1'] = {
        'doc': 'docs/api_v1_content.md',
        'endpoint': 'PUT /wiki/rest/api/content/{id}'
    }
    grounding['delete_content_v1'] = {
        'doc': 'docs/api_v1_content.md',
        'endpoint': 'DELETE /wiki/rest/api/content/{id}'
    }
    
    # Labels (v1)
    grounding['add_label_v1'] = {
        'doc': 'docs/api_v1_content-labels.md',
        'endpoint': 'POST /wiki/rest/api/content/{id}/label'
    }
    grounding['remove_label_v1'] = {
        'doc': 'docs/api_v1_content-labels.md',
        'endpoint': 'DELETE /wiki/rest/api/content/{id}/label'
    }
    
    # Attachments (v1)
    grounding['upload_attachment_v1'] = {
        'doc': 'docs/api_v1_content-attachments.md',
        'endpoint': 'POST /wiki/rest/api/content/{id}/child/attachment'
    }
    grounding['list_attachments_v1'] = {
        'doc': 'docs/api_v1_content-attachments.md',
        'endpoint': 'GET /wiki/rest/api/content/{id}/child/attachment'
    }
    
    # Comments (v1)
    grounding['add_comment_v1'] = {
        'doc': 'docs/api_v1_content-comments.md',
        'endpoint': 'POST /wiki/rest/api/content/{id}/child/comment'
    }
    grounding['list_comments_v1'] = {
        'doc': 'docs/api_v1_content-comments.md',
        'endpoint': 'GET /wiki/rest/api/content/{id}/child/comment'
    }
    
    # Versions (v1)
    grounding['restore_version_v1'] = {
        'doc': 'docs/api_v1_content-versions.md',
        'endpoint': 'POST /wiki/rest/api/content/{id}/version'
    }
    
    # Write grounding.json
    with open('grounding.json', 'w') as f:
        json.dump(grounding, f, indent=2)
    
    print(f"Generated grounding.json with {len(grounding)} tools")

if __name__ == "__main__":
    main()
