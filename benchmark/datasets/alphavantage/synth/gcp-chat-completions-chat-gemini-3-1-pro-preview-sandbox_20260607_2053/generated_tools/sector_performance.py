from .time_series import make_request

def get_sector_performance() -> dict:
    """Get real-time sector performance across S&P 500."""
    return make_request({
        "function": "SECTOR"
    })
