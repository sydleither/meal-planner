from flask import Flask, render_template, request
from controller.input_controller import parse_data
from controller.view_to_model import submit_data
from controller.model_to_view import all_recipes, single_recipe


app = Flask(__name__, template_folder='view', static_folder='view')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/confirm', methods=['GET', 'POST'])
def add_recipe():
    data = request.form
    global name, link, meal_type, subtype, servings, vegan
    name, link, ingredients, instructions, meal_type, subtype, servings, vegan = parse_data(data)
    return render_template('confirm.html', name=name, ingredients=ingredients, \
                           instructions=instructions, link=link, meal_type=meal_type, \
                            subtype=subtype, servings=servings, vegan=vegan)


@app.route('/', methods=['GET', 'POST'])
def confirm_recipe():
    data = request.form
    submit_data(data, name, link, meal_type, subtype, servings, vegan)
    return render_template('index.html')


@app.route('/recipes', methods=['GET'])
def view_recipes():
    recipes = all_recipes()
    return render_template('recipes.html', recipes=recipes)


@app.route('/recipe', methods=['GET'])
def view_recipe():
    recipe_id = request.args.get('id')
    recipe, ingredients = single_recipe(recipe_id)
    return render_template('recipe.html', recipe_id=recipe_id, recipe=recipe, ingredients=ingredients)


if __name__ == '__main__':
    app.run(debug=True)