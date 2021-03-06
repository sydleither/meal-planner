from flask import Flask, render_template, request, redirect
from controller.recipe_input_parser import parse_data
from controller.view_to_model import submit_recipe, submit_planner, delete_recipe
from controller.model_to_view import all_recipes, single_recipe, planner, grocery_list


app = Flask(__name__, template_folder='view', static_folder='view')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/new', methods=['GET'])
def new_recipe():
    return render_template('new_recipe.html')


@app.route('/planner/new', methods=['GET'])
def new_planner():
    recipes = all_recipes()
    return render_template('new_planner.html', recipes=recipes)


@app.route('/planner', methods=['POST'])
def new_planner_submit():
    data = request.form
    submit_planner(data)
    planner_data = planner()
    return render_template('planner.html', planner=planner_data)


@app.route('/planner', methods=['GET'])
def view_planner():
    planner_data = planner()
    return render_template('planner.html', planner=planner_data)


@app.route('/groceries', methods=['GET'])
def view_groceries():
    groceries = grocery_list()
    return render_template('groceries.html', groceries=groceries)


@app.route('/confirm', methods=['POST'])
def add_recipe():
    data = request.form
    global name, link, meal_type, subtype, servings, vegan
    name, link, ingredients, instructions, meal_type, subtype, servings, vegan = parse_data(data)
    return render_template('confirm.html', name=name, ingredients=ingredients, \
                           instructions=instructions, link=link, meal_type=meal_type, \
                            subtype=subtype, servings=servings, vegan=vegan)


@app.route('/new', methods=['POST'])
def confirm_recipe():
    data = request.form
    submit_recipe(data, name, link, meal_type, subtype, servings, vegan)
    return render_template('new_recipe.html')


@app.route('/recipes', methods=['GET'])
def view_recipes():
    recipes = all_recipes()
    return render_template('recipes.html', recipes=recipes)


@app.route('/recipe', methods=['GET'])
def view_recipe():
    recipe_id = request.args.get('id')
    recipe, ingredients = single_recipe(recipe_id)
    return render_template('recipe.html', recipe_id=recipe_id, recipe=recipe, ingredients=ingredients)


@app.route('/delete', methods=['GET'])
def remove_recipe():
    delete_recipe(request.args.get('id'))
    return redirect('recipes')


if __name__ == '__main__':
    app.run(debug=True)