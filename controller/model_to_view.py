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
    
    
def add_measurements(name, q1, m1, q2, m2):
    measurements = {} #TODO read in measurements dict
    m1_cat = ''
    m2_cat = ''
    q_temp = 0
    final_quantity = 0
    final_measurement = ''
    
    if m1 == m2:
        final_measurement = m1
        q_temp = q1+q2
    else:
        for key,value in measurements.items():
            if m1 in value[0]:
                m1_cat = key
            if m2 in value[0]:
                m2_cat = key
        if m1_cat != '' and m2_cat != '':
            if m1_cat > m2_cat:
                final_measurement = measurements[m1_cat][0]
                q_temp = q2/(measurements[m1_cat]/measurements[m2_cat])
            elif m2_cat < m1_cat:
                final_measurement = measurements[m2_cat][0]
                q_temp = q1/(measurements[m2_cat]/measurements[m1_cat])
            else:
                final_measurement = measurements[m1_cat][0]
                q_temp = q1+q2
        else:
            return #TODO deal with meausrements not in list

    if m1 == m2 or (m1_cat != '' and m2_cat != ''):
        return #TODO convert quantity to proper measurement
        
    return [name,final_quantity,final_measurement]