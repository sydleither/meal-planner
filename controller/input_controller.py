#TODO name this file something better

import re
from fractions import Fraction


def normalize_ingredients(ingredients):
    with open('controller/measurements.txt') as f:
        measurements = f.read().split()
    
    final_ingredients = []
    for line in ingredients.split('\n'):
        characters = re.findall('\w', line)
        if len(characters) > 0:
            quantity = re.findall('\d.+?(?=[a-zA-Z])', line)
            if len(quantity) == 0:
                quantity = 0
            else:
                quantity = float(sum([Fraction(x.strip('-').rstrip()) for x in quantity[0].split()]))
            
            measurement = re.findall('[\d][\d\/\s–.]*(\w+)', line)
            measurement = measurement[0].lower() if len(measurement) > 0 else 'NONE'
            measurement = measurement if measurement in measurements else 'NONE'
            if measurement == 'NONE':
                item = re.sub('[\d][\d\/\s–.]*', '', line, 1).strip(" -").rstrip()
            else:
                item = re.sub('[\d][\d\/\s–.]*\w+', '', line, 1).strip(" -").rstrip().replace('of ','')
                
            note = re.findall('\(.*\)|,.*', item)
            note = note[0].strip(", ()") if len(note) > 0 else 'NONE'
            
            item = re.sub('\(.*\)|,.*', '', item, 1).rstrip()
            
            final_ingredients.append({'item':item, 'quantity':quantity, 'measurement':measurement, 'note':note})
            
    return final_ingredients


def parse_data(data):
    data = data.to_dict()
    
    name = data.get("name")
    ingredients = normalize_ingredients(data.get("ingredients"))
    instructions = data.get("instructions")
    meal_type = data.get("type")
    subtype = data.get("subtype")
    servings = data.get("servings")
    vegan = data.get("vegan")
    
    return name, ingredients, instructions, meal_type, subtype, servings, vegan