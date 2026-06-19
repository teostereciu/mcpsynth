from .common import get_user_token, get_base_url, request


def get_user():
    tok = get_user_token()
    if "error" in tok:
        return tok
    return request("GET", f"{get_base_url()}/commerce/identity/v1/user", tok["access_token"])
