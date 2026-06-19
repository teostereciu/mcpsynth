from server import mcp, make_request

@mcp.tool()
def create_invoice(customer: str, auto_advance: bool = None, collection_method: str = None) -> dict:
    """Create an Invoice."""
    data = {"customer": customer}
    if auto_advance is not None:
        data["auto_advance"] = "true" if auto_advance else "false"
    if collection_method:
        data["collection_method"] = collection_method
    return make_request("POST", "/invoices", data=data)

@mcp.tool()
def retrieve_invoice(invoice_id: str) -> dict:
    """Retrieve an Invoice."""
    return make_request("GET", f"/invoices/{invoice_id}")

@mcp.tool()
def update_invoice(invoice_id: str, auto_advance: bool = None) -> dict:
    """Update an Invoice."""
    data = {}
    if auto_advance is not None:
        data["auto_advance"] = "true" if auto_advance else "false"
    return make_request("POST", f"/invoices/{invoice_id}", data=data)

@mcp.tool()
def delete_invoice(invoice_id: str) -> dict:
    """Delete an Invoice."""
    return make_request("DELETE", f"/invoices/{invoice_id}")

@mcp.tool()
def finalize_invoice(invoice_id: str) -> dict:
    """Finalize an Invoice."""
    return make_request("POST", f"/invoices/{invoice_id}/finalize")

@mcp.tool()
def pay_invoice(invoice_id: str) -> dict:
    """Pay an Invoice."""
    return make_request("POST", f"/invoices/{invoice_id}/pay")
