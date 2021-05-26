import re
from model.types import Recipe, Ingredient, Quantity
from model.recipe_model import add_recipe_to_database
from model.ingredient_model import add_ingredients_to_database


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


def submit_data(data):
    data = data.to_dict()
    
    name = data.get("name")
    ingredients = ingredients_to_list(data.get("ingredients"))
    instructions = data.get("instructions")
    meal_type = data.get("type")
    subtype = data.get("subtype")
    servings = data.get("servings")
    
    recipe = Recipe(name, instructions, meal_type, subtype, servings)
    ingredient_class_list = []
    for ingredient in ingredients: #TODO check that ingredient is not already in the database
        ingredient_class_list.append(Ingredient(ingredient.get('item')))
    
    recipe_id = add_recipe_to_database(recipe)
    ingredient_ids = add_ingredients_to_database(ingredient_class_list)