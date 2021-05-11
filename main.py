from flask import Flask, render_template, request


app = Flask(__name__, template_folder='view', static_folder='view')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def post():
    data = request.form
    print(data) #convert data, then do regex to get ingredients into a list
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)