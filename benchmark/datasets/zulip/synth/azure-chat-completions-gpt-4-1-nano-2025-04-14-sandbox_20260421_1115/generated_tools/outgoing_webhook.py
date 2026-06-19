def send_outgoing_webhook_payload(payload):
    """Send an outgoing webhook payload."""
    return call_endpoint('/outgoing-webhook-payload', method='POST', request=payload)
