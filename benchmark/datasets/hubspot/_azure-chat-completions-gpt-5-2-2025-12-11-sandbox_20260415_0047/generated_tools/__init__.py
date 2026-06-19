"""HubSpot MCP server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("hubspot-crm")

# Import modules so decorators run.
from . import associations as _associations  # noqa: E402,F401
from . import companies as _companies  # noqa: E402,F401
from . import contacts as _contacts  # noqa: E402,F401
from . import deals as _deals  # noqa: E402,F401
from . import owners as _owners  # noqa: E402,F401
from . import pipelines as _pipelines  # noqa: E402,F401
from . import properties as _properties  # noqa: E402,F401
from . import search as _search  # noqa: E402,F401
from . import tickets as _tickets  # noqa: E402,F401


# ---- Register tools ----

# Contacts
mcp.tool()(_contacts.contacts_create)
mcp.tool()(_contacts.contacts_get)
mcp.tool()(_contacts.contacts_list)
mcp.tool()(_contacts.contacts_update)
mcp.tool()(_contacts.contacts_delete)
mcp.tool()(_contacts.contacts_batch_create)
mcp.tool()(_contacts.contacts_batch_read)
mcp.tool()(_contacts.contacts_batch_update)
mcp.tool()(_contacts.contacts_batch_archive)
mcp.tool()(_contacts.contacts_associate)
mcp.tool()(_contacts.contacts_disassociate)

# Companies
mcp.tool()(_companies.companies_create)
mcp.tool()(_companies.companies_get)
mcp.tool()(_companies.companies_list)
mcp.tool()(_companies.companies_update)
mcp.tool()(_companies.companies_delete)
mcp.tool()(_companies.companies_batch_create)
mcp.tool()(_companies.companies_batch_read)
mcp.tool()(_companies.companies_batch_update)
mcp.tool()(_companies.companies_batch_archive)
mcp.tool()(_companies.companies_associate)
mcp.tool()(_companies.companies_disassociate)

# Deals
mcp.tool()(_deals.deals_create)
mcp.tool()(_deals.deals_get)
mcp.tool()(_deals.deals_list)
mcp.tool()(_deals.deals_update)
mcp.tool()(_deals.deals_delete)
mcp.tool()(_deals.deals_batch_create)
mcp.tool()(_deals.deals_batch_read)
mcp.tool()(_deals.deals_batch_update)
mcp.tool()(_deals.deals_batch_archive)
mcp.tool()(_deals.deals_associate)
mcp.tool()(_deals.deals_disassociate)

# Tickets
mcp.tool()(_tickets.tickets_create)
mcp.tool()(_tickets.tickets_get)
mcp.tool()(_tickets.tickets_list)
mcp.tool()(_tickets.tickets_update)
mcp.tool()(_tickets.tickets_delete)
mcp.tool()(_tickets.tickets_batch_create)
mcp.tool()(_tickets.tickets_batch_read)
mcp.tool()(_tickets.tickets_batch_update)
mcp.tool()(_tickets.tickets_batch_archive)
mcp.tool()(_tickets.tickets_associate)
mcp.tool()(_tickets.tickets_disassociate)

# Search
mcp.tool()(_search.crm_search)

# Owners
mcp.tool()(_owners.owners_list)
mcp.tool()(_owners.owners_get)

# Pipelines
mcp.tool()(_pipelines.pipelines_list)
mcp.tool()(_pipelines.pipelines_get)
mcp.tool()(_pipelines.pipelines_create)
mcp.tool()(_pipelines.pipelines_replace)
mcp.tool()(_pipelines.pipelines_update)
mcp.tool()(_pipelines.pipelines_delete)
mcp.tool()(_pipelines.pipeline_stages_list)
mcp.tool()(_pipelines.pipeline_stages_get)
mcp.tool()(_pipelines.pipeline_stages_create)
mcp.tool()(_pipelines.pipeline_stages_replace)
mcp.tool()(_pipelines.pipeline_stages_update)
mcp.tool()(_pipelines.pipeline_stages_delete)
mcp.tool()(_pipelines.pipelines_audit)
mcp.tool()(_pipelines.pipeline_stages_audit)

# Properties
mcp.tool()(_properties.properties_list)
mcp.tool()(_properties.properties_get)
mcp.tool()(_properties.properties_create)

# Associations
mcp.tool()(_associations.associations_v3_types)
mcp.tool()(_associations.associations_v3_batch_create)
mcp.tool()(_associations.associations_v3_batch_read)
mcp.tool()(_associations.associations_v3_batch_archive)
mcp.tool()(_associations.associations_v4_labels)
mcp.tool()(_associations.associations_v4_associate_default)
mcp.tool()(_associations.associations_v4_get_associations)
mcp.tool()(_associations.associations_v4_delete_all_between)
mcp.tool()(_associations.associations_v4_batch_read)
mcp.tool()(_associations.associations_v4_batch_associate_default)
