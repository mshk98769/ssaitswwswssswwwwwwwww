from flask import Flask, render_template, request

appweb = Flask(__name__)



@appweb.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return f'ваше имя {name} а возраст {age}'
    return render_template('main.html')


@appweb.route('/регистрация', methods=['GET', 'POST'])
def registration():


    return render_template('index.html')


if __name__ == '__main__':
    appweb.run(debug=True)