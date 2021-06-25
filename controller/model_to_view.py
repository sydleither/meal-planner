from model.recipe_model import get_all_recipes, get_single_recipe, \
    get_recipe_ingredients, get_recipe_ingredients_with_ids, get_single_recipe_name
from model.planner_model import get_planner, get_planner_recipe_ids


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


def grocery_list():
    planner = get_planner_recipe_ids()
    recipes = [x for meal in planner for x in meal]

    groceries = {}
    for recipe in recipes:
        try:
            int(recipe)
            ingredients = get_recipe_ingredients_with_ids(recipe)
            for ingredient in ingredients:
                if ingredient[0] in groceries:
                    new_grocery = add_measurements(ingredient[0], \
                                                   groceries[ingredient[0]][1], \
                                                   groceries[ingredient[0]][2], \
                                                   ingredient[1], ingredient[2])
                    groceries[ingredient[0]] = new_grocery
                else:
                    groceries[ingredient[0]] = [ingredient[1], ingredient[2], ingredient[3]]
        except:
            if recipe != '' and recipe != 'Leftovers':
                groceries[recipe] = []
    
    
def add_measurements(name, q1, m1, q2, m2): #TODO deal with meausrements not in list
    measurements = open('controller/measurements.txt').read().split()
    
    return [name,0,'']