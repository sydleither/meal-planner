from flask import Flask, render_template, request
from controller.input_controller import parse_data


app = Flask(__name__, template_folder='view', static_folder='view')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/confirm', methods=['GET', 'POST'])
def add_recipe():
    data = request.form
    name, ingredients, instructions = parse_data(data)
    return render_template('confirm.html', name=name, ingredients=ingredients, instructions=instructions)


@app.route('/', methods=['GET', 'POST'])
def confirm_recipe():
    data = request.form
    print(data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)