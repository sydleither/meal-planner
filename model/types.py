class Recipe(object):
    def __init__(self, name, instructions, link, meal_type, subtype, servings, vegan):
        self.name = name
        self.instructions = instructions
        self.link = link
        self.meal_type = meal_type
        self.subtype = subtype
        self.servings = servings
        self.vegan = vegan
        
        
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
        
        
class Planner(object):
    def __init__(self, meal, monday, tuesday, wednesday, thursday, friday, saturday, sunday):
        self.meal = meal
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday