class Recipe(object):
    def __init__(self, name, instructions, meal_type, subtype, servings, selected=False):
        self.name = name
        self.instructions = instructions
        self.meal_type = meal_type
        self.subtype = subtype
        self.servings = servings
        self.selected = selected
        
        
class Ingredient(object):
    def __init__(self, name, note=None):
        self.name = name
        self.note = note
        
        
class Quantity(object):
    def __init__(self, recipe_id, ingredient_id, amount, measurement, note=None):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.amount = amount
        self.measurement = measurement
        self.note = note