from model.recipe_model import get_all_recipes, get_single_recipe, get_recipe_ingredients, get_single_recipe_name
from model.planner_model import get_planner


def planner():
    planner = get_planner()
    new_planner = []
    for meal in planner:
        new_meal = []
        for day in meal:
            try:
                int(day)
                new_meal.append([day,get_single_recipe_name(day)])
            except:
                new_meal.append([0,day])
        new_planner.append(new_meal)
    return new_planner


def all_recipes():
    recipes = get_all_recipes()
    return recipes


def single_recipe(recipe_id):
    recipe = list(get_single_recipe(recipe_id))
    recipe[3] = recipe[3].replace('\r\n\r\n', '\n')
    ingredients = get_recipe_ingredients(recipe_id)
    return recipe, ingredients