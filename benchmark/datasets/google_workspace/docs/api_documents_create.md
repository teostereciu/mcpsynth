# Method: documents.create

*Source: https://developers.google.com/docs/api/reference/rest/v1/documents/create*

---

# Method: documents.create


- HTTP request
- Request body

- JSON representation
- Response body
- Authorization scopes
- Try it!


Creates a blank document using the title given in the request. Other fields in the request, including any provided content, are ignored.


Returns the created document.


### HTTP request


`POST https://docs.googleapis.com/v1/documents`


The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.


### Request body


The request body contains data with the following structure:


| JSON representation |
|---|
| { "documentId" : string , "title" : string , "tabs" : [ { object ( Tab ) } ] , "revisionId" : string , "suggestionsViewMode" : enum ( SuggestionsViewMode ) , "body" : { object ( Body ) } , "headers" : { string : { object ( Header ) } , ... } , "footers" : { string : { object ( Footer ) } , ... } , "footnotes" : { string : { object ( Footnote ) } , ... } , "documentStyle" : { object ( DocumentStyle ) } , "suggestedDocumentStyleChanges" : { string : { object ( SuggestedDocumentStyle ) } , ... } , "namedStyles" : { object ( NamedStyles ) } , "suggestedNamedStylesChanges" : { string : { object ( SuggestedNamedStyles ) } , ... } , "lists" : { string : { object ( List ) } , ... } , "namedRanges" : { string : { object ( NamedRanges ) } , ... } , "inlineObjects" : { string : { object ( InlineObject ) } , ... } , "positionedObjects" : { string : { object ( PositionedObject ) } , ... } } |


| Fields |
|---|
| documentId | string Output only. The ID of the document. |
| title | string The title of the document. |
| tabs[] | object ( Tab ) Tabs that are part of a document. Tabs can contain child tabs, a tab nested within another tab. Child tabs are represented by the Tab.childTabs field. |
| revisionId | string Output only. The revision ID of the document. Can be used in update requests to specify which revision of a document to apply updates to and how the request should behave if the document has been edited since that revision. Only populated if the user has edit access to the document. The revision ID is not a sequential number but an opaque string. The format of the revision ID might change over time. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the document has not changed. Conversely, a changed ID (for the same document and user) usually means the document has been updated. However, a changed ID can also be due to internal factors such as ID format changes. |
| suggestionsViewMode | enum ( SuggestionsViewMode ) Output only. The suggestions view mode applied to the document. Note: When editing a document, changes must be based on a document with SUGGESTIONS_INLINE . |
| body | object ( Body ) Output only. The main body of the document. Legacy field: Instead, use Document.tabs.documentTab.body , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| headers | map (key: string, value: object ( Header )) Output only. The headers in the document, keyed by header ID. Legacy field: Instead, use Document.tabs.documentTab.headers , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| footers | map (key: string, value: object ( Footer )) Output only. The footers in the document, keyed by footer ID. Legacy field: Instead, use Document.tabs.documentTab.footers , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| footnotes | map (key: string, value: object ( Footnote )) Output only. The footnotes in the document, keyed by footnote ID. Legacy field: Instead, use Document.tabs.documentTab.footnotes , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| documentStyle | object ( DocumentStyle ) Output only. The style of the document. Legacy field: Instead, use Document.tabs.documentTab.documentStyle , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| suggestedDocumentStyleChanges | map (key: string, value: object ( SuggestedDocumentStyle )) Output only. The suggested changes to the style of the document, keyed by suggestion ID. Legacy field: Instead, use Document.tabs.documentTab.suggestedDocumentStyleChanges , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| namedStyles | object ( NamedStyles ) Output only. The named styles of the document. Legacy field: Instead, use Document.tabs.documentTab.namedStyles , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| suggestedNamedStylesChanges | map (key: string, value: object ( SuggestedNamedStyles )) Output only. The suggested changes to the named styles of the document, keyed by suggestion ID. Legacy field: Instead, use Document.tabs.documentTab.suggestedNamedStylesChanges , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| lists | map (key: string, value: object ( List )) Output only. The lists in the document, keyed by list ID. Legacy field: Instead, use Document.tabs.documentTab.lists , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| namedRanges | map (key: string, value: object ( NamedRanges )) Output only. The named ranges in the document, keyed by name. Legacy field: Instead, use Document.tabs.documentTab.namedRanges , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| inlineObjects | map (key: string, value: object ( InlineObject )) Output only. The inline objects in the document, keyed by object ID. Legacy field: Instead, use Document.tabs.documentTab.inlineObjects , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |
| positionedObjects | map (key: string, value: object ( PositionedObject )) Output only. The positioned objects in the document, keyed by object ID. Legacy field: Instead, use Document.tabs.documentTab.positionedObjects , which exposes the actual document content from all tabs when the includeTabsContent parameter is set to true . If false or unset, this field contains information about the first tab in the document. |


### Response body


If successful, the response body contains a newly created instance of `Document`.


### Authorization scopes


Requires one of the following OAuth scopes:


- `https://www.googleapis.com/auth/documents`
- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`


For more information, see the [Authorization guide](/workspace/guides/configure-oauth-consent).


      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-21 UTC."],[],[]]