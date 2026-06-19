# REST API endpoints for dependency submission

*Source: https://docs.github.com/en/rest/dependency-graph/dependency-submission*

---

# REST API endpoints for dependency submission
Use the REST API to submit dependencies.

## About dependency submissions
You can use the REST API to submit dependencies for a project. This enables you to add dependencies, such as those resolved when software is compiled or built, to GitHub's dependency graph feature, providing a more complete picture of all of your project's dependencies.
The dependency graph shows any dependencies you submit using the API in addition to any dependencies that are identified from manifest or lock files in the repository (for example, apackage-lock.jsonfile in a JavaScript project). For more information about viewing the dependency graph, seeExploring the dependencies of a repository.
Submitted dependencies will receive Dependabot alerts and Dependabot security updates for any known vulnerabilities. You will only get Dependabot alerts for dependencies that are from one of the supported ecosystems for the GitHub Advisory Database. For more information about these ecosystems, seeAbout the GitHub Advisory database. For transitive dependencies submitted via the dependency submission API, Dependabot will automatically open pull requests to update the parent dependency, if an update is available.
Submitted dependencies will be shown in dependency review, but arenotavailable in your organization's dependency insights.
Note
The dependency review API and the dependency submission API work together. This means that the dependency review API will include dependencies submitted via the dependency submission API.
You can submit dependencies in the form of a snapshot. A snapshot is a set of dependencies associated with a commit SHA and other metadata, that reflects the current state of your repository for a commit. You can choose to use pre-made actions or create your own actions to submit your dependencies in the required format each time your project is built. For more information, seeUsing the dependency submission API.
You can submit multiple sets of dependencies to be included in your dependency graph. The REST API uses thejob.correlatorproperty and thedetector.namecategory of the snapshot to ensure the latest submissions for each workflow get shown. Thecorrelatorproperty itself is the primary field you will use to keep independent submissions distinct. An examplecorrelatorcould be a simple combination of two variables available in actions runs:<GITHUB_WORKFLOW> <GITHUB_JOB>.
A repository can use multiple methods for dependency submission, which can cause the same package manifest to be scanned multiple times, potentially with different outputs from each scan. Dependency graph uses deduplication logic to parse the outputs, prioritizing the most accurate information for each manifest file.
Dependency graph displays only one instance of each manifest file using the following precedence rules.
1. User submissionstake the highest priority, because they are usually created during artifact builds they have the most complete information.If there are multiple manual snapshots from different detectors, they are sorted alphabetically by correlator and the first one used.If there are two correlators with the same detector, the resolved dependencies are merged. For more information about correlators and detectors, seeREST API endpoints for dependency submission.
2. Automatic submissionshave the second-highest priority since they are also created during artifact builds, but are not submitted by users.
3. Static analysis resultsare used when no other data is available.
- If there are multiple manual snapshots from different detectors, they are sorted alphabetically by correlator and the first one used.
- If there are two correlators with the same detector, the resolved dependencies are merged. For more information about correlators and detectors, seeREST API endpoints for dependency submission.

## Create a snapshot of dependencies for a repository
Create a new snapshot of a repository's dependencies.
The authenticated user must have access to the repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a snapshot of dependencies for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Create a snapshot of dependencies for a repository"

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
versionintegerRequiredThe version of the repository snapshot submission.
jobobjectRequired
Properties ofjobName, Type, DescriptionidstringRequiredThe external ID of the job.correlatorstringRequiredCorrelator provides a key that is used to group snapshots submitted over time. Only the "latest" submitted snapshot for a given combination ofjob.correlatoranddetector.namewill be considered when calculating a repository's current dependencies. Correlator should be as unique as it takes to distinguish all detection runs for a given "wave" of CI workflow you run. If you're using GitHub Actions, a good default value for this could be the environment variables GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If you're using a build matrix, then you'll also need to add additional key(s) to distinguish between each submission inside a matrix variation.html_urlstringThe url for the job. | Name, Type, Description | idstringRequiredThe external ID of the job. | correlatorstringRequiredCorrelator provides a key that is used to group snapshots submitted over time. Only the "latest" submitted snapshot for a given combination ofjob.correlatoranddetector.namewill be considered when calculating a repository's current dependencies. Correlator should be as unique as it takes to distinguish all detection runs for a given "wave" of CI workflow you run. If you're using GitHub Actions, a good default value for this could be the environment variables GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If you're using a build matrix, then you'll also need to add additional key(s) to distinguish between each submission inside a matrix variation. | html_urlstringThe url for the job.
Name, Type, Description
idstringRequiredThe external ID of the job.
correlatorstringRequiredCorrelator provides a key that is used to group snapshots submitted over time. Only the "latest" submitted snapshot for a given combination ofjob.correlatoranddetector.namewill be considered when calculating a repository's current dependencies. Correlator should be as unique as it takes to distinguish all detection runs for a given "wave" of CI workflow you run. If you're using GitHub Actions, a good default value for this could be the environment variables GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If you're using a build matrix, then you'll also need to add additional key(s) to distinguish between each submission inside a matrix variation.
html_urlstringThe url for the job.
shastringRequiredThe commit SHA associated with this dependency snapshot. Maximum length: 40 characters.
refstringRequiredThe repository branch that triggered this snapshot.
detectorobjectRequiredA description of the detector used.
Properties ofdetectorName, Type, DescriptionnamestringRequiredThe name of the detector used.versionstringRequiredThe version of the detector used.urlstringRequiredThe url of the detector used. | Name, Type, Description | namestringRequiredThe name of the detector used. | versionstringRequiredThe version of the detector used. | urlstringRequiredThe url of the detector used.
Name, Type, Description
namestringRequiredThe name of the detector used.
versionstringRequiredThe version of the detector used.
urlstringRequiredThe url of the detector used.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
manifestsobjectA collection of package manifests, which are a collection of related dependencies declared in a file or representing a logical group of dependencies.
Properties ofmanifestsName, Type, DescriptionkeyobjectA user-defined key to represent an item inmanifests.Properties ofkeyName, Type, DescriptionnamestringRequiredThe name of the manifest.fileobjectProperties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.resolvedobjectA collection of resolved package dependencies.Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | keyobjectA user-defined key to represent an item inmanifests. | Properties ofkeyName, Type, DescriptionnamestringRequiredThe name of the manifest.fileobjectProperties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.resolvedobjectA collection of resolved package dependencies.Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | namestringRequiredThe name of the manifest. | fileobject | Properties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository. | Name, Type, Description | source_locationstringThe path of the manifest file relative to the root of the Git repository. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | resolvedobjectA collection of resolved package dependencies. | Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | keyobjectA user-defined key to represent an item inresolved. | Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
keyobjectA user-defined key to represent an item inmanifests.
Properties ofkeyName, Type, DescriptionnamestringRequiredThe name of the manifest.fileobjectProperties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.resolvedobjectA collection of resolved package dependencies.Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | namestringRequiredThe name of the manifest. | fileobject | Properties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository. | Name, Type, Description | source_locationstringThe path of the manifest file relative to the root of the Git repository. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | resolvedobjectA collection of resolved package dependencies. | Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | keyobjectA user-defined key to represent an item inresolved. | Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
namestringRequiredThe name of the manifest.
fileobject
Properties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository. | Name, Type, Description | source_locationstringThe path of the manifest file relative to the root of the Git repository.
Name, Type, Description
source_locationstringThe path of the manifest file relative to the root of the Git repository.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
resolvedobjectA collection of resolved package dependencies.
Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | keyobjectA user-defined key to represent an item inresolved. | Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
keyobjectA user-defined key to represent an item inresolved.
Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect
scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development
dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
scannedstringRequiredThe time at which the snapshot was scanned.
[/TABLE]
The version of the repository snapshot submission.

[TABLE]
Name, Type, Description
idstringRequiredThe external ID of the job.
correlatorstringRequiredCorrelator provides a key that is used to group snapshots submitted over time. Only the "latest" submitted snapshot for a given combination ofjob.correlatoranddetector.namewill be considered when calculating a repository's current dependencies. Correlator should be as unique as it takes to distinguish all detection runs for a given "wave" of CI workflow you run. If you're using GitHub Actions, a good default value for this could be the environment variables GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If you're using a build matrix, then you'll also need to add additional key(s) to distinguish between each submission inside a matrix variation.
html_urlstringThe url for the job.
[/TABLE]
The external ID of the job.
Correlator provides a key that is used to group snapshots submitted over time. Only the "latest" submitted snapshot for a given combination ofjob.correlatoranddetector.namewill be considered when calculating a repository's current dependencies. Correlator should be as unique as it takes to distinguish all detection runs for a given "wave" of CI workflow you run. If you're using GitHub Actions, a good default value for this could be the environment variables GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If you're using a build matrix, then you'll also need to add additional key(s) to distinguish between each submission inside a matrix variation.
The url for the job.
The commit SHA associated with this dependency snapshot. Maximum length: 40 characters.
The repository branch that triggered this snapshot.
A description of the detector used.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the detector used.
versionstringRequiredThe version of the detector used.
urlstringRequiredThe url of the detector used.
[/TABLE]
The name of the detector used.
The version of the detector used.
The url of the detector used.
User-defined metadata to store domain-specific information limited to 8 keys with scalar values.
A collection of package manifests, which are a collection of related dependencies declared in a file or representing a logical group of dependencies.

[TABLE]
Name, Type, Description
keyobjectA user-defined key to represent an item inmanifests.
Properties ofkeyName, Type, DescriptionnamestringRequiredThe name of the manifest.fileobjectProperties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.resolvedobjectA collection of resolved package dependencies.Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | namestringRequiredThe name of the manifest. | fileobject | Properties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository. | Name, Type, Description | source_locationstringThe path of the manifest file relative to the root of the Git repository. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | resolvedobjectA collection of resolved package dependencies. | Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | keyobjectA user-defined key to represent an item inresolved. | Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
namestringRequiredThe name of the manifest.
fileobject
Properties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository. | Name, Type, Description | source_locationstringThe path of the manifest file relative to the root of the Git repository.
Name, Type, Description
source_locationstringThe path of the manifest file relative to the root of the Git repository.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
resolvedobjectA collection of resolved package dependencies.
Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | keyobjectA user-defined key to represent an item inresolved. | Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
keyobjectA user-defined key to represent an item inresolved.
Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect
scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development
dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
[/TABLE]
A user-defined key to represent an item inmanifests.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the manifest.
fileobject
Properties offileName, Type, Descriptionsource_locationstringThe path of the manifest file relative to the root of the Git repository. | Name, Type, Description | source_locationstringThe path of the manifest file relative to the root of the Git repository.
Name, Type, Description
source_locationstringThe path of the manifest file relative to the root of the Git repository.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
resolvedobjectA collection of resolved package dependencies.
Properties ofresolvedName, Type, DescriptionkeyobjectA user-defined key to represent an item inresolved.Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | keyobjectA user-defined key to represent an item inresolved. | Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
keyobjectA user-defined key to represent an item inresolved.
Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect
scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development
dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
[/TABLE]
The name of the manifest.

[TABLE]
Name, Type, Description
source_locationstringThe path of the manifest file relative to the root of the Git repository.
[/TABLE]

```
source_location
```
The path of the manifest file relative to the root of the Git repository.
User-defined metadata to store domain-specific information limited to 8 keys with scalar values.
A collection of resolved package dependencies.

[TABLE]
Name, Type, Description
keyobjectA user-defined key to represent an item inresolved.
Properties ofkeyName, Type, Descriptionpackage_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirectscopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,developmentdependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies. | Name, Type, Description | package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details. | metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values. | relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect | scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development | dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
Name, Type, Description
package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect
scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development
dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
[/TABLE]
A user-defined key to represent an item inresolved.

[TABLE]
Name, Type, Description
package_urlstringPackage-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.
metadataobjectUser-defined metadata to store domain-specific information limited to 8 keys with scalar values.
relationshipstringA notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.Can be one of:direct,indirect
scopestringA notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.Can be one of:runtime,development
dependenciesarray of stringsArray of package-url (PURLs) of direct child dependencies.
[/TABLE]

```
package_url
```
Package-url (PURL) of dependency. Seehttps://github.com/package-url/purl-specfor more details.
User-defined metadata to store domain-specific information limited to 8 keys with scalar values.

```
relationship
```
A notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.
Can be one of:direct,indirect
A notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.
Can be one of:runtime,development

```
development
```

```
dependencies
```
Array of package-url (PURLs) of direct child dependencies.
The time at which the snapshot was scanned.

### HTTP response status codes for "Create a snapshot of dependencies for a repository"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a snapshot of dependencies for a repository"

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
  https://api.github.com/repos/OWNER/REPO/dependency-graph/snapshots \
  -d '{"version":0,"sha":"ce587453ced02b1526dfb4cb910479d431683101","ref":"refs/heads/main","job":{"correlator":"yourworkflowname_youractionname","id":"yourrunid"},"detector":{"name":"octo-detector","version":"0.0.1","url":"https://github.com/octo-org/octo-repo"},"scanned":"2022-06-14T20:25:00Z","manifests":{"package-lock.json":{"name":"package-lock.json","file":{"source_location":"src/package-lock.json"},"resolved":{"@actions/core":{"package_url":"pkg:/npm/%40actions/core@1.1.9","dependencies":["@actions/http-client"]},"@actions/http-client":{"package_url":"pkg:/npm/%40actions/http-client@1.0.7","dependencies":["tunnel"]},"tunnel":{"package_url":"pkg:/npm/tunnel@0.0.6"}}}}}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 12345,
  "created_at": "2018-05-04T01:14:52Z",
  "message": "Dependency results for the repo have been successfully updated.",
  "result": "SUCCESS"
}
```