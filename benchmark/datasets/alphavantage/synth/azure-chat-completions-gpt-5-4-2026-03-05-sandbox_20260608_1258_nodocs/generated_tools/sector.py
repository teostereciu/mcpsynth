from .common import alpha_vantage_get


def get_sector_performance():
    return alpha_vantage_get({"function": "SECTOR"})
