'''
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
'''


from flask import Flask, render_template, request


app = Flask(__name__)


@app.get('/')
def index():
    return render_template('age.html')

@app.post('/')
def index_post():
    name = request.form.get('name')
    age = int(request.form.get('age'))

    if 100 > age > 0:
        result = f'Привет, я {name.capitalize()}, мне {age} лет'
    else:
        result = f'Ошибка, попробуйте еще раз'


    return render_template('age.html', result=result, name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)