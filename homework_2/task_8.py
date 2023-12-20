'''
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
'''


from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

app.secret_key = '0a0cd78f393fe8a47d3cf11df28ba1a6035a4dc48c892507ea6c6289919bcf51'

@app.route('/flashh/', methods=['GET', 'POST'])
def flashh():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name.capitalize()}!', 'success')
        return redirect(url_for('flashh'))
    return render_template('flashh.html')

if __name__ == '__main__':
    app.run(debug=True)