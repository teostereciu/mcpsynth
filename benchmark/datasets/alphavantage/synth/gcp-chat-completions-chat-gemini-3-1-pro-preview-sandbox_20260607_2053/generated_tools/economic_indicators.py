from .time_series import make_request

def get_cpi(interval: str = "monthly") -> dict:
    """Get Consumer Price Index (CPI)."""
    return make_request({
        "function": "CPI",
        "interval": interval
    })

def get_inflation() -> dict:
    """Get inflation rates."""
    return make_request({
        "function": "INFLATION"
    })

def get_real_gdp(interval: str = "annual") -> dict:
    """Get Real Gross Domestic Product (GDP)."""
    return make_request({
        "function": "REAL_GDP",
        "interval": interval
    })

def get_unemployment() -> dict:
    """Get unemployment rates."""
    return make_request({
        "function": "UNEMPLOYMENT"
    })

def get_treasury_yield(interval: str = "monthly", maturity: str = "10year") -> dict:
    """Get treasury yields."""
    return make_request({
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity
    })
