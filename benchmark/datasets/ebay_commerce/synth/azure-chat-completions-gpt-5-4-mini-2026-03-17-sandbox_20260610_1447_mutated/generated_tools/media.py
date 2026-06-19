from .common import request_json


def get_image(image_id: str):
    return request_json("GET", f"/commerce/media/v1_beta/image/{image_id}", media=True, token_type="user")
