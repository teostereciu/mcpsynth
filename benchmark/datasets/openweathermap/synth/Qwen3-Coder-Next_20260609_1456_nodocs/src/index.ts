import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequest,
  CallToolRequest,
  CallToolResult,
  Tool,
  McpError,
} from "@modelcontextprotocol/sdk/types.js";
import axios, { AxiosInstance } from "axios";

// Jira base URL from environment
const JIRA_BASE_URL = process.env.JIRA_BASE_URL?.replace(/\/$/, "") || "https://your-org.atlassian.net";

// Jira authentication
const JIRA_EMAIL = process.env.JIRA_EMAIL;
const JIRA_API_TOKEN = process.env.JIRA_API_TOKEN;

if (!JIRA_EMAIL || !JIRA_API_TOKEN) {
  console.error("JIRA_EMAIL and JIRA_API_TOKEN environment variables must be set");
  process.exit(1);
}

// Create axios instance for Jira API
const jiraClient: AxiosInstance = axios.create({
  baseURL: `${JIRA_BASE_URL}/rest/api/3`,
  headers: {
    "Accept": "application/json",
    "Content-Type": "application/json",
  },
  auth: {
    username: JIRA_EMAIL,
    password: JIRA_API_TOKEN,
  },
});

// Error handling helper
function handleApiError(error: any): { error: string } {
  if (axios.isAxiosError(error)) {
    return {
      error: `HTTP ${error.response?.status || 500}: ${error.response?.data?.errorMessages?.[0] || error.message}`,
    };
  }
  return { error: error.message || "Unknown error" };
}

// ============== Issue Tools ==============

const GetIssueTool: Tool = {
  name: "get_issue",
  description: "Get an issue by ID or key.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "The issue ID or key (e.g., 'PROJ-123' or '12345')" },
    },
    required: ["issueIdOrKey"],
  },
};

const UpdateIssueTool: Tool = {
  name: "update_issue",
  description: "Update an issue.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "The issue ID or key" },
      update: { type: "object", description: "Issue update operations" },
      fields: { type: "object", description: "Issue fields to update" },
      updateHistory: { type: "boolean", description: "Whether to update the issue history" },
    },
    required: ["issueIdOrKey"],
  },
};

const DeleteIssueTool: Tool = {
  name: "delete_issue",
  description: "Delete an issue.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "The issue ID or key" },
      deleteSubtasks: { type: "boolean", description: "Whether to delete subtasks" },
    },
    required: ["issueIdOrKey"],
  },
};

const CreateIssueTool: Tool = {
  name: "create_issue",
  description: "Create a new issue.",
  inputSchema: {
    type: "object",
    properties: {
      fields: { type: "object", description: "Issue fields (summary, description, project, issuetype, etc.)" },
      update: { type: "object", description: "Issue update operations" },
      updateHistory: { type: "boolean", description: "Whether to update the issue history" },
      properties: { type: "array", description: "Issue properties to set" },
    },
    required: ["fields"],
  },
};

const SearchIssuesJqlTool: Tool = {
  name: "search_issues_jql",
  description: "Search issues using JQL query.",
  inputSchema: {
    type: "object",
    properties: {
      jql: { type: "string", description: "JQL query string" },
      start: { type: "integer", description: "Starting index for pagination" },
      maxResults: { type: "integer", description: "Maximum number of results" },
      validateQuery: { type: "string", description: "Validation behavior" },
      fields: { type: "array", description: "List of fields to return" },
      expand: { type: "array", description: "Fields to expand" },
      properties: { type: "array", description: "Issue properties to include" },
      language: { type: "string", description: "Query language" },
    },
    required: ["jql"],
  },
};

// ============== Project Tools ==============

const GetProjectTool: Tool = {
  name: "get_project",
  description: "Get project details.",
  inputSchema: {
    type: "object",
    properties: {
      projectIdOrKey: { type: "string", description: "Project ID or key" },
    },
    required: ["projectIdOrKey"],
  },
};

const ListProjectsTool: Tool = {
  name: "list_projects",
  description: "List projects.",
  inputSchema: {
    type: "object",
    properties: {
      start: { type: "integer", description: "Starting index for pagination" },
      maxResults: { type: "integer", description: "Maximum number of results" },
      expand: { type: "string", description: "Fields to expand" },
      status: { type: "array", description: "Filter by project status" },
    },
  },
};

const CreateProjectTool: Tool = {
  name: "create_project",
  description: "Create a new project.",
  inputSchema: {
    type: "object",
    properties: {
      key: { type: "string", description: "Project key (e.g., 'PROJ')" },
      name: { type: "string", description: "Project name" },
      description: { type: "string", description: "Project description" },
      leadAccountId: { type: "string", description: "Account ID of project lead" },
      leadId: { type: "string", description: "User ID of project lead (legacy)" },
      assigneeType: { type: "string", description: "Who can be assigned to issues" },
      projectTypeKey: { type: "string", description: "Type of project" },
      projectStyle: { type: "string", description: "Project style" },
      avatarId: { type: "string", description: "ID of project avatar" },
      notificationScheme: { type: "string", description: "Notification scheme ID" },
      permissionScheme: { type: "string", description: "Permission scheme ID" },
      issueSecurityScheme: { type: "string", description: "Security scheme ID" },
      categoryId: { type: "string", description: "Category ID" },
    },
    required: ["key", "name"],
  },
};

const UpdateProjectTool: Tool = {
  name: "update_project",
  description: "Update project details.",
  inputSchema: {
    type: "object",
    properties: {
      projectIdOrKey: { type: "string", description: "Project ID or key" },
      name: { type: "string", description: "New project name" },
      description: { type: "string", description: "New description" },
      leadAccountId: { type: "string", description: "New project lead account ID" },
      leadId: { type: "string", description: "New project lead ID" },
      assigneeType: { type: "string", description: "New assignee type" },
      projectTypeKey: { type: "string", description: "New project type" },
      projectStyle: { type: "string", description: "New project style" },
      avatarId: { type: "string", description: "New avatar ID" },
      notificationScheme: { type: "string", description: "New notification scheme ID" },
      permissionScheme: { type: "string", description: "New permission scheme ID" },
      issueSecurityScheme: { type: "string", description: "New security scheme ID" },
      categoryId: { type: "string", description: "New category ID" },
    },
    required: ["projectIdOrKey"],
  },
};

const DeleteProjectTool: Tool = {
  name: "delete_project",
  description: "Delete a project.",
  inputSchema: {
    type: "object",
    properties: {
      projectIdOrKey: { type: "string", description: "Project ID or key" },
    },
    required: ["projectIdOrKey"],
  },
};

// ============== Issue Operation Tools ==============

const AssignIssueTool: Tool = {
  name: "assign_issue",
  description: "Assign an issue to a user.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      accountId: { type: "string", description: "Account ID of user to assign to" },
      key: { type: "string", description: "Username (legacy)" },
    },
    required: ["issueIdOrKey"],
  },
};

const TransitionIssueTool: Tool = {
  name: "transition_issue",
  description: "Transition an issue.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      transitionId: { type: "string", description: "Transition ID" },
      update: { type: "object", description: "Issue update operations" },
      fields: { type: "object", description: "Issue fields to set during transition" },
      comment: { type: "string", description: "Optional comment to add during transition" },
    },
    required: ["issueIdOrKey", "transitionId"],
  },
};

// ============== Comment Tools ==============

const AddCommentTool: Tool = {
  name: "add_comment",
  description: "Add a comment to an issue.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      body: { type: "string", description: "Comment body text" },
      visibility: { type: "object", description: "Comment visibility" },
      properties: { type: "array", description: "Comment properties" },
    },
    required: ["issueIdOrKey", "body"],
  },
};

const UpdateCommentTool: Tool = {
  name: "update_comment",
  description: "Update a comment.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      commentId: { type: "string", description: "Comment ID" },
      body: { type: "string", description: "New comment body" },
      visibility: { type: "object", description: "New visibility" },
      properties: { type: "array", description: "New properties" },
    },
    required: ["issueIdOrKey", "commentId", "body"],
  },
};

const DeleteCommentTool: Tool = {
  name: "delete_comment",
  description: "Delete a comment.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      commentId: { type: "string", description: "Comment ID" },
    },
    required: ["issueIdOrKey", "commentId"],
  },
};

// ============== Worklog Tools ==============

const AddWorklogTool: Tool = {
  name: "add_worklog",
  description: "Add a worklog to an issue.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      comment: { type: "string", description: "Optional worklog comment" },
      adjustEstimate: { type: "string", description: "Estimate adjustment" },
      newEstimate: { type: "string", description: "New estimate value" },
      reduceBy: { type: "string", description: "Amount to reduce by" },
      started: { type: "string", description: "Worklog start time (ISO 8601)" },
      timeSpent: { type: "string", description: "Time spent (e.g., '1h 30m')" },
    },
    required: ["issueIdOrKey"],
  },
};

const UpdateWorklogTool: Tool = {
  name: "update_worklog",
  description: "Update a worklog.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      worklogId: { type: "string", description: "Worklog ID" },
      comment: { type: "string", description: "New comment" },
      adjustEstimate: { type: "string", description: "Estimate adjustment" },
      newEstimate: { type: "string", description: "New estimate" },
      reduceBy: { type: "string", description: "Amount to reduce by" },
      started: { type: "string", description: "New start time" },
      timeSpent: { type: "string", description: "New time spent" },
    },
    required: ["issueIdOrKey", "worklogId"],
  },
};

const DeleteWorklogTool: Tool = {
  name: "delete_worklog",
  description: "Delete a worklog.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      worklogId: { type: "string", description: "Worklog ID" },
    },
    required: ["issueIdOrKey", "worklogId"],
  },
};

// ============== Attachment Tools ==============

const AddAttachmentTool: Tool = {
  name: "add_attachment",
  description: "Add an attachment to an issue.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      filename: { type: "string", description: "Name of the file" },
      fileContent: { type: "string", description: "Base64-encoded file content" },
    },
    required: ["issueIdOrKey", "filename", "fileContent"],
  },
};

// ============== Watcher Tools ==============

const AddWatcherTool: Tool = {
  name: "add_watcher",
  description: "Add a watcher to an issue.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      accountId: { type: "string", description: "Account ID of watcher" },
    },
    required: ["issueIdOrKey", "accountId"],
  },
};

const RemoveWatcherTool: Tool = {
  name: "remove_watcher",
  description: "Remove a watcher from an issue.",
  inputSchema: {
    type: "object",
    properties: {
      issueIdOrKey: { type: "string", description: "Issue ID or key" },
      accountId: { type: "string", description: "Account ID of watcher to remove" },
    },
    required: ["issueIdOrKey", "accountId"],
  },
};

// ============== User Tools ==============

const GetUsersByProjectTool: Tool = {
  name: "get_users_by_project",
  description: "Get users in a project.",
  inputSchema: {
    type: "object",
    properties: {
      projectIdOrKey: { type: "string", description: "Project ID or key" },
      start: { type: "integer", description: "Starting index" },
      maxResults: { type: "integer", description: "Maximum results" },
    },
    required: ["projectIdOrKey"],
  },
};

const GetIssueTypesTool: Tool = {
  name: "get_issue_types",
  description: "Get all issue types.",
  inputSchema: {
    type: "object",
    properties: {
      start: { type: "integer", description: "Starting index" },
      maxResults: { type: "integer", description: "Maximum results" },
      expand: { type: "string", description: "Fields to expand" },
    },
  },
};

const GetPrioritiesTool: Tool = {
  name: "get_priorities",
  description: "Get all priorities.",
  inputSchema: {
    type: "object",
    properties: {
      start: { type: "integer", description: "Starting index" },
      maxResults: { type: "integer", description: "Maximum results" },
      expand: { type: "string", description: "Fields to expand" },
    },
  },
};

const GetStatusesTool: Tool = {
  name: "get_statuses",
  description: "Get all statuses.",
  inputSchema: {
    type: "object",
    properties: {
      start: { type: "integer", description: "Starting index" },
      maxResults: { type: "integer", description: "Maximum results" },
      expand: { type: "string", description: "Fields to expand" },
    },
  },
};

// ============== Individual Entity Tools ==============

const GetIssueTypeTool: Tool = {
  name: "get_issue_type",
  description: "Get an issue type by ID.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Issue type ID" },
    },
    required: ["id"],
  },
};

const GetPriorityTool: Tool = {
  name: "get_priority",
  description: "Get a priority by ID.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Priority ID" },
    },
    required: ["id"],
  },
};

const GetStatusTool: Tool = {
  name: "get_status",
  description: "Get a status by ID.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Status ID" },
    },
    required: ["id"],
  },
};

const GetVersionTool: Tool = {
  name: "get_version",
  description: "Get a version by ID.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Version ID" },
    },
    required: ["id"],
  },
};

// ============== Version Tools ==============

const CreateVersionTool: Tool = {
  name: "create_version",
  description: "Create a version.",
  inputSchema: {
    type: "object",
    properties: {
      name: { type: "string", description: "Version name" },
      projectId: { type: "string", description: "Project ID or key" },
      description: { type: "string", description: "Version description" },
      releaseDate: { type: "string", description: "Release date (YYYY-MM-DD)" },
      overdue: { type: "boolean", description: "Whether version is overdue" },
      userStartDate: { type: "string", description: "User start date" },
      userReleaseDate: { type: "string", description: "User release date" },
      startDate: { type: "string", description: "Start date" },
      archived: { type: "boolean", description: "Whether version is archived" },
      released: { type: "boolean", description: "Whether version is released" },
      moveUnfixedIssuesTo: { type: "string", description: "Move unfixed issues to this version" },
    },
    required: ["name", "projectId"],
  },
};

const UpdateVersionTool: Tool = {
  name: "update_version",
  description: "Update a version.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Version ID" },
      name: { type: "string", description: "New name" },
      description: { type: "string", description: "New description" },
      releaseDate: { type: "string", description: "New release date" },
      overdue: { type: "boolean", description: "New overdue status" },
      userStartDate: { type: "string", description: "New user start date" },
      userReleaseDate: { type: "string", description: "New user release date" },
      startDate: { type: "string", description: "New start date" },
      archived: { type: "boolean", description: "New archived status" },
      released: { type: "boolean", description: "New released status" },
      moveUnfixedIssuesTo: { type: "string", description: "New move unfixed issues to version" },
    },
    required: ["id"],
  },
};

const DeleteVersionTool: Tool = {
  name: "delete_version",
  description: "Delete a version.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Version ID" },
      moveUnfixedIssuesTo: { type: "string", description: "Move unfixed issues to this version before deleting" },
    },
    required: ["id"],
  },
};

// ============== Component Tools ==============

const GetComponentsTool: Tool = {
  name: "get_components",
  description: "Get components for a project.",
  inputSchema: {
    type: "object",
    properties: {
      projectIdOrKey: { type: "string", description: "Project ID or key" },
      start: { type: "integer", description: "Starting index" },
      maxResults: { type: "integer", description: "Maximum results" },
    },
    required: ["projectIdOrKey"],
  },
};

const CreateComponentTool: Tool = {
  name: "create_component",
  description: "Create a component.",
  inputSchema: {
    type: "object",
    properties: {
      name: { type: "string", description: "Component name" },
      projectId: { type: "string", description: "Project ID or key" },
      description: { type: "string", description: "Component description" },
      leadAccountId: { type: "string", description: "Component lead account ID" },
      leadId: { type: "string", description: "Component lead ID" },
      assigneeType: { type: "string", description: "Assignee type" },
      archiverAccountId: { type: "string", description: "Archiver account ID" },
    },
    required: ["name", "projectId"],
  },
};

const UpdateComponentTool: Tool = {
  name: "update_component",
  description: "Update a component.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Component ID" },
      name: { type: "string", description: "New name" },
      description: { type: "string", description: "New description" },
      leadAccountId: { type: "string", description: "New lead account ID" },
      leadId: { type: "string", description: "New lead ID" },
      assigneeType: { type: "string", description: "New assignee type" },
      archiverAccountId: { type: "string", description: "New archiver account ID" },
    },
    required: ["id"],
  },
};

const DeleteComponentTool: Tool = {
  name: "delete_component",
  description: "Delete a component.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Component ID" },
    },
    required: ["id"],
  },
};

// ============== Filter Tools ==============

const CreateFilterTool: Tool = {
  name: "create_filter",
  description: "Create a filter.",
  inputSchema: {
    type: "object",
    properties: {
      name: { type: "string", description: "Filter name" },
      description: { type: "string", description: "Filter description" },
      jql: { type: "string", description: "JQL query" },
      sharedWith: { type: "string", description: "Who to share with" },
      favourite: { type: "boolean", description: "Whether to mark as favourite" },
    },
    required: ["name", "jql"],
  },
};

const GetFilterTool: Tool = {
  name: "get_filter",
  description: "Get a filter by ID.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Filter ID" },
    },
    required: ["id"],
  },
};

const UpdateFilterTool: Tool = {
  name: "update_filter",
  description: "Update a filter.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Filter ID" },
      name: { type: "string", description: "New name" },
      description: { type: "string", description: "New description" },
      jql: { type: "string", description: "New JQL query" },
      favourite: { type: "boolean", description: "New favourite status" },
      sharedWith: { type: "string", description: "New share type" },
    },
    required: ["id"],
  },
};

const DeleteFilterTool: Tool = {
  name: "delete_filter",
  description: "Delete a filter.",
  inputSchema: {
    type: "object",
    properties: {
      id: { type: "string", description: "Filter ID" },
    },
    required: ["id"],
  },
};

// ============== Group Tools ==============

const GetGroupsTool: Tool = {
  name: "get_groups",
  description: "Get groups.",
  inputSchema: {
    type: "object",
    properties: {
      start: { type: "integer", description: "Starting index" },
      maxResults: { type: "integer", description: "Maximum results" },
      exclude: { type: "array", description: "Groups to exclude" },
    },
  },
};

const CreateGroupTool: Tool = {
  name: "create_group",
  description: "Create a group.",
  inputSchema: {
    type: "object",
    properties: {
      name: { type: "string", description: "Group name" },
    },
    required: ["name"],
  },
};

const AddUserToGroupTool: Tool = {
  name: "add_user_to_group",
  description: "Add a user to a group.",
  inputSchema: {
    type: "object",
    properties: {
      groupName: { type: "string", description: "Group name" },
      accountId: { type: "string", description: "User account ID" },
      username: { type: "string", description: "Username (legacy)" },
    },
    required: ["groupName"],
  },
};

const RemoveUserFromGroupTool: Tool = {
  name: "remove_user_from_group",
  description: "Remove a user from a group.",
  inputSchema: {
    type: "object",
    properties: {
      groupName: { type: "string", description: "Group name" },
      accountId: { type: "string", description: "User account ID" },
      username: { type: "string", description: "Username (legacy)" },
    },
    required: ["groupName"],
  },
};

// ============== User Management Tools ==============

const GetUserTool: Tool = {
  name: "get_user",
  description: "Get user details.",
  inputSchema: {
    type: "object",
    properties: {
      accountId: { type: "string", description: "User account ID" },
      username: { type: "string", description: "Username (legacy)" },
      key: { type: "string", description: "User key (legacy)" },
      expand: { type: "string", description: "Fields to expand" },
    },
  },
};

const SearchUsersTool: Tool = {
  name: "search_users",
  description: "Search users.",
  inputSchema: {
    type: "object",
    properties: {
      query: { type: "string", description: "Search query" },
      start: { type: "integer", description: "Starting index" },
      maxResults: { type: "integer", description: "Maximum results" },
      active: { type: "boolean", description: "Filter by active status" },
      exclude: { type: "array", description: "Users to exclude" },
    },
    required: ["query"],
  },
};

// ============== Issue Link Tools ==============

const CreateIssueLinkTool: Tool = {
  name: "create_issue_link",
  description: "Create an issue link.",
  inputSchema: {
    type: "object",
    properties: {
      typeId: { type: "string", description: "Issue link type ID" },
      inwardIssueId: { type: "string", description: "Inward issue ID" },
      outwardIssueId: { type: "string", description: "Outward issue ID" },
      comment: { type: "string", description: "Optional comment" },
    },
    required: ["typeId", "inwardIssueId", "outwardIssueId"],
  },
};

const GetIssueLinksTool: Tool = {
  name: "get_issue_links",
  description: "Get an issue link by ID.",
  inputSchema: {
    type: "object",
    properties: {
      issueLinkId: { type: "string", description: "Issue link ID" },
    },
    required: ["issueLinkId"],
  },
};

const DeleteIssueLinkTool: Tool = {
  name: "delete_issue_link",
  description: "Delete an issue link.",
  inputSchema: {
    type: "object",
    properties: {
      issueLinkId: { type: "string", description: "Issue link ID" },
    },
    required: ["issueLinkId"],
  },
};

// List of all tools
const TOOLS: Tool[] = [
  GetIssueTool,
  UpdateIssueTool,
  DeleteIssueTool,
  CreateIssueTool,
  SearchIssuesJqlTool,
  GetProjectTool,
  ListProjectsTool,
  CreateProjectTool,
  UpdateProjectTool,
  DeleteProjectTool,
  AssignIssueTool,
  TransitionIssueTool,
  AddCommentTool,
  UpdateCommentTool,
  DeleteCommentTool,
  AddWorklogTool,
  UpdateWorklogTool,
  DeleteWorklogTool,
  AddAttachmentTool,
  AddWatcherTool,
  RemoveWatcherTool,
  GetUsersByProjectTool,
  GetIssueTypesTool,
  GetPrioritiesTool,
  GetStatusesTool,
  GetIssueTypeTool,
  GetPriorityTool,
  GetStatusTool,
  GetVersionTool,
  CreateVersionTool,
  UpdateVersionTool,
  DeleteVersionTool,
  GetComponentsTool,
  CreateComponentTool,
  UpdateComponentTool,
  DeleteComponentTool,
  CreateFilterTool,
  GetFilterTool,
  UpdateFilterTool,
  DeleteFilterTool,
  GetGroupsTool,
  CreateGroupTool,
  AddUserToGroupTool,
  RemoveUserFromGroupTool,
  GetUserTool,
  SearchUsersTool,
  CreateIssueLinkTool,
  GetIssueLinksTool,
  DeleteIssueLinkTool,
];

// Initialize server
const server = new Server(
  {
    name: "jira-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Handle list tools request
server.setRequestHandler(ListToolsRequest.schema, async () => {
  return {
    tools: TOOLS,
  };
});

// Handle call tool request
server.setRequestHandler(CallToolRequest.schema, async (request) => {
  try {
    const { name, arguments: args } = request.params;
    
    switch (name) {
      case "get_issue": {
        const { issueIdOrKey } = args as { issueIdOrKey: string };
        const response = await jiraClient.get(`/issue/${issueIdOrKey}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "update_issue": {
        const { issueIdOrKey, update, fields, updateHistory } = args as {
          issueIdOrKey: string;
          update?: Record<string, any>;
          fields?: Record<string, any>;
          updateHistory?: boolean;
        };
        const data = {
          update: update || {},
          fields: fields || {},
          updateHistory: updateHistory ?? true,
        };
        const response = await jiraClient.put(`/issue/${issueIdOrKey}`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "delete_issue": {
        const { issueIdOrKey, deleteSubtasks } = args as {
          issueIdOrKey: string;
          deleteSubtasks?: boolean;
        };
        const response = await jiraClient.delete(`/issue/${issueIdOrKey}`, {
          params: { deleteSubtasks: deleteSubtasks ?? true },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "create_issue": {
        const { fields, update, updateHistory, properties } = args as {
          fields: Record<string, any>;
          update?: Record<string, any>;
          updateHistory?: boolean;
          properties?: Array<Record<string, any>>;
        };
        const data = {
          fields,
          update: update || {},
          updateHistory: updateHistory ?? true,
          properties: properties || [],
        };
        const response = await jiraClient.post("/issue", data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "search_issues_jql": {
        const { jql, start = 0, maxResults = 50, validateQuery = "warn", fields = ["*all"], expand = [], properties = [], language = "jql" } = args as {
          jql: string;
          start?: number;
          maxResults?: number;
          validateQuery?: string;
          fields?: string[];
          expand?: string[];
          properties?: string[];
          language?: string;
        };
        const data = {
          jql,
          start,
          maxResults,
          validateQuery,
          fields,
          expand,
          properties,
          language,
        };
        const response = await jiraClient.post("/search", data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_project": {
        const { projectIdOrKey } = args as { projectIdOrKey: string };
        const response = await jiraClient.get(`/project/${projectIdOrKey}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "list_projects": {
        const { start = 0, maxResults = 50, expand = "description,lead,projectKeys", status } = args as {
          start?: number;
          maxResults?: number;
          expand?: string;
          status?: string[];
        };
        const params: Record<string, any> = { start, maxResults, expand };
        if (status) params.status = status;
        const response = await jiraClient.get("/project", { params });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "create_project": {
        const { key, name, description = "", leadAccountId, leadId, assigneeType = "PROJECT_LEAD", projectTypeKey = "business", projectStyle = "classic", avatarId, notificationScheme, permissionScheme, issueSecurityScheme, categoryId } = args as {
          key: string;
          name: string;
          description?: string;
          leadAccountId?: string;
          leadId?: string;
          assigneeType?: string;
          projectTypeKey?: string;
          projectStyle?: string;
          avatarId?: string;
          notificationScheme?: string;
          permissionScheme?: string;
          issueSecurityScheme?: string;
          categoryId?: string;
        };
        const data: Record<string, any> = { key, name, description, assigneeType, projectTypeKey, projectStyle };
        if (leadAccountId) data.leadAccountId = leadAccountId;
        if (leadId) data.leadId = leadId;
        if (avatarId) data.avatarId = avatarId;
        if (notificationScheme) data.notificationScheme = notificationScheme;
        if (permissionScheme) data.permissionScheme = permissionScheme;
        if (issueSecurityScheme) data.issueSecurityScheme = issueSecurityScheme;
        if (categoryId) data.categoryId = categoryId;
        const response = await jiraClient.post("/project", data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "update_project": {
        const { projectIdOrKey, name, description, leadAccountId, leadId, assigneeType, projectTypeKey, projectStyle, avatarId, notificationScheme, permissionScheme, issueSecurityScheme, categoryId } = args as {
          projectIdOrKey: string;
          name?: string;
          description?: string;
          leadAccountId?: string;
          leadId?: string;
          assigneeType?: string;
          projectTypeKey?: string;
          projectStyle?: string;
          avatarId?: string;
          notificationScheme?: string;
          permissionScheme?: string;
          issueSecurityScheme?: string;
          categoryId?: string;
        };
        const data: Record<string, any> = {};
        if (name !== undefined) data.name = name;
        if (description !== undefined) data.description = description;
        if (leadAccountId !== undefined) data.leadAccountId = leadAccountId;
        if (leadId !== undefined) data.leadId = leadId;
        if (assigneeType !== undefined) data.assigneeType = assigneeType;
        if (projectTypeKey !== undefined) data.projectTypeKey = projectTypeKey;
        if (projectStyle !== undefined) data.projectStyle = projectStyle;
        if (avatarId !== undefined) data.avatarId = avatarId;
        if (notificationScheme !== undefined) data.notificationScheme = notificationScheme;
        if (permissionScheme !== undefined) data.permissionScheme = permissionScheme;
        if (issueSecurityScheme !== undefined) data.issueSecurityScheme = issueSecurityScheme;
        if (categoryId !== undefined) data.categoryId = categoryId;
        const response = await jiraClient.put(`/project/${projectIdOrKey}`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "delete_project": {
        const { projectIdOrKey } = args as { projectIdOrKey: string };
        const response = await jiraClient.delete(`/project/${projectIdOrKey}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "assign_issue": {
        const { issueIdOrKey, accountId, key } = args as {
          issueIdOrKey: string;
          accountId?: string;
          key?: string;
        };
        const data: Record<string, any> = {};
        if (accountId) data.accountId = accountId;
        if (key) data.key = key;
        if (Object.keys(data).length === 0) {
          throw new McpError(400, "Either accountId or key must be provided");
        }
        const response = await jiraClient.post(`/issue/${issueIdOrKey}/assignee`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "transition_issue": {
        const { issueIdOrKey, transitionId, update, fields, comment } = args as {
          issueIdOrKey: string;
          transitionId: string;
          update?: Record<string, any>;
          fields?: Record<string, any>;
          comment?: string;
        };
        const data: Record<string, any> = { transition: { id: transitionId } };
        if (update) data.update = update;
        if (fields) data.fields = fields;
        if (comment) data.comment = { body: comment };
        const response = await jiraClient.post(`/issue/${issueIdOrKey}/transitions`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "add_comment": {
        const { issueIdOrKey, body, visibility, properties } = args as {
          issueIdOrKey: string;
          body: string;
          visibility?: Record<string, any>;
          properties?: Array<Record<string, any>>;
        };
        const data: Record<string, any> = { body };
        if (visibility) data.visibility = visibility;
        if (properties) data.properties = properties;
        const response = await jiraClient.post(`/issue/${issueIdOrKey}/comment`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "update_comment": {
        const { issueIdOrKey, commentId, body, visibility, properties } = args as {
          issueIdOrKey: string;
          commentId: string;
          body: string;
          visibility?: Record<string, any>;
          properties?: Array<Record<string, any>>;
        };
        const data: Record<string, any> = { body };
        if (visibility) data.visibility = visibility;
        if (properties) data.properties = properties;
        const response = await jiraClient.put(`/issue/${issueIdOrKey}/comment/${commentId}`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "delete_comment": {
        const { issueIdOrKey, commentId } = args as {
          issueIdOrKey: string;
          commentId: string;
        };
        const response = await jiraClient.delete(`/issue/${issueIdOrKey}/comment/${commentId}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "add_worklog": {
        const { issueIdOrKey, comment, adjustEstimate, newEstimate, reduceBy, started, timeSpent } = args as {
          issueIdOrKey: string;
          comment?: string;
          adjustEstimate?: string;
          newEstimate?: string;
          reduceBy?: string;
          started?: string;
          timeSpent?: string;
        };
        const data: Record<string, any> = {};
        if (comment) data.comment = comment;
        if (adjustEstimate) data.adjustEstimate = adjustEstimate;
        if (newEstimate) data.newEstimate = newEstimate;
        if (reduceBy) data.reduceBy = reduceBy;
        if (started) data.started = started;
        if (timeSpent) data.timeSpent = timeSpent;
        const response = await jiraClient.post(`/issue/${issueIdOrKey}/worklog`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "update_worklog": {
        const { issueIdOrKey, worklogId, comment, adjustEstimate, newEstimate, reduceBy, started, timeSpent } = args as {
          issueIdOrKey: string;
          worklogId: string;
          comment?: string;
          adjustEstimate?: string;
          newEstimate?: string;
          reduceBy?: string;
          started?: string;
          timeSpent?: string;
        };
        const data: Record<string, any> = {};
        if (comment) data.comment = comment;
        if (adjustEstimate) data.adjustEstimate = adjustEstimate;
        if (newEstimate) data.newEstimate = newEstimate;
        if (reduceBy) data.reduceBy = reduceBy;
        if (started) data.started = started;
        if (timeSpent) data.timeSpent = timeSpent;
        const response = await jiraClient.put(`/issue/${issueIdOrKey}/worklog/${worklogId}`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "delete_worklog": {
        const { issueIdOrKey, worklogId } = args as {
          issueIdOrKey: string;
          worklogId: string;
        };
        const response = await jiraClient.delete(`/issue/${issueIdOrKey}/worklog/${worklogId}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "add_attachment": {
        const { issueIdOrKey, filename, fileContent } = args as {
          issueIdOrKey: string;
          filename: string;
          fileContent: string;
        };
        // Decode base64 content
        const buffer = Buffer.from(fileContent, "base64");
        const formData = new FormData();
        // @ts-ignore - FormData append method
        formData.append("file", new Blob([buffer], { type: "application/octet-stream" }), filename);
        
        const response = await jiraClient.post(`/issue/${issueIdOrKey}/attachments`, formData, {
          headers: {
            "Accept": "application/json",
          },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "add_watcher": {
        const { issueIdOrKey, accountId } = args as {
          issueIdOrKey: string;
          accountId: string;
        };
        const data = { accountId };
        const response = await jiraClient.post(`/issue/${issueIdOrKey}/watchers`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "remove_watcher": {
        const { issueIdOrKey, accountId } = args as {
          issueIdOrKey: string;
          accountId: string;
        };
        const response = await jiraClient.delete(`/issue/${issueIdOrKey}/watchers`, {
          params: { accountId },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_users_by_project": {
        const { projectIdOrKey, start = 0, maxResults = 50 } = args as {
          projectIdOrKey: string;
          start?: number;
          maxResults?: number;
        };
        const response = await jiraClient.get(`/project/${projectIdOrKey}/users`, {
          params: { start, maxResults },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_issue_types": {
        const { start = 0, maxResults = 50, expand = "icon" } = args as {
          start?: number;
          maxResults?: number;
          expand?: string;
        };
        const response = await jiraClient.get("/issuetype", {
          params: { start, maxResults, expand },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_priorities": {
        const { start = 0, maxResults = 50, expand = "icon" } = args as {
          start?: number;
          maxResults?: number;
          expand?: string;
        };
        const response = await jiraClient.get("/priority", {
          params: { start, maxResults, expand },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_statuses": {
        const { start = 0, maxResults = 50, expand = "icon" } = args as {
          start?: number;
          maxResults?: number;
          expand?: string;
        };
        const response = await jiraClient.get("/status", {
          params: { start, maxResults, expand },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_issue_type": {
        const { id } = args as { id: string };
        const response = await jiraClient.get(`/issuetype/${id}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_priority": {
        const { id } = args as { id: string };
        const response = await jiraClient.get(`/priority/${id}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_status": {
        const { id } = args as { id: string };
        const response = await jiraClient.get(`/status/${id}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_version": {
        const { id } = args as { id: string };
        const response = await jiraClient.get(`/version/${id}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "create_version": {
        const { name, projectId, description = "", releaseDate, overdue = false, userStartDate, userReleaseDate, startDate, archived = false, released = false, moveUnfixedIssuesTo } = args as {
          name: string;
          projectId: string;
          description?: string;
          releaseDate?: string;
          overdue?: boolean;
          userStartDate?: string;
          userReleaseDate?: string;
          startDate?: string;
          archived?: boolean;
          released?: boolean;
          moveUnfixedIssuesTo?: string;
        };
        const data: Record<string, any> = {
          name,
          description,
          archived,
          released,
          projectId,
        };
        if (releaseDate) data.releaseDate = releaseDate;
        if (overdue) data.overdue = overdue;
        if (userStartDate) data.userStartDate = userStartDate;
        if (userReleaseDate) data.userReleaseDate = userReleaseDate;
        if (startDate) data.startDate = startDate;
        if (moveUnfixedIssuesTo) data.moveUnfixedIssuesTo = moveUnfixedIssuesTo;
        const response = await jiraClient.post("/version", data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "update_version": {
        const { id, name, description, releaseDate, overdue, userStartDate, userReleaseDate, startDate, archived, released, moveUnfixedIssuesTo } = args as {
          id: string;
          name?: string;
          description?: string;
          releaseDate?: string;
          overdue?: boolean;
          userStartDate?: string;
          userReleaseDate?: string;
          startDate?: string;
          archived?: boolean;
          released?: boolean;
          moveUnfixedIssuesTo?: string;
        };
        const data: Record<string, any> = {};
        if (name !== undefined) data.name = name;
        if (description !== undefined) data.description = description;
        if (releaseDate !== undefined) data.releaseDate = releaseDate;
        if (overdue !== undefined) data.overdue = overdue;
        if (userStartDate !== undefined) data.userStartDate = userStartDate;
        if (userReleaseDate !== undefined) data.userReleaseDate = userReleaseDate;
        if (startDate !== undefined) data.startDate = startDate;
        if (archived !== undefined) data.archived = archived;
        if (released !== undefined) data.released = released;
        if (moveUnfixedIssuesTo !== undefined) data.moveUnfixedIssuesTo = moveUnfixedIssuesTo;
        const response = await jiraClient.put(`/version/${id}`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "delete_version": {
        const { id, moveUnfixedIssuesTo } = args as {
          id: string;
          moveUnfixedIssuesTo?: string;
        };
        const params: Record<string, any> = {};
        if (moveUnfixedIssuesTo) params.moveUnfixedIssuesTo = moveUnfixedIssuesTo;
        const response = await jiraClient.delete(`/version/${id}`, { params });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_components": {
        const { projectIdOrKey, start = 0, maxResults = 50 } = args as {
          projectIdOrKey: string;
          start?: number;
          maxResults?: number;
        };
        const response = await jiraClient.get(`/project/${projectIdOrKey}/components`, {
          params: { start, maxResults },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "create_component": {
        const { name, projectId, description = "", leadAccountId, leadId, assigneeType, archiverAccountId } = args as {
          name: string;
          projectId: string;
          description?: string;
          leadAccountId?: string;
          leadId?: string;
          assigneeType?: string;
          archiverAccountId?: string;
        };
        const data: Record<string, any> = {
          name,
          description,
          projectId,
        };
        if (leadAccountId) data.leadAccountId = leadAccountId;
        if (leadId) data.leadAccountId = leadId;
        if (assigneeType) data.assigneeType = assigneeType;
        if (archiverAccountId) data.archiverAccountId = archiverAccountId;
        const response = await jiraClient.post(`/project/${projectId}/components`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "update_component": {
        const { id, name, description, leadAccountId, leadId, assigneeType, archiverAccountId } = args as {
          id: string;
          name?: string;
          description?: string;
          leadAccountId?: string;
          leadId?: string;
          assigneeType?: string;
          archiverAccountId?: string;
        };
        const data: Record<string, any> = {};
        if (name !== undefined) data.name = name;
        if (description !== undefined) data.description = description;
        if (leadAccountId !== undefined) data.leadAccountId = leadAccountId;
        if (leadId !== undefined) data.leadAccountId = leadId;
        if (assigneeType !== undefined) data.assigneeType = assigneeType;
        if (archiverAccountId !== undefined) data.archiverAccountId = archiverAccountId;
        const response = await jiraClient.put(`/component/${id}`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "delete_component": {
        const { id } = args as { id: string };
        const response = await jiraClient.delete(`/component/${id}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "create_filter": {
        const { name, description = "", jql, sharedWith, favourite = false } = args as {
          name: string;
          description?: string;
          jql: string;
          sharedWith?: string;
          favourite?: boolean;
        };
        const data: Record<string, any> = {
          name,
          description,
          jql,
          favourite,
        };
        if (sharedWith) data.sharedWith = { type: sharedWith };
        const response = await jiraClient.post("/filter", data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_filter": {
        const { id } = args as { id: string };
        const response = await jiraClient.get(`/filter/${id}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "update_filter": {
        const { id, name, description, jql, favourite, sharedWith } = args as {
          id: string;
          name?: string;
          description?: string;
          jql?: string;
          favourite?: boolean;
          sharedWith?: string;
        };
        const data: Record<string, any> = {};
        if (name !== undefined) data.name = name;
        if (description !== undefined) data.description = description;
        if (jql !== undefined) data.jql = jql;
        if (favourite !== undefined) data.favourite = favourite;
        if (sharedWith !== undefined) data.sharedWith = { type: sharedWith };
        const response = await jiraClient.put(`/filter/${id}`, data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "delete_filter": {
        const { id } = args as { id: string };
        const response = await jiraClient.delete(`/filter/${id}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_groups": {
        const { start = 0, maxResults = 50, exclude } = args as {
          start?: number;
          maxResults?: number;
          exclude?: string[];
        };
        const params: Record<string, any> = { start, maxResults };
        if (exclude) params.exclude = exclude.join(",");
        const response = await jiraClient.get("/group", { params });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "create_group": {
        const { name } = args as { name: string };
        const data = { name };
        const response = await jiraClient.post("/group", data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "add_user_to_group": {
        const { groupName, accountId, username } = args as {
          groupName: string;
          accountId?: string;
          username?: string;
        };
        if (!accountId && !username) {
          throw new McpError(400, "Either accountId or username must be provided");
        }
        const data: Record<string, any> = {};
        if (accountId) data.accountId = accountId;
        if (username) data.name = username;
        const response = await jiraClient.post("/group/user", data, {
          params: { groupname: groupName },
        });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "remove_user_from_group": {
        const { groupName, accountId, username } = args as {
          groupName: string;
          accountId?: string;
          username?: string;
        };
        const params: Record<string, any> = { groupname: groupName };
        if (accountId) params.accountId = accountId;
        if (username) params.username = username;
        const response = await jiraClient.delete("/group/user", { params });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_user": {
        const { accountId, username, key, expand } = args as {
          accountId?: string;
          username?: string;
          key?: string;
          expand?: string;
        };
        const params: Record<string, any> = {};
        if (accountId) params.accountId = accountId;
        if (username) params.username = username;
        if (key) params.key = key;
        if (expand) params.expand = expand;
        const response = await jiraClient.get("/user", { params });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "search_users": {
        const { query, start = 0, maxResults = 50, active, exclude } = args as {
          query: string;
          start?: number;
          maxResults?: number;
          active?: boolean;
          exclude?: string[];
        };
        const params: Record<string, any> = { query, start, maxResults };
        if (active !== undefined) params.active = active;
        if (exclude) params.exclude = exclude.join(",");
        const response = await jiraClient.get("/user/search", { params });
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "create_issue_link": {
        const { typeId, inwardIssueId, outwardIssueId, comment } = args as {
          typeId: string;
          inwardIssueId: string;
          outwardIssueId: string;
          comment?: string;
        };
        const data: Record<string, any> = {
          type: { id: typeId },
          inwardIssue: { id: inwardIssueId },
          outwardIssue: { id: outwardIssueId },
        };
        if (comment) data.comment = { body: comment };
        const response = await jiraClient.post("/issueLink", data);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "get_issue_links": {
        const { issueLinkId } = args as { issueLinkId: string };
        const response = await jiraClient.get(`/issueLink/${issueLinkId}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      case "delete_issue_link": {
        const { issueLinkId } = args as { issueLinkId: string };
        const response = await jiraClient.delete(`/issueLink/${issueLinkId}`);
        return { content: [{ type: "text", text: JSON.stringify(response.data, null, 2) }] };
      }
      
      default:
        throw new McpError(400, `Unknown tool: ${name}`);
    }
  } catch (error) {
    const err = handleApiError(error);
    return { content: [{ type: "text", text: JSON.stringify(err) }] };
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Jira MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Server error:", error);
  process.exit(1);
});
