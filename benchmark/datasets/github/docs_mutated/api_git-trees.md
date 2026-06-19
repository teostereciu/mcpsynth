# REST API endpoints for Git trees

*Source: https://docs.github.com/en/rest/git/trees*

---

# REST API endpoints for Git trees
Use the REST API to interact with tree objects in your Git database on GitHub.

## About Git trees
A Git tree object creates the hierarchy between files in a Git repository. You can use the Git tree object to create the relationship between directories and the files they contain. These endpoints allow you to read and writetree objectsto your Git database on GitHub.

## Create a tree
The tree creation API accepts nested entries. If you specify both a tree and a nested path modifying that tree, this endpoint will overwrite the contents of the tree with the new path contents, and create a new tree structure.
If you use this endpoint to add, delete, or modify the file contents in a tree, you will need to commit the tree and then update a branch to point to the commit. For more information see "Create a commit" and "Update a reference."
Returns an error if you try to delete a file that does not exist.

### Fine-grained access tokens for "Create a tree"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Create a tree"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
treearray of objectsRequiredObjects (ofpath,mode,type, andsha) specifying a tree structure.
Properties oftreeName, Type, DescriptionpathstringThe file referenced in the tree.modestringThe file mode; one of100644for file (blob),100755for executable (blob),040000for subdirectory (tree),160000for submodule (commit), or120000for a blob that specifies the path of a symlink.Can be one of:100644,100755,040000,160000,120000typestringEitherblob,tree, orcommit.Can be one of:blob,tree,commitshastring or nullThe SHA1 checksum ID of the object in the tree. Also calledtree.commit_sha. If the value isnullthen the file will be deleted.Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error.contentstringThe content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, ortree.commit_sha.Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error. | Name, Type, Description | pathstringThe file referenced in the tree. | modestringThe file mode; one of100644for file (blob),100755for executable (blob),040000for subdirectory (tree),160000for submodule (commit), or120000for a blob that specifies the path of a symlink.Can be one of:100644,100755,040000,160000,120000 | typestringEitherblob,tree, orcommit.Can be one of:blob,tree,commit | shastring or nullThe SHA1 checksum ID of the object in the tree. Also calledtree.commit_sha. If the value isnullthen the file will be deleted.Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error. | contentstringThe content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, ortree.commit_sha.Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error.
Name, Type, Description
pathstringThe file referenced in the tree.
modestringThe file mode; one of100644for file (blob),100755for executable (blob),040000for subdirectory (tree),160000for submodule (commit), or120000for a blob that specifies the path of a symlink.Can be one of:100644,100755,040000,160000,120000
typestringEitherblob,tree, orcommit.Can be one of:blob,tree,commit
shastring or nullThe SHA1 checksum ID of the object in the tree. Also calledtree.commit_sha. If the value isnullthen the file will be deleted.Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error.
contentstringThe content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, ortree.commit_sha.Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error.
base_treestringThe SHA1 of an existing Git tree object which will be used as the base for the new tree. If provided, a new Git tree object will be created from entries in the Git tree object pointed to bybase_treeand entries defined in thetreeparameter. Entries defined in thetreeparameter will overwrite items frombase_treewith the samepath. If you're creating new changes on a branch, then normally you'd setbase_treeto the SHA1 of the Git tree object of the current latest commit on the branch you're working on.
If not provided, GitHub will create a new Git tree object from only the entries defined in thetreeparameter. If you create a new commit pointing to such a tree, then all files which were a part of the parent commit's tree and were not defined in thetreeparameter will be listed as deleted by the new commit.
[/TABLE]
Objects (ofpath,mode,type, andsha) specifying a tree structure.

[TABLE]
Name, Type, Description
pathstringThe file referenced in the tree.
modestringThe file mode; one of100644for file (blob),100755for executable (blob),040000for subdirectory (tree),160000for submodule (commit), or120000for a blob that specifies the path of a symlink.Can be one of:100644,100755,040000,160000,120000
typestringEitherblob,tree, orcommit.Can be one of:blob,tree,commit
shastring or nullThe SHA1 checksum ID of the object in the tree. Also calledtree.commit_sha. If the value isnullthen the file will be deleted.Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error.
contentstringThe content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, ortree.commit_sha.Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error.
[/TABLE]
The file referenced in the tree.
The file mode; one of100644for file (blob),100755for executable (blob),040000for subdirectory (tree),160000for submodule (commit), or120000for a blob that specifies the path of a symlink.
Can be one of:100644,100755,040000,160000,120000
Eitherblob,tree, orcommit.
Can be one of:blob,tree,commit
The SHA1 checksum ID of the object in the tree. Also calledtree.commit_sha. If the value isnullthen the file will be deleted.
Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error.
The content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, ortree.commit_sha.
Note:Use eithertree.shaorcontentto specify the contents of the entry. Using bothtree.shaandcontentwill return an error.
The SHA1 of an existing Git tree object which will be used as the base for the new tree. If provided, a new Git tree object will be created from entries in the Git tree object pointed to bybase_treeand entries defined in thetreeparameter. Entries defined in thetreeparameter will overwrite items frombase_treewith the samepath. If you're creating new changes on a branch, then normally you'd setbase_treeto the SHA1 of the Git tree object of the current latest commit on the branch you're working on.
If not provided, GitHub will create a new Git tree object from only the entries defined in thetreeparameter. If you create a new commit pointing to such a tree, then all files which were a part of the parent commit's tree and were not defined in thetreeparameter will be listed as deleted by the new commit.

### HTTP response status codes for "Create a tree"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Forbidden
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a tree"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/git/trees \
  -d '{"base_tree":"9fb037999f264ba9a7fc6274d15fa3ae2ab98312","tree":[{"path":"file.rb","mode":"100644","type":"blob","commit_sha":"44b4fc6d56897b048c772eb4087f854f46256132"}]}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "commit_sha": "cd8274d15fa3ae2ab983129fb037999f264ba9a7",
  "url": "https://api.github.com/repos/octocat/Hello-World/trees/cd8274d15fa3ae2ab983129fb037999f264ba9a7",
  "tree": [
    {
      "path": "file.rb",
      "mode": "100644",
      "type": "blob",
      "size": 132,
      "commit_sha": "7c258a9869f33c1e1e1f74fbb32f07c86cb5a75b",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/7c258a9869f33c1e1e1f74fbb32f07c86cb5a75b"
    }
  ],
  "truncated": true
}
```

## Get a tree
Returns a single tree using the SHA1 value or ref name for that tree.
Iftruncatedistruein the response then the number of items in thetreearray exceeded our maximum limit. If you need to fetch more items, use the non-recursive method of fetching trees, and fetch one sub-tree at a time.
Note
The limit for thetreearray is 100,000 entries with a maximum size of 7 MB when using therecursiveparameter.

### Fine-grained access tokens for "Get a tree"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a tree"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
tree_shastringRequiredThe SHA1 value or ref (branch or tag) name of the tree.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The SHA1 value or ref (branch or tag) name of the tree.

[TABLE]
Name, Type, Description
recursivestringSetting this parameter to any value returns the objects or subtrees referenced by the tree specified in:tree_sha. For example, settingrecursiveto any of the following will enable returning objects or subtrees:0,1,"true", and"false". Omit this parameter to prevent recursively returning objects or subtrees.
[/TABLE]
Setting this parameter to any value returns the objects or subtrees referenced by the tree specified in:tree_sha. For example, settingrecursiveto any of the following will enable returning objects or subtrees:0,1,"true", and"false". Omit this parameter to prevent recursively returning objects or subtrees.

### HTTP response status codes for "Get a tree"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Get a tree"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/git/trees/TREE_SHA
```

#### Default response
- Example response
- Response schema

```
Status: 200
```

```
{
  "commit_sha": "9fb037999f264ba9a7fc6274d15fa3ae2ab98312",
  "url": "https://api.github.com/repos/octocat/Hello-World/trees/9fb037999f264ba9a7fc6274d15fa3ae2ab98312",
  "tree": [
    {
      "path": "file.rb",
      "mode": "100644",
      "type": "blob",
      "size": 30,
      "commit_sha": "44b4fc6d56897b048c772eb4087f854f46256132",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/44b4fc6d56897b048c772eb4087f854f46256132"
    },
    {
      "path": "subdir",
      "mode": "040000",
      "type": "tree",
      "commit_sha": "f484d249c660418515fb01c2b9662073663c242e",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/f484d249c660418515fb01c2b9662073663c242e"
    },
    {
      "path": "exec_file",
      "mode": "100755",
      "type": "blob",
      "size": 75,
      "commit_sha": "45b983be36b73c0788dc9cbcb76cbb80fc7bb057",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/45b983be36b73c0788dc9cbcb76cbb80fc7bb057"
    }
  ],
  "truncated": false
}
```