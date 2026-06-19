from generated_tools.common import api_get


def get_meal_plan_week(username, start_date, **kwargs):
    return api_get(f"/mealplanner/{username}/week/{start_date}", kwargs)


def get_meal_plan_day(username, date, **kwargs):
    return api_get(f"/mealplanner/{username}/day/{date}", kwargs)


def generate_meal_plan(**kwargs):
    return api_get("/mealplanner/generate", kwargs)
