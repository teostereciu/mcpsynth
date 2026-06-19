import os
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.contacts import (
    contacts_archive,
    contacts_associate,
    contacts_batch_create,
    contacts_batch_read,
    contacts_batch_update,
    contacts_batch_upsert,
    contacts_create,
    contacts_disassociate,
    contacts_get,
    contacts_list,
    contacts_update,
)
from generated_tools.companies import (
    companies_archive,
    companies_associate,
    companies_batch_archive,
    companies_batch_create,
    companies_batch_read,
    companies_batch_update,
    companies_create,
    companies_disassociate,
    companies_get,
    companies_list,
    companies_update,
)
from generated_tools.deals import (
    deals_archive,
    deals_associate,
    deals_batch_archive,
    deals_batch_create,
    deals_batch_read,
    deals_batch_update,
    deals_create,
    deals_disassociate,
    deals_get,
    deals_list,
    deals_update,
)
from generated_tools.tickets import (
    tickets_archive,
    tickets_associate,
    tickets_batch_archive,
    tickets_batch_create,
    tickets_batch_read,
    tickets_batch_update,
    tickets_create,
    tickets_disassociate,
    tickets_get,
    tickets_list,
    tickets_update,
)
from generated_tools.search import crm_search
from generated_tools.associations_v4 import (
    associations_v4_associate_default,
    associations_v4_associate_labeled,
    associations_v4_batch_archive_all,
    associations_v4_batch_archive_labels,
    associations_v4_batch_associate_default,
    associations_v4_batch_create_labeled,
    associations_v4_batch_read,
    associations_v4_delete_all_between,
    associations_v4_get,
    associations_v4_get_labels,
)
from generated_tools.owners import owners_get, owners_list
from generated_tools.pipelines import (
    pipeline_stages_audit,
    pipeline_stages_create,
    pipeline_stages_delete,
    pipeline_stages_get,
    pipeline_stages_list,
    pipeline_stages_replace,
    pipeline_stages_update,
    pipelines_audit,
    pipelines_create,
    pipelines_delete,
    pipelines_get,
    pipelines_list,
    pipelines_replace,
    pipelines_update,
)
from generated_tools.properties import (
    properties_archive,
    properties_create,
    properties_get,
    properties_list,
    properties_update,
)
from generated_tools.notes import (
    notes_archive,
    notes_associate,
    notes_batch_archive,
    notes_batch_create,
    notes_batch_read,
    notes_batch_update,
    notes_create,
    notes_disassociate,
    notes_get,
    notes_list,
    notes_update,
)
from generated_tools.tasks import (
    tasks_archive,
    tasks_associate,
    tasks_batch_archive,
    tasks_batch_create,
    tasks_batch_read,
    tasks_batch_update,
    tasks_create,
    tasks_disassociate,
    tasks_get,
    tasks_list,
    tasks_update,
)
from generated_tools.calls import (
    calls_archive,
    calls_associate,
    calls_batch_archive,
    calls_batch_create,
    calls_batch_read,
    calls_batch_update,
    calls_create,
    calls_disassociate,
    calls_get,
    calls_list,
    calls_update,
)
from generated_tools.meetings import (
    meetings_archive,
    meetings_associate,
    meetings_batch_archive,
    meetings_batch_create,
    meetings_batch_read,
    meetings_batch_update,
    meetings_create,
    meetings_disassociate,
    meetings_get,
    meetings_list,
    meetings_update,
)
from generated_tools.communications import (
    communications_archive,
    communications_associate,
    communications_batch_read,
    communications_batch_update,
    communications_create,
    communications_disassociate,
    communications_get,
    communications_list,
    communications_update,
)

mcp = FastMCP("hubspot-crm")


def _auth_check() -> Optional[Dict[str, Any]]:
    if not os.getenv("HUBSPOT_ACCESS_TOKEN"):
        return {"error": "missing_env", "details": "HUBSPOT_ACCESS_TOKEN is not set"}
    return None


@mcp.tool()
def hubspot_auth_status() -> Dict[str, Any]:
    """Check whether HUBSPOT_ACCESS_TOKEN is set."""
    err = _auth_check()
    return {"ok": err is None, **({} if err is None else err)}


# Contacts
@mcp.tool()
def hubspot_contacts_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_create(properties, associations)


@mcp.tool()
def hubspot_contacts_get(
    contact_id_or_email: str,
    id_property: Optional[str] = None,
    properties: Optional[str] = None,
    properties_with_history: Optional[str] = None,
    associations: Optional[str] = None,
    archived: Optional[bool] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_get(
        contact_id_or_email,
        id_property=id_property,
        properties=properties,
        properties_with_history=properties_with_history,
        associations=associations,
        archived=archived,
    )


@mcp.tool()
def hubspot_contacts_list(
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[str] = None,
    properties_with_history: Optional[str] = None,
    associations: Optional[str] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_list(
        limit=limit,
        after=after,
        properties=properties,
        properties_with_history=properties_with_history,
        associations=associations,
        archived=archived,
    )


@mcp.tool()
def hubspot_contacts_update(contact_id_or_email: str, properties: Dict[str, Any], id_property: Optional[str] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_update(contact_id_or_email, properties, id_property=id_property)


@mcp.tool()
def hubspot_contacts_archive(contact_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_archive(contact_id)


@mcp.tool()
def hubspot_contacts_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_batch_create(inputs)


@mcp.tool()
def hubspot_contacts_batch_read(
    inputs: List[Dict[str, Any]],
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_batch_read(
        inputs,
        id_property=id_property,
        properties=properties,
        properties_with_history=properties_with_history,
    )


@mcp.tool()
def hubspot_contacts_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_batch_update(inputs)


@mcp.tool()
def hubspot_contacts_batch_upsert(inputs: List[Dict[str, Any]], id_property: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_batch_upsert(inputs, id_property)


@mcp.tool()
def hubspot_contacts_associate(contact_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_associate(contact_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_contacts_disassociate(contact_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or contacts_disassociate(contact_id, to_object_type, to_object_id, association_type_id)


# Companies
@mcp.tool()
def hubspot_companies_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_create(properties, associations)


@mcp.tool()
def hubspot_companies_get(
    company_id: str,
    properties: Optional[str] = None,
    properties_with_history: Optional[str] = None,
    associations: Optional[str] = None,
    archived: Optional[bool] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_get(
        company_id,
        properties=properties,
        properties_with_history=properties_with_history,
        associations=associations,
        archived=archived,
    )


@mcp.tool()
def hubspot_companies_list(
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[str] = None,
    properties_with_history: Optional[str] = None,
    associations: Optional[str] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_list(
        limit=limit,
        after=after,
        properties=properties,
        properties_with_history=properties_with_history,
        associations=associations,
        archived=archived,
    )


@mcp.tool()
def hubspot_companies_update(company_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_update(company_id, properties)


@mcp.tool()
def hubspot_companies_archive(company_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_archive(company_id)


@mcp.tool()
def hubspot_companies_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_batch_create(inputs)


@mcp.tool()
def hubspot_companies_batch_read(
    inputs: List[Dict[str, Any]],
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_batch_read(
        inputs,
        id_property=id_property,
        properties=properties,
        properties_with_history=properties_with_history,
    )


@mcp.tool()
def hubspot_companies_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_batch_update(inputs)


@mcp.tool()
def hubspot_companies_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_batch_archive(inputs)


@mcp.tool()
def hubspot_companies_associate(company_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_associate(company_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_companies_disassociate(company_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or companies_disassociate(company_id, to_object_type, to_object_id, association_type_id)


# Deals
@mcp.tool()
def hubspot_deals_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_create(properties, associations)


@mcp.tool()
def hubspot_deals_get(
    deal_id: str,
    properties: Optional[str] = None,
    properties_with_history: Optional[str] = None,
    associations: Optional[str] = None,
    archived: Optional[bool] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_get(
        deal_id,
        properties=properties,
        properties_with_history=properties_with_history,
        associations=associations,
        archived=archived,
    )


@mcp.tool()
def hubspot_deals_list(
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[str] = None,
    properties_with_history: Optional[str] = None,
    associations: Optional[str] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_list(
        limit=limit,
        after=after,
        properties=properties,
        properties_with_history=properties_with_history,
        associations=associations,
        archived=archived,
    )


@mcp.tool()
def hubspot_deals_update(deal_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_update(deal_id, properties)


@mcp.tool()
def hubspot_deals_archive(deal_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_archive(deal_id)


@mcp.tool()
def hubspot_deals_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_batch_create(inputs)


@mcp.tool()
def hubspot_deals_batch_read(
    inputs: List[Dict[str, Any]],
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_batch_read(
        inputs,
        id_property=id_property,
        properties=properties,
        properties_with_history=properties_with_history,
    )


@mcp.tool()
def hubspot_deals_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_batch_update(inputs)


@mcp.tool()
def hubspot_deals_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_batch_archive(inputs)


@mcp.tool()
def hubspot_deals_associate(deal_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_associate(deal_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_deals_disassociate(deal_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or deals_disassociate(deal_id, to_object_type, to_object_id, association_type_id)


# Tickets
@mcp.tool()
def hubspot_tickets_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_create(properties, associations)


@mcp.tool()
def hubspot_tickets_get(
    ticket_id: str,
    properties: Optional[str] = None,
    properties_with_history: Optional[str] = None,
    associations: Optional[str] = None,
    archived: Optional[bool] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_get(
        ticket_id,
        properties=properties,
        properties_with_history=properties_with_history,
        associations=associations,
        archived=archived,
    )


@mcp.tool()
def hubspot_tickets_list(
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[str] = None,
    properties_with_history: Optional[str] = None,
    associations: Optional[str] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_list(
        limit=limit,
        after=after,
        properties=properties,
        properties_with_history=properties_with_history,
        associations=associations,
        archived=archived,
    )


@mcp.tool()
def hubspot_tickets_update(ticket_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_update(ticket_id, properties)


@mcp.tool()
def hubspot_tickets_archive(ticket_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_archive(ticket_id)


@mcp.tool()
def hubspot_tickets_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_batch_create(inputs)


@mcp.tool()
def hubspot_tickets_batch_read(
    inputs: List[Dict[str, Any]],
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_batch_read(
        inputs,
        id_property=id_property,
        properties=properties,
        properties_with_history=properties_with_history,
    )


@mcp.tool()
def hubspot_tickets_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_batch_update(inputs)


@mcp.tool()
def hubspot_tickets_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_batch_archive(inputs)


@mcp.tool()
def hubspot_tickets_associate(ticket_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_associate(ticket_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_tickets_disassociate(ticket_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or tickets_disassociate(ticket_id, to_object_type, to_object_id, association_type_id)


# Search
@mcp.tool()
def hubspot_crm_search(
    object_type: str,
    query: Optional[str] = None,
    filter_groups: Optional[List[Dict[str, Any]]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    properties: Optional[List[str]] = None,
    limit: Optional[int] = None,
    after: Optional[str] = None,
) -> Dict[str, Any]:
    err = _auth_check()
    return err or crm_search(
        object_type,
        query=query,
        filter_groups=filter_groups,
        sorts=sorts,
        properties=properties,
        limit=limit,
        after=after,
    )


# Associations v4
@mcp.tool()
def hubspot_associations_v4_get_labels(from_object_type: str, to_object_type: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_get_labels(from_object_type, to_object_type)


@mcp.tool()
def hubspot_associations_v4_associate_default(from_object_type: str, from_object_id: str, to_object_type: str, to_object_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_associate_default(from_object_type, from_object_id, to_object_type, to_object_id)


@mcp.tool()
def hubspot_associations_v4_batch_associate_default(from_object_type: str, to_object_type: str, inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_batch_associate_default(from_object_type, to_object_type, inputs)


@mcp.tool()
def hubspot_associations_v4_associate_labeled(
    from_object_type: str,
    from_object_id: str,
    to_object_type: str,
    to_object_id: str,
    types: List[Dict[str, Any]],
) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_associate_labeled(from_object_type, from_object_id, to_object_type, to_object_id, types)


@mcp.tool()
def hubspot_associations_v4_batch_create_labeled(from_object_type: str, to_object_type: str, inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_batch_create_labeled(from_object_type, to_object_type, inputs)


@mcp.tool()
def hubspot_associations_v4_get(from_object_type: str, object_id: str, to_object_type: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_get(from_object_type, object_id, to_object_type)


@mcp.tool()
def hubspot_associations_v4_batch_read(from_object_type: str, to_object_type: str, inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_batch_read(from_object_type, to_object_type, inputs)


@mcp.tool()
def hubspot_associations_v4_delete_all_between(from_object_type: str, from_object_id: str, to_object_type: str, to_object_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_delete_all_between(from_object_type, from_object_id, to_object_type, to_object_id)


@mcp.tool()
def hubspot_associations_v4_batch_archive_all(from_object_type: str, to_object_type: str, inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_batch_archive_all(from_object_type, to_object_type, inputs)


@mcp.tool()
def hubspot_associations_v4_batch_archive_labels(from_object_type: str, to_object_type: str, inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or associations_v4_batch_archive_labels(from_object_type, to_object_type, inputs)


# Owners
@mcp.tool()
def hubspot_owners_list(archived: bool = False, email: Optional[str] = None, after: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or owners_list(archived=archived, email=email, after=after, limit=limit)


@mcp.tool()
def hubspot_owners_get(owner_id: str, archived: Optional[bool] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or owners_get(owner_id, archived=archived)


# Pipelines
@mcp.tool()
def hubspot_pipelines_list(object_type: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipelines_list(object_type)


@mcp.tool()
def hubspot_pipelines_get(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipelines_get(object_type, pipeline_id)


@mcp.tool()
def hubspot_pipelines_create(object_type: str, pipeline: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipelines_create(object_type, pipeline)


@mcp.tool()
def hubspot_pipelines_replace(object_type: str, pipeline_id: str, pipeline: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipelines_replace(object_type, pipeline_id, pipeline)


@mcp.tool()
def hubspot_pipelines_update(object_type: str, pipeline_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipelines_update(object_type, pipeline_id, properties)


@mcp.tool()
def hubspot_pipelines_delete(object_type: str, pipeline_id: str, validate_references_before_delete: bool = False) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipelines_delete(object_type, pipeline_id, validate_references_before_delete=validate_references_before_delete)


@mcp.tool()
def hubspot_pipeline_stages_list(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipeline_stages_list(object_type, pipeline_id)


@mcp.tool()
def hubspot_pipeline_stages_get(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipeline_stages_get(object_type, pipeline_id, stage_id)


@mcp.tool()
def hubspot_pipeline_stages_create(object_type: str, pipeline_id: str, stage: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipeline_stages_create(object_type, pipeline_id, stage)


@mcp.tool()
def hubspot_pipeline_stages_replace(object_type: str, pipeline_id: str, stage_id: str, stage: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipeline_stages_replace(object_type, pipeline_id, stage_id, stage)


@mcp.tool()
def hubspot_pipeline_stages_update(object_type: str, pipeline_id: str, stage_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipeline_stages_update(object_type, pipeline_id, stage_id, properties)


@mcp.tool()
def hubspot_pipeline_stages_delete(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipeline_stages_delete(object_type, pipeline_id, stage_id)


@mcp.tool()
def hubspot_pipelines_audit(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipelines_audit(object_type, pipeline_id)


@mcp.tool()
def hubspot_pipeline_stages_audit(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or pipeline_stages_audit(object_type, pipeline_id, stage_id)


# Properties
@mcp.tool()
def hubspot_properties_list(object_type: str, data_sensitivity: Optional[str] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or properties_list(object_type, data_sensitivity=data_sensitivity)


@mcp.tool()
def hubspot_properties_get(object_type: str, property_name: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or properties_get(object_type, property_name)


@mcp.tool()
def hubspot_properties_create(object_type: str, definition: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or properties_create(object_type, definition)


@mcp.tool()
def hubspot_properties_update(object_type: str, property_name: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or properties_update(object_type, property_name, updates)


@mcp.tool()
def hubspot_properties_archive(object_type: str, property_name: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or properties_archive(object_type, property_name)


# Notes
@mcp.tool()
def hubspot_notes_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_create(properties, associations)


@mcp.tool()
def hubspot_notes_get(note_id: str, properties: Optional[str] = None, associations: Optional[str] = None, archived: Optional[bool] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_get(note_id, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_notes_list(limit: int = 100, after: Optional[str] = None, properties: Optional[str] = None, associations: Optional[str] = None, archived: bool = False) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_list(limit=limit, after=after, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_notes_update(note_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_update(note_id, properties)


@mcp.tool()
def hubspot_notes_archive(note_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_archive(note_id)


@mcp.tool()
def hubspot_notes_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_batch_create(inputs)


@mcp.tool()
def hubspot_notes_batch_read(inputs: List[Dict[str, Any]], id_property: Optional[str] = None, properties: Optional[List[str]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_batch_read(inputs, id_property=id_property, properties=properties)


@mcp.tool()
def hubspot_notes_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_batch_update(inputs)


@mcp.tool()
def hubspot_notes_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_batch_archive(inputs)


@mcp.tool()
def hubspot_notes_associate(note_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_associate(note_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_notes_disassociate(note_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or notes_disassociate(note_id, to_object_type, to_object_id, association_type_id)


# Tasks
@mcp.tool()
def hubspot_tasks_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_create(properties, associations)


@mcp.tool()
def hubspot_tasks_get(task_id: str, properties: Optional[str] = None, associations: Optional[str] = None, archived: Optional[bool] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_get(task_id, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_tasks_list(limit: int = 100, after: Optional[str] = None, properties: Optional[str] = None, associations: Optional[str] = None, archived: bool = False) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_list(limit=limit, after=after, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_tasks_update(task_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_update(task_id, properties)


@mcp.tool()
def hubspot_tasks_archive(task_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_archive(task_id)


@mcp.tool()
def hubspot_tasks_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_batch_create(inputs)


@mcp.tool()
def hubspot_tasks_batch_read(inputs: List[Dict[str, Any]], id_property: Optional[str] = None, properties: Optional[List[str]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_batch_read(inputs, id_property=id_property, properties=properties)


@mcp.tool()
def hubspot_tasks_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_batch_update(inputs)


@mcp.tool()
def hubspot_tasks_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_batch_archive(inputs)


@mcp.tool()
def hubspot_tasks_associate(task_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_associate(task_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_tasks_disassociate(task_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or tasks_disassociate(task_id, to_object_type, to_object_id, association_type_id)


# Calls
@mcp.tool()
def hubspot_calls_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_create(properties, associations)


@mcp.tool()
def hubspot_calls_get(call_id: str, properties: Optional[str] = None, associations: Optional[str] = None, archived: Optional[bool] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_get(call_id, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_calls_list(limit: int = 100, after: Optional[str] = None, properties: Optional[str] = None, associations: Optional[str] = None, archived: bool = False) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_list(limit=limit, after=after, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_calls_update(call_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_update(call_id, properties)


@mcp.tool()
def hubspot_calls_archive(call_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_archive(call_id)


@mcp.tool()
def hubspot_calls_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_batch_create(inputs)


@mcp.tool()
def hubspot_calls_batch_read(inputs: List[Dict[str, Any]], id_property: Optional[str] = None, properties: Optional[List[str]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_batch_read(inputs, id_property=id_property, properties=properties)


@mcp.tool()
def hubspot_calls_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_batch_update(inputs)


@mcp.tool()
def hubspot_calls_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_batch_archive(inputs)


@mcp.tool()
def hubspot_calls_associate(call_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_associate(call_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_calls_disassociate(call_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or calls_disassociate(call_id, to_object_type, to_object_id, association_type_id)


# Meetings
@mcp.tool()
def hubspot_meetings_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_create(properties, associations)


@mcp.tool()
def hubspot_meetings_get(meeting_id: str, properties: Optional[str] = None, associations: Optional[str] = None, archived: Optional[bool] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_get(meeting_id, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_meetings_list(limit: int = 100, after: Optional[str] = None, properties: Optional[str] = None, associations: Optional[str] = None, archived: bool = False) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_list(limit=limit, after=after, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_meetings_update(meeting_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_update(meeting_id, properties)


@mcp.tool()
def hubspot_meetings_archive(meeting_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_archive(meeting_id)


@mcp.tool()
def hubspot_meetings_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_batch_create(inputs)


@mcp.tool()
def hubspot_meetings_batch_read(inputs: List[Dict[str, Any]], id_property: Optional[str] = None, properties: Optional[List[str]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_batch_read(inputs, id_property=id_property, properties=properties)


@mcp.tool()
def hubspot_meetings_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_batch_update(inputs)


@mcp.tool()
def hubspot_meetings_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_batch_archive(inputs)


@mcp.tool()
def hubspot_meetings_associate(meeting_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_associate(meeting_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_meetings_disassociate(meeting_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    err = _auth_check()
    return err or meetings_disassociate(meeting_id, to_object_type, to_object_id, association_type_id)


# Communications
@mcp.tool()
def hubspot_communications_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_create(properties, associations)


@mcp.tool()
def hubspot_communications_get(communication_id: str, properties: Optional[str] = None, associations: Optional[str] = None, archived: Optional[bool] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_get(communication_id, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_communications_list(limit: int = 100, after: Optional[str] = None, properties: Optional[str] = None, associations: Optional[str] = None, archived: bool = False) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_list(limit=limit, after=after, properties=properties, associations=associations, archived=archived)


@mcp.tool()
def hubspot_communications_update(communication_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_update(communication_id, properties)


@mcp.tool()
def hubspot_communications_archive(communication_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_archive(communication_id)


@mcp.tool()
def hubspot_communications_batch_read(inputs: List[Dict[str, Any]], id_property: Optional[str] = None, properties: Optional[List[str]] = None) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_batch_read(inputs, id_property=id_property, properties=properties)


@mcp.tool()
def hubspot_communications_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_batch_update(inputs)


@mcp.tool()
def hubspot_communications_associate(communication_id: str, to_object_type: str, to_object_id: str, association_type_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_associate(communication_id, to_object_type, to_object_id, association_type_id)


@mcp.tool()
def hubspot_communications_disassociate(communication_id: str, to_object_type: str, to_object_id: str, association_type_id: str) -> Dict[str, Any]:
    err = _auth_check()
    return err or communications_disassociate(communication_id, to_object_type, to_object_id, association_type_id)


if __name__ == "__main__":
    mcp.run()
