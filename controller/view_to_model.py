def ingredients_to_list(ingredients):
    print('')


def submit_data(data):
    data = data.to_dict()
    
    name = data.get("name")
    ingredients = ingredients_to_list(data.get("ingredients"))
    instructions = data.get("instructions")
    meal_type = data.get("type")
    subtype = data.get("subtype")
    servings = data.get("servings")