from generated_tools.common import api_get


def wine_dishes(wine):
    return api_get("/food/wine/dishes", {"wine": wine})


def wine_pairing(food, **kwargs):
    return api_get("/food/wine/pairing", {"food": food, **kwargs})


def wine_description(wine):
    return api_get("/food/wine/description", {"wine": wine})


def wine_recommendation(wine, **kwargs):
    return api_get("/food/wine/recommendation", {"wine": wine, **kwargs})
