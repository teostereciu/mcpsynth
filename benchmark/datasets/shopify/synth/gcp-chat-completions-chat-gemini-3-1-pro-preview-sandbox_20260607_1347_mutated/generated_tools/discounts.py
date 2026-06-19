import json

def register_tools(mcp, make_request):
    # Price Rules
    @mcp.tool()
    def get_price_rules(limit: int = 50):
        """Retrieve a list of price rules."""
        return make_request("GET", "/price_rules.json", params={"limit": limit})

    @mcp.tool()
    def get_price_rule(price_rule_id: int):
        """Retrieve a single price rule by ID."""
        return make_request("GET", f"/price_rules/{price_rule_id}.json")

    @mcp.tool()
    def create_price_rule(title: str, target_type: str, target_selection: str, allocation_method: str, value_type: str, value: str, customer_selection: str, starts_at: str):
        """Create a new price rule."""
        rule = {
            "title": title,
            "target_type": target_type,
            "target_selection": target_selection,
            "allocation_method": allocation_method,
            "value_type": value_type,
            "value": value,
            "customer_selection": customer_selection,
            "starts_at": starts_at
        }
        return make_request("POST", "/price_rules.json", json_data={"price_rule": rule})

    @mcp.tool()
    def update_price_rule(price_rule_id: int, title: str = None, value: str = None, ends_at: str = None):
        """Update an existing price rule."""
        rule = {"id": price_rule_id}
        if title: rule["title"] = title
        if value: rule["value"] = value
        if ends_at: rule["ends_at"] = ends_at
        return make_request("PUT", f"/price_rules/{price_rule_id}.json", json_data={"price_rule": rule})

    @mcp.tool()
    def delete_price_rule(price_rule_id: int):
        """Delete a price rule."""
        return make_request("DELETE", f"/price_rules/{price_rule_id}.json")

    # Discount Codes
    @mcp.tool()
    def get_discount_codes(price_rule_id: int):
        """Retrieve a list of discount codes for a price rule."""
        return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json")

    @mcp.tool()
    def get_discount_code(price_rule_id: int, discount_code_id: int):
        """Retrieve a single discount code by ID."""
        return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")

    @mcp.tool()
    def create_discount_code(price_rule_id: int, code: str):
        """Create a new discount code for a price rule."""
        discount_code = {"code": code}
        return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json_data={"discount_code": discount_code})

    @mcp.tool()
    def update_discount_code(price_rule_id: int, discount_code_id: int, code: str):
        """Update an existing discount code."""
        discount_code = {"id": discount_code_id, "code": code}
        return make_request("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", json_data={"discount_code": discount_code})

    @mcp.tool()
    def delete_discount_code(price_rule_id: int, discount_code_id: int):
        """Delete a discount code."""
        return make_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
