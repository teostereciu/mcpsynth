from generated_tools.common import api_get, api_post


def search_all_food(**kwargs):
    return api_get("/food/search", kwargs)


def search_food_videos(**kwargs):
    return api_get("/food/videos/search", kwargs)


def quick_answer(q):
    return api_get("/recipes/quickAnswer", {"q": q})


def detect_food(text):
    return api_post("/food/detect", {"text": text})


def search_site_content(search_query):
    return api_get("/food/site/search", {"search_query": search_query})
