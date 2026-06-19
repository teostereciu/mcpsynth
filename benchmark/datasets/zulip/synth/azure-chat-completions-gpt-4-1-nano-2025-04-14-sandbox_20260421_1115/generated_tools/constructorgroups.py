def create_constructor_groups_call():
    """Create a Constructor Groups video call URL."""
    request = {}
    return call_endpoint('/calls/constructorgroups/create', method='POST', request=request)
