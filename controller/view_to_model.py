import re
from model.types import Recipe, Ingredient, Quantity, Planner
from model.recipe_model import add_recipe_to_database
from model.ingredient_model import add_ingredients_to_database
from model.quantity_model import add_quantities_to_database
from model.planner_model import add_planner_to_database, clear_planner


def ingredients_to_list(ingredients):
    final_ingredients = []
    temp_list = []
    
    for i in ingredients.replace('\r','').split('\n'):
        if len(i) > 2:
            line = re.findall(': (.*)', i)[0]
            temp_list.append(line)
            
        if len(temp_list) == 4:
            final_ingredients.append({'item':temp_list[0], 'quantity':temp_list[1], \
                                      'measurement':temp_list[2], 'note':temp_list[3]})
            temp_list = []
            
    return final_ingredients


def submit_recipe(data, name, link, meal_type, subtype, servings, vegan):
    data = data.to_dict()
    
    ingredients = ingredients_to_list(data.get("ingredients"))
    instructions = data.get("instructions")

    recipe = Recipe(name, instructions, link, meal_type, subtype, servings, vegan)
    ingredient_object_list = []
    for ingredient in ingredients: #TODO check that ingredient is not already in the database
        ingredient_object_list.append(Ingredient(ingredient.get('item')))
    
    recipe_id = add_recipe_to_database(recipe)
    ingredient_ids = add_ingredients_to_database(ingredient_object_list)
    
    quantity_object_list = []
    for i,ingredient_id in enumerate(ingredient_ids):
        quantity_object = Quantity(recipe_id, ingredient_id, ingredients[i].get('quantity'), \
                                   ingredients[i].get('measurement'), ingredients[i].get('note'))
        quantity_object_list.append(quantity_object)
        
    add_quantities_to_database(quantity_object_list)
    
    
def submit_planner(data):
    data = list(data.items())
    
    planner_list = []
    for i in range(0,len(data),7):
        planner = Planner(data[i][0][7:], data[i][1], data[i+1][1], data[i+2][1], \
                          data[i+3][1], data[i+4][1], data[i+5][1], data[i+6][1])
        planner_list.append(planner)
    
    clear_planner()
    add_planner_to_database(planner_list)