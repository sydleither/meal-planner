import re


def normalize_ingredients(ingredients):
    final_ingredients = []
    for line in ingredients.split('\n'):
        characters = re.findall('\w', line)
        if len(characters) > 0:
            quantity = re.findall('\d.+?(?=[a-zA-Z])', line)
            quantity = quantity[0].replace(' ', '') if len(quantity) > 0 else 0 #TODO modify for 1 8oz can
            measurement = re.findall('[\d][\d\/\s–.]*(\w+)', line)
            measurement = measurement[0].lower() if len(measurement) > 0 else 'NONE'
            item = re.sub('[\d][\d\/\s–.]*\w+', '', line, 1).strip(" -").rstrip()
            note = re.findall('\(.*\)|,.*', item)
            note = note[0].strip(", ()") if len(note) > 0 else 'NONE'
            item = re.sub('\(.*\)|,.*', '', item, 1)
            final_ingredients.append({'quantity':quantity, 'measurement':measurement, 'item':item, 'note':note})
    return final_ingredients


def parse_data(data):
    data = data.to_dict()
    name = data.get("name")
    ingredients = normalize_ingredients(data.get("ingredients"))
    instructions = data.get("instructions")
    print(ingredients)
    return name, ingredients, instructions