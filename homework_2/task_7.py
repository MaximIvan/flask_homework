'''
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
'''


from flask import Flask, render_template, request


app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form_square.html')

@app.post('/')
def index_post():
    num = float(request.form.get('num'))
    square = num**2

    return render_template('form_square.html', num=num, square=square)


if __name__ == '__main__':
    app.run(debug=True)