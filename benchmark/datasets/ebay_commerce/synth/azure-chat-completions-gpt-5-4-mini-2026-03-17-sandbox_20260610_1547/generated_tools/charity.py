from .common import get_user_token, get_base_url, request


def get_charity_org(org_id):
    tok = get_user_token()
    if "error" in tok:
        return tok
    return request("GET", f"{get_base_url()}/commerce/charity/v1/charity_org/{org_id}", tok["access_token"])


def get_charity_orgs(q=None, limit=None, offset=None):
    tok = get_user_token()
    if "error" in tok:
        return tok
    params = {k: v for k, v in {"q": q, "limit": limit, "offset": offset}.items() if v is not None}
    return request("GET", f"{get_base_url()}/commerce/charity/v1/charity_org", tok["access_token"], params=params)
