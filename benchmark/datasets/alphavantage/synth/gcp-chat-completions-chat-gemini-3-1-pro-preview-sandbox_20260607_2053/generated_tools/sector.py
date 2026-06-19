from .base import make_request

def get_sector_performance() -> dict:
    """Get real-time sector performance."""
    return make_request({
        "function": "SECTOR"
    })
