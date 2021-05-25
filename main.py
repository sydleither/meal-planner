from flask import Flask, render_template, request
from controller.input_controller import parse_data
from controller.view_to_model import submit_data


app = Flask(__name__, template_folder='view', static_folder='view')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/confirm', methods=['GET', 'POST'])
def add_recipe():
    data = request.form
    name, ingredients, instructions, meal_type, subtype, servings = parse_data(data)
    return render_template('confirm.html', name=name, ingredients=ingredients, \
                           instructions=instructions, meal_type=meal_type, \
                            subtype=subtype, servings=servings)


@app.route('/', methods=['GET', 'POST'])
def confirm_recipe():
    data = request.form
    submit_data(data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)