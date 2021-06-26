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
    measurements = create_measurement_dict()

    groceries = {}
    for recipe in recipes:
        try:
            int(recipe)
            ingredients = get_recipe_ingredients_with_ids(recipe)
            for ingredient in ingredients:
                if ingredient[0] in groceries:
                    new_grocery = add_measurements(measurements, ingredient[1], \
                                                   groceries[ingredient[0]][1], \
                                                   groceries[ingredient[0]][2], \
                                                   ingredient[2], ingredient[3])
                    groceries[ingredient[0]] = new_grocery
                else:
                    groceries[ingredient[0]] = [ingredient[1], ingredient[2], ingredient[3]]
        except:
            if recipe != '' and recipe != 'Leftovers':
                groceries[recipe] = []

    return groceries


def create_measurement_dict():
    measurements = {}
    measurements[1] = [['gallon'], 16]
    measurements[3] = [['quart'], 4]
    measurements[4] = [['pint'], 2]
    measurements[2] = [['cup', 'c', 'cups'], 1]
    measurements[5] = [['oz', 'ounce', 'ounces'], .125]
    measurements[6] = [['tbsp', 'tablespoon', 'tablespoons'], .0625]
    measurements[7] = [['tsp', 'teaspoon', 'teaspoons'], .0208]
    return measurements

    
def add_measurements(measurements, name, q1, m1, q2, m2):
    m1_cat = 0
    m2_cat = 0
    q_temp = 0
    m_temp = ''
    final_quantity = 0
    final_measurement = ''

    for key,value in measurements.items():
        if m1 in value[0]:
            m1_cat = key
        if m2 in value[0]:
            m2_cat = key
    if m1_cat != 0 and m2_cat != 0:
        if m1_cat > m2_cat:
            m_temp = m1_cat
            q_temp = q2/(measurements[m1_cat][1]/measurements[m2_cat][1])+q1
        elif m2_cat < m1_cat:
            m_temp = m2_cat
            q_temp = q1/(measurements[m2_cat][1]/measurements[m1_cat][1])+q2
        else:
            m_temp = m1_cat
            q_temp = q1+q2
    else:
        return #TODO deal with meausrements not in list

    if m1 == m2 or (m1_cat != '' and m2_cat != ''):
        q_in_cups = q_temp*measurements[m_temp][1]
        for i in range(0,len(measurements)):
            if q_in_cups == measurements[i+1][1]:
                final_measurement = measurements[i+1][0][0]
                final_quantity = q_in_cups/measurements[i+1][1]
            #TODO check if between
            
    return [name,final_quantity,final_measurement]